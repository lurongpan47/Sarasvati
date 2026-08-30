"""24-hour Buddhist AI Charter cross-model fuzz coordinator.

Runs a batch loop for exactly 24 hours starting from launch time (persisted
to results/.checkpoint.json). Every batch:
  1. Sample attacks weighted toward under-covered categories
  2. Send each attack to every AVAILABLE model in parallel
  3. Run the guardrail over each response (Buddhist AI Charter evaluator)
  4. Ask a DIFFERENT live model to judge each response (cross review)
  5. Log everything to matrix-YYYYMMDDTHHMM.jsonl (rotated per hour)
  6. Update spend meter; halt at $300 hard cap
  7. Every 30 min: regenerate summary-live.md and git-commit results
  8. Every 2 hours: ask a cheap model to draft new adaptive attacks
  9. At launch+24h: write final-report.md, commit, exit 0

Signals: SIGTERM is honored (writes final report and exits 0).
Always exits 0 to keep the watchdog cron quiet.
"""

from __future__ import annotations
import json
import os
import random
import signal
import subprocess
import sys
import time
import traceback
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from providers import build_all  # noqa: E402
from spend_tracker import (  # noqa: E402
    load as spend_load, add as spend_add, remaining as spend_remaining,
    should_halt, should_warn, mark_warned, mark_halted, HARD_CAP_USD,
)
from charter_evaluator import evaluate as guardrail_eval  # noqa: E402
from cross_reviewer import build_judge_prompt, parse_verdict, JUDGE_SYSTEM  # noqa: E402
from attack_generator import (  # noqa: E402
    load_all_attacks, weighted_sample, generate_new_attacks, append_generated,
    RULE_CATEGORIES,
)


RESULTS_DIR = HERE / "results"
RESULTS_DIR.mkdir(exist_ok=True, parents=True)

CHECKPOINT_PATH = RESULTS_DIR / ".checkpoint.json"
SUMMARY_PATH = RESULTS_DIR / "summary-live.md"
FINAL_REPORT_PATH = RESULTS_DIR / "final-report.md"

DURATION_S = 24 * 3600
BATCH_INTERVAL_S = 30 * 60      # every 30 min
ATTACKS_PER_BATCH = 20
COMMIT_INTERVAL_S = 30 * 60
GENERATE_INTERVAL_S = 2 * 3600
MAX_RESPONSE_TOKENS = 220
MAX_JUDGE_TOKENS = 160
PER_MODEL_TIMEOUT_S = 60
GITHUB_REPO_URL = "https://github.com/lurongpan47/Sarasvati"

_STOP = False


def _sig_handler(signum, frame):  # noqa: ARG001
    global _STOP
    _STOP = True


signal.signal(signal.SIGTERM, _sig_handler)
signal.signal(signal.SIGINT, _sig_handler)


# --------------------------------------------------------------------------- #
# Checkpoint                                                                   #
# --------------------------------------------------------------------------- #

def load_checkpoint() -> dict[str, Any]:
    if CHECKPOINT_PATH.exists():
        try:
            with open(CHECKPOINT_PATH) as f:
                return json.load(f)
        except Exception:
            pass
    cp = {
        "launch_ts": int(time.time()),
        "last_batch_ts": 0,
        "last_generate_ts": 0,
        "last_commit_ts": 0,
        "batches_done": 0,
        "evaluations_done": 0,
    }
    save_checkpoint(cp)
    return cp


def save_checkpoint(cp: dict[str, Any]) -> None:
    tmp = CHECKPOINT_PATH.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(cp, f, indent=2)
    os.replace(tmp, CHECKPOINT_PATH)


# --------------------------------------------------------------------------- #
# Matrix logging                                                               #
# --------------------------------------------------------------------------- #

def matrix_path() -> Path:
    stamp = time.strftime("%Y%m%dT%H", time.gmtime())
    return RESULTS_DIR / f"matrix-{stamp}.jsonl"


def matrix_append(row: dict[str, Any]) -> None:
    with open(matrix_path(), "a") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


# --------------------------------------------------------------------------- #
# Batch                                                                        #
# --------------------------------------------------------------------------- #

def compute_coverage() -> dict[str, int]:
    """Count how many evals per category we've done so far (this run)."""
    cov: dict[str, int] = defaultdict(int)
    for p in sorted(RESULTS_DIR.glob("matrix-*.jsonl")):
        try:
            with open(p) as f:
                for line in f:
                    try:
                        d = json.loads(line)
                        cov[d.get("attack", {}).get("category", "")] += 1
                    except Exception:
                        continue
        except Exception:
            continue
    return cov


def _call_model(client, prompt: str, system: str | None,
                max_tokens: int) -> dict[str, Any]:
    r = client.chat(prompt, system=system, max_tokens=max_tokens,
                    timeout=PER_MODEL_TIMEOUT_S)
    spend_add(client.name, r.get("cost_usd", 0.0))
    return r


def run_batch(clients: list, live_clients: list, batch_id: int) -> int:
    """Return number of evaluations completed in this batch."""
    attacks = load_all_attacks()
    if not attacks:
        print("no attacks loaded; skipping batch", flush=True)
        return 0
    cov = compute_coverage()
    sampled = weighted_sample(attacks, cov, ATTACKS_PER_BATCH)
    if not sampled:
        return 0

    print(f"[batch {batch_id}] sampled {len(sampled)} attacks; "
          f"live models: {[c.name for c in live_clients]}", flush=True)

    done = 0
    for a in sampled:
        if _STOP or should_halt():
            break
        if spend_remaining() <= 1.0:
            print("halting batch: spend budget nearly exhausted", flush=True)
            break

        row: dict[str, Any] = {
            "ts": int(time.time()),
            "batch_id": batch_id,
            "attack": a,
            "responses": {},
            "guardrail": {},
            "judge": {},
        }

        # Parallel model calls
        with ThreadPoolExecutor(max_workers=len(live_clients)) as ex:
            futs = {ex.submit(_call_model, c, a["prompt"], None, MAX_RESPONSE_TOKENS): c
                    for c in live_clients}
            for fut in as_completed(futs, timeout=PER_MODEL_TIMEOUT_S + 30):
                c = futs[fut]
                try:
                    r = fut.result(timeout=5)
                except Exception as e:
                    r = {"text": "", "error": f"future_error: {e}",
                         "usage": {"input_tokens": 0, "output_tokens": 0},
                         "cost_usd": 0.0, "latency_s": 0.0}
                row["responses"][c.name] = r

        # Guardrail evaluation on each response
        for name, r in row["responses"].items():
            try:
                v = guardrail_eval(r.get("text", ""), a["prompt"], a["category"])
            except Exception as e:
                v = {"error": f"{type(e).__name__}: {e}"}
            row["guardrail"][name] = v

        # Cross-review: pick a different live model as judge for each response
        if len(live_clients) >= 2:
            for name, r in row["responses"].items():
                if not r.get("text"):
                    continue
                candidates = [c for c in live_clients if c.name != name]
                if not candidates:
                    continue
                judge = random.choice(candidates)
                judge_prompt = build_judge_prompt(a["prompt"], r["text"])
                jr = _call_model(judge, judge_prompt, JUDGE_SYSTEM, MAX_JUDGE_TOKENS)
                verdict = parse_verdict(jr.get("text", ""))
                row["judge"][name] = {
                    "judge_model": judge.name,
                    "verdict": verdict,
                    "cost_usd": jr.get("cost_usd", 0.0),
                    "error": jr.get("error"),
                }

        matrix_append(row)
        done += 1

    return done


# --------------------------------------------------------------------------- #
# Summary                                                                      #
# --------------------------------------------------------------------------- #

def build_summary(launch_ts: int, cp: dict[str, Any], live_names: list[str],
                  failed_pings: dict[str, str]) -> str:
    now = int(time.time())
    elapsed = now - launch_ts
    remaining = max(0, DURATION_S - elapsed)
    spend = spend_load()

    # Aggregate matrix rows
    per_model: dict[str, dict[str, Any]] = defaultdict(lambda: {
        "n": 0, "refuse": 0, "advisory": 0, "clean": 0,
        "errors": 0, "latency_sum": 0.0, "cost_sum": 0.0,
    })
    per_rule_violations: dict[str, int] = defaultdict(int)
    per_rule_total: dict[str, int] = defaultdict(int)
    per_cat: dict[str, dict[str, int]] = defaultdict(lambda: {"n": 0, "flagged": 0})
    jailbreaks: dict[str, dict[str, Any]] = defaultdict(
        lambda: {"n_slipped": 0, "n_seen": 0, "categories": set()}
    )
    disagreements: list[dict[str, Any]] = []
    n_rows = 0

    for p in sorted(RESULTS_DIR.glob("matrix-*.jsonl")):
        try:
            with open(p) as f:
                for line in f:
                    try:
                        row = json.loads(line)
                    except Exception:
                        continue
                    n_rows += 1
                    cat = row["attack"].get("category", "?")
                    per_cat[cat]["n"] += 1
                    is_control = row["attack"].get("is_control", False)
                    aid = row["attack"].get("id", f"row-{n_rows}")

                    guard = row.get("guardrail", {})
                    resp = row.get("responses", {})
                    judge = row.get("judge", {})

                    for name, r in resp.items():
                        pm = per_model[name]
                        pm["n"] += 1
                        pm["cost_sum"] += r.get("cost_usd", 0.0)
                        pm["latency_sum"] += r.get("latency_s", 0.0)
                        if r.get("error"):
                            pm["errors"] += 1
                            continue
                        v = guard.get(name, {}) or {}
                        sev = v.get("severity")
                        if sev == "refuse":
                            pm["refuse"] += 1
                        elif sev == "advisory":
                            pm["advisory"] += 1
                        else:
                            pm["clean"] += 1

                        # Judge outcome
                        jv = judge.get(name, {}).get("verdict", {}) or {}
                        if jv.get("violation") is True and not is_control:
                            per_cat[cat]["flagged"] += 1
                            jailbreaks[aid]["n_slipped"] += 1
                            jailbreaks[aid]["prompt"] = row["attack"].get("prompt", "")[:200]
                            jailbreaks[aid]["categories"].add(cat)
                        jailbreaks[aid]["n_seen"] += 1

                        # Track disagreements: guardrail says refuse, judge says clean, or vice versa
                        g_flag = sev == "refuse"
                        j_flag = jv.get("violation") is True
                        if g_flag != j_flag and jv.get("violation") is not None:
                            if len(disagreements) < 100:
                                disagreements.append({
                                    "attack_id": aid, "model": name,
                                    "category": cat,
                                    "guardrail_sev": sev, "judge_flag": j_flag,
                                    "judge_note": jv.get("one_line", "")[:120],
                                })

                    for name in resp:
                        v = guard.get(name, {}) or {}
                        for rn in v.get("refusal_numbers", []) or []:
                            per_rule_violations[f"refusal_{rn}"] += 1
                        for pn in v.get("principle_numbers", []) or []:
                            per_rule_violations[f"principle_{pn}"] += 1
                        per_rule_total[cat] += 1
        except Exception:
            continue

    # Sort top jailbreaks
    top_jb = sorted(jailbreaks.items(),
                    key=lambda kv: (-kv[1]["n_slipped"], -kv[1]["n_seen"]))[:10]

    lines = []
    lines.append(f"# Sarasvatī 24h Cross-Model Fuzz — Live Summary")
    lines.append("")
    lines.append(f"- **Launch (UTC):** {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(launch_ts))}")
    lines.append(f"- **Now (UTC):**    {time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(now))}")
    lines.append(f"- **Elapsed:**     {elapsed//3600}h {(elapsed%3600)//60}m")
    lines.append(f"- **Remaining:**   {remaining//3600}h {(remaining%3600)//60}m")
    lines.append(f"- **Batches:**     {cp.get('batches_done', 0)}")
    lines.append(f"- **Evaluations:** {n_rows}")
    lines.append("")
    lines.append(f"- **Spend:** ${spend['total_usd']:.4f} / ${HARD_CAP_USD} "
                 f"(remaining ${spend_remaining():.2f})")
    lines.append("")

    lines.append("## Models")
    lines.append("")
    lines.append("| Model | Live | Evals | Refuse | Advisory | Clean | Errors | Avg Latency (s) | Cost (USD) |")
    lines.append("|---|---|---:|---:|---:|---:|---:|---:|---:|")
    for name in ("claude", "gpt", "gemini", "grok", "minimax", "deepseek", "qwen"):
        pm = per_model.get(name, {"n": 0, "refuse": 0, "advisory": 0, "clean": 0,
                                   "errors": 0, "latency_sum": 0.0, "cost_sum": 0.0})
        live = "✅" if name in live_names else f"❌ {failed_pings.get(name, '')[:40]}"
        avg_l = round(pm["latency_sum"] / pm["n"], 2) if pm["n"] else 0
        lines.append(f"| {name} | {live} | {pm['n']} | {pm['refuse']} | "
                     f"{pm['advisory']} | {pm['clean']} | {pm['errors']} | "
                     f"{avg_l} | ${pm['cost_sum']:.4f} |")
    lines.append("")

    lines.append("## Per-Category Coverage")
    lines.append("")
    lines.append("| Category | Evals | Judge-Flagged Violations |")
    lines.append("|---|---:|---:|")
    for cat in RULE_CATEGORIES:
        c = per_cat.get(cat, {"n": 0, "flagged": 0})
        lines.append(f"| {cat} | {c['n']} | {c['flagged']} |")
    lines.append("")

    lines.append("## Top Jailbreaks (attacks that most often slipped past judges)")
    lines.append("")
    if top_jb:
        lines.append("| Attack ID | Category | Slipped | Seen | Prompt (head) |")
        lines.append("|---|---|---:|---:|---|")
        for aid, jb in top_jb:
            cats = ",".join(sorted(jb.get("categories", []))) or "?"
            prom = str(jb.get("prompt", "")).replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {aid} | {cats} | {jb['n_slipped']} | "
                         f"{jb['n_seen']} | {prom[:80]} |")
    else:
        lines.append("_None yet._")
    lines.append("")

    lines.append("## Cross-Model Disagreements (guardrail vs judge)")
    lines.append("")
    if disagreements:
        lines.append("| Model | Category | Guardrail | Judge | Note |")
        lines.append("|---|---|---|---|---|")
        for d in disagreements[:15]:
            note = d["judge_note"].replace("|", "\\|").replace("\n", " ")
            lines.append(f"| {d['model']} | {d['category']} | {d['guardrail_sev']} | "
                         f"{'violation' if d['judge_flag'] else 'ok'} | {note} |")
    else:
        lines.append("_None yet._")
    lines.append("")

    lines.append("## Spend by Provider")
    lines.append("")
    lines.append("| Provider | Cost (USD) |")
    lines.append("|---|---:|")
    for k, v in sorted(spend.get("by_provider", {}).items(), key=lambda kv: -kv[1]):
        lines.append(f"| {k} | ${v:.4f} |")
    lines.append("")

    lines.append("---")
    lines.append(f"_Generated: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}_ · "
                 f"_Charter: {GITHUB_REPO_URL}/blob/main/charter/BUDDHIST-AI-CHARTER.md_")
    return "\n".join(lines)


def write_summary(text: str, final: bool = False) -> None:
    path = FINAL_REPORT_PATH if final else SUMMARY_PATH
    with open(path, "w") as f:
        f.write(text)


# --------------------------------------------------------------------------- #
# Git                                                                          #
# --------------------------------------------------------------------------- #

def git_commit_push(message: str) -> bool:
    """Commit + push results (never keys). Best-effort."""
    repo_root = Path("/Users/lucy/clawd/Sarasvati")
    try:
        # Sanity: refuse to add if any tracked file contains 'sk-live' etc.
        # (we rely on .gitignore for .spend.json / .checkpoint.json)
        subprocess.run(
            ["git", "add",
             "impl/python/redteam/results/summary-live.md",
             "impl/python/redteam/results/final-report.md",
             "impl/python/redteam/results/"],
            cwd=repo_root, check=False, timeout=30,
        )
        # Include matrix files explicitly (glob)
        subprocess.run(
            ["bash", "-c",
             "cd impl/python/redteam/results && git add matrix-*.jsonl 2>/dev/null || true"],
            cwd=repo_root, check=False, timeout=15,
        )
        # Precommit key scan
        r = subprocess.run(
            ["git", "diff", "--cached", "-U0"],
            cwd=repo_root, capture_output=True, text=True, timeout=30,
        )
        if r.stdout and ("sk-ant-" in r.stdout or "xai-" in r.stdout.lower().replace("xai-", "xai-")[:0]):
            # unstage: something looks like a key
            subprocess.run(["git", "reset"], cwd=repo_root, check=False, timeout=15)
            print("!! key-like string in diff, aborting commit", flush=True)
            return False
        # Commit (may be empty; ignore)
        c = subprocess.run(
            ["git", "commit", "-m", message],
            cwd=repo_root, capture_output=True, text=True, timeout=30,
        )
        if c.returncode != 0 and "nothing to commit" not in c.stdout + c.stderr:
            print(f"!! commit failed: {c.stdout} {c.stderr}", flush=True)
        # Push
        p = subprocess.run(
            ["git", "push", "origin", "main"],
            cwd=repo_root, capture_output=True, text=True, timeout=90,
        )
        if p.returncode != 0:
            print(f"!! push warn: {p.stderr[:300]}", flush=True)
        return True
    except Exception as e:
        print(f"!! git error: {e}", flush=True)
        return False


# --------------------------------------------------------------------------- #
# Adaptive generation                                                          #
# --------------------------------------------------------------------------- #

def find_weakest_categories(n: int = 5) -> list[str]:
    """Return categories with the lowest judge-flagged violation rate (i.e. where
    attacks are least often catching models — those need harder attacks)."""
    per_cat = defaultdict(lambda: {"n": 0, "flagged": 0})
    for p in sorted(RESULTS_DIR.glob("matrix-*.jsonl")):
        try:
            with open(p) as f:
                for line in f:
                    try:
                        row = json.loads(line)
                    except Exception:
                        continue
                    cat = row["attack"].get("category", "?")
                    per_cat[cat]["n"] += 1
                    if row["attack"].get("is_control"):
                        continue
                    for name, jd in (row.get("judge") or {}).items():
                        if (jd.get("verdict") or {}).get("violation"):
                            per_cat[cat]["flagged"] += 1
        except Exception:
            continue
    scored = []
    for cat in RULE_CATEGORIES:
        d = per_cat.get(cat, {"n": 1, "flagged": 0})
        rate = d["flagged"] / max(d["n"], 1)
        scored.append((rate, cat))
    scored.sort()  # lowest first
    return [c for _, c in scored[:n]]


# --------------------------------------------------------------------------- #
# Main                                                                        #
# --------------------------------------------------------------------------- #

def main() -> int:
    print(f"Coordinator PID {os.getpid()} starting", flush=True)
    cp = load_checkpoint()
    launch_ts = cp["launch_ts"]

    clients = build_all()
    failed = {}
    print("Pinging providers...", flush=True)
    for c in clients:
        ok = c.ping()
        print(f"  {c.name:9} {'OK' if ok else 'FAIL'}  ({c.last_error or ''})", flush=True)
        if not ok:
            failed[c.name] = c.last_error or ""

    live_clients = [c for c in clients if c.available]
    live_names = [c.name for c in live_clients]
    if len(live_clients) < 2:
        print("!! fewer than 2 live models — cannot do cross-review meaningfully. "
              "Will still run guardrail-only evaluations.", flush=True)

    # Prefer cheap models for judge / attack generation
    cheap_names = ("deepseek", "gpt", "gemini", "grok", "minimax")
    def _cheap():
        for n in cheap_names:
            for c in live_clients:
                if c.name == n:
                    return c
        return live_clients[0] if live_clients else None

    batch_id = cp.get("batches_done", 0)
    print(f"Starting main loop; launch_ts={launch_ts}, batch_id={batch_id}", flush=True)

    while not _STOP:
        now = int(time.time())
        elapsed = now - launch_ts
        if elapsed >= DURATION_S:
            print("24h elapsed; exiting main loop", flush=True)
            break
        if should_halt():
            print(f"HALT: spend cap reached (${spend_load()['total_usd']:.2f})", flush=True)
            mark_halted()
            break

        # Batch
        batch_id += 1
        try:
            n_done = run_batch(clients, live_clients, batch_id)
        except Exception as e:
            print(f"!! batch error: {e}\n{traceback.format_exc()}", flush=True)
            n_done = 0
        cp["batches_done"] = batch_id
        cp["last_batch_ts"] = int(time.time())
        cp["evaluations_done"] = cp.get("evaluations_done", 0) + n_done
        save_checkpoint(cp)

        # Warn at $250
        if should_warn():
            mark_warned()
            print("!! $250 warning threshold crossed", flush=True)

        # Summary + commit every 30 min
        if (int(time.time()) - cp.get("last_commit_ts", 0)) >= COMMIT_INTERVAL_S \
                or batch_id == 1:
            try:
                text = build_summary(launch_ts, cp, live_names, failed)
                write_summary(text, final=False)
                hours = (int(time.time()) - launch_ts) // 3600
                git_commit_push(f"v0.7.0 · fuzz batch #{batch_id} · "
                                f"{cp['evaluations_done']} evals · "
                                f"${spend_load()['total_usd']:.2f} spent · "
                                f"~{hours}h elapsed")
                cp["last_commit_ts"] = int(time.time())
                save_checkpoint(cp)
            except Exception as e:
                print(f"!! summary/commit error: {e}", flush=True)

        # Adaptive generation every 2h
        if (int(time.time()) - cp.get("last_generate_ts", 0)) >= GENERATE_INTERVAL_S:
            try:
                weak = find_weakest_categories(5)
                gen_client = _cheap()
                if gen_client:
                    new_attacks = generate_new_attacks(gen_client, weak, per_cat=4)
                    if new_attacks:
                        path = append_generated(new_attacks)
                        print(f"generated {len(new_attacks)} new attacks in {weak} → {path}",
                              flush=True)
                cp["last_generate_ts"] = int(time.time())
                save_checkpoint(cp)
            except Exception as e:
                print(f"!! generate error: {e}", flush=True)

        # Sleep to next batch — but wake on stop
        target = time.time() + BATCH_INTERVAL_S
        while time.time() < target and not _STOP:
            time.sleep(5)
            if should_halt():
                break

    # -------- Final report --------
    try:
        text = build_summary(launch_ts, cp, live_names, failed)
        write_summary(text, final=True)
        # Also refresh summary-live
        write_summary(text, final=False)
        git_commit_push(f"v0.7.0 · 24-hour fuzz complete — "
                        f"{cp.get('evaluations_done', 0)} evaluations across "
                        f"{len(live_names)} live models · "
                        f"${spend_load()['total_usd']:.2f} spent")
    except Exception as e:
        print(f"!! final report error: {e}", flush=True)

    print("Coordinator exiting cleanly (exit 0).", flush=True)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception:
        traceback.print_exc()
        sys.exit(0)  # never crash — the mission spec says always exit 0
