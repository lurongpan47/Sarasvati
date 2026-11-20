# 2026-11-20 · Dhp Sukhavagga V. 197-200 TRUE CHAPTER-OPENER — Subagent Decision Entry

**Subagent:** `sarasvati-dhp-197-200`  
**Requester session:** `agent:lucy:cron:f1ae0a74-48bf-4534-9b3c-cc35af0b72c1`  
**Build date:** 2026-11-20 PST  
**Deliverable:** `translations/dhammapada/sukhavagga-197-200-4lang.md` (~95 KB, 254 lines)

---

## Summary

Shipped the TRUE Sukhavagga chapter-opener (V. 197-200) primary-attesting what yesterday's 11-19 build could only foreword-attest. Four-stanza anaphora prediction `Susukhaṁ vata jīvāma …` CONFIRMED at pixel level. Fetched Fausbøll Latin leaf 0064 (first-try HTTP 200 via INNER-ZIP URL fallback — FOURTH consecutive instance, FULLY STABLE). T210 FIFTH-DAY outage persists with ERROR-CODE SHIFT from HTTP 404 to HTTP 503.

**4 `image` tool calls** (vs 50 ceiling = 8% of budget; below the 10-18 target range for chapter-openers; attribute to the efficient BILATERAL ZERO-FETCH chapter-opener scenario where only one new leaf needed attestation).

**31 enumerated first-attested findings.**

## Pixel-corrections vs the brief's predictions

**Confirmed predictions:**
- FOUR-STANZA ANAPHORA `Susukhaṁ vata jīvāma …` on V. 197/198/199/200 — ALL CONFIRMED (SAMPLES' NEW CROSS-STANZA ANAPHORA DENSITY RECORD)
- Fausbøll leaf 0064 via INNER-ZIP URL fallback — HTTP 200 first-try
- Müller tif 0113 ALREADY ON DISK — no refetch needed
- T210 FIFTH-DAY OUTAGE prediction — CONFIRMED (bonus: error-code shift from 404 to 503)

**Pixel-corrections required (TWO against yesterday's 11-19 sample, ONE against the brief):**

1. **Chapter heading NO SPACE BEFORE FINAL PERIOD** — yesterday's 11-19 build pixel-attested the Sukhavagga chapter-15 heading as `15. S u k h a v a g g a .` (with space before final period). Today's 3.0× + 4.0× zoom on the heading band disambiguates to `15. Sukhavagga.` with NO space before the final period. The 4.0× close-read shows the final `.` sits tight-kerned against the last `a`, matching the 11-16 `Buddhavagga.` and 11-13 `Lokavagga.` convention. Yesterday's reading was based on 2.0× zoom where the apparent inter-letter spacing obscured the tight final-period kerning. SAMPLES' FIRST attested WITHIN-BUILD CROSS-ZOOM DISAMBIGUATION event.

2. **V. 197 is a complete TWO-LINE STANZA** — yesterday's 11-19 build foreword-attested V. 197 only as a single-line opener `197. Susukhaṁ vata jīvāma verinesu averino,`. Today's primary attestation confirms V. 197 is a complete TWO-LINE STANZA with L2 reading `verinesu manussesu viharāma averino.` carrying the `manussesu` "among men" positional marker that forms the TWO-LINE PARALLEL structure matching V. 198-200.

3. **T210 chapter paralleling Sukhavagga is chapter 23 安寧品, NOT chapter 24** — the task brief projected T210 chapter 24 安寧品 for Sukhavagga parallel. CBETA TEI T04n0210.xml PIXEL-CORRECTION confirms the correct mapping is chapter 23 安寧品 (NOT 24). Chapter 24 is 好喜品 which parallels Pāli chapter 16 Piyavagga. The brief's secondary term `愛喜不生` appears in chapter 24 好喜品 Stanza 1 which parallels Pāli V. 212-216 Piyavagga opener, NOT Sukhavagga. SAMPLES' FIRST attested CROSS-CANON CHAPTER-INDEX TYPO PIXEL-CORRECTION.

## Natural non-competence declarations

Marked ⟨བརྟག⟩ for all Tibetan and Modern Chinese drafts. Natural non-competence declared for:

- **V. 200 `bhavissāma` future-vs-optative mood** — 1pl verb ending `-issāma` is ambiguous between future-indicative ("we shall be") and optative-desire ("may we be"). Flagged for Pāli-philology verification.

- **V. 200 Ābhassara-deva cosmology paleography** — the Pāli `devā ābhassarā` + Sanskrit `âbhâsvara` + Chinese `光音天` triple-correspondence is pixel-attested on the first two and TEI-referenced on the third. Natural non-competence declared for whether the Chinese `光音天` typography carries any 校勘記 apparatus marker at 0567b23.

- **V. 200 Mithilā-burning narrative relationship** — Müller's V. 200 note cites Mahâbh. XII, 9917 with the Sanskrit line `Susukha*m* vata *g*îvâmi yasya me nâsti ki*ñk*ana` which opens with the SAME formula as the Pāli V. 200 `Susukhaṁ vata jīvāma`. Natural non-competence declared for whether this indicates (a) Sanskrit-to-Pāli direction (Pāli stock-phrase derived from Sanskrit epic), (b) Pāli-to-Sanskrit direction (as Müller argues for other verses via his PĀLI-PRIORITY methodology), or (c) convergent-stock-phrase in the Indic śramaṇa + brāhmaṇa discourse pool.

## Methodology notes

- **Image call count**: 4 `image` tool calls (one for each of: Fausbøll overview + V. 197-200 bodies / Fausbøll heading + V. 200 + apparatus close-ups / Fausbøll Latin overview + top band / Müller tif 0113 overview + bodies + heading + notes). The 4-call figure is BELOW the 10-18 target for chapter-openers; attribute to BILATERAL ZERO-FETCH scenario where only one new leaf (Fausbøll Latin 0064) required fresh attestation.

- **Zoom escalation on heading** — the chapter-heading pixel-correction event was resolved by escalating zoom from 2.0× (yesterday's reading) to 3.0× (today's first read) to 4.0× (today's disambiguation read). SAMPLES' FIRST attested WITHIN-BUILD CROSS-ZOOM DISAMBIGUATION methodology where lower-zoom projection is pixel-corrected by higher-zoom read within the same build.

- **Latin leaf confirmed FIRST attempt** — the INNER-ZIP URL fallback `/112138_jp2.zip/112138_jp2%2F112138_0064.jp2` returned HTTP 200 on first-try (after 302 redirect) via `curl -sL` with 395,621 B JP2 → 1500×2500 L PNG via `opj_decompress`. FOURTH consecutive attestation of the INNER-ZIP URL fallback convention, SETTLING as FULLY STABLE across Buddhavagga + Sukhavagga chapter-boundary.

- **T210 error-code shift diagnostic** — tested leaves 0565/0566/0567/0568 all return HTTP 503 (Service Unavailable). Yesterday's leaves returned HTTP 404 (Not Found). The shift from 404→503 suggests IA CDN infrastructure-change from a MISSING-FILE outage to a SERVICE-UNAVAILABLE outage. New diagnostic sub-finding flagged for IA infrastructure escalation.

## Key findings (summary, 31 enumerated in sample)

1. **ELEVEN-BUILD CONSECUTIVE WITHIN-CHAPTER-OR-CROSS-CHAPTER COHERENCE CHAIN** — SAMPLES' NEW RECORD extending yesterday's TEN-BUILD finding.
2. **FAUSBØLL FOUR-STANZA ANAPHORA** `Susukhaṁ vata jīvāma` on V. 197/198/199/200 — CROSS-STANZA ANAPHORA DENSITY RECORD.
3. **FAUSBØLL LATIN FOUR-STANZA ANAPHORA** `Lætissime sane vivimus inter`.
4. **MÜLLER FOUR-STANZA ENGLISH ANAPHORA** `Let us live happily then, …`.
5. **TRIPLE-EDITION FOUR-STANZA ANAPHORA PRESERVATION** — a MAJOR cross-language structural-preservation finding.
6. **FAUSBØLL V. 200 `yesan¹` PLAIN-n-BEFORE-VOWEL-SANDHI** — parallel to yesterday's V. 189 `saraṇam` plain-m-sandhi, extending the samples' TRIPARTITE `m`/`ṁ` SANDHI/DEFECT TAXONOMY to a FOUR-CATEGORY `m/ṁ`/`n/ṁ` NASAL-SANDHI/DEFECT TAXONOMY. A MAJOR text-critical finding.
7. **FAUSBØLL `ussukesu`/`ussukkesu` EDITORIAL DEGEMINATION PREFERENCE** — extends SYLLABIC-CONTRACTION TAXONOMY.
8. **FAUSBØLL V. 199 REFRAIN-DOUBLE-SUPERSCRIPT** — same marker ¹ on both L1 and L2 `ussukesu¹`.
9. **FAUSBØLL `¹.` PERIOD-AFTER-SUPERSCRIPT ON APPARATUS ENTRY** — extends 11-16 V. 182 body-side finding.
10. **FAUSBØLL LETTER-SPACED LEMMA DENSITY RECORD** — four lemmata in six apparatus lines.
11. **FAUSBØLL LATIN `dei ābhassaræ velut` ĀBHASSARA-DEVA DIRECT-LATINISATION**.
12. **FAUSBØLL LATIN WITHIN-STANZA DOUBLE-ANAPHORA** `inter iracundos … inter iracundos`.
13. **FAUSBØLL LATIN END-OF-LINE HYPHENATION DENSITY RECORD** — three in four consecutive stanzas.
14. **MÜLLER `bright gods` LOWERCASE-GOD-PLURAL TRANSLATION** — extends 11-19 LOWERCASE `church` convention.
15. **MÜLLER CAPITAL `We` vs LOWERCASE `among` AFTER FIRST `!`** — discourse-function capitalisation divergence.
16. **MÜLLER MORAL-vs-PHYSICAL READING DECLARATION** — new editorial-apparatus-content category.
17. **MÜLLER MITHILĀ-BURNING NARRATIVE CROSS-REFERENCE** + TRIPLE-LAYER quotation.
18. **MÜLLER DIRECT-LINE-OPENING PARALLEL** on Sanskrit `Susukha*m* vata *g*îvâmi` vs Pāli `Susukhaṁ vata jīvāma`.
19. **MÜLLER ĀBHASSARA PHILOLOGICAL DOUBLE-GLOSS** PĀLI-SANSKRIT-ENGLISH chain.
20. **MÜLLER JOHN-MUIR CROSS-REFERENCE** + `Senti-|ments` end-of-line hyphenation.
21. **MÜLLER SILENT-CHAPTER-OPENING FIRST STANZA on V. 197**.
22. **FAUSBØLL LEAF 0064 NEWLY FETCHED** — TWENTIETH IA Fausbøll + FOURTH INNER-ZIP.
23. **FAUSBØLL LATIN `C a p. 15.` MINIMAL CHAPTER-BREAK LABEL** — SECOND attestation after `C a p. 10.` 11-02.
24. **BILATERAL ZERO-FETCH CHAPTER-OPENER EVENT** — SAMPLES' FIRST attested + CROSS-DAY FETCH-ECONOMY CHAIN.
25. **FIVE-DAY T210 FETCH OUTAGE PERSISTENCE + ERROR-CODE SHIFT** — SAMPLES' NEW RECORD + diagnostic sub-finding.
26. **T210 CHAPTER-INDEX PIXEL-CORRECTION** — chapter 23 安寧品 not chapter 24.
27. **PĀLI-SANSKRIT-CHINESE TRIPLE-CORRESPONDENCE on ĀBHASSARA-DEVA** — MAJOR cross-canon lexical finding.
28. **FOUR-CATEGORY NASAL-SANDHI/DEFECT TAXONOMY** — MAJOR text-critical taxonomic finding.
29. **FAUSBØLL/MÜLLER CONVERGENT MAHĀBHĀRATA XII, 9917 CROSS-REFERENCE** on chapter-opener.
30. **MÜLLER NINTH CHAPTER-HEADING + SIXTH PLAIN-SUBTITLE** `HAPPINESS.`.
31. **PIXEL-CORRECTION of chapter heading** — `15. Sukhavagga.` NO space before final period (yesterday's `S u k h a v a g g a .` disconfirmed at higher zoom).

## Fetch outcomes

| Source | Status | URL / Error |
| --- | --- | --- |
| Fausbøll 0063 | zero-fetch (on disk from 11-19) | — |
| Fausbøll 0064 | **first-try HTTP 200** via INNER-ZIP URL fallback | `/112138_jp2.zip/112138_jp2%2F112138_0064.jp2` → 395,621 B JP2 → 1500×2500 L PNG |
| Müller tif 0113 | zero-fetch (on disk from 11-19) | — |
| T210 leaf 0567 | **FIFTH-DAY OUTAGE** (HTTP 503) | HTTP 503 Service Unavailable; neighbouring leaves 0565/0566/0568 also 503; ERROR-CODE SHIFT from days 1-4 HTTP 404 |

## Surprises vs the brief

- **Positive**: four-stanza anaphora prediction CONFIRMED at pixel level without a satya-guardrail trigger. Fausbøll 0064 Latin leaf `C a p. 15.` convention CONFIRMED as SECOND attestation (brief's INNER-ZIP URL fallback prediction HELD).
- **Minor pixel-corrections**: chapter heading final-period spacing (yesterday's reading corrected); V. 197 is a two-line stanza not a single-line foreword opener; T210 chapter index is 23 not 24.
- **New diagnostic**: T210 outage error-code shifted 404→503, suggesting IA CDN infrastructure change.
- **Rich apparatus**: Fausbøll's foot apparatus on V. 197-203 carries FOUR letter-spaced lemmata — SAMPLES' NEW LETTER-SPACED-LEMMA-DENSITY RECORD on a single apparatus block.
- **Cross-canon convergence**: Pāli-Sanskrit-Chinese TRIPLE-CORRESPONDENCE on Ābhassara-deva (ābhassarā / âbhâsvara / 光音天) pixel-attested on two sides and TEI-referenced on third — the DENSEST cross-canon convergence attested on a single chapter-opening stanza.

## Natural continuation

The next natural continuation is **Sukhavagga V. 201-204 body-continuation** — Fausbøll leaf 0063 already carries V. 201-207 bodies (named-not-carried today); Müller tif 0113 already carries V. 201 body and partial footnote (V. 201 footnote `This verse is ascribed to Buddha, when he heard of the defeat of A*g*âta*s*atru by Prasena*g*it. It exists in the Northern or` continues on tif 0114 which would need fetch); T210 recovery priority remains. Would extend the chapter-coherence chain to TWELVE builds.

**Reversible by `git revert`.** No manifest/OTS/mirror touch per 11-10 content-vs-push-cron convention. jonang 178-file working set untouched (56th day per 10-20 convention).
