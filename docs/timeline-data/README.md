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
