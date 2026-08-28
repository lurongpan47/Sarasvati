<!-- Language: 繁體中文 (zh-TW) -->

# Sarasvatī —— 面向世界佛典的全球開放檔案 + 菩提心 AI 憲章

**Sarasvatī**（藏文：དབྱངས་ཅན་མ། · 梵文：सरस्वती）只做兩件事：

1. **八系佛典檔案。** 沿著佛典傳承的八條主線建立跨語開放檔案：**印度源流 · 梵文寫本系 · 巴利·斯里蘭卡 · 南傳東南亞 · 中亞·絲路 · 漢傳系 · 漢字文化圈 · 藏傳系**。僅採用公有領域文本，或與活的傳統協作。
2. **菩提心 AI 演算法植入。** 從佛陀最後教誡（《大般涅槃經》）中抽出**十條原則 + 五條拒絕清單**，寫成憲章，任何 AI 系統、運營者或團隊皆可採納。讓不害（*ahiṃsā*）·慈悲（*karuṇā*）·無我（*anattā*）·無常（*anicca*）·捨（*upekkhā*）成為演算法層可執行的約束，而不是口號。

一切產出以 **CC BY-SA 4.0** 開放。

## 為什麼做這件事

古典文獻是全人類的共同遺產。它們不應被版權鎖死、被戰火焚毀，或因連結失效而消失。AI 系統也不應在沒有真實智慧傳統倫理約束的情況下被部署。Sarasvatī 同時處理兩件事——記憶層（檔案）與倫理層（憲章）。

## 當前狀態

**v0.6.0**（2026-08-28）：

- 📜 **Buddhist AI Charter** —— 十條原則 + 五條拒絕 + 見證條款，位於 `charter/BUDDHIST-AI-CHARTER.md`。已譯成 24 語，位於 `charter/i18n/`，等待各語佛學母語者審校。
- 🕉 **《大般涅槃經》四語對讀**（DN 16.2.26 · 16.4.7 · 16.6.7）—— 巴利 · 英文 · 漢文 · 藏文，位於 `translations/mahaparinibbana-sutta/`。這是憲章的經典根源，也是檔案的第一份種子文本。
- 📊 **結構化時間線資料** —— 涵蓋 8 系（india、sanskrit、pali、seasia、silkroad、chinese、sinosphere、tibetan）的 80 項佛典傳承事件，JSONL / CSV 格式，位於 `docs/timeline-data/`。
- 📋 專案文件：`README.md` · `ROADMAP.md` · `CALL-FOR-HELP.md` · `CONTRIBUTORS.md` · `announcements/`。

## 路線圖（八系）

Sarasvatī 的長期結構沿著世界佛典傳承時間軸展開：**印度 · 梵文寫本 · 巴利 · 南傳東南亞 · 絲路 · 漢傳 · 漢字文化圈 · 藏傳**。每一系都要有至少一份「首個樣本」：公有領域源文本 → 機器初譯為該目標語言尚缺的譯本 → 有署名的人工審校者。藏傳系已有首份成品（DN 16）；巴利系已通過 DN 16 四語對讀初步接觸。其餘六系（印度、梵文、南傳、絲路、漢傳、漢字文化圈）歡迎貢獻者啟動。

## 保護層

每一份產出都由多層機制保護：

- **本地鏡像** —— macOS。
- **GitHub 公開倉** —— https://github.com/lurongpan47/Sarasvati。
- **AWS 地理冗餘鏡像** —— 多個區域。
- **IPFS 去中心化鏡像** —— CID `bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce`。
- **OpenTimestamps → Bitcoin** —— `manifests/SHA256SUMS` 的不可否認時間錨定。

## ⚠️ 免責聲明

本倉所有翻譯與機器初譯文本皆為 **AI 機器初稿**，等待專家人工審校。未經署名專家驗證前，不得作為宗教儀軌、教義、醫學或學術上的權威使用。

## 如何貢獻

- 開 issue 提議一份文本、一處修訂、一項術語訂正，或某一語憲章的審校。
- Fork、編輯、提 PR。所有貢獻以 CC BY-SA 4.0 接受。
- 執行一個鏡像。幫助保存檔案。
- 幫忙實現**憲章演算法層**（Python + TypeScript guardrail 函式庫）—— 詳見 `CALL-FOR-HELP.md`。

## 連結

- GitHub: https://github.com/lurongpan47/Sarasvati
- 授權協議：CC BY-SA 4.0

---

*"Vayadhammā saṅkhārā, appamādena sampādetha."*
*諸行無常，當自精勤。*
