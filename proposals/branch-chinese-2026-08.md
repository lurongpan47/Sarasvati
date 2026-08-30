# Sarasvatī · Chinese branch (`chinese`) — First-sample proposal

**Version:** v0.6.4 · draft
**Author:** subagent (drafted 2026-08-29, awaiting Lucy approval)
**Branch:** `chinese` — 汉传大藏经系
**Existing asset in branch:** None. This is the branch's first standalone project.

---

## ⚠️ Licence problem (must be resolved before source selection)

Sarasvatī publishes under **CC BY-SA 4.0**. Three canonical Chinese sources have three different licences:

| Source | Actual licence | Compatible with CC BY-SA 4.0? |
|---|---|---|
| **CBETA online / CBReader / GitHub XML** | CC BY-**NC**-SA 2.5 Taiwan (explicitly non-commercial; see <https://cbeta.org/en/copyright-notice>: "Not for sale · No Commercial Use Allowed") | **No.** The NC clause is a downstream restriction that CC BY-SA 4.0 rejects. Distributing CBETA text under CC BY-SA 4.0 would infringe CBETA's licence. |
| **SAT Daizōkyō Text Database (東大 SAT)** | Restrictive terms of use — academic / non-profit only, redistribution "generally prohibited" (see <https://21dzk.l.u-tokyo.ac.jp/SAT/termsofuse_en.html>). Sub-datasets (Jiaxing DB, image DB, Japanese-works collation DB) are CC BY / CC BY-SA. | **No** for the main Taishō body; **yes** for Jiaxing DB (CC BY) and Japanese-works collation DB (CC BY-SA 4.0). |
| **Printed Taishō (1924–1934), Wikisource, archive.org scans** | Original print edition: public domain in Japan (editor Takakusu Junjirō died 1945; expired ~1996 under old 50-year rule, still PD under current 70-year rule from 2018). Underlying source texts (pre-Tang, Tang, Song translations) are 700–1600 years old, PD everywhere. | **Yes.** The *typography* of a 1924 printed volume is uncopyrightable in most jurisdictions; the *text itself* has been PD for a millennium. Wikisource copies inherit PD status. |

### Three resolution paths (recommendation later)

- **Path A · SAT-source only for scholarly reference; primary source = archive.org Taishō scan or Wikisource.**
  We OCR / transcribe from the PD printed volume (or use Wikisource's PD transcription), use SAT and CBETA only under fair-quotation for cross-checking. Everything we publish is genuinely PD-derived. Cleanest legally.

- **Path B · Use only CBETA-marked "public-domain" fascicles.**
  CBETA maintains provenance metadata: some texts are marked as PD by them (typically material where the digitiser explicitly waived rights). This is a narrow subset. Requires per-text audit; slow.

- **Path C · Skip the Taishō canon entirely; use an already-PD Chinese Buddhist text with public archive.org backing.**
  Example: T.1735 《大方廣佛華嚴經疏》(Chengguan's Huayan Commentary, 738–839 CE) is textually PD; scanned reprints exist on archive.org and 中國哲學書電子化計劃 (ctext.org). Same idea for Song and Ming works (Zongjinglu, Wudeng-Huiyuan).

**Recommended path: A** (source = Wikisource / archive.org PD scan; CBETA and SAT retained as reference only, fair-use quoted).

Rationale for A: (i) it lets us tackle the *most-wanted* Chinese texts (the Āgamas) without licence contamination; (ii) it forces us to build our own transcription pipeline, which every future Sarasvatī chinese-branch project will need anyway; (iii) it produces a genuinely PD source file we can release under CC BY-SA 4.0 without any grey area.

---

## Goal of this sample

Pick **one short Chinese Buddhist text that is (a) verifiably PD in source, (b) lacks a rigorous modern English translation, (c) has cross-canon leverage (Pāli or Tibetan parallel or catalogic value)**, and produce Sarasvatī's first chinese-branch project: 中文 → English, with optional Pāli cross-reading.

Constraints:

- Public domain source path A (Wikisource / archive.org).
- Under 1500 characters of Classical Chinese (single-day human review).
- Not competing with an existing modern academic translation (i.e. not Yamamoto/Tanahashi/BDK territory).

---

## Candidate 1 · T.99 SA 262 · 《雜阿含經·闡陀經》 (Saṃyuktāgama 262 · Channa Sūtra)

- **Location:** Taishō 大正藏 vol. 2, T.99, fascicle 10 (卷第十)
- **Length:** ~950 Chinese characters
- **Content:** After the Buddha's *parinirvāṇa*, monk Channa asks Ānanda about the doctrine of no-self. Ānanda cites Kātyāyana's teaching (SN 12.15 / Kaccānagotta Sutta): *"the world is bound between existence and non-existence; the middle way avoids both."*
- **Pāli parallel:** SN 22.90 (Channa) + SN 12.15 (Kaccānagotta) — Sujato has CC0 English.
- **Sanskrit parallel:** SĀ(Skt) 301 (Turfan fragments).
- **Tibetan parallel:** Kātyāyana citation preserved in Nāgārjuna's *Mūlamadhyamakakārikā* XV.7 — a bridge into the Tibetan branch.
- **Existing English translations:** Only Anālayo's academic paper (2013, restricted access) and Bhikkhu Bodhi's SN 22.90 (Pāli-only). **No public-domain English rendering of SA 262 itself exists.**
- **Source path A verification:** T.99 was translated by Guṇabhadra (求那跋陀羅) in 435–443 CE — text is over 1500 years old, unambiguously PD. Wikisource transcription exists at <https://zh.wikisource.org/wiki/雜阿含經>. Archive.org has scanned Taishō vol. 2.
- **Target languages:** 中文 → English (primary); Pāli SN 22.90 as reference reading; Tibetan MMK XV.7 as bridge sample.
- **Why it fits:** *Genuine philological rarity* — this is one of the most-cited-by-scholars, least-publicly-translated Āgama texts. Nāgārjuna cites it; the Kaccānagotta reading is one of the roots of Mādhyamika. **Enormous cross-branch payoff.**

**Sample (~100 characters of Classical Chinese, from Wikisource transcription of T.99 fascicle 10):**

> 如是我聞：一時，佛住波羅㮈國仙人住處鹿野苑中。爾時，尊者闡陀晨朝著衣持鉢，入波羅㮈城乞食。食已，還攝衣鉢，洗足已，持戶鉤，從林至林，從房至房，從經行處至經行處，處處請諸比丘言："當教授我，為我說法，令我知法、見法，我當如法知、如法觀。"

*(Note: the precise byte-for-byte source we ship will be re-transcribed from the archive.org scan or verified against Wikisource under a source-hash manifest, not copied from CBETA.)*

---

## Candidate 2 · T.2076 《景德傳燈錄》· 卷三 · 菩提達摩章 (Jingde Chuandeng Lu · fasc. 3 · Bodhidharma entry)

- **Location:** Taishō vol. 51, T.2076, fascicle 3
- **Date:** Compiled by Daoyuan 道原, 1004 CE (Song dynasty).
- **Length:** Bodhidharma section ~1200 characters.
- **Content:** The *locus classicus* for the "wall-gazing" (面壁) Bodhidharma legend, the encounter with Emperor Wu of Liang, and the transmission of the *Laṅkāvatāra Sūtra* to Huike.
- **Pāli parallel:** None.
- **Tibetan parallel:** None direct, but Chan-Tibetan encounter texts (Bsam yas debate, 794 CE) engage the same tradition — cross-branch reading possible.
- **Existing English translations:** Whitfield & Ferguson (partial, dated), Yampolsky (adjacent texts). No modern rigorous full translation of the Bodhidharma section is in the public domain.
- **Source path A verification:** 1004 CE — unambiguously PD. Archive.org has Taishō vol. 51 scans. 中華電子佛典 CBETA has it too but we won't ship from CBETA.
- **Target languages:** 中文 → English (primary); optional bridge to Tibetan for the Chan-Tibetan encounter context.
- **Why it fits:** Historical anchor for Chan; opens the door to future Chan/Tibetan cross-readings; there is a real English-translation gap for the *literary* rather than *hagiographic* register of the Chuandeng Lu.

**Sample (~100 characters):**

> 菩提達摩者，南天竺國香至王第三子也。姓剎帝利，本名菩提多羅，後遇二十七祖般若多羅至本國，受王供養。知師密迹，因試令與二兄辯所施寶珠，發明心要。既而尊者謂曰："汝於諸法已得通量，夫達摩者，通大之義也。宜名達摩。"

---

## Candidate 3 · T.2145 《出三藏記集》· 卷一 · 胡漢譯經音義同異記 (Chu Sanzang Ji Ji · fasc. 1 · Sengyou on transliteration vs. translation)

- **Location:** Taishō vol. 55, T.2145, fascicle 1
- **Date:** Compiled by Sengyou 僧祐, ca. 515 CE.
- **Length:** The short essay ~800 characters (fits well); full fascicle is longer.
- **Content:** The earliest surviving Chinese Buddhist bibliographical / meta-translation essay. Sengyou catalogues the phonetic mismatches between Indic and Chinese Buddhist vocabulary, and articulates a theory of translation — a proto-linguistics of the Silk Road.
- **Pāli parallel:** None.
- **Tibetan parallel:** None direct, but the *Sgra sbyor bam po gnyis pa* (Tibetan translation-manual, ca. 814 CE) covers the same problem for Tibetan. **Excellent future cross-branch reading.**
- **Existing English translations:** Wang Bangwei (partial, in monographs); no free-standing PD English translation.
- **Source path A verification:** 515 CE — unambiguously PD.
- **Target languages:** 中文 → English (primary); notes-only cross-reference to *Sgra sbyor bam po gnyis pa* for the Tibetan branch.
- **Why it fits:** This is meta-canon: it's *about* translation, so it's a natural first text for Sarasvatī's own charter of translation ethics. Pairs beautifully with `charter/BUDDHIST-AI-CHARTER.md`.

**Sample (~100 characters):**

> 夫神理無聲，因言辭以寫意；言辭無跡，緣文字以圖音。故字為言蹄，言為理筌。音義合符，不可偏失。是以文字應用彌綸宇宙，雖跡係翰墨，而理契乎神。昔造書之主凡有三人，長者曰梵，其書右行；次曰佉樓，其書左行；少者蒼頡，其書下行。

---

## Recommendation

**Preferred: Candidate 3 — T.2145 Sengyou's translation-theory essay (Path A source).**

Reasoning:

1. **Self-referential fit.** Sarasvatī is a translation project; our first Chinese-canon text should be the earliest Chinese meditation on translation itself. Symbolic weight matches practical scope.
2. **Genuine gap.** No public English version.
3. **Cross-branch payoff.** Directly maps to Tibetan `Sgra sbyor bam po gnyis pa` — sets up a translation-theory reading pair across two branches.
4. **Manageable scope.** ~800 characters.
5. **Cleanest licence story.** 515 CE, uncontroversial PD.

Fallback: **Candidate 1 (SA 262)** if Lucy wants Pāli-parallel prestige over meta-canon symbolism. It is arguably more *important* doctrinally but far harder philologically (Nāgārjuna citation chains, MMK XV.7 comparison, multiple Sanskrit fragments), pushing review hours 2×.

Candidate 2 (Bodhidharma) is deferred — Chan is more of a `sinosphere`-branch anchor once we start the Japanese/Korean Chan lineage (Dōgen, Chinul).

**Licence path selected: A.** Source = Wikisource transcription verified against archive.org PD scan of Taishō. CBETA and SAT retained only as scholarly reference (fair-use quotation, not redistribution).

---

## Resource estimate (Candidate 3)

| Stage | Tokens (Anthropic Opus 4.7) | Wall time | Human hours |
|---|---|---|---|
| Transcription verification (Wikisource ↔ archive.org scan) | ~3k in / ~2k out (OCR spot-check) | 20 min | 0.25 (subagent) |
| Machine first-draft 中文 → English | ~5k in / ~4k out | 3 min | 0 |
| Notes: Silk Road linguistic context, Sgra-sbyor pointer | ~4k in / ~4k out | 3 min | 0 |
| Repo layout + markdown build | — | 20 min | 0.5 (subagent) |
| **Native-speaker human review (Classical Chinese + Buddhist Studies English)** | — | — | **3–4 hours** |
| **Total AI budget** | **~20k tokens** | ~10 min | — |
| **Total human budget** | — | — | **~4–5 hours** |

Estimated USD cost of Anthropic pipeline: **< $1**.

**For Candidate 1 (SA 262):** double the human hours (~6–8 hrs) due to Pāli/Sanskrit/Tibetan cross-references, and add a Pāli-literate reviewer to the sign-off chain.

---

## Deliverable structure (proposed, for Candidate 3)

```
translations/chinese/t2145-sengyou-fanhan/
  ├── README.md                 (branch, provenance, licence path A explained)
  ├── source-zh-classical.md    (Wikisource + archive.org verified, PD)
  ├── source-hash.txt           (SHA-256 of source-zh-classical.md)
  ├── translation-en.md         (Sarasvatī machine draft, CC BY-SA 4.0)
  ├── apparatus.md              (variants, Tibetan Sgra-sbyor cross-ref, glossary)
  └── review-log.md             (awaiting human sign-off)
```

Add events.jsonl entry only after human review sign-off.

---

## Open questions for Lucy

1. Path A confirmed as licence policy for the whole `chinese` branch going forward? (This is the biggest structural decision.)
2. T.2145 Sengyou vs T.99 SA 262 as first sample? (Sengyou = meta-canon symbolism; SA 262 = doctrinal prestige + Pāli-Tibetan bridge.)
3. Reviewer sourcing: Classical Chinese scholar (Sengyou route) vs early-Buddhism specialist (SA 262 route).
4. Do we want the transcription-verification tool (OCR + Wikisource diff) built as a reusable script now, or improvise it for the first sample and generalise later?
