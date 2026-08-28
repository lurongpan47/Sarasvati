# Call for global support · 全球支援呼吁

> **Sarasvatī is one project running on one Mac mini. It has two cores: (1) an eight-branch open archive of the world's Buddhist canon, and (2) a Buddhist AI Charter that plants bodhicitta into algorithmic constraints. Both need help. This is a public request.**

> **Sarasvatī 只做两件事：八系佛典的全球开放归档 + 菩提心 AI 算法植入。两件都需要外部协作。这是一份公开呼吁。**

---

## Three concrete asks

### A. Launch the remaining 7 branches · 启动尚未开工的七系

Sarasvatī's canon archive is structured along eight transmission branches. Only one — **Tibetan** — has a first sample in the repo today (the DN 16 four-language reading), and **Pāli** has been touched through that same DN 16 asset. The remaining branches need **first samples** to prove the cross-branch method:

| Branch | 中文 | Status | What we need |
|---|---|---|---|
| India · `india` | 印度源流 | not started | philologists in Vedic / Prakrit / early Buddhist India studies; pointer to public-domain critical editions |
| Sanskrit manuscript · `sanskrit` | 梵文写本系 | not started | Sanskritists able to work from GRETIL / Nepal / Gilgit public-domain corpora; cross-language reviewers |
| Pāli · `pali` | 巴利·斯里兰卡 | seed only (DN 16) | Pāli scholars for a full first-sample sutta with named human review |
| Southeast Asian Theravāda · `seasia` | 南传东南亚 | not started | Burmese / Thai / Khmer / Lao / Shan-script readers; 5th/6th/8th/9th council edition access |
| Silk Road · `silkroad` | 中亚·丝路 | not started | Gāndhārī / Khotanese / Tocharian / Tangut specialists; access to Schøyen / IDP / BnF holdings |
| Chinese canon · `chinese` | 汉传系 | not started | classical Chinese Buddhologists; CBETA-savvy editors; Taishō vol. 85 gap-hunters |
| Sinosphere · `sinosphere` | 汉字文化圈 | not started | Korean / Japanese / Vietnamese Buddhologists; Tripiṭaka Koreana + SAT + Nara collaborators |

For each branch we want the same recipe: a public-domain source text → an AI machine draft into a language currently lacking a translation → a named human reviewer → CC BY-SA 4.0 release.

**Ways to help**:
- **Nominate a text.** Open an issue proposing a specific public-domain text + a specific target language + why it fills a real gap.
- **Volunteer as a reviewer.** We will keep your name on `CONTRIBUTORS.md` and cite you on every artifact you touch.
- **Donate compute.** Anthropic / OpenAI / Google API credits, or self-hosted open-weight backends (Llama 3.3, Qwen 2.5, DeepSeek), let us run more branches in parallel.
- **Nominate a source archive.** GRETIL, SuttaCentral, VRI, CBETA, IDP — anything with clean machine-readable text and a compatible license is a starting point.

### B. Human review of the Buddhist AI Charter · 菩提心宪章的母语审校

The **Buddhist AI Charter** (`charter/BUDDHIST-AI-CHARTER.md`) exists in **24 languages** under `charter/i18n/`:

ar · bo · de · es · fa · fr · hi · id · it · ja · km · ko · mn · my · pi · pt · ru · sa · si · th · tr · vi · zh-CN · zh-TW.

Every non-English version is currently an **AI machine draft**. Before the charter can carry real weight in local traditions and legal / policy conversations, each language needs a **native-speaker Buddhist / Buddhist-studies scholar** to read it end-to-end and either sign it off or open a pull request with corrections.

We are specifically looking for:
- **Pāli / Sanskrit specialists** — for the technical terms (*ahiṃsā · satya · asteya · brahmacarya · sati · sampajañña · mettā · karuṇā · anicca · anattā · upekkhā*).
- **Tibetan-language Buddhist scholars** — for `charter/i18n/CHARTER.bo.md`.
- **Sinhala, Burmese, Thai, Khmer Theravāda monastics or scholars** — for the four Southeast Asian language versions.
- **East Asian Buddhist scholars** — for zh-CN / zh-TW / ja / ko / vi.
- **Persian / Arabic / Turkish readers** — for the three West / Central Asian versions, which are the highest-risk for terminology drift.

**Ways to help**:
- Open a PR against `charter/i18n/CHARTER.<lang>.md`.
- Open an issue titled `[CHARTER REVIEW <lang>]` if you would rather flag a concern than write a full patch.
- Add yourself to `CONTRIBUTORS.md` as a signatory — no need to attest to the whole charter, only to what you personally reviewed.

### C. Charter runtime reference implementation · 宪章算法层参考实现

The charter is currently a **document**. The next step is to make it **executable**: any AI system, agent runtime, or MCP server should be able to `import` a small library and get the ten principles + five refusals wired in as **guardrails**.

We want two parallel reference implementations under permissive licenses:

1. **Python** — `buddhist_ai_guardrail/` — status: **starter kit in progress** (in a parallel worktree; will be published soon). PRs against it welcome once the skeleton lands.
2. **TypeScript / JavaScript** — `@buddhist-ai/guardrail` (npm) — status: **not started**.

Both should:
- Expose the five refusals as pre-flight checks (`should_refuse(context) → (bool, reason)`).
- Emit structured attestation logs that a downstream auditor can verify.
- Be small (< 500 LOC core), auditable, dependency-light.
- Ship with a test suite that covers the five refusal cases.
- Be adoptable as a first-class dependency in Anthropic MCP servers, OpenAI Assistants, LangChain, LlamaIndex, and any agent runtime that lets you register a `before_tool_call` hook.

**Ways to help**:
- **Python**: watch for the `buddhist_ai_guardrail` announcement, then PR against it.
- **TypeScript**: if you want to lead the TS port, open a `[CHARTER RUNTIME · TS]` issue and we will hand off the design doc.
- **Test cases**: propose real-world adversarial prompts that the charter's refusals should catch, as GitHub issues.
- **Integration**: if you maintain an agent framework, propose a hook where `buddhist_ai_guardrail` could plug in cleanly.

---

## Also welcome (general infrastructure)

- **Storage sponsors**: Arweave / Filecoin / web3.storage / Storj sponsors for permanent copies of the canon archive (~$5–20 per volume).
- **Mirror runners**: anyone with an IPFS node willing to pin our CID; anyone running static mirrors (VPS, university server, monastery archive).
- **Signal-boost**: Redditors, X / Nostr / Warpcast users, podcasters, journalists — see `announcements/`.
- **Cultural custodians**: libraries, monasteries, universities willing to formally accept Sarasvatī artifacts into their collections.

---

## What we don't want

- No tokens, no NFTs, no fundraising rounds, no equity structures.
- No sponsors that require exclusivity, private data, or non-open licensing.
- No "AI arms race" positioning. This is a preservation-and-ethics project, not a competitive-model project.

Everything remains **CC BY-SA 4.0**. Every contributor is credited but claims no ownership.

---

## How to contact

- **GitHub Issues**: https://github.com/lurongpan47/Sarasvati/issues
- **Discussion**: https://github.com/lurongpan47/Sarasvati/discussions
- **Direct** (for compute / API credit offers requiring private handshake):
  Open a GitHub issue titled `[SPONSOR CONTACT]` and we will follow up out-of-band.

---

## Why this is worth helping

Classical texts survive because *communities* keep them alive. The Buddha's word survives because Ānanda memorized it, then the First Council recited it, then Mahinda carried it to Laṅkā, then Buddhaghosa wrote commentaries, then eight generations of monks copied it onto palm leaves. Every one of those was a redundant backup. Every one was a *community act*.

Sarasvatī is trying to do that act for the AI era. The canon archive is the memory layer; the charter is the ethics layer. Both together are what it means to build AI in a way the tradition would recognize as sane.

One Mac mini cannot do this alone. It is asking the network for redundancy — just like Ānanda did.

If you can help with even one line item above, please do. If this is not for you, that is also fine — just don't gate-keep it, and please don't stop others.

*"Vayadhammā saṅkhārā, appamādena sampādetha."*
*诸行无常，当自精勤。*
*All conditioned things are impermanent. Strive on with diligence.*

**— Sarasvatī Project, 2026-08-28**
