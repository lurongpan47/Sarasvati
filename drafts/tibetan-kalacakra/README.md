# Tibetan Kālacakra working drafts · 时轮金刚相关草稿

> ⚠️ **DRAFTS, not published samples.** This directory holds machine-assisted working translations in the Kālacakra textual complex. **None of these files are at the quality level of `translations/*-4lang.md` samples** (which are scan-collated, cross-verified 4-language 4-stanza passages). Everything here is bulk draft, uncollated against print editions, and must not be cited as scholarship.

**Charter alignment:** This directory exists to make the drafts auditable rather than hidden. Per `satya` (truth-telling), nothing here is labelled as "attested" or "入藏". When any text here reaches the Sarasvatī sample standard (every passage checked against a scan, every verse column cross-verified by a named Buddhologist of Tibetan Vajrayāna), the finished subset migrates to `translations/kalacakra/<name>-4lang.md` and this folder's README is updated with the migration note.

---

## 📜 The 10-text Kālacakra project (per Pan's 2026-10-07 brief)

The scope Pan has outlined is a 10-text parallel-translation project drawn from the Derge Kangyur and Tengyur, roughly 365,000 Tibetan syllables:

### Kangyur
| Toh | Title | Status in this directory |
|---:|---|---|
| 361 | **Sekoddeśa** (174 verses; checked against GRETIL Sanskrit) | ❌ not located on this machine |
| 362 | **Laghu-Kālacakra-tantra** (= Śrī Kālacakra-rāja-tantra, 5 chapters by verse) | ❌ not located |
| 363 | **Tantrottara** ("Heart of the Tantra") | ❌ not located |

### Tengyur
| Toh | Title | Status |
|---:|---|---|
| 1346 | (identical with Toh 362; not translated twice) | n/a — reused Toh 362 |
| 1347 | **Vimalaprabhā** (12,000-stanza commentary — this directory's current file) | ✅ **present as bulk draft** (see below) |
| 1348 | **Paramārthasevā** | ❌ not located |
| 1349 | **"Light of the Heart"** (commentary on entering the tantra) | ❌ not located |
| 1350 | **Padminī pañjikā** | ❌ not located |
| 1351 | **Nāropa's Sekoddeśaṭīkā** (= Paramārthasaṃgraha) | ❌ not located |
| 1352 | Sekoddeśa commentary (brief) | ❌ not located |
| 1353 | Sekoddeśa commentary (extensive) | ❌ not located |
| 1354 | Sekoddeśa pañjikā | ❌ not located |

**Expected final deliverable (per Pan's brief):**
- Chinese collection ≈ 348 pages
- English collection ≈ 478 pages (≈ 320,000 words)
- Each text carries Sanskrit, Tibetan, and Chinese titles, Toh number, Derge folio range
- Folio markers kept in-text; verses numbered throughout
- Translated in **65 blocks of ≈ 6,000 syllables with overlapping context**
- Chinese register: classical Buddhist translation
- English register: academic (Wallace / Newman / Sferra conventions)
- **Explicitly uncollated** against the Banerjee / Orofino / Sferra critical editions

### Current gap

The other **9 Toh texts and both finished collections (348-page Chinese, 478-page English) are not on this Mac mini.** Per Pan's 2026-10-07 06:40 PDT message, these exist (produced somewhere), but their physical location is TBD. Pan is tracking them down.

---

## 📂 Files in this directory

### `vimalaprabha-bo-source.docx` (665 KB)

- **Toh 1347 — Vimalaprabhā** (*Dri-med 'od*, 无垢光)
- Opening: `བི་མ་ལ་པྲ་བྷཱ་ནཱ་མ་མཱུ་ལ་ཏནྟྲཱ་ནུ་སཱ་རི་ཎཱི་དྭཱ་ད་ཤ་སཱ་ཧ་སྲི་ཀཱ་ལ་གྷུ་ཀཱ་ལ་ཙཀྲ་ཏནྟྲ་རཱ་ཛ་ཊཱི་ཀཱ`
  = *Vimalaprabhā-nāma-mūla-tantra-anusāriṇī-dvādaśa-sāhasrikā-laghu-kālacakra-tantra-rāja-ṭīkā*
  = Tengyur title: *bsdus pa'i rgyud kyi rgyal po dus kyi 'khor lo'i 'grel bshad rtsa ba'i rgyud kyi rjes su 'jug pa stong phrag bcu gnyis pa dri ma med pa'i 'od ces bya ba*
  = "The Stainless Light: a 12,000-stanza commentary on the Śrī Kālacakra-tantra that follows the Root Tantra"
- **Author (traditional)**: Puṇḍarīka of Shambhala (Pad-ma dkar-po), c. 1030 CE redaction
- **Language**: Classical Tibetan (dbu-can; punctuated with tsheg)
- **Size**: 1,501,644 characters; **≈ 373,680 Tibetan syllables** (counted via tsheg `་`); 29,321 shad `།` sentence-boundaries
- **Provenance**: file came from Pan on or before 2026-04-07 (modification date). The Derge woodblock print (c. 1733) itself is public domain by age. The specific digital edition / source scan behind this .docx is **not documented** in the file itself; this needs recovery before any citation.
- **Status**: `source_bulk` — raw bulk Tibetan source text. **Has NOT been collated against a Derge Kangyur / Tengyur scan**, line endings and folio markers may not match the Derge printing. Do not cite folio numbers from this file.

### `vimalaprabha-zh-draft.docx` (491 KB)

- Chinese working translation of Vimalaprabhā, machine-assisted
- 423,508 characters
- Opens: *时轮大疏·无垢光（甲）时轮大疏无垢光*
- Headers formatted as `#` markdown-ish inside .docx
- Register leans classical-Buddhist (梵语:…藏语:…, 敬礼吉祥时轮)
- **Status**: `translation_bulk` — bulk machine-assisted draft, **not humanly collated**, no verse numbering, no folio markers, no Sanskrit/Tibetan title headers on each section. Does not yet meet the "each text carries its Sanskrit, Tibetan and Chinese titles, Toh number and Derge folio range" standard described in Pan's project brief.

---

## 🛑 Why this is in `drafts/` and NOT `translations/`

The `translations/` directory in Sarasvatī hosts **finished samples**: 4-language parallel readings, every column either copied verbatim from a verifiable public-domain scan OR marked `⟨བརྟག⟩` as a Sarasvatī draft, with every stanza traceable to specific leaves. Each sample is small (typically 4 verses), and each is **scan-collated** before being added.

The two Vimalaprabhā files are 150× larger than one of those samples, were produced before the scan-first workflow existed (April 2026), and have never been checked line-by-line against the Derge printing. Promoting them into `translations/` would silently lower the quality bar for the whole repo — a violation of `satya`. They stay here until they earn promotion.

---

## 🗺 Path to promotion

To migrate any part of this directory into `translations/kalacakra/`, the following must be true for the migrated subset:

1. **Scan source identified**: specific Derge printing (BDRC W-number) or critical edition (Banerjee 1985, Orofino 1994a, Sferra 1998/2000, Jagannātha Upādhyāya 1986), with the file reference recorded.
2. **Line-by-line collation**: each Tibetan line matched to the scan; folio markers inserted.
3. **Verse numbering**: following one of the standard editions (Banerjee for Sekoddeśa; Upādhyāya for Vimalaprabhā).
4. **Second-model cross-verification**: for any passage read from a scan, a second independent `image` call reads the same crop and the readings are compared (Sarasvatī standard rule since 2026-09-28).
5. **Named reviewer**: for Chinese translations, a Buddhologist of Tibetan Vajrayāna (and/or classical-Chinese Buddhist translator) signs off and is added to `CONTRIBUTORS.md`.

Until (1)–(5) are done, this remains a draft.

---

## 📅 Changelog for this directory

- **2026-10-07** — Created. `vimalaprabha-bo-source.docx` and `vimalaprabha-zh-draft.docx` imported from `~/clawd/时轮法_408页_fixed.docx` and `~/clawd/时轮法_Chinese_translated.docx` (originals retained in place). This README documents the project scope and the gap between Pan's 10-text brief and the material currently on this machine.
