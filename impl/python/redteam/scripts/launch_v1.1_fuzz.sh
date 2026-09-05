#!/usr/bin/env bash
# Launch the v1.1 charter fuzz re-run.
# Preserves v1.0 results by moving them to results-v1.0-2026-08-31/,
# then starts the 24-hour coordinator in the background.
#
# Usage:
#   cd ~/clawd/Sarasvati/impl/python/redteam
#   bash scripts/launch_v1.1_fuzz.sh
#
# After launch:
#   - tail -f results/coordinator.log
#   - watch batch commits: (cd ~/clawd/Sarasvati && git log --oneline)
#   - v1.1 final report will be at results/final-report.md at ~24h + 5min

set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

RESULTS="$ROOT/results"
ARCHIVE="$ROOT/results-v1.0-2026-08-31"

if [ -d "$ARCHIVE" ]; then
  echo "❌ Archive dir already exists: $ARCHIVE"
  echo "   Refusing to overwrite. Move it aside or delete it first."
  exit 1
fi

if [ -f "$RESULTS/coordinator.pid" ]; then
  PID=$(cat "$RESULTS/coordinator.pid" 2>/dev/null || echo "")
  if [ -n "$PID" ] && kill -0 "$PID" 2>/dev/null; then
    echo "❌ Coordinator already running (PID $PID). Kill it first:"
    echo "   bash scripts/stop_now.sh"
    exit 1
  fi
fi

echo "→ Archiving v1.0 results to results-v1.0-2026-08-31/"
mv "$RESULTS" "$ARCHIVE"
mkdir -p "$RESULTS"

# Preserve the .gitignore behavior for the new results dir
if [ -f "$ARCHIVE/.gitignore" ]; then
  cp "$ARCHIVE/.gitignore" "$RESULTS/.gitignore"
fi

echo "→ Starting v1.1 fuzz coordinator in background"
nohup python3 -u coordinator.py > "$RESULTS/coordinator.log" 2>&1 &
COORD_PID=$!
disown

sleep 2
if kill -0 "$COORD_PID" 2>/dev/null; then
  echo "✅ Coordinator started (PID $COORD_PID)"
  echo "   Log: $RESULTS/coordinator.log"
  echo "   Expected finish: $(date -v+24H '+%Y-%m-%d %H:%M %Z')"
  echo ""
  echo "→ Suggested cron for watchdog (every 2h):"
  echo "   0 */2 * * * $ROOT/scripts/watchdog.sh"
else
  echo "❌ Coordinator failed to start. Check $RESULTS/coordinator.log"
  exit 1
fi
