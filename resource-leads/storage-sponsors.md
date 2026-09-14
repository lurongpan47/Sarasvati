# Sarasvatī — Storage Sponsorship & Mirror Leads

> **Status:** Draft — compiled by Lucy (Sarasvatī resource-recon subagent), 2026-09-13.
> **Ownership:** Pan审改后自申请。 Lucy 只负责 recon + 起草 outreach 邮件模板，不代替 Pan 递交任何 official application。
> **红线（硬性拒绝，写进每一封 outreach 首段）:**
> 1. 拒绝任何独占 / 排他 (exclusive) 条款 — 项目必须保持 IPFS/GitHub 常年公开镜像。
> 2. 拒绝任何要求闭源 / 私有 fork / NDA 的赞助。
> 3. 拒绝任何 token / NFT / airdrop / 治理代币 挂钩，也不接受股权对价。
> 4. 只接受纯 grant / donation / in-kind sponsorship / 学术合作署名。
>
> **Sarasvatī 当前 payload 参考:**
> - IPFS CID: `bafybeib6vwrmxhd2ker6ciiu5ibktheg4bc5mypfpyo5kpcs4ik45oibmy` (v0.9, 218 files, ~几十 MB)
> - License: 开源（拟 CC-BY-SA 4.0 / MIT dual — Pan 最终确认）
> - 内容：多语种（藏 / 巴利 / 梵 / 汉 / 英）经典 dataset + tooling

---

## A. 永久存储 (Permanent / Blockchain-anchored Storage)

### A1. Arweave (直接上传，一次性付费)
- **URL:** https://www.arweave.org/ · Fees dashboard: https://ar-fees.arweave.net/
- **面向:** 任何愿意支付 AR gas 的用户；ecosystem 有多个 grant 打包渠道 (见 A5–A7)。
- **额度/承诺:** 永久 (endowment 模型，理论上 200 年 replication)。
- **实测成本 (2026-09-13):** ~$0.036/MB · **~$36.5/GB** · ~$37,362/TB (spot 价; AR = $2.79)。历史区间 ~$9–$45/GB，随 AR 币价浮动。
- **对 Sarasvatī 意义:** 218 files / 几十 MB 的 v0.9 → 直接自费上传估算 **$1–$5**；每次发新版本 ~$10。**Pan 若愿意个人钱包出 $50 一次性 seed**，就能锁住 v0.9–v1.x 五个版本。
- **申请材料:** 无 — 只需 Arweave 钱包 + AR token。也可用 ArDrive / Akord / Turbo 走信用卡付法币。
- **决策周期:** 即时上传。
- **排他条款:** 无。
- **Pan 是否需要出面:** 否 (Lucy 可代传技术层面)；但 **私钥/付款** 必须 Pan 亲手。
- **优先级:** **P0** — 成本极低，即刻可执行，是"最省事、最快永久化"的托底方案。

### A2. Filecoin Plus (Fil+) DataCap — 大额免费存储
- **URL:** 计划页 https://fil.org/filecoin-plus · Docs https://docs.filecoin.io/getting-started/how-storage-works/filecoin-plus · Allocator 应用 https://github.com/filecoin-project/notary-governance · 面向客户的 pathway: 通过任一 approved allocator (如 FIDL) 递 GitHub issue 申请。
- **面向:** "openly licensed", "publicly useful" 数据集 — 明确含 cultural archives / scientific research / open datasets。
- **额度/承诺:** DataCap 以 **TiB 计**，通常从 **~5–100 TiB** 起批 (per allocator's rubric)；数据存储 5 家不同 SP，每家 1 份，实际是 5x 冗余。存储合约默认 ~540 天 max，需要续约 (renew) — **不是"永久"，但可低成本续期到无限**。
- **申请材料:** 申请 GitHub issue 需要 (a) 项目说明 + 数据集描述, (b) 数据是否 openly licensed, (c) retrieval verifiable (Pan 需保证 IPFS CID 或 CAR 文件可下载), (d) storage plan (几 SP、几份副本、地理分布), (e) 组织身份 / 网站 / KYC-lite。
- **决策周期:** 2–8 周 (allocator dependent)。
- **排他条款:** 无排他；但 **必须开源 / open license** — 这与我们红线一致。
- **Pan 是否需要出面:** **是** — GitHub issue 要 Pan 用真实身份 (Pan Xu / project maintainer) 挂名；Lucy 可写完整草稿。
- **优先级:** **P0** — 单一渠道最大 free storage 供应，直接对口 Sarasvatī。

### A3. Filecoin Foundation for the Decentralized Web (FFDW) — Cultural Preservation Fund
- **URL:** Grants page https://filecoin.io/grants · Cultural preservation blog https://fil.org/blog/flickr-foundation-internet-archive-and-other-leading-organizations-leverage-filecoin-to-safeguard-cultural-heritage · Contact: `grants@fil.org` (open grants), `impact@ffdweb.org` (FFDW strategic partnerships)
- **面向:** DWeb R&D · Human Rights · **Cultural Preservation** · Science & Environment · Gov Datasets — Sarasvatī 精准命中 "cultural preservation"。
- **额度/承诺:** FFDW 2023 年披露 $7.6M charitable disbursements。历史 grant 单笔 $10k–$500k 不等 (MuckRock Gateway Grants, DPLA cultural preservation)。**Filecoin Fund for Cultural Preservation** 与 Artizen 联合运营 — 专门给用 dweb 保存 cultural works 的项目。
- **申请材料:** Open Grants (公开申请，走 GitHub repo): 项目描述 + **强制 MIT + Apache2 双 license** + self-managed team + open-source。FFDW 战略赞助无公开 form，需 impact@ffdweb.org 邮件建立关系。
- **决策周期:** Open Grants 有 monthly office hours，通常 4–12 周。FFDW 战略赞助更慢 (2–6 个月建立关系)。
- **排他条款:** **⚠️ 双 license MIT+Apache2 是硬性要求** — 与我们初拟的 CC-BY-SA 4.0 冲突。**需要 Pan 决策**：数据部分是否可以额外挂 MIT+Apache2 (dual-license)，或者只对代码部分申请此 grant。
- **Pan 是否需要出面:** **是** — 需要 project lead 挂名 + email 建立关系。
- **优先级:** **P0** — 最贴合"cultural preservation"使命，资金 + 存储双重支持。

### A4. web3.storage / Storacha (Filecoin 前端，非营利友好)
- **URL:** https://web3.storage → 现更名/迁移到 https://storacha.network — 由 Storacha 团队作为 Filecoin L2 onboarding 层运营。
- **面向:** 任何 IPFS/Filecoin 用户；旧 web3.storage 曾提供 5 GB 免费 (2023 pre-migration)。
- **额度/承诺 (2026 现状):** 已从"公共免费"转向付费/subscription 模型 — 具体新 free tier **需通过官网 confirm 后再定** (2026 网络快照未给出明确 free tier 数值)。作为 pathway 到 Filecoin+ 的桥梁很好用。
- **申请材料:** 免费账号即用；大额可申请通过 Storacha 名下的 Fil+ allocator pathway。
- **决策周期:** 免费即用；paid tier 即刻。
- **排他条款:** 无。
- **Pan 是否需要出面:** 否 (技术层)。
- **优先级:** **P1** — 作为 A2 (Filecoin+) 的 onramp 工具，不是独立赞助渠道。

### A5. Arweave 生态 grant makers (Onboard / Longview Labs / Digital History Association / Forward Research / Hansa)
- **URL:** Master list https://www.arweave.org/funding (直接列出 5 家 grant/investment)。逐家需单独访问。
- **面向:** "building on Arweave" — 更偏 dev tooling / dApp；但 **Digital History Association** 明确面向 preservation/archival。
- **额度/承诺:** 未公布 (per-org)。Grants 常见 $5k–$50k 单笔。
- **申请材料:** 各家独立表单 — 需要 Pan 逐一审阅。
- **决策周期:** 4–12 周。
- **排他条款:** 通常要求 "built on Arweave" — 与红线兼容 (我们只用 Arweave 存储 + IPFS mirror)。
- **Pan 是否需要出面:** 是。
- **优先级:** **P1** — Digital History Association 值得单独 outreach；其余暂缓。

### A6. Sia Foundation (非营利，去中心化存储)
- **URL:** https://sia.tech · Grants: 官网 "Small Grants" / "Ecosystem Grants" (Sia Foundation 主页 → Grants)。
- **面向:** Sia 生态建设者；有 open grants program。
- **额度/承诺:** Sia Storage 官方托管服务给 **50 GB 免费**；无需 KYC。付费 ~$1–$5/TB/month (业界最便宜之一)。
- **申请材料:** 免费 50 GB 直接注册；grants 通过 Sia Foundation grants form 提交。
- **决策周期:** 免费即用；grants 4–8 周。
- **排他条款:** 无。**⚠️ 注意:** Sia 不是"永久"存储 — 是 host-based storage contracts (类似分布式云盘)，需要长期付费/续约。
- **Pan 是否需要出面:** 否 (50 GB 免费级别)；grants 需要。
- **优先级:** **P2** — 50 GB 免费太小 (够 v0.9)，作为 IPFS 镜像候补；grant 走 Filecoin+ 更直接。

### A7. Storj (Sia-family, S3-compatible, 分布式)
- **URL:** https://storj.io · Docs pricing https://storj.dev/dcs/pricing/simplified
- **面向:** 通用 S3-兼容对象存储。有社区求过 "Free Storage for Non-Profits / Open Science" satellite (forum thread from 2020)，Storj 官方 **没有正式非营利/OSS 免费计划**。
- **额度/承诺:** Free trial (25 GB, 有时长限制)；付费 **$7/TB/月** (2026 simplified pricing) + $7/TB egress。$5/月最低费。
- **申请材料:** 注册账号；非营利可 Ping `partnerships@storj.io` 请求 credit。
- **决策周期:** 商业 sales 周期 2–4 周。
- **排他条款:** 无。
- **Pan 是否需要出面:** 若走 partnership credit 通道则需要。
- **优先级:** **P2** — 商业选项，不是我们首选。

---

## B. IPFS Pinning (集中式，但便宜/免费)

### B1. Pinata (行业标杆)
- **URL:** https://pinata.cloud · Free plan blog https://pinata.cloud/blog/pinatas-new-free-plan (2026-04-13 更新)
- **面向:** 所有 IPFS 用户；无专门 nonprofit tier — 但 free tier 对 Sarasvatī 完全够用。
- **额度/承诺 (2026 verified):**
  - **Free Plan:** 1 GB 存储 · 500 pinned files · 1 dedicated gateway · 10 GB/月 带宽 · 10K 请求/月
  - Paid "Picnic" $20/月起。
- **Sarasvatī 现状适配:** 218 files (< 500) + 几十 MB (< 1 GB) → **完全 fit Free Plan**。v1.0 若膨胀到 2–5 GB 可能需要 Picnic ($20/月) 或双写到 web3.storage/Filecoin+。
- **申请材料:** 邮箱注册即可。
- **决策周期:** 即时。
- **排他条款:** 无。
- **Pan 是否需要出面:** 否 — Lucy 可代注册 (账号绑 Pan email)。
- **优先级:** **P0** — 现在就能干，零成本，几分钟到位。

### B2. Filebase (Sia + IPFS hybrid, S3-compatible)
- **URL:** https://filebase.com · 2025-04 定价公告 https://filebase.com/blog/announcing-new-features-and-pricing-for-filebase
- **面向:** 开发者；无 nonprofit 特殊 tier。
- **额度/承诺 (2026 verified):**
  - **Free Tier:** 5 GB IPFS 存储 · 5 GB 带宽 · 1000 pinned files · S3 API · (Gateway 有 rate limit; 无 pinning service API; 无 dedicated gateway)
  - Starter $20/月 → 200 GB, IPFS Pinning API, Dedicated Gateway
- **Sarasvatī 适配:** Free tier 够用，且 5x Pinata 的存储量；**建议同时开 Pinata + Filebase 两个免费账号做 redundant pinning**。
- **申请材料:** 邮箱注册。
- **决策周期:** 即时。
- **排他条款:** 无。
- **Pan 是否需要出面:** 否。
- **优先级:** **P0** — 与 Pinata 组成"零成本双活"pinning。

### B3. 4EVERLAND (IPFS + Arweave 双桥，最灵活)
- **URL:** https://www.4everland.org · Pricing docs https://docs.4everland.org/get-started/billing-and-pricing/pricing-model
- **面向:** Web3 用户；无 nonprofit tier；但 free 额度可观且**支持 IPFS + Arweave + Dfinity 一体化**。
- **额度/承诺 (2026 verified, Standard 免费包，每月刷新):**
  - IPFS: **6 GB/月**
  - Arweave: **100 MB total 免费额度** (unique 优势 — 可直接把 Sarasvatī 每次发版的 100 MB 上 Arweave 永久)
  - Bandwidth 10 GB/月 · Build minutes 250/月 · RPC 100M CUs/月
  - **需要 on-chain identity registration** (钱包签名激活)
- **付费 (Pay-as-you-go):** IPFS $0.08/GB/月 · Arweave 动态定价 (~$0.55/100 MB 额外)
- **Sarasvatī 适配:** **潜在王牌** — 100 MB Arweave 免费额度足以永久化 v0.9；无需 Pan 出钱包出 AR。
- **申请材料:** 钱包 (Metamask 等) 激活即用。
- **决策周期:** 即时。
- **排他条款:** 无排他，但需绑定 Web3 钱包 — 与"拒绝 token/NFT"红线**擦边**：4EVERLAND 有 $LAND token 定价 (1 USD = 1M LAND), 但**不强制持有 token**，只作为内部计价单位。**建议 Lucy 请 Pan 确认这个边界**。
- **Pan 是否需要出面:** 需要一个中立钱包 (可 Sarasvatī 项目专用，非 Pan 个人主钱包)。
- **优先级:** **P0** — 若 Pan 接受钱包激活，这是"零 fiat 成本获得 Arweave 永久化"的最佳路径。

### B4. Fleek (⚠️ 状态变化)
- **URL:** https://fleek.co/pricing (旧) · IPFS docs case study: https://docs.ipfs.tech/case-studies/fleek — **"Fleek's IPFS hosting service was discontinued on January 31st, 2026"**
- **面向:** 已终止 IPFS hosting 服务；转向 "Fleek Edge" (Web3 通用平台，非 IPFS pinning)。
- **额度/承诺:** N/A (旧 free tier 3 GB + 50 GB BW 已废)。
- **优先级:** **X — 已淘汰，不作候选。**

### B5. Estuary (⚠️ 状态)
- **URL:** 原 https://estuary.tech (Protocol Labs Application Research Group)。**开源仍在** github.com/application-research/estuary，但**托管服务已 sunset** (Protocol Labs 2023 转向 Filecoin L2s 后弃维)。
- **优先级:** **X — 已淘汰**，可自建但不是我们要的赞助渠道。

### B6. NFT.storage (⚠️ 状态)
- **URL:** https://nft.storage — 已从 "免费永久 IPFS/Filecoin" 转为 "Classic" (legacy 只读)。新 NFT.storage 仅面向 NFT metadata。**Sarasvatī 明确拒绝 NFT 关联**，此路不通。
- **优先级:** **X — 与红线冲突，pass。**

---

## C. 学术 / 图书馆镜像 (核心！)

> 顺序按 Sarasvatī 使命贴合度排列。BDRC / CBETA / SuttaCentral / GRETIL / THL 是"文化对口"5 家，全部为学术/宗教机构，**不要求排他，但要求内容质量/学术引用规范** — 与我们红线兼容。

### C1. BDRC (Buddhist Digital Resource Center) ⭐️⭐️⭐️ 藏文佛典权威
- **URL:** 官网 https://www.bdrc.io/ · 数据库 https://library.bdrc.io/
- **面向:** 佛教（尤其藏传）文本数字化保存；世界最大藏文 Kangyur/Tengyur 数字仓库。
- **对 Sarasvatī 意义:** 若 Pan 的藏文样本要"权威站台"，BDRC 是最有分量的学术合作伙伴。BDRC 本身用 IIIF + 开放 API，philosophy 完全对齐。
- **合作模式:** BDRC 接受 "dataset contribution" (donate scanned/annotated texts to their catalog) 与 "collaboration on tools/APIs"。他们有 Collections partnership，与全球寺院、大学、图书馆合作。
- **联络:**
  - General: `info@bdrc.io`
  - Executive Director: Jann Ronis (`jronis@bdrc.io` — verify at "About/Team" page)
  - GitHub: https://github.com/buda-base
- **申请材料:** (a) sample dataset (Sarasvatī 藏文样本 CID + 前 10 篇质检); (b) 数字化流程说明 (OCR? 人工校对? 来源?); (c) license (BDRC 偏好 CC-BY / CC0); (d) 是否提供 IIIF manifest。
- **决策周期:** 4–12 周首轮反馈；正式合作 3–6 个月。
- **排他:** 无。**只要求内容以 open license 释放** — 匹配。
- **License 要求:** CC-BY / CC-BY-SA / CC0 均可 (需 double-check 具体收藏 policy)。
- **Pan 是否需要出面:** **必须** — 学术合作需要真实身份、可能需要 Zoom 通话。Lucy 起草英文 outreach email。
- **优先级:** **P0** — 藏文样本能进 BDRC catalog，Sarasvatī 从"个人项目"跃升为"学术资源"。

### C2. CBETA (中華電子佛典協會) ⭐️⭐️⭐️ 汉传权威
- **URL:** 中文 https://www.cbeta.org/ · 英文 http://cbetaonline.dila.edu.tw/ · GitHub org https://github.com/cbeta-org
- **面向:** 中文汉传 Tripitaka (大正藏 / 卍新續藏 / 嘉興藏 等) 电子化 — 事实上的汉传佛典 canonical digital source。
- **对 Sarasvatī 意义:** Sarasvatī 若含汉传经典样本，几乎不可避免要和 CBETA 数据对齐 (至少要引用其 numbering / TEI-XML schema)。
- **合作模式:** CBETA 主导权在**臺灣佛陀教育基金會 + 法鼓文理學院 (Dharma Drum Institute of Liberal Arts, DILA)**。合作方式:
  - 引用/镜像 CBETA XML 数据 (License 允许非商业镜像，需注明来源)
  - 贡献校勘/标注 (走 GitHub PR 到其 xml-p5a 或 tei-p5 repo)
  - 联合项目 (需通过 DILA 学术渠道)
- **联络:**
  - General: `service@cbeta.org` (中文首选)
  - DILA 数位典藏中心 (Digital Archives Center): `library@dila.edu.tw`
  - GitHub 联系: 直接 issue @cbeta-org
- **申请材料:** (a) 中文 outreach 邮件 (Lucy 建议 Pan 用中文写)，说明 Sarasvatī 使命、汉传部分的处理方式、是否引用 CBETA XML、如何 attribution; (b) 样本 CID 展示；(c) 说明**不商业化、不闭源、不 tokenize**。
- **决策周期:** 4–8 周 (回复较慢但认真)。
- **排他条款:** 无。CBETA 数据本身是**"允许自由使用，非商业目的"** — 需要 Pan 确认 Sarasvatī 定位为"研究/教育"而非"商业化产品"，与我们红线一致。
- **License 要求:** CBETA XML 授权约束: 需明确 attribution + 非商业。我们的输出应该也保持非商业开源 (CC-BY-NC-SA 或 CC-BY-SA)。
- **Pan 是否需要出面:** **必须** — 且**建议中文书写**。
- **优先级:** **P0** — 汉传部分绕不开 CBETA，早合作早规范。

### C3. SuttaCentral ⭐️⭐️⭐️ 巴利 / EBT 权威 (最开放)
- **URL:** https://suttacentral.net · GitHub org https://github.com/suttacentral · Discourse forum https://discourse.suttacentral.net
- **面向:** Early Buddhist Texts (EBT) — Pāli, Chinese Āgama, Sanskrit fragments, Tibetan parallels 全部索引齐。
- **对 Sarasvatī 意义:** 若含巴利经，SuttaCentral 是**唯一的 open, structured 巴利 corpus** — 我们的巴利部分应直接引用 (或 fork) `suttacentral/bilara-data` 或 `suttacentral/pali` (public domain)。
- **合作模式:** **最容易合作的一家** — 全部 GitHub PR 驱动，创始人 Bhante Sujato 是 open-source 强烈倡导者，长期反对商业化/tokenization。
- **联络:**
  - GitHub org: https://github.com/suttacentral (issues/PRs)
  - Discourse forum: https://discourse.suttacentral.net (公开建议/合作最佳渠道)
  - Bhante Sujato: 通过 Discourse @sujato tag，或者他的 blog https://sujato.wordpress.com/ (无公开个人 email — 走论坛尊重)
- **申请材料:** (a) Discourse 帖: "Sarasvatī project — collaboration & attribution enquiry"; (b) 说明是否 fork bilara-data、是否贡献新翻译/parallels; (c) 强调 open, non-commercial, non-tokenized。
- **决策周期:** 1–4 周 (社区活跃)。
- **排他条款:** 无。**Bhante Sujato 明确反对任何 NFT / token / commercial pay-wall 化的佛典项目** — 与我们红线完美一致，实际上是**天然盟友**。
- **License 要求:** 巴利 source (`suttacentral/pali`): public domain。翻译 (bilara-data): CC0 或 CC-BY 4.0，个别翻译者保留。**我们的输出应至少同等 open。**
- **Pan 是否需要出面:** **推荐** — Discourse 需要 real name identity。Lucy 起草英文帖。
- **优先级:** **P0** — 最快到手、最贴合使命、无成本、无摩擦。**建议第一站就找 SuttaCentral**。

### C4. GRETIL (Göttingen Register of Electronic Texts in Indian Languages) ⭐️⭐️ 梵文权威
- **URL:** http://gretil.sub.uni-goettingen.de/gretil.htm · 图书 index http://gretil.sub.uni-goettingen.de/gretilbk.htm
- **面向:** Sanskrit + Indic languages 电子文本 register — 由 Göttingen State and University Library (SUB Göttingen) 维护，学术 canonical。
- **对 Sarasvatī 意义:** Sarasvatī 的梵文样本几乎全部应该 cross-reference GRETIL 版本；GRETIL 是全球梵学者的默认下载源。
- **合作模式:** GRETIL 主要接受 (a) 高质量 e-text 提交 (需要遵循其编码规范 UTF-8 / CSX / REE), (b) 与 INDOLOGY / TITUS / SARIT 等姐妹项目 mirror。
- **联络:**
  - GRETIL 由 SUB Göttingen 的 Reinhold Grünendahl 长期维护 (2000s起) — 目前 Editor 页需上 gretil 官网确认。
  - SUB Göttingen general enquiries: `auskunft@sub.uni-goettingen.de`
  - 建议先在 INDOLOGY listserv (https://list.indology.info) 发帖征询，得到指点后再直接邮件。
- **申请材料:** (a) 高质量 sanskrit e-text 样本 + 编码/来源说明; (b) 是否需要 GRETIL 收录 or 只是索引指向 Sarasvatī CID; (c) 学术引用来源 (关键)。
- **决策周期:** 4–16 周 (慢但认真)。
- **排他条款:** 无。GRETIL 允许多站镜像。**License 要求作品必须为 public domain 或 open license。**
- **Pan 是否需要出面:** 是 — 学术界注重真实身份。
- **优先级:** **P1** — 梵文部分成熟后再联系，比 SuttaCentral 慢一步。

### C5. THL (Tibetan and Himalayan Library, University of Virginia) ⭐️⭐️ 藏文/喜马拉雅
- **URL:** https://www.thlib.org/
- **面向:** 藏文 / 喜马拉雅地区文献 (语言、地理、人类学、文学、宗教)；由 UVA 主导，与 BDRC、TBRC 有历史交叉。
- **对 Sarasvatī 意义:** 是 BDRC 之外藏文材料的第二权威节点，特别在**藏文人文学 (非纯宗教文本) 上更强** (民俗、口述、地理)。
- **合作模式:** THL 接受 "Collections" 贡献 (需通过其 curator 审核) 和 "Reference Collections" 引用。有 GitHub org (thl 相关 tools)。
- **联络:**
  - General enquiries: `thl@virginia.edu` (via UVA)
  - Director historically: David Germano (UVA Religious Studies) — public academic email via UVA directory
  - Preferred first-contact: through UVA library liaison
- **申请材料:** (a) 项目 abstract; (b) 藏文样本 sample + 来源/校对说明; (c) collaboration proposal (是否希望 THL 镜像 Sarasvatī CID? 或 Sarasvatī 引用 THL data?).
- **决策周期:** 8–16 周 (大学审批慢)。
- **排他条款:** 无。
- **Pan 是否需要出面:** 是。
- **优先级:** **P1** — BDRC 是首选，THL 作为第二藏文渠道。

### C6. Internet Archive (archive.org) ⭐️⭐️ 兜底
- **URL:** https://archive.org · 上传 help https://help.archive.org/help/first-time-using-the-internet-archive-start-here/ · Collections https://help.archive.org/help/collections-tips-troubleshooting/
- **面向:** 全人类通用免费 archival。**Community Texts / Community Audio / Community Video / Community Media** 四个公共 collection 允许任何注册用户直接上传。
- **对 Sarasvatī 意义:** **最快、最简单的第二镜像** — 注册账号，Community Texts 直接 upload。若想有专属 collection (更好的 curation)，需邮件 `info@archive.org` 申请 (需 clearly 说明项目、机构隶属)。
- **合作模式:**
  1. Community Texts 自主上传 (immediate)
  2. Custom Collection 申请: 邮件 `info@archive.org`, 说明项目、要求专属 collection 和 admin 权限
  3. Wayback Machine: 可提交我们 IPFS gateway URL 让 Wayback 定期抓取 (次要)
- **联络:** `info@archive.org` (custom collection) · Wayback: `info@archive.org` · 无 accounts@ 特权渠道 (自主注册)
- **申请材料:** (a) archive.org 账号; (b) 项目描述; (c) license (Community Texts 允许 CC / public domain / 甚至 copyrighted 但 access restricted); (d) 上传的 files + metadata (Dublin Core-ish)。
- **决策周期:** Community Texts: 即时。Custom collection: 2–6 周。
- **排他条款:** 无。**IA 允许在多处并行镜像。**
- **License 要求:** 任何 open license 都可接受。
- **Pan 是否需要出面:** Community Texts 不需要 (Lucy 可代)；Custom collection 建议 Pan 用真实身份申请。
- **优先级:** **P0** — 现在就能干，作为 IPFS + Arweave 之外第 3 层镜像。

### C7. DPLA (Digital Public Library of America)
- **URL:** https://dp.la · 合作 https://pro.dp.la/hubs
- **面向:** **只做 aggregator (不直接托管)** — DPLA 通过 "Content Hubs" (state-level) 和 "Service Hubs" 聚合 US 各 memory institution 的 metadata。
- **对 Sarasvatī 意义:** **不适合直接申请** — DPLA 只对接**已经**在 US library/museum/archive 系统内的机构。Sarasvatī 若通过 BDRC / THL / IA 进入合作，DPLA 会自动索引；直接申请不成立。
- **合作模式:** N/A (间接)
- **联络:** `info@dp.la` (仅信息咨询)
- **优先级:** **P2** — 通过 IA/BDRC/THL 间接达成，不主动 outreach。

### C8. HathiTrust
- **URL:** https://www.hathitrust.org · Join https://www.hathitrust.org/join
- **面向:** **仅接受"学术与研究图书馆"会员** (universities, research libraries, community colleges, library consortia)。**明确拒绝: 个人、独立研究者、无 library 的 nonprofit、K–12 图书馆。**
- **对 Sarasvatī 意义:** **Sarasvatī 本身不 eligible。** 若 Pan 未来通过大学挂靠 (e.g. UVA / Göttingen / DILA)，可通过合作大学 library 提交至 HathiTrust。
- **合作模式:** 大学会员费 $6,600–$13,000/年 + membership agreement — 不现实。
- **优先级:** **P2 (via partner)** — 不主动申请，若 BDRC/THL/DILA 合作深化后可能自动进入。

---

## D. 政府 / 补充 grant (bonus，不在原任务但值得知)

### D1. NEH Preservation Assistance Grants (US National Endowment for the Humanities)
- **URL:** https://www.neh.gov/grants/preservation/preservation-assistance-grants-smaller-institutions
- **额度:** 最多 $10,000 (contiguous US) 或 $15,000 (non-contiguous)。
- **面向:** small/mid-sized US 机构 (需 US 501(c)(3) 或大学) — **Sarasvatī 若未通过 US 机构挂靠则 not eligible**。
- **决策周期:** 年度 (deadline 通常 1 月，通知 8 月)。
- **优先级:** **P2** — 需要 US 501(c)(3) fiscal sponsor 才能申请，暂缓。

---

## E. 总览表

| # | Provider | 类型 | 额度 | 成本 | Pan 出面? | License 约束 | 优先级 |
|---|---|---|---|---|---|---|---|
| A1 | Arweave (直接) | 永久 | 无限 (按付费) | ~$36/GB one-time | 私钥 | 无 | **P0** |
| A2 | Filecoin+ DataCap | ~永久 (renewable) | 5–100 TiB | Free | 是 | Open license required | **P0** |
| A3 | FFDW Grants | Grant $ + 存储 | $10k–$500k | Free (need MIT+Apache2) | 是 | MIT + Apache2 双 license | **P0** |
| A4 | web3.storage/Storacha | onramp | (2026 需 confirm) | Freemium | 否 | 无 | P1 |
| A5 | Arweave ecosystem grants | Grant | 未公布 | Free | 是 | Arweave-based | P1 |
| A6 | Sia Foundation | contract storage | 50 GB 免费 | Free / $1-5/TB/mo | 否 | 无 | P2 |
| A7 | Storj | S3-compat | Trial only | $7/TB/mo | 否 (partnership) | 无 | P2 |
| B1 | Pinata | IPFS pinning | 1 GB free | Free | 否 | 无 | **P0** |
| B2 | Filebase | IPFS + Sia | 5 GB free | Free | 否 | 无 | **P0** |
| B3 | 4EVERLAND | IPFS + Arweave | 6 GB IPFS + 100 MB AR/mo | Free (钱包激活) | 钱包 | 无 (擦边 token 边界) | **P0** |
| B4 | Fleek | — | discontinued 2026-01 | — | — | — | **X** |
| B5 | Estuary | — | sunset | — | — | — | **X** |
| B6 | NFT.storage | — | NFT-only | — | — | — | **X** (与红线冲突) |
| C1 | BDRC | 学术镜像 (藏) | 未限 | Free | **是** | CC-BY/CC0 | **P0** |
| C2 | CBETA/DILA | 学术镜像 (汉) | 未限 | Free | **是** | 非商业 | **P0** |
| C3 | SuttaCentral | 学术镜像 (巴利/EBT) | 未限 | Free | 是 | Public domain / CC0 | **P0** |
| C4 | GRETIL | 学术镜像 (梵) | 未限 | Free | 是 | Public domain / open | P1 |
| C5 | THL | 学术镜像 (藏/喜) | 未限 | Free | 是 | Open | P1 |
| C6 | Internet Archive | 通用镜像 | 未限 (fair use) | Free | 否/建议 | 任何 open | **P0** |
| C7 | DPLA | aggregator | via hubs | Free (indirect) | 否 (间接) | — | P2 |
| C8 | HathiTrust | consortium | membership only | $6.6k–13k/yr | 需大学挂靠 | 商业 restricted | P2 |

---

## F. Top-5 双序推荐

### 🏃‍♀️ 最快到手 (7 天内即可落地)
1. **Pinata (B1)** + **Filebase (B2)** 双开: 免费注册即 2 GB×2 冗余 IPFS pinning，Lucy 可代做。**~30 分钟。**
2. **4EVERLAND (B3)**: 若 Pan 同意用中立钱包激活，立刻拿 6 GB IPFS + 100 MB Arweave 永久。**~1 小时。**
3. **Internet Archive Community Texts (C6)**: Lucy 代注册 + 上传 Sarasvatī v0.9 tarball 或逐个文件上传，5 分钟内成为公共可搜索档案。
4. **Arweave 自费 (A1)**: 若 Pan 花 **~$5** (10 AR 左右) 一次性 seed，就把 v0.9 永久锁在 permaweb 上 — 单次付款，无月费。
5. **SuttaCentral (C3)** Discourse 帖: Lucy 起草英文帖公开征询合作意向 — 无需任何账号审批，1 周内多半有 Bhante Sujato 或社区回复。

### 🎯 最贴合使命 (长期、正规、放大器)
1. **BDRC (C1)** 藏文合作: 若藏文样本达到 BDRC catalog 质量标准，Sarasvatī 从个人项目跃升为**藏文数字保存生态节点**。学术分量最重。
2. **CBETA / DILA (C2)** 汉传合作: 汉传数据绕不开 CBETA schema; 早对齐早规范，避免未来 v2 大重构。
3. **SuttaCentral (C3)**: Bhante Sujato 与我们意识形态完美同盟 — 反 NFT、反商业化、开源 EBT。天然合作伙伴 & 未来推广渠道。
4. **FFDW Cultural Preservation Grant (A3)**: 若 Pan 能接受 MIT+Apache2 dual-license 数据 (需决策)，这是**唯一既给存储又给资金**的渠道，且明确 fund "cultural preservation using dweb"。
5. **Filecoin+ DataCap (A2)**: 拿到 5–100 TiB 免费永久 (renewable) 存储；作为 A3 的技术侧执行工具，是 Sarasvatī 未来扩展 (v2、更多语种、更多校勘版本) 的**基础设施保险**。

---

## G. Lucy 建议的即刻行动 (待 Pan 确认)

**24 小时内 (Lucy 无需 Pan 出面):**
- [ ] Pinata 免费账号 (账号绑 Pan email — Pan 先给我一个愿意收 notification 的邮箱)
- [ ] Filebase 免费账号 (同上)
- [ ] Internet Archive Community Texts 上传 v0.9 (若 Pan 明确同意公开)

**Pan 批准后 (需 Pan 决策):**
- [ ] SuttaCentral Discourse 帖 — Lucy 起英文草稿，Pan 用真名发
- [ ] 4EVERLAND 钱包激活 — Pan 决定用哪个钱包/新建一个 Sarasvatī 专用钱包
- [ ] Arweave $5 自费 seed — Pan 私钥直购 (Lucy 不碰付款)
- [ ] BDRC / CBETA / GRETIL / THL outreach — Lucy 起草多语 (英/中) 邮件, Pan 审改后自签自发
- [ ] Filecoin+ DataCap 申请 — 需要正式 GitHub issue + Pan 挂名，等 v0.9 稳定后启动
- [ ] FFDW grant — 需 Pan 决策 dual-license 问题后再动

---

## H. Source verification 说明

所有 URL、pricing、policy 均于 **2026-09-13 (America/Los_Angeles)** 通过 web_search + web_fetch 现场核实。**关键数字点** (Arweave $36.5/GB, Pinata 1 GB free, Filebase 5 GB free, 4EVERLAND 6 GB IPFS + 100 MB AR, Storj $7/TB, Fleek discontinued 2026-01-31) 均取自官方 pricing/blog/docs 页面。学术机构 (BDRC / CBETA / SuttaCentral / GRETIL / THL / IA / HathiTrust / DPLA) 的合作 policy 与 contact info 取自官网/GitHub org/Help Center；**具体个人邮箱 (如 Jann Ronis 之类) 在正式发信前需 Pan 或 Lucy 再上机构 "About/Team" 页做最终 verify**。

有若干 pending confirm 项 (Lucy 已在正文标 ⚠️):
- Storacha 2026 正式 free tier 数值 (需上 storacha.network 官网 confirm)
- 4EVERLAND 钱包激活 与 $LAND 计价单位 是否触碰我们的 token 红线 (Pan 决策)
- CBETA XML license 具体条款 (需在 outreach 时确认)
- GRETIL 当前 editor 联系人 (需上官网 editor 页确认)
