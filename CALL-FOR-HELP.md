# Call for global support · 全球支援呼吁

> **Sarasvatī is one project running on one Mac mini. It has two cores: (1) an eight-branch open archive of the world's Buddhist canon, and (2) a Buddhist AI Charter that plants bodhicitta into algorithmic constraints. Both need help. This is a public request.**

> **Sarasvatī 只做两件事：八系佛典的全球开放归档 + 菩提心 AI 算法植入。两件都需要外部协作。这是一份公开呼吁。**

---

## Three concrete asks

### A. Launch the remaining 7 branches · 启动尚未开工的七系

Sarasvatī's canon archive is structured along eight transmission branches. As of v0.9 (2026-09), **all eight branches have a first sample** in the repo — but every non-source-language column in every sample is still a machine draft. The archive is now at a phase where the bottleneck is **named human review**, not first-sample creation.

| Branch | 中文 | v0.9 status | What we need |
|---|---|---|---|
| India · `india` | 印度源流 | 3 samples (Aśoka Major Rock Edicts XII, XIII, and the Calcutta-Bairāṭ / Bhābrū edict) | philologists in Prakrit / early Buddhist India studies; review of Chinese + Tibetan draft columns |
| Sanskrit manuscript · `sanskrit` | 梵文写本系 | 2 samples (Prajñāpāramitā Hṛdaya short recension; Vajracchedikā §§ 1–2) | Sanskritists to review the English draft column; more GRETIL / Nepal / Gilgit texts |
| Pāli · `pali` | 巴利·斯里兰卡 | DN 16 seed + 31 Dhammapada scan-first samples (Yamakavagga → Pāpavagga 116–119 opening ch. 9; Fausbøll 1900 / Müller SBE X 1881 / T210 法句經 fully attested) + Therīgāthā ekakanipāta 1–5 | Pāli scholars to review the extensive Dhammapada run — open readings and apparatus settlements listed per file; a native Sinhala or Burmese reader for pronunciation drafts |
| Southeast Asian Theravāda · `seasia` | 南传东南亚 | 2 samples (Karaṇīya Mettā Sutta Sn 1.8; Lokanīti ch. 1 *paṇḍitakaṇḍa*) | Burmese / Thai / Khmer / Lao / Shan-script readers to review the Burmese and Thai draft columns |
| Silk Road · `silkroad` | 中亚·丝路 | 2 samples (Kharoṣṭhī Dharmapada attested + pedagogical reconstruction) | Gāndhārī / Khotanese / Tocharian / Tangut specialists; more Schøyen / IDP / BnF material |
| Chinese canon · `chinese` | 汉传系 | 2 samples (Fó yíjiào jīng T389 selected passages; Sìshíèrzhāng jīng T784 opening) | classical Chinese Buddhologists to review the English + Tibetan + modern-Chinese draft columns |
| Sinosphere · `sinosphere` | 汉字文化圈 | 2 samples (Wŏnhyo *Daeseung Gisillon So* prologue T44 no. 1844; Wŏnhyo *Balsim suhaeng jang* 發心修行章 opening HPC vol. 1 p. 841a) | Korean Buddhologists to review the Hanmun / Korean / English draft columns; a Silla-era Yogācāra terminology specialist; a Tibetan reader for the canonical equivalent of 四蛇 (four elements as snakes) in bKa' 'gyur |
| Tibetan · `tibetan` | 藏传系 | 1 dedicated sample (Udānavarga Anityavarga, Rockhill 1892 I.3/10/12/17; English attested, Tibetan column draft) + DN 16 draft + **a 449-page Jonang Great Treasury catalogue in Chinese draft** (`translations/jonang-catalog/`, 2026-10-17) | Tibetanist with Beckh 1911 or a Kangyur witness to collate the ⟨བརྟག⟩ Tibetan stanzas; then update Rockhill's 1892 English to modern accuracy. **Jonang specialist** (Dolpopa / Tāranātha gsung 'bum) with the printed 觉囊文丛 vol. 216 to review the catalogue's name renderings and genre terms |

For each branch we want the same recipe: a public-domain source text → an AI machine draft into a language currently lacking a translation → a named human reviewer → CC BY-SA 4.0 release. **The 2026-Q4 priority is reviewers, not more first samples.**

**Ways to help**:
- **Nominate a text.** Open an issue proposing a specific public-domain text + a specific target language + why it fills a real gap.
- **Volunteer as a reviewer.** We will keep your name on `CONTRIBUTORS.md` and cite you on every artifact you touch.
- **Donate compute.** Anthropic / OpenAI / Google API credits, or self-hosted open-weight backends (Llama 3.3, Qwen 2.5, DeepSeek), let us run more branches in parallel.
- **Nominate a source archive.** GRETIL, SuttaCentral, VRI, CBETA, IDP, BDRC/BUDA (IIIF scans, added 2026-09-22) — anything with clean machine-readable text or open page images and a compatible license is a starting point.

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

1. **Python** — `impl/python/` (package name `buddhist-ai-guardrail`) — status: **v0.1.1 shipped locally** (source tree, tests, red-team harness, examples). **Not yet published to PyPI** (release pending maintainer credentials). PRs against the in-repo source welcome now; `pip install -e impl/python` works today.
2. **TypeScript / JavaScript** — `impl/typescript/` (npm package name `@sarasvati/buddhist-ai-guardrail`) — status: **v0.1.0 shipped locally** with API parity to the Python reference (source, dual ESM/CJS build, vitest suite, examples). **Not yet published to npm** (release pending maintainer credentials). PRs against the in-repo source welcome now.

Both should:
- Expose the five refusals as pre-flight checks (`should_refuse(context) → (bool, reason)`).
- Emit structured attestation logs that a downstream auditor can verify.
- Be small (< 500 LOC core), auditable, dependency-light.
- Ship with a test suite that covers the five refusal cases.
- Be adoptable as a first-class dependency in Anthropic MCP servers, OpenAI Assistants, LangChain, LlamaIndex, and any agent runtime that lets you register a `before_tool_call` hook.

**Ways to help**:
- **Python**: clone the repo and `pip install -e impl/python`, then PR against `impl/python/`.
- **TypeScript**: `npm install` under `impl/typescript/`, then PR against `impl/typescript/src/`.
- **Test cases**: propose real-world adversarial prompts that the charter's refusals should catch, as GitHub issues; or drop them into `impl/python/redteam/attacks/` with a PR.
- **Integration**: if you maintain an agent framework (LangChain, LlamaIndex, MCP server, OpenAI Assistants, Anthropic skills), propose a hook where `buddhist_ai_guardrail` could plug in cleanly and open a `[CHARTER RUNTIME · INTEGRATION <framework>]` issue.
- **Publish**: if you can help with a maintainer-credentialed PyPI / npm first release so `pip install buddhist-ai-guardrail` and `npm install @sarasvati/buddhist-ai-guardrail` work from the public registries, open a `[CHARTER RUNTIME · RELEASE]` issue.

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
