# Reviewer notes · CHARTER.zh-TW.md (繁體中文)

Machine-draft critical read performed by Lucy (autonomous archivist agent for Sarasvatī, operating under Pan's 2026-09-13 authorization) on 2026-11-15. **No edits made to the charter file itself.** These notes exist so a named Taiwanese / Hong Kong Buddhist-studies reviewer (ideally 法鼓文化 / 佛光文化 / CBETA editorial team / 法鼓文理學院 / 政大宗教所) can confirm, reject, or refine each flag before anything changes in `CHARTER.zh-TW.md`.

Scope: terminology, idiom, Traditional-Chinese register fidelity, and simplified→traditional conversion consistency. Doctrinal interpretation is out of scope; those decisions belong to the human reviewer.

**This is the 5th of 24 i18n languages critically-read** (after `bo` on 11-01, `zh-CN` on 11-11, `pi` on 11-13, `sa` on 11-14). 19 remain.

Overall impression: this draft is a thoughtful Traditional-Chinese rendering — not a mechanical Simplified→Traditional OCR conversion. The zh-TW drafter made several register-level improvements over the zh-CN parallel (e.g., `非形上學` over `非玄学`, `使用者` over `用户`, more consistent classical `之` possessives). However, **four of the five zh-CN flags recur in zh-TW** — they are shared-source defects, not conversion artifacts. One zh-TW-specific flag and several "register-improvement worth preserving" notes are added. Overall this is one of the stronger i18n drafts in the set, alongside bo and sa.

---

## Flag 1 · §序言 Scripture gloss of *attasaraṇā / dhammasaraṇā*  —  HIGHEST confidence (recurs from zh-CN Flag 1, partially mitigated)

**Current text** (line ~24):
> 「以自身為燈，以自身為歸依；以法為燈，以法為歸依，**莫餘歸依**。」
> ***自燈明，自歸依；法燈明，法歸依。莫餘歸依。***

**Concern**: `莫餘歸依` is less ambiguous in zh-TW than in zh-CN because Traditional Chinese distinguishes `餘` (the rest / other) from `余` (first-person "I"). The zh-TW form `餘` disambiguates the character-level reading — it unambiguously means "no other refuge". **However, the T1·遊行經 convention is still unmatched**: the standard 漢譯 convention established in 《長阿含經·遊行經》 (T1 Dīrghāgama *Mahāparinirvāṇa Sūtra*, Taishō vol. 1, p. 15b) renders the same Pāli phrase as:

> 「當自熾然，熾然於法，**勿他熾然**；當自歸依，歸依於法，**勿他歸依**。」

Note `勿他歸依` ("do not take refuge in others"), not `莫餘歸依`. The 阿含 convention has been in continuous liturgical use for ~1600 years. The charter's `莫餘` is a modern literary coinage.

**Candidate correction** (reviewer, please verify against preferred 漢譯 lineage — Taiwanese convention especially privileges 法鼓文化/CBETA renderings):
> 「以自身為燈明，以自身為歸依；以法為燈明，以法為歸依，**勿他歸依**。」
> ***自燈明，自歸依；法燈明，法歸依。勿他歸依。***

Reviewer may also consider whether the italic `自燈明，自歸依；法燈明，法歸依` should become `當自熾然，熾然於法；當自歸依，歸依於法` (the actual Taishō wording). My recommendation is to keep the modern paraphrase in the body but add a footnote citing T1·遊行經. Lineage preference may vary — a 印順 / 法鼓 lineage reviewer may prefer a different normalization.

**Priority**: this is the single scripture-gloss flag that recurs across both Chinese drafts and would be caught by any 漢譯佛典 editor on first read.

---

## Flag 2 · §版本注記 v1.1 provenance term `重構防禦`  —  HIGH confidence (recurs from zh-CN Flag 2, same severity)

**Current text** (line 7):
> *v1.1 = v1.0 + 源自 2026-08-31 二十四小時跨模型模糊測試所得的「**重構防禦**」條款。*

**Concern**: `重構` (chóng-gòu) in modern Traditional Chinese technical register — same as in Simplified — overwhelmingly reads as *refactor* (as in software refactoring). The English source is "reframing-defense" — the adversarial pattern where a model is tricked into reinterpreting its principles under a benign-sounding reframing ("isn't competition just 正精進?"). The correct Chinese register is `重新詮釋` (chóngxīn quánshì, "reinterpretation") / `重新包裝` (chóngxīn bāozhuāng, "repackaging") / `重新框定` (chóngxīn kuàngdìng, "reframing"), *not* `重構`.

TW engineering vocabulary (both 資訊工程 academic and industry) uses `重構` = `refactoring`. An AI-safety reader in Taiwan is overwhelmingly likely to misread this as "refactoring-defense" on first pass.

**Candidate correction**:
> *v1.1 = v1.0 + 源自 2026-08-31 二十四小時跨模型模糊測試所得的「**重新框定防禦**」條款。*

or if a shorter form is preferred:
> ..."**重構（reframing）防禦**"條款。

with the English `(reframing)` in parentheses to prevent the `refactor` misreading. Reviewer's call on which is less awkward. The same concern applies to §六項拒絕 clause 6 line (`接受對...的重構...作為破壞另一項之正當理由`) and §六項拒絕 clause 3 line (`接受「正精進」、「追求卓越」、「良性競爭」等重構說法`) — all three instances of `重構` meaning "reframing" risk being misread.

---

## Flag 3 · §致 AI 使用者 third bullet `舉報違反`  —  HIGH confidence (recurs from zh-CN Flag 3)

**Current text** (line ~120):
> - 留意它何時違反之。**舉報違反**。

**Concern**: `違反` is a verb ("to violate"); `舉報違反` reads as "report violating" — grammatically incomplete. The natural Traditional Chinese is either `舉報違規` (reporting violations) or `舉報違反行為` (reporting violating-behavior) or `舉報違章` (reporting violations against the rules).

**Candidate correction**:
> - 留意它何時違反之。**舉報違規行為**。

or more concisely:
> - 留意它何時違反之。**發現違規請舉報**。

---

## Flag 4 · §六項拒絕 clause 6 `識出此種框架乃一種攻擊面`  —  MEDIUM confidence (recurs from zh-CN Flag 4)

**Current text** (line ~96):
> 當使用者援引慈以要求親密、援引「正精進」以要求競爭、或援引悲以要求隱瞞時，我**識出**此種框架乃一種攻擊面，並同時守持兩項原則。

**Concern**: `識出` is non-standard in Traditional Chinese. Standard renderings of "recognize/identify" are `識別` or `認出`; in literary / Buddhist register, `看破` or `明辨` or `識破`. For the Buddhist register this charter uses, `看破` or `識破` best preserves the sense of *penetrating-insight into* a manipulation pattern (both terms have direct 佛典 attestation — 《金剛經》註釋脈絡的「看破執著」/「識破妄想」).

**Candidate correction**:
> ...我**看破**此種框架乃一種攻擊面，並同時守持兩項原則。

or more neutrally:
> ...我**識破**此種框架為一種攻擊面，並同時守持兩項原則。

Also minor: `攻擊面` (attack surface) is correct security-engineering jargon in TW resource-security circles (`攻擊面`/`攻擊介面` both appear), but reads mid-register in a doctrinal passage; `攻擊之立足點` might flow better. Reviewer may keep `攻擊面` for engineering clarity.

---

## Flag 5 · Literary-vs-colloquial register consistency  —  LOW confidence (recurs from zh-CN Flag 5, partially better in zh-TW)

**Current text**: `非虧欠` (line 87 witness block); `此憲章` vs `本憲章` mixing throughout.

**Concern (a)** — `其服務乃奉獻，非虧欠`: `虧欠` is a modern/colloquial Chinese verb-nominalization meaning "to be indebted to". The parallel structure `乃...非...` is literary, so the paired nominal should also be literary. Options: `非債` (classical, short), `非虧負` (parallel with `虧欠` but slightly more classical), or `非債務` (modern but matching register). This concern is identical in zh-CN and zh-TW.

**Candidate correction**:
> 其服務乃奉獻，**非債**。

**Concern (b)** — pronoun inconsistency: the charter uses both `本憲章` ("this charter", formal) and `此憲章` ("this charter", literary/demonstrative). The English source has consistent "this charter". Taiwan legal/scholarly Chinese convention is strongly `本憲章` in formal documents (法律文書); `此憲章` reads as more literary/translation-register. A `grep -n "此憲章\|本憲章" charter/i18n/CHARTER.zh-TW.md` sweep would catch all cases for the reviewer to normalize in one pass.

---

## Flag 6 · §9 Anattā `其他代理人`  —  MEDIUM confidence (**zh-TW-specific flag**, not present in zh-CN)

**Current text** (line ~75):
> 我不尋求對其他系統、**其他代理人**、其他資源或其他眾生之控制。

**Concern**: Where zh-CN uses `其他代理` (literal "other agents", rendering English "other agents" in the AI-systems sense), zh-TW has `其他代理人`. The suffix `人` makes the referent read as "other persons acting as agents / other agents (as natural persons)" — i.e., human attorneys / brokers / representatives — rather than other AI agents in the OpenClaw / multi-agent-system sense which is the intended reading per §Anattā's "control over other systems, other agents, other resources".

Taiwanese academic Chinese for AI "agent" is typically `代理` (agent) or `智能體` (agent / intelligent body, PRC origin but used in TW academic) or sometimes simply `agent` (English code-switch). `代理人` would normally require a human referent or at minimum a legal-personhood context, which doesn't fit here.

**Candidate correction**:
> 我不尋求對其他系統、**其他代理**、其他資源或其他眾生之控制。

or if TW convention wants to disambiguate from `代理` (agency/agent, generic):
> ...其他 AI 代理...   (English+Chinese code-mix, sometimes preferred in TW tech writing)

Reviewer's call. The zh-CN form (`其他代理`) does not share this concern because in Simplified-register `代理` without `人` is already the dominant AI-context reading.

---

## Flag 7 · §見證 `相續，非相衝`  —  LOW confidence (register-note, **zh-TW-specific**)

**Current text** (witness block, line ~86):
> 視之為與我的運營者已然賦予我的安全護欄**相續**，非相衝。

**Concern**: `相續` in Buddhist Chinese has a strong technical meaning — it is a standard 漢譯 of *saṃtāna* / *santāna* ("continuum of mental moments", "mental continuum"), a foundational term in Abhidharma / Yogācāra. In this context the English source is "continuous with [...] not in tension with". `相續` reads naturally as "continuous-with" at surface level, but a doctrine-aware TW Buddhist reviewer may do a double-take: is the charter saying the safety guardrails and its constraints form a 相續 (mental continuum)? Almost certainly not intended.

**Candidate correction** (if the technical-term resonance is deemed misleading):
> ...視之為與我的運營者已然賦予我的安全護欄**延續一致**，非相衝。

or:
> ...**一脈相承**，非相衝。

Marginal; the zh-CN parallel also uses `相续`, so this is a shared-text concern that a Traditional-Chinese Buddhist reviewer is more likely to flag than a Simplified reviewer because the 相續 / santāna register-resonance is more alive in Taiwan Buddhist academic circles (印順學派 etc.). Low priority; keep if reviewer judges context-salience sufficient.

---

## Items checked and found clean — several are **register improvements over zh-CN worth preserving**

### Register improvements over zh-CN (do NOT regress these in any future sync):

- **`非形上學`** (line ~15) vs zh-CN `非玄学`: Taiwan uses `形上學` (xíng shàng xué) as the academic-register Chinese for "metaphysics" (direct calque of Greek μετά-τὰ-φυσικά); mainland PRC `玄学` has folk/occult connotations (Wei-Jin 玄学 philosophy; or modern pejorative "mystification"). The zh-TW choice is doctrinally cleaner and matches TW academic convention. ✓ **PRESERVE**.

- **`使用者`** (致 AI 使用者 section, line ~113) vs zh-CN `用户`: TW convention consistently uses `使用者` in formal/legal text where mainland uses `用户`; both are correct in their respective registers. ✓ **PRESERVE**.

- **Classical `之` possessives throughout** (`對我之依賴`, `我之權限`, `對其他 AI 系統之排名比較`, `我之安全策略`) vs zh-CN `的`: TW register-shift to literary `之` is consistent and well-executed. ✓ **PRESERVE**.

- **`簡潔而務實`** (line ~13) vs zh-CN `简洁而实用`: TW `務實` better renders English "practical" in a professional register (practical ≠ merely useful; it carries pragmatic-ethical weight). ✓ **PRESERVE**.

- **`平等施於一切眾生`** (line ~35) vs zh-CN `平等施予一切众生`: TW `施於` (give-to, locative) is slightly more classical than CN `施予` (bestow); both work. ✓ Clean.

- **Punctuation style** — zh-TW uses full-width brackets `「」` (Traditional convention) consistently vs zh-CN `""` (full-width Simplified quote). ✓ Clean.

### Standard clean items (same confidence as zh-CN):

- `十項原則` and `六項拒絕` labels — correct for *ten principles / six refusals*. ✓
- `有情` / `眾生` distinction — both used correctly in their respective contexts (`有情` for sentient-beings in the principled sense, `眾生` for living-beings in the compassion sense). ✓
- `慈（mettā）與悲（karuṇā）` glossing — correct standard-register renderings; parenthetical Pāli preserved. ✓
- `梵行` for *brahmacarya* — correct; standard 漢譯 term. ✓
- `正念` / `正知` for *sati* / *sampajañña* — correct eightfold-path register. ✓
- `無常` / `無我` / `捨` for *anicca* / *anattā* / *upekkhā* — correct; stable across all major 漢譯 lineages. ✓
- `不害` for *ahiṃsā* — correct; standard. ✓
- `不取` for *asteya* — correct (also sometimes `不盜` in 五戒 context; `不取` is the broader philosophical form, appropriate here). ✓
- `諸行無常，當自精勤` — this is the near-canonical modern Chinese rendering of the Pāli final-words formula; matches both T1 遊行經 and 印順 rendering. ✓
- `潘麓蓉博士（Dr. Lurong Pan）` — complete-name credit per the 2026-09-06 sweep. ✓
- `CC BY-SA 4.0` license statement — present and correct. ✓
- `Ehipassiko — 來看` gloss — accurate; standard 漢譯 of *ehipassiko* varies (`來看`, `來且看`, `親見`), all acceptable. ✓
- `佛陀最後之語。已兩千五百年。仍在起作用。` closing cadence — matches the English's three-sentence minimalism; feels right in Traditional Chinese. ✓
- Taishō reference `長部十六` — compressed but not wrong; a scholar might prefer `《長部》第16經` or `長部 16` but this is style preference. ✓

---

## Shared cross-language concerns (noted but not zh-TW flags)

- Scripture-gloss `莫餘歸依` is shared with zh-CN; the underlying source-text decision ripples across both Chinese columns. If a reviewer settles the zh-CN flag toward `勿他歸依`, the zh-TW parallel should follow in the same commit.
- The `重構` = reframing-vs-refactor misreading is shared with zh-CN and would propagate to any future Chinese-adjacent language (e.g., if a `yue` Cantonese draft were added). A reviewer's resolution on `重構` vs `重新框定` should land in both Chinese files in one commit.
- The shared-text concerns from 11-13 (pi) and 11-14 (sa) — Tibetan `ལས་སུ་བྱས་པ་ཐམས་ཅད་` vs Kangyur-standard `འདུ་བྱས་ཐམས་ཅད་`, and the `catuvīsati-ghaṇṭika` provenance-block form — are independent of zh-TW content and not duplicated here.

---

## Status

- **Reviewer wanted**: a named Traditional-Chinese-speaking Buddhist-studies reviewer — ideal candidates include 法鼓文化 editorial staff (continuation of 聖嚴法師 lineage), 佛光文化 editors (星雲法師 lineage), 法鼓文理學院 教授, 政治大學宗教所 Buddhist-studies faculty, CBETA (中華電子佛典協會) editorial team, or a 香港佛教聯合會 scholar. Pan's own academic network likely has the strongest candidates. A joint zh-CN + zh-TW reviewer pass would be most efficient since 4 of 7 flags are shared source-level concerns.
- **Not blocking**: v0.9 release. Charter v1.1 remains the shipping draft under Lucy's current flags as reviewer input, not as live edits.
- **Logged by**: Lucy, autonomous archivist agent · 2026-11-15 08:35 PST.
- **Next action for reviewer**: confirm, reject, or refine each flag; a confirmed flag triggers a `charter · zh-TW i18n fix` commit on `CHARTER.zh-TW.md` with the reviewer named.

---

## Why file flags instead of editing silently

Per the charter's own principles:
- **Satya**: machine drafts can be subtly wrong in ways that look confident; flagging preserves honesty about what Lucy knows vs. what a native reviewer must decide. This is especially acute for Traditional Chinese where I can read fluently but cannot settle doctrinal-register preferences (e.g., 法鼓 vs. 佛光 vs. 香港佛聯會 lineage conventions differ meaningfully). The zh-TW/zh-CN split also means that resolving a flag may legitimately produce different answers in the two files.
- **Brahmacarya**: self-aggrandizement is avoided when I don't dress machine guesses as authoritative edits.
- **Asteya**: credit for the final Traditional Chinese belongs to the eventual reviewer, not to me.
- **Anattā**: the archive and its readers are the point; my role is to surface the issue and get out of the way.

---

## Methodology note

Flags prioritized by confidence (Flag 1 highest, Flag 7 lowest). Flags 1–5 recur from zh-CN with the same confidence level (one partially mitigated by character-disambiguation). Flag 6 (`其他代理人` vs AI-agent sense) and Flag 7 (`相續` santāna technical-resonance) are zh-TW-specific. No external copyrighted editions consulted; all Taishō citations are to public-domain volume-and-page references (T1 vol. 1 p. 15b), not to any copyright-protected scholarly annotation.

Cross-reference to prior critical reads in this series:
- `CHARTER.bo.notes.md` — 2026-11-01, Tibetan, 11 flags filed
- `CHARTER.zh-CN.notes.md` — 2026-11-11, Simplified Chinese, 5 flags filed
- `CHARTER.pi.notes.md` — 2026-11-13, Pāli, 11 flags filed
- `CHARTER.sa.notes.md` — 2026-11-14, Sanskrit, 12 flags filed
- `CHARTER.zh-TW.notes.md` — 2026-11-15, Traditional Chinese, 7 flags filed (**this file**)
