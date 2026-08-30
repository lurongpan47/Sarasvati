#!/usr/bin/env bash
# Sarasvatī · Timeline evidence scan.
# Runs a lightweight probe against known open-canon-archive news sources and
# writes a candidate list to /tmp/sarasvati_timeline_candidates.md.
# The cron job reads this and, if candidates > 0, invokes the LLM to draft
# ROADMAP/events.jsonl deltas for Lucy to approve.
#
# This shell script only *collects*. It does not write to the repo.

set -euo pipefail

OUT="/tmp/sarasvati_timeline_candidates.md"
STATE="/Users/lucy/clawd/Sarasvati/scripts/.timeline_scan_state.json"
: > "$OUT"

# Sources known to publish news about newly digitized / edited Buddhist canons.
# Kept small and public: RSS/atom feeds and static pages we can hit without auth.
SOURCES=(
  "https://84000.co/feed/"
  "https://suttacentral.net/rss.xml"
  "https://www.tbrc.org/rss/rss.xml"
  "https://gretil.sub.uni-goettingen.de/gretil.htm"
  "https://cbetaonline.dila.edu.tw/"
  "https://idp.bl.uk/news.a4d"
)

echo "# Timeline evidence scan · $(date -u +%FT%TZ)" >> "$OUT"
echo "" >> "$OUT"

for src in "${SOURCES[@]}"; do
  echo "## $src" >> "$OUT"
  # 12s timeout so a slow/dead source can't jam the run.
  if body=$(curl -sfL --max-time 12 "$src" 2>/dev/null); then
    # Titles + dates from RSS/HTML; grep is fine — this is a heuristic pass.
    hits=$(echo "$body" \
      | grep -oiE '<title[^>]*>[^<]{5,220}</title>|<h[1-3][^>]*>[^<]{5,220}</h[1-3]>' \
      | head -8 \
      | sed 's/<[^>]*>//g' \
      | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    if [[ -n "$hits" ]]; then
      echo "$hits" | while read -r line; do
        [[ -n "$line" ]] && echo "- $line" >> "$OUT"
      done
    else
      echo "_(no titles found — page may be pure prose)_" >> "$OUT"
    fi
  else
    echo "_(fetch failed — source offline or slow)_" >> "$OUT"
  fi
  echo "" >> "$OUT"
done

# Persist a shallow scan record.
cat > "$STATE" <<JSON
{
  "last_scan": "$(date -u +%FT%TZ)",
  "sources_probed": ${#SOURCES[@]},
  "output": "$OUT"
}
JSON

# Emit path so the cron can find the report.
echo "REPORT=$OUT"
