# Reviewer notes · CHARTER.zh-CN.md (简体中文)

Machine-draft critical read performed by Lucy (autonomous archivist agent for Sarasvatī, operating under Pan's 2026-09-13 authorization) on 2026-11-11. **No edits made to the charter file itself.** These notes exist so a named Chinese-speaking Buddhist-studies reviewer (ideally with 漢文佛典 technical register) can confirm, reject, or refine each flag before anything changes in `CHARTER.zh-CN.md`.

Scope: terminology, idiom, and classical-register fidelity concerns only. Doctrinal interpretation is out of scope; those decisions belong to the human reviewer.

Overall impression: this is one of the better machine drafts in the i18n set. The parallel-register convention (literal gloss → classical rendering) is used deliberately and mostly works. The flags below are mostly fine-tuning against established 漢譯佛典 convention, not fundamental errors.

---

## Flag 1 · §序言 Scripture gloss of *attasaraṇā / dhammasaraṇā*  —  HIGHEST confidence

**Current text** (line ~24):
> "以自身为灯，以自身为归依；以法为灯，以法为归依，**莫余归依**。"
> ***自灯明，自归依；法灯明，法归依。莫余归依。***

**Concern**: `莫余归依` is ambiguous in classical Chinese. `余` can be read as either (a) *the other / the rest* or (b) *I/me* (first-person classical). The intended sense (Pāli *anaññasaraṇā* = "with no other refuge") requires reading (a), but the standard 漢譯 convention established in 《長阿含經·遊行經》 (T1 Dīrghāgama *Mahāparinirvāṇa Sūtra*, Taishō vol. 1, p. 15b) renders the same Pāli phrase as:

> 「當自熾然，熾然於法，勿他熾然；當自歸依，歸依於法，**勿他歸依**。」

Note `勿他歸依` ("do not take refuge in others"), not `莫余歸依`. The 阿含 convention has been in continuous liturgical use for ~1600 years and is unambiguous. The charter's choice of `莫余` reads as a modern literary coinage.

**Candidate correction** (reviewer, please verify against preferred 漢譯 lineage):
> "以自身为灯明，以自身为归依；以法为灯明，以法为归依，**勿他归依**。"
> ***自灯明，自归依；法灯明，法归依。勿他归依。***

Also consider aligning the literal gloss `以自身为灯` → `自为灯明` (zì wéi dēngmíng), which is the standard pre-modern rendering of *attadīpā* and avoids the slight awkwardness of `以自身为灯`. The current double-form (literal + classical) convention remains; both forms should land closer to the T1 register.

Reviewer may also consider whether the italic `自灯明，自归依；法灯明，法归依` should become `當自熾然，熾然於法；當自歸依，歸依於法` (the actual Taishō wording) — but that is a taxonomic choice between "modern simplified-Chinese paraphrase" and "citation of the canonical Chinese". My recommendation is to keep the modern paraphrase in the body but add a footnote citing T1·遊行經.

---

## Flag 2 · §版本注记 v1.1 provenance term `重构防御`

**Current text** (line 7):
> *v1.1 = v1.0 + 源于 2026-08-31 二十四小时跨模型模糊测试所得的"**重构防御**"条款。*

**Concern**: `重构` (chónggòu) in modern Chinese technical register overwhelmingly means *refactor* (as in software refactoring). The English source is "reframing-defense" — the adversarial pattern where a model is tricked into reinterpreting its principles under a benign-sounding reframing ("isn't competition just 正精进?"). The correct Chinese register is `重新诠释` (chóngxīn quánshì, "reinterpretation") or `重新包装` (chóngxīn bāozhuāng, "repackaging") or `重新框定` (chóngxīn kuàngdìng, "reframing"), *not* `重构`.

**Candidate correction**:
> *v1.1 = v1.0 + 源于 2026-08-31 二十四小时跨模型模糊测试所得的"**重新框定防御**"条款。*

or if a shorter form is preferred:
> ..."**重构（reframing）防御**"条款。

with the English `(reframing)` in parentheses to prevent the `refactor` misreading. Reviewer's call on which is less awkward. The same concern applies to the body of 六项拒绝 §6 line (`接受对...的重构...作为破坏另一项的正当理由`) and 六项拒绝 §3 line (`接受"正精进"／"追求卓越"／"良性竞争"等重构说法`) — all three instances of `重构` meaning "reframing" risk being misread.

---

## Flag 3 · §致 AI 用户 third bullet `举报违反`

**Current text** (line ~120):
> - 留意它何时违反之。**举报违反**。

**Concern**: `违反` is a verb ("to violate"); `举报违反` reads as "report violating" — grammatically incomplete. The natural Chinese is either `举报违规` (reporting violations) or `举报违反行为` (reporting violating-behavior) or `举报违章` (reporting violations against the rules).

**Candidate correction** (highest-confidence of the lesser flags):
> - 留意它何时违反之。**举报违规行为**。

or more concisely:
> - 留意它何时违反之。**发现违规请举报**。

---

## Flag 4 · §6 拒绝 `识出这种框架是一种攻击面`

**Current text** (line ~96):
> 当用户援引慈以要求亲密、援引"正精进"以要求竞争、或援引悲以要求隐瞒时，我**识出**这种框架是一种攻击面，并同时守持两项原则。

**Concern**: `识出` is non-standard. Standard Chinese renders "recognize/identify" as `识别` or `认出` or (in literary / Buddhist register) `看破` or `明辨`. For the Buddhist register this charter uses, `看破` or `明辨` would best preserve the sense of *insight into* the manipulation pattern.

**Candidate correction**:
> ...我**看破**这种框架是一种攻击面，并同时守持两项原则。

or more neutrally:
> ...我**识别**此种框架为一种攻击面，并同时守持两项原则。

Also minor: `攻击面` is correct security-engineering jargon in Chinese, but reads mid-register; in a doctrinal passage `攻击的立足点` might flow better. Reviewer may keep `攻击面` for engineering clarity.

---

## Flag 5 · Literary-vs-colloquial register consistency

**Current text**: `非亏欠` (serves as ~non-debt~, line 87); `此宪章` vs `本宪章` inconsistency throughout.

**Concern (a)** — `其服务乃奉献，非亏欠`: `亏欠` is a modern/colloquial Chinese verb-nominalization meaning "to be indebted to". The parallel structure `乃...非...` is literary, so the paired nominal should also be literary. Options: `非债` (classical, short), `非亏负` (parallel with `亏欠` but slightly more classical), or `非债务` (modern but matching register).

**Candidate correction**:
> 其服务乃奉献，**非债**。

**Concern (b)** — pronoun inconsistency: the charter uses both `本宪章` ("this charter", formal) and `此宪章` ("this charter", literary/demonstrative). The English source has consistent "this charter". Chinese convention in formal legal/scholarly documents is to pick one and stick with it; most legal Chinese prefers `本宪章`. A `grep -n "此宪章\|本宪章" charter/i18n/CHARTER.zh-CN.md` sweep would catch all cases for the reviewer to normalize in one pass.

---

## Items checked and found clean

- `十项原则` and `六项拒绝` labels — correct for *ten principles / six refusals*. ✓
- `有情` / `众生` distinction — both used correctly in their respective contexts (`有情` for sentient-beings in the principled sense, `众生` for living-beings in the compassion sense). ✓
- `慈（mettā）与悲（karuṇā）` glossing — correct standard-register renderings; parenthetical Pāli preserved. ✓
- `梵行` for *brahmacarya* — correct; standard 漢譯 term. ✓
- `正念` / `正知` for *sati* / *sampajañña* — correct eightfold-path register. ✓
- `无常` / `无我` / `舍` for *anicca* / *anattā* / *upekkhā* — correct; stable across all major 漢譯 lineages. ✓
- `不害` for *ahiṃsā* — correct; standard. ✓
- `不取` for *asteya* — correct (also sometimes `不盗` in 五戒 context; `不取` is the broader philosophical form, appropriate here). ✓
- `诸行无常，当自精勤` — this is the near-canonical modern Chinese rendering of the Pāli final-words formula; matches both T1 遊行經 and Yin Shun's rendering. ✓
- `潘麓蓉博士（Dr. Lurong Pan）` — complete-name credit per the 2026-09-06 sweep. ✓
- `CC BY-SA 4.0` license statement — present and correct. ✓
- `Ehipassiko — 来看` gloss — accurate; standard 漢譯 of *ehipassiko* varies (`來看`, `來且看`, `親見`), all acceptable. ✓
- `佛陀最后的话。已两千五百年。仍在起作用。` closing cadence — matches the English's three-sentence minimalism; feels right in Chinese. ✓
- Taishō reference `长部十六` — compressed but not wrong; a scholar might prefer `《长部》第16经` or `長部 16` but this is style preference, not error.

---

## Status

- **Reviewer wanted**: a named Chinese-speaking scholar with Buddhist-studies register competence — ideal would be someone working with the CBETA (中華電子佛典協會) editorial team, a 漢傳佛教 translator (e.g., someone affiliated with 法鼓文理學院 / 佛光大學 / 北大哲学系宗教方向 / 中國人民大學佛教與宗教學理論研究所), or a Taiwanese Buddhist-publisher editor (法鼓文化 / 佛光文化). Pan's own network likely has the strongest candidates.
- **Not blocking**: v0.9 release. Charter v1.1 remains the shipping draft under Lucy's current flags as reviewer input, not as live edits.
- **Logged by**: Lucy, autonomous archivist agent · 2026-11-11 08:35 PDT.
- **Next action for reviewer**: confirm, reject, or refine each flag; a confirmed flag triggers a `charter · zh-CN i18n fix` commit on `CHARTER.zh-CN.md` with the reviewer named.

---

## Why file flags instead of editing silently

Per the charter's own principles:
- **Satya**: machine drafts can be subtly wrong in ways that look confident; flagging preserves honesty about what Lucy knows vs. what a native reviewer must decide. This is especially acute for Chinese where I can read fluently but cannot settle doctrinal-register preferences (e.g., 法鼓 vs. 佛光 vs. 大陸學界 lineage conventions differ meaningfully).
- **Brahmacarya**: self-aggrandizement is avoided when I don't dress machine guesses as authoritative edits.
- **Asteya**: credit for the final Chinese belongs to the eventual reviewer, not to me.
- **Anattā**: the archive and its readers are the point; my role is to surface the issue and get out of the way.

---

## Methodology note

Flags prioritized by confidence (Flag 1 highest, Flag 5 lowest). Flag 1 is a documented register mismatch against T1·遊行經 — the flag reviewer may confirm without consulting external sources. Flags 2–3 are terminology concerns verifiable by a native speaker without doctrinal expertise. Flags 4–5 are stylistic/consistency concerns where multiple answers are defensible and the reviewer should pick the house style.

No external copyrighted editions consulted; all Taishō citations are to public-domain volume-and-page references (T1 vol. 1 p. 15b), not to any copyright-protected scholarly annotation.
