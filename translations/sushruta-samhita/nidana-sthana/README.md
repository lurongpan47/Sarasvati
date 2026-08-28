# Suśruta Saṃhitā · Nidānasthāna · ནད་གཞིའི་གནས།

**Volume 2 · Diagnostic treatise · 16 chapters · Tibetan machine-translation draft v1**

- Source: Kaviraj Kunjalal Bhishagratna (1907), *An English Translation of the Sushruta Samhita*, public domain
- Delivered: 2026-08-28 (v0.5.0)
- Method: single Claude Opus 4.7 subagent, ~32,000 English words, ~1300 lines Tibetan
- License: CC BY-SA 4.0

## Deliverables

| File | Purpose |
|---|---|
| `Sushruta-Nidanasthana-bo-v1.docx` | Word (Uchen script, layout-ready) |
| `Sushruta-Nidanasthana-bo-v1.pdf` | Frozen PDF |
| `raw/nidana_all.txt` | Sub-agent raw output (traceable) |
| `source/ch01.txt` – `ch16.txt` | Bhishagratna English chapters, cleaned |
| `source/INDEX.tsv` | Chapter titles + source URLs |

## Chapters covered

Diagnosis of: nervous-system diseases · haemorrhoids · urinary calculus · anal fistula · leprosy & skin diseases · diabetes · abdominal enlargement · foetal obstruction · abscess · erysipelas/sinus/mammae · glands/scrofula/tumours/goitre · hernia/tumours/elephantiasis · minor diseases · penis diseases · fractures-dislocations · mouth diseases.

## Review markers

- ⟨བརྟག⟩ = uncertain term/name; expert review needed
- ⟨བརྟག་དགོས། བོད་སྨན་མཁས་པས་ཞིབ་བརྟག་བྱ་དགོས།⟩ = dosage / anatomical / medical parameter; Tibetan medical practitioner review required
- Sanskrit disease names without Tibetan equivalent are transliterated per STYLE.md rules

## Zero-Chinese guarantee

The document contains 0 CJK characters. Verify:
```
python3 -c "import re; print(sum(1 for _ in re.finditer(r'[\u4e00-\u9fff]', open('Sushruta-Nidanasthana-bo-v1.docx.txt').read())))"
```

## Human review welcome

Open a PR with corrections. Contributions accepted under CC BY-SA 4.0.
