#!/usr/bin/env bash
# Sarasvatī community feedback poller.
# Combines Cores B (GitHub feedback) + D (PyPI/Guardrail usage).
# Emits a short markdown report on stdout. Only surfaces meaningful signals.

set -euo pipefail

REPO_OWNER="lurongpan47"
REPO_NAME="Sarasvati"
STATE_FILE="/Users/lucy/clawd/Sarasvati/scripts/.feedback_state.json"
PKG_NAME="buddhist-ai-guardrail"

previous() {
  if [[ -f "$STATE_FILE" ]]; then
    jq -r ".${1} // 0" "$STATE_FILE"
  else
    echo 0
  fi
}

save_state() {
  cat > "$STATE_FILE" <<JSON
{
  "stars": $stars,
  "forks": $forks,
  "open_issues": $open_issues,
  "open_prs": $open_prs,
  "watchers": $watchers,
  "pypi_downloads_last_month": $pypi_dl,
  "timestamp": "$(date -u +%FT%TZ)"
}
JSON
}

# --- GitHub repo stats (Core B) ---
repo_json=$(gh api "repos/$REPO_OWNER/$REPO_NAME" 2>/dev/null || echo "{}")
stars=$(echo "$repo_json" | jq -r '.stargazers_count // 0')
forks=$(echo "$repo_json" | jq -r '.forks_count // 0')
watchers=$(echo "$repo_json" | jq -r '.subscribers_count // 0')
open_issues=$(echo "$repo_json" | jq -r '.open_issues_count // 0')
open_prs=$(gh pr list --repo "$REPO_OWNER/$REPO_NAME" --state open --json number 2>/dev/null | jq 'length' || echo 0)

# --- New activity in last 24h ---
since=$(date -u -v-24H +%FT%TZ 2>/dev/null || date -u -d '24 hours ago' +%FT%TZ)
new_issues=$(gh api "repos/$REPO_OWNER/$REPO_NAME/issues?state=all&since=$since&per_page=100" 2>/dev/null \
  | jq '[.[] | select(.pull_request == null)] | length' || echo 0)
new_prs=$(gh api "repos/$REPO_OWNER/$REPO_NAME/pulls?state=all&sort=created&direction=desc&per_page=20" 2>/dev/null \
  | jq --arg s "$since" '[.[] | select(.created_at >= $s)] | length' || echo 0)

# --- PyPI stats (Core D) — skip cleanly if not published ---
pypi_dl=0
pypi_published="no"
if pypi_json=$(curl -sfL "https://pypi.org/pypi/$PKG_NAME/json" 2>/dev/null); then
  pypi_published="yes"
  # pypistats API for downloads
  if dl_json=$(curl -sfL "https://pypistats.org/api/packages/$PKG_NAME/recent" 2>/dev/null); then
    pypi_dl=$(echo "$dl_json" | jq -r '.data.last_month // 0')
  fi
fi

# --- Deltas vs previous run ---
prev_stars=$(previous stars)
prev_forks=$(previous forks)
prev_dl=$(previous pypi_downloads_last_month)
d_stars=$((stars - prev_stars))
d_forks=$((forks - prev_forks))
d_dl=$((pypi_dl - prev_dl))

# --- Report ---
have_signal=0
report="📊 **Sarasvatī Community Feedback**

⭐ Stars: $stars"
[[ $d_stars -gt 0 ]] && { report="$report (+$d_stars)"; have_signal=1; }
report="$report
🍴 Forks: $forks"
[[ $d_forks -gt 0 ]] && { report="$report (+$d_forks)"; have_signal=1; }
report="$report
👀 Watchers: $watchers
🐛 Open issues: $open_issues"
[[ $new_issues -gt 0 ]] && { report="$report ($new_issues new in 24h)"; have_signal=1; }
report="$report
🔀 Open PRs: $open_prs"
[[ $new_prs -gt 0 ]] && { report="$report ($new_prs new in 24h)"; have_signal=1; }

if [[ "$pypi_published" == "yes" ]]; then
  report="$report
📦 PyPI $PKG_NAME: last-month downloads $pypi_dl"
  [[ $d_dl -gt 0 ]] && { report="$report (+$d_dl vs prev poll)"; have_signal=1; }
else
  report="$report
📦 PyPI: $PKG_NAME not yet published (skipping downloads)"
fi

save_state

if [[ $have_signal -eq 0 ]]; then
  # Quiet day — say so tersely.
  echo "$report

_no new activity_"
else
  echo "$report"
fi
