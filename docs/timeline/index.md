---
layout: page
title: "Transmission Timeline"
permalink: /timeline/
---

# Global Buddhist Canon Transmission Timeline

**82 events × 8 traditions.** Trilingual titles (English · 中文 · བོད་ཡིག). Living dataset — PRs welcome.

<p align="center">
  <img src="{{ '/timeline-preview-3lang.png' | relative_url }}" alt="Timeline preview — 8 traditions, 82 events" style="max-width:100%; height:auto; border:1px solid #ddd; border-radius:6px;">
</p>

<p style="margin: 1.5rem 0;">
  <a href="{{ '/Global-Buddhist-Canon-Transmission-Timeline.pdf' | relative_url }}" style="display:inline-block; padding:.6rem 1rem; background:#2a5885; color:#fff; text-decoration:none; border-radius:6px; font-weight:600; margin-right:.5rem;">📄 Full PDF</a>
  <a href="{{ '/timeline-preview-3lang.png' | relative_url }}" style="display:inline-block; padding:.6rem 1rem; background:#555; color:#fff; text-decoration:none; border-radius:6px; font-weight:600; margin-right:.5rem;">🖼 Preview PNG</a>
  <a href="{{ '/timeline-banner-3lang.png' | relative_url }}" style="display:inline-block; padding:.6rem 1rem; background:#555; color:#fff; text-decoration:none; border-radius:6px; font-weight:600;">🎌 Banner PNG</a>
</p>

<embed src="{{ '/Global-Buddhist-Canon-Transmission-Timeline.pdf' | relative_url }}" type="application/pdf" width="100%" height="720px" style="border:1px solid #ddd; border-radius:6px;">

---

## Structured data

The timeline is machine-readable and versioned in the repo. **Do not modify canonical files without maintainer approval** — they are checkpoints of an ongoing scholarly review.

- [`docs/timeline-data/traditions.jsonl`](https://github.com/lurongpan47/Sarasvati/blob/main/docs/timeline-data/traditions.jsonl) — the 8 branches (id, zh, en, note)
- [`docs/timeline-data/events.jsonl`](https://github.com/lurongpan47/Sarasvati/blob/main/docs/timeline-data/events.jsonl) — 82 milestones with tri-lingual titles
- [`docs/timeline-data/events.csv`](https://github.com/lurongpan47/Sarasvati/blob/main/docs/timeline-data/events.csv) — CSV mirror for spreadsheet users
- [`docs/timeline-data/README.md`](https://github.com/lurongpan47/Sarasvati/blob/main/docs/timeline-data/README.md) — schema + coverage docs

### Schema at a glance

```jsonl
{"id": "council-1-rajgir",
 "tradition_id": "india",
 "year_min": -483, "year_max": -483,
 "title_en": "First Council at Rājagṛha",
 "title_zh": "第一次结集",
 "title_bo": "བསྡུ་བ་དང་པོ།",
 "note": "..."}
```

---

## See also

- [Buddhas & Bodhisattvas network]({{ '/buddhas-bodhisattvas-network.html' | relative_url }}) — interactive 132-node visualisation.
- [Branches page]({{ '/branches/' | relative_url }}) — the eight branches as project scope.
