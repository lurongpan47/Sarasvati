# CHANGELOG · Sarasvatī

All notable changes to this project will be documented here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning: SemVer.

## [v0.1.0] — 2026-08-28

### Added
- Project bootstrap: README (藏/英/汉 tri-lingual), LICENSE (CC BY-SA 4.0), STYLE.md.
- **Suśruta Saṃhitā · Sūtrasthāna** Tibetan machine-translation draft (46 chapters):
  - `translations/sushruta-samhita/sutrasthana/Sushruta-Sutrasthana-bo-v3.docx`
  - `translations/sushruta-samhita/sutrasthana/Sushruta-Sutrasthana-bo-v3.pdf`
- Source materials:
  - `translations/sushruta-samhita/sutrasthana/source/` — Bhishagratna 1907 English text, chapter-split, cleaned.
  - `translations/sushruta-samhita/sutrasthana/raw/` — Four sub-agent group outputs (traceable).
- Reference documents:
  - `docs/Sushruta-Tibetan-Project-Plan.docx` — original project design (structure, style, glossary, 186 chapters).
  - `docs/Global-Buddhist-Canon-Transmission-Timeline.pdf` — global chronology of Buddhist canonical transmission.
- SHA-256 checksums in `manifests/SHA256SUMS`.

### Method
- English source (public domain): Kaviraj Kunjalal Bhishagratna, *An English Translation of the Sushruta Samhita*, 1907; scraped from wisdomlib.org.
- Translation: four parallel Claude Opus 4.7 subagents, each handling ~12 chapters, sharing a common STYLE.md (glossary tied to *Aṣṭāṅgahṛdaya* Tibetan and *rGyud bZhi* traditions).
- Cleanup: single subagent pass to eliminate residual Chinese phrases in footnotes/dispute lists (0 CJK characters remaining).
- Assembly: python-docx with multi-script font hints (Tibetan complex-script → *Microsoft Himalaya* fallback).

### Known limitations
- Machine draft only; requires expert human review before authoritative use.
- Register is modern Tibetan medical prose, not classical *śāstra* register.
- ⟨བརྟག⟩ and ⟨བརྟག་དགོས།⟩ markers indicate items awaiting Tibetan medical validation.

### Distribution
- GitHub: https://github.com/wingring47-stack/Sarasvati
- Local: `~/clawd/Sarasvati/` (macOS)
- AWS mirror: `aws-quant:/home/ubuntu/Sarasvati/` (us-east-1)
