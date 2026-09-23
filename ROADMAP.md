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
- **First sample (v0.9; scan-checked and corrected 2026-09-21)**: Aśoka Major Rock Edict XII, Girnar recension — 4-language reading (Prakrit / English / Chinese / Tibetan). `translations/ashoka-edicts/major-rock-edict-XII-4lang.md`. Prakrit and English are now copied from the Hultzsch 1925 page images (IA `InscriptionsOfAsoka.NewEditionByE.Hultzsch`, pp. 20–22) with his footnotes; the 09-13 columns had been written from memory (Pāli-ised `siyā` for attested `asa`, invented `suṇārū` / `suśruṣerā` for `sruṇāru` / `susuṁsera`, emendations printed as text, English paraphrased) — erratum table at the top of the file. Chinese and Tibetan are machine drafts awaiting named human review.
- **Second sample (added 2026-09-15; scan-checked and corrected 2026-09-22)**: Aśoka Major Rock Edict XIII, Kālsī recension — 4-language reading covering Kalinga-war remorse, dhamma-vijaya, and the naming of the Hellenistic kings (c. 256 BCE). `translations/ashoka-edicts/major-rock-edict-XIII-4lang.md`. Prakrit and English are now Hultzsch's Roman transliteration rows (pp. 45–46) and translation (pp. 47–49) copied from the page images with his footnotes; the 09-15 columns had mis-stated the pages ("plate on p. 45"), used a mixed IAST/Pāli convention, printed emendations as text and filled Kālsī's lacunae with words on no rock (`mukhya-mute`, `hida cha`, `shaveshu manuśyeshu`, `chalambu`) — erratum table at the top of the file. Chinese + Tibetan are Sarasvatī machine drafts awaiting named human review. Audit-queue score: 5 of 5 "attested" source columns checked were not what they claimed (Udānavarga 09-18, Gāndhārī 09-20, REXII 09-21, REXIII 09-22, Sn 1.8 Chalmers/PTS 09-23); remaining: T389 → Wŏnhyo prologue → new content.
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
- **First sample (v0.9; scan-checked and corrected 2026-09-23)**: Karaṇīya Mettā Sutta (Sn 1.8, complete 10 verses) — 5-language reading (Pāli PTS 1913 / English Chalmers 1932 / Chinese / Burmese / Thai). `translations/karaniya-metta-sutta/Sn1.8-4lang.md`. Pāli and English are now copied from the page images (PTS Andersen & Smith 1913 pp. 25–26 with apparatus, IA `in.ernet.dli.2015.343993` n39–n40; Chalmers HOS 37 pp. 37 + 39, IA `buddhasteachings032310mbp` n68 + n70); the 09-13 columns had been a Burmese-recension (CST-style) Pāli labelled "PTS" and a modern prose chanting-book rendering of unidentified provenance labelled "Chalmers" — erratum table at the top of the file. US copyright status of Chalmers 1932 checked (Stanford renewal DB + CCE 1959–60: no renewal found) and stated in the file. Chinese, Burmese, Thai are machine drafts awaiting Myanmar/Thai Saṅgha review.
- **Second sample (added 2026-09-21, weekly proposal → approved same day)**: Lokanīti ch. 1 *Paṇḍitakaṇḍa*, 40 gāthās — the first text in the archive *composed* in Southeast Asia (Burmese Pāli nīti). Pāli VRI CST re-keyed from XML / English Gray 1886 (PD, IA `cu31924052490913`, page-checked on 5 leaves) / 汉文 + བོད་ཡིག Sarasvatī drafts ⟨བརྟག⟩. `translations/lokaniti/lokaniti-01-panditakanda-4lang.md`. Needs a Pāli reader (VRI text is uneven), Chinese, Tibetan, and a Burmese nissaya teacher. Remaining Lokanīti chapters 2–7 (127 gāthās) and Gray's Dhammanīti / Rājanīti are the natural continuation.
- **Priority pool**: 5th, 6th, 8th, 9th council editions; VRI Chaṭṭha Saṅgāyana digital.
- **Sample targets**: Khmer, Lao, Shan-script vernacular commentaries.

### 5. Silk Road / Central Asia — 中亚·丝路 · `silkroad`
Gāndhārī, Khotanese, Tocharian, Uighur, Tangut.
- **First sample (v0.9, attested-text version, added 2026-09-14; scan-checked and corrected 2026-09-20)**: Gāndhārī Dharmapada, Khotan (Dutreuil de Rhins) manuscript, *Apramādavaga* chapter — 4-language reading with **real manuscript readings** in the Gāndhārī column, from the public-domain Barua–Mitra 1921 edition (based on Senart 1897; IA `in.ernet.dli.2015.41588`). Four verses (B–M vv. 20, 11, 23, 12) parallel to Pāli Dhp 27, 30, 327, 167. The 09-14 text had been written from memory and mis-transcribed three of the four verses (`prasaṃṣati` for attested `prasajhati`, etc.); erratum table at the top of the file. `translations/gandhari-dharmapada/khotan-manuscript-apramadavaga-4lang.md`.
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
- **First dedicated sample (v0.9, added 2026-09-17, corrected 2026-09-18)**: Udānavarga (ཆེད་དུ་བརྗོད་པའི་ཚོམས, *Ched-du brjod-pa'i tshoms*, Dharmatrāta; Kangyur Tōh. 326), Anityavarga (chapter 1, *mi rtag pa'i tshoms*), Rockhill verses I.3 · I.10 · I.12 · I.17 — 4-language reading (Tibetan dbu-can ⟨བརྟག⟩ / Wylie / English Rockhill 1892 / Pāli Sn + Dhp parallels / T210 Chinese parallel). `translations/udanavarga-tibetan/anityavarga-selected-verses-4lang.md`. **English is attested public-domain** (Rockhill 1892, verbatim from the scan). **Tibetan column is a Sarasvatī draft** — Rockhill prints no Tibetan; collation against Beckh 1911 (PD) or Derge Tōh. 326 is the branch's top open task. See the file's erratum header.
- **Additional asset**: DN 16 Tibetan draft embedded in the Pāli · English · Chinese · Tibetan cross-branch reading.
- **Priority pool (designated by Pan, 2026-09-22)**: **BDRC / BUDA — Buddhist Digital Archives** (https://library.bdrc.io, "Instance" view sorted by newest scans). Access verified 2026-09-22 with no credentials: RDF metadata per resource at `purl.bdrc.io/resource/<ID>` (Turtle), admin data at `purl.bdrc.io/admindata/<W-ID>` (`adm:access bda:AccessOpen` / `adm:status bda:StatusReleased` are the gates we honour), IIIF Presentation manifests at `iiifpres.bdrc.io/2.1.1/v:bdr:<VolumeID>/manifest`, page images at `iiif.bdrc.io/bdr:<ImageGroup>::<file>.tif/full/max/0/default.png`. Pilot target: Derge Kangyur (`bdr:MW22084`, 103 volumes, e.g. `V22084_I0886` = 622 canvases). Rule: only `AccessOpen` + `StatusReleased` scans; every BDRC-derived Tibetan column carries the volume ID + folio (`I0886::08860008`) so the reading can be checked against the same leaf. Texts whose `copyrightStatus` is `CopyrightUndetermined` are used for *reading a woodblock print*, never for copying a modern edition.
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
