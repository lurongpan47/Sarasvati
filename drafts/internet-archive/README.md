<!-- Prepared 2026-09-13 by Lucy. IA upload flow: Pan reviews metadata → Pan approves Lucy to upload OR runs upload.sh himself. -->

# Sarasvatī → Internet Archive · Upload Package

Everything needed to mirror Sarasvatī v0.9 to [archive.org](https://archive.org) in one pass.

**Why IA?** Free, permanent, world-mirrored, no gate-keeping. Fastest additional backup layer we can stand up. Complements — does not replace — the GitHub primary and the eventual Zenodo DOI.

**Author-of-record on IA**: `Dr. Lurong Pan (潘麓蓉) · Sarasvatī project`.
**License on every item**: [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/).
**Collection**: `opensource` (which auto-surfaces under `opensource_texts` = *Community Texts*).

---

## Files in this directory

```
drafts/internet-archive/
├── README.md                  ← you are here
├── upload-manifest.md         ← human-readable spec of what goes where
├── upload.sh                  ← bash driver, dry-run by default
└── metadata/
    ├── sarasvati-charter-v1.1.yaml
    ├── sarasvati-dn16-mahaparinibbana-4lang.yaml
    ├── sarasvati-ashoka-rock-edict-XII.yaml
    ├── sarasvati-prajnaparamita-hridaya.yaml
    ├── sarasvati-gandhari-dharmapada-khotan-Ia.yaml
    ├── sarasvati-foyijiao-jing-T389.yaml
    ├── sarasvati-karaniya-metta-sutta-Sn1.8.yaml
    ├── sarasvati-wonhyo-daeseung-gisillon-preface.yaml
    └── sarasvati-full-corpus-v0.9.yaml
```

Nothing here is committed to git yet. After Pan approves the metadata, the whole `drafts/internet-archive/` directory can be committed (or kept out of git — it never needs to ship in the repo).

---

## Which IA account do we use?

**Pan to decide before upload.** Two clean options:

1. **Dedicated project account** — e.g. `sarasvati-project@…` or `sarasvati@…`. Preferred for continuity: future collaborators can be granted access without touching Pan's personal profile. Contact + about page can be Sarasvatī-branded. Recommended.
2. **Pan's personal IA account** — fastest to spin up if Pan already has one, but every upload is filed under Pan's personal username on IA.

Either way, the `creator` metadata field on every item stays `Dr. Lurong Pan (潘麓蓉) · Sarasvatī project` — that is the authoritative attribution, not the uploader username.

**Lucy is not authorised to create IA accounts under Pan's name.** Pan must either create the account himself, or explicitly hand credentials to Lucy after creation.

---

## Prerequisites

On whichever machine will run `upload.sh --live`:

```bash
# 1. Install the IA CLI (once)
pip install internetarchive        # or: pipx install internetarchive

# 2. Configure credentials (once)
ia configure
# → prompts for the IA account email + password created above
# → writes ~/.config/internetarchive/ia.ini (or ~/.ia)

# 3. Sanity check
ia whoami
```

Also required: `bash`, `tar`, `awk` (all in the macOS base install).

---

## Dry-run first (mandatory)

```bash
cd ~/clawd/Sarasvati/drafts/internet-archive
./upload.sh                       # full dry-run, prints every ia command
./upload.sh --only=sarasvati-charter-v1.1     # dry-run one item
```

Dry-run **does not** require the `ia` CLI to be installed. It just echoes the exact `ia upload …` commands that will run under `--live`. Review these with Pan.

---

## Live upload

```bash
# Full push, all 9 items:
./upload.sh --live

# Or one item at a time (safer for the first live run):
./upload.sh --live --only=sarasvati-charter-v1.1
./upload.sh --live --only=sarasvati-dn16-mahaparinibbana-4lang
# … etc, in the order printed by dry-run.
```

Behaviour under `--live`:

- Verifies `ia whoami` returns a logged-in identity; aborts if not.
- For the `sarasvati-full-corpus-v0.9` item, builds `build/sarasvati-v0.9.tar.gz` (repo tree minus `.git/`, `drafts/`, `.github/`, `.DS_Store`) and prints its SHA-256 for spot-checking against `manifests/SHA256SUMS`.
- Runs `ia upload` with `--retries=5`. IA uploads are resumable, so a dropped connection is safe to re-run.

Expected wall-clock: ~5–15 minutes total from a home connection. Each item derives a `<identifier>_files.xml`, `<identifier>_meta.xml`, torrent, and IPFS gateway URL within a few minutes of upload. Full-text search indexing takes up to 24 h.

---

## Post-upload verification

Once each item is live, verify:

```bash
# 1. Item page loads
open https://archive.org/details/<identifier>

# 2. Metadata JSON matches what we sent
curl -s https://archive.org/metadata/<identifier> | jq '.metadata | {title, creator, licenseurl, subject, language}'

# 3. Every declared file is present
ia list <identifier>
```

Expected item URLs after successful `--live` run:

| Item | URL |
| --- | --- |
| `sarasvati-charter-v1.1` | https://archive.org/details/sarasvati-charter-v1.1 |
| `sarasvati-dn16-mahaparinibbana-4lang` | https://archive.org/details/sarasvati-dn16-mahaparinibbana-4lang |
| `sarasvati-ashoka-rock-edict-XII` | https://archive.org/details/sarasvati-ashoka-rock-edict-XII |
| `sarasvati-prajnaparamita-hridaya` | https://archive.org/details/sarasvati-prajnaparamita-hridaya |
| `sarasvati-gandhari-dharmapada-khotan-Ia` | https://archive.org/details/sarasvati-gandhari-dharmapada-khotan-Ia |
| `sarasvati-foyijiao-jing-T389` | https://archive.org/details/sarasvati-foyijiao-jing-T389 |
| `sarasvati-karaniya-metta-sutta-Sn1.8` | https://archive.org/details/sarasvati-karaniya-metta-sutta-Sn1.8 |
| `sarasvati-wonhyo-daeseung-gisillon-preface` | https://archive.org/details/sarasvati-wonhyo-daeseung-gisillon-preface |
| `sarasvati-full-corpus-v0.9` | https://archive.org/details/sarasvati-full-corpus-v0.9 |

Each URL is also — automatically — a torrent seed, an IPFS gateway path, and a stable permalink usable in citations.

---

## After a successful live run

1. **Copy the 9 URLs** into `~/clawd/Sarasvati/RESOURCE-QUEUE.md` and into the next `CHANGELOG.md` entry (v0.9.1 or v0.10).
2. **Add a `Mirrors` section** to `README.md`: "This repository is also mirrored on Internet Archive; identifiers begin with `sarasvati-`."
3. **Cite the full-corpus tarball SHA-256** in the CHANGELOG next to the OpenTimestamps proof — that ties the IA mirror back to the same signed tree.
4. **Do NOT delete `drafts/internet-archive/`** — the metadata YAMLs are the audit trail for what got uploaded. Keep them; revise them for v0.10.

---

## What Pan needs to decide

Before Lucy (or anyone) runs `--live`:

1. **Account identity** — dedicated `sarasvati-project` IA account, or Pan's personal one? (See above.)
2. **Who runs `--live`** — Pan himself, or does Pan hand credentials to Lucy for one run?
3. **Are the 24 charter language editions ready for public mirroring**, given they are still AI drafts flagged `⟨བརྟག⟩`? (Charter README already declares this; safe to mirror as long as the "awaiting review" flag is preserved — which it is, because we upload the source files verbatim.)
4. **Include internal folders?** Current package excludes `impl/`, `proposals/`, `announcements/`, `resource-leads/`, `scripts/`, `.github/` from item 9's tarball. Change if Pan wants those mirrored too (one-line edit in `upload.sh`).

Once Pan says yes to (1)–(4), a `--live` run is one command.
