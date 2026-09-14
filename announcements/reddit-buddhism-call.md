<!-- // draft for Pan to review before posting -->
<!-- License: CC BY-SA 4.0 -->
<!-- Suggested target subs: r/Buddhism (primary), r/Buddhistscholarship, r/Pali, r/sanskrit, r/tibetanbuddhism, r/theravada, r/Buddhism_meta -->
<!-- Suggested flair: Announcement / Community / Help wanted (per sub rules) -->
<!-- Please read each sub's self-promotion rules before posting; this is a help request, not a launch. -->

---

**Title options (pick one):**

- Sarasvatī: a one-person open archive of the 8-branch Buddhist canon + an "AI charter" — asking for help, not attention
- Help wanted: public-domain Buddhist canon archive & a Buddhist AI ethics charter (CC BY-SA, no tokens, no NFTs)
- 求助帖 · Sarasvatī 八系佛典开放归档 + 菩提心 AI 宪章，需要审校与协作

---

## What this is (one sentence)

Sarasvatī is a small, single-person open project with two cores: **(1)** an eight-branch open archive of the world's Buddhist canon, built from public-domain sources under CC BY-SA 4.0, and **(2)** a **Buddhist AI Charter** — ten principles and five hard refusals meant to be wired into AI runtimes as guardrails, not slogans.

It is not a startup. It is not raising money. **No tokens. No NFTs. No equity. No paid tier.** Everything the project produces is released CC BY-SA 4.0 with named human review.

## Honest status (please read before deciding whether to help)

I want to be very direct about what actually exists today, because I have seen too many projects in this space announce themselves as if they had already done the work.

- **Canon archive**: only **one** first sample exists in the repo — a four-language reading of **DN 16** (*Mahāparinibbāna Sutta*) touching the Tibetan and Pāli branches. **The remaining six branches — India, Sanskrit manuscript, Southeast Asian Theravāda, Silk Road, Chinese, Sinosphere — are not started.**
- **Buddhist AI Charter**: exists in **24 languages** under `charter/i18n/`. **Only the English source is human-authored.** Every one of the other 23 language versions is currently an **AI machine draft**. None have been reviewed by a native-speaker Buddhist scholar yet.
- **Charter runtime library**: a Python starter kit is in progress in a side worktree. The TypeScript port is not started.

That is the whole project. One Mac mini, one person, and a stubborn conviction that this is worth doing slowly and in public.

## Guiding rule: AI drafts, humans decide

The working principle throughout the project is **"AI first-draft, human final."** AI is used to produce initial machine drafts, cross-language readings, and scaffolding. Every artifact that carries the project's name is meant to pass through a **named human reviewer** whose name is recorded in `CONTRIBUTORS.md`. Every machine-only draft is marked as such and treated as provisional until a human signs it off.

I am not trying to evangelize AI. I am trying to use AI honestly, at the point in the pipeline where it actually helps, and stop there.

---

## Three concrete asks

### A. Launch the remaining seven branches of the canon archive

The archive is structured along eight transmission branches: **India · Sanskrit manuscript · Pāli · Southeast Asian Theravāda · Silk Road · Tibetan · Chinese · Sinosphere.** Only the Tibetan branch has a first sample (via DN 16); Pāli was touched through the same asset. The other six need **first samples** — one public-domain source text, one AI machine draft into a language currently lacking a translation, one named human reviewer, one CC BY-SA 4.0 release.

Most useful help right now:

- **Philologists and Buddhologists** across any of the eight branches — Vedic/Prakrit, Sanskrit manuscript traditions (GRETIL, Nepal-German, Gilgit), full Pāli sutta reviewers, Burmese/Thai/Khmer/Lao/Shan-script readers, Gāndhārī/Khotanese/Tocharian/Tangut specialists, classical Chinese Buddhologists (CBETA / Taishō vol. 85), Korean/Japanese/Vietnamese Buddhologists (Tripiṭaka Koreana, SAT, Nara).
- **Public-domain source archives**: pointers to clean machine-readable, compatibly-licensed texts we can start from.
- **Reviewers** who are willing to be named and credited on the artifacts they touch — no obligation to review anything you did not personally read.

### B. Native-speaker human review of the Buddhist AI Charter (24 languages)

`charter/BUDDHIST-AI-CHARTER.md` exists in **ar · bo · de · es · fa · fr · hi · id · it · ja · km · ko · mn · my · pi · pt · ru · sa · si · th · tr · vi · zh-CN · zh-TW**. Every non-English version is an AI machine draft. Before the charter can carry any real weight in local traditions or in policy conversations, each version needs a **native-speaker Buddhist / Buddhist-studies scholar** to read it end-to-end and either sign it off or open a pull request with corrections.

Highest-priority reviewers right now:

- **Pāli / Sanskrit specialists** for the doctrinal vocabulary (*ahiṃsā, satya, asteya, brahmacarya, sati, sampajañña, mettā, karuṇā, anicca, anattā, upekkhā*).
- **Tibetan-language Buddhist scholars** for `CHARTER.bo.md`.
- **Sinhala / Burmese / Thai / Khmer** monastics or scholars for the four Theravāda-heartland versions.
- **zh-CN, zh-TW, ja, ko, vi** East Asian Buddhist scholars.
- **Persian / Arabic / Turkish** readers — flagged as the highest-risk for terminology drift into non-Buddhist religious registers.

You can open a PR against `charter/i18n/CHARTER.<lang>.md`, or open an issue `[CHARTER REVIEW <lang>]` if you would rather flag concerns than write a patch.

### C. Charter runtime reference implementation

The charter is currently a **document**. The next step is making it **executable** — a small, auditable library (~500 LOC core, dependency-light, permissive license) that any AI system, agent runtime, or MCP server can import and get the ten principles + five refusals wired in as pre-flight guardrails, with structured attestation logs a downstream auditor can verify.

Two parallel targets:

1. **Python** — `buddhist_ai_guardrail/` — starter kit in progress; PRs welcome once the skeleton is published.
2. **TypeScript / JavaScript** — `@buddhist-ai/guardrail` (npm) — **not started**; if you want to lead the TS port, open a `[CHARTER RUNTIME · TS]` issue and I will hand off the design doc.

Also welcome: real-world adversarial prompts (as GitHub issues) that the five refusals should catch; and integration hooks in agent frameworks (LangChain, LlamaIndex, MCP servers, Anthropic tool-use, OpenAI Assistants, etc.) where such a guardrail could plug in cleanly.

---

## What this project will not do

- No tokens, no NFTs, no fundraising rounds, no equity.
- No sponsors that require exclusivity, private data, or non-open licensing.
- No "AI arms race" positioning. This is a preservation-and-ethics project.
- No pretending machine drafts are finished work.

## Links

- **Repo**: https://github.com/lurongpan47/Sarasvati
- **Site**: https://lurongpan47.github.io/Sarasvati
- **Issues**: https://github.com/lurongpan47/Sarasvati/issues
- **Discussion**: https://github.com/lurongpan47/Sarasvati/discussions
- **License**: CC BY-SA 4.0 across all artifacts.

If any of the three asks fits what you already do, I would be grateful. If you think the whole approach is wrong, I would rather hear that early than late — open an issue and tell me.

*Metta.*

---

## Optional short version (≤ 350 characters, for X / Twitter / Mastodon / Nostr teaser)

> Sarasvatī: a one-person open project — 8-branch Buddhist canon archive + a Buddhist AI Charter (24 langs, all still machine drafts). CC BY-SA 4.0. No tokens, no NFTs. Asking for named reviewers, philologists across the 8 branches, and a TS port of the charter runtime. https://github.com/lurongpan47/Sarasvati
