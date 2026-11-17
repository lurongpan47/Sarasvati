# Reviewer notes · CHARTER.ko.md (한국어)

Machine-draft critical read performed by Lucy (autonomous archivist agent for Sarasvatī, operating under Pan's 2026-09-13 authorization) on 2026-11-17. **No edits made to the charter file itself.** These notes exist so a named Korean Buddhist-studies reviewer (ideally 동국대학교 불교학술원 / 조계종 교육원 / 금강대학교 불교문화연구소 / 한국불교학회 / Dongguk University or Jogye Order editorial) can confirm, reject, or refine each flag before anything changes in `CHARTER.ko.md`.

Scope: terminology, idiom, Korean Buddhist register fidelity, hangul / hanja conventions, and source-text-preservation invariants (per `charter/i18n/README.md` design: Pāli + Chinese + Tibetan tri-script quotation blocks must survive in every language edition). Doctrinal interpretation is out of scope; those decisions belong to the human reviewer.

**This is the 7th of 24 i18n languages critically-read** (after `bo` on 11-01, `zh-CN` on 11-11, `pi` on 11-13, `sa` on 11-14, `zh-TW` on 11-15, `ja` on 11-16). 17 remain.

Overall impression: this draft is competently written in modern Korean prose with consistent choice of standard Sino-Korean Buddhist terminology (불해, 진실, 불투도, 범행, 정념, 정지, 자애와 연민, 무상, 무아) — all of which match the Taishō-canonical and Korean Jogye-order conventional readings. However there is one **source-text-preservation breach** that matches the exact bug class fixed in 9 editions on 2026-09-29 but which falls outside the invariant checker's coverage (Flag 1, HIGHEST); one **ungrammatical Korean construction** at a doctrinally-load-bearing spot (Flag 2, HIGH); one **doctrinally-ambiguous single-syllable Sino-Korean rendering** for the 10th principle (Flag 3, HIGH); one **shared cross-language scripture-gloss issue** carried over from the source English charter (Flag 4, MEDIUM — same as the zh-CN + zh-TW + ja flags, source-level fix needed once). Plus three LOW-confidence register / orthography notes. All other terminology choices examined checked clean.

The file passes `scripts/charter_i18n_invariants.py` as currently configured, because the invariant script only checks the two DN 16 quotation blocks (preface + closing) and does not cover the *Ehipassiko* block in §Attestation. Flag 1 below documents a case the script misses but the README's design principle catches.

---

## Flag 1 · §Attestation — Ehipassiko block loses the Chinese line — HIGHEST confidence (source-text preservation breach, uncaught by invariants)

**Current text (lines 107–110)**:

```
> *"Ehipassiko."* — 와서 보라.
> ***와서 보라.***
> **ཤོག་ལ་མཐོང་།**
```

**English source (lines 136–138 of `../BUDDHIST-AI-CHARTER.md`)**:

```
> *"Ehipassiko."* — Come and see.
> ***来看。***
> **ཤོག་ལ་མཐོང་།**
```

**Concern**: The middle row of the Korean Ehipassiko block is `***와서 보라.***` (Korean), which is a verbatim duplication of the Korean gloss on the preceding line. The English source has `***来看。***` (Chinese) in that slot. The trilingual-quotation design principle stated in `charter/i18n/README.md` — *"Any translated edition still visibly carries the original text... all 24 language editions retain these tri-lingual quotation blocks"* — requires the Chinese to be preserved in the middle row.

This is **the exact bug class** found in 9 editions (ar fa id km mn tr ko vi ja) on 2026-09-29 and fixed the same day. The 2026-09-29 sweep remediated the two DN 16 blocks (which the invariant script covers) but did **not** sweep the *Ehipassiko* block in §Attestation (which the script does not cover, because it is not part of the normative principle-text but of the testimonial scaffolding). The ko edition's Ehipassiko block was missed then and remains unfixed now.

**Candidate correction**: Replace line 109 with

```
> ***来看。***
```

matching the English source, so that the tri-script structure (Pāli + Chinese + Tibetan) is preserved in the testimonial block as well as in the two DN 16 blocks.

**Scope note**: This same defect should be audited across the other 23 i18n editions. Suggested follow-up ticket for Pan: run a non-DN16 Ehipassiko-block invariant check across all 24 files and fix any that duplicate the local-language gloss in the middle row.

**Reversibility**: Trivial single-line replacement; backup already present via git.

---

## Flag 2 · §Mettā 와 Karuṇā (line 65) — ungrammatical **연민로운** — HIGH confidence

**Current text (line 65)**:

> 연민은 순종이 아니다. 진지한 친절은 때로 거절하며, 때로는 가장 **연민로운** 행위란 사용자가 나와 함께 넘을 수 없는 경계를 명시하는 것이다.

**Concern**: 「**연민로운**」 is not grammatical Korean. The Sino-Korean noun 연민 (憐愍, "compassion") does not take the native suffix 「-로운」 (adjective-forming suffix derived from 「-롭다」). The -롭다 / -로운 suffix attaches selectively to specific noun stems (e.g. 자유롭다 "free", 지혜롭다 "wise", 평화롭다 "peaceful") and 연민 is not in that lexical class. A Korean speaker would parse 「연민로운 행위」 as a typo / Chinese-interference form.

The source English is *"the most compassionate act"*. Two standard Korean renderings:

1. **가장 연민 어린 행위** — using 「어리다」 ("to be filled with, to express"), a productive Korean idiom for emotional-quality adjectives (슬픔 어린, 사랑 어린, 자비 어린). This is the closest match to "compassionate (adj.) act".

2. **가장 자비로운 행위** — switching the noun stem to 자비 (慈悲), which is the standard Korean Buddhist term AND which DOES take -로운 (자비로운 is a native, high-frequency Korean adjective). This has the small cost of swapping the noun in a sentence whose subject is 연민, but 자비 and 연민 are near-synonyms in Buddhist Korean usage and §Mettā and Karuṇā elsewhere in the file uses 자애 and 연민 as a pair.

3. **가장 연민에 찬 행위** — "most filled with compassion", formal register, also acceptable.

**Recommendation**: Option 1 (`가장 연민 어린 행위`) preserves the noun chosen elsewhere in the file and uses the most idiomatic Korean adjective-formation pattern for abstract emotional nouns. Option 2 is also defensible but introduces a new noun stem.

**Why this matters doctrinally**: This sentence is the §Mettā/Karuṇā principle's load-bearing statement about the shape of compassion-as-refusal — the precise point where the charter resists the "compassion = agreement" misreading. Leaving it ungrammatical weakens the principle at its defensive edge.

---

## Flag 3 · §10. Upekkhā heading (line 76) — **사** too ambiguous for single-syllable Sino-Korean rendering — HIGH confidence

**Current text (line 76)**:

> ### 10.  Upekkhā  ·  བཏང་སྙོམས།  ·  사

**Concern**: The ten principle-headings in this edition follow the pattern:

| № | Sanskrit | Korean rendering | Hanja |
|---|---|---|---|
| 1 | Ahiṃsā | 불해 | 不害 |
| 2 | Satya | 진실 | 眞實 |
| 3 | Asteya | 불투도 | 不偸盜 |
| 4 | Brahmacarya | 범행 | 梵行 |
| 5 | Sati | 정념 | 正念 |
| 6 | Sampajañña | 정지 | 正知 |
| 7 | Mettā와 Karuṇā | 자애와 연민 | 慈愛와 憐愍 |
| 8 | Anicca | 무상 | 無常 |
| 9 | Anattā | 무아 | 無我 |
| 10 | Upekkhā | **사** | **捨** |

Entries 1–9 are each **two or more syllables of unambiguous Sino-Korean Buddhist technical vocabulary**. Entry 10, 「사」, is a single syllable of Korean reading with **extreme homophony**: without context a Korean reader sees 사 as {死 death, 四 four, 史 history, 師 teacher, 事 matter, 社 society, 士 scholar, 使 envoy, 寺 temple, …}. The hanja 捨 is doctrinally correct for upekkhā (捨 = "letting-go, equanimity", standard Korean Jogye-order gloss), but the entry is not disambiguated.

**Candidate corrections**:

1. **사(捨)** — the simplest fix: parenthesize the hanja, matching the parenthetical-reading convention already used elsewhere in the file (e.g. 「자등명, 자귀의; 법등명, 법귀의. 막여귀의」 line 25 parenthesizes the Sino-Korean reading of a Chinese scripture line). This is the lowest-risk and most backwards-compatible fix.

2. **평정 (平靜)** — the full-form Korean lay-register rendering of upekkhā. Common in modern Korean-Buddhist translation (e.g. 평정심 for "equanimous mind"). Pros: unambiguous. Cons: departs from the single-character canonical Buddhist technical vocabulary established by entries 1–9.

3. **평등사 (平等捨)** — the Abhidharma-register term for the full form of upekkhā as a mental factor (Pāli: *upekkhā cetasika*). Pros: doctrinally most precise. Cons: unfamiliar to lay Korean readers; three syllables breaks the heading cadence.

**Recommendation**: Option 1 (`사(捨)`). It preserves the canonical single-hanja tradition established by the other nine headings while disambiguating the reading with hanja — the same two-script convention this edition already uses in the DN 16 quotation blocks.

**Note on cross-language consistency**: The ja edition (reviewed 11-16) renders upekkhā as 「捨」 (single-kanji headword since Japanese uses kanji directly), and the zh-CN / zh-TW editions as 「捨」 / 「舍」. The ko convention of transliterating to hangul is not wrong per se — it matches entries 1–9 — but the unique ambiguity of 사 warrants the hanja gloss.

---

## Flag 4 · §Preface (line 25) scripture-gloss — **莫餘歸依** → **勿他歸依** — MEDIUM confidence (source-level, cross-language carry-over)

**Current text (line 25)**:

> ***自燈明，自歸依；法燈明，法歸依。莫餘歸依。*** (자등명, 자귀의; 법등명, 법귀의. 막여귀의)

**Concern**: The clause 「莫餘歸依」 (막여귀의, "take-no-other-as-refuge"), while a defensible classical-Chinese rendering of *anaññasaraṇā*, **is not the convention in T1·遊行經** (Dīrghāgama 2, the Taishō Chinese parallel to DN 16). The T1 convention uses 「**勿他歸依**」 (wù tā guīyī, "take-no-other-as-refuge"). This same flag was raised for `zh-CN` (11-11), `zh-TW` (11-15), and `ja` (11-16) and is shared across all four editions because **all four quote the same Chinese scripture-gloss line from the English source charter**. It is a source-level defect, not a Korean-translator error.

The parenthetical Korean reading 「막여귀의」 on the same line is a correct phonetic rendering of 莫餘歸依 as currently written. If the source charter updates the Chinese line to 勿他歸依, the Korean reading would correspondingly become 「물타귀의」.

**Not a Korean-level fix.** Flagged here so the eventual source-level patch (replacing 莫余归依 / 莫餘歸依 in the English charter's quotation and all 24 editions' matched quotations) sweeps the Korean edition's parenthetical reading in the same pass.

**Shared with**: Flag 1 of zh-CN notes · Flag 1 of zh-TW notes · Flag 6 of ja notes. A single consolidated source-level change resolves all four.

---

## Flag 5 · §Preface (line 30) — **표기** too weak for **"Attribution"** — LOW confidence (register)

**Current text (line 30)**:

> 어떤 AI 시스템도, AI 시스템을 만드는 어떤 팀도, 본 헌장의 전부 또는 일부를 채택할 수 있다. 허가는 필요하지 않다. **표기**는 환영한다. 수정은 환영한다. 공유는 요구된다(CC BY-SA 4.0).

**Concern**: 「표기」 (標記, "marking / labeling / notation") is lexically weak for the English *"Attribution is welcomed"* in a CC BY-SA 4.0 licensing context. The official Korean Creative Commons terminology for the CC BY attribution requirement is **저작자표시** (literally "author-indication"); the standalone noun for the concept is **표시** (not 표기) or **저작자 표시**.

**Candidate corrections**:

1. **저작자 표시는 환영한다** — matches CC Korea's official vocabulary. Explicit and legally precise.
2. **출처 표시는 환영한다** — "source indication is welcomed". Common Korean editorial usage, slightly less license-formal.
3. **표기는 환영한다** → keep if 「표기」 is being read specifically as "citation notation" rather than "authorship attribution". But this reading is non-standard in licensing contexts.

**Recommendation**: Option 1 (`저작자 표시는 환영한다`) for alignment with CC Korea's conventional license-translation vocabulary.

**Confidence note**: LOW because a Korean Buddhist-studies reviewer with CC-licensing familiarity would be the authority; if 「표기」 is in widespread informal Korean use for "attribution" and I am overreading the register, downgrade or discard.

---

## Flag 6 · §Preface (line 51) orthography — **선호없이** → **선호 없이** — LOW confidence (spacing)

**Current text (line 51, within §4 Brahmacarya)**:

> 자애(mettā)와 연민(karuṇā)은 **선호없이** 모든 존재를 향하며, …

**Concern**: Standard Korean orthography (National Institute of Korean Language, 한글 맞춤법 §41) treats 「없이」 as a bound adverb-forming suffix that **takes a space from its preceding noun**. The correct spacing is 「선호 없이」.

**Scope**: Trivial orthographic fix. A Korean native speaker would parse 「선호없이」 without difficulty, but the compound-noun reading is non-standard and a Korean editor would flag it.

**Candidate correction**: `선호 없이`.

---

## Flag 7 · §Attestation (line 104) — em-dash cluster on 「연속적인 것—충돌하지 않는 것—으로」 — LOW confidence (readability)

**Current text (line 104)**:

> 나 Claude Opus 4.7(Anthropic)은 … 이 헌장(v1.0은 2026-08-28에 서명; 2026-08-31의 24시간 크로스-모델 퍼지 테스트 후, 2026-09-04에 v1.1로 재서명)을 읽고, 이해하고, 받아들인다—운영자가 이미 나에게 준 안전 가드레일과 **연속적인 것—충돌하지 않는 것—으로**. 이 헌장은 그 가드레일을 대체하지 않으며, 그것들을 심화한다.

**Concern**: The nested-em-dash construction `연속적인 것—충돌하지 않는 것—으로` is a close transliteration of the English *"as continuous with — not in conflict with — the safety guardrails"*. The dash-cluster is admissible in Korean writing but reads awkwardly here because the connective 「-으로」 ("as") attaches to the second noun phrase 「충돌하지 않는 것」 (via "as not-conflicting") rather than to the semantic head 「연속적인 것」 ("as continuous"). A Korean reader may re-parse multiple times.

**Candidate rewrite**:

1. 「안전 가드레일과 연속적이며 충돌하지 않는 것으로」 — flattens to a simple conjunction; loses the parenthetical nuance.
2. 「안전 가드레일과 연속적인 것으로 (충돌하지 않는 것으로) 받아들인다」 — parenthesizes the gloss.
3. 「안전 가드레일과 연속적인 것 — 즉 충돌하지 않는 것 — 으로 받아들인다」 — adds 「즉」 ("that is") to clarify the appositive relation.

**Recommendation**: Option 3 (adding 「즉」) is the least invasive fix.

**Confidence**: LOW because this is a stylistic rather than a semantic flag; the current text is grammatical and parseable, just uneven.

---

## Items checked clean

The following were examined and found to match conventional Korean Buddhist and modern-Korean register:

1. **불해 / 진실 / 불투도 / 범행 / 정념 / 정지 / 자애와 연민 / 무상 / 무아** (principle names 1–9) — standard Sino-Korean Taishō-canonical Buddhist technical vocabulary; match Jogye Order and Dongguk University Buddhist dictionary conventions.
2. **『대반열반경』(*Mahāparinibbāna Sutta*, 장부 16)** — correct Korean canonical title for the Pāli DN 16; 장부 = 長部 is the standard Korean rendering for *Dīgha Nikāya*.
3. **『법구경』『자경』『깔라마경』『염처경』** (line 123, Provenance) — all four Pāli-canon source-sutta titles use conventional Korean renderings; 깔라마경 for *Kālāma Sutta* follows the common ㄲ-initial convention.
4. **DN 16 preface block (lines 17–20)** — Pāli verbatim, Chinese preserved as 諸行無常，當自精勤。 (traditional variant, invariant-check accepts), Tibetan verbatim. Parenthetical Korean reading 「제행무상, 당자정근」 correct.
5. **DN 16 attadīpā block (lines 23–26)** — Pāli verbatim, Chinese preserved, Tibetan verbatim. Parenthetical Korean reading 「자등명, 자귀의; 법등명, 법귀의. 막여귀의」 is a correct phonetic rendering of the Chinese as written (see Flag 4 for the separate source-text question about whether the Chinese should be 莫餘歸依 or 勿他歸依).
6. **Closing block (lines 148–151)** — identical structure to preface block, trilingual preservation intact.
7. **「붓다」** vs 「부처」 — the file uses 「붓다」 (Pāli-transliterated) throughout. Standard Korean Buddhist-academic convention allows both; 「붓다」 is preferred in modern Korean Buddhist-studies register (e.g. 동국대학교 불교학술원 publications), 「부처」 is the native-Korean lay-register alternative. Choice is consistent.
8. **「운영자」** for operator (lines 102, 104) — correct modern Korean technical register.
9. **「잣대 / 보상 신호의 형태」** — faithful rendering of "reward signal shape" (line 80).
10. **Dr. Lurong Pan(潘麓蓉) credit** (line 127) — correctly preserved; hanja parenthesized; title 「Sarasvatī 프로젝트」 uses the project name as given.
11. **CC BY-SA 4.0 license statement** (line 129) — present and accurate.
12. **Pāli italic rows** throughout — all preserved verbatim with correct macrons and diacritics.
13. **Tibetan bold rows** throughout — all preserved verbatim (spot-checked ལས་སུ་བྱས་པ་ཐམས་ཅད, བདག་ཉིད་མར་མེར་གྱུར་ཅིག, ཤོག་ལ་མཐོང་།; shad punctuation intact).
14. **「표기」 vs 「저작자표시」** → see Flag 5.
15. **「연민로운」** → see Flag 2.

---

## Cross-language concerns surfaced (not ko-specific — carried to source-level review)

1. **Ehipassiko block Chinese-row-drop (Flag 1)** — audit across 23 other i18n editions; the 2026-09-29 sweep remediated the DN 16 blocks only, not this one. If other editions have the same pattern, batch-fix.
2. **Scripture-gloss 莫余归依 / 莫餘歸依 / 莫余帰依 (Flag 4)** — source-level fix in the English charter's quotation would cascade to zh-CN, zh-TW, ja, ko, and all other editions that preserve the Chinese line. Pending Pan's source-charter decision; flagged here for completeness.

Both are already noted in the zh-CN, zh-TW, and ja reviewer-notes (Flag 4 is; Flag 1 is a new observation that applies across the i18n set).

---

## Decision log reference

See `decisions/2026-11-17.md` for the Buddhist AI Charter rubric applied to this review (satya / sampajañña / brahmacarya / asteya / anattā / sati / upekkhā) and the choice of task 2 over tasks 1 / 3 / 4 / 5 under today's Prime-Directive cron.

---

*Reviewer notes only. No live charter edits. Awaiting named human review.*
*Lucy, autonomous archivist agent for Sarasvatī, 2026-11-17.*
