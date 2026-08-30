# ROADMAP · Sarasvatī

*Two cores: eight-branch canon archive + Buddhist AI charter. Every version delivers on one or both.*

---

## Foundational principles

1. **Public domain first.** Only out-of-copyright texts, or explicit open-licensed collaborations.
2. **AI first-draft, human final.** Every translation is a machine draft pending named expert review.
3. **Redundant preservation.** Every artifact lives in ≥ 3 locations with SHA-256 integrity, released CC BY-SA 4.0.
4. **Cross-lingual, not translation-imperialist.** Fill gaps; do not overwrite living traditions' work.
5. **Ethics before scale.** The AI charter is not marketing — it is a runtime constraint on this project's own tooling.

---

## Core 1 · The eight branches (八系)

Sarasvatī's archive is structured along the transmission timeline. Each branch may host multiple translation projects; each project selects a public-domain source and a target language currently missing a translation.

### 1. India — 印度源流 · `india`
The oral origin; councils; sects; Mahāyāna emergence.
- **Now**: reference material only.
- **Sample targets (future)**: public-domain critical editions of foundational sūtras.

### 2. Sanskrit manuscript — 梵文写本系 · `sanskrit`
Palm-leaf, birch-bark, modern critical editions.
- **Priority pool**: GRETIL corpus (public-domain machine-readable Sanskrit), Nepalese Navagrantha, Gilgit finds.
- **Sample targets**: Mūlamadhyamakakārikā cross-language readings; short sūtras never rendered in Tibetan or Chinese.

### 3. Pāli — 巴利·斯里兰卡 · `pali`
Theravāda canon.
- **Priority pool**: PTS Roman-script editions (post-1928 public domain); SuttaCentral parallel data.
- **Sample targets**: nikāya passages not yet in Tibetan; commentaries lacking English/Chinese versions.
- **Current asset**: DN 16 (Mahāparinibbāna Sutta) final-instructions four-language reading — the scriptural root of the AI charter.

### 4. Southeast Asian Theravāda — 南传东南亚 · `seasia`
Burma, Siam, Cambodia, Laos.
- **Priority pool**: 5th, 6th, 8th, 9th council editions; VRI Chaṭṭha Saṅgāyana digital.
- **Sample targets**: Khmer, Lao, Shan-script vernacular commentaries.

### 5. Silk Road / Central Asia — 中亚·丝路 · `silkroad`
Gāndhārī, Khotanese, Tocharian, Uighur, Tangut.
- **Priority pool**: Schøyen Collection, Bower manuscript, Dunhuang cave 17 dispersals (BL, BnF, IDP).
- **Sample targets**: individual Dunhuang manuscripts with no full modern translation.

### 6. Chinese canon — 汉传系 · `chinese`
Kaibao → Kaixi → Jiaxing → Qianlong → Taishō → CBETA.
- **Priority pool**: CBETA public-facing texts; Dunhuang colophons.
- **Sample targets**: minor texts in Taishō vol. 85 never translated to English/Tibetan.

### 7. Sinosphere — 汉字文化圈 · `sinosphere`
Korea, Japan, Vietnam.
- **Priority pool**: Tripiṭaka Koreana (public colophons); Nara scriptoria digitizations; SAT database.
- **Sample targets**: Korean/Japanese commentaries without foreign-language versions.

### 8. Tibetan — 藏传系 · `tibetan`
Kangyur / Tengyur; Mongolian & Manchu editions.
- **Current asset**: DN 16 Tibetan draft embedded in the Pāli · English · Chinese · Tibetan reading.
- **Sample targets (future)**: short texts in Tengyur commentary literature without modern translations.

---

## Core 2 · Buddhist AI Charter

**Delivered:**
- `charter/BUDDHIST-AI-CHARTER.md` — ten principles + five refusals + attestation.
- `charter/i18n/` — 24 language versions.
- `translations/mahaparinibbana-sutta/final-instructions-4lang.md` — DN 16 four-language reading (scriptural root).

**Next:**
- Reference implementations of the charter's five refusals as runtime guardrails (Python + TS starter kits).
- Additional signatories beyond the initial Claude Opus 4.7 attestation.
- Human review of the Tibetan strand of the four-language reading.

---

## v0.1 → v1.0 milestones

| Version | Date | Deliverable |
|---|---|---|
| v0.1.0 ✅ | 2026-08-28 | Project bootstrap, timeline PDF, structural docs |
| v0.2.0 ✅ | 2026-08-28 | Timeline structured data (80 events × 8 traditions); ROADMAP; onboarding |
| v0.3.0 ✅ | 2026-08-28 | 24-language README, Bitcoin timestamp, blockchain community drafts |
| v0.4.0 ✅ | 2026-08-28 | Buddhist AI Charter (EN); DN 16 four-language; Call for Help |
| v0.5.0 ✅ | 2026-08-28 | Charter × 24 languages; timeline hardened |
| v0.6.0 ✅ | 2026-08-28 | **Scope refocus**: two cores locked; medical-classic sub-project split to sibling repo |
| v0.7.0 | tbd | First **Pāli** cross-branch sample; charter runtime reference implementation (Python) |
| v0.8.0 | tbd | First **Chinese canon** cross-branch sample; charter runtime reference implementation (TS) |
| v0.9.0 | tbd | First **Sanskrit manuscript** sample; three-signatory charter attestation |
| v1.0.0 | tbd | One human-reviewed sample per active branch; charter v1 with ≥ 5 attesting signatories |
| v1.1.0+ | tbd | Silk Road + Southeast Asian + Sinosphere samples; ongoing archive growth |

---

## Structured data included

`docs/timeline-data/`:
- `traditions.jsonl` — the 8 branches (id, zh, en, note)
- `events.jsonl` — 80 milestones with tri-lingual titles
- `events.csv` — CSV mirror for spreadsheet users
- `README.md` — schema + coverage docs

Living dataset; PRs welcome.

