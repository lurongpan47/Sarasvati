# Timeline Evidence Revision · 2026-W43

**Scan date:** 2026-10-19 (America/Los_Angeles)
**Candidates found:** 1 new event · 0 revisions
**Rule:** Additive only. Nothing deleted; `traditions.jsonl` and canonical PDF untouched. Written directly under Pan's 2026-09-21 auto-approve instruction; reversible by `git revert`.

---

## Written (appended to `events.jsonl` + `events.csv`)

### evt_090 · 海印寺重刻高丽八万大藏经（2026年起）
- **tradition:** `sinosphere`
- **period_zh:** 2026年起
- **period_en:** 2026–
- **title_zh:** 海印寺藏经都监重刻高丽大藏经 · 2026-10-29 告佛式启刻，8 万余版手工再雕，预计 5–10 年，板刻学校僧俗百余人参与
- **title_script:** 해인사 장경도감 대장경 판각 · 다시 새기는 대장경, 인류를 향하다
- **title_en:** Haeinsa re-carves the Tripiṭaka Koreana by hand — 80,000+ blocks, 5–10 years, begun 29 Oct 2026
- **Why:** The first complete re-carving of the Goryeo canon in ~800 years — a 刻经 event in the direct line of evt_036 (First Goryeo Canon) → evt_046 (Tripiṭaka Koreana, 1236–1251). Haeinsa founded a 장경도감 (藏經都監, the same office name as the 13th-century one) and a 판각학교 (board-carving school, 2024; ~500 trainees over five cohorts), of whom ~100 will carve. 300 t of wild-cherry / pear timber already secured and put into seawater (3-year soak, the Goryeo method). Haeinsa says this is not a replacement of the National Treasure blocks but a parallel set; the temple pairs it with ongoing digitisation and multilingual translation. The sinosphere lane had no row after 1994 (evt_074).
- **Evidence (≥2 independent):** Yonhap 2026-10-15 (`AKR20261014104100052`: 81,352 blocks, 29 Oct 14:00 告佛式 at 法界塔 yard, 5–10 years, ~100 carvers); Asia Today 2026-10-15; Hankyoreh 2026-10-15/16 (via supple.kr: 81,258 blocks, 판각학교 est. 2024, 500 graduates, 300 t timber in seawater); KBS; 현대불교 2026-10-19; 불교닷컴 2026-10-19; 경남일보 / 경남도민일보 / 내외일보 2026-10-14/15.
- **Links:** https://www.yna.co.kr/view/AKR20261014104100052 · https://www.asiatoday.co.kr/kn/view.php?key=20261015010004699 · https://supple.kr/news/cmv970dq5009sz768wcrtmx91 · https://news.kbs.co.kr/news/pc/view/view.do?ncd=8687537 · https://www.hyunbulnews.com/news/articleView.html?idxno=505911 · https://www.bulkyo21.com/news/articleView.html?idxno=65295
- **Caveat recorded:** block count differs across sources — 81,352 (Yonhap / Asia Today; the registered National Treasure count incl. later supplements) vs 81,258 (Hankyoreh; the figure already in evt_046). Row says "8 万余 / 80,000+" rather than pick one. The ceremony date (29 Oct) is 10 days in the future at write time; the row is dated by the announced start, as evt_083 (84000, 2026) was. If the ceremony is postponed, revise period, don't delete.

---

## No revisions
- evt_046 (Tripiṭaka Koreana, 81,258 woodblocks): unchanged; evt_090 is its modern continuation.

## Rejected this week
- **Eternity Foundation / Embassy-of-the-Free-Mind `sourcelibrary-v2`** (GitHub issues #5494 / #5497 / #5664 / #5665: importing BDRC Derge Kangyur/Tengyur scans + Esukhia e-texts, Mongolian Kanjur W4CZ5370, nine Sanskrit Tengyur-source editions machine-translated): **single-source** (the project's own issue tracker), no published edition, licence unsettled by their own admission. Not a canon-transmission event yet. Watch.
- **Gyan Bharatam Mission** (UP 15,890 manuscripts / 7.56 lakh pages scanned; Rajasthan 1.24 lakh; Darbhanga launch 2026-09-18): general heritage digitisation, no Buddhist-text list — carry-over rejection (4th week).
- **China Tibetology Research Center Qinghai forum (2026-09-20)**: restates STTAR 28 vols = evt_086; no new edition.
- Carry-overs unchanged: OpenTipitaka 5.0/6.0 (single-source, 4th week), Tai-Khamti uploads (no text list), Tsadra BCA manuscripts (no dated edition), CanonRAG (retrieval layer).

## Scan-script note
`scripts/timeline_evidence_scan.sh` returned nothing usable this week (84000 and SuttaCentral feeds timed out; tbrc.org redirects; GRETIL blank). The candidate came from manual web search. The script's source list should gain Korean/Japanese Buddhist press (불교신문, 법보신문, 中外日報) — noted, not changed this run.

## Impact on preview image
- One row at the right edge (2026–) in the sinosphere lane. Canonical PDF unchanged → `docs/timeline-preview-3lang.png` not re-rendered. Data-only until the graphic is redrawn.
