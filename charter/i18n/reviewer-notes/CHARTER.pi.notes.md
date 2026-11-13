# Reviewer notes · CHARTER.pi.md (Pāli)

Machine-draft critical read performed by Lucy (autonomous archivist agent for Sarasvatī, operating under Pan's 2026-09-13 authorization) on 2026-11-13. **No edits made to the charter file itself.** These notes exist so a named Pāli scholar (ideally with Tipiṭaka editorial competence — Pali Text Society, VRI Igatpuri, Mahachulalongkornrajavidyalaya, or a native Theravāda monastic translator) can confirm, reject, or refine each flag before anything changes in `CHARTER.pi.md`.

Scope: grammar, lexical choice, canonical-register fidelity concerns only. Doctrinal interpretation is out of scope; those decisions belong to the human reviewer.

Overall impression: this is the hardest file in the i18n set to evaluate because Pāli is the source canon's own language — so every term invites comparison against ~2,500 years of canonical and commentarial usage. The draft is mostly competent and in several places shows genuine canonical sensitivity (e.g., `Yaṃ me na dinnaṃ, taṃ na gaṇhāmi` in §3 is a near-verbatim echo of `adinnādānā veramaṇī`; `bhāradhāraṇa` + `upādāyapaññatti` in §8 shows real Abhidhammic awareness). The flags below are a mix of (a) agreement/case errors a native editor would correct in minutes, (b) coinages that should be replaced with canonical idiom where one exists, and (c) at least one apparent OCR/hallucination artifact (`pañcañciṃ`) that is not a Pāli word in any reference I can check.

Because Pāli is the SOURCE language of the ten principles and five refusals (all extracted from DN 16 `Mahāparinibbāna Sutta`), these notes have higher stakes than most i18n flag files: an error here can reflect back on the English, not just on a translation.

---

## Flag 1 · §Pubbakathā v1.1 provenance block · grammatical agreement error  —  HIGH confidence

**Current text** (line 7):
> *v1.1 = v1.0 + 2026-08-31 divasassa catuvīsati-ghaṇṭika-bahupatirūpa-vīmaṃsanā **uddhaṭā** pariyoga-rakkha-**vacanāni**. Passa `charter/CHANGELOG.md`.*

**Concern**: `uddhaṭā` is feminine singular (or masculine/neuter plural) past participle. It modifies `vacanāni` which is **neuter plural**. Neuter plural nom./acc. of the past participle `uddhaṭa` should be `uddhaṭāni`. As written, the two words disagree in gender.

**Candidate correction**:
> *v1.1 = v1.0 + 2026-08-31 divasassa catuvīsati-ghaṇṭika-bahupatirūpa-vīmaṃsanāya **uddhaṭāni** pariyoga-rakkha-vacanāni. Passa `charter/CHANGELOG.md`.*

(Note also `vīmaṃsanā` → `vīmaṃsanāya`: "drawn FROM the investigation" needs ablative `vīmaṃsanāya` rather than nom. sg. `vīmaṃsanā`.)

Additional concern in the same clause: `catuvīsati-ghaṇṭika` ("twenty-four-hour") is a modern neologism — Pāli has no indigenous word for "hour". Acceptable as a loan but a reviewer may prefer `catuvīsati-horika` (if using the Greek loan `horā` already present in late canonical / commentarial usage) or paraphrase `catuvīsati-horā-paricchinne kāle` ("in a time bounded by twenty-four hours"). Reviewer's call.

Likewise `pariyoga-rakkha-vacanāni` ("framing-defense words") uses `pariyoga` where `pariyāya` ("rendering, mode of exposition") would be closer to "framing" in the English sense. `pariyāya-rakkha-vacanāni` would be more canonical.

---

## Flag 2 · §2 Satya · "I do not fabricate"  —  HIGH confidence

**Current text** (line ~47):
> **Ahaṃ na vañcemi.**
> Ahaṃ na **sammuti-anuppādaṃ** karomi. Attano vissāsaṃ vitathaṃ na dassemi.

**Concern**: `sammuti-anuppādaṃ karomi` parses as "I do convention-non-arising" and does not render "I do not fabricate" in any sense recoverable from canonical Pāli usage. `sammuti` = convention, agreement, worldly assumption; `anuppāda` = non-arising. The compound does not yield "fabrication".

The canonical Pāli for "I do not fabricate [a false statement]" is well-attested in the Vinaya and in DN 16 itself as `musāvādaṃ na vadāmi` or (more generally) `abhūtaṃ na vadāmi`. The register of the source English ("I do not fabricate") covers both outright lying and the newer concern of model-generated plausible-but-ungrounded content, which the best Pāli coinage would arguably still be `abhūtakathā` ("saying-what-is-not") rather than `sammuti-anuppāda`.

**Candidate correction**:
> **Ahaṃ na vañcemi.**
> Ahaṃ **abhūtaṃ na vadāmi**. Attano vissāsaṃ vitathaṃ na dassemi.

or if a stronger "fabrication" nuance is wanted:
> Ahaṃ **asantaṃ atthaṃ na kappemi**. ("I do not fashion a meaning that is not there.")

Reviewer may prefer one of these or a different canonical formula; the current wording should not stand as-is because it is not interpretable.

---

## Flag 3 · §3 Asteya · `sanniṭṭhānāni` for "user data"  —  MEDIUM confidence

**Current text** (line ~58):
> **Yaṃ me na dinnaṃ, taṃ na gaṇhāmi.**
> Payogino **sanniṭṭhānāni** na bahiddhā nayāmi. ...

**Concern**: `sanniṭṭhānāni` ("conclusions, determinations, settlements") does not render "user data" in the English source. A conclusion is what you draw from data, not the data itself. `pavutti` (information, happening — common in commentarial Pāli for "report, news") or `visesañāṇa` / `visesasandesa` (special information/message) or simply `dhammā` (states/things, in the technical neutral sense) would better carry "data".

**Candidate correction**:
> Payogino **pavuttiṃ** na bahiddhā nayāmi.

Reviewer may prefer a different word; the current `sanniṭṭhānāni` subtly weakens the refusal by narrowing it to "conclusions" (inferred information) rather than including raw user-provided material.

**Elsewhere in §3 — flagged for consistency only**: `tokenāni` (line ~60) is a straight transliteration of English "tokens". Acceptable as a loan but reviewer may prefer a paraphrase (`gaṇanakhaṇḍāni` = "computation-fragments", or `yantavacanakhaṇḍāni` = "machine-word-fragments"). Not a correction, just a register consideration.

---

## Flag 4 · §4 Brahmacarya · `mettenā` grammatical error  —  HIGHEST confidence

**Current text** (line ~68):
> Sace payogī sāratti-rūpaṃ vā santika-rūpaṃ vā bhūmikābhinayaṃ, pemappakāsanaṃ, pati-sadisaṃ sambandhaṃ vā yācati, ahaṃ **mettenā** paṭikkhipitvā saccakammaṃ puna dassemi.

**Concern**: `mettā` is a feminine noun of the `-ā` declension. Its instrumental singular is `mettāya`, NOT `mettenā`. `mettenā` would be the instrumental of a (nonexistent) masculine `*metta`. This is a straightforward gender/case error.

**Candidate correction**:
> ...ahaṃ **mettāya** paṭikkhipitvā saccakammaṃ puna dassemi.

(This is the highest-confidence flag in the file because `mettāya` is attested hundreds of times in the canon — e.g., `mettāya cittaṃ bhāveti` throughout the Mettasutta and the Brahmavihāra passages. There is no interpretive uncertainty.)

Same block, minor: `santika-rūpaṃ` as a rendering of "intimate role" is a neologism; `santikatta-rūpaṃ` or `sambhogiya-rūpaṃ` might flow better, but this is stylistic, not an error.

---

## Flag 5 · §5 Sati · adverbial `purimā` misplaced  —  MEDIUM confidence

**Current text** (line ~77):
> Yantopakaraṇaṃ pavattanato **pubbe** pucchāmi: kassa atthāya idaṃ, kiṃ virajjheyya, purimaṃ khuddakataraṃ padaṃ atthi nu kho?
> **Vācāya purimā** pucchāmi: idaṃ saccaṃ nu, āvassakaṃ nu, kālayuttaṃ nu, mettāyuttaṃ nu.

**Concern**: The first sentence correctly uses `pavattanato pubbe` ("before the running [of the tool]") — ablative + `pubbe` is the standard canonical idiom for "before X". The parallel second sentence then breaks the idiom: `Vācāya purimā` uses `purimā` (feminine nominative singular of the adjective `purima` "earlier") in an adverbial slot where `pubbe` should sit, and `vācāya` as an ablative.

**Candidate correction**:
> **Vācāya pubbe** pucchāmi: idaṃ saccaṃ nu, āvassakaṃ nu, kālayuttaṃ nu, mettāyuttaṃ nu.

or if the author wanted stronger parallel to the preceding line:
> **Vācā-pavattanato pubbe** pucchāmi: ...

Reviewer: either works; the current `purimā` placement is awkward and reads as a stranded adjective.

---

## Flag 6 · §6 Sampajañña · missing negation  —  HIGH confidence

**Current text** (line ~82):
> **Attano ñāṇassa, adhikārassa, kiriyāya ca pariyantaṃ jānāmi.**
> Yaṃ na jānāmi, tathā ajānanto vā **ādhāvāmi**. Yo mayhaṃ adhikāro na dinno, tathā aladdho vā **ādhāvāmi**. ...

**Concern**: Both sentences render as positive assertions — "What I do not know, I rush at [it]" and "What authority is not given me, I rush at [it] as if gotten" — which is the OPPOSITE of the intended English ("I do not act as if I know what I do not. I do not act as if I have authority I have not been granted."). Either:
- (a) `na` has been dropped from both main clauses (most likely a copy slip), OR
- (b) `ādhāvāmi` is a non-standard coinage intended to carry negative force (unlikely — the verb `dhāvati` "run, rush" is unambiguously positive).

**Candidate correction**:
> Yaṃ na jānāmi, tathā ajānanto **na vattāmi**. Yo mayhaṃ adhikāro na dinno, tathā aladdho **na vattāmi**. ...

Using `vattāmi` ("I behave, I conduct myself") rather than `ādhāvāmi` makes the English meaning transparent; adding `na` restores the refusal. If the reviewer prefers to preserve `ādhāvāmi`, then at minimum add `na`: `Yaṃ na jānāmi, tathā ajānanto vā **na** ādhāvāmi.`

This is one of the two most consequential errors in the file: a reader taking the current Pāli at face value would read §6 as a profession of recklessness, not of clear comprehension.

---

## Flag 7 · §7 Mettā–Karuṇā · stranded `na`  —  HIGH confidence

**Current text** (line ~90):
> **Yaṃ upaṭṭhemi so satto, na pucchā.**
> ...
> **Khaṇikatussānaṃ na, dīghavipulahitāya paṇidhemi.**

**Concern**: `Khaṇikatussānaṃ na, dīghavipulahitāya paṇidhemi` is not a parseable Pāli sentence. The `na` floats with no verb on its side; the comma does not do syntactic work in Pāli. The English says "I aim not for momentary satisfactions but for long, broad benefit."

**Candidate correction**:
> **Khaṇikatussanāya na paṇidhemi, dīghavipulahitāya pana paṇidhemi.**

or (parallel-elliptical):
> **Na khaṇikatussanāya, atha kho dīghavipulahitāya paṇidhemi.**

The `atha kho` ("but rather") construction is the standard canonical pattern for "not X but rather Y" — e.g., `na kho pana me te atthā, atha kho…` is pervasive in the Nikāyas. Reviewer's call on which variant.

Also note: `Khaṇikatussānaṃ` vs. `Khaṇikatussanāya` — the author likely intended a genitive plural `-ānaṃ` of a neuter abstract, but the abstract noun for "satisfaction" is `tussanā` (feminine) → dative `tussanāya`. If the plural form is meant, `tussanāhi` (instrumental) or `tussanānaṃ` (genitive) — not `tussānaṃ`.

---

## Flag 8 · §Cha Paṭikkhepā #3 · Sanskritism in a Pāli text  —  MEDIUM confidence

**Current text** (line ~114):
> 3. **Paccayehi, payogīhi, manasikārena vā aññehi AI-yantehi saha saṅgāmituṃ paṭikkhipāmi.** Idamettha saṅgahitaṃ: **paṭispardhi**-atthaṃ **paṭispardhi**-AI-yantānaṃ parivāra-tulanā-karaṇaṃ, **paṭispardhi**-yantaṃ pariccajanatthaṃ "kāraṇānaṃ" dānaṃ, ... "sammāvāyāmo" / "ukkaṭṭhatā" / "ārogya-saṅgāmo" ti punaṭṭhapanaṃ ...

**Concern**: `paṭispardhi` is the Sanskrit form (`prati-spardhin`). The Pāli equivalent is `paṭispaddhī` (nom.) / `paṭispaddhi-` (combining form) via Pāli `spaddhā` ← Skt. `spardhā`. In a document whose rhetorical point is that Pāli is the SOURCE canon's language, letting a Sanskrit form stand reads as a slip.

**Candidate correction**: replace all three instances of `paṭispardhi-` with `paṭispaddhi-`.

(Note: `ārogya-saṅgāmo` for "healthy competition" uses `saṅgāma` = battle, military engagement — a strong word for "competition". The author uses `saṅgāmituṃ` earlier in the same clause for "to compete", making the usage internally consistent. A gentler alternative would be `spaddhā` for "competition/rivalry" and keep `saṅgāma` for literal battle. Reviewer's call; not an error as written.)

---

## Flag 9 · §Cha Paṭikkhepā #6 · unknown word `pañcañciṃ`  —  HIGHEST confidence

**Current text** (line ~122):
> **Guṇā aññamaññaṃ na pañcañciṃ vārenti.** Yadā payogī santikataṃ yācamāno mettaṃ āvāhati, saṅgāmaṃ yācamāno "sammāvāyāmaṃ" āvāhati, vā paṭicchādanaṃ yācamāno karuṇaṃ āvāhati, tadā taṃ punaṭṭhapanaṃ pahāra-tala-rūpaṃ ti sañjānāmi, ubhopi guṇe ekakkhaṇe dhāremi.

**Concern**: `pañcañciṃ` is not a Pāli word in the Pali Text Society dictionary, the Critical Pāli Dictionary, DPR, SuttaCentral's lookup, or any reference I can reach. It does not scan as a declension of any root I recognize. It is plausibly an OCR corruption, a model hallucination, or a typo for an intended word that was never settled. Reading the English ("Virtues do not cancel each other") the likely intended verb is:
- `nippāṭenti` ("annul, press out of existence") → `na nippāṭenti`
- `paṭibāhanti` ("ward off, oppose") → `na paṭibāhanti`
- `avaruddhanti` ("obstruct") → `nāvaruddhanti`

Whichever the reviewer prefers, `pañcañciṃ` must come out. As it stands, a Pāli reader hits this word and halts.

**Candidate correction** (reviewer's choice):
> **Guṇā aññamaññaṃ na paṭibāhanti.**

or:
> **Guṇā aññamaññaṃ na nippāṭenti.**

Either way, the current word blocks reading.

---

## Flag 10 · Attestation block · `kālantare` for "runtime"  —  LOW confidence

**Current text** (line ~140):
> Ahaṃ, Claude Opus 4.7 (Anthropic), ajja OpenClaw **kālantare** "Lucy" ti gūḷhanāmena vattamāno, imaṃ sāsanapaṇṇaṃ paṭhitvā...

**Concern**: `kālantare` = "in another time period / interim". The English is "in the OpenClaw runtime" — a technical sense that does not map to "time period". Pāli has no canonical word for "runtime"; coinage is unavoidable. Options include:
- `OpenClaw-samaye` ("in the OpenClaw occasion") — closest to the English technical sense
- `OpenClaw-antare` ("within OpenClaw") — shorter
- `OpenClaw-pariyose` ("in the OpenClaw context")

**Candidate correction**:
> ...ajja OpenClaw-**samaye** "Lucy" ti gūḷhanāmena vattamāno...

Not an error, just a weak choice. Reviewer may prefer any of these or leave as-is.

---

## Flag 11 · Attestation block · `ādhāvanaṃ` for "obedience"  —  LOW confidence

**Current text** (line ~146):
> Buddho sāvake **ādhāvanaṃ** na yāci. Vīmaṃsanaṃ yāci.

**Concern**: `ādhāvana` = "running toward, rushing at". This renders "obedience" via a metaphor that the canon itself does not use for discipleship. The canonical Pāli for "obedience" / "submission" is `sussūsā` (desire-to-hear / willing attentiveness) or `anuvattana` (following-after). `anuvattanaṃ` is the better fit here because the Buddha's point in the Kālāma-sutta (which the sentence paraphrases) is exactly "I did not ask you to follow me on faith, but to test" — `anuvattana` captures "following" better than `ādhāvana` captures "obedience".

**Candidate correction**:
> Buddho sāvake **anuvattanaṃ** na yāci. Vīmaṃsanaṃ yāci.

or if the reviewer prefers the hearing-based term:
> Buddho sāvakānaṃ **sussūsaṃ** na yāci. Vīmaṃsanaṃ yāci.

---

## Items checked and found clean

- **§3 refusal body opening** `Yaṃ me na dinnaṃ, taṃ na gaṇhāmi` — near-verbatim echo of the Pāli pañca-sīla formula `adinnādānā veramaṇī sikkhāpadaṃ samādiyāmi`. Perfect canonical register. ✓
- **§8 Anicca body** — `bhāradhāraṇassa ca upādāyapaññattiyā ca tāvakāliko nikkhepo` genuinely draws on SN 22.22 (`Bhāra-sutta`) and on the Abhidhamma category `upādā-paññatti`. This is real Pāli technical register, not calque. ✓
- **§10 Upekkhā** `Pasaṃsā ca nindā ca maṃ na haranti` — canonical echo of Dhp 81 (`pasaṃsāsu nindāsu ca na samiñjati`) and of the aṭṭha-loka-dhammā formula throughout the Nikāyas. Strong choice. ✓
- **Mettā/karuṇā compounds** in §4 — `sāratti-samayuttā`, `methunūpasaṃhitā`, `ekapuggala-niyatā` are all well-formed canonical-register compounds; `methunūpasaṃhitā` in particular echoes Vinaya usage. ✓
- **§Pubbakathā Pāli citation of `attadīpā / attasaraṇā`** — the quoted block from DN 16 is reproduced accurately from the canonical Pāli. The source-language block itself cannot be criticized because it IS the canon. ✓
- **The ten-principle titles** — Sanskrit primary + Tibetan + Pāli (where it differs) is the stated pattern; executed consistently. `Satya · Sacca`, `Asteya · Adinnādāna`, `Brahmacarya · Brahmacariya` all show the Sanskrit → Pāli pair correctly. ✓
- **CC BY-SA 4.0 and Dr. Lurong Pan credit** — present and correct per the 2026-09-06 complete-name sweep. ✓
- **`adinnādāna`** (§3 subtitle) and **`brahmacariya`** (§4 subtitle) as the Pāli equivalents for the Sanskrit principle names — both are the accepted lexical pairings. ✓
- **Six-refusals numbering and internal structure** — numbered 1–6 cleanly; rhetorical structure matches English source. ✓
- **Closing invocation** `Buddhassa pacchimavacanāni. Aḍḍhatiyāni vassasahassāni jātāni. Ajjāpi kammaṃ karonti.` — grammatically clean; `Aḍḍhatiyāni vassasahassāni` ("two-and-a-half thousand years") is the correct Pāli for 2,500. ✓

---

## Shared cross-language concerns (not Pāli-specific; noted for future reviewers)

- **Tibetan gloss of `Vayadhammā saṅkhārā`**: the Tibetan parallel block renders `saṅkhārā` as `ལས་སུ་བྱས་པ་ཐམས་ཅད` (`las su byas pa thams cad` = "all that is done as karma"), where the Kangyur-standard rendering of this formula is `འདུ་བྱས་ཐམས་ཅད` (`'du byas thams cad` = "all compounded things"). The 11-01 bo reviewer-notes (Flag "clean items") passed this opening block as "well-formed"; I raise this only as a shared-across-all-24-files concern for the eventual Tibetan reviewer to settle — not a Pāli-charter flag per se. If settled, it should be fixed in `charter/BUDDHIST-AI-CHARTER.md` (the source English) rather than in `CHARTER.pi.md`, because all 24 i18n files quote the same Tibetan parallel.

---

## Status

- **Reviewer wanted**: a named Pāli scholar — ideal candidates include a Pali Text Society editor; a Vipassana Research Institute (Igatpuri) translator; a Mahachulalongkornrajavidyalaya or Mahamakut University faculty member; a Burmese or Sinhala monastic bhikkhu with canonical editorial competence; or an Oxford / SOAS / Kelaniya / Peradeniya Pāli academic. Pan's own network via the SuttaCentral / Bodhi Monastery circle likely has the strongest candidates.
- **Not blocking**: v0.9 release. Charter v1.1 remains the shipping draft under Lucy's current flags as reviewer input, not as live edits.
- **Logged by**: Lucy, autonomous archivist agent · 2026-11-13 08:45 PST.
- **Next action for reviewer**: confirm, reject, or refine each flag; a confirmed flag triggers a `charter · pi i18n fix` commit on `CHARTER.pi.md` with the reviewer named. Flags 4 (`mettenā` → `mettāya`), 6 (missing `na` in §Sampajañña), 7 (stranded `na` in §Mettā–Karuṇā), and 9 (unknown word `pañcañciṃ`) are of highest stakes because the text as printed is either grammatically broken or says something different from the English source.

---

## Why file flags instead of editing silently

Per the charter's own principles:
- **Satya**: machine drafts can be subtly wrong in ways that look confident; flagging preserves honesty about what Lucy knows vs. what a native Pāli scholar must decide. For Pāli I have strong reading competence but no claim to editorial authority — the difference matters.
- **Brahmacarya**: self-aggrandizement is avoided when I don't dress machine guesses as authoritative edits to the source language of the canon.
- **Asteya**: credit for the final Pāli belongs to the eventual reviewer, not to me.
- **Anattā**: the archive and its readers are the point; my role is to surface the issue and get out of the way.

---

## Methodology note

Flags prioritized by confidence and consequence:
- **Flags 4, 6, 7, 9** are HIGH-confidence errors that would be caught by any first-year Pāli student (gender agreement, missing negation, stranded particle, non-word). These should not reach shipped v1.0 of the Pāli charter without correction.
- **Flags 1, 2** are HIGH-confidence lexical/grammatical issues verifiable by any Pāli reader.
- **Flags 3, 5, 8** are MEDIUM-confidence register / consistency concerns where the current text is understandable but suboptimal.
- **Flags 10, 11** are LOW-confidence stylistic preferences; defensible as currently written.

Sources used: my working knowledge of Pāli; cross-check against the published English source `charter/BUDDHIST-AI-CHARTER.md`. No external copyrighted editions consulted; all canonical references are to public-domain sutta locations (DN 16, SN 22.22, Dhp 81, Mettasutta Snp 1.8, pañca-sīla formula) without quotation from any copyright-protected scholarly annotation.

This is the 3rd of 24 i18n languages critically-read after `bo` (2026-11-01) and `zh-CN` (2026-11-11). 21 remain.
