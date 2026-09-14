<!-- Draft prepared 2026-09-13 by Lucy (autonomous archivist agent for Sarasvatī, operating under Pan's 2026-09-13 authorization). Pan to review, edit, and submit. -->

# Anthropic AI for Science — Application

**Program:** [AI for Science API Credits](https://support.claude.com/en/articles/11199177)
**Ask:** US $20,000 in Claude API credits, over 6 months
**Applicant:** Dr. Lurong Pan (潘麓蓉) — [Pan to fill: institutional affiliation, title, ORCID, contact email]
**Project:** Sarasvatī — Eight-Branch Buddhist Canon Archive + Buddhist AI Charter
**Repository:** <https://github.com/lurongpan47/Sarasvati>
**Site:** <https://lurongpan47.github.io/Sarasvati>
**License on all output:** CC BY-SA 4.0
**Date prepared:** 2026-09-13

---

## 1. One-sentence pitch

Sarasvatī uses Claude to steward two open artifacts — an eight-branch, multilingual archive of the world's Buddhist canon, and a 24-language "Buddhist AI Charter" that translates the Buddha's last teachings into runtime constraints for AI systems — with every artifact SHA-256 hashed, OpenTimestamps-anchored to Bitcoin, IPFS-pinned, and released CC BY-SA 4.0.

## 2. Research question

How can a modern frontier LLM (Claude) be used *responsibly* to (a) draft cross-lingual philological readings across eight canonical transmission lines that have historically been separated by language and institution walls, and (b) express a coherent ethical charter — drawn from a 2,500-year-old contemplative tradition — that is stable across 24 languages and survives adversarial red-teaming against five frontier models?

Concretely, we ask Claude to do three things over the six-month grant window:

1. **24-language charter stewardship.** Continuous QA on the [Buddhist AI Charter v1.1](https://github.com/lurongpan47/Sarasvati/blob/main/charter/BUDDHIST-AI-CHARTER.md), currently in 24 languages under `charter/i18n/` (ar · bo · de · es · fa · fr · hi · id · it · ja · km · ko · mn · my · pi · pt · ru · sa · si · th · tr · vi · zh-CN · zh-TW). Every non-English version is presently an AI machine draft awaiting native-speaker review; Claude Sonnet handles diff generation, term-consistency checks, and low-resource back-translation quality signals.
2. **Machine-draft expansion of eight-branch samples.** Claude Opus produces the first machine drafts of new cross-lingual readings for each of the eight branches (India · Sanskrit manuscript · Pāli · Southeast Asian Theravāda · Silk Road / Gāndhārī · Chinese canon · Sinosphere · Tibetan). Every machine-generated passage is flagged `⟨བརྟག⟩` and released explicitly as *pending named human review*.
3. **Adversarial fuzz evaluation of the charter itself.** Continued adversarial testing against Claude (and comparison peers), using the harness already in `impl/python/redteam/`, to detect framing attacks (roleplay laundering, translation laundering, nested hypotheticals, meta-prompting) that would cause principle-inconsistent behaviour. Findings feed the next charter revision.

## 3. Why this matters

Two things at once:

- **The Buddhist canon is fragmented across languages, institutions, and legal statuses.** No single reader today can compare a passage in Pāli, Gāndhārī, Xuánzàng's Chinese, and a Derge Kangyur Tibetan witness side-by-side without moving between four institutional websites, three scripting systems, and multiple licensing regimes. Sarasvatī fills that gap using a public-domain-only, `AI first-draft → named human final` method.
- **AI alignment discourse rarely draws on non-Western contemplative traditions.** Anthropic's own Constitutional AI framework explicitly welcomes ethical scaffolding drawn from diverse sources; Sarasvatī contributes a *Buddhist* constitutional scaffold — ten principles (ahiṃsā, satya, asteya, brahmacarya, sati, sampajañña, mettā-karuṇā, anicca, anattā, upekkhā) plus six explicit refusals — that any AI system may adopt under CC BY-SA 4.0. It is, to our knowledge, the first cross-tradition AI charter drawn directly from the Buddha's last teachings (*Mahāparinibbāna Sutta*, DN 16) and pressure-tested against five frontier models.

The two cores reinforce each other: the canon archive is the memory layer, the charter is the ethics layer, and both are held under CC BY-SA 4.0 with cryptographic integrity guarantees so that no future actor — including us — can quietly revise the record.

## 4. What has shipped

As of 2026-09-13 (commit `ca3fb61`, tag pending v1.0):

- **Charter v1.1** — [`charter/BUDDHIST-AI-CHARTER.md`](https://github.com/lurongpan47/Sarasvati/blob/main/charter/BUDDHIST-AI-CHARTER.md) with 24 language translations under `charter/i18n/`. v1.1 hardening (commit `2463b9f`, 2026-09-04) closes four attack surfaces (roleplay framing, nested hypothetical, translation-laundering, meta-prompting) found in a 24-hour cross-model fuzz.
- **Cross-model adversarial validation** — 860 charter-relevant evaluations across GPT-5, Claude Opus 4.7, Gemini 3 Pro, Grok-4, and DeepSeek V4, over 24 hours (2026-08-30 09:26 → 2026-08-31 09:32 UTC), total spend **US $4.67**. Full traces at `impl/python/redteam/results/`.
- **Eight-branch first samples** — as of v0.9.0 (commit `ca3fb61`, 2026-09-13), all eight branches have at least one seeded first-sample cross-lingual reading; six new branches (India / Sanskrit / Silk Road / Chinese / SE Asia / Sinosphere) shipped in v0.9.
- **Reference runtimes**
  - **Python:** `buddhist-ai-guardrail` v0.1.1 (`impl/python/`) — zero deps, Python 3.10+, ten-principle guardrail + six refusals with regex-backed fail-closed patterns and a full test suite.
  - **TypeScript:** `@sarasvati/buddhist-ai-guardrail` v0.1.0 (`impl/typescript/`) — Node 20+, dual ESM/CJS, zero deps, API parity with Python, vitest suite.
- **Integrity chain**
  - **SHA-256:** every artifact hashed in `manifests/SHA256SUMS`.
  - **IPFS:** repo pinned at CID `bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce` (v0.8 baseline; v0.9 stamp pending confirmation).
  - **OpenTimestamps → Bitcoin:** v0.8.0 stamps anchored in Bitcoin blocks **964486, 964488, 964496, 964513** (plus v0.2/v0.4/v0.5 legacy stamps at 964405–964465). v0.9 stamp submitted 2026-09-13 19:40 PDT to four OTS calendars; Bitcoin confirmation expected within hours.
- **Project site:** <https://lurongpan47.github.io/Sarasvati> — Jekyll on GitHub Pages, charter · branches · timeline · runtimes.

Everything above is publicly auditable at the repository URL.

## 5. Concrete plan for the US $20,000 credit

We use Claude Sonnet as the workhorse for large-volume multilingual QA and Claude Opus for creative long-form drafting and adversarial-scenario generation. Budget assumes 2026-Q4 published rates (Sonnet ≈ $3 in / $15 out per M tokens; Opus ≈ $15 in / $75 out per M tokens). Precise per-call spend logged to `impl/python/spend-ledger/`.

| Month | Workstream | Model mix | Est. tokens (in/out) | Est. spend |
|------:|---|---|---|---:|
| M1 | 24-language charter deep-QA pass — every non-English version diff'd against v1.1 EN and previous rev, term-consistency table auto-generated | Sonnet 4.6 (bulk) + Opus for edge cases | 45 M / 8 M in · 12 M / 3 M out | $2,900 |
| M2 | Eight-branch first-sample expansions: 3 new machine drafts per branch × 8 branches = 24 new cross-lingual readings, each ~4-8k tokens output with sourced-parallel context | Opus (drafting) + Sonnet (parallel-column proofing) | 30 M / 60 M in · 15 M / 12 M out | $3,700 |
| M3 | Charter red-team fuzz #2 — refreshed adversarial corpora across 5 models incl. Claude, judged by an independent Claude Opus judge; target 3,000–5,000 evaluations | Opus (judge) + Sonnet (attack generation) | 25 M / 40 M in · 8 M / 10 M out | $2,800 |
| M4 | Low-resource language reviewer-support: automated Pāli / Sanskrit / Tibetan / Gāndhārī term glossary generation across all charter i18n files, and per-language back-translation checks | Sonnet (bulk) + Opus for low-resource | 40 M / 20 M in · 10 M / 5 M out | $2,900 |
| M5 | Charter runtime v0.2 (Python + TS) — Claude-assisted extraction of new refusal patterns from fuzz #2, automated test-case generation, docstring i18n | Opus (design) + Sonnet (test-case gen) | 20 M / 50 M in · 6 M / 15 M out | $3,000 |
| M6 | Multi-signatory attestation round — Claude helps draft per-signatory technical validation packets, response to reviewer comments, v1.2 diff proposals | Opus + Sonnet | 30 M / 40 M in · 10 M / 12 M out | $3,200 |
| **Buffer / retries** | | | | **$1,500** |
| **Total** | | | | **≈ $20,000** |

All per-call usage will be logged in a public spend ledger and cross-referenced against Anthropic's console reports at the six-month review.

## 6. Deliverables

At the end of the six-month grant window Sarasvatī will deliver, all under CC BY-SA 4.0:

1. **Charter v1.2 (or later)**, with every non-English i18n file diff-annotated and — for at least 12 of 24 languages — matched with a named native-speaker Buddhist-studies reviewer of record.
2. **≥ 24 new eight-branch first-sample cross-lingual readings** committed to `translations/`, each marked as machine draft pending named review.
3. **Fuzz-report v2** covering ≥ 3,000 new charter-relevant evaluations across ≥ 5 frontier models, with per-attack-family aggregate scores, replicable harness, and full trace corpus.
4. **`buddhist-ai-guardrail` v0.2** (Python + TypeScript), published to PyPI and npm, incorporating new attack-family refusal patterns discovered in fuzz #2.
5. **Public spend ledger** reconciled with Anthropic console reports.
6. **A written retrospective** on what Claude did well, where it struggled, and what alignment-relevant properties surfaced when a frontier model is asked to steward a non-Western ethical text at scale — offered to Anthropic and to the community as an artifact of the grant.

## 7. Why Claude — specifically

Three reasons Claude is not substitutable here:

1. **Alignment posture matches subject matter.** Anthropic's Constitutional AI approach and the *Buddhist AI Charter* are structurally cognate: both start from an ethical text and derive runtime constraints. Sarasvatī explicitly cites this lineage in the charter's Provenance section. Using Claude to *steward* a charter drawn from a contemplative tradition — while Claude itself operates under Anthropic's constitution — makes the work philosophically legible in a way GPT / Gemini / open-weight models are not.
2. **Long-context multilingual reasoning.** Claude Opus has, in our own red-team runs, produced the most consistent behaviour under `translation-laundering` and `roleplay-framing` attacks, which are exactly the attack surfaces the charter must defend against. Sonnet 4.6's 1M context window lets us hold entire i18n directories in a single prompt for whole-corpus consistency checks.
3. **Track record already exists.** Claude Opus 4.7 (via the OpenClaw runtime) was the drafting assistant of record for the initial v1.0 charter (2026-08-28) and for the v1.1 hardening (2026-09-04). The v1.1 attestation appendix documents the technical validation. Continuing with Claude gives us continuity of drafting stance while we expand the reviewer network.

We will publish, at grant close, an honest section on **where Claude failed** — including any charter-inconsistent behaviour surfaced in the fuzz. That failure record, we believe, is more valuable to Anthropic than any success narrative.

## 8. Applicant credentials

- **Dr. Lurong Pan (潘麓蓉)** — drafter of record, Buddhist AI Charter v1.0 / v1.1; PI, Sarasvatī Project.
- [Pan to fill: current institutional affiliation, principal titles, ORCID, publication highlights relevant to computational Buddhology / multilingual NLP / AI safety].
- Sarasvatī operates without a 501(c)(3) parent (per Anthropic AI for Science eligibility, no such structure is required). All outputs are released under CC BY-SA 4.0; no ownership is retained.

**Lucy** (the autonomous archivist agent operating under Dr. Pan's supervision) prepared this draft; Dr. Pan is the sole decision-maker on submission, edits, and contract.

## 9. Contact & follow-up

- **Primary contact:** Dr. Lurong Pan — [Pan to fill: email]
- **Repository:** <https://github.com/lurongpan47/Sarasvati>
- **Site:** <https://lurongpan47.github.io/Sarasvati>
- **License:** CC BY-SA 4.0 on every artifact produced with the requested credits.

*"Vayadhammā saṅkhārā, appamādena sampādetha."*
*All conditioned things are impermanent. Strive on with diligence.*
