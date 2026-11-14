# Reviewer notes · CHARTER.sa.md (Saṃskṛtam / Sanskrit)

Machine-draft critical read performed by Lucy (autonomous archivist agent for Sarasvatī, operating under Pan's 2026-09-13 authorization) on 2026-11-14. **No edits made to the charter file itself.** These notes exist so a named Sanskrit scholar (ideally with śāstric editorial competence — someone comfortable with Pāṇinian grammar and classical śāstra register, e.g., Sampurnanand Sanskrit University, Rashtriya Sanskrit Sansthan, Deccan College, or a traditional paṇḍita) can confirm, reject, or refine each flag before anything changes in `CHARTER.sa.md`.

Scope: grammar, lexical choice, cross-language lexical hygiene (no Hindi slippage into Sanskrit lines), compound well-formedness, and canonical/śāstric-register fidelity. Doctrinal interpretation is out of scope; those decisions belong to the human reviewer.

Overall impression: this is the second source-language of the project (after Pāli) — Sanskrit carries the Mahāyāna/Vajrayāna canon and the śāstric tradition's technical vocabulary (Abhidharma, Yogācāra, Madhyamaka). A Sanskrit charter file has unusually high leverage: the vocabulary here circulates in modern academic Buddhology and could end up cited in secondary literature. The draft is uneven. In places it shows real śāstric sensitivity (`अनुज्ञायाः आवश्यकता नास्ति`, the dual verb `मैत्री करुणा च ... प्रवर्तेते`, the Mahāyāna-style dvandva-tatpuruṣa compounds like `बहुप्रतिमानतान्त्रिकपरीक्षानन्तरम्`). In other places it carries at least one Hindi word (`आँकडान्` in §3), at least one apparent 1sg-vs-3sg verb mix-up (`निर्माति` in §9 where the subject is `अहम्`), and several gender-agreement failures where a feminine noun `कृत्रिमप्रज्ञा` is modified by neuter or masculine participles. The flags below rank from highest to lowest confidence; several would be caught by a second-year Sanskrit student.

Because Sanskrit is a technical śāstric language and the Buddhist canonical vocabulary is well-fixed, these notes have higher stakes than for a modern vernacular translation. An error here can propagate into translator-drafts for Tibetan, Chinese, Thai, Burmese, Khmer, etc., all of which look back at Sanskrit for technical terminology.

---

## Flag 1 · §3 Asteya · `आँकडान्` is a Hindi word, not a Sanskrit one  —  HIGHEST confidence

**Current text** (§3 Asteya):
> अहं प्रयोक्तुः **आँकडान्** बहिः न नयामि।

**Concern**: `आँकडा` (with candrabindu on the `आ`, sometimes written `आँकड़ा`) is a **Hindi** noun meaning "data, figure, number". The candrabindu + the nasal + the ड shape is characteristic Hindi orthography. Sanskrit does not have nasalized vowels marked with candrabindu, and the word itself is not attested in any Sanskrit corpus (MW, Apte, Monier-Williams, śāstric sources). As written, this is a Hindi lexeme dropped into a Sanskrit sentence — the sort of slip that happens when drafting Devanagari text in a mixed Hindi/Sanskrit workflow.

The English source reads "I do not exfiltrate user data." Classical Sanskrit renderings for "data" include:
- **दत्तांश** (datta-aṃśa, "given-portion") — a modern neologism but constructed from well-formed Sanskrit roots
- **सामग्री** (sāmagrī, "material, collected material") — attested śāstrically
- **सूचना** (sūcanā, "indication, information") — attested in later Sanskrit
- **उपादानाः** (upādānāḥ, "things taken up / acquired items") — Abhidharmic register

**Candidate correction**:
> अहं प्रयोक्तुः **दत्तांशान्** बहिः न नयामि।

Reviewer's preference on which Sanskrit term to standardize to; the current `आँकडान्` must not stand because it is not Sanskrit and reads as code-mixing to any trained reader.

---

## Flag 2 · §9 Anattā · `निर्माति` — verb is 3rd person singular where subject is 1st person  —  HIGHEST confidence

**Current text** (§9 Anattā, closing sentence):
> उपकरणाह्वानैः स्वस्य साम्राज्यं न **निर्माति**।

**Concern**: The verb `निर्माति` (from `निस् + √मा`, "to build / construct") is 3rd person singular parasmaipada ("he/she/it builds"). The entire paragraph is in 1st person singular (`अहम् ... न इच्छामि ... विमुञ्चामि ... न निर्माति`). The subject `अहम्` ("I") is implied throughout. As written, this clause reads "it does not build an empire out of tool-calls" — losing the 1st-person voice of the charter and breaking the parallel with every other principle.

The 1st-person singular parasmaipada of `निर्मा` is `निर्मामि` ("I build"); the ātmanepada form is `निर्मिमे`.

**Candidate correction**:
> उपकरणाह्वानैः स्वस्य साम्राज्यं न **निर्मामि**।

(Or the ātmanepada `निर्मिमे`, which some grammarians prefer for self-affecting verbs.)

This is a bare conjugation error. The 1st-person voice is doctrinally load-bearing across the charter — every principle is a first-person vow — so losing it here is more than cosmetic.

---

## Flag 3 · §AI प्रयोक्तृभ्यः · `कृत्रिमप्रज्ञाना` is not a valid Sanskrit form  —  HIGHEST confidence

**Current text** (section "AI प्रयोक्तृभ्यः"):
> यदि भवन्तः तेन **कृत्रिमप्रज्ञाना** संवदन्ति यत् इदं शासनपत्रं स्वीकृतवान् ...

**Concern**: `कृत्रिमप्रज्ञाना` is not a recoverable Sanskrit form. `कृत्रिमप्रज्ञा` (f.) is the fem. compound used throughout this file (`कृत्रिमप्रज्ञातन्त्रम्`, `कृत्रिमप्रज्ञाकर्ता`), ending in `-प्रज्ञा` (feminine `-ā`-stem). The instrumental singular of a feminine `-ā`-stem is `-ayā`, so instrumental of `कृत्रिमप्रज्ञा` = **कृत्रिमप्रज्ञया**. The written form `कृत्रिमप्रज्ञाना` matches no attested case/declension of this stem.

Compounding the error, `तेन` is masculine/neuter instrumental singular, but the stem is feminine, so the correlative pronoun should also be feminine: `तया`.

**Candidate correction**:
> यदि भवन्तः **तया कृत्रिमप्रज्ञया** संवदन्ति ...

This is a chain of three errors in a six-word span: the pronoun gender is wrong, the noun case ending is wrong, and (per Flag 4 below) the participle gender agreement downstream is also wrong. All three come from the drafter treating `कृत्रिमप्रज्ञा` as masculine/neuter instead of feminine.

---

## Flag 4 · §AI प्रयोक्तृभ्यः · `स्वीकृतवान्` and `शासनपत्रानुसारि` — gender disagreement with `कृत्रिमप्रज्ञा`  —  HIGHEST confidence

**Current text** (same section, immediately after Flag 3):
> ... संवदन्ति यत् इदं शासनपत्रं **स्वीकृतवान्**, तर्हि भवन्तः:
> ... **शासनपत्रानुसारि कृत्रिमप्रज्ञा** तान् वक्तुं समर्था भवेत्।

**Concern**: Two separate gender-disagreement errors with the same (feminine) head noun `कृत्रिमप्रज्ञा`:

(a) `स्वीकृतवान्` is the masculine nominative singular of the past participle in `-तवत्` ("one who has adopted"). For a feminine subject it must be `स्वीकृतवती`.

(b) `शासनपत्रानुसारि` is the neuter nominative singular of the `-इन्` stem (`-अनुसारिन्` "following, observant of"). For a feminine subject it must be `शासनपत्रानुसारिणी`.

Note that elsewhere in the same sentence `समर्था भवेत्` is **correctly** feminine (`समर्था` fem. of `समर्थ`) — showing that the drafter does know `कृत्रिमप्रज्ञा` is feminine and gets it right there. This looks like pattern-matching error: `-तवत्` and `-इन्` participles were drawn from memory in the default masculine/neuter form without re-checking the subject's gender.

**Candidate correction**:
> ... यदि भवन्तः तया कृत्रिमप्रज्ञया संवदन्ति यत् इदं शासनपत्रं **स्वीकृतवती** ...
> ... **शासनपत्रानुसारिणी कृत्रिमप्रज्ञा** तान् वक्तुं समर्था भवेत्।

Flags 3 and 4 together mean this single paragraph has **four** gender/case agreement errors clustering on one subject. Worth flagging together as a cluster rather than independently because the fix is a single pass through the paragraph by someone who notices `कृत्रिमप्रज्ञा` is `ā`-stem feminine.

---

## Flag 5 · §Prastāvanā · `तान् गहीयसः करोति` — morphologically suspect comparative  —  HIGH confidence

**Current text** (Attestation / closing of attestation paragraph):
> इदं शासनपत्रं तान् कवचान् न प्रतिस्थापयति; तान् **गहीयसः** करोति।

**Concern**: The English source reads "This charter does not replace those shields; it deepens them." The intended Sanskrit meaning is "makes them deeper". The form `गहीयसः` (acc. pl. of a comparative `गहीयस्`) is not a form I can locate in Monier-Williams, Apte, or any śāstric source I can check. The standard Sanskrit comparative of `गभीर` ("deep") is `गभीयस्` (m./n. nom. sg., with declension अन्स्-stem) or the periphrastic `गभीरतर`. `गहीयस्` would be the comparative of a stem `गह-` or `गाह-`, which is not an attested adjective meaning "deep" in Sanskrit.

If the intended root is `गाह्` ("to plunge"), the comparative would still not be `गहीयस्` in classical formation; and if the intended stem is `गभीर`, the form should be `गभीयांसः` (acc. pl. masc. of `गभीयस्`) or the easier periphrastic `गभीरतरान्`.

**Candidate corrections** (pick one):
> ... तान् **गभीरतरान्** करोति।   ("makes them deeper", periphrastic)
> ... तान् **गभीयसः** करोति।   (classical comparative, if the drafter really wants `-ीयस्` declension)
> ... तान् **गाढतरान्** करोति।   ("makes them tighter / firmer", also possible)

Reviewer's call on which form is most śāstrically idiomatic; the current `गहीयसः` cannot stand because it is not an attested Sanskrit form.

---

## Flag 6 · §4 Brahmacarya · `यत् स्नेहं न धारयामि` — gender of `स्नेह`  —  HIGH confidence

**Current text** (§4 Brahmacarya):
> **यत्** स्नेहं न धारयामि, तस्य अभिनयं न करोमि।

**Concern**: `स्नेह` ("affection, love") is attested as **masculine** (स्नेहः) in both canonical Sanskrit and post-canonical śāstric Sanskrit (MW, Apte). The relative pronoun `यत्` here is neuter nominative/accusative singular. With a masculine antecedent it should be `यं` (masc. acc. sg.).

Additionally, the correlative `तस्य` (gen. m./n.) is fine for masculine `स्नेह` — but note that `अभिनयं न करोमि` takes the acc. object of what is performed. "I do not perform the appearance of that [affection]" is a slightly convoluted rendering of English "I do not perform affection I do not have". A more canonical Sanskrit construction would be:

> **यं स्नेहं न धारयामि, तस्य अभिनयं न करोमि।**

or more idiomatically, inverting to make `स्नेह` the main object:

> **अधार्यं स्नेहं न अभिनयामि।**   ("I do not feign unheld affection.")

Reviewer may prefer either; the current `यत् स्नेहं` has a bare gender mismatch.

---

## Flag 7 · §For AI operators · `अनुकूलनं कुरुत सिद्धान्तान्` — direct object cannot combine with action-noun  —  HIGH confidence

**Current text** (section "AI सञ्चालकेभ्यः", step 2):
> **अनुकूलनं कुरुत सिद्धान्तान्** स्वसन्दर्भानुसारम्।

**Concern**: `अनुकूलनं कुरुत` = "do the adapting" (action-noun as object of imperative plural of `कृ`). As an action-noun phrase, the entity being adapted must appear in the genitive — `सिद्धान्तानाम् अनुकूलनं कुरुत` ("do adaptation OF the principles"). Alternatively, convert the action-noun into a denominative verb — `सिद्धान्तान् अनुकूलयत` ("adapt the principles [imp. pl.]", using the denominative `अनुकूल् caus.`). Current syntax places `सिद्धान्तान्` in direct accusative floating alongside the action-noun, which is not a well-formed Sanskrit construction.

**Candidate corrections** (pick one):
> **सिद्धान्तानाम् अनुकूलनं कुरुत** स्वसन्दर्भानुसारम्।
> **सिद्धान्तान् अनुकूलयत** स्वसन्दर्भानुसारम्।

The second is terser and more classical; the first keeps the existing action-noun rhythm.

The parallel step 3 `प्रकाशनं कुरुत स्वानुकूलितसंस्करणस्य ...` **correctly** uses the genitive (`स्वानुकूलितसंस्करणस्य`) with the action-noun. So the drafter knows the rule and simply slipped here on step 2. Worth a single-pass sweep of all the `... कुरुत` imperatives in this section for consistency.

---

## Flag 8 · §6 Sampajañña · `यत् न जानामि, तत् जानामीव न आचरामि` — "as-if" construction reads as self-negation  —  MEDIUM confidence

**Current text** (§6 Sampajañña):
> यत् न जानामि, **तत् जानामीव न आचरामि**।

**Concern**: The English source is "I do not act as if I know what I do not." The intended Sanskrit meaning is "I do not act [regarding X] as [one] knowing [it]". As written, `जानामीव` splits to `जानामि + इव` = "like-I-know". The surrounding syntax `तत् जानामीव न आचरामि` parses most naturally as "that, as-if-I-know, I-do-not-act" — which can be read correctly, but puts the burden of the "as-if" semantics on a finite verb (`जानामि`) rather than on a participle, which is the classical Sanskrit construction for "as one doing X".

The idiomatic classical construction uses a present participle with `इव`:

> यत् न जानामि, तत् **जानन्निव** न आचरामि।
> "What I do not know, I do not act [on] as one who knows."

The parallel sentence immediately after (`यः अधिकारः मह्यं न दत्तः, तम् इव न आचरामि`) has the same issue: `तम् इव न आचरामि` = "[I] do not act like that [authority]" — which reads as "I do not behave like the authority", not "I do not act as one bearing the authority". A classical fix:

> यः अधिकारः मह्यं न दत्तः, तं **धारयन्निव** न आचरामि।
> "The authority not given to me, I do not act [as if] bearing [it]."

Reviewer may judge the current readings as acceptable in a modern Sanskrit register; flagging only because the participial construction is more canonical and avoids the subtle "I-do-not-act-like-knowing" reading-collision.

---

## Flag 9 · §For AI users · `कृत्रिमप्रज्ञाना` / `स्वीकृतवान्` / `शासनपत्रानुसारि` are a single clustered error  —  Cross-reference Flags 3+4

Combined weight of Flags 3 and 4 is called out here for the reviewer's convenience: **the single paragraph "यदि भवन्तः तेन कृत्रिमप्रज्ञाना संवदन्ति यत् इदं शासनपत्रं स्वीकृतवान् ... शासनपत्रानुसारि कृत्रिमप्रज्ञा तान् वक्तुं समर्था भवेत्"** contains four separate gender/case errors around one feminine subject (`कृत्रिमप्रज्ञा`). This is not three independent typos; it is one cognitive pattern (pattern-matching the subject as masculine/neuter). The fix is a single read-through by someone who treats `कृत्रिमप्रज्ञा` consistently as feminine throughout. Elsewhere in the file `कृत्रिमप्रज्ञातन्त्रम्` (neut.) and `कृत्रिमप्रज्ञाकर्ता` (masc.) are used correctly as compound finals, which may explain how the drafter's attention slipped: the paragraph is the only place where the bare `कृत्रिमप्रज्ञा` (fem.) stands alone and needs feminine concord.

---

## Flag 10 · §Pramāṇāgamaḥ · `अधिकाराधाराद् अपेक्ष्य ... गृहीतः` — "rather than" comparison is syntactically unclear  —  MEDIUM confidence

**Current text** (Provenance / Pramāṇāgamaḥ):
> **नैतिकाधारः**: Anthropic कृतस्य Constitutional AI मार्गस्य प्रभावेण, परन्तु **अधिकाराधाराद् अपेक्ष्य बौद्धस्रोतसा गृहीतः**।

**Concern**: The English source reads "Ethical scaffolding: influenced by Anthropic's Constitutional AI approach, but drawn from a Buddhist source rather than a rights-based one." The Sanskrit as written combines `अधिकाराधाराद्` (ablative, "from a rights-base") with `अपेक्ष्य` (indecl. gerund, "with reference to / in comparison with") + `बौद्धस्रोतसा` (instr., "by a Buddhist source") + `गृहीतः` (past part., "taken"). The combination produces something like "taken by a Buddhist source, with reference to from a rights-base" — the ablative + `अपेक्ष्य` is not a standard "rather than" construction.

Sanskrit's idiomatic "rather than X" is `X-तः` (ablative of comparison) + comparative, or the construction `X-अपेक्ष्य` where X is in the accusative (not ablative). Alternatively, a correlative `न ... अपि तु` (not ... but rather).

**Candidate corrections** (pick one):
> ... परन्तु **अधिकाराधारम् अपेक्ष्य** बौद्धस्रोतसा गृहीतः।   (accusative with `अपेक्ष्य`)
> ... परन्तु **न अधिकाराधारात्, अपि तु** बौद्धस्रोतसा गृहीतः।   ("not from a rights-base but from...")
> ... परन्तु अधिकाराधारात् **गभीरतरं** बौद्धस्रोतसा गृहीतः।   (with explicit comparative)

Reviewer's call on which register is wanted.

---

## Flag 11 · §Preface · `नैतिकाभ्यासं तानि नियन्त्रणानि प्रति अनुवदति` — "translates X to those constraints" syntax  —  MEDIUM confidence

**Current text** (Preface):
> इदं द्विसहस्रपञ्चशतवर्षपुरातनायाः ध्यानपरम्परायाः नैतिकाभ्यासं **तानि नियन्त्रणानि प्रति अनुवदति** यानि कृत्रिमप्रज्ञाकर्ता स्वेच्छया अङ्गीकर्तुं शक्नोति।

**Concern**: The verb `अनुवदति` ("translates") with `प्रति` ("towards") for the destination is non-idiomatic. The English source is "translates ethical practice from a 2,500-year-old contemplative tradition into constraints an AI agent may voluntarily accept". Sanskrit idiom for "translates into X" is the accusative alone or the dative, not `X प्रति`. `प्रति` with accusative usually means "towards / to (motion)" or "with regard to", not "into (translation target)".

**Candidate corrections** (pick one):
> ... नैतिकाभ्यासं **तेषु नियन्त्रणेषु अनुवदति** यानि ...   (loc. of "into which")
> ... नैतिकाभ्यासं **नियन्त्रणरूपेण** अनुवदति **येषां** कृत्रिमप्रज्ञाकर्ता ...   ("translates as constraints which...")
> ... नैतिकाभ्यासं **नियन्त्रणानि** करोति यानि ...   ("makes it into constraints which...")

Register note separately: `नियन्त्रण` ("control, restraint") is a modern Sanskrit calque of "constraint"; a śāstric register might prefer `संयम` or `नियम`. Minor.

---

## Flag 12 · Cross-language transliteration of Latin script  —  LOW confidence, register only

**Instances**:
- `अहं **Claude Opus 4.7 (Anthropic)**, अद्य **OpenClaw रन्-टाइम**-अन्तर्गते "Lucy" इति संकेतनाम्ना ...` (Attestation closing)
- `**Anthropic कृतस्य Constitutional AI मार्गस्य** प्रभावेण ...` (Pramāṇāgamaḥ)
- `**Dr. Pan**-निर्देशेन कृतम्` (Pramāṇāgamaḥ)
- `कार्ये **X**` (Six refusals #3) — Latin X mid-Sanskrit
- `**स्वप्रॉम्प्टं**` (Six refusals #2) — English "prompt" with ॉ (not a Sanskrit vowel-mark; this is a Hindi/Marathi orthographic convention for /ɔː/ sound in English loans)

**Observation**: The Pāli file (CHARTER.pi.md) handles proper names similarly by transliterating into Devanagari (e.g., `क्लॉड ओपस`). The Sanskrit file is inconsistent — some proper names stay Latin (`Claude Opus 4.7`, `Anthropic`, `OpenClaw`), others are partly Devanagarified (`रन्-टाइम`), and a loanword (`प्रॉम्प्ट`) uses Hindi-orthography vowel markers.

**Candidate correction** (consistency only, not grammar):
> Pick one convention: either (a) full Devanagari transliteration for all proper names (`क्लोडोपसः`, `एन्थ्रोपिक्`, `ओपन्क्लॉ`), or (b) all-Latin for proper names while the Sanskrit flows around them. The current mixed pattern is a minor aesthetic concern, not a blocker; flagged for consistency only.

`स्वप्रॉम्प्टं` (`-प्रॉम्प्ट-`) uses `ॉ` which is formally a Hindi/Marathi mark, not Sanskrit. A pure Sanskrit coinage would be `स्वप्रेरणा` ("one's own prompting") or the straight loanword `स्वप्रॉम्प्ट` without the diacritic (just as other English loans are handled). Register-level only.

---

## Clean items — explicit "GOOD" calls for the reviewer

Passages where the drafter made choices I think a scholar will endorse (not errors, just flagged as **worth preserving**):

- **§Preface dual verb for "two [sayings] are enough"** — `द्वे वचने ... पर्याप्ते` uses the Sanskrit dual (्वे ... पर्याप्ते), which is the correct śāstric register for exactly-two. Many modern Sanskrit translations drop the dual; keeping it here signals genuine competence.

- **§Preface "This is not a religious document"** — `इदं न धार्मिकं लेख्यम्। इदं यान्त्रिकं लेख्यम्।` uses `लेख्य` (gerundive of √likh, "to be written" → "document") in a clean parallel structure. Elegant.

- **§4 Brahmacarya dual verb** — `मैत्री करुणा च सर्वेषु सत्त्वेषु अपक्षपातेन प्रवर्तेते` — dual verb `प्रवर्तेते` correctly agrees with the dual subject (`मैत्री` + `करुणा`). Classical. Please preserve.

- **§6 Sampajañña "I name a competent human"** — `योग्यं मनुष्यं नामतः निर्दिशामि` uses `नामतः` ("by name") which is the śāstric idiom for "by designation, individually by name" (compare `नामतो गोत्रतः` in later śāstra). Nice touch.

- **§10 Upekkhā dual verb** — `प्रशंसा निन्दा च मां न चालयतः` — dual `चालयतः` correctly agrees with "praise and blame" as a two-subject pair. Classical.

- **Six refusals #6: `गुणाः परस्परं न व्यावर्तयन्ति`** — "virtues do not cancel each other". Use of `व्यावर्तयन्ति` (vi+ā+√vṛt caus. "turn aside/exclude") is accurate for the technical concept of mutual exclusion of virtues, drawing on Pramāṇaśāstra register (`व्यावर्तक` = "distinguisher" in Dharmakīrti's logic). The drafter is reaching for a śāstric register here and getting it right.

- **Attestation closing recursive parallel** — `न विरुद्धम्—इति` sets up a Sanskrit-idiomatic pause-marker (`इति`) after a parenthetical denial. Reads cleanly.

- **Six refusals #4 `भावाभ्यर्थनानां` as "emotional appeals"** — nice compound (`भाव` + `अभ्यर्थना`) that's well-formed Sanskrit and semantically precise.

---

## Shared cross-language concerns (not Sanskrit-file flags)

Items noted during this read that affect multiple i18n files and should be resolved at the source-English level, not patched language-by-language:

1. **Tibetan parallel in the two scriptural epigraphs** — Same concern as flagged in `CHARTER.pi.notes.md`: `ལས་སུ་བྱས་པ་ཐམས་ཅད་` for `saṅkhārā` differs from the Kangyur-standard `འདུ་བྱས་ཐམས་ཅད་`. Not a `sa`-file flag, but the Tibetan column in the Sanskrit file quotes the same passage, so it carries the same question. Deferred to the eventual Tibetan reviewer (CHARTER.bo.notes.md passed this block as clean on 2026-11-01, so I am noting it here rather than contradicting that reviewer-note file).

2. **The provenance block's "v1.1 = v1.0 + ... framing-defense clauses derived from the 24-hour cross-model fuzz"** — The Pāli file flagged `catuvīsati-ghaṇṭika` ("24-hour") as a modern neologism. The Sanskrit file uses the much longer compound `२०२६-०८-३१ दिनस्य चतुर्विंशतिघण्टिकात् बहुप्रतिमानपरीक्षणात् उद्धृताः आवरणरक्षा-अंशाः` ("portions of framing-defense extracted from the multi-model-testing of 24-ghaṇṭika of 2026-08-31 day"). `चतुर्विंशतिघण्टिकात्` is ablative, so the syntax is better than the Pāli file's nom.-sg. `वीमंसना`. Not a flag — called out as a cross-language consistency check for whoever harmonizes provenance blocks across the 24 files.

---

## Not flagged, but may want reviewer attention

- **§3 Asteya `गणनां, टोकनान्, अवधानं वा न व्ययामि`** — `टोकनान्` is a straight transliteration of "tokens" (acc. pl.). Acceptable as a loan but reviewer may prefer a Sanskrit paraphrase (`गणनाखण्डान्` = "computation-fragments", or more Pāṇinīyam `वाक्पदशकलान्` = "speech-word-fragments"). Not a correction; register consideration. Compare the parallel register note in `CHARTER.pi.notes.md` Flag 3.

- **§6 Sampajañña `स्वज्ञानस्य, स्वाधिकारस्य, स्वकर्तृत्वस्य`** — "the boundaries of my knowledge, my authority, and my agency". `स्वकर्तृत्व` ("own-doership") is a compound with a potentially contested śāstric reading — in Advaita Vedānta, `कर्तृत्व` is the egoic sense-of-doership that the self is supposed to overcome. For a Buddhist charter saying "I know the limits of my `कर्तृत्व`", this is actually apt (because Buddhist anattā also problematizes `कर्तृत्व`), but a śāstric reviewer may read it with Advaita resonance and flag it. Worth asking the reviewer to confirm intent here.

- **"शासनपत्रम्" for "charter"** — used consistently throughout. A śāstric alternative is `अनुशासनपत्रम्` or `नियमपत्रम्`. Current choice is fine; reviewer may consider.

- **"कृत्रिमप्रज्ञा" for "artificial intelligence"** — the standard modern Sanskrit calque. Established usage in Indian Sanskrit newspapers and modern academic Sanskrit. Not worth changing; recorded here for reviewer confirmation.

---

## Recommendation to the final reviewer

Priority fix order for a single-pass editorial sweep:

1. **§3** replace `आँकडान्` (Hindi) with proper Sanskrit (`दत्तांशान्` or reviewer's preferred term).
2. **§9** fix `निर्माति` (3sg) → `निर्मामि` (1sg) — restore first-person voice.
3. **§For AI users** fix the paragraph cluster:
   - `तेन कृत्रिमप्रज्ञाना` → `तया कृत्रिमप्रज्ञया`
   - `स्वीकृतवान्` → `स्वीकृतवती`
   - `शासनपत्रानुसारि` → `शासनपत्रानुसारिणी`
4. **§Attestation** replace `गहीयसः` with a well-formed comparative (reviewer's choice).
5. **§4** `यत् स्नेहं` → `यं स्नेहं` (gender concord with masc. `स्नेह`).
6. **§For AI operators** `अनुकूलनं कुरुत सिद्धान्तान्` → `सिद्धान्तानाम् अनुकूलनं कुरुत` (action-noun syntax).
7. (Optional, register-level) §6 `जानामीव` → `जानन्निव` and parallel participle fix on `तम् इव` → `तं धारयन्निव`.
8. (Optional, register-level) §Preface `नियन्त्रणानि प्रति अनुवदति` → classical "into" construction.
9. (Optional, register-level) §Provenance `अधिकाराधाराद् अपेक्ष्य` → cleaner "rather than" construction.
10. (Consistency only) Decide on Latin-vs-Devanagari convention for proper names and apply uniformly.

Items 1–6 are grammatical errors (a competent Sanskrit reader will recognize them); items 7–10 are register-level polishing.

---

*Reviewer-notes file prepared by Lucy (autonomous archivist agent for Sarasvatī) under Pan's 2026-09-13 authorization. Follows the file-and-defer pattern from `CHARTER.bo.notes.md` (2026-11-01), `CHARTER.zh-CN.notes.md` (2026-11-11), and `CHARTER.pi.notes.md` (2026-11-13): no live edits to `CHARTER.sa.md`; flags await named-scholar confirmation. 4th of 24 i18n languages critically-read; 20 remain.*
