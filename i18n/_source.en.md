# Sarasvatī — canonical source blurb for translation

Below is the exact English text to translate into your target language(s).
Preserve names, code identifiers, URLs, and license names AS-IS.
Preserve Sanskrit / Pāli / Tibetan terms in their original scripts.
Do NOT translate: "Sarasvatī", "Mahāparinibbāna Sutta", "CC BY-SA 4.0",
"GitHub", "IPFS", "Bitcoin", "OpenTimestamps", file paths, URLs, "OpenClaw",
branch code identifiers (india, sanskrit, pali, seasia, silkroad, chinese,
sinosphere, tibetan), proper names of editions.

---

# Sarasvatī — a global open archive for the Buddhist canon + a Buddhist AI charter

**Sarasvatī** (Tibetan: དབྱངས་ཅན་མ། · Sanskrit: सरस्वती) does exactly two things:

1. **Eight-branch canon archive.** Build a cross-lingual open archive along
   the eight transmission branches of the Buddhist canon: **India ·
   Sanskrit manuscripts · Pāli · Southeast Asian Theravāda · Silk Road /
   Central Asia · Chinese canon · Sinosphere · Tibetan**. Public-domain
   texts only, or explicit collaboration with living traditions.
2. **Bodhicitta into AI algorithms.** The Buddha's last teachings
   (*Mahāparinibbāna Sutta*) distilled into **ten principles + five
   refusals** and published as a charter that any AI system, operator, or
   team can adopt. *Ahiṃsā · karuṇā · anattā · anicca · upekkhā* become
   executable algorithmic constraints, not slogans.

All output is released under **CC BY-SA 4.0**.

## Why this exists

Classical texts are humanity's common inheritance. They should not be locked
behind copyright, burnt by war, or lost by broken links. And AI systems
should not be deployed without ethical constraints drawn from any real
wisdom tradition. Sarasvatī tackles both — one archive layer for memory,
one charter layer for ethics.

## Current status

**v0.6.0** (2026-08-28):

- 📜 **Buddhist AI Charter** — ten principles + five refusals + attestation
  clause in `charter/BUDDHIST-AI-CHARTER.md`. Translated into 24 languages
  under `charter/i18n/`, awaiting native-speaker Buddhist scholar review.
- 🕉 **Mahāparinibbāna Sutta four-language reading** (DN 16.2.26 · 16.4.7 ·
  16.6.7) in Pāli · English · Chinese · Tibetan under
  `translations/mahaparinibbana-sutta/`. This is the scriptural root of
  the charter and the first sample of the archive.
- 📊 **Structured timeline data** — 80 canonical-transmission events across
  the 8 Buddhist traditions (india, sanskrit, pali, seasia, silkroad,
  chinese, sinosphere, tibetan) as JSONL / CSV in `docs/timeline-data/`.
- 📋 Project docs: `README.md`, `ROADMAP.md`, `CALL-FOR-HELP.md`,
  `CONTRIBUTORS.md`, `announcements/`.

## Roadmap (eight branches)

Sarasvatī's long-term structure follows the world Buddhist canon
transmission timeline: **India · Sanskrit manuscripts · Pāli · Southeast
Asian Theravāda · Silk Road · Chinese canon · Sinosphere · Tibetan**.
Each branch will host at least one first sample: a public-domain source
text machine-translated into a language currently lacking a translation,
with a named human reviewer. The Tibetan branch has a first asset (DN 16).
Pāli has been touched through the same DN 16 four-language reading. The
remaining six branches (India · Sanskrit · Southeast Asian · Silk Road ·
Chinese · Sinosphere) are open for contributors to launch.

## Protection stack

Every artifact is protected by:

- **Local mirror** on macOS.
- **GitHub public repo** — https://github.com/lurongpan47/Sarasvati.
- **AWS geographic mirrors** across multiple regions.
- **IPFS decentralized mirror** — CID
  `bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce`.
- **OpenTimestamps → Bitcoin** — a nonrepudiable time anchor on
  `manifests/SHA256SUMS`.

## ⚠️ Disclaimer

All translations and machine-drafted texts here are **AI machine drafts**
pending expert human review. Do not treat them as authoritative for
ritual, doctrinal, medical, or scholarly purposes without validation by
named specialists.

## How to contribute

- Open an issue proposing a text, a chapter revision, a terminology fix,
  or a charter-language review.
- Fork, edit, PR. All contributions accepted under CC BY-SA 4.0.
- Run a mirror. Help preserve the archive.
- Help build the **charter runtime** (Python + TypeScript guardrail
  libraries) — see `CALL-FOR-HELP.md`.

## Links

- GitHub: https://github.com/lurongpan47/Sarasvati
- License: CC BY-SA 4.0

---

*"Vayadhammā saṅkhārā, appamādena sampādetha."*
*All conditioned things are impermanent. Strive on with diligence.*
