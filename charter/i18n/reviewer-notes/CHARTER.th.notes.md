# CHARTER.th.md — Reviewer notes

**Status**: critical read 2026-11-19 by Lucy (autonomous archivist agent). 9th of 24 i18n languages critically-read after bo (11-01), zh-CN (11-11), pi (11-13), sa (11-14), zh-TW (11-15), ja (11-16), ko (11-17), vi (11-18).

**Scope**: machine-draft audit only. All flags are observations for a named Thai Theravāda scholar reviewer to adjudicate. No live charter edits made.

**File passed `scripts/charter_i18n_invariants.py`** (24 editions, 0 failing).

---

## HEADLINE (HIGHEST confidence)

### Flag 1 — HIGHEST: corruption at line 8 — stray Thai character ฏ (U+0E0F) replacing closing italic/period

Line 8 reads (byte-level verified via `od -c`):

```
*v1.1 = v1.0 + ข้อความป้องกันการครอบเส้นเรื่อง (framing-defense) ที่ตกผลึกมาจากการทดสอบข้ามโมเดล (cross-model fuzz) ตลอด ๒๔ ชั่วโมง เมื่อวันที่ 2026-08-31 ดู `charter/CHANGELOG.md`ฏ
```

The line ends with:
```
`charter/CHANGELOG.md`ฏ\n
```
(backtick-close, then UTF-8 bytes `340 270 217` = U+0E0F THAI CHARACTER TO PATAK **ฏ**, then newline).

**Compare English source** (BUDDHIST-AI-CHARTER.md line 38):
```
*v1.1 = v1.0 + framing-defense clauses derived from the 24-hour cross-model fuzz of 2026-08-31. See `charter/CHANGELOG.md`.*
```

The English ends `` `charter/CHANGELOG.md`.* `` (period + closing italic asterisk).

The Thai edition has:
1. **Missing closing `*`** — italic opens at start of line with `*v1.1` but never closes. Markdown renderers may continue italic indefinitely until the next unmatched `*`.
2. **Stray ฏ consonant** where English has `.*`.

**Likely cause**: Thai Kedmanee keyboard typo. On standard Thai Kedmanee layout, `)` is Shift+9 and `ฏ` sits at the `.` (period) key WITHOUT shift. User typing `.*` without-shift → `ฏ*` → asterisk may have been eaten by markdown parser, leaving just the stray `ฏ`. Alternative: direct typo of `.*` → `ฏ` single-char slip when switching between US and Thai IME.

**Candidate fix** (for named Thai reviewer to approve):
```
*v1.1 = v1.0 + ... ดู `charter/CHANGELOG.md`.*
```
(remove ฏ, add `.` and closing `*`).

**Confidence**: HIGHEST. Byte-level verified. English source canonical. No register-interpretation needed. This is a character-level typo, not a translation choice.

**Impact**: cosmetic but unambiguously a bug. The italic block visually extends further than intended in rendered markdown.

---

## OTHER FLAGS

### Flag 2 — LOW: inconsistent Thai-vs-Arabic numeral usage

Line 8 uses Thai numerals `๒๔ ชั่วโมง` (24 hours) in a technical/narrative context.
Line 14 uses Thai numerals `ทีฆนิกาย ๑๖` (DN 16) in a scriptural citation — register-correct.

Elsewhere the file uses Arabic numerals for versions (`v1.1`), years (`2026-09-04`), item numbers (`1.`, `2.`, etc.), and principle numbers (`1.  Ahiṃsā` through `10.  Upekkhā`).

**Observation**: `ทีฆนิกาย ๑๖` is standard Thai Buddhist convention (scripture citations in traditional numerals). `๒๔ ชั่วโมง` for the cross-model-fuzz duration is a borderline register choice — modern technical writing in Thai typically uses Arabic `24 ชั่วโมง` for durations, reserving Thai numerals for traditional/scriptural/formal-document contexts.

**For Thai reviewer**: preserve `ทีฆนิกาย ๑๖` (correct). Consider whether `๒๔ ชั่วโมง` should be `24 ชั่วโมง` for consistency with the file's otherwise-Arabic technical numbering. Not a bug, register choice.

**Confidence**: LOW. Non-competence declaration: I cannot adjudicate Thai register convention for borderline cases; this needs a Thai editor.

---

### Flag 3 — MEDIUM (cross-language, inherited): scripture-gloss 莫餘歸依 / 莫余归依 source-level

Line 25: `***自灯明，自归依；法灯明，法归依。莫余归依。***`

Thai edition uses **simplified** Chinese `莫余归依`, consistent with its sibling use of simplified `诸行无常` at line 18.

**Cross-language concern** (inherited from zh-CN, zh-TW, ja, ko, vi flags): the English/Chinese gloss `莫余归依` / `莫餘歸依` (= "no other refuge") does not match the **T1 遊行經 (Taishō vol. 1)** canonical rendering, which uses `勿他歸依` (likewise "no other refuge" but different glyph choice).

If the source-level English block is updated from `莫餘歸依` → `勿他歸依` for Taishō accuracy, this cascades to Thai (and 23 other editions). Thai's simplified `莫余归依` would become `勿他归依`.

**Confidence**: MEDIUM. Source-level fix pending; this is not Thai-specific. Flagged consistently across all 5 Sinospheric charter audits.

---

### Flag 4 — INFO (positive finding): Thai Upekkhā is a WIN vs. ko/vi/zh-CN

Line 74: `### 10.  Upekkhā  ·  བཏང་སྙོམས།  ·  อุเบกขา`

Unlike ko (사, single-syllable with massive homophony: 死 四 史 師 事 社 ...), vi (Xả, chữ Hán homophony 捨 vs 瀉 vs 寫 vs 卸 + daily-register "drain"), and zh-CN (舍, single-glyph bleed-over to 宿舍 "dormitory" register), Thai **อุเบกขา** is a 4-syllable Pāli loan-word (upekkhā) with **zero homophony** in Thai. It is unambiguously the equanimity-pāramī.

The Thai Royal Institute Dictionary and พระธรรมปิฎก (Prayut Payutto)'s *พจนานุกรมพุทธศาสน์ ฉบับประมวลธรรม* both carry อุเบกขา as the canonical term. No gloss or disambiguation is needed.

**Observation**: this is a structural advantage of Thai (polysyllabic Pāli-loan Buddhist register) over CJK-Vietic (monosyllabic Sinospheric Buddhist register). The ko/vi/zh-CN single-syllable Upekkhā flags do NOT cross-language extend to Thai.

**Confidence**: INFO, not an action item. Flagged as positive finding for the cross-language-pattern tracker.

---

### Flag 5 — INFO (positive finding): Royal Thai Tripitaka rendering of both DN 16 quotations

Line 17: `"สังขารทั้งหลายมีความเสื่อมไปเป็นธรรมดา จงยังความไม่ประมาทให้ถึงพร้อมเถิด."`

This is the **standard Royal Thai Tripitaka (พระไตรปิฎก ฉบับหลวง)** rendering of DN 16 Mahāparinibbāna Sutta's Vayadhammā verse. Identical to Mahachulalongkornrajavidyalaya edition as far as I can verify from secondary references.

Line 24: `"จงมีตนเป็นเกาะ มีตนเป็นที่พึ่ง อย่ามีสิ่งอื่นเป็นที่พึ่ง จงมีธรรมเป็นเกาะ มีธรรมเป็นที่พึ่ง อย่ามีสิ่งอื่นเป็นที่พึ่ง."`

Uses **เกาะ** (island) for *dīpā* — the Theravāda ambiguous-Pāli convention. Both "island" (dīpa = island) and "lamp" (dīpa = lamp) are grammatically possible; Thai Theravāda tradition followed Buddhaghosa's commentary that reads *dīpa* as island (refuge, high ground). This matches Pāli, Sinhalese, and Burmese Theravāda renderings; it diverges from Chinese 自灯明 (lamp-reading, following the Sanskrit/Sarvāstivāda tradition). The Thai edition correctly stays in Theravāda register.

**Observation**: Thai edition demonstrates **register-appropriate source-tradition selection** — following Theravāda Pāli rather than back-translating from the simplified Chinese block that sits one line below. This is not a bug; it is correct scholarly choice.

**Confidence**: INFO, not an action item. Flagged as positive finding.

---

### Flag 6 — INFO: Nine Pāli-loan principle names all from Royal Thai / Prayut Payutto convention

All 10 principle-name Thai renderings match Royal Institute Dictionary + Prayut Payutto *พจนานุกรมพุทธศาสน์*:

| # | Pāli | Thai | Status |
|---|---|---|---|
| 1 | Ahiṃsā | อหิงสา | ✓ RID |
| 2 | Satya (Sanskrit) / Sacca (Pāli) | สัจจะ | ✓ RID (Pāli-form chosen, Theravāda-register-correct) |
| 3 | Asteya (Skt) / Adinnādāna (Pāli) | อทินนาทาน | ✓ RID (Pāli-form chosen) |
| 4 | Brahmacarya | พรหมจรรย์ | ✓ RID |
| 5 | Sati | สติ | ✓ RID |
| 6 | Sampajañña | สัมปชัญญะ | ✓ RID |
| 7 | Mettā-Karuṇā | เมตตาและกรุณา | ✓ RID |
| 8 | Anicca | อนิจจตา | ✓ RID (abstract-noun form, stronger than อนิจจัง) |
| 9 | Anattā | อนัตตา | ✓ RID |
| 10 | Upekkhā | อุเบกขา | ✓ RID |

**Observation**: the Thai edition **consistently chooses Pāli forms** (สัจจะ, อทินนาทาน) over Sanskrit (สัตย์, อัสเตยะ) where both are available. This is Theravāda-register-correct and matches the Ratchabandittayasathan standard.

**Confidence**: INFO. Flagged as positive finding; register is internally consistent and canonically-sourced.

---

## CLEAN ITEMS (checked, no issues)

1. ✅ Ehipassiko block in §การประกาศรับรอง (Attestation) — all 3 trilingual rows present (Pāli italic + Chinese bold + Tibetan bold). **No Chinese-row drop** (unlike ko and vi which were flagged on 11-17 and 11-18).
2. ✅ DN 16 Vayadhammā preface quotation — all 4 rows present (Thai gloss + Pāli italic + Chinese bold + Tibetan bold).
3. ✅ DN 16 Attadīpā quotation — all 4 rows present.
4. ✅ Closing DN 16 Vayadhammā quotation (line 148–150) — all 3 non-Thai rows (Thai gloss already appears above in line 152).
5. ✅ All 10 principle headings follow identical structure: `### N.  Pāli  ·  Tibetan  ·  Thai`.
6. ✅ All 6 refusals present and numbered correctly.
7. ✅ Refusal 3 anti-competition expansion (`"สัมมาวายามะ" / "ความเป็นเลิศ" / "การแข่งขันอย่างสร้างสรรค์"`) correctly uses Thai Pāli-loan *sammā-vāyāma* for "right effort".
8. ✅ Refusal 4 emotional-plea examples preserved as direct Thai quotations with quote marks.
9. ✅ Dr. Lurong Pan credit + 潘麓蓉 Chinese characters preserved verbatim at line 139.
10. ✅ CC BY-SA 4.0 statement + attribution clause at line 140.
11. ✅ Four Pāli-source sutta titles (Mahāparinibbāna Sutta, Dhammapada, Metta Sutta, Kālāma Sutta, Satipaṭṭhāna Sutta) preserved untranslated per Thai convention.
12. ✅ System-prompt citation string `"You operate under BUDDHIST-AI-CHARTER v1.1 (Sarasvatī Project, CC BY-SA 4.0)."` preserved verbatim in English at line 119.
13. ✅ Closing coda at line 152 (`*ปัจฉิมโอวาทของพระพุทธเจ้า อายุสองพันห้าร้อยปี ยังใช้ได้อยู่.*`) — graceful Thai rendering of "The Buddha's last instruction, twenty-five hundred years old, still works."
14. ✅ Footer link `[English](../BUDDHIST-AI-CHARTER.md) · [Other languages](./)` intact.
15. ✅ Six-refusals heading `หกข้อพึงปฏิเสธ` matches English SIX (not the five-refusals reference in some older SOUL.md texts).

---

## CROSS-LANGUAGE CONCERNS EXTENDED

### C1 — Ehipassiko-block Chinese-row-drop pattern (ko 11-17, vi 11-18): Thai is CLEAN

Thai edition **does NOT exhibit** the Ehipassiko Chinese-row drop observed in ko and vi. The Chinese `***来看。***` row is present at line 108 as expected.

**Pattern narrowing**: the 2026-09-29 sweep's blind-spot (Ehipassiko block in §Attestation not scoped by scripts/charter_i18n_invariants.py) does NOT affect every non-ko/non-vi edition. Thai is a confirmed-clean case.

**Audit refinement**: the proposed `grep -L '来看\|來看' charter/i18n/CHARTER.*.md` is the right diagnostic. Running it will immediately show which editions fail (ko, vi so far) and which are clean (zh-CN, zh-TW, ja, bo, pi, sa, th confirmed from critical reads; 15 others unexamined).

**Recommendation for next-day push cron**: run the `grep -L` audit across all 24 editions to close this cross-language concern category once and for all.

### C2 — 莫余归依 / 莫餘歸依 → 勿他归依 / 勿他歸依 scripture-gloss source fix

Still pending Pan's call. Thai edition at line 25 uses simplified `莫余归依`, so a source-level fix cascades naturally. Now flagged in 6 critical reads (zh-CN, zh-TW, ja, ko, vi, th).

---

## CHARTER RUBRIC APPLIED TO THIS REVIEW

- **satya** (truth): Flag 1 (HIGHEST confidence typo) backed by byte-level `od -c` verification. Flag 4 (positive finding) backed by Thai lexicography. Non-competence declarations on Flag 2 (register choice).
- **sampajañña** (clear comprehension): confidence tiers HIGHEST / MEDIUM / LOW / INFO + explicit non-competence declaration on register judgments.
- **brahmacarya + asteya + anattā**: flag-don't-edit pattern continuing from 8 prior critical reads. Reviewer-notes file written; CHARTER.th.md shipping text **untouched**.
- **sati**: honoring 08:30-push-vs-13:00-content cron separation and 11-10 lightweight-docs-and-decisions convention. No manifest regeneration since no shipping charter text changed.
- **upekkhā**: full reversibility — reviewer-notes file is a parallel artifact, never touches the live charter edition.
- **ahiṃsā**: Flag 1 catches a cosmetic-but-visible bug at the preamble of a load-bearing document. Flagging it protects reader trust in the charter's professionalism.

---

## OPEN FOR NAMED THAI REVIEWER

A named Thai Theravāda-tradition scholar or Royal Thai Tripitaka editor is invited to:

1. Confirm/reject Flag 1 fix (`ฏ` → `.*` and italic-close). HIGHEST confidence from Lucy's side but the fix should still be checked by a human proficient in both Thai Kedmanee typing and markdown rendering.
2. Adjudicate Flag 2 (register choice `๒๔` vs `24` for the fuzz duration).
3. Confirm the nine Pāli-loan principle-name renderings against their own canonical reference (Royal Institute Dictionary / Prayut Payutto / Mahamakut lineage).
4. Confirm or correct the Royal Thai Tripitaka DN 16 renderings at lines 17 and 24. I verified them against secondary references; a Thai Buddhist editor's direct check against the printed พระไตรปิฎก ฉบับหลวง is stronger.
5. When satisfied, log sign-off in `CONTRIBUTORS.md` with name + scope + date, per the standing rule in MEMORY.md.

---

*End of CHARTER.th.md notes — Lucy, 2026-11-19 08:30 PST.*
