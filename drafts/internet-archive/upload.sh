#!/usr/bin/env bash
# ==============================================================================
# Sarasvatī v0.9 · Internet Archive uploader
# ------------------------------------------------------------------------------
# Prepared 2026-09-13 by Lucy.
# IA upload flow: Pan reviews metadata → Pan approves Lucy to upload OR runs
# this script himself.
#
# Reads every metadata/<id>.yaml, pushes the listed files to
#   https://archive.org/details/<id>
# using the `ia` CLI (`pip install internetarchive`; then `ia configure`).
#
# DEFAULT is dry-run. Pass --live to actually upload.
# ==============================================================================

set -euo pipefail

# ---------- locate ourselves --------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"   # ~/clawd/Sarasvati
META_DIR="$SCRIPT_DIR/metadata"
BUILD_DIR="$SCRIPT_DIR/build"

# ---------- args --------------------------------------------------------------
LIVE=0
ONLY=""
for arg in "$@"; do
  case "$arg" in
    --live) LIVE=1 ;;
    --only=*) ONLY="${arg#--only=}" ;;
    -h|--help)
      cat <<EOF
Usage: $0 [--live] [--only=<identifier>]

Default: dry-run (echoes the ia commands without executing).
--live         Actually upload to archive.org.
--only=<id>    Only process the identifier <id> (e.g. sarasvati-charter-v1.1).

Prereqs:
  1. pip install internetarchive
  2. ia configure   # enter Sarasvatī IA account email + password
  3. tar available in PATH
EOF
      exit 0
      ;;
    *)
      echo "Unknown arg: $arg (use -h for help)" >&2
      exit 2
      ;;
  esac
done

# ---------- helpers -----------------------------------------------------------
say()  { printf "\033[1;36m[ia]\033[0m %s\n" "$*"; }
warn() { printf "\033[1;33m[ia][warn]\033[0m %s\n" "$*"; }
err()  { printf "\033[1;31m[ia][err ]\033[0m %s\n" "$*" >&2; }
run()  {
  if [[ $LIVE -eq 1 ]]; then
    say "RUN:  $*"
    eval "$@"
  else
    say "DRY:  $*"
  fi
}

# Tiny YAML reader — good enough for our flat schemas.
# Usage: yaml_scalar <file> <key>  → prints the trimmed value of `key: value`.
yaml_scalar() {
  local file="$1" key="$2"
  awk -v k="$key" '
    $0 ~ "^"k":" {
      sub("^"k":[[:space:]]*", "");
      # strip surrounding quotes if present
      sub("^\"", ""); sub("\"$", "");
      sub("^>-.*", "");
      print; exit
    }' "$file"
}

# Usage: yaml_list_block <file> <key>  → prints the list items under `key:`
yaml_list_block() {
  local file="$1" key="$2"
  awk -v k="$key" '
    $0 ~ "^"k":" { inblk=1; next }
    inblk {
      if ($0 ~ /^[^[:space:]-]/) { inblk=0; next }
      if ($0 ~ /^[[:space:]]*-[[:space:]]/) {
        sub(/^[[:space:]]*-[[:space:]]*/, "");
        print
      }
    }' "$file"
}

# Multiline `description: >-` folded scalar reader (folds newlines into spaces).
yaml_description() {
  local file="$1"
  awk '
    /^description:[[:space:]]*>-/ { inblk=1; next }
    inblk {
      if ($0 ~ /^[^[:space:]]/) { exit }
      sub(/^[[:space:]]+/, "");
      if (out == "") { out = $0 } else { out = out " " $0 }
    }
    END { print out }
  ' "$file"
}

# ---------- pre-flight --------------------------------------------------------
if [[ $LIVE -eq 1 ]]; then
  if ! command -v ia >/dev/null 2>&1; then
    err "'ia' CLI not found. Install with: pip install internetarchive && ia configure"
    exit 1
  fi
  # Verify credentials
  if ! ia whoami >/dev/null 2>&1; then
    err "'ia' is not configured. Run: ia configure"
    exit 1
  fi
  say "Logged in as: $(ia whoami)"
else
  say "DRY-RUN MODE — pass --live to actually upload."
  if ! command -v ia >/dev/null 2>&1; then
    warn "'ia' CLI not installed. Dry-run will still work; install before --live."
  fi
fi

# ---------- build tarball for full-corpus item --------------------------------
build_full_corpus_tarball() {
  mkdir -p "$BUILD_DIR"
  local tarball="$BUILD_DIR/sarasvati-v0.9.tar.gz"
  say "Building repo tarball → $tarball"
  if [[ $LIVE -eq 1 ]]; then
    tar --exclude='.git' \
        --exclude='drafts' \
        --exclude='.github' \
        --exclude='.DS_Store' \
        -czf "$tarball" \
        -C "$(dirname "$REPO_ROOT")" \
        "$(basename "$REPO_ROOT")"
    say "Tarball size: $(du -h "$tarball" | cut -f1)"
    sha256sum "$tarball" 2>/dev/null || shasum -a 256 "$tarball"
  else
    say "DRY: tar -czf $tarball  (repo minus .git/drafts/.github/.DS_Store)"
  fi
  echo "$tarball"
}

# ---------- process one metadata file ----------------------------------------
process_item() {
  local meta="$1"
  local id title creator date mediatype collection language licenseurl description
  id="$(yaml_scalar "$meta" identifier)"
  title="$(yaml_scalar "$meta" title)"
  creator="$(yaml_scalar "$meta" creator)"
  date="$(yaml_scalar "$meta" date)"
  mediatype="$(yaml_scalar "$meta" mediatype)"
  collection="$(yaml_scalar "$meta" collection)"
  language="$(yaml_scalar "$meta" language)"
  licenseurl="$(yaml_scalar "$meta" licenseurl)"
  description="$(yaml_description "$meta")"

  if [[ -n "$ONLY" && "$id" != "$ONLY" ]]; then
    return 0
  fi

  say "──────────────────────────────────────────────────────────────"
  say "ITEM: $id"
  say "  title:      $title"
  say "  creator:    $creator"
  say "  collection: $collection"

  # Collect files. For full-corpus, we build the tarball first.
  local -a file_args=()
  local -a subject_args=()

  # subjects → repeated --metadata=subject:...
  while IFS= read -r s; do
    [[ -z "$s" ]] && continue
    subject_args+=( "--metadata=subject:$s" )
  done < <(yaml_list_block "$meta" subject)

  # files → absolute paths (or built tarball path)
  while IFS= read -r f; do
    [[ -z "$f" ]] && continue
    if [[ "$f" == "sarasvati-v0.9.tar.gz" ]]; then
      # Special: build now, use resulting path.
      local tarball
      tarball="$(build_full_corpus_tarball)"
      file_args+=( "$tarball" )
    else
      local abs="$REPO_ROOT/$f"
      if [[ ! -e "$abs" ]]; then
        err "File missing: $abs (declared in $meta)"
        return 1
      fi
      file_args+=( "$abs" )
    fi
  done < <(yaml_list_block "$meta" files)

  say "  files (${#file_args[@]}):"
  local ff
  for ff in "${file_args[@]}"; do
    say "    - $ff"
  done

  # Build the ia upload command.
  # Note: `ia upload <id> <files...> --metadata=key:value ...`
  local cmd="ia upload $(printf '%q' "$id")"
  for ff in "${file_args[@]}"; do
    cmd+=" $(printf '%q' "$ff")"
  done
  cmd+=" --metadata=title:$(printf '%q' "$title")"
  cmd+=" --metadata=creator:$(printf '%q' "$creator")"
  cmd+=" --metadata=date:$(printf '%q' "$date")"
  cmd+=" --metadata=mediatype:$(printf '%q' "$mediatype")"
  cmd+=" --metadata=collection:$(printf '%q' "$collection")"
  cmd+=" --metadata=language:$(printf '%q' "$language")"
  cmd+=" --metadata=licenseurl:$(printf '%q' "$licenseurl")"
  cmd+=" --metadata=description:$(printf '%q' "$description")"
  local sarg
  for sarg in "${subject_args[@]}"; do
    cmd+=" $(printf '%q' "$sarg")"
  done
  # Retry on transient failure; IA supports resumable uploads by default.
  cmd+=" --retries=5"

  run "$cmd"

  if [[ $LIVE -eq 1 ]]; then
    say "→ https://archive.org/details/$id"
  fi
}

# ---------- main --------------------------------------------------------------
say "Sarasvatī → Internet Archive uploader"
say "Repo:       $REPO_ROOT"
say "Metadata:   $META_DIR"
say "Mode:       $([[ $LIVE -eq 1 ]] && echo LIVE || echo DRY-RUN)"
[[ -n "$ONLY" ]] && say "Filter:     only $ONLY"

# Deterministic order (charter first, samples in branch order, full corpus last)
ORDER=(
  sarasvati-charter-v1.1
  sarasvati-dn16-mahaparinibbana-4lang
  sarasvati-ashoka-rock-edict-XII
  sarasvati-prajnaparamita-hridaya
  sarasvati-gandhari-dharmapada-khotan-Ia
  sarasvati-foyijiao-jing-T389
  sarasvati-karaniya-metta-sutta-Sn1.8
  sarasvati-wonhyo-daeseung-gisillon-preface
  sarasvati-full-corpus-v0.9
)

for id in "${ORDER[@]}"; do
  meta="$META_DIR/$id.yaml"
  if [[ ! -f "$meta" ]]; then
    err "Missing metadata file: $meta"
    exit 1
  fi
  process_item "$meta"
done

say "──────────────────────────────────────────────────────────────"
if [[ $LIVE -eq 1 ]]; then
  say "DONE — all items pushed. Verify at https://archive.org/details/@<your-ia-account>"
else
  say "DRY-RUN complete. Re-run with --live to actually upload."
fi
