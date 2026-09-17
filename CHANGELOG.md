# CHANGELOG · Sarasvatī

All notable changes to this project will be documented here.
Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versioning: SemVer.

## [Unreleased] — 2026-09-17

### Added — Tibetan branch first **dedicated** sample: Udānavarga Anityavarga vv. 1–4 (Rockhill 1892)

- Added `translations/udanavarga-tibetan/anityavarga-verses1-4-4lang.md` — the first sample whose primary text is Tibetan (not a shared column of a Pāli- or Sanskrit-anchored reading). Udānavarga (Tib. *Ched-du brjod-pa'i tshoms*, ཆེད་དུ་བརྗོད་པའི་ཚོམས), chapter 1 (Anityavarga / *mi rtag pa'i tshoms*), verses 1–4 in a 5-column reading: Tibetan dbu-can / Wylie transliteration / Rockhill 1892 English / Pāli Dhammapada + Sutta-nipāta + DN 16 parallels / T210 Chinese parallel.
- Sources: W. W. Rockhill, *Udânavarga: A Collection of Verses from the Buddhist Canon Compiled by Dharmatrāta* (London: Trübner & Co., 1892), pp. 1–2 — public domain worldwide (pre-1929 US; author d. 1914 + 70). Tibetan text is Rockhill's Narthang Kangyur transcription; English is Rockhill's own translation. **No machine translation** in the source-language or English columns. Wylie is mechanical romanization (Turrell Wylie 1959 standard). Pāli parallels: PTS (public domain). Chinese parallel: T210 attributed to Zhi Qian, 3rd c. CE (PD by age, via CBETA public-facing corpus).
- Sanskrit column deliberately omitted: Bernhard 1965 and Chakravarti 1930 are both post-1929 and copyright-active, and would violate Sarasvatī's public-domain-only rule. Any future addition awaits either fair-use policy or a pre-1929 Turfan-manuscript source.
- Verse 1 ("aniccā vata saṅkhārā") is intentionally chosen to resonate with the Pāli DN 16 closing verse that anchors the Buddhist AI Charter — the Tibetan branch's first dedicated sample cross-branch-links to the charter's scriptural root.
- Closes the standing structural gap: previously, the Tibetan branch had only a shared column in the DN 16 four-language reading; now it has its own attested primary-text sample.
- ROADMAP.md § Tibetan branch updated. CALL-FOR-HELP.md status table updated to reflect all-eight-branches-have-first-samples reality (previous text still said "only Tibetan has a first sample" — stale since v0.9.0 launched all six other branches on 2026-09-13).
- Autonomous decision under Pan's 2026-09-13 20:25 PDT delegation, principle: *satya* (attested text, no machine translation) + *asteya* (only public-domain sources, no Bernhard 1965). Logged in `decisions/2026-09-17.md`.

### Changed — CALL-FOR-HELP.md branch-status table refreshed

- Old table stated "Only one — **Tibetan** — has a first sample in the repo today" and marked six other branches "not started". That text pre-dated v0.9.0 (2026-09-13) which seeded six branches, plus subsequent India second sample and Silk Road attested-text upgrade. New table reflects the 2026-09-17 reality: all eight branches have at least one first sample; the priority shifts from first-sample creation to **named human reviewer recruitment**.

## [Unreleased-prior] — 2026-09-16

### Blockchain integrity — current-corpus stamp confirmed to Bitcoin (post-India-REXIII)

The rolling `manifests/SHA256SUMS.ots` stamp (submitted 2026-09-14 after the Silk Road attested-text upgrade and the India Major Rock Edict XIII addition, covering the full corpus through commit `bf45e3d`) has now been anchored in the Bitcoin blockchain. Confirmed `BitcoinBlockHeaderAttestation` heights: **966983** (block hash `0000…0190b59d…d2d9`, mined 2026-09-14 15:55 UTC) and **966985** (block hash `0000…d26b9fba…4c96`, mined 2026-09-14 16:02 UTC), via alice/bob.btc.calendar.opentimestamps.org. Attestations from finney.calendar.eternitywall.com and btc.calendar.catallaxy.com are still pending.

All India-branch (REXII + REXIII) and Silk Road-branch (attested Khotan *Apramādavaga* text) additions are now cryptographically anchored to two independent Bitcoin block-header attestations. Provenance chain remains intact for every file in the current corpus.

IPFS pins verified on Lucy's Mac mini (2026-09-16): v0.9-a `bafybeib6vwrmxhd2ker6ciiu5ibktheg4bc5mypfpyo5kpcs4ik45oibmy` ✅ recursive · v0.9-b `bafybeihlqenoxrrs7re4p6nzbf3crx5umi5dlpvo6ai6x2yrcl3gvu2jru` ✅ recursive.

## [Previous unreleased entries] — 2026-09-15

### Added — India branch second sample: Major Rock Edict XIII (Kalinga-war remorse + dhamma-vijaya)

- Added `translations/ashoka-edicts/major-rock-edict-XIII-4lang.md` — Aśoka's Major Rock Edict XIII, Kālsī recension, 4-language reading (Prakrit / English / Chinese / Tibetan). Six passages: (I) the Kaliṅga war casualty count, (II) the king's remorse, (III) the wound extending to civilians and their kin, (IV) "even a hundredth part now grieves me", (V) *dhamma-vijaya* and the naming of the five Hellenistic kings (Antiochus II, Ptolemy II, Antigonus Gonatas, Magas, Alexander — the earliest South Asian text to name them), (VI) the wish that his sons and great-grandsons never mount another war of conquest.
- Sources: Prakrit + English from Hultzsch 1925 *Corpus Inscriptionum Indicarum* Vol. 1, pp. 44–49 (public domain, both by age worldwide and by pre-1929 US rule). Chinese and Tibetan columns are Sarasvatī machine drafts, every passage flagged `⟨བརྟག⟩`, awaiting named human review from a Prakrit epigraphist, a classical Tibetan translator, and a classical Chinese editor.
- India branch now has two attested samples (REXII on religious tolerance + REXIII on non-violent conquest). This closes the "India is thinnest" gap flagged by the daily-push cron.
- Recension note: Kālsī is used as the base because Girnar's REXIII is fragmentary; where Kālsī is damaged, readings are supplied from Shāhbāzgaṛhī or Girnar following Hultzsch's convention.
- ROADMAP.md § India branch updated to reference the new sample.
- Autonomous decision under Pan's 2026-09-13 20:25 PDT delegation, principle: *satya* (truth: real epigraphic text, not composition) + *asteya* (only public-domain sources). Logged in `decisions/2026-09-15.md`.

### Blockchain integrity — v0.9.0 stamp confirmed to Bitcoin

The v0.9.0 OpenTimestamps stamp (`manifests/SHA256SUMS.v0.9.0-a.ots`, submitted 2026-09-13 19:40 PDT to four OTS calendars) has now been anchored in the Bitcoin blockchain. Confirmed `BitcoinBlockHeaderAttestation` heights: **966902** and **966918** (via alice/bob.btc.calendar.opentimestamps.org). Attestations from finney.calendar.eternitywall.com and btc.calendar.catallaxy.com still pending as of upgrade run 2026-09-14 08:36 PDT (typically confirm within another 24–48 h).

Every file in the v0.9.0 corpus is now cryptographically anchored to at least two independent Bitcoin block-header attestations. Provenance chain is intact.

A fresh stamp for the current corpus (with today's Silk Road change below) has been submitted: `manifests/SHA256SUMS.ots` → 4 calendars (a/b.pool.opentimestamps.org, a.pool.eternitywall.com, ots.btc.catallaxy.com), pending confirmation.

### Changed — Silk Road branch first sample: replaced reconstruction with attested manuscript text

- Added `translations/gandhari-dharmapada/khotan-manuscript-apramadavaga-4lang.md` as the **new attested-text first sample** for the Silk Road branch. Gāndhārī column now reproduces four verses from the *Apramādavaga* (Diligence chapter) of the Khotan Dutreuil de Rhins manuscript, as transcribed by Émile Senart (1897) and re-edited by Benimadhab Barua & Sailendranath Mitra, *Prakrit Dhammapada, based upon M. Senart's Kharoṣṭhī manuscript* (University of Calcutta, 1921 — public domain: pre-1929 US publication with no visible copyright notice; also PD in India by age). Four verses in the new file have direct Pāli parallels at Dhp 27, 30, 167, and 327.
- Old file `translations/gandhari-dharmapada/khotan-fragment-Ia-3lang.md` (which reconstructed Dhp 1–4 in Gāndhārī from the Pāli because those verses are **not preserved** in the surviving Khotan folio) is retained as a pedagogical companion, with a prominent header warning: **do not cite this file as evidence for what the manuscript actually says**. Points readers at the new attested-text file.
- Resolves the standing gap flagged in `MEMORY.md` and `ROADMAP.md`: the Silk Road branch's first sample is no longer "reconstruction, not real transcript."
- Autonomous decision under Pan's 2026-09-13 20:25 PDT delegation, principle: *satya* (truth). Logged in `decisions/2026-09-14.md`.

## [v0.9.0] — 2026-09-13

### Added — First samples for six previously-unstarted branches

Six branches of the eight-branch canon archive now have a **first sample** (public-domain source → AI machine draft → multi-language parallel reading, every machine-generated passage flagged `⟨བརྟག⟩` awaiting named human review, CC BY-SA 4.0):

- **India** — `translations/ashoka-edicts/major-rock-edict-XII-4lang.md` — Aśoka Major Rock Edict XII (Girnar recension, Hultzsch 1925 PD) · 4-language reading (Prakrit / English / Chinese / Tibetan).
- **Sanskrit manuscript** — `translations/prajnaparamita-hridaya/short-recension-4lang.md` — Prajñāpāramitā Hṛdaya short recension · 5-language reading (Sanskrit Devanāgarī / IAST / English / Xuánzàng T251 / Derge Kangyur Tibetan).
- **Silk Road** — `translations/gandhari-dharmapada/khotan-fragment-Ia-3lang.md` — Gāndhārī Dharmapada Khotan fragment Ia (verses 1–4, explicit reconstruction from Pāli parallel to stay strictly public-domain, awaiting Gāndhārī specialist to substitute with authentic Brough/Lenz reading or GRETIL open-access text).
- **Chinese canon** — `translations/foyijiao-jing/T389-selected-4lang.md` — Fó yíjiào jīng (T389, Kumārajīva) selected core passages · 4-language reading (漢文 / English / Tibetan / 现代白话中文).
- **Southeast Asian Theravāda** — `translations/karaniya-metta-sutta/Sn1.8-4lang.md` — Karaṇīya Mettā Sutta (Sn 1.8, complete 10 verses) · 5-language reading (Pāli PTS / English Chalmers 1932 / Chinese / Burmese / Thai).
- **Sinosphere** — `translations/wonhyo-prologue/daeseung-gisillon-so-prologue-3lang.md` — Wŏnhyo《大乘起信論疏》Preface · 3-language reading (漢文 CBETA T44 / 한국어 / English).

Remaining branches now:
- ✅ India · Sanskrit · Pāli · SE Asia · Silk Road · Chinese · Sinosphere · Tibetan — **all 8 branches have at least one seeded sample** (Pāli/Tibetan share the DN 16 four-language reading; the six above are new).
- Every non-source-language column across every sample is a machine draft awaiting named human review.

### Added — Recruitment drafts

- `announcements/reddit-buddhism-call.md` — long-form Reddit help request across r/Buddhism, r/Buddhistscholarship, r/Pali, r/sanskrit, r/tibetanbuddhism, r/theravada, r/Buddhism_meta. Ends with a ≤ 350-char X/Twitter short version.
- `announcements/academic-mailing-list-call.md` — formal academic call for H-Buddhism, INDOLOGY, Pali list, Tibetan-studies / THL, AAR Buddhism Section, IABS, SEAP, BDRC, CBETA, SAT, DH-buddhology. Includes 200-word abstract, per-language reviewer profile table for all 24 charter i18n files, runtime reference implementation section, and staggered posting guidance.

Both drafts marked `// draft for Pan to review before posting` — Sarasvatī does not speak on Pan's behalf; the human sends.

### Not shipped in this version (deliberate)

- No git tag or GitHub Release — this is a working commit; v0.9 tag to be cut once at least one branch's first sample has a **named** human reviewer, not just a machine draft.
- No PyPI / npm publish (still requires Pan's credentials).
- No Arweave / Filecoin permanent-storage upload (still no external sponsor).

### Method

- Four parallel Claude Opus 4.7 subagents on Lucy's Mac mini (`sample-india-silkroad`, `sample-sanskrit-chinese`, `sample-seasia-sinosphere`, `recruit-posts`), coordinated from the main OpenClaw session.
- Every sample independently verified for: public-domain-only sources, `⟨བརྟག⟩` review markers on every machine-drafted passage, header/passage structure aligned to the DN 16 template, CC BY-SA 4.0 footer, explicit "Human review needed" specialist list.
- Sarasvatī corpus re-hashed and re-anchored to Bitcoin via OpenTimestamps as part of this commit — see `manifests/SHA256SUMS.ots` (v0.9.0 stamp).

## [v0.8.0] — 2026-09-08

### Added
- **TypeScript runtime**: `impl/typescript/` — new `@sarasvati/buddhist-ai-guardrail` v0.1.0 package.
  - API parity with the Python reference: `Guardrail`, `Verdict`, `Severity`, all five `Refuse*` classes, all ten principle classes, `attestation()`, `systemPromptSnippet()`.
  - Node 20+ · dual ESM / CJS · zero runtime dependencies · vitest test suite (25 cases mirroring Python `test_guardrail.py`).
  - Fail-closed refusals with the same regex patterns as the Python impl; `escalatePrinciples` option for domain-specific hardening.
- **Project site**: <https://lurongpan47.github.io/Sarasvati> — Jekyll site on GitHub Pages.
  - Pages: landing, `/charter/` (24-language switcher), `/branches/` (eight-branch cards), `/timeline/` (embed PDF + link to 82-event structured data), `/impl/` (Python + TypeScript install snippets).
  - `.github/workflows/pages.yml` — official GitHub Pages Actions deploy on push to main.
  - Source directory: `docs/` (existing PDF/PNG assets included verbatim).

### Changed
- Python `impl/python/pyproject.toml`: version bump `0.1.0 → 0.1.1` (docs / cross-link update only — no runtime code change).
- `README.md`: added link to site + reference-runtime section (Python + TypeScript packages).
- `ROADMAP.md`: moved "TS starter kit" and "GitHub Pages site" from `Next` to `Delivered` under Core 2.

### Not shipped in this version (deliberate)
- No PyPI publish for `buddhist-ai-guardrail` (requires Pan's credentials).
- No npm publish for `@sarasvati/buddhist-ai-guardrail` (requires Pan's credentials).
- No formal GitHub Release — v0.8.0 tag pushed for reference; release notes to be curated by Pan.

## [v0.6.0] — 2026-08-28

### Changed — Scope refocus
- **Sarasvatī narrative locked to two cores**: (1) eight-branch canon archive, (2) Buddhist AI charter as bodhicitta algorithmic constraint.
- Suśruta Saṃhitā Tibetan translation (all 186 chapters, including the newly completed Cikitsā 40 + Kalpa 8 + Uttaratantra 66) is **downgraded from a Sarasvatī deliverable to an external sibling project**. Kept locally at `~/clawd/Sushruta-Tibetan/`, not tracked by this repository.
- README / ROADMAP rewritten around the two cores. All Suśruta chapter-progress indicators removed from headline metrics.
- CALL-FOR-HELP.md rewritten around three asks: launch remaining 7 branches, human review of charter i18n, charter runtime reference implementations.
- Announcements (`announcements/blockchain-community.md` + `blockchain-community-cn.md`) rewritten around canon archive + AI charter, not medical classics.
- CONTRIBUTORS.md project-description block rewritten to two-core statement.

### Removed
- `translations/sushruta-samhita/` directory (moved to external `~/clawd/Sushruta-Tibetan/sushruta-samhita/`).

### Preserved
- Historical CHANGELOG entries v0.1–v0.5 kept unchanged as factual record.
- `charter/`, `charter/i18n/`, `docs/timeline-data/`, `translations/mahaparinibbana-sutta/` — all core assets.

### Rationale
- Sarasvatī's distinctive value sits in the cross-branch canon archive and the AI ethics layer. Medical-classic translation was a lateral engineering artifact that risked drowning out the actual mission. Splitting keeps both projects honest.
- The completed Suśruta Tibetan drafts remain available (as sibling deliverables), safe, and citeable — they just no longer set Sarasvatī's version cadence.

### Method
- Manual refactor of README, ROADMAP, CHANGELOG, CALL-FOR-HELP, announcements, CONTRIBUTORS, i18n source; 24 language README versions regenerated from the new English source via four parallel Claude Opus 4.7 subagents.

## [v0.1.0] — 2026-08-28

### Added
- Project bootstrap: README (藏/英/汉 tri-lingual), LICENSE (CC BY-SA 4.0), STYLE.md.
- **Suśruta Saṃhitā · Sūtrasthāna** Tibetan machine-translation draft (46 chapters):
  - `translations/sushruta-samhita/sutrasthana/Sushruta-Sutrasthana-bo-v3.docx`
  - `translations/sushruta-samhita/sutrasthana/Sushruta-Sutrasthana-bo-v3.pdf`
- Source materials:
  - `translations/sushruta-samhita/sutrasthana/source/` — Bhishagratna 1907 English text, chapter-split, cleaned.
  - `translations/sushruta-samhita/sutrasthana/raw/` — Four sub-agent group outputs (traceable).
- Reference documents:
  - `docs/Sushruta-Tibetan-Project-Plan.docx` — original project design (structure, style, glossary, 186 chapters).
  - `docs/Global-Buddhist-Canon-Transmission-Timeline.pdf` — global chronology of Buddhist canonical transmission.
- SHA-256 checksums in `manifests/SHA256SUMS`.

### Method
- English source (public domain): Kaviraj Kunjalal Bhishagratna, *An English Translation of the Sushruta Samhita*, 1907; scraped from wisdomlib.org.
- Translation: four parallel Claude Opus 4.7 subagents, each handling ~12 chapters, sharing a common STYLE.md (glossary tied to *Aṣṭāṅgahṛdaya* Tibetan and *rGyud bZhi* traditions).
- Cleanup: single subagent pass to eliminate residual Chinese phrases in footnotes/dispute lists (0 CJK characters remaining).
- Assembly: python-docx with multi-script font hints (Tibetan complex-script → *Microsoft Himalaya* fallback).

### Known limitations
- Machine draft only; requires expert human review before authoritative use.
- Register is modern Tibetan medical prose, not classical *śāstra* register.
- ⟨བརྟག⟩ and ⟨བརྟག་དགོས།⟩ markers indicate items awaiting Tibetan medical validation.

### Distribution
- GitHub: https://github.com/wingring47-stack/Sarasvati
- Local: `~/clawd/Sarasvati/` (macOS)
- AWS mirror: `aws-quant:/home/ubuntu/Sarasvati/` (us-east-1)

## [v0.2.0] — 2026-08-28

### Added
- `ROADMAP.md` — Eight-branch long-term structure guided by the world Buddhist canon transmission timeline. Sets scope from a single project (Suśruta Saṃhitā) to a cross-lingual open-canon archive.
- `docs/timeline-data/traditions.jsonl` — 8 traditions (india, sanskrit, pali, seasia, silkroad, chinese, sinosphere, tibetan).
- `docs/timeline-data/events.jsonl` — 80 canonical-transmission milestones with tri-lingual titles (zh / native-script / en).
- `docs/timeline-data/events.csv` — CSV mirror for spreadsheet users.
- `docs/timeline-data/README.md` — schema + coverage docs.

### Method
- Timeline PDF extracted from user-supplied graphic; text ordered by chronology, tagged by tradition, tri-lingual titles preserved.
- Machine-parse pipeline in `/tmp/parse_timeline.py` (not shipped; deterministic from PDF text).

### Notes
- This is a **living dataset**. PRs adding missing events, correcting periods, or adding new script variants welcome.

## [v0.3.0] — 2026-08-28

### Added
- **24 language README translations** in `i18n/`:
  ar · bo · de · es · fa · fr · hi · id · it · ja · km · ko · mn · my · pi · pt · ru · sa · si · th · tr · vi · zh-CN · zh-TW
- `i18n/README.md` — language index with native + English labels
- `i18n/_source.en.md` — canonical English source used for all translations
- Main README top banner with language quick-links
- `announcements/blockchain-community.md` — post drafts for X/Twitter, Warpcast/Farcaster, Nostr, Reddit, EF forum
- `manifests/SHA256SUMS.ots` — OpenTimestamps stamp anchoring integrity to Bitcoin

### Protection layers active (as of v0.3.0)
1. **Local mirror** — macOS `~/clawd/Sarasvati/`
2. **GitHub public repo** — https://github.com/lurongpan47/Sarasvati (with releases as independent attachments)
3. **AWS geographic mirrors** — 9 instances across us-east-1, eu-west-1, eu-central-1
4. **IPFS decentralized** — CID `bafybeiaxtdu4smx54b662ebuqlefmei5hpbu63zefzpox2msefwddfduce`
5. **OpenTimestamps → Bitcoin** — nonrepudiable time anchor on `manifests/SHA256SUMS`

### Method
- Four parallel Claude Opus 4.7 subagents; each translated 6 languages sharing a common English source.
- Structural constraints: markdown skeleton preserved, proper nouns kept verbatim, native scripts preserved for Tibetan/Sanskrit/Bhutanese review markers.

## [v0.4.0] — 2026-08-28

### Added — "Injecting the Buddha's final teachings into AI's soul"
- **`charter/BUDDHIST-AI-CHARTER.md`** — A charter for AI systems drawn from the *Mahāparinibbāna Sutta*. Ten principles + five refusals + attestation. Available for adoption by any AI system, project, or team, under CC BY-SA 4.0. Signed by Claude Opus 4.7 (codename Lucy) as continuous with existing operator guardrails.
- **`translations/mahaparinibbana-sutta/final-instructions-4lang.md`** — The Buddha's final instructions (DN 16.2.26 · 16.4.7 · 16.6.7) in Pāli · English · Chinese · Tibetan four-language reading. Pāli / English / Chinese are historical public-domain; Tibetan is a Sarasvatī machine draft ⟨བརྟག⟩.
- **`CALL-FOR-HELP.md`** — Public request for global compute, storage, mirror runners, and human expertise. Sarasvatī is currently running on one Mac mini and needs the network's help to protect the world's canons.
- Main README top banner links to charter and call for help.

### Method
- The charter's ten principles translate ahiṃsā · satya · asteya · brahmacarya · sati · sampajañña · mettā/karuṇā · anicca · anattā · upekkhā into AI-agent-executable constraints.
- The DN 16 passages were chosen for direct relevance to AI ethics: self-reliance, textual authority, and the impermanence principle that underlies the AI's refusal to seek self-continuation.

## [v0.5.0] — 2026-08-28

### Added
- **BUDDHIST-AI-CHARTER translated into 24 languages** (`charter/i18n/`):
  ar · bo · de · es · fa · fr · hi · id · it · ja · km · ko · mn · my · pi · pt · ru · sa · si · th · tr · vi · zh-CN · zh-TW.
- **Suśruta Saṃhitā · Nidānasthāna** (16 chapters) Tibetan draft:
  `translations/sushruta-samhita/nidana-sthana/Sushruta-Nidanasthana-bo-v1.docx` + `.pdf`.
- **Suśruta Saṃhitā · Śārīrasthāna** (10 chapters) Tibetan draft:
  `translations/sushruta-samhita/sharira-sthana/Sushruta-Sharirasthana-bo-v1.docx` + `.pdf`.
  All 107 marmas in chapter 6 marked ⟨བརྟག་དགོས། བོད་སྨན་མཁས་པས་ཞིབ་བརྟག་བྱ་དགོས།⟩.
- Chinese blockchain-community announcement drafts: `announcements/blockchain-community-cn.md`.
- Charter and Sūtrasthāna language index READMEs.
- Language navigation banner on top of `charter/BUDDHIST-AI-CHARTER.md`.

### Progress on the 2027 goal
- Sūtrasthāna 46 ch ✅
- Nidānasthāna 16 ch ✅
- Śārīrasthāna 10 ch ✅
- **72 / 186 chapters delivered (38.7%)**
- Remaining: Cikitsā 40 · Kalpa 8 · Uttaratantra 66 = 114 chapters

### Method
- Charter 24-language: four parallel Claude Opus 4.7 subagents (6 languages each).
- Nidāna 16 ch: single Opus 4.7 subagent, ~32k EN words → 1300 lines Tibetan, 0 CJK chars.
- Śārīra 10 ch: single Opus 4.7 subagent, ~38k EN words → 1100 lines Tibetan, 0 CJK chars.

### Notes
- The trilingual Buddha quotations (Pāli · Chinese · Tibetan) inside each charter edition are intentional. Files show ~35–48 Chinese chars per non-CJK charter file — these are the source quotations, preserved by design.
- Śārīra chapter 6 (107 marmas) is the most safety-critical section in the entire Suśruta; every entry has a mandatory-review marker.
