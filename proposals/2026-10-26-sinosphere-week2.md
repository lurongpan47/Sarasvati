# Weekly Branch Proposal · 2026-10-26 · Sinosphere (汉字文化圈), Week 2

**Branch:** `sinosphere` · Korea / Japan / Vietnam strand
**Status:** second cycle (week 1 was 2026-09-07, Wŏnhyo *Daeseung Gisillon So* prologue, 3-lang)
**Selected from:** Han'guk Pulgyo chŏnsŏ (HPC); CBETA Taishō / X / HPC digital corpus; acmuller.net Collected Works of Korean Buddhism (DDB)

## Candidates (3)

### 1. **Preferred — Wŏnhyo, *Balsim suhaeng jang* 發心修行章 (Awaken Your Mind and Practice), opening passage**
- **Author / date:** attributed to Wŏnhyo (元曉, 617–686), Silla Korea; also independently in Chosŏn Haeinsa (1883) and Weoljeongsa (1574) blocks.
- **Length:** full text ~700 characters (one HPC column, 841a–841c); opening passage targeted here ≈ 150 characters (4 couplets, 8 pādas).
- **Public-domain evidence:** author died 686 CE; the text itself is PD worldwide. Preserved in HPC vol. 1 pp. 841a–841c (Dongguk UP 1979, derived from the 1883 Haeinsa woodblock print). CBETA digital edition in HPC_W0019.
- **Target languages missing:** **Modern Chinese vernacular** — only classical Hanmun; **Tibetan** — never rendered; **English PD** — the Muller 2016 online translation is copyrighted CC-BY-NC; no PD English exists. (This file's English, Chinese, and Tibetan columns are therefore all machine drafts ⟨བརྟག⟩.)
- **Why it matters:** the canonical Chosŏn-era śrāmaṇera curriculum text, read for 450+ years as part of the *Cho balsim jagyeong mun* 初發心自警文 trio (with Jinul's *Gye chosim hag-in mun* and Yaun's *Jagyeong mun*). The clearest short Wŏnhyo text for 4-language parallel reading — a natural charter-style companion to DN 16 and the Dhammapada Yamakavagga.

### 2. Alt — Nichiren, *Risshō Ankoku Ron* 立正安國論 (1260) opening memorial
- Nichiren (日蓮, 1222–1282), Kamakura Japan. T.2688 and Nichiren canonical collections. Opening dialogue frame (客来嘆曰 …) ≈ 300 chars. Masaharu Anesaki, *Nichiren, the Buddhist Prophet* 1916 (IA `in.ernet.dli.2015.68435`, PD) contains partial PD English quotations. Scan path exists; risk: Anesaki's rendering is paraphrase + selected quotation, not line-for-line.
- Target gaps: Modern Chinese vernacular, Tibetan, Korean modern.

### 3. Alt — Kūkai, *Sangō Shiiki* 三教指歸 (797), preface
- Kūkai (空海, 774–835), Heian Japan. Taishō vol. 56; the preface is Kūkai's own apologetic framing of Buddhism, Confucianism, Taoism. ~400 chars. No PD English (Hakeda 1972 abridgement copyrighted). Scan on IA via Dai Nippon zokuzōkyō / SAT.

## Resource estimate (candidate #1, *Balsim suhaeng jang* opening passage)

| Item | Estimate |
|---|---|
| Source acquisition (CBETA HPC digital, scan unavailable this session) | 15 min |
| AI first-draft (Hanmun → EN + zh-Hans + Tibetan) | ~5k tokens in / ~20k out, ≈ $1–2 |
| Expert review (Yogācāra / Silla Korean / Chosŏn Buddhist studies) | 4–6 h, 1 reviewer |
| Formatting + attestation footer (scan-first methodology erratum: Hanmun = digital text, not scan this session) | 1 h |
| **Total to v0.x sample release** | **~$2 + ~6 h human** |

## Scan honesty note

Unlike the Dhammapada / Ashoka / Vajracchedikā samples (where source + English columns are both from PD scans opened in-session), the HPC scans at kabc.dongguk.edu are behind a dynamic viewer and I could not open leaf 841 this session. The Hanmun column is therefore from **CBETA's digital transcription of HPC vol. 1 pp. 841a–841c (HPC_W0019)**, traceable but not image-attested. English/Chinese/Tibetan all `⟨བརྟག⟩` drafts. The sinosphere branch's week-1 sample (`wonhyo-prologue/daeseung-gisillon-so-prologue-3lang.md`, 2026-09-07) was built the same way; this file documents the limit explicitly in its header. A future reviewer with HPC vol. 1 physically open can promote the Hanmun column to `attested`.

## Under 09-21 auto-approve rule

Pan's WhatsApp 2026-09-21 13:46 PDT: 「请自动approve 这个问题不要再问我」. This proposal is written and candidate #1 is built in the same session; the sample file lives at `translations/wonhyo-prologue/balsim-suhaeng-jang-opening-4lang.md`. All reversible via `git revert`.
