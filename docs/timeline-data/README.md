# Timeline data · 世界佛典传承时序

Structured extraction of the **World Buddhist Canon Transmission Timeline** (八系并观 / Eight-system chronology), which underlies Sarasvatī's ROADMAP.

## Files

- `traditions.jsonl` — 8 traditions/branches
- `events.jsonl` — 80 canonical-transmission milestones
- `events.csv` — same, comma-separated

## Schema

**traditions.jsonl** (one JSON object per line):
```
{ "id": "tibetan", "zh": "藏传系", "en": "Tibetan, Mongolian, Manchu", "note": "西藏·蒙古·满洲" }
```

**events.jsonl**:
```
{
  "id":            "evt_027",
  "tradition":     "chinese",              // FK → traditions.id
  "period_zh":     "645–664年",
  "period_en":     "645–664",
  "title_zh":      "玄奘携归梵本六五七部·玄奘译场",
  "title_script":  "玄奘",                 // any indigenous / iconic script snippet
  "title_en":      "Xuanzang; 657 Sanskrit manuscripts to Chang'an"
}
```

## Coverage summary

| Tradition        | Events |
|------------------|-------:|
| india            | 8      |
| sanskrit         | 6      |
| pali             | 6      |
| seasia           | 9      |
| silkroad         | 6      |
| chinese          | 13     |
| sinosphere       | 9      |
| tibetan          | 12     |
| (multi-branch)   | 11     |

*(counts approximate; see `events.jsonl` for canonical source)*

## Source

Original graphic: `docs/Global-Buddhist-Canon-Transmission-Timeline.pdf` (bundled).

## License

CC BY-SA 4.0 (same as project). Attribution: "Sarasvatī project, timeline data v0.2."

## Uses

- Interactive web visualization (d3 / observable / vega)
- Filter/pivot for research
- Bind future translation projects to a specific timeline node
- Extend by adding rows; PRs welcome

## Revision history

### revision v2 · 2026-08-29

Full audit of `events.jsonl` against the canonical source PDF
`docs/Global-Buddhist-Canon-Transmission-Timeline.pdf`
(SHA-256: `e97ba4d82ad2abd7e6640b17ae58f4de2a50d8bc4b0ca31553d09b05c68c6cca`).

Summary:

- **+2 新增 (MISSING → added)**
  - `evt_081` — 霍奇森搜集尼泊尔梵本 (Brian H. Hodgson, 1824–1845, sanskrit column). Was absent from v1.
  - `evt_082` — 玄奘携归梵本六五七部 (657 Sanskrit manuscripts, 645–664, sanskrit column). PDF splits this from Xuanzang's Chang'an bureau (`evt_026`, chinese column). v1 had collapsed both PDF cells into a single chinese-column event.
- **~50 修正 (DIVERGENT → fixed)** — period_zh / period_en / tradition realigned to the PDF's row-header time band and column tradition. Notable tradition shifts:
  - `evt_014` Bower Manuscript: `silkroad` → `sanskrit` (PDF places it in the 梵文写本系 column)
  - `evt_022` Polonnaruwa / Parākramabāhu: `seasia` → `pali` (PDF places it in the 巴利·斯里兰卡 column)
  - `evt_069` SuttaCentral: `pali` → `seasia` (PDF places it in the 南传东南亚 column)
  - Dozens of period bands realigned to the PDF's row headings (e.g. 8–12世纪 → 8世纪 for Vikramaśīla; 12世纪 → 1203年 for Vikramaśīla-destroyed; etc.). Where an event carried a precise sub-year, that year is preserved in `title_zh` inside parentheses.
- **0 删除** — every v1 row maps to a PDF cell; nothing dropped.
- **Total after v2:** 82 events (was 80).

### revision v1 · 2026-08-28

Initial extraction from the source PDF — 80 events across 8 traditions.

