# Sanskrit manuscript lineage (`sanskrit`) · Weekly candidate proposal · 2026-10-19 (second cycle, week 3)

**Branch selected**: `sanskrit` — third in the rotation's second cycle (Pāli 10-05 → Chinese 10-12 → Sanskrit 10-19). The 08-31 proposal named Bhadracarī (preferred) / Vajracchedikā-Gilgit / Hṛdaya; only the Hṛdaya was built (v0.9, English a machine draft). This week takes the Vajracchedikā — not the Gilgit MS but **Müller's 1881 editio princeps**, because it is the one Sanskrit edition of the text with a **public-domain English by the same editor read from a leaf**, so for the first time in this branch *both* the source and the English columns are attested, and Kumārajīva's T235 adds an attested third.

## Candidates

### A. **Vajracchedikā §§ 1–2 — Müller 1881 pp. 19–20 + SBE XLIX 1894 pp. 111–113 + T235 Taishō 8.748c16–749a04** *(preferred — built this session)*
- **Sanskrit**: *Buddhist Texts from Japan* (Anecdota Oxoniensia, Aryan I.1), Oxford 1881 — IA `p1anecdotaoxonie01oxfouoft`, files `_0029`/`_0030` = pp. 19–20, 2259 × 2924 px; title, invocation, § 1 whole (11 lines + `‖१‖`), § 2 whole (p. 19 ll. 12–14 + p. 20 ll. 1–14 + `‖२‖`), apparatus notes p. 19 ¹–⁶ and p. 20 ¹–⁴, read at 1.7×–6×.
- **English (PD)**: *Buddhist Mahâyâna Texts* (SBE XLIX part II), Oxford 1894, pp. 111–113 — IA `sacredbooksoftheeastvol49_202002`, files `_0362`–`_0364`, 5224 × 6977 px; §§ I–II with notes 1–4 (p. 111), 1–5 (p. 112), 1 (p. 113).
- **Chinese (PD)**: Taishō vol. 8 p. 748 register c + p. 749 register a — IA `taisho-tripitaka` 第008冊 leaves `_0747`/`_0748`; c16–c29, a01–a04; foot ㉕–㉘.
- **Targets**: IAST (derived), 现代汉语 + བོད་ཡིག drafts ⟨བརྟག⟩ (Derge *rdo rje gcod pa* Toh. 16 not opened).

### B. **Bhadracarīpraṇidhāna** — the 08-31 preferred candidate, still unbuilt
- Watanabe 1912 (Leipzig diss., PD) for the Sanskrit; no PD English found that can be read from a leaf (Izumi 1930 is Japan-PD but US status unclear) — English would be a Sarasvatī draft. Deferred until a PD English surfaces or the branch accepts a draft English.

### C. **Vajracchedikā § 3 onward** — the natural continuation of A
- Müller p. 20 l. 15 – p. 21 (file `_0031`, fetched) · SBE p. 113 `III.` – 114 · T235 749a05–a12. Same leaves, same pipeline.

## Public-domain evidence
Müller (1823–1900): both the 1881 edition and the 1894 translation PD worldwide. Kumārajīva (402 CE) PD by age; the Taishō editorial layer as in the T389 / T784 files (Japan PD since 2016; typography uncopyrightable). The IA copy of SBE XLIX is additionally labelled CC0 by its uploader.

## Resource estimate (A)
- Build: 22 `image` calls (3 overviews, 9 Sanskrit strips/zooms, 7 SBE crops, 6 Taishō strips/foot thirds — two calls failed on paths); ~20 k tokens for the IAST, two draft columns and the file.
- Human review: a Sanskritist for three apparatus akṣaras (p. 19 fn ³ ⁴ ⁵) and the orthography; a reader of SBE XLIX for the italics and note keys; a Sinologist for the kaeriten, the c24 ring and ㉕'s seam; a Tibetan reader with Derge open.
- Bitcoin timestamp + 9 mirrors: existing pipeline.

## One-line summary for WhatsApp
Sanskrit week 2 — **Vajracchedikā §§ 1–2: Müller 1881 pp. 19–20 (IA files _0029/_0030) + SBE XLIX pp. 111–113 + T235 Taishō 748c–749a — three attested columns**; alternates Bhadracarī (B, no PD English) and § 3 (C). Built directly under the 09-21 auto-approve rule.
