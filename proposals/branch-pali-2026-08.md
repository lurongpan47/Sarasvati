# Sarasvatī · Pāli branch (`pali`) — First-sample proposal

**Version:** v0.6.4 · draft
**Author:** subagent (drafted 2026-08-29, awaiting Lucy approval)
**Branch:** `pali` — Theravāda canon
**Existing asset in branch:** DN 16 (Mahāparinibbāna Sutta) — used only for the four-language reading of the final-instructions passage. No standalone Pāli-source production yet.

---

## Goal of this sample

Pick **one short Pāli text that has never received a systematic Chinese (or Tibetan) translation of comparable philological rigor**, and produce Sarasvatī's first bona-fide Pāli-source project: Pāli → Simplified Chinese, with English cross-check and (stretch) Tibetan.

Constraints:

- Public domain / open-license only.
- Under 500 Pāli words (single sitting, low review cost).
- Has a genuine gap in modern Chinese scholarship (not Dhammapada, not Mettā Sutta, not the standard "Sangha-favourite" suttas that already have 5+ Chinese renderings).
- Ideally has a Chinese-canon parallel (SA/EA/MA) so we can *contrast* rather than duplicate.

---

## Source & licence

**SuttaCentral** (<https://suttacentral.net>) — Mahāsaṅgīti Tipiṭaka Buddhavasse 2500 (MS) edition of the Pāli root.

**Bilara data repository**: <https://github.com/suttacentral/bilara-data>

**Licence (verified 2026-08-29 via `_publication.json` metadata and SC repo README)**:

> "It is dedicated to the public domain via Creative Commons Zero (CC0)."

CC0 is fully compatible with Sarasvatī's CC BY-SA 4.0 output licence: we can copy, adapt, and redistribute the Pāli root without restriction. Attribution to the MS edition is retained as a matter of scholarly courtesy, not legal obligation.

Reference English translation (Bhikkhu Sujato, 2020–2021) is also CC0 and can be shown side-by-side.

---

## Candidate 1 · Ud 1.1 · *Paṭhamabodhisutta* (第一菩提經 / "Upon Awakening, 1st")

- **Location:** Khuddaka Nikāya · Udāna · Bodhivagga 1
- **Length:** ~140 Pāli words (prose narration + one 4-line udāna verse)
- **Content:** The Buddha, in the first week after awakening at the Bodhi tree, contemplates dependent origination *anuloma* (forward), then utters an udāna verse.
- **Chinese parallels:** No direct T-number equivalent. Fragments of dependent-origination formulae appear across SA/MA but no single Chinese sūtra corresponds to the Bodhivagga structure. **This is a real gap.**
- **Tibetan parallels:** None known (Udāna as a book was never fully Tibetanised; only excerpts via *Udānavarga*, and Ud 1.1's specific *paṭicca-samuppāda anuloma* frame is not there).
- **Target languages:** Pāli → Simplified Chinese (primary); English (cross-check via Sujato CC0); Tibetan draft (stretch).
- **Existing Chinese translations:** None systematic. 元亨寺《漢譯南傳大藏經》has a rendering, but it is under active copyright (Taiwan, ~1990s), and its quality has been widely criticised. So the field is effectively open.
- **Why it fits:** *Short, canonical, philosophically dense (paṭicca-samuppāda formula), narrative frame, has verse and prose, and there is no unencumbered modern Chinese version.* Perfect first-sample scope.

**Sample (100-word Pāli excerpt, verbatim from bilara-data `ud1.1_root-pli-ms.json`):**

> Evaṁ me sutaṁ—ekaṁ samayaṁ bhagavā uruvelāyaṁ viharati najjā nerañjarāya tīre bodhirukkhamūle paṭhamābhisambuddho. Tena kho pana samayena bhagavā sattāhaṁ ekapallaṅkena nisinno hoti vimuttisukhapaṭisaṁvedī. Atha kho bhagavā tassa sattāhassa accayena tamhā samādhimhā vuṭṭhahitvā rattiyā paṭhamaṁ yāmaṁ paṭiccasamuppādaṁ anulomaṁ sādhukaṁ manasākāsi: "Iti imasmiṁ sati idaṁ hoti, imassuppādā idaṁ uppajjati, yadidaṁ—avijjāpaccayā saṅkhārā, saṅkhārapaccayā viññāṇaṁ, viññāṇapaccayā nāmarūpaṁ, nāmarūpapaccayā saḷāyatanaṁ, saḷāyatanapaccayā phasso, phassapaccayā vedanā, vedanāpaccayā taṇhā, taṇhāpaccayā upādānaṁ, upādānapaccayā bhavo, bhavapaccayā jāti, jātipaccayā jarāmaraṇaṁ sokaparidevadukkhadomanassupāyāsā sambhavanti."

---

## Candidate 2 · Iti 1 · *Lobhasutta* (貪經 / "Greed")

- **Location:** Khuddaka Nikāya · Itivuttaka · Ekakanipāta · Paṭhamavagga 1
- **Length:** ~80 Pāli words (short prose frame + 6-line verse)
- **Content:** "Abandon this one thing — greed — and I guarantee non-return." Bhagavā's declaration, verse restatement.
- **Chinese parallels:** T.765《本事經》(Ireland-Tokiwai style), Xuanzang's translation of *Itivṛttaka*, does correspond fascicle-by-fascicle but is 7th-century literary Chinese; no modern vernacular Chinese version exists in the public domain.
- **Tibetan parallels:** None as a book.
- **Target languages:** Pāli → Modern Simplified Chinese (compare with T.765 Xuanzang); English (Sujato CC0).
- **Why it fits:** Extremely short (perfect first attempt); has a Chinese parallel we can juxtapose (educational, not duplicative); the Chinese parallel is Xuanzang so we're not competing with any modern translator.
- **Risk:** Almost *too* short — the philological payoff per unit effort is lower than Candidate 1.

**Sample (verbatim from bilara-data `iti1_root-pli-ms.json`):**

> Vuttañhetaṁ bhagavatā vuttamarahatāti me sutaṁ: "Ekadhammaṁ, bhikkhave, pajahatha; ahaṁ vo pāṭibhogo anāgāmitāya. Katamaṁ ekadhammaṁ? Lobhaṁ, bhikkhave, ekadhammaṁ pajahatha; ahaṁ vo pāṭibhogo anāgāmitāyā"ti. Etamatthaṁ bhagavā avoca. Tatthetaṁ iti vuccati: "Yena lobhena luddhāse, sattā gacchanti duggatiṁ; Taṁ lobhaṁ sammadaññāya, pajahanti vipassino; Pahāya na punāyanti, imaṁ lokaṁ kudācanan"ti. Ayampi attho vutto bhagavatā, iti me sutanti.

---

## Candidate 3 · Snp 4.1 · *Kāmasutta* (欲經 / "Sense-pleasures") — Aṭṭhakavagga opening

- **Location:** Khuddaka Nikāya · Sutta Nipāta · Aṭṭhakavagga 1
- **Length:** ~80 Pāli words · 6 gāthās
- **Content:** The desire-verses that open the archaic Aṭṭhakavagga — one of the earliest strata of the Pāli canon, linguistically distinct (metrical, Old Pāli).
- **Chinese parallels:** T.198《義足經》(Zhi Qian, 3rd c. CE) is a full Chinese Aṭṭhakavagga — extremely archaic literary Chinese, a philological treasure but almost unreadable to modern readers.
- **Tibetan parallels:** Fragmentary via Nāgārjuna quotations; no full Tibetan version.
- **Target languages:** Pāli → Simplified Chinese (compare with T.198); English (Sujato CC0).
- **Why it fits:** This is the **most philologically important** of the three — the Aṭṭhakavagga is pre-sectarian material older than most of the Nikāyas. A rigorous modern Chinese rendering is genuinely absent.
- **Risk / cost:** Old-metre Pāli is harder. Human reviewer must be Sutta Nipāta–competent. Estimate +40% review time vs. Candidate 1.

**Sample (verbatim from bilara-data `snp4.1_root-pli-ms.json`):**

> Kāmaṁ kāmayamānassa, tassa ce taṁ samijjhati; Addhā pītimano hoti, laddhā macco yadicchati. Tassa ce kāmayānassa, chandajātassa jantuno; Te kāmā parihāyanti, sallaviddhova ruppati. Yo kāme parivajjeti, sappasseva padā siro; Somaṁ visattikaṁ loke, sato samativattati. Khettaṁ vatthuṁ hiraññaṁ vā, gavāssaṁ dāsaporisaṁ; Thiyo bandhū puthu kāme, yo naro anugijjhati. Abalā naṁ balīyanti, maddantenaṁ parissayā; Tato naṁ dukkhamanveti, nāvaṁ bhinnamivodakaṁ. Tasmā jantu sadā sato, Kāmāni parivajjaye; Te pahāya tare oghaṁ, Nāvaṁ sitvāva pāragūti.

---

## Recommendation

**Preferred: Candidate 1 — Ud 1.1 Paṭhamabodhisutta.**

Reasoning:

1. **True gap.** No public-domain modern Chinese exists; the Bodhivagga narrative frame has no Chinese parallel.
2. **Doctrinal density.** The full 12-fold *paṭicca-samuppāda anuloma* is a keystone formula that shows up everywhere else — good "seed vocabulary" for later Pāli projects.
3. **Balanced form.** Prose narration + verse: exercises both registers in the first sample.
4. **Right length.** ~140 words fits a single translator's session, ~1500 tokens total pipeline cost.
5. **Sujato CC0 English** available for immediate machine cross-check.

Fallback: Candidate 3 (Snp 4.1) if Lucy wants to prioritise the philologically-oldest stratum first. Candidate 2 is a "warm-up" option — cheap but arguably too small to justify a review cycle.

---

## Resource estimate (Candidate 1)

| Stage | Tokens (Anthropic Opus 4.7 or Sonnet) | Wall time | Human hours |
|---|---|---|---|
| Machine first-draft Pāli → 中文 (Opus 4.7, thinking on) | ~4k in / ~3k out | 3 min | 0 |
| English cross-check pass against Sujato CC0 | ~3k in / ~2k out | 2 min | 0 |
| Tibetan stretch draft | ~4k in / ~3k out | 3 min | 0 |
| Notes + apparatus (variants, references) | ~5k in / ~4k out | 5 min | 0 |
| Repo layout + markdown build | — | 15 min | 0.25 (subagent) |
| **Native-speaker human review (中文, Pāli-literate)** | — | — | **2–3 hours** |
| Optional Tibetan review | — | — | 1–2 hours |
| **Total AI budget** | **~25k tokens** | ~15 min | — |
| **Total human budget** | — | — | **~3–5 hours** |

Estimated USD cost of Anthropic pipeline: **< $1** at Opus 4.7 rates.

---

## Deliverable structure (proposed)

```
translations/pali/ud1.1-pathamabodhisutta/
  ├── README.md            (branch + provenance + licence)
  ├── source-pali.md       (bilara MS root text, verbatim, CC0)
  ├── source-english.md    (Sujato 2021 CC0)
  ├── translation-zh.md    (Sarasvatī machine draft, CC BY-SA 4.0)
  ├── translation-bo.md    (stretch)
  ├── apparatus.md         (variants, PTS refs, cross-canon parallels)
  └── review-log.md        (empty until human reviewer signs)
```

Add corresponding events.jsonl entry only *after* human review sign-off, per Sarasvatī's "AI first-draft, human final" principle.

---

## Open questions for Lucy

1. Ud 1.1 vs Snp 4.1 as first sample? (Ud 1.1 recommended for scope; Snp 4.1 recommended for philological weight.)
2. Do we commit to producing a Tibetan draft in the first sample, or defer that to the tibetan-branch's own pipeline?
3. Reviewer sourcing: use `CALL-FOR-HELP.md` to recruit, or approach a known Theravāda-Chinese scholar directly?
