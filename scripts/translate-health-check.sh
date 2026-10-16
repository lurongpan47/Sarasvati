#!/usr/bin/env bash
# Sarasvatī weekly health check for the embedded DeerPress.ai /free translator.
#
# What it tests:
#   1. /free HTTP 200
#   2. iframe CSP allows lurongpan47.github.io
#   3. API accepts POST, returns valid JSON
#   4. Tibetan → English round-trip returns non-empty, non-error text
#
# Writes:  ~/clawd/Sarasvati/manifests/translate-health.json
# Commits: once per week via cron (see docs below)

set -u  # don't -e, we want to collect all errors

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MANIFEST="$ROOT/manifests/translate-health.json"
UPSTREAM="https://deerpress.ai"
TEST_TEXT='དེ་བཞིན་གཤེགས་པ་ལ་ཕྱག་འཚལ་ལོ།'   # "Homage to the Tathāgata."
TEST_TARGET="English"
EMBED_ORIGIN="https://lurongpan47.github.io"
UA="Sarasvati-health-check/1.0 (+https://lurongpan47.github.io/Sarasvati/translate/)"

status="ok"
notes=()
checks_json=()

now_iso() { date -u +"%Y-%m-%dT%H:%M:%SZ"; }

add_check() {
  # args: name, status, detail
  local name="$1" st="$2" detail="$3"
  checks_json+=("$(printf '{"name":"%s","status":"%s","detail":%s}' \
    "$name" "$st" "$(printf '%s' "$detail" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))')" )")
  if [ "$st" != "pass" ]; then status="degraded"; fi
}

# ---------- 1. /free is up ----------
http=$(curl -sS -o /tmp/.free.body -w "%{http_code}" --max-time 20 -A "$UA" "$UPSTREAM/free") || http=000
if [ "$http" = "200" ]; then
  add_check "page_http" "pass" "HTTP 200"
else
  add_check "page_http" "fail" "HTTP $http"
  notes+=("Page did not return 200")
fi

# ---------- 2. CSP allows github.io ----------
csp=$(curl -sS -I --max-time 20 -A "$UA" "$UPSTREAM/free" | grep -i "content-security-policy" || true)
if printf '%s' "$csp" | grep -q "lurongpan47.github.io\|\*\.github\.io"; then
  add_check "iframe_csp" "pass" "frame-ancestors allows github.io"
else
  add_check "iframe_csp" "fail" "CSP missing github.io origin: $csp"
  notes+=("iframe will be blocked for Sarasvatī readers")
fi

# ---------- 3. API round-trip ----------
api_body=$(printf '{"text":%s,"target_language":"%s"}' \
  "$(printf '%s' "$TEST_TEXT" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))')" \
  "$TEST_TARGET")

# The /free widget calls its own Flask app at /free/translate-text (nginx strips /free and
# proxies to the Flask app on :5000, which exposes /translate-text).
api_resp=$(curl -sS --max-time 120 -A "$UA" \
  -X POST "$UPSTREAM/free/translate-text" \
  -H "Content-Type: application/json" \
  -d "$api_body" || true)

if printf '%s' "$api_resp" | python3 -c 'import json,sys; d=json.loads(sys.stdin.read()); assert d.get("translation") or d.get("translations")' 2>/dev/null; then
  translated=$(printf '%s' "$api_resp" | python3 -c 'import json,sys; d=json.loads(sys.stdin.read()); print(d.get("translation") or next(iter((d.get("translations") or {}).values()), ""))' 2>/dev/null)
  if [ -n "$translated" ] && [ "$translated" != "$TEST_TEXT" ]; then
    # Buddhist terminology sanity
    if printf '%s' "$translated" | grep -qiE "tathagata|tathāgata|homage|buddha"; then
      add_check "api_translation" "pass" "Returned: $(printf '%s' "$translated" | head -c 120)"
    else
      add_check "api_translation" "warn" "Returned text but no Buddhist term match: $(printf '%s' "$translated" | head -c 120)"
      notes+=("Translation returned but terminology mismatch — model may have drifted")
    fi
  else
    add_check "api_translation" "fail" "Empty or echoed source: $(printf '%s' "$translated" | head -c 120)"
    notes+=("Translation returned source unchanged")
  fi
else
  add_check "api_translation" "fail" "Non-JSON or error response: $(printf '%s' "$api_resp" | head -c 400)"
  notes+=("API did not return valid translation JSON")
fi

# ---------- 4. Write manifest ----------
mkdir -p "$(dirname "$MANIFEST")"

checks_body="[$(IFS=,; printf '%s' "${checks_json[*]}")]"
if [ ${#notes[@]} -eq 0 ]; then
  notes_body="[]"
else
  notes_body="[$(for n in "${notes[@]}"; do printf '%s' "$n" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read()))'; echo ","; done | sed 's/,$//' | tr -d '\n' | sed 's/,$//')]"
fi

python3 - "$MANIFEST" "$status" "$(now_iso)" "$UPSTREAM" "$checks_body" "$notes_body" << 'PY'
import json, sys
path, status, ts, upstream, checks_s, notes_s = sys.argv[1:7]
out = {
  "schema": "sarasvati.translate-health.v1",
  "checked_at": ts,
  "upstream": upstream,
  "status": status,
  "checks": json.loads(checks_s),
  "notes": json.loads(notes_s) if notes_s.strip() != "[]" else [],
}
with open(path, "w") as f:
  json.dump(out, f, indent=2, ensure_ascii=False)
  f.write("\n")
print(json.dumps({"wrote": path, "status": status}))
PY

echo "[translate-health] status=$status  manifest=$MANIFEST"

# Exit code: 0 on ok, 2 on degraded (so cron can detect)
[ "$status" = "ok" ] && exit 0 || exit 2
