#!/usr/bin/env bash
# Watchdog: check the coordinator is alive; if not (and 24h window still open),
# restart it from checkpoint. Intended for a cron job every 2 hours.
#
# Idempotent: safe to run whether coordinator is already up or down.
set -u

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RESULTS="$ROOT/results"
PID_FILE="$RESULTS/coordinator.pid"
LOG="$RESULTS/coordinator.log"
CHECKPOINT="$RESULTS/.checkpoint.json"

# Are we still within the 24h window?
if [ -f "$CHECKPOINT" ]; then
  LAUNCH=$(python3 -c "import json,sys; print(json.load(open('$CHECKPOINT'))['launch_ts'])" 2>/dev/null || echo 0)
  NOW=$(date +%s)
  ELAPSED=$((NOW - LAUNCH))
  if [ "$ELAPSED" -ge $((24*3600)) ]; then
    echo "$(date -u +%FT%TZ) watchdog: 24h window already closed; no restart" >> "$LOG"
    exit 0
  fi
else
  echo "$(date -u +%FT%TZ) watchdog: no checkpoint; not restarting" >> "$LOG"
  exit 0
fi

# Is the coordinator alive?
if [ -f "$PID_FILE" ]; then
  PID=$(cat "$PID_FILE")
  if kill -0 "$PID" 2>/dev/null; then
    echo "$(date -u +%FT%TZ) watchdog: coordinator PID $PID alive" >> "$LOG"
    exit 0
  fi
fi

echo "$(date -u +%FT%TZ) watchdog: coordinator DOWN — restarting from checkpoint" >> "$LOG"
cd "$ROOT"
nohup python3 coordinator.py >> "$LOG" 2>&1 &
NEW_PID=$!
echo "$NEW_PID" > "$PID_FILE"
echo "$(date -u +%FT%TZ) watchdog: relaunched PID $NEW_PID" >> "$LOG"
exit 0
