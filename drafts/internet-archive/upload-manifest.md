<!-- Prepared 2026-09-13 by Lucy. IA upload flow: Pan reviews metadata → Pan approves Lucy to upload OR runs upload.sh himself. -->

# Sarasvatī v0.9 — Internet Archive Upload Manifest

**Target collection**: [`opensource`](https://archive.org/details/opensource) (also indexed under `opensource_texts` = Community Texts) — free, permanent, world-mirrored.
**Uploader**: Sarasvatī project (Lucy prepares the package; Pan approves the metadata and either authorises Lucy to upload with his IA credentials, or runs `upload.sh --live` himself).
**License for every item**: [CC BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/) — matches repo `LICENSE`.
**Common creator**: `Dr. Lurong Pan (潘麓蓉) · Sarasvatī project`
**Common contact**: (Pan to fill on first upload; IA propagates from account.)

## Why Internet Archive

IA is the **fastest additional mirror** we can stand up right now:
- Free forever, world-mirrored (Petabox + partial replication at partner libraries).
- No academic gate-keeping — we do not need a librarian's sponsorship.
- Every upload gets a stable `archive.org/details/<identifier>` URL, permanent DOI-style permalink, and torrent + IPFS gateway automatically.
- Complements the primary GitHub repo and the eventual Zenodo DOI without competing with them.

## Items (9 total)

Each item below becomes **one IA item** (`https://archive.org/details/<identifier>`). Files listed are what `upload.sh` will push. Paths are relative to the repo root (`~/clawd/Sarasvati/`).

### 1. `sarasvati-charter-v1.1`
- **Title**: Buddhist-AI Charter v1.1 (Sarasvatī project, 24-language edition)
- **Files**:
  - `charter/BUDDHIST-AI-CHARTER.md` (English + trilingual header)
  - `charter/CHANGELOG.md`
  - `charter/i18n/README.md` (translator's note)
  - `charter/i18n/CHARTER.*.md` × 24 languages
- **Description**: Ten principles and five refusals for AI systems, distilled from the Buddha's last teachings (Mahāparinibbāna Sutta). v1.1 with framing-defense clauses from the 2026-08-31 24-hour cross-model fuzz. Charter body plus 24 parallel-language editions (zh-CN, zh-TW, ja, ko, vi, bo, hi, sa, pi, th, si, my, km, id, mn, es, fr, de, it, pt, ru, ar, fa, tr). AI-drafted; awaiting named human review per language.
- **Subject**: `buddhism; ethics; artificial intelligence; ai safety; mahaparinibbana sutta; open charter; multilingual`
- **Language**: `multiple` (25: English + 24 translations)
- **Mediatype**: `texts`
- **Collection**: `opensource` (auto-inherits `opensource_texts`)

### 2. `sarasvati-dn16-mahaparinibbana-4lang`
- **Title**: Mahāparinibbāna Sutta — Final Instructions (DN 16, 4-language parallel reading)
- **Files**:
  - `translations/mahaparinibbana-sutta/README.md`
  - `translations/mahaparinibbana-sutta/final-instructions-4lang.md`
- **Description**: Selected passages from the Buddha's last discourse (Dīgha Nikāya 16). Pāli (PTS, PD), English (Rhys Davids 1910, PD), Chinese (T01 Taishō, PD), Tibetan (Sarasvatī AI draft cross-referenced with Derge Kangyur). Anchor text for both the Pāli branch and the Charter itself. AI-drafted columns flagged `⟨བརྟག⟩` awaiting review.
- **Subject**: `buddhism; pali canon; mahaparinibbana; digha nikaya; parallel translation; tibetan; chinese buddhist canon`
- **Language**: `pli; eng; zho; bod` (multiple)

### 3. `sarasvati-ashoka-rock-edict-XII`
- **Title**: Aśoka Major Rock Edict XII — Religious Tolerance (Girnar recension, 4-language)
- **Files**: `translations/ashoka-edicts/major-rock-edict-XII-4lang.md`
- **Description**: India-branch first sample. Girnar recension of Aśoka's Major Rock Edict XII (c. 257 BCE), one of the earliest surviving royal decrees on religious pluralism. Prakrit + English from Hultzsch 1925 (PD); Chinese and Tibetan are Sarasvatī AI drafts awaiting named human review. CC BY-SA 4.0.
- **Subject**: `buddhism; ashoka; edicts of ashoka; prakrit; ancient india; religious tolerance; epigraphy`
- **Language**: `pra; eng; zho; bod` (multiple)

### 4. `sarasvati-prajnaparamita-hridaya`
- **Title**: Prajñāpāramitā Hṛdaya Sūtra — Heart Sūtra (short recension, 5-language)
- **Files**: `translations/prajnaparamita-hridaya/short-recension-4lang.md`
- **Description**: Sanskrit-manuscript-branch first sample. Nepalese Navagrantha short recension of the Heart Sūtra: Sanskrit Devanāgarī + IAST (Müller & Nanjio 1884, PD), Chinese (Xuánzàng T251, PD), Tibetan (Derge Kangyur Tōh. 531, PD), fresh English AI draft. AI columns await review; CC BY-SA 4.0.
- **Subject**: `buddhism; prajnaparamita; heart sutra; sanskrit manuscripts; mahayana; xuanzang; tibetan kangyur`
- **Language**: `san; eng; zho; bod` (multiple)

### 5. `sarasvati-gandhari-dharmapada-khotan-Ia`
- **Title**: Gāndhārī Dharmapada — Khotan fragment Ia, opening verses (3-language)
- **Files**: `translations/gandhari-dharmapada/khotan-fragment-Ia-3lang.md`
- **Description**: Silk-Road-branch first sample. Verses 1–4 of the Khotan Kharoṣṭhī birch-bark manuscript context (Dutreuil de Rhins). Gāndhārī column is a **pedagogical reconstruction** from the Pāli parallel to stay strictly public-domain (Brough 1962 edition still in copyright); every verse flagged `⟨བརྟག⟩` for a Gāndhārī specialist to replace with the authentic Brough/Lenz reading or a GRETIL PD file. English + Chinese are AI drafts. CC BY-SA 4.0.
- **Subject**: `buddhism; gandhari; dharmapada; kharosthi; silk road; central asia; khotan manuscripts`
- **Language**: `pra; eng; zho` (multiple; Gāndhārī labelled `pra` per ISO 639-2 collective)

### 6. `sarasvati-foyijiao-jing-T389`
- **Title**: Fó yíjiào jīng 佛遺教經 — Buddha's Bequeathed Teaching (T389, selected passages, 4-language)
- **Files**: `translations/foyijiao-jing/T389-selected-4lang.md`
- **Description**: Chinese-canon-branch first sample. Selected core passages of the *Fó chuí bān-nièpán lüè-shuō jiàojiè jīng* (Kumārajīva, Taishō vol. 12 no. 389, PD by age). English, Tibetan and Modern Chinese vernacular columns are Sarasvatī AI drafts — no modern copyrighted translation reused — awaiting named human review. CC BY-SA 4.0.
- **Subject**: `buddhism; chinese buddhist canon; taisho tripitaka; kumarajiva; foyijiao; T389; bequeathed teaching`
- **Language**: `zho; eng; bod` (multiple)

### 7. `sarasvati-karaniya-metta-sutta-Sn1.8`
- **Title**: Karaṇīya Mettā Sutta — Discourse on Loving-Kindness (Sn 1.8, complete, 5-language)
- **Files**: `translations/karaniya-metta-sutta/Sn1.8-4lang.md`
- **Description**: Southeast-Asian-Theravāda-branch first sample. Complete 10 verses of Sn 1.8. Pāli (PTS, PD) and English (Chalmers 1932, PD) are historical; Chinese, Burmese and Thai are Sarasvatī AI drafts awaiting Myanmar and Thai Saṅgha review before liturgical or scholarly use. CC BY-SA 4.0.
- **Subject**: `buddhism; pali canon; sutta nipata; metta sutta; theravada; loving-kindness; southeast asia`
- **Language**: `pli; eng; zho; mya; tha` (multiple)

### 8. `sarasvati-wonhyo-daeseung-gisillon-preface`
- **Title**: Wŏnhyo 元曉 — Preface to the Commentary on the Awakening of Faith (T44 no.1844, 3-language)
- **Files**: `translations/wonhyo-prologue/daeseung-gisillon-so-prologue-3lang.md`
- **Description**: Sinosphere-branch first sample. Wŏnhyo's (617–686) preface to the *Daeseung-gisillon-so* 《大乘起信論疏》 (CBETA T44 no.1844, PD by age — 1,300+ years old). Modern Korean and English columns are Sarasvatī AI drafts requiring review by qualified East Asian Buddhologists. CC BY-SA 4.0.
- **Subject**: `buddhism; wonhyo; korean buddhism; awakening of faith; cbeta; sinosphere; east asian buddhism`
- **Language**: `zho; kor; eng` (multiple)

### 9. `sarasvati-full-corpus-v0.9`
- **Title**: Sarasvatī v0.9 — Full Corpus Snapshot (charter + 8-branch samples + manifests)
- **Files**:
  - `sarasvati-v0.9.tar.gz` (built by `upload.sh` immediately before upload; whole repo minus `.git/`, `drafts/`, `.github/`)
  - `manifests/SHA256SUMS`
  - `manifests/SHA256SUMS.v0.9.0-a.ots` (OpenTimestamps proof)
  - `manifests/SHA256SUMS.v0.8.0.ots` (prior stamp, for chain-of-custody)
  - `README.md`
  - `CHANGELOG.md`
  - `ROADMAP.md`
  - `LICENSE`
  - `CALL-FOR-HELP.md`
  - `CONTRIBUTORS.md`
- **Description**: Full snapshot of the Sarasvatī open Buddhist archive at v0.9 (2026-09-13). Contains the 24-language Buddhist-AI Charter, first samples for all 8 branches (India · Sanskrit · Pāli · SE Asia · Silk Road · Chinese · Sinosphere · Tibetan), OpenTimestamps-stamped SHA256 manifest, and top-level project docs. CC BY-SA 4.0.
- **Subject**: `buddhism; open corpus; multilingual; buddhist canon; ai ethics; opentimestamps; snapshot; v0.9`
- **Language**: `multiple`

## Delta from what already lives on GitHub

- IA items 1–8 are **redundant copies** of files already in the GitHub repo — that is the point (mirror layer).
- IA item 9 is the **first tarball snapshot** we publish externally; the SHA256SUMS + OTS proof anchors this exact tree to the Bitcoin blockchain via the existing v0.9.0-a OpenTimestamps stamp. No new cryptographic action is required at upload time.
- No `impl/`, `proposals/`, `announcements/`, `resource-leads/`, `scripts/`, or `.github/` in item 9 — those are internal working documents. If Pan wants them mirrored, it is a one-line change in `upload.sh` (`--include-internal`).

## Post-upload URLs (once live)

| Identifier | URL |
| --- | --- |
| sarasvati-charter-v1.1 | https://archive.org/details/sarasvati-charter-v1.1 |
| sarasvati-dn16-mahaparinibbana-4lang | https://archive.org/details/sarasvati-dn16-mahaparinibbana-4lang |
| sarasvati-ashoka-rock-edict-XII | https://archive.org/details/sarasvati-ashoka-rock-edict-XII |
| sarasvati-prajnaparamita-hridaya | https://archive.org/details/sarasvati-prajnaparamita-hridaya |
| sarasvati-gandhari-dharmapada-khotan-Ia | https://archive.org/details/sarasvati-gandhari-dharmapada-khotan-Ia |
| sarasvati-foyijiao-jing-T389 | https://archive.org/details/sarasvati-foyijiao-jing-T389 |
| sarasvati-karaniya-metta-sutta-Sn1.8 | https://archive.org/details/sarasvati-karaniya-metta-sutta-Sn1.8 |
| sarasvati-wonhyo-daeseung-gisillon-preface | https://archive.org/details/sarasvati-wonhyo-daeseung-gisillon-preface |
| sarasvati-full-corpus-v0.9 | https://archive.org/details/sarasvati-full-corpus-v0.9 |

Each item auto-generates: HTTPS download, torrent, IPFS gateway URL, permanent identifier, `<identifier>_meta.xml` metadata, and machine-readable JSON. Full-text search is indexed within ~24h.
