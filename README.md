# དབྱངས་ཅན་མ།  ·  Sarasvatī  ·  萨拉斯瓦蒂

> **A global open archive for the protection and cross-lingual translation of world classical canons.**
> **全世界经典跨语种保护与流通的开放归档。**
> **འཛམ་གླིང་གི་གནའ་བོའི་གཞུང་རྣམས་སྐད་བརྒྱུད་སྐད་ཡིག་སོ་སོའི་ལམ་ནས་སྲུང་སྐྱོབ་དང་སྤེལ་བའི་ཁྲོམ་གྱི་ཉར་ཚགས།**

---

## 项目宗旨  ·  Mission  ·  ལས་ཀའི་དམིགས་ཡུལ།

**中文**  经典是人类的公共遗产。它们不该被版权圈养、被战火焚毁、被数字断链失落。萨拉斯瓦蒂项目做三件事：

1. **翻译**  把仍在版权保护期外的公有领域文本，用现代 AI 与人机协作流水线转成尚未有译本的目标语（首批：梵文/英文 → 藏文）。所有产出为**机器初译**，公开征集人工审定。
2. **归档**  同一份文件多点镜像（GitHub + 本地 + AWS + 未来加入 Internet Archive / IPFS），SHA-256 校验保证完整性。
3. **开放**  一律 **CC BY-SA 4.0** 授权，任何人可自由复制、改进；派生作品必须同样开源。

**English**  Canonical texts are humanity's common inheritance. They should not be locked by copyright, burnt by war, or lost by broken links. Sarasvatī does three things: **translate** public-domain texts into languages that lack translations (AI first-draft + open review); **archive** them redundantly with cryptographic integrity; **release** everything under CC BY-SA 4.0.

**བོད་ཡིག**  བསྟན་བཅོས་གནའ་བོ་རྣམས་ནི་མི་ཡི་སྤྱིར་བཏང་གི་བདག་གཞིས་ཡིན་ལ། ཁྲིམས་མཐར་གཏུགས་པའི་བདག་གི་ལག་ཏུ་བཏགས་པའམ། དགྲ་དམག་གི་མེ་སྟེང་ནས་བསྲེགས་པའམ། གློག་ཀླད་ཀྱི་བཅོས་ལམ་ཆག་པས་ཡལ་བར་མི་བྱ། དབྱངས་ཅན་མའི་ལས་གཞིས་བྱ་བ་གསུམ་ལས།  ༡། སྐད་བསྒྱུར།  ༢། ཉར་ཚགས།  ༣། ཀུན་ལ་གོ་བའི་ལམ་ནས་སྤེལ་བ་ཞེས་བགྱིད།

---

## 目前的进度  ·  Current release

### v0.1 (2026-08-28)
- 📜 **Suśruta Saṃhitā · Sūtrasthāna** (46 章) 藏译机器初稿
  - 底本  Kaviraj Kunjalal Bhishagratna, *An English Translation of the Sushruta Samhita*, 1907 (public domain)
  - 输出  `translations/sushruta-samhita/sutrasthana/Sushruta-Sutrasthana-bo-v3.docx` (.docx + .pdf)
  - 全藏文，46 章齐备，0 汉字残留，脚注/存疑处以 `⟨བརྟག⟩`、`⟨བརྟག་དགོས།⟩` 标记
- 📚 世界佛典传承时序图（八系并观）`docs/Global-Buddhist-Canon-Transmission-Timeline.pdf`
- 📋 藏译工程规划（体例·术语·186 章章目）`docs/Sushruta-Tibetan-Project-Plan.docx`

### 未来 · Roadmap
- 📖 Suśruta Saṃhitā 后续五部：Nidāna（16 章）· Śārīra（10 章）· Cikitsā（40 章）· Kalpa（8 章）· Uttaratantra（66 章）
- 🌍 更多经典：视需要与合作者提议扩展至其他语系（巴利↔藏、汉↔藏、藏↔英 等）
- 🤝 与 84000、BDRC、Adarshah、SuttaCentral、Internet Archive 建立镜像与协作

---

## ⚠️ 免责与阅读须知  ·  Disclaimer

本仓库全部藏文译文为 **AI 机器初译稿**，语域为现代藏语医学/古典文本，**非古典医典体**。凡涉及药物鉴定、剂量、marma（要害）方位、藏医与阿育吠陀概念不完全重合处，**必须由藏医译师人工审定**方可作为定稿使用。

⟨བརྟག⟩ = 存疑，请审。
⟨བརྟག་དགོས། བོད་སྨན་མཁས་པས་ཞིབ་བརྟག་བྱ་དགོས།⟩ = 须藏医验定。

**校对邀请**  欢迎藏医、印度学、梵学、译经学者提 issue / PR。逐段校订、术语商榷、章题修订均欢迎。校订贡献者按提交次数记入 CONTRIBUTORS。

---

## 目录结构  ·  Layout

```
Sarasvati/
├── README.md                   ← 本文件
├── LICENSE                     ← CC BY-SA 4.0
├── CHANGELOG.md                ← 版本历史
├── CONTRIBUTORS.md             ← 贡献者与致谢
├── docs/
│   ├── Sushruta-Tibetan-Project-Plan.docx        工程规划（体例/术语/186 章）
│   └── Global-Buddhist-Canon-Transmission-Timeline.pdf   世界佛典传承时序图
├── translations/
│   └── sushruta-samhita/
│       ├── STYLE.md                                     体例与术语参考
│       └── sutrasthana/
│           ├── Sushruta-Sutrasthana-bo-v3.docx          ← 交付主文件
│           ├── Sushruta-Sutrasthana-bo-v3.pdf          ← 冻结版
│           ├── source/       (Bhishagratna 1907 英译 46 章清洗文本)
│           └── raw/          (4 组子agent 输出 raw txt，可溯源)
└── manifests/
    ├── SHA256SUMS
    └── SHA256SUMS.txt         (人类可读版)
```

---

## 完整性校验  ·  Integrity

```bash
cd Sarasvati
shasum -a 256 -c manifests/SHA256SUMS
```

发布节点  ·  Release nodes：
- GitHub: `https://github.com/wingring47-stack/Sarasvati`
- 本地: `~/clawd/Sarasvati/` (macOS)
- AWS: `aws-quant:/home/ubuntu/Sarasvati/` (us-east-1)
- （规划中）Internet Archive · IPFS · Zenodo (DOI)

---

## 联系  ·  Contact

- Issues & PRs → GitHub
- Project code: **Sarasvatī**（藏文 `དབྱངས་ཅན་མ།` · 梵文 `सरस्वती` · 智慧、语言、经典之神）
- 项目发起 2026-08-27

---

*献给经典守护者。To those who keep the canons safe.*

*"ཆོས་ནི་སྐལ་བ་མེད་པའི་མི་ལ་མི་སྟོན།"*
*—— The Dharma is not shown to those without the fortune to receive it, but the text stays open for those who do.*
