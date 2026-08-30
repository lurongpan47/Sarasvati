#!/usr/bin/env bash
# Gracefully stop the coordinator (SIGTERM). Coordinator writes final report
# and exits 0.
set -e
PID_FILE="$(cd "$(dirname "$0")/.." && pwd)/results/coordinator.pid"
if [ -f "$PID_FILE" ]; then
  PID=$(cat "$PID_FILE")
  if kill -0 "$PID" 2>/dev/null; then
    echo "Sending SIGTERM to coordinator PID $PID"
    kill "$PID"
    echo "Sent."
  else
    echo "No live process at PID $PID."
  fi
else
  echo "No PID file at $PID_FILE."
fi
