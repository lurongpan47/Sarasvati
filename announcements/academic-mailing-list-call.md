<!-- // draft for Pan to review before posting -->
<!-- License: CC BY-SA 4.0 -->
<!-- Intended recipients: H-Buddhism, INDOLOGY, Pali (Pali-list), Tibetan-studies lists, plus discipline-specific lists noted at the foot. -->
<!-- Register: formal academic. English primary. Do not post without a real reply-to address and a real institutional or personal affiliation line. -->

---

**Subject:** Call for named reviewers · Sarasvatī: an open eight-branch Buddhist canon archive and a multilingual Buddhist AI Charter (CC BY-SA 4.0)

**From:** [Pan — please fill affiliation / contact]
**Reply-to:** GitHub Issues at https://github.com/lurongpan47/Sarasvati/issues and Discussions at https://github.com/lurongpan47/Sarasvati/discussions

---

## Abstract (≈ 200 words)

Sarasvatī is a small, non-commercial, single-maintainer open project with two coupled objectives. First, it is building an **open archive of the Buddhist canon organised along eight transmission branches** — India, Sanskrit manuscript, Pāli, Southeast Asian Theravāda, Silk Road, Tibetan, Chinese, and Sinosphere — using only public-domain or compatibly-licensed source editions (GRETIL, SuttaCentral / PTS, VRI, CBETA, Tripiṭaka Koreana, SAT, Derge Kangyur, IDP, and comparable holdings). Second, it is drafting a **Buddhist AI Charter**: a compact ethical instrument of ten principles and five refusals, intended to be adopted both as a public document and as an executable guardrail library that AI systems and agent runtimes can import. Every non-English artifact currently in the repository is an **AI machine draft** and is flagged as provisional pending native-speaker review; the project's operational rule is *"AI first-draft, human final."* We are now requesting **named scholarly review** of the canon samples and of the 24-language charter, and technical collaborators on the runtime reference implementation. Everything is released under **CC BY-SA 4.0**. There are no tokens, no NFTs, no fundraising, and no equity structures attached to the project.

## Present state of the repository (as of this posting)

We wish to be candid about the actual state of the work, so that reviewers can assess whether their time is well spent:

- **Canon archive.** Only one first sample presently exists in the repository: a four-language reading of **DN 16 (*Mahāparinibbāna Sutta*)** touching the **Tibetan** and **Pāli** branches. The remaining six branches (India, Sanskrit manuscript, Southeast Asian Theravāda, Silk Road, Chinese, Sinosphere) have not yet been opened.
- **Buddhist AI Charter.** The English source is human-authored. Twenty-three additional language versions are present under `charter/i18n/` and are all **AI machine drafts**, marked in-line with `⟨བརྟག⟩` (Tib. *brtag*, "to be examined") to indicate provisional status. None has yet received a signed human review.
- **Runtime library.** A Python starter kit (`buddhist_ai_guardrail/`) is in progress in a parallel worktree. The TypeScript port has not been started.

## Source-text policy

Only **public-domain or CC-compatible** source editions are used as starting texts. The following are the archives currently on the working list; additions and corrections are welcome:

- **GRETIL** (Göttingen Register of Electronic Texts in Indian Languages) — Sanskrit / Prakrit.
- **PTS** (Pali Text Society) editions in the public domain; **SuttaCentral** machine-readable Pāli; **VRI** (Vipassana Research Institute) Chaṭṭha Saṅgāyana.
- **CBETA** (Chinese Buddhist Electronic Text Association) — Taishō and Xuzangjing, with Taishō vol. 85 gaps explicitly tracked.
- **Tripiṭaka Koreana** and **SAT Daizōkyō** — for the Sinosphere branch.
- **Derge Kangyur / Tengyur** (BDRC / Adarsha / Rangjung Yeshe archives, where licensing permits) — Tibetan branch.
- **IDP** (International Dunhuang Project), Schøyen Collection catalogues, BnF holdings — Silk Road branch (Gāndhārī, Khotanese, Tocharian, Tangut).
- **Nepal-German Manuscript Preservation Project**, **Gilgit** holdings — Sanskrit manuscript branch.

Where a critical edition is not yet in the public domain, we defer to it and cite it, but we do not reproduce it.

## AI-use transparency statement

The project uses large-language-model assistance for (i) initial cross-language machine drafts, (ii) scaffolding of comparative readings across branches, and (iii) the twenty-three non-English charter drafts. Every artifact produced with LLM assistance carries an in-line `⟨བརྟག⟩` marker and a machine-readable provenance record in its front-matter, and is treated as **provisional until a named human reviewer has signed it off**. Human-signed artifacts have the marker removed and the reviewer's name and affiliation recorded in `CONTRIBUTORS.md` and in the artifact's front-matter. We do not present machine drafts as finished scholarship, and we will retract any artifact whose provenance chain is contested by a qualified reviewer.

---

## Request 1 · Named review across the eight branches

For each of the eight branches we are seeking scholars willing to be **named reviewers** on individual samples. A review may be as narrow as a single sutta, a single terminological choice, or a single paragraph. Reviewers are credited on the artifact they reviewed and in `CONTRIBUTORS.md`; no reviewer is asked to attest to material they did not personally read.

Specific needs at present:

- **India** — Vedic and Prakrit philologists; scholars of early Buddhist India able to point to compatibly-licensed critical editions.
- **Sanskrit manuscript** — Sanskritists working from GRETIL / Nepal / Gilgit corpora.
- **Pāli** — a full first-sample sutta beyond DN 16, with named human review.
- **Southeast Asian Theravāda** — Burmese, Thai, Khmer, Lao, and Shan-script readers; access to Fifth / Sixth / Eighth / Ninth Council editions.
- **Silk Road** — Gāndhārī, Khotanese, Tocharian, and Tangut specialists; access to Schøyen / IDP / BnF holdings.
- **Tibetan** — reviewers for the DN 16 sample and nominations for the next Kangyur / Tengyur asset.
- **Chinese** — classical Chinese Buddhologists; CBETA-experienced editors; scholars tracking the Taishō vol. 85 apocrypha gap.
- **Sinosphere** — Korean, Japanese, and Vietnamese Buddhologists working with Tripiṭaka Koreana, SAT, and Nara-period materials.

To volunteer: open a GitHub Issue titled `[REVIEW · <branch> · <text-id>]`, or a Discussion thread if the scope is exploratory.

## Request 2 · Charter i18n review (24 languages)

`charter/BUDDHIST-AI-CHARTER.md` exists in twenty-four languages under `charter/i18n/`:

**ar · bo · de · es · fa · fr · hi · id · it · ja · km · ko · mn · my · pi · pt · ru · sa · si · th · tr · vi · zh-CN · zh-TW**

We are seeking a **single, named, native-speaker Buddhist or Buddhist-studies scholar** to sign off on each version, with priority as follows:

- **Doctrinal-vocabulary reviewers**: Pāli and Sanskrit specialists to verify the technical lexicon (*ahiṃsā, satya, asteya, brahmacarya, sati, sampajañña, mettā, karuṇā, anicca, anattā, upekkhā*) across all versions.
- **`pi` (Pāli)** — a Pāli-list-appropriate reviewer for the doctrinal register.
- **`sa` (Sanskrit)** — an INDOLOGY-appropriate reviewer for Buddhist Sanskrit register.
- **`bo` (Tibetan)** — a Tibetan-studies reviewer familiar with modern doctrinal prose.
- **`si` (Sinhala), `my` (Burmese), `th` (Thai), `km` (Khmer)** — monastics or scholars from the Theravāda heartland.
- **`zh-CN`, `zh-TW`, `ja`, `ko`, `vi`** — East Asian Buddhologists comfortable with modern religious-ethical prose.
- **`mn` (Mongolian)** — a reviewer familiar with the Gelug-inflected modern doctrinal register.
- **`hi` (Hindi), `id` (Indonesian)** — reviewers familiar with modern non-canonical Buddhist prose.
- **`fa` (Persian), `ar` (Arabic), `tr` (Turkish)** — flagged as the **highest-risk group** for terminological drift into non-Buddhist religious registers; reviewers with comparative-religion experience are especially welcome.
- **`de`, `es`, `fr`, `it`, `pt`, `ru`** — European-language Buddhologists.

Reviews may be submitted as pull requests against the relevant file, or as GitHub Issues titled `[CHARTER REVIEW · <lang>]`. Reviewers are added to `CONTRIBUTORS.md` and credited in the artifact's front-matter.

## Request 3 · Runtime reference implementation

The charter is currently a document. We are building a **small, auditable reference library** so that any AI system, agent runtime, or MCP server can import the ten principles and five refusals as pre-flight guardrails, with structured attestation logs a downstream auditor can verify. Design constraints:

- Fewer than 500 LOC in the core.
- Dependency-light; permissive license.
- Refusals exposed as `should_refuse(context) → (bool, reason)`.
- Structured, machine-verifiable attestation logs.
- Test suite covering the five refusal cases.
- Adoptable as a first-class dependency in Anthropic MCP servers, OpenAI Assistants, LangChain, LlamaIndex, and any agent runtime with a `before_tool_call` hook.

Two parallel implementations are planned:

1. **`buddhist_ai_guardrail/` (Python)** — starter kit in progress; PRs welcome once the skeleton lands.
2. **`@buddhist-ai/guardrail` (TypeScript)** — not started. Volunteers to lead the port are invited to open a `[CHARTER RUNTIME · TS]` issue; a design document will be handed off in that thread.

Contributions from scholars of Buddhist ethics on the framing of the five refusals — in particular on the boundary between *upāya* (skilful accommodation) and *musāvāda* (false speech) — are especially welcome, as GitHub Issues under `[CHARTER · ETHICS]`.

---

## Contact and process

- **GitHub Issues**: https://github.com/lurongpan47/Sarasvati/issues
- **GitHub Discussions**: https://github.com/lurongpan47/Sarasvati/discussions
- **Repository**: https://github.com/lurongpan47/Sarasvati
- **Site**: https://lurongpan47.github.io/Sarasvati
- **License**: CC BY-SA 4.0 on all artifacts.

Named reviewers are recorded in `CONTRIBUTORS.md` with the specific artifact and scope they reviewed. No reviewer is asked to attest to material outside their own reading. No contributor is asked to sign the charter as a whole to sign off on a single language version.

## What this project will not do

- No tokens, no NFTs, no fundraising rounds, no equity.
- No sponsorship arrangements that require exclusivity, private data, or non-open licensing.
- No competitive-model positioning; this is a preservation-and-ethics project.
- No presentation of AI machine drafts as finished scholarship.

We would rather do this slowly, in public, and with named human review than quickly and without accountability. If any part of the above fits your expertise, we would be grateful for your time; if the whole approach seems methodologically wrong, we would rather hear that from you now than later.

With respect and *mettā*,

[Pan — signature and affiliation to be filled before sending]

---

## Suggested distribution list (please review before mailing)

- **H-Buddhism** (H-Net) — primary; general Buddhist studies audience.
- **INDOLOGY list** (`indology.info`) — for the Sanskrit, Pāli-adjacent, and India-branch asks.
- **Pali list** — for Pāli-specific reviewers.
- **Tibetan-studies mailing list** (e.g., THL / Tibet-L community lists) — for `bo` reviewers and Kangyur / Tengyur nominations.
- **AAR Buddhism Section** announcements channel (if permitted) — East Asian, Theravāda, and comparative asks.
- **IABS** (International Association of Buddhist Studies) newsletter / member list — for cross-branch nominations.
- **SEAP** (Southeast Asia Program) newsletters at relevant universities — for Burmese / Thai / Khmer / Lao asks.
- **BDRC** community channels — for Tibetan-source pointers.
- **CBETA** and **SAT** mailing lists — for Chinese-canon and Sinosphere asks.
- **DH-buddhology** and adjacent digital-humanities lists — for the runtime-implementation ask.

**Do not** cross-post the same message across lists on the same day; stagger by 48–72 hours and adjust the subject line so that recipients on multiple lists do not experience it as spam. Please also observe each list's charter regarding project announcements versus discussion, and use the reply-to address the list expects (Issues / Discussions above are stable).
