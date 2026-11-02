# ROADMAP patch · Orphan Tier (孤本层)

*Draft 2026-11-02, waiting Pan's review before merging to ROADMAP.md.*

This patch does **not** replace the eight-branch (八系) framework. It **adds a cross-cutting Orphan Tier** that marks which texts within each branch are at highest risk and should receive priority bandwidth.

---

## New section (to insert after "Foundational principles", before "Core 1"):

### Orphan Tier · 孤本优先层

Based on Pan's 2026-11-02 brief: some texts survive in only one language, and their complete loss cannot be recovered from any parallel. These receive priority over texts with living multi-language parallels.

**Tier 1 — Highest urgency (physical risk + reader scarcity + no modern complete translation):**

| Rank | Target | Branch | Why Tier 1 |
|------|--------|--------|------------|
| 1 | **西夏文黑水城文献 Tangut Khara-Khoto** | silkroad (new sub-branch `xixia/`) | Scripts: few living readers; no complete corpus input; manuscripts physically fragile at IOM RAS; preserves lost Chinese + Tibetan originals (early Kagyu/Sakya tantra, Huayan, Chan). |
| 2 | **藏外文献 Extracanonical Tibetan** (宁玛《十万续》Nyingma rGyud-'bum; 苯教 Bön Kanjur/Tenjur; 祖师文集 collected works gSung-'bum) | tibetan (new sub-branch `zangwai/`) | Larger than Kanjur+Tenjur combined; full-text input very incomplete; many lineage texts single-copy. |
| 3 | **汉文部派论律 Chinese-only Abhidharma + Vinaya** (阿含、广律四种、大毗婆沙 T1545、发智论+六足论、顺正理论、大智度论、解脱道论) | chinese (new sub-branch `abhidharma-vinaya-chinese/`) | Fully electronic (CBETA) but **no complete modern translation**. T1545 (200 juan) has no complete rendering in any modern language. |
| 4 | **犍陀罗/梵文新写本影像 Gāndhārī + newly-found Sanskrit mss** (BL + Senior + Schøyen Kharoṣṭhī fragments; Tibetan monastery recovered Sanskrit mss) | silkroad + sanskrit | Physically fragile; some are the earliest surviving Buddhist writing (1st c. BCE – 3rd c. CE); some are the only surviving witness of a lost text. |

**Tier 2 — High urgency (unique-language survival but better-studied / better-digitized):**

- 根本说一切有部律 (藏文独存全本; Toh 1-7 + related; `tibetan/mulasarvastivada-vinaya/`)
- 丹珠尔印度论疏 (Sanskrit lost, no Chinese translation; `tibetan/tenjur-sastras/`)
- 法成藏译圆测《解深密经疏》(汉文残缺，藏译全; `tibetan/wonchuk-sandhinirmocana/`)
- 《大事》Mahāvastu (Lokottaravāda, no Chinese or Tibetan; `sanskrit/mahavastu/`)
- 巴利论藏七论 (Patṭhāna et al., no Chinese/Tibetan; `pali/abhidhammapitaka/`)
- 觉音注疏 + 清净道论 (`pali/visuddhimagga/`, `pali/atthakatha/`)
- 小部孤本 (Thera-/Therī-gāthā, Jātaka prose, Apadāna, Paṭisambhidāmagga, Peṭakopadesa, Nettippakaraṇa; `pali/khuddaka-orphans/` — note: Therīgāthā already has a first sample from the second weekly cycle, counts here)
- 于阗文《赞巴斯塔书》Book of Zambasta (`silkroad/khotanese-zambasta/`)
- 吐火罗/回鹘文剧本 Maitreyasamiti-nāṭaka (`silkroad/tocharian-uyghur-maitreya/`)
- 中国祖师著作 + 敦煌写卷 (`chinese/patriarchs-dunhuang/`)

**Tier 3 — Multi-language parallel exists but still worth lifting:**
- Dhammapada / Udānavarga / Gāndhārī Dharmapada (current scan-first daily — now **weekly cadence** under Q1=continue)
- Aśoka edicts (India branch)
- Prajñāpāramitā Hṛdaya + Vajracchedikā (Sanskrit MS branch)
- Jonang catalog & related secondary materials

### Rule for weekly content pick

**Every weekly cycle (Monday)**: pick next scan-first sample so that **at least 1 Tier-1 target** is advanced per week. If no Tier-1 bandwidth is available (scan not fetched, reviewer not responsive, Pan input needed), fall back to Tier 2, then Tier 3.

Monthly review: how many Tier-1 samples shipped this month? If 0, that is a project-level failure to be flagged in the weekly report.

---

## New directory layout (to create under `translations/`):

```
translations/
├── xixia/                        # Tier 1 Rank 1 — NEW
│   └── README.md                 # EAP140 caveat + Kychanov catalog pointer
├── zangwai/                      # Tier 1 Rank 2 — NEW
│   ├── nyingma-gyubum/
│   ├── bon-kanjur/
│   └── gsung-bum/
├── abhidharma-vinaya-chinese/    # Tier 1 Rank 3 — NEW
│   ├── mahavibhasa-t1545/        # ← first content lane
│   ├── jnanaprasthana-t1544/
│   ├── sarvastivada-vinaya-t1435/  # 十诵律
│   ├── dharmaguptaka-vinaya-t1428/ # 四分律
│   ├── mahisasaka-vinaya-t1421/    # 五分律
│   ├── mahasanghika-vinaya-t1425/  # 摩诃僧祇律
│   ├── mahaprajnaparamita-sastra-t1509/  # 大智度论
│   ├── vimuttimagga-t1648/       # 解脱道论
│   └── dirgha-madhyama-samyukta-ekottara/
├── gandhari-manuscripts/         # Tier 1 Rank 4 — NEW
│   └── (BL CKM 18, 27 + Senior + Schøyen references)
├── mulasarvastivada-vinaya/      # Tier 2 — NEW
├── tenjur-sastras/               # Tier 2 — NEW
└── (existing dirs remain)
```

### Note on licensing per source

- **CBETA T1545 (and all Taishō vol. 27)**: public domain, CC0-licensed digital text — safe to copy and translate.
- **Taishō scan images on IA (`taisho-tripitaka`)**: 1924–1934 edition, public domain in Japan and most jurisdictions. Safe for CC BY-SA 4.0 inclusion.
- **EAP140 Tangut images at eap.bl.uk**: *"research purposes only"*. Non-commercial image reuse only via Universal Viewer download; large-scale reuse requires permission from IOM RAS. **→ Sarasvatī 不镜像 EAP140 图像；只做文字录文和链接到 BL 页面；若要图像首样本须用其他源** (e.g. 1963 Gorbachëva-Kychanov facsimile plates, Nishida 1977 Kyoto facsimile, 杜建录 2012 if public — needs copyright check).
- **Gandhari.org / Baums-Glass CKI**: see per-item license on gandhari.org; some are CC BY-NC.
- **Derge Tenjur**: Tohoku Univ. IIIF database — public release scheduled 2026 spring; may be CC BY. Pending.
- **BDRC**: generally open access with per-collection license.

---

## v1.0 milestone — proposed rewrite

**Current v1.0 definition (unclear)**: eight-branch "coverage" without specifying what counts.

**Proposed v1.0 definition (Pan Q2 approved 2026-11-02)**:

> **v1.0 ships when, for every Tier (1, 2, 3):**
> 1. Each Tier-1 rank has **at least 1 scan-first sample** committed with ⟨བརྟག⟩ marks on all draft columns.
> 2. Each Tier-1 rank has **at least 1 named human reviewer** signed up (CONTRIBUTORS.md entry) — even if review is still in progress.
> 3. Each Tier-2 target has **at least 1 scan-first sample** (reviewer-pending OK).
> 4. Each eight-branch (八系) has **at least 1 sample** (already met except as noted).
> 5. The Buddhist AI Charter has **shipping Python + TypeScript guardrail libraries** on PyPI + npm (currently pending Pan's credentials).

By this definition: today we are at 0 of 4 Tier-1 ranks sampled, 1 of 10 Tier-2 (Therīgāthā). This is honest work remaining.

---

## v0.10 milestone (interim)

**Proposed interim release once all 4 Tier-1 ranks have their first scan-first sample** (even without reviewers yet). This gives the project a visible marker of the pivot and something to point outreach letters at.

Target: **2026-12-01** if daily pacing holds for Tier 1.
