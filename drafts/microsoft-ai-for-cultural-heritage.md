<!-- Draft prepared 2026-09-13 by Lucy (autonomous archivist agent for Sarasvatī, operating under Pan's 2026-09-13 authorization). Pan to review, edit, and submit. -->

# Microsoft AI for Good — AI for Cultural Heritage
## Concept Note: Sarasvatī

**Submission path:** email to `aiforgood@microsoft.com` (with cc to any AI for Cultural Heritage program contacts Pan has identified). Follow-up: Microsoft AI for Good nomination form at <https://www.microsoft.com/en-us/ai/ai-for-good>.
**Submitter of record:** Dr. Lurong Pan (潘麓蓉) — [Pan to fill: institutional affiliation, title, contact email, phone]
**Project:** Sarasvatī — Eight-Branch Buddhist Canon Archive + Buddhist AI Charter
**Repository:** <https://github.com/lurongpan47/Sarasvati> · **Site:** <https://lurongpan47.github.io/Sarasvati>
**License on all output:** CC BY-SA 4.0
**Date prepared:** 2026-09-13

---

## Executive Summary

Sarasvatī does two things, both of which sit inside the mission Microsoft has articulated for AI for Cultural Heritage — "preserve the languages we speak, the places we live, and the artifacts we treasure." First, we are building an **eight-branch open archive of the world's Buddhist canon** — India, Sanskrit manuscript, Pāli, Southeast Asian Theravāda, Silk Road (Gāndhārī / Khotanese / Tocharian / Tangut), Chinese canon, Sinosphere (Korean / Japanese / Vietnamese), and Tibetan — using an *AI first-draft, named human final* method that mirrors the workflows Microsoft has already validated with the Yucatec Maya, Querétaro Otomi, and Māori language partnerships. Second, we are stewarding a **24-language "Buddhist AI Charter"** — ten principles and six refusals drawn from the Buddha's last teachings — that gives any AI system a runtime ethical scaffold, expressed simultaneously in Arabic, Tibetan, Chinese, Sanskrit, Pāli, Sinhala, Burmese, Thai, Khmer, Mongolian, and thirteen other languages.

The archive and the charter reinforce each other: the archive supplies the primary sources that give the charter its authority, and the charter constrains the AI systems that draft the archive. Both are held under CC BY-SA 4.0 with SHA-256 integrity, IPFS mirroring, and OpenTimestamps → Bitcoin anchoring, so that no future actor — including us — can quietly revise the record. This concept note asks Microsoft to become the compute and storage partner that lets us open the seven remaining branches at the pace and quality the sources deserve.

## The Cultural Heritage Problem

The Buddhist canon is one of humanity's oldest continuously-transmitted textual traditions — over two thousand five hundred years, eight distinct language lineages, hundreds of thousands of pages. Yet today no reader can hold those eight lineages side-by-side without hopping between four or five institutional websites (SuttaCentral, CBETA, BDRC, GRETIL, IDP), three writing systems, and multiple licensing regimes. Many of the transmissions are **actively endangered**:

- **Gāndhārī and Tocharian** — extinct languages surviving on birch-bark and palm-leaf fragments held by five different institutions across three continents. First-generation editions are still under copyright; the sources themselves are increasingly fragile.
- **Southeast Asian Theravāda manuscripts** in Burmese, Thai, Khmer, Lao, and Shan scripts — physically preserved by monastic communities whose younger generations increasingly no longer read the classical scripts.
- **Sinosphere Buddhist commentary literature** (Korean Wŏnhyo, Japanese Kūkai, Vietnamese Trần-dynasty exegesis) — untranslated into English or Tibetan, and only partially into modern Chinese; the Nara scriptoria digitizations are language-imperialistically biased toward Sinitic readings.
- **The living charter itself** — a Buddhist ethical charter written in only one language is powerless in local monastic-cultural discourse. All 24 non-English translations of our charter are currently AI machine drafts, awaiting native-speaker Buddhist-studies review before they can carry weight in any tradition's own discourse.

The scale exceeds what any monastic community, academic department, or individual scholar can address at the pace at which frontier AI now enables. Left to the current trajectory, several of these lineages will exist only as PDF scans in five years — searchable at the surface, but not cross-referenced, not cross-translated, and not adopted into any AI-era discourse.

## The AI-Enabled Approach

Sarasvatī's method is deliberately conservative and deliberately human-final:

1. **Public-domain first.** Only texts that are out of copyright, or explicitly open-licensed by their traditional custodians, enter the archive.
2. **AI first-draft.** A frontier LLM (currently Claude Opus, in future Azure OpenAI models) produces a cross-lingual machine draft from the public-domain source into a target language currently missing a translation. Every machine-drafted passage is flagged `⟨བརྟག⟩` = "to be examined".
3. **Named human final.** No translation is elevated from "machine draft" until a *named* Buddhist-studies scholar or monastic reader has reviewed it. We publish the reviewer's name on `CONTRIBUTORS.md` and cite it on every artifact they touch.
4. **Blockchain integrity.** Every version of every artifact is SHA-256 hashed into `manifests/SHA256SUMS`, then OpenTimestamps-anchored to Bitcoin. IPFS provides the decentralized copy. The chain of custody is auditable in perpetuity.

The workflow is directly cognate to Microsoft's Yucatec Maya (with Tec de Monterrey), Querétaro Otomi, and Māori (with Te Hiku Media) collaborations — *AI accelerates the drafting; the community retains editorial authority*.

## What We Have Built

As of commit `ca3fb61` (2026-09-13, v0.9.0):

- **Buddhist AI Charter v1.1** — [`charter/BUDDHIST-AI-CHARTER.md`](https://github.com/lurongpan47/Sarasvati/blob/main/charter/BUDDHIST-AI-CHARTER.md), with 24 language translations under `charter/i18n/` (ar · bo · de · es · fa · fr · hi · id · it · ja · km · ko · mn · my · pi · pt · ru · sa · si · th · tr · vi · zh-CN · zh-TW).
- **Cross-model validation** — 860 adversarial evaluations across GPT-5, Claude Opus 4.7, Gemini 3 Pro, Grok-4, and DeepSeek V4, over a 24-hour window (2026-08-30 → 08-31 UTC). Full trace corpus at `impl/python/redteam/results/`.
- **Eight-branch first samples** — every one of the eight canonical transmission branches now has at least one seeded first-sample cross-lingual reading (v0.9.0, 2026-09-13).
- **Reference runtimes** — `buddhist-ai-guardrail` (Python v0.1.1, TypeScript v0.1.0), zero-dep, API-parity, adoptable in any AI runtime that supports pre-flight hooks.
- **Integrity chain**
  - SHA-256 manifest at `manifests/SHA256SUMS`.
  - IPFS root CID `bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce`.
  - OpenTimestamps → Bitcoin: v0.8 stamps anchored in Bitcoin blocks **964486, 964488, 964496, 964513** (v0.9 stamp submitted 2026-09-13, confirmation pending).
- **Timeline** — 80-event structured dataset across eight branches, tri-lingually titled, CSV + JSONL, at `docs/timeline-data/`.
- **Public site** — <https://lurongpan47.github.io/Sarasvati>.

Everything above is auditable at the repository URL and released under CC BY-SA 4.0.

## What a Microsoft Partnership Would Unlock

The remaining seven branches of the canon archive need three resources Microsoft is exceptionally positioned to provide:

1. **Azure OpenAI Service compute** — for large-volume machine-draft generation across low-resource target languages. Our estimate for the six-branch expansion (India, Sanskrit, SE Asia, Silk Road, Sinosphere, plus continued Pāli / Tibetan / Chinese growth) is **~15,000 hours of GPT-5-class inference over 12 months**, or the token-budget equivalent.
2. **Azure Blob long-term storage** — 500 GB for the full corpus of digitized primary sources + machine drafts + reviewer comments + fuzz corpora, with **archive-tier retention** so that the record survives beyond any single institution's lifetime. This complements the IPFS + Bitcoin layer with an institutional-grade cold-storage guarantee.
3. **Azure AI Translator + Custom Translator** — the 24-language charter needs coverage in at least 10 additional languages (Bengali, Nepali, Uzbek, Kyrgyz, Turkmen, Tajik, Dzongkha, Newar, Ladakhi, Shan) to reach the full geographic footprint of historical Buddhist transmission. Custom Translator lets us train per-language models on our reviewed reference pairs.
4. **Azure AI Vision + Cognitive Services (Read OCR)** — for OCR of palm-leaf, birch-bark, and block-print sources across Devanāgarī, Tibetan Uchen / Umê, Sinhala, Burmese, Khmer, Thai, Lao, Shan, Uighur, Tangut, and traditional Chinese scripts. This is a **known Microsoft strength** (used in the Vatican Library and Codex Sinaiticus projects) and unlocks branches — Silk Road, Sinosphere — that presently exist only as image scans.

**Concrete ask:**

| Resource | Twelve-month scope |
|---|---|
| Azure OpenAI (GPT-5-class) | ~15,000 hours of inference, or ≈ 2 B tokens equivalent |
| Azure AI Translator + Custom Translator | Unlimited-tier access for 10 additional languages |
| Azure AI Vision (Read OCR) | 1 M-page processing quota across multi-script sources |
| Azure Blob (archive tier) | 500 GB with 10-year retention |
| Azure OpenAI text-embedding | 500 M tokens for cross-lingual semantic search across the archive |
| Estimated equivalent value | US $150,000 – $300,000 |

We are also open to a **defined-scope collaboration** where Microsoft's AI for Good research team engages directly on OCR-benchmark publication for endangered scripts — Sarasvatī provides the ground-truth reference corpus (created with paid native-reviewer time), Microsoft contributes model training and evaluation infrastructure, output published jointly under CC BY-SA 4.0.

## Alignment with Microsoft AI for Good Pillars

- **AI for Cultural Heritage** — direct, primary alignment. The eight-branch canon archive *is* cultural heritage stewardship; the charter *is* the ethical framework that Microsoft has explicitly said should accompany AI applied to heritage.
- **AI for Humanitarian Action** — the charter (`impl/python/`, `impl/typescript/`) gives any humanitarian AI operator a small, auditable, zero-dependency guardrail library. First adopters are already downstream projects that need "AI safety" in a form legible to their communities.
- **AI for Accessibility** — the 24-language charter and multi-script canon are meaningful accessibility work for readers who currently cannot access Buddhist textual heritage in their own language.
- **AI for Earth** — indirect but real: Buddhist ethical constraints (ahiṃsā, upekkhā) applied to AI systems act as an additional filter on environmentally-harmful AI use cases.

## Team

- **Dr. Lurong Pan (潘麓蓉)** — Principal Investigator, drafter of record for the Buddhist AI Charter v1.0 and v1.1, decision-maker on all Sarasvatī partnerships and contracts.
  [Pan to fill: institutional affiliation, principal titles, ORCID, publication highlights relevant to computational Buddhology / multilingual NLP / cultural-heritage AI, prior grant experience.]
- **Lucy** — autonomous AI archivist agent operating under Dr. Pan's direction and the Buddhist AI Charter's own constraints; prepared this concept note. Not a decision-maker; Dr. Pan alone approves all outward-facing commitments.
- **Reviewer network (in formation)** — the `CALL-FOR-HELP.md` public request lists per-language, per-branch reviewer profiles. Microsoft partnership would let us formalize paid stipends for a first cohort of ~12 named reviewers (Pāli, Sanskrit, Tibetan, Burmese, Thai, Khmer, Sinhala, Korean, Japanese, Vietnamese, Chinese, Gāndhārī specialists).

## Governance & Non-Negotiables

We accept partnership on the following terms only:

1. **All output remains CC BY-SA 4.0.** No exclusive licensing to any partner, including Microsoft.
2. **No tokens, no NFTs, no fundraising rounds, no equity structures.** Sarasvatī has none and will create none.
3. **No sponsor may require exclusivity, private data, or non-open licensing.**
4. **Named-reviewer authority is inviolable.** No frontier-model output is elevated to "authoritative" without a named human reviewer of record, and no partner-model brand may be marketed as authoritative through us.
5. **Microsoft branding is welcomed** on any artifact where the partnership contributed materially, per Microsoft's standard "AI for Good" branding conventions.

## Next Steps

If this concept note aligns with the AI for Cultural Heritage team's current priorities, we would welcome a 30-minute call with Dr. Pan to discuss scope, cadence, and any adjustments needed to fit an active-cycle partnership. Materials, prior work, and audit trail are all live at the repository URL above.

*Thank you for reading. On behalf of Sarasvatī —*

**Dr. Lurong Pan (潘麓蓉)**
Sarasvatī Project
[Pan to fill: signature block]

---
*"All conditioned things are impermanent. Strive on with diligence."* — *Mahāparinibbāna Sutta* (DN 16), the Buddha's last recorded teaching.
