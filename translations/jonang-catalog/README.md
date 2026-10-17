# 觉囊·大智慧藏总目录 — 汉译草稿

**ཇོ་ནང་རིག་མཛོད་ཆེན་མོའི་དཀར་ཆག** · *Jonang Rig-mdzod chen-mo'i dkar-chag*

Sarasvatī 第八支（藏传佛典）档案材料 · AI 一稿 ⟨བརྟག⟩ · 待具名学者复核

---

## 文件清单

| 文件 | 大小 | 描述 |
|---|---|---|
| `source.pdf` | 8.4 MB | 原本：觉囊文丛第 216 册藏文 PDF（449 页，~99 万藏文字符）— **仅存本机，不入库、不分发**（见下「来源与权利」） |
| `pages_tib/pNNN.txt` | 449 files | 原本按页抽取的藏文文本（`pypdf`，有损，见「已知限制」第 5 条）— **仅存本机，不入库** |
| `pages_zh/pNNN.md` | 449 files | 对应页汉译（含源 token 用量 / 时间 / 费用元数据） |
| `jonang-catalog_zh.md` | 414 KB | 全本合并 Markdown（CC BY-SA 4.0 头 + 449 页译文 + 源页标记） |
| `jonang-catalog_zh.pdf` | 892 KB | 全本中文版 PDF (210 页，Noto Sans CJK) |
| `jonang-catalog_zh.docx` | 213 KB | 全本中文版 Word (SimSun, 可编辑复核) |
| `GLOSSARY.md` | — | 术语与人名对照表（含待复核项） |
| `translate.py` | — | 翻译脚本（resumable，可用 `state.json` 续跑）。脚本引用的 `glossary.json` 在本次运行时**不存在**（回退为空表）；术语统一未被脚本强制，`GLOSSARY.md` 为事后整理 |
| `build_pdf.py` | — | 中文 PDF 生成脚本 |
| `translate.log` | — | 完整翻译日志（每页 token/时间/费用） |
| `state.json` | — | 翻译进度状态（done / failed / token 累计） |

## 翻译统计

| | |
|---|---|
| 源页数 | 449 |
| 实际翻译页 | 447（2 页为源 PDF 空白页） |
| 失败页 | **0** |
| 源字符数 | 990,516 (Tibetan) |
| 译文字符数 | ~160,000 (Chinese) ← 更紧凑 |
| 模型 | `anthropic/claude-opus-4-7` |
| 用时 | ~90 分钟（11-14 秒/页，并行度=1） |
| **总费用** | **$30.67** (prepaid, Anthropic API) |
| 日期 | 2026-10-17 (America/Los_Angeles) |

## 关于内容

《觉囊大宝藏总目录》是觉囊派（Jo-nang-pa）大藏——即觉囊派传承所整理的完整 གསུང་འབུམ (gsung 'bum, 文集)集成——的目录。按人物时序排列：

1. **先期传承**（第 1–10 页）：卓译师·喜饶扎巴 → 域摩·弥觉多杰 → 达磨伊什瓦拉 → 南喀沃色 → 色摩且瓦
2. **多波巴·喜饶坚赞 (Dolpopa, 1292–1361)** 文集（第 11 页起 — 该派实际奠基者，他空见集大成者）
3. 后代传承（含多罗那他 Tāranātha, 1575–1634）
4. **医方（藏医）章节**（第 88 页前后）— 涉及汤剂 / 散剂 / 膏剂 / 灌肠（niruha）等。
   ⚠️ **与 Sarasvatī 的姊妹项目 `~/clawd/Sushruta-Tibetan/` 直接相关**，可做交叉参考。

## 来源与权利 · Provenance and rights (2026-10-17)

原本《觉囊文丛》第 216 册是**现代排印本**（非公版古籍）。Sarasvatī 的 asteya 原则只收公版来源；在其权利状态查明之前，`source.pdf` 与逐页抽取的 `pages_tib/` **不入 git、不推到 GitHub、不入 IPFS / 清单 / 时间戳**，只留在本机（`.gitignore` 有记）。入库的是 AI 汉译稿本身（目录条目 = 书名 / 作者 / 卷次等书目事实）、术语表、脚本与日志。原本由 Pan 提供；若 Pan 确认其为开放授权，再把来源补入库，并在 CHANGELOG 记一笔。复核者请直接以原书 / 原 PDF 对照，不要以 `pages_tib/` 为准。

## 已知限制 / 待复核项

1. **所有汉译均为 AI 一稿**（Claude Opus 4.7），未经任何人工复核。标记 `⟨བརྟག⟩` 存在于合并 Markdown 顶部，表示整份文件待审。
2. 术语对照表（`GLOSSARY.md`）列出了核心人名 / 教派术语 / 文献类别的汉译，连同已知的歧义点。
3. 源 PDF 的某些点阵（leader dots）在 `pypdf` 抽取时呈现为 `���`，脚本已处理为 `……`。个别可能遗漏。
4. 多波巴等常见名字的汉译存在学界多种版本（如 "喜饶坚赞" vs "西饶坚参"），本稿统一采用其中一种，具体见 `GLOSSARY.md`。
5. **`pypdf` 抽取有损**：字体映射把部分下加字丢掉或换掉（如 བླ་མ་ 抽成 `བ་མ་`，ཀྱི་ 抽成 `ཀྙི་`，བཞི་ 抽成 `བཞྙི་`），模型是在这种带噪文本上翻译的，多数处靠上下文还原（`བ་མ་` → 上师），但人名音译处可能出错。10-17 推送线抽查 p011 / p088 时发现一例：p088 `དཀའ་བཞི་འཛིན་པ་བློ་ལྡན་བཟང་པོ` 译作「四难论持者**宝贤** (Kādrug Dzinpa Lodan Zangpo)」— *blo ldan bzang po* 应为「洛丹桑波 / 慧贤」，「宝贤」是 *rin chen bzang po*；括注的 Kādrug 应为 *dka' bzhi*。译文未改（一日之见不改稿），记入 `GLOSSARY.md` 待复核项。

## 复核欢迎

如您是觉囊派研究者 / Dolpopa 或 Tāranātha 文集的汉译者 / 任何藏传佛教学者，恳请复核本目录。
修订请在相应 `pages_zh/pNNN.md` 文件中直接改写并提 PR；在 `CONTRIBUTORS.md` 中记录您的署名范围。

---

**License**: CC BY-SA 4.0 (与 Sarasvatī 整体一致)
**Repo**: `~/clawd/Sarasvati/translations/jonang-catalog/`
**上游**: Sarasvatī 第八支 (藏传佛典全球开放归档)
**Draft marker**: `⟨བརྟག⟩` (未复核)
