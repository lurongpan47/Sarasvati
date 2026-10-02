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
- **Second sample (added 2026-09-15; scan-checked and corrected 2026-09-22)**: Aśoka Major Rock Edict XIII, Kālsī recension — 4-language reading covering Kalinga-war remorse, dhamma-vijaya, and the naming of the Hellenistic kings (c. 256 BCE). `translations/ashoka-edicts/major-rock-edict-XIII-4lang.md`. Prakrit and English are now Hultzsch's Roman transliteration rows (pp. 45–46) and translation (pp. 47–49) copied from the page images with his footnotes; the 09-15 columns had mis-stated the pages ("plate on p. 45"), used a mixed IAST/Pāli convention, printed emendations as text and filled Kālsī's lacunae with words on no rock (`mukhya-mute`, `hida cha`, `shaveshu manuśyeshu`, `chalambu`) — erratum table at the top of the file. Chinese + Tibetan are Sarasvatī machine drafts awaiting named human review. Audit-queue score: 7 of 7 "attested" source columns checked were not what they claimed (Udānavarga 09-18, Gāndhārī 09-20, REXII 09-21, REXIII 09-22, Sn 1.8 Chalmers/PTS 09-23, T389 09-24, Wŏnhyo 09-25); the audit queue is closed — remaining: new content.
- **Third sample (added 2026-09-28, weekly proposal → built same session under the 09-21 auto-approve rule, scan-first)**: the **Calcutta-Bairāṭ rock-inscription** ("Bhābrū edict") — Aśoka's letter to the Magadha Saṅgha naming seven *dhaṁma-paliyāyāni*, 8 lines, sentences (A)–(G). Prakrit = Hultzsch 1925 Roman rows pp. 172–173 with his notes (p. 172 nn. 6–11, p. 173 nn. 1–11) / English = Hultzsch pp. 173–174 with nn. 12–19 and p. 174 n. 1 (the 1925 state of the seven-text identifications) / 现代汉语 + བོད་ཡིག Sarasvatī drafts ⟨བརྟག⟩. `translations/ashoka-edicts/calcutta-bairat-rock-inscription-4lang.md`. Leaves n349 / n352 / n353 (+ estampage plate n351) of IA `InscriptionsOfAsoka.NewEditionByE.Hultzsch`, page numbers read from the running heads (the leaf−136 rule of pp. 20–45 no longer holds past the interleaved plates). 23 image calls. Needs an epigraphist (*Aliya-vasāṇi* ṇ/n, the final long vowels *chā* / *-yeyū* / *jānaṁtū*), a Sinologist and a Tibetan reader for the drafts, a Pāli reader for the seven identifications. Proposal: `proposals/2026-09-28-india-week1.md` (alternates: Rummindeī pillar pp. 164–165, Sārnāth schism edict pp. 161–164).
- **Sample targets (future)**: Rummindeī and Sārnāth pillar inscriptions from the same edition; public-domain critical editions of foundational sūtras.

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
- **Second sample (added 2026-09-26, built scan-first)**: Dhammapada Yamakavagga 1–4 — Pāli Fausbøll 1900 (Luzac; IA `india.history.resource.112138` leaf 0019 = p. 2 by count, no number printed; apparatus with his sigla) / English Max Müller SBE X 1881 (Clarendon; IA `dhammapadaacoll00mlgoog` tif 0063–0064 = pp. 3–4, notes 1–3 in full) / Chinese T210 法句經 雙要品 (Taishō vol. 4 p. 562a10–a22, IA `taisho-tripitaka` leaf 0561, margins read, Taishō 句點-less pāda layout, kaeriten and foot apparatus as printed; 慍於怨者 stanza given as the counterpart of vv. 3–4 jointly, under the Taishō's own 下二頌巴利文無 note) / 现代汉语 + བོད་ཡིག Sarasvatī drafts ⟨བརྟག⟩. `translations/dhammapada/yamakavagga-1-4-4lang.md`. Modelled on the seasia Mettā/Lokanīti files. Needs a Pāli reader (open readings listed in the file), a Sinologist (note ❿ reads 慢 against CBETA's 懆), a Tibetan reader with Udānavarga ch. 31 / 14 open. Natural continuation: Yamakavagga 5–20 from the same three leaves + Fausbøll leaves 0021–0023.
- **Third sample (added 2026-09-27, built scan-first — first repeat of the method)**: Dhammapada Yamakavagga 5–8 — Pāli Fausbøll 1900 (leaf 0019 = p. 2 by count for vv. 5–7, leaf 0021 printed 4 for v. 8; the V. 5 – V. 7 apparatus is a run-over at the foot of the Latin leaf 0020, read as 8–16× line strips; sigla as printed, a 7-shaped ² flagged) / English Müller SBE X 1881 (tif 0065 = p. 5, notes 6–7 in full, no note on 5 or 8, tif 0066 read to prove it) / Chinese T210 雙要品 (Taishō vol. 4 p. 562a20–a26, leaf 0561; stanza boundaries mid-column marked ‖; notes ⓫–⓮ as printed; Dhp 5 given as a cross-reference to the 1–4 file's joint 3–4 stanza, 6 ↔ a21–a22a, 7 ↔ a22b–a24a, 8 ↔ a24b–a26a, all labelled ours; CBETA agrees with the leaf throughout) / 现代汉语 + བོད་ཡིག drafts ⟨བརྟག⟩. `translations/dhammapada/yamakavagga-5-8-4lang.md`. 46 image calls. Needs a Pāli reader (Cᵏ², Mahābh. V 2642, C.|tator's, v. 27, -pass’?), a Müller reader (οἱ πόλλοι), a Sinologist (飲/墮 glyph forms, three kaeriten, the ‖ boundaries), a Tibetan reader with Udānavarga ch. 14 / 29 open. Natural continuation: Yamakavagga 9–12 (Fausbøll leaf 0021 + its foot, Müller pp. 5–6 with note 9's Mahâbhârata run-over, T210 a26 onward under the Taishō's own ⑯/⑱ 四句一 notes and ⑲ 下二頌巴利文無).
- **Fourth sample (added 2026-09-30, built scan-first — second repeat of the method, across two layout boundaries)**: Dhammapada Yamakavagga 9–12 — Pāli Fausbøll 1900 (vv. 9–12 all on leaf 0021 printed 4 — not 0023 as predicted; leaf 0023 printed 6 opens with v. 18; apparatus V. 9 – V. 11 as 8–16× line strips, V. 11's note running over onto the Latin leaf 0022, no note on v. 12; *kāsāvaṁ* / *kāsāvam*, *read paridhassati?*, *p. 384,5*) / English Müller SBE X 1881 (v. 9 on tif 0065 = p. 5, vv. 10–12 on tif 0066 = p. 6; note 9 complete across the page turn with the Mahâbhârata XII, 568 couplet and its italics verified at 3×; note 10; shared note keyed `11, 12.`) / Chinese T210 雙要品 (Taishō vol. 4 p. 562a26–b02, leaf 0561; **register a → b between a29 and b01 inside the Dhp 11 stanza**; notes ⓯ 戒＝我【聖】 and ⓰ 〔知眞…利〕四句－【聖】 — the 聖語藏 lacks the Dhp 12 stanza; 9 ↔ a26b–a27b, 10 ↔ a27c–a28, 11 ↔ a29–b01a, 12 ↔ b01b–b02b, all labelled ours; 眞 爲 僞 as printed; CBETA agrees throughout) / 现代汉语 + བོད་ཡིག drafts ⟨བརྟག⟩. `translations/dhammapada/yamakavagga-9-12-4lang.md`. 31 image calls. Needs a Pāli reader (*Anikkasāvo* tick, *Bʳ* fleck, 9—10 dash, 384,5), a Müller reader (*Kâsâva or* comma, italic *g*, the circumflex table), a Sinologist (a29 kaeriten 3×/6×, the ‖ boundaries, ⓰'s omission in 聖), a Tibetan reader with Udānavarga ch. 29 open. Natural continuation: Yamakavagga 13–16 (Fausbøll leaf 0021 lower half + leaf 0022 foot V. 13 – V. 16, Müller p. 6 notes 13 and 15 → p. 7, T210 b02c onward under ⓱ ⓲ and the 1–4 file's ⑲ 下二頌巴利文無).
- **Fifth sample (added 2026-10-02, built scan-first — third repeat of the method, across the two no-Pāli stanzas)**: Dhammapada Yamakavagga 13–16 — Pāli Fausbøll 1900 (vv. 13–16 in the lower half of leaf 0021 printed 4, 13–14 in two lines, 15–16 in four; apparatus V. 13 – V. 16 entirely on the foot of the Latin leaf 0022, four lines, V. 13 opening line 1 after V. 11's `339. … p. 384,5.` — the prediction held; `V. 14.` with a single numeral `² Sᵏ -ī.` against the verse's ¹ ²; `Bʳ kammaṁ visuddhaṁ.`; plain *-m attano* twice) / English Müller SBE X 1881 (vv. 13–14 and the first line of 15 on tif 0066 = p. 6, the rest on tif 0067 = p. 7; **verse 15 and note 15 both cross the turn**; note 13; no 14; note 16 present — predicted absent, wrong; italics klish*t*a vi*s*uddhi kle*s*a verified at 3×) / Chinese T210 雙要品 (Taishō vol. 4 p. 562b02–b10, leaf 0561; 13 ↔ b02c–b03, 14 ↔ b04–b05a, **b05b–b07 鄙夫染人 … 行成潔芳 two stanzas with no Pāli, under the Taishō's own ⓳ 下二頌巴利文無 — the "⑲" found**, 15 ↔ b08–b09a, 16 ↔ b09b–b10b, all labelled ours; foot line 3 = seven notes ⓱–㉓, ⓲ 〔蓋屋…生〕四句－【聖】 the second 聖 omission of a second twin; 淫/婬 熏 爲 眞 懅 as printed; CBETA agrees throughout) / 现代汉语 + བོད་ཡིག drafts ⟨བརྟག⟩. `translations/dhammapada/yamakavagga-13-16-4lang.md`. 14 image calls; written incrementally after the 10-01 attempt died unwritten; crop list in `.scratch/dhp/13-16-crops.txt`. Needs a Pāli reader (V. 14's missing ¹, the inked ² opening line 2, the plain *m* before *attano*), a Müller reader (*'evil or sin,'* thin space, the italics), a Sinologist (**all kaeriten at 3× only**, 懅, 熏, the ‖ boundaries, ⓰/⓲ in 聖), a Tibetan reader with Udānavarga ch. 31 and ch. 28 open. Natural continuation: Yamakavagga 17–20 (closes the chapter: Fausbøll v. 17 at the foot of leaf 0021's text and vv. 18–20 on leaf 0023 printed 6, apparatus V. 17 on leaf 0022 lines 3–4 — `³ Bʳ -tiṁ.` doubtful at 8× — then leaf 0023's foot; Müller p. 7 notes 17, 18 and 19 → p. 8; T210 b10c 今悔後悔 onward, ㉓ 歡＝勸【聖】＊ at b12).

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
- **First sample (v0.9; scan-checked and corrected 2026-09-24)**: Fó yíjiào jīng (佛遺教經, T389, Kumārajīva) — selected core passages, 4-language reading (漢文 T389 / English / Tibetan / 现代白话中文). `translations/foyijiao-jing/T389-selected-4lang.md`. The Chinese column is now the Taishō text copied from the vol. 12 page images (IA `taisho-tripitaka`, leaves 1109–1111 = pp. 1110–1112) with line numbers, the Taishō 句點 and foot apparatus; the 09-13 column had been the popular 流通本 wording (涯/崖, 宜/應, 諸功德/諸善功德, 種種/若種種, 所說…已/所欲…以, 善道/善導 — four of the six being the 宋元明宮 variants the Taishō relegates to its notes) with no page and no apparatus — erratum table at the top of the file. English, Tibetan, modern-Chinese vernacular are machine drafts awaiting review; four sentences flagged where the corrections change the sense.
- **Priority pool**: CBETA public-facing texts; Dunhuang colophons.
- **Sample targets**: minor texts in Taishō vol. 85 never translated to English/Tibetan.

### 7. Sinosphere — 汉字文化圈 · `sinosphere`
Korea, Japan, Vietnam.
- **First sample (v0.9; scan-checked and corrected 2026-09-25)**: Wŏnhyo (元曉, 617–686), the opening 標宗體 section of the *Commentary on the Awakening of Faith* (起信論疏上卷, 釋元曉撰 — Taishō T44 no. 1844, p. 202a25–b28, read from IA leaf 0201) — 3-language reading (漢文 / 한국어 / English). `translations/wonhyo-prologue/daeseung-gisillon-so-prologue-3lang.md`. The 09-13 Chinese column had called itself a "序" from "CBETA T44 no.1844": 110 of its 352 characters are on no leaf (pastiche openings/closings of Passages II and III), 大士/菩薩 and 奧旨/奧義 altered, two cuts unmarked, no page/line — erratum table at the top of the file; column now the printed Taishō text with line numbers, 句點 and the page's one note. Korean and English are machine drafts (sentences rendering the invented text are flagged); awaiting Korean Buddhologist review against 韓國佛敎全書 vol. 1.
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
