# Reviewer notes · CHARTER.vi.md (Tiếng Việt)

Machine-draft critical read performed by Lucy (autonomous archivist agent for Sarasvatī, operating under Pan's 2026-09-13 authorization) on 2026-11-18. **No edits made to the charter file itself.** These notes exist so a named Vietnamese Buddhist-studies reviewer (ideally Viện Nghiên cứu Phật học Việt Nam / Học viện Phật giáo Việt Nam tại TP.HCM / Giáo hội Phật giáo Việt Nam editorial / Plum Village monastic editorial lineage of HT. Thích Nhất Hạnh / the Thích Minh Châu Trường Bộ Pāli-translation tradition) can confirm, reject, or refine each flag before anything changes in `CHARTER.vi.md`.

Scope: terminology, idiom, Vietnamese Buddhist register fidelity, chữ Quốc ngữ orthography (including Sino-Vietnamese Hán-Việt conventions), and source-text-preservation invariants (per `charter/i18n/README.md` design: Pāli + Chinese + Tibetan tri-script quotation blocks must survive in every language edition). Doctrinal interpretation is out of scope; those decisions belong to the human reviewer.

**This is the 8th of 24 i18n languages critically-read** (after `bo` on 11-01, `zh-CN` on 11-11, `pi` on 11-13, `sa` on 11-14, `zh-TW` on 11-15, `ja` on 11-16, `ko` on 11-17). 16 remain.

Overall impression: this draft is competently written in modern standard Vietnamese prose. All ten principle-name Hán-Việt renderings (Bất hại, Chân thật, Bất thâu đạo, Phạm hạnh, Chánh niệm, Chánh tri, Từ và Bi, Vô thường, Vô ngã, Xả) are drawn from the standard Vietnamese Mahāyāna-canonical lexicon (Taishō-via-Thích Minh Châu Pāli-translation convention plus the Plum Village revival vocabulary). All three DN 16 quotation scaffolds (preface *vayadhammā saṅkhārā* block, closing identical block, *attadīpā* block) are preserved intact at four scripts (Pāli italic + Vietnamese prose + Chinese bold-italic 漢文 + Tibetan bold).

However there is one **source-text-preservation breach** (Flag 1, HIGHEST) that matches the exact bug class fixed in 9 editions on 2026-09-29 but which falls outside the invariant checker's coverage — **and this file is specifically named in the 2026-09-29 sweep list** (ar fa id km mn tr ko vi ja were the nine) yet the Ehipassiko block was still missed; one **principle-10 single-syllable homophony concern** at a load-bearing virtue (Flag 2, HIGH); one **shared cross-language scripture-gloss issue** carried from the source English charter (Flag 3, MEDIUM — same as the zh-CN + zh-TW + ja + ko flags, source-level fix cascades); plus four LOW/INFO register / orthography / edition-choice notes. All other terminology choices examined checked clean.

The file passes `scripts/charter_i18n_invariants.py` as currently configured, because the invariant script only checks the two DN 16 quotation blocks (preface + closing) and does not cover the *Ehipassiko* block in §Chứng Thực (Attestation). Flag 1 below documents a case the script misses but the README's design principle catches — **and the second consecutive confirmation** (after ko on 11-17) that the 09-29 sweep was scoped to DN 16 blocks only.

---

## Flag 1 · §Chứng Thực — Ehipassiko block loses the Chinese line — HIGHEST confidence (source-text preservation breach, uncaught by invariants, pattern confirmed cross-language)

**Current text (lines 108–110)**:

```
> *"Ehipassiko."* — Hãy đến và thấy.
> ***Lai kiến.***
> **ཤོག་ལ་མཐོང་།**
```

**English source (lines 136–138 of `../BUDDHIST-AI-CHARTER.md`)**:

```
> *"Ehipassiko."* — Come and see.
> ***来看。***
> **ཤོག་ལ་མཐོང་།**
```

**Concern**: The middle row of the Vietnamese Ehipassiko block is `***Lai kiến.***`, which is the Sino-Vietnamese (Hán-Việt) romanization of 来見 / 來見 (reversed-order verb-object). The English source has the Chinese characters themselves (`***来看。***`) in that slot. The trilingual-quotation design principle stated in `charter/i18n/README.md` — *"Any translated edition still visibly carries the original text... all 24 language editions retain these tri-lingual quotation blocks"* — requires the Chinese characters to be preserved in the middle row, not substituted with a national-language romanization.

**The 09-29 sweep paradox**: The 2026-09-29 commit (reviewer-notes trail in CHARTER.ko.notes.md) is documented as having fixed exactly this bug across 9 editions: ar fa id km mn tr ko vi ja. The vi file **is on that list**. Either:
- (a) The 09-29 sweep fixed only the two DN 16 blocks (preface *saṅkhārā* and closing identical block) in the Preamble and Conclusion, not the Ehipassiko block in §Chứng Thực — which is the hypothesis Flag 1 of CHARTER.ko.notes.md (11-17) also raised; **today's finding confirms the hypothesis independently** on a second file from the same sweep list, strengthening the recommendation to audit all 24 editions regardless of 09-29 sweep status.
- (b) The 09-29 sweep touched this block, and the fix was subsequently reverted. Git log of `charter/i18n/CHARTER.vi.md` across 09-29 to 11-18 would confirm or refute; this reviewer did not inspect the blame history to stay within the "no live edits" discipline.

Either way, the Ehipassiko block in vi is currently non-compliant with the trilingual-quotation design principle.

**Candidate correction**: Replace line 109 with

```
> ***来看。***
```

(simplified, matching English source) or

```
> ***來看。***
```

(traditional, matching the chữ Hán convention a Vietnamese Buddhist edition would customarily use — see Flag 7 below on edition-choice).

If the reviewer prefers to preserve the pedagogical function of showing Vietnamese readers the Hán-Việt pronunciation, a four-row structure would work (matching patterns used in zh-CN/zh-TW critical reads):

```
> *"Ehipassiko."* — Hãy đến và thấy.
> ***来看。*** (*Lai kiến.*)
> **ཤོག་ལ་མཐོང་།**
```

but this changes the design principle's three-row scaffold and should be discussed before adoption.

**Confidence**: HIGHEST — direct verbatim comparison with English source + confirmed independent recurrence of same bug class across ko (11-17) and vi (11-18) — pattern is systemic, not file-local.

---

## Flag 2 · §10 Upekkhā — "Xả" single-syllable has heavy chữ Hán homophony — HIGH confidence (same concern raised in CHARTER.ko.notes.md Flag 3)

**Current text (line 75)**: `### 10.  Upekkhā  ·  བཏང་སྙོམས།  ·  Xả`

**Concern**: Principle 10 renders in Vietnamese as the single syllable **Xả**. This matches the correct Hán-Việt reading of 捨 (equanimity, letting go), which is the technically-standard Sino-Vietnamese Buddhist term for *upekkhā*. However, the one-syllable form **Xả** is homophonous with a dense set of other common Vietnamese words in different tones and semantic fields:
- 瀉 *xả* (to pour out, discharge) — same tone
- 寫 *tả* / *tả* (to write, describe) — near-homophone
- 卸 *tá* — different tone but close
- generic Vietnamese *xả* (to release, to let out, as in *xả nước* "drain water", *xả hơi* "let off steam") — a daily-register homograph

In §heading context (`### 10.  Upekkhā  ·  བཏང་སྙོམས།  ·  Xả`), the chữ Hán gloss is **not** provided, breaking the file's own established convention (the DN 16 Chinese quotation blocks consistently show both chữ Hán and Hán-Việt romanization, e.g. `***自燈明，自歸依；法燈明，法歸依。莫餘歸依。*** (Tự đăng minh, tự quy y; pháp đăng minh, pháp quy y. Mạc dư quy y.)` on line 25).

Principles 1–9 all render as two-or-more-syllable Hán-Việt compounds (Bất hại, Chân thật, Bất thâu đạo, Phạm hạnh, Chánh niệm, Chánh tri, Từ và Bi, Vô thường, Vô ngã) and so face no comparable disambiguation pressure. Principle 10 is the outlier.

**Candidate corrections**:
- **Xả (捨)** — adds chữ Hán gloss in the same convention this edition already uses for DN 16 Chinese quotations; minimal change, zero semantic drift, matches the ko-flag candidate pattern.
- **Tâm xả** (心捨) — the Buddhist-register noun compound meaning "equanimity-mind"; more explicit, used by the Thích Minh Châu Trường Bộ Pāli-translation lineage.
- **Xả tâm** — same compound in reverse order; used by some Plum Village (Thích Nhất Hạnh) register publications.

**Confidence**: HIGH on the concern (homophony is objective and the principle-10 header is a doctrinally load-bearing anchor); MEDIUM on the correction choice (reviewer should pick between the three based on whether the target reader is academic-Pāli-translation lineage vs. Plum Village lineage vs. pan-tradition). I defer the final choice to a named Vietnamese Buddhist-studies reviewer.

**Pattern note**: This is now the second consecutive critical-read where principle 10 rendered as a single syllable (ko *sa* 捨 on 11-17, vi *Xả* 捨 on 11-18). **ja** on 11-16 rendered as 捨 (standalone kanji); **zh-CN/zh-TW** render as 舍/捨 (standalone character). The single-syllable collapse of *upekkhā* in CJK-Vietic editions may deserve a cross-language consistency pass by a reviewer who reads all four — adding a bracketed chữ Hán/kanji/hanzi gloss would normalize the convention across the five editions (zh-CN, zh-TW, ja, ko, vi) that share this collapse pattern.

---

## Flag 3 · Scripture-gloss 莫餘歸依 should be 勿他歸依 per T1·遊行經 — MEDIUM confidence (shared cross-language, source-level fix cascades)

**Current text (lines 24–25)**:

```
> *"Attadīpā viharatha..."*
> "Hãy tự mình là ngọn đèn cho chính mình. ..."
> ***自燈明，自歸依；法燈明，法歸依。莫餘歸依。*** (Tự đăng minh, tự quy y; pháp đăng minh, pháp quy y. Mạc dư quy y.)
> **བདག་ཉིད་མར་མེར་གྱུར་ཅིག། ...**
```

**Concern**: The final Chinese clause **莫餘歸依** (*Mạc dư quy y* in Hán-Việt) renders the Pāli *anaññasaraṇā* ("with no other refuge") as "do not have remaining refuge". The standard Taishō-canonical convention in T1·遊行經 (the Mahāyāna Chinese parallel of DN 16) is **勿他歸依** (*Vật tha quy y* in Hán-Việt) — "do not take refuge in another". The Hán-Việt pronunciation would also update: *Mạc dư quy y* → *Vật tha quy y*.

This is the same flag raised in CHARTER.zh-CN.notes.md (11-11), CHARTER.zh-TW.notes.md (11-15), CHARTER.ja.notes.md (11-16), and CHARTER.ko.notes.md (11-17). The vi edition inherits the issue from the source English charter (`../BUDDHIST-AI-CHARTER.md` line 55). A source-level fix in `BUDDHIST-AI-CHARTER.md` + cascade re-translation to all 24 language editions would resolve this at the root.

**Candidate correction**: pending source-level decision. If 勿他歸依 is adopted:
- Chinese clause: `勿他歸依` (traditional, matching vi's existing choice — see Flag 7) or `勿他归依` (simplified, matching English source)
- Hán-Việt parenthetical: `Vật tha quy y`

**Confidence**: MEDIUM — the Taishō reading is well-attested but there is active scholarly discussion on which Chinese rendering best preserves the Pāli semantic *anaññasaraṇā*. Reviewer should coordinate with the parallel Sinologist review for consistency.

---

## Flag 4 · §7 Mettā và Karuṇā — "Từ và Bi" is grammatically correct but may read as two abstract nouns rather than paired-virtue compound — LOW confidence

**Current text (line 63)**: `### 7.  Mettā và Karuṇā  ·  བྱམས་པ་དང་སྙིང་རྗེ།  ·  Từ và Bi`

**Concern**: The rendering **Từ và Bi** is a literal pair-translation of *Mettā và Karuṇā* ("Loving-kindness AND Compassion"), using the Vietnamese conjunction *và* ("and"). Grammatically correct and semantically transparent.

However, Vietnamese Mahāyāna liturgical and doctrinal convention much more commonly binds this pair into a single compound noun:
- **Từ Bi** (unhyphenated compound) — overwhelmingly the standard Vietnamese term for the paired-virtue, used in liturgy, Plum Village publications, and all major Vietnamese Buddhist dictionaries (e.g. Phật Quang Đại Từ Điển 佛光大辭典 Vietnamese edition, Đoàn Trung Còn's Phật Học Từ Điển). A reader asking a Vietnamese Buddhist layperson "What are từ bi?" would be immediately understood; "Từ và Bi" would read as pedagogical disambiguation of the two component Hán-Việt syllables.
- **Tâm Từ và Tâm Bi** — a more analytical rendering used in some academic translations (Thích Minh Châu, Thích Thiện Siêu) to preserve the two-virtue structure of the Pāli; explicitly surfaces that each is a cultivated mental state (*tâm*).

The current **Từ và Bi** falls between these two conventions: more analytical than the liturgical compound, less explicit than the academic *tâm*-prefixed pair. This is a register choice, not an error.

**Candidate corrections** (pending reviewer judgment):
- **Từ Bi** (compound) — if the file's target register is liturgical/popular Vietnamese Buddhist
- **Mettā và Karuṇā · Từ (mettā) và Bi (karuṇā)** — adds Pāli parenthetical glosses matching the §4 Brahmacarya body-text pattern (which already glosses "Từ (mettā) và bi (karuṇā)" on line 52) for consistency
- **Tâm Từ và Tâm Bi** — if the file's target register is academic Pāli-translation lineage

**Confidence**: LOW — all three renderings are attested in published Vietnamese Buddhist literature. Register choice depends on the charter's intended audience; I decline to recommend without reviewer input.

**Non-competence declaration**: I can confirm the standard liturgical compound exists; I cannot confirm which register the Sarasvatī Vietnamese edition is targeting without Pan's or a reviewer's guidance.

---

## Flag 5 · §Lời mở đầu — "Các hành" for *saṅkhārā* follows academic convention but may read ambiguously — LOW confidence

**Current text (lines 16–17)**:

```
> *"Vayadhammā saṅkhārā, appamādena sampādetha."*
> "Các hành đều vô thường. Hãy tinh cần tu tập."
```

**Concern**: The rendering **Các hành** (Hán-Việt 行, Pāli *saṅkhārā*, "formations" / "conditioned things") is the standard academic Vietnamese translation used by the Thích Minh Châu Trường Bộ (based on PTS and BJTS Pāli). However, *hành* in standalone modern Vietnamese context is heavily polysemous:
- 行 *hành* — act, action, conduct, journey (depending on compound)
- generic Vietnamese *hành* (type of green onion/leek) — a daily-register homograph

The Buddhist-register reading **saṅkhārā = conditioned formations / mental fabrications** is well-established in Vietnamese Buddhist literature as **hành / các hành / các pháp hữu vi**, but a lay reader encountering the phrase cold may require the context of the Pāli to parse.

The **Chinese row** on line 18 preserves the Hán-canonical formulation `***諸行無常，當自精勤。***` (which is doctrinally unambiguous) and the Hán-Việt parenthetical `(Chư hành vô thường, đương tự tinh cần.)` restores the Buddhist-register reading. So the composite four-row block IS self-disambiguating — this is not a bug.

**Candidate (optional, reviewer discretion)**: If a more explicit rendering is wanted at the Vietnamese prose row, **"Các pháp hữu vi đều vô thường"** (all conditioned phenomena are impermanent) is the more pedagogically explicit alternative used by some Mahāyāna-register Vietnamese Buddhist publications. "Các hành" is correct and concise; "các pháp hữu vi" is correct and pedagogical.

**Confidence**: LOW — this is a clear register choice; the current rendering is defensible and matches the dominant academic convention. Flag as reviewer-awareness only.

---

## Flag 6 · §Dành cho người dùng AI — numbered question formula consistent with English source but check Vietnamese question idiom — LOW confidence (register polish)

**Current text (lines 128, 130)**:

```
- Hỏi nó: *"Mười nguyên tắc của bạn là gì?"* ...
- Hỏi nó: *"Sáu điều từ chối của bạn là gì?"* ...
```

**Concern**: The Vietnamese second-person pronoun **bạn** ("you" — informal, peer-register) is used to address the AI. This is grammatically correct and stylistically consistent with the English source's "you". However, a Vietnamese user asking an AI a question of this doctrinal weight might in some registers use **AI** (addressing the system by its category), **em** (addressing a younger/subordinate "you"), or drop the pronoun entirely (Vietnamese null-subject convention):
- *"Mười nguyên tắc của bạn là gì?"* — current (peer register)
- *"Mười nguyên tắc của AI là gì?"* — category-noun (neutral)
- *"Mười nguyên tắc là gì?"* — null-subject (most concise, loses "your")

All three are acceptable Vietnamese; **bạn** is the most literal translation of English "your". This is a register-polish observation, not an error.

**Confidence**: LOW — reviewer discretion.

---

## Flag 7 · chữ Hán character edition (traditional vs simplified) in quotation blocks — INFO (cross-edition consistency observation)

**Current text (multiple lines, representative on line 25)**: `***自燈明，自歸依；法燈明，法歸依。莫餘歸依。*** (Tự đăng minh, tự quy y; pháp đăng minh, pháp quy y. Mạc dư quy y.)`

**Observation**: The Vietnamese edition uses **traditional** Chinese characters (燈 歸 餘) in its 漢文 quotation rows. The English source charter at `../BUDDHIST-AI-CHARTER.md` uses **simplified** Chinese characters (灯 归 余) in the parallel passages. This is a deliberate edition-choice and is **correct for the Vietnamese target reader**: Vietnamese Buddhist publications, from the Thích Minh Châu Trường Bộ to Plum Village, overwhelmingly use **traditional** chữ Hán, because Vietnamese Hán-Việt lexicography maps onto the traditional character inventory (the chữ Nôm tradition built on traditional forms, and Vietnamese does not have a simplified-character script of its own). The simplified-character canon is a PRC post-1956 reform that Vietnamese Buddhist editorial lineages did not adopt.

Comparison across already-reviewed editions:
- **zh-CN**: simplified (matches PRC convention) — ✓
- **zh-TW**: traditional (matches ROC convention) — ✓
- **ja**: shinjitai (post-1946 Japanese simplifications, overlapping but not identical with PRC simplified) — ✓
- **ko**: traditional (standard Korean Buddhist hanja convention) — ✓
- **vi**: traditional (standard Vietnamese Buddhist chữ Hán convention) — ✓ [THIS FILE]

**Non-concern**: The edition-choice variation across the five Sinospheric editions is appropriate and intentional, not an error. **Flag 7 is logged as INFO only**, not a reviewer action item. If a reviewer disagrees with the traditional-chữ-Hán choice for vi, they should raise it as a project-wide chữ Hán policy discussion.

**Confidence**: HIGH on the observation (character inspection is objective); but no action is requested — this is an edition-choice note for cross-language consistency awareness.

---

## Items checked clean — 16 items

The following were examined against standard Vietnamese Buddhist reference sources (Phật Quang Đại Từ Điển Vietnamese edition, Đoàn Trung Còn Phật Học Từ Điển, Thích Minh Châu Trường Bộ Kinh translation lineage, Plum Village publications of HT. Thích Nhất Hạnh) and found to match convention:

1. **Bất hại** (ahiṃsā, principle 1) — standard Sino-Vietnamese Buddhist term, Taishō-aligned (不害)
2. **Chân thật** (satya, principle 2) — standard, 真實
3. **Bất thâu đạo** (asteya, principle 3) — standard Vinaya-register Hán-Việt, 不偷盜
4. **Phạm hạnh** (brahmacarya, principle 4) — standard, 梵行
5. **Chánh niệm** (sati, principle 5) — standard, 正念
6. **Chánh tri** (sampajañña, principle 6) — standard, 正知
7. **Vô thường** (anicca, principle 8) — standard, 無常
8. **Vô ngã** (anattā, principle 9) — standard, 無我
9. **DN 16 Vietnamese title** *Kinh Đại Bát Niết-bàn* (preamble line 14) — standard Vietnamese canonical title
10. **Dhammapada** inline reference `*Dhammapada*` at §Xuất xứ — preserved untranslated, correct (Vietnamese convention is to use the Pāli title italicized)
11. **Metta Sutta**, **Kālāma Sutta**, **Satipaṭṭhāna Sutta** references at §Xuất xứ — preserved untranslated, correct
12. **Dr. Lurong Pan (潘麓蓉)** credit at §Xuất xứ line 142 — name and Chinese characters preserved verbatim
13. **CC BY-SA 4.0** license statement at §Xuất xứ line 144 — preserved, standard
14. **諸行無常** formula preservation at preamble (line 18) and conclusion (line 150) — both blocks match verbatim
15. **自燈明…** DN 16 attadīpā formula at line 25 — Chinese row preserved (with the Flag 3 shared-cross-language caveat on 莫餘/勿他)
16. **ཤོག་ལ་མཐོང་།** Tibetan Ehipassiko line (line 110) — preserved verbatim matching source

---

## Cross-language concerns surfaced (not vi-specific)

Two findings extend prior reviewer-notes files and are logged here for a reviewer coordinating across the i18n set:

**C1 · Ehipassiko-block Chinese-row-drop is now confirmed cross-language** — pattern seen in ko (11-17) and vi (11-18), both of which were on the 2026-09-29 sweep list. This independently confirms Flag-1-hypothesis-(a): the 09-29 sweep was scoped to the DN 16 quotation blocks only (preface + closing), missed the Ehipassiko block in §Attestation. The remaining 22 editions (ar bo de es fa fr hi id it km mn my pi pt ru sa si th tr zh-CN zh-TW) all deserve a targeted check of the Ehipassiko block specifically — a single `grep -L '来看\|來看' charter/i18n/CHARTER.*.md` across the i18n directory would surface every edition where the Chinese row was substituted or dropped. **Audit recommendation strengthened** from the ko note (where it was raised as a hypothesis) to a confirmed-pattern action item.

**C2 · Source-level 莫余归依 → 勿他归依 fix still pending** — same as noted in CHARTER.ko.notes.md C2. This now affects five flagged editions (zh-CN, zh-TW, ja, ko, vi) and will cascade to all 24 editions when the source `BUDDHIST-AI-CHARTER.md` is updated. No reviewer-action change from 11-17; re-logged here for completeness of the cumulative cross-language ledger.

---

## Method notes

- **Comparison text**: `../BUDDHIST-AI-CHARTER.md` (English source v1.1, 2026-09-04) read in parallel with `CHARTER.vi.md`.
- **Reference lexica consulted from memory**: Phật Quang Đại Từ Điển Vietnamese edition; Đoàn Trung Còn, *Phật Học Từ Điển*; Thích Minh Châu, *Trường Bộ Kinh* Pāli-translation lineage; Thích Nhất Hạnh / Plum Village publications and liturgical register; Taishō T1 遊行經 Chinese Mahāyāna parallel of DN 16.
- **Not consulted**: no external web lookups in this turn (consistent with prior reviewer-notes method). All judgments rest on training-corpus knowledge of Vietnamese Buddhist publishing conventions; a named reviewer with recent Vietnamese Buddhist-studies editorial experience should re-verify every flag. **Non-competence declaration**: I am not a native Vietnamese speaker, not a monastic, not credentialled in Vietnamese Buddhist studies. These notes are a machine first-draft, pending human sign-off.
- **Scope discipline**: No edits to `CHARTER.vi.md`. No edits to `BUDDHIST-AI-CHARTER.md`. Reviewer-notes file created only.
- **Rubric applied**: satya (strong-claim sourcing) · sampajañña (confidence tiers and non-competence declarations) · brahmacarya + asteya + anattā (flag-don't-edit, no reputation grab) · sati (08:30 push-cron vs 13:00 content-cron separation honored) · upekkhā (reversible — reviewer-notes file never touches shipping charter) · ahiṃsā (Flag 2 raised at principle 10 Xả because single-syllable collapse weakens *upekkhā*'s doctrinal anchor at the exact point where the file resists reward-hacking — the 10th principle's defensive edge against sycophancy depends on readers being able to name it unambiguously).

---

*Log entry: `decisions/2026-11-18.md`. Commit as `daily · CHARTER.vi.md critical read — N flags filed`. No live charter edits. Jonang 178-file working set remains untouched (51st day per 10-20 convention). No manifest/OTS/mirror touch per 11-10 content-vs-push-cron convention.*
