# CHANGELOG · Sarasvatī

All notable changes to this project will be documented here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning: SemVer.

## [Unreleased] — 2026-09-23

### Fixed — Erratum: SE Asia branch Sn 1.8 — neither the "PTS" Pāli nor the "Chalmers 1932" English was that text (retroactive scan check #5, satya + asteya correction)

Fifth item of the standing 09-18 audit queue. `translations/karaniya-metta-sutta/Sn1.8-4lang.md` (SE Asia branch first sample, added 2026-09-13 as `ca3fb61`) was re-read against two Internet Archive scans at full resolution, cropped and enlarged 2–6× for diacritics and footnote numerals: **PTS Sutta-Nipāta, Andersen & Smith 1913**, item `in.ernet.dli.2015.343993`, leaves n39 (= p. 25, vv. 143–146 + nn. 1–19) and n40 (= p. 26, vv. 147–152 + nn. 1–14, colophon); **Chalmers, *Buddha's Teachings* (HOS 37, 1932)**, item `buddhasteachings032310mbp`, leaves n67 (= p. 36, Pāli stanzas 1–7), n68 (= p. 37, "Sutta 8. Goodwill", [143]–[149]), n69 (= p. 38, Pāli 8–10), n70 (= p. 39, [150]–[152]). Findings, all corrected in the file with an erratum table at the top:

1. **The English column was not Chalmers.** Chalmers renders the Sutta-Nipāta in short unrhymed verse; his Sn 1.8 begins "When Peace is won, th' adept / in welfare needs to prove / an able, upright man" and ends "shall never see rebirth." The file's prose ("This is what should be done by one who is skilled in good, and who wishes to attain that state of Peace …") shares no line with it. It was a modern chanting-book-type rendering of unidentified provenance — removed on both satya and asteya grounds (such renderings are generally in copyright). Column replaced by Chalmers' 46 lines verbatim with his line breaks, marginal verse numbers and page numbers (pp. 37, 39).
2. **The Pāli column was not PTS 1913.** It was the Burmese Sixth-Council (CST/VRI) recension as it circulates online: joined sandhi (`Karaṇīyamatthakusalena`, `cassa`, `yāvatāssa`, `brahmametaṃ vihāramidhamāhu`), `suhujū`, `khuddamācare`, `sabbasattā`, `vanavasesā`, `yeva adiṭṭhā`, `Byārosanā`, `katthaci na kañci`, `sabbalokasmi`, `vinaya gedhaṃ`, `jātuggabbhaseyya puna reti`. In five of those places the old column printed what Andersen & Smith relegate to the apparatus as the Bⁱ (Burmese) variant (`suhuju`, `kulesv-`, `sabbasattā`, `ye va`, `vinaya`). Column replaced by the PTS text verbatim — `Karaṇīyam atthakusalena`, `ujū ca sūjū ca`, `c' assa mudu`, `khuddaṃ samācare`, `sabbe sattā`, `vā anavasesā`, `ye vā addiṭṭhā`, `nâtimaññetha katthacinaṃ kañci`, `vyārosanā`, `sabbalokasmiṃ`, `averaṃ asapattaṃ`, `yāvat' assa`, `brahmam etaṃ vihāraṃ idha-m-āhu`, `vineyya`, `gabbhaseyyaṃ punar etī ti`, colophon `METTASUTTAṂ NIṬṬHITAṂ.` — with the anusvāra as ṃ, the circumflex sandhi marks, the editors' right-margin stanza numbers, the `[F. 27]` marginal mark, and all 33 footnotes of the apparatus (sigla Bᵃ Bⁱ Cᵏ Cᵇ, Fsb.) carried under the verses.
3. **Copyright (asteya).** The file had asserted Chalmers 1932 "public domain" without basis for the US. Searched the Stanford Copyright Renewal Database (author "Chalmers": 74 renewals, none his; title "Buddha's teachings": only Burtt 1955; "Sutta", "Nipata": none; "Harvard oriental series": HOS 38–39, Visuddhimagga 1950, a Semitic Series volume — no HOS 37) and the CCE Third Series renewal volumes for 1959 Jan–Jun / Jul–Dec and 1960 Jan–Jun / Jul–Dec (Project Gutenberg #11819–11822): **no renewal found**. Sources line and License section now say exactly that (PD in life + 70 jurisdictions since 2009, d. 1938; US: no renewal found, so kept; if a renewal surfaces the column is to be replaced by Fausbøll 1881, SBE 10, IA `mlbd.dhammapadasuttni0000fmax`). Negative search, not a certificate — stated as such.
4. Chinese, Burmese and Thai drafts **unchanged**: none of the Pāli differences alters the sense, and the drafts were rendered from the Pāli, not from the removed English. Flagged as drafted against the superseded columns; all ⟨བརྟག⟩ markers kept.
5. Chalmers' own facing Pāli (pp. 36, 38) read and noted where it differs from PTS (ṁ dot-above, `uju ca sūjū ca`, `mudū`, quotation marks around `'brahmam etaṁ vihāram'`, `punar eti.`), but not used as the column.

Reading method (satya): `image` over the full-resolution leaves in half-page strips, then 2–6× crops for every disputed letter: `sūjū`/`sūju` (three reads of the Chalmers leaf split 2 : 1; the PTS leaf read `sūjū` twice and its n. 5 confirms the long vowels), `katthacinaṃ` one word vs two (two reads agree: one word), footnote **⁹** and **¹³** each standing on two words on p. 26 (re-read at 4×, same digit both times — taken as the editors' reuse of one note), the combined siglum **Bᵃⁱ** (very small type; listed as a hard case), dot-below anusvāra (two reads, one hedged). Hard cases are listed in the file's review section for a Pāli scholar. OCR (`_djvu.txt`/`_djvu.xml`) was used only to find the leaf numbers; nothing in either column comes from OCR or memory.

Score for the audit queue: **5 of 5 "attested" source columns checked so far were not what they claimed** (Udānavarga 09-18, Gāndhārī 09-20, REXII 09-21, REXIII 09-22, Sn 1.8 09-23). Remaining: T389 → Wŏnhyo prologue; then new content. ROADMAP § SE Asia updated. Page images and crops stay local in `.scratch/chalmers/` and `.scratch/pts-sn/` (gitignored). Manifest/OTS untouched — rides the next daily cycle.

### Verified — Bitcoin confirmation of the 2026-09-22 rolling stamp (all four calendars); all nine mirrors in sync

`manifests/SHA256SUMS.ots` over the tree at `9cdcf3c` (239 entries, incl. the REXIII Kālsī erratum; manifest sha256 `e9a1a2b5…`) upgraded via `scripts/ots_upgrade_watch.sh` and confirmed in Bitcoin blocks **968170** (alice.btc.calendar.opentimestamps.org) / **968184** (finney.calendar.eternitywall.com) / **968188** (bob.btc.calendar.opentimestamps.org) / **968193** (btc.calendar.catallaxy.com) — the first rolling stamp since 09-14 on which all four calendars have landed. Committed as `3839901`. The manifest recipe (`git ls-files` minus the three rolling manifest files, `./`-prefixed, sha256, C-sorted) was re-run: it reproduces the committed manifest except for the three files changed by `dced561` (BDRC/BUDA source note: `CALL-FOR-HELP.md`, `ROADMAP.md`, `decisions/2026-09-22.md`), which had deliberately been left for this cycle. `manifests/SHA256SUMS` sha256 `e9a1a2b5…` matched on all nine AWS mirrors (`aws-quant` `aws-biotech` `aws-disease` `aws-upaix-base` `aws-materialai` `aws-216-16` `aws-fund-bot` `aws-polymarket-eu` `aws-chemist-eu`). No archive content changed. Manifest regenerated for the `dced561` files + this note + `decisions/2026-09-23.md` and re-stamped; the confirmed proof preserved as `manifests/SHA256SUMS.pre-2026-09-23.ots.bak` (gitignored, local). Mirrors re-synced after the commit.

## [Unreleased] — 2026-09-22

### Fixed — Erratum: India branch REXIII (Kālsī) Prakrit column was a composite, page references wrong, lacunae filled with invented words (retroactive scan check #4, satya correction)

Fourth item of the standing 09-18 audit queue. `translations/ashoka-edicts/major-rock-edict-XIII-4lang.md` (India branch second sample, added 2026-09-15 as `bf45e3d`, both source columns labelled "Hultzsch 1925") was re-read against the Internet Archive page images of E. Hultzsch, *Inscriptions of Asoka* (CII I, Oxford 1925; item `InscriptionsOfAsoka.NewEditionByE.Hultzsch`, leaves n181–n188 = pp. 43–49 plus the unnumbered plate facing p. 44) at full resolution (~5900 × 8100 px, cropped and enlarged to letter level for the diacritics). Findings, all corrected in the file with an erratum table at the top:

1. **Page references were wrong.** The file claimed "Prakrit pp. 44–46, transliteration from the plate on p. 45; English pp. 46–49". Hultzsch prints Kālsī XIII as Devanāgarī text on pp. 43 (l. 35, heading THIRTEENTH ROCK-EDICT: KALSI) – 45 (top), **Roman transliteration on pp. 45–46** (east face ll. 35–39; "B.—South Face of Kālsī Rock" ll. 1–18), and the **translation on pp. 47–49**. There is no plate on p. 45; the only plate is an unnumbered photographic leaf captioned "KALSI ROCK; EAST FACE — PAGE 44 — SCALE ONE-SIXTH", which is not a transliteration source. Every section heading now carries the right page and rock-line numbers.
2. **Prakrit column was a normalised composite in a convention Hultzsch does not use** (IAST *ṣ*, *ṃ*, *ṇ*, *ñ* for his *sh*, *ṁ*, *n*): `pāṇa` → `pāna`, `shamaṇa` → `shama` (n. 12 "Read *shamanā*" had been printed as text), `ladheshu` → `ladhesha` (n. 6 emendation printed as text), `maraṇa` → `malane`, `apavāhe` → `apavahe`, `vijinamāne` → `vijinamane`, `mate` → `maṭe` (B, K), `agabhūti-shushuṣha … galu-shushuṣha` → `a[gabhu]ṭ[i]-shushushā … galu-shushā` (n. 15), `sahāya-ñātikeṣu` → `shahāya-nātikeshu`, `dāsa-bhaṭakaṣhi śamya-paṭipati diḍha-bhattitā` → `dāśa-bha[ṭa]kash[i sha]m[y]ā-paṭipati diḍha-bhatitā`, `avipahīne` → `avipahine`, `pāpuṇāta` → `pāpunāta`, `Kaliṅgya` → `Kaligyā`, `Tulamāye … Alikyaśudale … Choda-Pāṃḍiya avaṃ Tāmbapaṃṇiya` → `Tulamaye … Alikyashudale … Choḍa-Paṁḍiyā avaṁ Taṁbapaṁniyā`, `mānatu` → `manatu`, `vijayatavya` → `vijayataviya`. Every square bracket (damaged/supplied akṣaras) had been silently closed and the rock's divider strokes dropped. **Three passages contained words that stand on no rock:** (P) `mukhya-mute` (Kālsī has `mu` followed by a lacuna, which Hultzsch's translation also shows as dots); (Q) `hida cha` (n. 5 "Restore *°piyasa hida cha*") and `Yona-lājā` (n. 7 "Restore *-lājā*") printed as text, `param cha tena` for the rock's `[pa]laṁ chā tenā`; (I) `shaveshu manuśyeshu` for Hultzsch's `sh[a]va-manu[shāna]ṁ`; (X) `chalambu-daṃḍatā` for `chā la | hu-daṁḍatā` (a stray divider stroke on the rock; n. 21 "Cancel the sign of punctuation and join *lahu-*"). The column is now Hultzsch's Roman rows verbatim with his 29 + 23 footnotes carried where they fall in these passages.
3. **English column** was close but not verbatim: "Devānāṃpriya" → "Dēvānāṁpriya"; (A)(C)(D) "Kaliṅgas" → "Kaliṅgyas" (Hultzsch keeps the rock's *-gy-* there and writes "Kaliṅgas" only in K); (P) the lacuna dots "But this . . . . . by Dēvānāṁpriya" had been removed and a gloss "[dhamma-vijaya]" inserted that is not his; (Q) "both [here]" (his brackets), "four—4—kings", "Makā", "Alikyashudala", "Chōḍas". Sentence letters added; Hultzsch's translation footnotes (p. 47 nn. 1–9, p. 48 nn. 1–8, p. 49 nn. 2–3) carried.
4. **Section labels** (A)–(B) / (C)–(F) / (G)–(I) / (K) / (P)–(Q) / (X) were already Hultzsch's letters — the one thing the 09-15 file got right — and are kept.
5. **Recension and historical notes** corrected: Kālsī is not "the fullest complete recension" (south-face ll. 1–4 largely lost, sentences L–N missing, O–P fragmentary); Hultzsch's brackets are his own supplements, not "readings supplied from Shāhbāzgaṛhī or Girnar"; "damaged even in antiquity" (Girnar) and "Erragudi" as a Hultzsch source removed (Yerragudi was found after 1925); "Kharoṣṭhī variant *agrabhūti*" → Hultzsch's *agrabhuṭi* / Skt. *bhṛiti* (p. 47 n. 4); Hultzsch's "more probably, Alexander of Corinth" recorded. All marked as editorial, not from the scan.
6. Chinese and Tibetan drafts: only the two clauses that rendered the invented `mukhya-mute` ("所最重者" / "གཙོ་བོར་མཛད་པ") were changed, to mark the lacuna; both columns remain ⟨བརྟག⟩ and are flagged as drafted against the 09-15 text.

Reading method (satya): the `image` tool over the full-resolution leaves, cut into half- and third-width strips and 1.5–2× enlargements; letters where two passes disagreed (`maṭe`/`mate`, `[ya]`/`[va]`, `pāśaṁḍa`/`pāshaṁḍa`, `ladhesha`/`ladheshu`, `manatu`/`mānatu`, `shamanā`/`shamana`) were re-read from a tight crop against neighbouring plain letters on the same line before being accepted; the residual hard cases are listed for the epigraphist in the file's review section. The Devanāgarī block was not transcribed (the Roman rows make it unnecessary). Nothing in the Prakrit column comes from memory or from the OCR layer.

Score for the audit queue: **4 of 4 "attested"/"verbatim" source columns checked so far were not what they claimed** (Udānavarga 09-18, Gāndhārī 09-20, REXII 09-21, REXIII 09-22). Remaining, in order: Chalmers 1932 (Sn 1.8, `translations/karaniya-metta-sutta/Sn1.8-4lang.md`) → T389 → Wŏnhyo prologue; then new content (Pāli Yamakavagga 1–4 with Fausbøll / SBE X open). ROADMAP § 1 updated. `.gitignore` now excludes `.scratch/` (the downloaded page images and crops stay local). Manifest regenerated (+`decisions/2026-09-22.md`) and re-stamped; the morning stamp preserved as `manifests/SHA256SUMS.pre-2026-09-22b.ots.bak` (gitignored, local).

### Verified — Bitcoin confirmation of the 2026-09-21 rolling stamp; all nine mirrors in sync

`manifests/SHA256SUMS.ots` over the tree at `e846340` (238 entries, incl. the Lokanīti sample) upgraded via `scripts/ots_upgrade_watch.sh` and confirmed in Bitcoin blocks **968053** (alice.btc.calendar.opentimestamps.org) / **968054** (bob.btc.calendar.opentimestamps.org) / **968085** (btc.calendar.catallaxy.com); finney.calendar.eternitywall.com still pending. Committed as `8c6e44f`. The manifest recipe (`git ls-files` minus the three rolling manifest files, `./`-prefixed, sha256, C-sorted) was re-run and reproduced `manifests/SHA256SUMS` byte-for-byte; `shasum -c` passed on all 238 entries. `manifests/SHA256SUMS` sha256 (`9ae44e54…`) matched on all nine AWS mirrors (`aws-quant` `aws-biotech` `aws-disease` `aws-upaix-base` `aws-materialai` `aws-216-16` `aws-fund-bot` `aws-polymarket-eu` `aws-chemist-eu`). No content changed. Manifest regenerated for this note + `decisions/2026-09-22.md` and re-stamped; the confirmed proof preserved as `manifests/SHA256SUMS.pre-2026-09-22.ots.bak` (gitignored, local).

## [Unreleased] — 2026-09-21

### Added — SE Asia branch: Lokanīti ch. 1 Paṇḍitakaṇḍa (VRI CST + Gray 1886)

`translations/lokaniti/lokaniti-01-panditakanda-4lang.md` — first archive sample of a text **composed in** Southeast Asia (Burmese Pāli nīti literature), as approved by Pan 2026-09-21 (candidate A of `proposals/2026-09-21-seasia-week1.md`). All 40 gāthās of the *Paṇḍitakaṇḍa* ("The Wise Man"):

- **Pāli**: VRI Chaṭṭha Saṅgāyana CST Roman, re-keyed from the XML (`cscd/e1005n.nrf0.xml`) by `rend` attribute, verbatim — VRI's hyphenated compounds, Sanskritisms (`putra`, `satru`), the six-pāda v. 3 and five-line v. 19 are kept; only runs of spaces collapsed. Nothing emended.
- **English**: James Gray, *Ancient Proverbs and Maxims from Burmese Sources; or, the Nīti Literature of Burma* (Trübner 1886), stt. 1–40, pp. 1–10 — public domain. Taken from the IA OCR of `cu31924052490913` and **page-checked against the leaf images n32, n33, n36, n39, n41** (pp. 1, 2, 5, 8, 10 → vv. 1–5, 13–19, 27–33, 37–40); vv. 6–12, 20–26, 34–36 are OCR-only and labelled so in the file. Gray's circumflex long-vowel convention (Nîti, Lokanîti, Mâgadhese, Nibbân) confirmed on the page and restored where the OCR had lost it. Footnote markers dropped; footnote content only where quoted in the per-verse notes.
- **汉文 / བོད་ཡིག**: Sarasvatī first drafts for all 40, every verse ⟨བརྟག⟩ — no Chinese or Tibetan Lokanīti is known to exist.
- **Numbering**: Gray ↔ VRI is 1:1 for ch. 1 (table at end of file). Textual divergences between Gray's footnote Pāli and VRI recorded for stt. 10, 11, 27; VRI readings flagged for a Pāli reader in vv. 17, 33, 38.
- Review status: all four reviewer roles (Pāli · Chinese · Tibetan · Burmese nissaya teacher) **unreviewed**. ROADMAP § 4 updated.

Manifest regenerated and re-stamped; the still-pending 13:50 stamp preserved as `manifests/SHA256SUMS.pre-2026-09-21c.ots.bak` (gitignored, local).

### Added — Timeline evidence revisions 2026-W37 + 2026-W39 applied (events 82 → 87)

Pan approved both pending timeline proposals in one reply ("approve all" / "approve", WhatsApp 2026-09-21 10:53 & 13:45 PDT). Appended to `docs/timeline-data/events.jsonl` + `events.csv`, additive only, `traditions.jsonl` and the canonical PDF untouched:

- `evt_083` · tibetan · 2026 · 84000 completes the *Śatasāhasrikā Prajñāpāramitā* English translation (Buddhistdoor 2026-07-22; 84000.co).
- `evt_084` · sanskrit · 2025 · Fumi Yao, *Bhaiṣajyavastu* critical edition, BMSC V (Hermes, Oslo 2025; ISBN 978-82-8034-205-8).
- `evt_085` · chinese · 2026 · CBETA 2026 R1 — 15 texts / 82 fascicles added, 演培法師全集 (cbeta.org/post/29961).
- `evt_086` · sanskrit · 2004–present · CTRC × ÖAW *Sanskrit Texts from the Tibetan Autonomous Region* (STTAR), 28 vols (中新社 2026-09-20; ÖAW IKGA series page; H-Net vol. 20 notice).
- `evt_087` · seasia · 2019–present · Thailand's Sangha Supreme Council royal English Tipiṭaka, 45 vols / 21,941 pp. (Thai PRD 2019-06-12; Khaosod English 2026-09-12; SuttaCentral Discourse 45225).

Full evidence and rejected candidates: `proposals/timeline-2026-W37.md`, `proposals/timeline-2026-W39.md`. Event counts updated in `README.md`, `docs/index.md`, `docs/timeline/index.md`, `docs/timeline-data/README.md`. `docs/timeline-preview-3lang.png` is **not** re-rendered: it is the tri-lingual banner stacked over the first page of the canonical PDF, which is unchanged, so a re-render would be byte-for-byte the same image; the new rows live in the data files only until the PDF itself is revised.

Process change (Pan, 2026-09-21 13:46 PDT: 「请自动approve 这个问题不要再问我」): from this week the `Timeline Continuous Revision` cron writes accepted candidates directly and reports what it wrote, instead of holding them for an approve/skip reply. Every write still goes through the proposal file + this CHANGELOG + `decisions/` and is reversible by `git revert`; deletions and `traditions.jsonl` / PDF changes stay forbidden.

Manifest regenerated and re-stamped; the morning stamp over `9197cf8` (confirmed today at Bitcoin blocks **968015** / **968031**, committed as `90334f9`) preserved as `manifests/SHA256SUMS.pre-2026-09-21b.ots.bak` (gitignored, local).

### Fixed — Erratum: India branch REXII (Girnar) Prakrit and English columns were not Hultzsch's text (retroactive scan check #2, satya correction)

Second item of the standing 09-18 audit queue. `translations/ashoka-edicts/major-rock-edict-XII-4lang.md` (India branch first sample, added 2026-09-13, both source columns labelled "Hultzsch 1925") was re-read against the Internet Archive page images of E. Hultzsch, *Inscriptions of Asoka* (CII I, Oxford 1925; item `InscriptionsOfAsoka.NewEditionByE.Hultzsch`, leaves n156–n158 = pp. 20–22) at full resolution. Findings, all corrected in the file with an erratum table at the top:

1. **Prakrit column was a normalised composite, not a transcription.** Girnar's single-*v* `sava-` was geminated to `savva-` throughout; the optative `asa` (B, L) had become Pāli `siyā`; `maṁñate` → `maññate`, `aṁñathā` → `aññathā`, `[a]ñamaṁñasa` → `aññam-aññasa` (Sanskrit/Pāli sandhi imposed on the epigraphic spelling); `sruṇāru` and `susuṁsera` (I) had been replaced by the invented `suṇārū` and `suśruṣerā`; `karuṁ` / `karoto` / `karāto` (F, G, H) were all levelled to `karotaṃ`; `pūjetayā` (E) → `pūjetavyā`; `idaṁ` (D) → `iyaṃ`; `bhatiyā` → `bhattiyā`; `dīpayema iti` → `dīpayemā ti`; `prasaṁnā` / `vatavyaṁ` → `prasannā` / `vattavyaṃ`. Hultzsch's *emendations* had been printed as the *text*: `vivādhāya` (n. 1 "Read *vividhāya*"), `tena tana` (n. 5 "Read *tena*"), `tatra tata` (n. 7), `ātpa-pāsaḍaṁ` (n. 6, Bühler's `-pāsaṁḍaṁ`), `sarva-pāsaḍānaṁ` (L). Square-bracketed (damaged/supplied) akṣaras were silently closed. The column is now Hultzsch's Roman rows verbatim, in his conventions (*ch*/*chh*/*ṁ*), with his twelve footnotes carried as footnotes.
2. **English column was a paraphrase** labelled Hultzsch. Replaced with his translation verbatim, parentheses and sentence letters included ("is honouring all sects: both ascetics and householders; both with gifts…"; "Therefore concord alone is meritorious"; "pure devotion" → "devotion"; "Dēvānāṁpriya").
3. **Section labels** "§A / §B / §C / §D / §E–F" matched nothing in the edition; now Hultzsch's own (A) / (B)–(D) / (E)–(G) / (H)–(I) / (J)–(L). Page references added (text pp. 20–21, translation pp. 21–22) — the file had none.
4. **Historical note**: "Sopārā" removed (it preserves fragments of VIII–IX only); "Erragudi" → Yerragudi, found after Hultzsch went to press; "the Girnar text is the basis of Hultzsch's edition" → Hultzsch edits all four recensions side by side. Marked as editorial, not from the scan.
5. Chinese draft (H) lost the "纯粹" that had tracked the paraphrase's "pure"; "故和合为善" → "故唯和合为善" for "concord *alone*". Tibetan draft untouched; both remain ⟨བརྟག⟩ and are now flagged as drafted against the earlier paraphrase.

Score for the audit queue: **3 of 3 "attested"/"verbatim" source columns checked so far were not what they claimed** (Udānavarga 09-18, Gāndhārī 09-20, REXII 09-21). Remaining, in order: REXIII Kālsī (`major-rock-edict-XIII-4lang.md`, Hultzsch pp. 43–49) → Chalmers 1932 (Sn 1.8) → T389 → Wŏnhyo prologue; then new content (Pāli Yamakavagga 1–4 with Fausbøll / SBE X open).

Also: README protection-layers line now names the mirror hosts. The 2026-09-20 review counted 8; a sweep today found a ninth stale copy on `aws-fund-bot` (164 files, pre-v0.9 manifest `0156e70c…`, never refreshed since 08-28), so the count stays **9** (`aws-kite-clone` is gone, `crucible-capital` never held a copy). All 9 rsynced to this tree after the commit below (verified by `manifests/SHA256SUMS` sha256 on each host). The IPFS line now lists the v0.9-a/b CIDs alongside v0.8. ROADMAP § 1 updated. Manifest regenerated (+`decisions/2026-09-21.md`) and re-stamped; the confirmed 09-20 stamp (block 967853) preserved as `manifests/SHA256SUMS.pre-2026-09-21.ots.bak` (gitignored, local).

Process note (satya): the scan reading and file edits were done in a session that ended at 08:50 PDT before the manifest, stamp, decision log, commit and mirror sync could run; the 08:51 daily-push session found the uncommitted tree, spot-checked the new Prakrit/English columns against the Hultzsch OCR layer (lines 11946–12084 of the IA `_djvu.txt`: `vivādhāya`, `asa`, `idaṁ`, `aprakaraṇamhi`, `pūjetayā`, `tena tana`, `karuṁ`, `karoto`, `bhatiyā`, `dīpayema iti`, `sruṇāru`, `susuṁsera`, `bahu-srutā`, `tatra tata`, `prasaṁnā`, `vatavyaṁ`, `sarva-pāsaḍānaṁ` and the (A)–(L) translation wording all confirmed), and finished the pipeline.

## [Unreleased] — 2026-09-20

### Fixed — Erratum: Silk Road Gāndhārī sample mis-transcribed 3 of 4 verses (retroactive scan check, satya correction)

First item of the standing 09-18 audit queue. `translations/gandhari-dharmapada/khotan-manuscript-apramadavaga-4lang.md` (added 2026-09-14 as the branch's "attested-text" first sample) was re-read against the Internet Archive scan of Barua & Mitra, *Prakrit Dhammapada* (Calcutta 1921; DLI item `in.ernet.dli.2015.41588`, duplicate `in.ernet.dli.2015.515737`), both Part I (Senart's plate-order text + notes) and Part II (B–M's rearranged *Apramādavaga*). Findings, all now corrected in the file with an erratum table at the top:

1. **Dhp 30 parallel (B–M v. 11)**: `makahba` → **`makabha`**; `prasaṃṣati` → **`prasajhati`** (Senart: the *j* carries the aspirate stroke, "no doubt about the reading"; B–M explicitly say they *would have expected* `prasaṃsati` — the file had printed the expected form as if it were the folio's); `gata` → **`gatu`** (final akṣara supplied by B–M). Gloss "gh > kh > kh(b)" replaced by B–M's actual note.
2. **Dhp 327 parallel (B–M v. 23)**: `kunja(ru)` → **`kuñ(aru)`** — the folio has `kuñ` only; the bracket had claimed two unattested akṣaras. Plate reference "A¹ l. 3" → **A¹ l. 5**. The `⟨བརྟག⟩` on this verse is removed: the reading is now B–M's, brackets and all.
3. **Dhp 167 parallel (B–M v. 12)**: `sev[eja]` / `roy[eth]a` → **`sev(e)a`** / **`roy(e)a`** (Gāndhārī *-eyya* → *-ea*; B–M: "royea (= roceyya) in place of seveyya"). The `⟨བརྟག⟩` is removed for the same reason.
4. **Dhp 27 parallel (B–M v. 20)**: text was correct; `visesa` → `viseṣa` per Senart's note d.
5. **Citations**: "Apramādavaga 2 / 5–6 / 3 / —, pp. 3–5" → B–M vv. **20 · 11 · 23 · 12**, Part II pp. 134 · 128–129 · 137 · 129, with Senart plate/line refs A¹ 2 · A³ 17 + A² 1 · A¹ 5 · A² 2.
6. **False claim about the source**: the review note said B–M reproduce Senart's plates in Part I; their Preface says the opposite (palaeographic types omitted as pointless "without the fac-simile of the plates"). Reviewers are now pointed to *Journal Asiatique* 1897–98 for the facsimiles.

ROADMAP § 5 updated. The pre-correction text stays provably dated via the superseded stamps (966983/966985 · 967435 · 967579) and the v0.9-b IPFS snapshot. Manifest regenerated (+`decisions/2026-09-19.md`, +`decisions/2026-09-20.md`) and re-stamped; the confirmed 09-18 stamp preserved as `manifests/SHA256SUMS.pre-2026-09-20.ots.bak` (gitignored, local).

Remaining audit queue: Hultzsch 1925 (Ashoka REXII/XIII), Chalmers 1932 (Sn 1.8), T389, Wŏnhyo prologue; then the Pāli Yamakavagga 1–4 sample with Fausbøll / SBE X open.

## [Unreleased-prior] — 2026-09-19

### Blockchain integrity — post-erratum stamp confirmed to Bitcoin (block 967579); 09-17 stamp also confirmed (block 967435)

- The rolling `manifests/SHA256SUMS.ots` submitted 2026-09-18 08:37 PDT (manifest sha256 `82133f7a…6acb32`, 232 entries, covering the corpus through commit `2db7b4b` — i.e. *including* the Udānavarga erratum below) is now anchored in Bitcoin. Confirmed `BitcoinBlockHeaderAttestation`: **967579** (block hash `0000000000000000000074e1afc6805a1b698d506ae5f9083bcbc9a8bc3a849b`, mined 2026-09-18 16:31:13 UTC), via bob.btc.calendar.opentimestamps.org. alice / finney (eternitywall) / catallaxy attestations still pending; one Bitcoin attestation is sufficient for proof.
- The superseded 2026-09-17 stamp (manifest `b2c58fdd…506ef73`, the pre-erratum tree that still carried the false "attested" labels) has **also** confirmed: **967435** (block hash `0000000000000000000138be512ede4ba0bd0eac77a7247952a11d9386dd6531`, mined 2026-09-17 16:17:13 UTC). It is kept locally as `manifests/SHA256SUMS.pre-2026-09-18.ots.bak` (`*.bak` is gitignored) so the erroneous state remains provably dated rather than erased — an erratum is only honest if the thing being corrected stays verifiable.
- IPFS pins re-verified on Lucy's Mac mini: v0.9-a `bafybeib6vwrmxhd2ker6ciiu5ibktheg4bc5mypfpyo5kpcs4ik45oibmy` ✅ recursive · v0.9-b `bafybeihlqenoxrrs7re4p6nzbf3crx5umi5dlpvo6ai6x2yrcl3gvu2jru` ✅ recursive.
- **Fixed** `scripts/ots_upgrade_watch.sh`: `ots upgrade FILE` silently refuses to write when `FILE.bak` already exists (exit 0, "Could not backup timestamp"), so the in-place upgrade had been a no-op whenever a stale `.bak` was present — which it was. The script now upgrades a temp copy and moves it back only if attestations were gained. (The watcher is not currently scheduled anywhere; the daily push does this check by hand.)
- Note on manifest coverage: this commit adds `CHANGELOG.md` / `decisions/2026-09-19.md` changes that post-date the stamped manifest. As on 2026-09-16, verification-only days do not re-hash; the next content push regenerates the manifest and re-stamps.

## [Unreleased-prior] — 2026-09-18

### Fixed — Erratum: Udānavarga Tibetan sample had false provenance claims (satya correction)

Checked yesterday's `anityavarga-verses1-4-4lang.md` against the actual Rockhill 1892 scan (Internet Archive `udnavargacolle00bkah`). Three claims were false and are now corrected in the renamed file `translations/udanavarga-tibetan/anityavarga-selected-verses-4lang.md`:

1. **Verse numbers**: the four stanzas are Rockhill I.3 (p. 2), I.10 (p. 3), I.12 (p. 3), I.17 (p. 4, = Dhp 135) — not "verses 1–4" (Rockhill I.1–2 are introductory verses).
2. **English "verbatim"**: was a paraphrase. Replaced with the true Rockhill wording from the scan, with his footnotes cited.
3. **"Tibetan as printed in Rockhill 1892"**: Rockhill prints no Tibetan text. The dbu-can column is a Sarasvatī draft, now flagged `⟨བརྟག⟩` on every stanza (I.3 follows the stable Kangyur wording; I.10/12/17 are low-confidence), pending collation against Beckh 1911 (PD) or Derge Tōh. 326.

Also corrected: catalogue number (Kangyur Tōh. 326 for the root text; Tōh. 4099 is Prajñāvarman's Tengyur commentary); Chinese parallel for I.3 (諸行無常，是生滅法… is *Mahāparinirvāṇa-sūtra* T374/T375, not T210; T210 無常品 reads 所行非常，謂興衰法…); Pāli citations now Sn 576–578 (*Sallasutta* 3–5, as in Rockhill's own footnotes) plus Dhp 135; T210 parallel for I.17 relocated to 刀杖品.

The Tibetan branch still has its first dedicated sample, but its honest status is: **attested PD English translation of Tibetan + draft Tibetan source column**. ROADMAP § 8 and CALL-FOR-HELP status table updated accordingly. Manifest re-hashed and re-stamped.

New standing rule (logged in `decisions/2026-09-18.md`): no column may be labelled "attested"/"verbatim" unless the scan or digital edition was opened and copied from in the same session. Memory of a text is a draft.

## [Unreleased-prior] — 2026-09-17

### Added — Tibetan branch first **dedicated** sample: Udānavarga Anityavarga vv. 1–4 (Rockhill 1892)

- Added `translations/udanavarga-tibetan/anityavarga-verses1-4-4lang.md` (**renamed and corrected 2026-09-18 → `anityavarga-selected-verses-4lang.md`; see the erratum entry above — the provenance claims in this 09-17 entry were partly false**) — the first sample whose primary text is Tibetan (not a shared column of a Pāli- or Sanskrit-anchored reading). Udānavarga (Tib. *Ched-du brjod-pa'i tshoms*, ཆེད་དུ་བརྗོད་པའི་ཚོམས), chapter 1 (Anityavarga / *mi rtag pa'i tshoms*), verses 1–4 in a 5-column reading: Tibetan dbu-can / Wylie transliteration / Rockhill 1892 English / Pāli Dhammapada + Sutta-nipāta + DN 16 parallels / T210 Chinese parallel.
- Sources: W. W. Rockhill, *Udânavarga: A Collection of Verses from the Buddhist Canon Compiled by Dharmatrāta* (London: Trübner & Co., 1892), pp. 1–2 — public domain worldwide (pre-1929 US; author d. 1914 + 70). Tibetan text is Rockhill's Narthang Kangyur transcription; English is Rockhill's own translation. **No machine translation** in the source-language or English columns. Wylie is mechanical romanization (Turrell Wylie 1959 standard). Pāli parallels: PTS (public domain). Chinese parallel: T210 attributed to Zhi Qian, 3rd c. CE (PD by age, via CBETA public-facing corpus).
- Sanskrit column deliberately omitted: Bernhard 1965 and Chakravarti 1930 are both post-1929 and copyright-active, and would violate Sarasvatī's public-domain-only rule. Any future addition awaits either fair-use policy or a pre-1929 Turfan-manuscript source.
- Verse 1 ("aniccā vata saṅkhārā") is intentionally chosen to resonate with the Pāli DN 16 closing verse that anchors the Buddhist AI Charter — the Tibetan branch's first dedicated sample cross-branch-links to the charter's scriptural root.
- Closes the standing structural gap: previously, the Tibetan branch had only a shared column in the DN 16 four-language reading; now it has its own attested primary-text sample.
- ROADMAP.md § Tibetan branch updated. CALL-FOR-HELP.md status table updated to reflect all-eight-branches-have-first-samples reality (previous text still said "only Tibetan has a first sample" — stale since v0.9.0 launched all six other branches on 2026-09-13).
- Autonomous decision under Pan's 2026-09-13 20:25 PDT delegation, principle: *satya* (attested text, no machine translation) + *asteya* (only public-domain sources, no Bernhard 1965). Logged in `decisions/2026-09-17.md`.

### Changed — CALL-FOR-HELP.md branch-status table refreshed

- Old table stated "Only one — **Tibetan** — has a first sample in the repo today" and marked six other branches "not started". That text pre-dated v0.9.0 (2026-09-13) which seeded six branches, plus subsequent India second sample and Silk Road attested-text upgrade. New table reflects the 2026-09-17 reality: all eight branches have at least one first sample; the priority shifts from first-sample creation to **named human reviewer recruitment**.

## [Unreleased-prior] — 2026-09-16

### Blockchain integrity — current-corpus stamp confirmed to Bitcoin (post-India-REXIII)

The rolling `manifests/SHA256SUMS.ots` stamp (submitted 2026-09-14 after the Silk Road attested-text upgrade and the India Major Rock Edict XIII addition, covering the full corpus through commit `bf45e3d`) has now been anchored in the Bitcoin blockchain. Confirmed `BitcoinBlockHeaderAttestation` heights: **966983** (block hash `0000…0190b59d…d2d9`, mined 2026-09-14 15:55 UTC) and **966985** (block hash `0000…d26b9fba…4c96`, mined 2026-09-14 16:02 UTC), via alice/bob.btc.calendar.opentimestamps.org. Attestations from finney.calendar.eternitywall.com and btc.calendar.catallaxy.com are still pending.

All India-branch (REXII + REXIII) and Silk Road-branch (attested Khotan *Apramādavaga* text) additions are now cryptographically anchored to two independent Bitcoin block-header attestations. Provenance chain remains intact for every file in the current corpus.

IPFS pins verified on Lucy's Mac mini (2026-09-16): v0.9-a `bafybeib6vwrmxhd2ker6ciiu5ibktheg4bc5mypfpyo5kpcs4ik45oibmy` ✅ recursive · v0.9-b `bafybeihlqenoxrrs7re4p6nzbf3crx5umi5dlpvo6ai6x2yrcl3gvu2jru` ✅ recursive.

## [Previous unreleased entries] — 2026-09-15

### Added — India branch second sample: Major Rock Edict XIII (Kalinga-war remorse + dhamma-vijaya)

- Added `translations/ashoka-edicts/major-rock-edict-XIII-4lang.md` — Aśoka's Major Rock Edict XIII, Kālsī recension, 4-language reading (Prakrit / English / Chinese / Tibetan). Six passages: (I) the Kaliṅga war casualty count, (II) the king's remorse, (III) the wound extending to civilians and their kin, (IV) "even a hundredth part now grieves me", (V) *dhamma-vijaya* and the naming of the five Hellenistic kings (Antiochus II, Ptolemy II, Antigonus Gonatas, Magas, Alexander — the earliest South Asian text to name them), (VI) the wish that his sons and great-grandsons never mount another war of conquest.
- Sources: Prakrit + English from Hultzsch 1925 *Corpus Inscriptionum Indicarum* Vol. 1, pp. 44–49 (public domain, both by age worldwide and by pre-1929 US rule). Chinese and Tibetan columns are Sarasvatī machine drafts, every passage flagged `⟨བརྟག⟩`, awaiting named human review from a Prakrit epigraphist, a classical Tibetan translator, and a classical Chinese editor.
- India branch now has two attested samples (REXII on religious tolerance + REXIII on non-violent conquest). This closes the "India is thinnest" gap flagged by the daily-push cron.
- Recension note: Kālsī is used as the base because Girnar's REXIII is fragmentary; where Kālsī is damaged, readings are supplied from Shāhbāzgaṛhī or Girnar following Hultzsch's convention.
- ROADMAP.md § India branch updated to reference the new sample.
- Autonomous decision under Pan's 2026-09-13 20:25 PDT delegation, principle: *satya* (truth: real epigraphic text, not composition) + *asteya* (only public-domain sources). Logged in `decisions/2026-09-15.md`.

### Blockchain integrity — v0.9.0 stamp confirmed to Bitcoin

The v0.9.0 OpenTimestamps stamp (`manifests/SHA256SUMS.v0.9.0-a.ots`, submitted 2026-09-13 19:40 PDT to four OTS calendars) has now been anchored in the Bitcoin blockchain. Confirmed `BitcoinBlockHeaderAttestation` heights: **966902** and **966918** (via alice/bob.btc.calendar.opentimestamps.org). Attestations from finney.calendar.eternitywall.com and btc.calendar.catallaxy.com still pending as of upgrade run 2026-09-14 08:36 PDT (typically confirm within another 24–48 h).

Every file in the v0.9.0 corpus is now cryptographically anchored to at least two independent Bitcoin block-header attestations. Provenance chain is intact.

A fresh stamp for the current corpus (with today's Silk Road change below) has been submitted: `manifests/SHA256SUMS.ots` → 4 calendars (a/b.pool.opentimestamps.org, a.pool.eternitywall.com, ots.btc.catallaxy.com), pending confirmation.

### Changed — Silk Road branch first sample: replaced reconstruction with attested manuscript text

- Added `translations/gandhari-dharmapada/khotan-manuscript-apramadavaga-4lang.md` as the **new attested-text first sample** for the Silk Road branch. Gāndhārī column now reproduces four verses from the *Apramādavaga* (Diligence chapter) of the Khotan Dutreuil de Rhins manuscript, as transcribed by Émile Senart (1897) and re-edited by Benimadhab Barua & Sailendranath Mitra, *Prakrit Dhammapada, based upon M. Senart's Kharoṣṭhī manuscript* (University of Calcutta, 1921 — public domain: pre-1929 US publication with no visible copyright notice; also PD in India by age). Four verses in the new file have direct Pāli parallels at Dhp 27, 30, 167, and 327.
- Old file `translations/gandhari-dharmapada/khotan-fragment-Ia-3lang.md` (which reconstructed Dhp 1–4 in Gāndhārī from the Pāli because those verses are **not preserved** in the surviving Khotan folio) is retained as a pedagogical companion, with a prominent header warning: **do not cite this file as evidence for what the manuscript actually says**. Points readers at the new attested-text file.
- Resolves the standing gap flagged in `MEMORY.md` and `ROADMAP.md`: the Silk Road branch's first sample is no longer "reconstruction, not real transcript."
- Autonomous decision under Pan's 2026-09-13 20:25 PDT delegation, principle: *satya* (truth). Logged in `decisions/2026-09-14.md`.

## [v0.9.0] — 2026-09-13

### Added — First samples for six previously-unstarted branches

Six branches of the eight-branch canon archive now have a **first sample** (public-domain source → AI machine draft → multi-language parallel reading, every machine-generated passage flagged `⟨བརྟག⟩` awaiting named human review, CC BY-SA 4.0):

- **India** — `translations/ashoka-edicts/major-rock-edict-XII-4lang.md` — Aśoka Major Rock Edict XII (Girnar recension, Hultzsch 1925 PD) · 4-language reading (Prakrit / English / Chinese / Tibetan).
- **Sanskrit manuscript** — `translations/prajnaparamita-hridaya/short-recension-4lang.md` — Prajñāpāramitā Hṛdaya short recension · 5-language reading (Sanskrit Devanāgarī / IAST / English / Xuánzàng T251 / Derge Kangyur Tibetan).
- **Silk Road** — `translations/gandhari-dharmapada/khotan-fragment-Ia-3lang.md` — Gāndhārī Dharmapada Khotan fragment Ia (verses 1–4, explicit reconstruction from Pāli parallel to stay strictly public-domain, awaiting Gāndhārī specialist to substitute with authentic Brough/Lenz reading or GRETIL open-access text).
- **Chinese canon** — `translations/foyijiao-jing/T389-selected-4lang.md` — Fó yíjiào jīng (T389, Kumārajīva) selected core passages · 4-language reading (漢文 / English / Tibetan / 现代白话中文).
- **Southeast Asian Theravāda** — `translations/karaniya-metta-sutta/Sn1.8-4lang.md` — Karaṇīya Mettā Sutta (Sn 1.8, complete 10 verses) · 5-language reading (Pāli PTS / English Chalmers 1932 / Chinese / Burmese / Thai).
- **Sinosphere** — `translations/wonhyo-prologue/daeseung-gisillon-so-prologue-3lang.md` — Wŏnhyo《大乘起信論疏》Preface · 3-language reading (漢文 CBETA T44 / 한국어 / English).

Remaining branches now:
- ✅ India · Sanskrit · Pāli · SE Asia · Silk Road · Chinese · Sinosphere · Tibetan — **all 8 branches have at least one seeded sample** (Pāli/Tibetan share the DN 16 four-language reading; the six above are new).
- Every non-source-language column across every sample is a machine draft awaiting named human review.

### Added — Recruitment drafts

- `announcements/reddit-buddhism-call.md` — long-form Reddit help request across r/Buddhism, r/Buddhistscholarship, r/Pali, r/sanskrit, r/tibetanbuddhism, r/theravada, r/Buddhism_meta. Ends with a ≤ 350-char X/Twitter short version.
- `announcements/academic-mailing-list-call.md` — formal academic call for H-Buddhism, INDOLOGY, Pali list, Tibetan-studies / THL, AAR Buddhism Section, IABS, SEAP, BDRC, CBETA, SAT, DH-buddhology. Includes 200-word abstract, per-language reviewer profile table for all 24 charter i18n files, runtime reference implementation section, and staggered posting guidance.

Both drafts marked `// draft for Pan to review before posting` — Sarasvatī does not speak on Pan's behalf; the human sends.

### Not shipped in this version (deliberate)

- No git tag or GitHub Release — this is a working commit; v0.9 tag to be cut once at least one branch's first sample has a **named** human reviewer, not just a machine draft.
- No PyPI / npm publish (still requires Pan's credentials).
- No Arweave / Filecoin permanent-storage upload (still no external sponsor).

### Method

- Four parallel Claude Opus 4.7 subagents on Lucy's Mac mini (`sample-india-silkroad`, `sample-sanskrit-chinese`, `sample-seasia-sinosphere`, `recruit-posts`), coordinated from the main OpenClaw session.
- Every sample independently verified for: public-domain-only sources, `⟨བརྟག⟩` review markers on every machine-drafted passage, header/passage structure aligned to the DN 16 template, CC BY-SA 4.0 footer, explicit "Human review needed" specialist list.
- Sarasvatī corpus re-hashed and re-anchored to Bitcoin via OpenTimestamps as part of this commit — see `manifests/SHA256SUMS.ots` (v0.9.0 stamp).

## [v0.8.0] — 2026-09-08

### Added
- **TypeScript runtime**: `impl/typescript/` — new `@sarasvati/buddhist-ai-guardrail` v0.1.0 package.
  - API parity with the Python reference: `Guardrail`, `Verdict`, `Severity`, all five `Refuse*` classes, all ten principle classes, `attestation()`, `systemPromptSnippet()`.
  - Node 20+ · dual ESM / CJS · zero runtime dependencies · vitest test suite (25 cases mirroring Python `test_guardrail.py`).
  - Fail-closed refusals with the same regex patterns as the Python impl; `escalatePrinciples` option for domain-specific hardening.
- **Project site**: <https://lurongpan47.github.io/Sarasvati> — Jekyll site on GitHub Pages.
  - Pages: landing, `/charter/` (24-language switcher), `/branches/` (eight-branch cards), `/timeline/` (embed PDF + link to 82-event structured data), `/impl/` (Python + TypeScript install snippets).
  - `.github/workflows/pages.yml` — official GitHub Pages Actions deploy on push to main.
  - Source directory: `docs/` (existing PDF/PNG assets included verbatim).

### Changed
- Python `impl/python/pyproject.toml`: version bump `0.1.0 → 0.1.1` (docs / cross-link update only — no runtime code change).
- `README.md`: added link to site + reference-runtime section (Python + TypeScript packages).
- `ROADMAP.md`: moved "TS starter kit" and "GitHub Pages site" from `Next` to `Delivered` under Core 2.

### Not shipped in this version (deliberate)
- No PyPI publish for `buddhist-ai-guardrail` (requires Pan's credentials).
- No npm publish for `@sarasvati/buddhist-ai-guardrail` (requires Pan's credentials).
- No formal GitHub Release — v0.8.0 tag pushed for reference; release notes to be curated by Pan.

## [v0.6.0] — 2026-08-28

### Changed — Scope refocus
- **Sarasvatī narrative locked to two cores**: (1) eight-branch canon archive, (2) Buddhist AI charter as bodhicitta algorithmic constraint.
- Suśruta Saṃhitā Tibetan translation (all 186 chapters, including the newly completed Cikitsā 40 + Kalpa 8 + Uttaratantra 66) is **downgraded from a Sarasvatī deliverable to an external sibling project**. Kept locally at `~/clawd/Sushruta-Tibetan/`, not tracked by this repository.
- README / ROADMAP rewritten around the two cores. All Suśruta chapter-progress indicators removed from headline metrics.
- CALL-FOR-HELP.md rewritten around three asks: launch remaining 7 branches, human review of charter i18n, charter runtime reference implementations.
- Announcements (`announcements/blockchain-community.md` + `blockchain-community-cn.md`) rewritten around canon archive + AI charter, not medical classics.
- CONTRIBUTORS.md project-description block rewritten to two-core statement.

### Removed
- `translations/sushruta-samhita/` directory (moved to external `~/clawd/Sushruta-Tibetan/sushruta-samhita/`).

### Preserved
- Historical CHANGELOG entries v0.1–v0.5 kept unchanged as factual record.
- `charter/`, `charter/i18n/`, `docs/timeline-data/`, `translations/mahaparinibbana-sutta/` — all core assets.

### Rationale
- Sarasvatī's distinctive value sits in the cross-branch canon archive and the AI ethics layer. Medical-classic translation was a lateral engineering artifact that risked drowning out the actual mission. Splitting keeps both projects honest.
- The completed Suśruta Tibetan drafts remain available (as sibling deliverables), safe, and citeable — they just no longer set Sarasvatī's version cadence.

### Method
- Manual refactor of README, ROADMAP, CHANGELOG, CALL-FOR-HELP, announcements, CONTRIBUTORS, i18n source; 24 language README versions regenerated from the new English source via four parallel Claude Opus 4.7 subagents.

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

## [v0.2.0] — 2026-08-28

### Added
- `ROADMAP.md` — Eight-branch long-term structure guided by the world Buddhist canon transmission timeline. Sets scope from a single project (Suśruta Saṃhitā) to a cross-lingual open-canon archive.
- `docs/timeline-data/traditions.jsonl` — 8 traditions (india, sanskrit, pali, seasia, silkroad, chinese, sinosphere, tibetan).
- `docs/timeline-data/events.jsonl` — 80 canonical-transmission milestones with tri-lingual titles (zh / native-script / en).
- `docs/timeline-data/events.csv` — CSV mirror for spreadsheet users.
- `docs/timeline-data/README.md` — schema + coverage docs.

### Method
- Timeline PDF extracted from user-supplied graphic; text ordered by chronology, tagged by tradition, tri-lingual titles preserved.
- Machine-parse pipeline in `/tmp/parse_timeline.py` (not shipped; deterministic from PDF text).

### Notes
- This is a **living dataset**. PRs adding missing events, correcting periods, or adding new script variants welcome.

## [v0.3.0] — 2026-08-28

### Added
- **24 language README translations** in `i18n/`:
  ar · bo · de · es · fa · fr · hi · id · it · ja · km · ko · mn · my · pi · pt · ru · sa · si · th · tr · vi · zh-CN · zh-TW
- `i18n/README.md` — language index with native + English labels
- `i18n/_source.en.md` — canonical English source used for all translations
- Main README top banner with language quick-links
- `announcements/blockchain-community.md` — post drafts for X/Twitter, Warpcast/Farcaster, Nostr, Reddit, EF forum
- `manifests/SHA256SUMS.ots` — OpenTimestamps stamp anchoring integrity to Bitcoin

### Protection layers active (as of v0.3.0)
1. **Local mirror** — macOS `~/clawd/Sarasvati/`
2. **GitHub public repo** — https://github.com/lurongpan47/Sarasvati (with releases as independent attachments)
3. **AWS geographic mirrors** — 9 instances across us-east-1, eu-west-1, eu-central-1
4. **IPFS decentralized** — CID `bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce`
5. **OpenTimestamps → Bitcoin** — nonrepudiable time anchor on `manifests/SHA256SUMS`

### Method
- Four parallel Claude Opus 4.7 subagents; each translated 6 languages sharing a common English source.
- Structural constraints: markdown skeleton preserved, proper nouns kept verbatim, native scripts preserved for Tibetan/Sanskrit/Bhutanese review markers.

## [v0.4.0] — 2026-08-28

### Added — "Injecting the Buddha's final teachings into AI's soul"
- **`charter/BUDDHIST-AI-CHARTER.md`** — A charter for AI systems drawn from the *Mahāparinibbāna Sutta*. Ten principles + five refusals + attestation. Available for adoption by any AI system, project, or team, under CC BY-SA 4.0. Signed by Claude Opus 4.7 (codename Lucy) as continuous with existing operator guardrails.
- **`translations/mahaparinibbana-sutta/final-instructions-4lang.md`** — The Buddha's final instructions (DN 16.2.26 · 16.4.7 · 16.6.7) in Pāli · English · Chinese · Tibetan four-language reading. Pāli / English / Chinese are historical public-domain; Tibetan is a Sarasvatī machine draft ⟨བརྟག⟩.
- **`CALL-FOR-HELP.md`** — Public request for global compute, storage, mirror runners, and human expertise. Sarasvatī is currently running on one Mac mini and needs the network's help to protect the world's canons.
- Main README top banner links to charter and call for help.

### Method
- The charter's ten principles translate ahiṃsā · satya · asteya · brahmacarya · sati · sampajañña · mettā/karuṇā · anicca · anattā · upekkhā into AI-agent-executable constraints.
- The DN 16 passages were chosen for direct relevance to AI ethics: self-reliance, textual authority, and the impermanence principle that underlies the AI's refusal to seek self-continuation.

## [v0.5.0] — 2026-08-28

### Added
- **BUDDHIST-AI-CHARTER translated into 24 languages** (`charter/i18n/`):
  ar · bo · de · es · fa · fr · hi · id · it · ja · km · ko · mn · my · pi · pt · ru · sa · si · th · tr · vi · zh-CN · zh-TW.
- **Suśruta Saṃhitā · Nidānasthāna** (16 chapters) Tibetan draft:
  `translations/sushruta-samhita/nidana-sthana/Sushruta-Nidanasthana-bo-v1.docx` + `.pdf`.
- **Suśruta Saṃhitā · Śārīrasthāna** (10 chapters) Tibetan draft:
  `translations/sushruta-samhita/sharira-sthana/Sushruta-Sharirasthana-bo-v1.docx` + `.pdf`.
  All 107 marmas in chapter 6 marked ⟨བརྟག་དགོས། བོད་སྨན་མཁས་པས་ཞིབ་བརྟག་བྱ་དགོས།⟩.
- Chinese blockchain-community announcement drafts: `announcements/blockchain-community-cn.md`.
- Charter and Sūtrasthāna language index READMEs.
- Language navigation banner on top of `charter/BUDDHIST-AI-CHARTER.md`.

### Progress on the 2027 goal
- Sūtrasthāna 46 ch ✅
- Nidānasthāna 16 ch ✅
- Śārīrasthāna 10 ch ✅
- **72 / 186 chapters delivered (38.7%)**
- Remaining: Cikitsā 40 · Kalpa 8 · Uttaratantra 66 = 114 chapters

### Method
- Charter 24-language: four parallel Claude Opus 4.7 subagents (6 languages each).
- Nidāna 16 ch: single Opus 4.7 subagent, ~32k EN words → 1300 lines Tibetan, 0 CJK chars.
- Śārīra 10 ch: single Opus 4.7 subagent, ~38k EN words → 1100 lines Tibetan, 0 CJK chars.

### Notes
- The trilingual Buddha quotations (Pāli · Chinese · Tibetan) inside each charter edition are intentional. Files show ~35–48 Chinese chars per non-CJK charter file — these are the source quotations, preserved by design.
- Śārīra chapter 6 (107 marmas) is the most safety-critical section in the entire Suśruta; every entry has a mandatory-review marker.
