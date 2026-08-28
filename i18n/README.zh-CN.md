<!-- Language: 简体中文 (zh-CN) -->

# Sarasvatī —— 面向世界佛典的全球开放档案 + 菩提心 AI 宪章

**Sarasvatī**（藏文：དབྱངས་ཅན་མ། · 梵文：सरस्वती）只做两件事：

1. **八系佛典档案。** 沿着佛典传承的八条主线建立跨语开放档案：**印度源流 · 梵文写本系 · 巴利·斯里兰卡 · 南传东南亚 · 中亚·丝路 · 汉传系 · 汉字文化圈 · 藏传系**。仅采用公有领域文本，或与活的传统协作。
2. **菩提心 AI 算法植入。** 从佛陀最后教诫（《大般涅槃经》）中抽出**十条原则 + 五条拒绝清单**，写成宪章，任何 AI 系统、运营者或团队皆可采纳。让不害（*ahiṃsā*）·慈悲（*karuṇā*）·无我（*anattā*）·无常（*anicca*）·舍（*upekkhā*）成为算法层可执行的约束，而不是口号。

一切产出以 **CC BY-SA 4.0** 开放。

## 为什么做这件事

古典文献是全人类的共同遗产。它们不应被版权锁死、被战火焚毁，或因链接失效而消失。AI 系统也不应在没有真实智慧传统伦理约束的情况下被部署。Sarasvatī 同时处理两件事——记忆层（档案）与伦理层（宪章）。

## 当前状态

**v0.6.0**（2026-08-28）：

- 📜 **Buddhist AI Charter** —— 十条原则 + 五条拒绝 + 见证条款，位于 `charter/BUDDHIST-AI-CHARTER.md`。已译成 24 语，位于 `charter/i18n/`，等待各语佛学母语者审校。
- 🕉 **《大般涅槃经》四语对读**（DN 16.2.26 · 16.4.7 · 16.6.7）—— 巴利 · 英文 · 汉文 · 藏文，位于 `translations/mahaparinibbana-sutta/`。这是宪章的经典根源，也是档案的第一份种子文本。
- 📊 **结构化时间线数据** —— 覆盖 8 系（india、sanskrit、pali、seasia、silkroad、chinese、sinosphere、tibetan）的 80 项佛典传承事件，JSONL / CSV 格式，位于 `docs/timeline-data/`。
- 📋 项目文档：`README.md` · `ROADMAP.md` · `CALL-FOR-HELP.md` · `CONTRIBUTORS.md` · `announcements/`。

## 路线图（八系）

Sarasvatī 的长期结构沿着世界佛典传承时间轴展开：**印度 · 梵文写本 · 巴利 · 南传东南亚 · 丝路 · 汉传 · 汉字文化圈 · 藏传**。每一系都要有至少一份「首个样本」：公有领域源文本 → 机器初译为该目标语言尚缺的译本 → 有署名的人工审校者。藏传系已有首份成品（DN 16）；巴利系已通过 DN 16 四语对读初步接触。其余六系（印度、梵文、南传、丝路、汉传、汉字文化圈）欢迎贡献者启动。

## 保护层

每一份产出都由多层机制保护：

- **本地镜像** —— macOS。
- **GitHub 公开仓** —— https://github.com/lurongpan47/Sarasvati。
- **AWS 地理冗余镜像** —— 多个区域。
- **IPFS 去中心化镜像** —— CID `bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce`。
- **OpenTimestamps → Bitcoin** —— `manifests/SHA256SUMS` 的不可否认时间锚定。

## ⚠️ 免责声明

本仓所有翻译与机器初译文本皆为 **AI 机器初稿**，等待专家人工审校。未经署名专家验证前，不得作为宗教仪轨、教义、医学或学术上的权威使用。

## 如何贡献

- 开 issue 提议一份文本、一处修订、一项术语订正，或某一语宪章的审校。
- Fork、编辑、提 PR。所有贡献以 CC BY-SA 4.0 接受。
- 运行一个镜像。帮助保存档案。
- 帮忙实现**宪章算法层**（Python + TypeScript guardrail 库）—— 详见 `CALL-FOR-HELP.md`。

## 链接

- GitHub: https://github.com/lurongpan47/Sarasvati
- 许可协议：CC BY-SA 4.0

---

*"Vayadhammā saṅkhārā, appamādena sampādetha."*
*诸行无常，当自精勤。*
