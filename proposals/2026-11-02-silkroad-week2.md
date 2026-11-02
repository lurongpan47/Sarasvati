# Silk Road (`silkroad`) · Weekly candidate proposal · 2026-11-02 (week 2)

**Branch selected**: Silk Road / Central Asia — week 2 of the branch rotation. Week 1 (2026-09-14) proposed Khotanese Vajracchedikā (Konow 1916) but was never built; existing silkroad translation files are all Gāndhārī (Khotan Dharmapada). This proposal reopens the Iranian-language slot with Konow 1916 as **preferred** and two alternates that have not yet been proposed in any form.

## Candidates (pick one; all three are drop-in for a 4- or 5-language reading page)

### A. **Khotanese Vajracchedikā, opening sections** *(preferred — scan-first build)*
- Source: Sten Konow (1916), *The Vajracchedikā in the Old Khotanese Version of Eastern Turkestan*, in A. F. R. Hoernle (ed.), *Manuscript Remains of Buddhist Literature Found in Eastern Turkestan*, vol. I pp. 214–288. Oxford: Clarendon. **Konow †1948, PD worldwide**; the Hoernle volume is pre-1929 (US rule).
- Internet Archive: `manuscriptremain00hoer` (whole volume) — leaves to be read in-session.
- Text: Vajracchedikā Nidāna / § 1 (preamble + Subhūti's question) in Old Khotanese with Konow's English facing-page translation and his critical notes.
- Reading page: **Old Khotanese (Konow Roman transcription) / English (Konow 1916) / Sanskrit Müller 1881 §§ 1–2 (already attested in sanskrit-week2 build 2026-10-19) / Chinese Kumārajīva T235 (same build) / 现代汉语 draft / བོད་ཡིག draft**.
- Why: closes the Iranian-language gap in the archive; the Sanskrit / Chinese columns can be lifted *attested* from the 2026-10-19 Vajracchedikā §§ 1–2 file (which Pan has already pushed and mirrored), so this build adds only the Khotanese + Konow English columns scan-first — a one-leaf, two-column add that produces a genuine 6-language parallel reading on a text already in Sarasvatī.

### B. **Tocharian B *Udānavarga* fragment (Berlin Turfan)**
- Source: Emil Sieg & Wilhelm Siegling (1921), *Tocharische Sprachreste I. Die Texte. A. Transcription.* Berlin: de Gruyter. **Sieg †1951, Siegling †1946, PD outside US; US pre-1929 rule covers it.**
- Internet Archive: `tocharischesprac0000sieg` (if present) or de Gruyter reprint.
- Text: 10–15 verses from the Berlin Turfan Udānavarga, with Sanskrit parallels from Rockhill 1892 (PD) and Pāli Dhammapada counterparts.

### C. **Khotanese *Book of Zambasta* ch. 5 (pāramitās)**
- Source: Ernst Leumann (1933–36, posthumous, ed. Manu Leumann), *Das nordarische (sakische) Lehrgedicht des Buddhismus*, Abhandlungen für die Kunde des Morgenlandes XX, Leipzig. **Leumann †1931, PD worldwide.**
- ~50 verses on the six perfections. Indigenous Khotanese composition, not translation — fills the "Central Asian Buddhist voice" gap.

## Public-domain evidence
Konow †1948, Sieg †1951, Siegling †1946, Leumann †1931 — all editors dead ≥ 70 years. The Hoernle 1916, Sieg–Siegling 1921 and Leumann 1933–36 imprints are pre-1929 or published posthumously under PD authorship; US and Berne Convention life+70 both satisfied. The Emmerick 1968 edition of Zambasta is intentionally **not** used (still in copyright until 2071).

## Resource estimate (candidate A, this session's build)
- Scan-first Khotanese + Konow English columns: ~20 image calls, 30–45 min subagent time (Konow prints facing pages; one leaf of IA scan = both columns).
- Sanskrit / Chinese columns lifted attested from `translations/vajracchedika/sections-1-2-4lang.md` (2026-10-19 build, already pushed).
- 现代汉语 + བོད་ཡིག columns: Sarasvatī drafts marked ⟨བརྟག⟩, awaiting named human review.
- Human review: Iranist (Khotanese typography, Konow transliteration conventions, Harold Bailey corrections if needed). Reviewer-recruitment is already drafted at `RESOURCE-QUEUE.md`; SOAS Iranian Studies and Harvard Sanskrit Department are the two best fits.
- Pipeline: regenerate `manifests/SHA256SUMS` → fresh `.ots` stamp → commit → push → rsync to 9 AWS mirrors → CHANGELOG + decisions entry.

## One-line summary for WhatsApp
Silk Road week 2 — proposing **Khotanese Vajracchedikā (Konow 1916, PD)** as preferred, with Tocharian B *Udānavarga* (Sieg–Siegling 1921) and *Book of Zambasta* ch. 5 (Leumann 1933) as alternates. **Building A this session under the 2026-09-21 auto-approve rule.**
