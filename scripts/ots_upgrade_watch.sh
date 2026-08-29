#!/usr/bin/env bash
# Sarasvatī OTS upgrade watcher.
# Checks if manifests/SHA256SUMS.ots has been Bitcoin-confirmed yet.
# If yes: commits the upgraded proof, pushes, and writes a marker file
#         that the cron reader uses to auto-disable this job.
# If no:  exits cleanly.
#
# Meant to be called by cron. Idempotent.

set -euo pipefail

OTS_BIN="/Users/lucy/Library/Python/3.13/bin/ots"
REPO="/Users/lucy/clawd/Sarasvati"
STAMP="$REPO/manifests/SHA256SUMS.ots"
MARKER="$REPO/manifests/.ots_confirmed"

cd "$REPO"

if [[ -f "$MARKER" ]]; then
  echo "OTS already confirmed and committed (marker exists). Nothing to do."
  exit 0
fi

if [[ ! -f "$STAMP" ]]; then
  echo "ERROR: no stamp at $STAMP" >&2
  exit 2
fi

# Try to upgrade the stamp.
BEFORE_HASH=$(shasum -a 256 "$STAMP" | awk '{print $1}')
echo "== OTS upgrade attempt =="
"$OTS_BIN" upgrade "$STAMP" 2>&1 || true
AFTER_HASH=$(shasum -a 256 "$STAMP" | awk '{print $1}')

# Verify. `ots verify` prints a Bitcoin block height if fully confirmed.
VERIFY_OUT=$("$OTS_BIN" verify "$STAMP" 2>&1 || true)
echo "$VERIFY_OUT"

if echo "$VERIFY_OUT" | grep -qiE "block ([0-9]+)"; then
  echo "== Bitcoin-confirmed! =="
  BLOCK=$(echo "$VERIFY_OUT" | grep -oiE "block [0-9]+" | head -1 | awk '{print $2}')

  if [[ "$BEFORE_HASH" != "$AFTER_HASH" ]]; then
    git add manifests/SHA256SUMS.ots
    git commit -m "chore(ots): upgrade Bitcoin timestamp — confirmed at block $BLOCK

manifests/SHA256SUMS.ots is now fully Bitcoin-anchored, no longer
depending on OpenTimestamps calendar servers. Any verifier with a
Bitcoin node can independently confirm the manifest hash existed
at or before block $BLOCK."
    git push origin main
  fi

  echo "$BLOCK" > "$MARKER"
  echo "Wrote marker $MARKER (cron self-disable)."
else
  echo "Still pending calendar confirmations. Try again later."
fi
