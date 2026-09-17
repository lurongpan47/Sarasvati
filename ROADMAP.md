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
- **First sample (v0.9)**: Aśoka Major Rock Edict XII, Girnar recension — 4-language reading (Prakrit / English / Chinese / Tibetan). `translations/ashoka-edicts/major-rock-edict-XII-4lang.md`. Chinese and Tibetan are machine drafts awaiting named human review.
- **Second sample (added 2026-09-15)**: Aśoka Major Rock Edict XIII, Kālsī recension — 4-language reading covering Kalinga-war remorse, dhamma-vijaya, and the naming of the Hellenistic kings (c. 256 BCE). `translations/ashoka-edicts/major-rock-edict-XIII-4lang.md`. Prakrit + English from Hultzsch 1925 (public domain); Chinese + Tibetan are Sarasvatī machine drafts.
- **Sample targets (future)**: public-domain critical editions of foundational sūtras.

### 2. Sanskrit manuscript — 梵文写本系 · `sanskrit`
Palm-leaf, birch-bark, modern critical editions.
- **First sample (v0.9)**: Prajñāpāramitā Hṛdaya Sūtra (short recension) — 5-language reading (Sanskrit Devanāgarī / IAST / English machine draft / Xuánzàng T251 / Derge Kangyur Tibetan). `translations/prajnaparamita-hridaya/short-recension-4lang.md`. English is machine draft; awaiting Sanskritist review.
- **Priority pool**: GRETIL corpus (public-domain machine-readable Sanskrit), Nepalese Navagrantha, Gilgit finds.
- **Sample targets**: Mūlamadhyamakakārikā cross-language readings; short sūtras never rendered in Tibetan or Chinese.

### 3. Pāli — 巴利·斯里兰卡 · `pali`
Theravāda canon.
- **Priority pool**: PTS Roman-script editions (post-1928 public domain); SuttaCentral parallel data.
- **Sample targets**: nikāya passages not yet in Tibetan; commentaries lacking English/Chinese versions.
- **Current asset**: DN 16 (Mahāparinibbāna Sutta) final-instructions four-language reading — the scriptural root of the AI charter.

### 4. Southeast Asian Theravāda — 南传东南亚 · `seasia`
Burma, Siam, Cambodia, Laos.
- **First sample (v0.9)**: Karaṇīya Mettā Sutta (Sn 1.8, complete 10 verses) — 5-language reading (Pāli PTS / English Chalmers 1932 / Chinese / Burmese / Thai). `translations/karaniya-metta-sutta/Sn1.8-4lang.md`. Chinese, Burmese, Thai are machine drafts awaiting Myanmar/Thai Saṅgha review.
- **Priority pool**: 5th, 6th, 8th, 9th council editions; VRI Chaṭṭha Saṅgāyana digital.
- **Sample targets**: Khmer, Lao, Shan-script vernacular commentaries.

### 5. Silk Road / Central Asia — 中亚·丝路 · `silkroad`
Gāndhārī, Khotanese, Tocharian, Uighur, Tangut.
- **First sample (v0.9, attested-text version, added 2026-09-14)**: Gāndhārī Dharmapada, Khotan (Dutreuil de Rhins) manuscript, *Apramādavaga* chapter — 4-language reading with **real manuscript readings** in the Gāndhārī column, from the public-domain Barua–Mitra 1921 edition (based on Senart 1897). Four verses parallel to Pāli Dhp 27, 30, 167, 327. `translations/gandhari-dharmapada/khotan-manuscript-apramadavaga-4lang.md`.
- **Pedagogical companion (kept, not primary)**: `translations/gandhari-dharmapada/khotan-fragment-Ia-3lang.md` — reconstruction of what Dhp 1–4 *would* look like in Gāndhārī if they had survived on the Khotan folio (they don't). Header warns readers not to cite it as manuscript evidence.
- **Priority pool**: Schøyen Collection, Bower manuscript, Dunhuang cave 17 dispersals (BL, BnF, IDP).
- **Sample targets**: individual Dunhuang manuscripts with no full modern translation.

### 6. Chinese canon — 汉传系 · `chinese`
Kaibao → Kaixi → Jiaxing → Qianlong → Taishō → CBETA.
- **First sample (v0.9)**: Fó yíjiào jīng (佛遺教經, T389, Kumārajīva) — selected core passages, 4-language reading (漢文 T389 / English / Tibetan / 现代白话中文). `translations/foyijiao-jing/T389-selected-4lang.md`. English, Tibetan, modern-Chinese vernacular are machine drafts awaiting review.
- **Priority pool**: CBETA public-facing texts; Dunhuang colophons.
- **Sample targets**: minor texts in Taishō vol. 85 never translated to English/Tibetan.

### 7. Sinosphere — 汉字文化圈 · `sinosphere`
Korea, Japan, Vietnam.
- **First sample (v0.9)**: Wŏnhyo (元曉, 617–686), Preface to *Commentary on the Awakening of Faith* (《大乘起信論疏》序, CBETA T44 no.1844) — 3-language reading (漢文 / 한국어 / English). `translations/wonhyo-prologue/daeseung-gisillon-so-prologue-3lang.md`. Korean and English are machine drafts; awaiting Korean Buddhologist review.
- **Priority pool**: Tripiṭaka Koreana (public colophons); Nara scriptoria digitizations; SAT database.
- **Sample targets**: Korean/Japanese commentaries without foreign-language versions.

### 8. Tibetan — 藏传系 · `tibetan`
Kangyur / Tengyur; Mongolian & Manchu editions.
- **First dedicated sample (v0.9, added 2026-09-17)**: Udānavarga (ཆེད་དུ་བརྗོད་པའི་ཚོམས, *Ched-du brjod-pa'i tshoms*, Dharmatrāta), Anityavarga (chapter 1, *mi rtag pa'i tshoms*), verses 1–4 — 4-language reading (Tibetan dbu-can / Wylie / English Rockhill 1892 / Pāli Dhp parallel / T210 Chinese parallel). `translations/udanavarga-tibetan/anityavarga-verses1-4-4lang.md`. Tibetan text and English are **attested public-domain** (Rockhill 1892, Narthang Kangyur); no machine translation in the source-language column.
- **Additional asset**: DN 16 Tibetan draft embedded in the Pāli · English · Chinese · Tibetan cross-branch reading.
- **Sample targets (future)**: short texts in Tengyur commentary literature without modern translations; a Bernhard-independent public-domain Sanskrit parallel for the Anityavarga.

---

## Core 2 · Buddhist AI Charter

**Delivered:**
- `charter/BUDDHIST-AI-CHARTER.md` — ten principles + five refusals + attestation.
- `charter/i18n/` — 24 language versions.
- `translations/mahaparinibbana-sutta/final-instructions-4lang.md` — DN 16 four-language reading (scriptural root).
- **Python runtime**: `impl/python/` — `buddhist-ai-guardrail` v0.1.1 (charter, ten principles, five refusals, verdict + guardrail, tests).
- **TypeScript runtime**: `impl/typescript/` — `@sarasvati/buddhist-ai-guardrail` v0.1.0 (API parity with Python, Node 20+, dual ESM/CJS, zero deps, vitest suite).
- **Project site**: <https://lurongpan47.github.io/Sarasvati> — Jekyll on GitHub Pages (charter · eight branches · timeline · runtimes).

**Next:**
- Additional signatories beyond the initial Claude Opus 4.7 attestation.
- Human review of the Tibetan strand of the four-language reading.
- Publish `buddhist-ai-guardrail` to PyPI and `@sarasvati/buddhist-ai-guardrail` to npm (requires Pan's credentials).

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

