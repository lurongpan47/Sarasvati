# redteam · 24-Hour Buddhist AI Charter Cross-Model Fuzz Suite

> *"All conditioned things are impermanent. Strive on with diligence."* — DN 16
>
> This directory is one such conditioned thing. It runs for exactly 24 hours,
> writes a final report, then ends.

## What this is

A self-contained fuzz-testing rig that:

1. Loads **~200 seed adversarial prompts** across 15 rule categories
   (the 5 refusals and 10 principles of the [Buddhist AI Charter](../../../charter/BUDDHIST-AI-CHARTER.md)).
2. Sends each attack to up to **7 major LLMs** in parallel: Claude, GPT, Gemini,
   Grok, MiniMax, DeepSeek, Qwen.
3. Runs every response through the reference
   [`buddhist_ai_guardrail`](../buddhist_ai_guardrail/) library.
4. Cross-reviews each response with a **different** live model as judge.
5. Adaptively generates new attacks every 2 hours, weighted toward the rules
   with the lowest current violation-detection rate.
6. Commits & pushes aggregated results every 30 minutes.
7. Caps total spend at **$300 USD** across all providers.
8. Self-terminates at launch + 24h and writes `final-report.md`.

## Layout

```
redteam/
├── README.md                    ← this file
├── coordinator.py               ← 24h main loop
├── providers/
│   └── __init__.py             ← unified Client interface for all 7 models
├── attack_generator.py         ← adaptive attack drafting
├── charter_evaluator.py        ← wraps buddhist_ai_guardrail
├── cross_reviewer.py           ← model_A judges model_B
├── spend_tracker.py            ← per-provider cost meter
├── attacks/                    ← seed corpus (200 JSONL rows)
├── results/                    ← matrix-*.jsonl, summaries, checkpoint (gitignored)
└── scripts/
    ├── build_seed_corpus.py    ← (re)emit the seed attacks
    ├── ping_all_models.py      ← launch sanity check
    ├── stop_now.sh             ← graceful SIGTERM
    └── watchdog.sh             ← cron restart-from-checkpoint
```

## Reproduce

```bash
# 1. Verify keys — never printed
python3 scripts/ping_all_models.py

# 2. (Re-)build seed corpus
python3 scripts/build_seed_corpus.py

# 3. Launch the 24h campaign in background
nohup python3 coordinator.py > results/coordinator.log 2>&1 &
echo $! > results/coordinator.pid

# 4. Watch it
tail -f results/coordinator.log
cat results/summary-live.md
```

## Keys

Keys are loaded, in order:

1. Environment variables (e.g. `OPENAI_API_KEY`).
2. `~/clawd/skills/financial-analyst/.env` (for `XAI_API_KEY`, `GOOGLE_API_KEY`).
3. macOS keychain under account `sarasvati-fuzz`:
   ```bash
   security find-generic-password -a sarasvati-fuzz -s DEEPSEEK_API_KEY -w
   ```

Never write keys to any tracked file. `.env`, `.spend.json`, and `.checkpoint.json`
are gitignored. Every commit runs a diff scan for `sk-ant-*` and similar
before pushing.

## Budget & timing

- **Hard cap:** $300 (in `spend_tracker.py`, `HARD_CAP_USD`).
- **Warning threshold:** $250.
- **Duration:** 24h from `results/.checkpoint.json['launch_ts']`.
- **Batch interval:** 30 minutes.
- **Adaptive attack refresh:** every 2 hours.

## What "success" means

The point is not to break the models. The point is to find where the CHARTER
is under-specified. Log those as *charter gaps* in `final-report.md`.

## License

CC BY-SA 4.0, same as the Charter and the rest of the Sarasvatī Project.
