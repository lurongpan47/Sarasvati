#!/usr/bin/env python3
"""Cheap ping to verify each of the 7 providers responds. Exit 0 always.

Usage:
    python3 scripts/ping_all_models.py
"""

from __future__ import annotations
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

from providers import build_all  # noqa: E402


def main() -> int:
    clients = build_all()
    print(f"Pinging {len(clients)} providers...\n")
    results = []
    total_cost = 0.0
    for c in clients:
        t0 = time.time()
        ok = c.ping()
        dt = round(time.time() - t0, 2)
        status = "OK " if ok else "FAIL"
        model = f"{c.name:<9} ({c.model_id})"
        err = "" if ok else f"  err={c.last_error}"
        print(f"  [{status}] {model:<50}  {dt}s{err}")
        results.append({
            "name": c.name, "model": c.model_id, "available": ok,
            "latency_s": dt, "error": c.last_error,
        })
    out_dir = HERE.parent / "results"
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "ping-latest.json", "w") as f:
        json.dump({"ts": int(time.time()), "results": results}, f, indent=2)
    up = sum(1 for r in results if r["available"])
    print(f"\n{up}/{len(results)} providers up.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
