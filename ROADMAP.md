# ROADMAP · Sarasvatī

*Guided by the world Buddhist canon transmission timeline (八系并观). Sarasvatī takes each of the eight branches as a long-term line of protection & translation work.*

---

## Foundational principles

1. **Public domain first.** We work only from texts safely out of copyright, or explicitly released under compatible open licenses.
2. **AI first-draft, human final.** All translations are machine drafts pending expert review. No "authoritative" claim without named human reviewers.
3. **Redundant preservation.** Every artifact lives in ≥ 3 locations with SHA-256 integrity, and is released under CC BY-SA 4.0.
4. **Cross-lingual, not translation-imperialist.** Where a language lacks a translation, we make one. We do not overwrite existing living traditions' work.

---

## The eight branches (八系)

Sarasvatī's long-term structure follows the transmission timeline. Each branch may host multiple translation projects.

### 1. India — 印度源流 · `india`
The oral origin; councils; sects; Mahāyāna emergence.
- **Now**: reference material only.
- **Future**: work on public-domain critical editions of foundational sūtras.

### 2. Sanskrit manuscript tradition — 梵文写本系 · `sanskrit`
Palm-leaf, birch-bark, modern critical editions.
- **Priority pool**: GRETIL corpus (public-domain machine-readable Sanskrit), Nepalese Navagrantha, Gilgit finds.
- **Sample targets**: Aṣṭāṅgahṛdayasaṃhitā re-translation cross-check with existing Tibetan; Nāgārjuna's Mūlamadhyamakakārikā cross-language readings.

### 3. Pāli — 巴利·斯里兰卡 · `pali`
Theravāda canon.
- **Priority pool**: PTS Roman-script editions (out of copyright post-1928); SuttaCentral parallel data.
- **Sample targets**: uncovered nikāya passages for Tibetan/Chinese cross-reading.

### 4. Southeast Asian Theravāda — 南传东南亚 · `seasia`
Burma, Siam, Cambodia, Laos.
- **Priority pool**: 5th, 6th, 8th, 9th council editions; VRI Chaṭṭha Saṅgāyana digital.
- **Sample targets**: Khmer, Lao, Shan-script vernacular commentaries with no English/Chinese versions.

### 5. Silk Road / Central Asia — 中亚·丝路 · `silkroad`
Gāndhārī, Khotanese, Tocharian, Uighur, Tangut.
- **Priority pool**: Schøyen Collection, Bower manuscript, Dunhuang cave 17 dispersals (BL, BnF, IDP).
- **Sample targets**: individual Dunhuang manuscripts with no full modern translation.

### 6. Chinese canon — 汉传系 · `chinese`
Kaibao → Kaixi → Jiaxing → Qianlong → Taishō → CBETA.
- **Priority pool**: CBETA public-facing texts; Dunhuang colophons.
- **Sample targets**: minor texts in Taishō vols 85 (dunhuang) never translated to English/Tibetan.

### 7. Sinosphere — 汉字文化圈 · `sinosphere`
Korea, Japan, Vietnam.
- **Priority pool**: Tripiṭaka Koreana (public colophons); Nara scriptoria digitizations; SAT database.
- **Sample targets**: Korean/Japanese commentaries without foreign-language versions.

### 8. Tibetan — 藏传系 · `tibetan` **(current focus)**
Kangyur / Tengyur; Mongolian & Manchu editions.
- **Now**: Suśruta Saṃhitā EN→bo (Sūtrasthāna 46 chapters delivered v0.1).
- **Next**: remaining 140 chapters of Suśruta (Nidāna 16 + Śārīra 10 + Cikitsā 40 + Kalpa 8 + Uttaratantra 66).
- **Future**: cross-check with Aṣṭāṅgahṛdaya Tibetan; Yogaśataka; other classical medical/philosophical texts lacking Tibetan translations.

---

## v0.1 → v1.0 milestones

| Version | Target date | Deliverable |
|---|---|---|
| v0.1.0 ✅ | 2026-08-28 | Suśruta · Sūtrasthāna Tibetan draft (46 ch) |
| v0.2.0 | tbd | Timeline structured data (80 events × 8 traditions); ROADMAP; onboarding docs |
| v0.3.0 | tbd | Suśruta · Nidāna + Śārīra (26 ch) |
| v0.4.0 | tbd | Suśruta · Cikitsā (40 ch) |
| v0.5.0 | tbd | Suśruta · Kalpa + Uttaratantra (74 ch) |
| v1.0.0 | tbd | Suśruta Saṃhitā full 186 ch, first human-reviewed round complete |
| v1.1.0 | tbd | First cross-branch project (Sanskrit or Pāli sample) |

---

## Structured data included

`docs/timeline-data/` (v0.2 addition):
- `traditions.jsonl` — the 8 branches (id, zh, en, note)
- `events.jsonl` — 80 events (id, tradition, period, tri-lingual title)
- `events.csv` — same, as CSV

This lets anyone build interactive visualizations, filter by tradition/era, or bind these events to their own translation projects.

---

## How to join

- Pick a branch. Pick an untranslated text. Open an issue proposing it.
- Or pick an existing draft and human-review it, chapter by chapter.
- Or pick a language pair we haven't touched and demonstrate a pipeline.
- Or run a mirror.

All contributions CC BY-SA 4.0.

---

*"Where translation stops, understanding stops. Where understanding stops, compassion cannot begin."*
