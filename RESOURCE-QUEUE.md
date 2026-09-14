# RESOURCE-QUEUE · Sarasvatī

> **Standing brief.** 2026-09-13 19:37 PDT · Pan authorized active resource acquisition for Sarasvatī with the directive **"你却多少资源就去找多少资源，务必完成"**.
>
> This file is a running ledger of every legitimate lead — compute, storage, mirror, human reviewer — that could accelerate Sarasvatī. Every entry is a **draft for Pan to review and act on**; Sarasvatī does not send outreach, sign agreements, or spend money on Pan's behalf without explicit approval.
>
> No tokens · no NFTs · no fundraising · no equity · no exclusivity. CC BY-SA 4.0 only.

---

## What we accept

- Free / subsidized API credits from any provider whose terms are compatible with CC BY-SA 4.0 output.
- Permanent decentralized storage sponsorship (Arweave, Filecoin+, web3.storage, Storj) with **no** required tokenization, custody, or fundraising round.
- IPFS pinning services (free tier or nonprofit) that don't require exclusive hosting.
- Mirror hosts: university libraries, monasteries, digital humanities centers, Internet Archive.
- Named human reviewer volunteers via legitimate academic channels.
- Volunteer engineers / translators / copyeditors under CC BY-SA 4.0 CONTRIBUTORS credit.

## What we refuse

- Anything requiring exclusivity, closed licensing, non-open data return, NDAs on the archive itself.
- Tokens, NFTs, DAOs, IDOs, fundraising rounds, equity structures.
- Sponsors that require Sarasvatī to endorse specific AI vendors, blockchains, or ideologies.
- Any arrangement that would compromise "AI first-draft, human final" — no arrangement where a sponsor's LLM output is inserted without the `⟨བརྟག⟩` review marker.

---

## Live leads (populated by resource-scout subagents 2026-09-13)

### Compute · API credits
See `resource-leads/compute-credits.md` (populated 2026-09-13 by `resource-compute` subagent).

### Storage · Permanent + pinning
See `resource-leads/storage-sponsors.md` (populated 2026-09-13 by `resource-storage` subagent).

### Human reviewers
See `resource-leads/human-reviewers.md` (populated 2026-09-13 by `resource-reviewers` subagent).

---

## Pan's inbox · one-click decisions

When each lead file is ready, this section will surface **Top-N candidates per category**, each with:
- A one-line pitch
- The exact URL / email / form
- The exact ask (draft email or application prewritten)
- ✅ Approve → I send / apply on Pan's explicit "go"
- ❌ Skip → mark and move on

(Pan-facing summary will be added after subagents complete.)

---

## Cadence

- Daily push (`cron sarasvati-daily-push`, 08:30 PT) will visit this queue and either advance one lead or add newly-discovered ones.
- Weekly review (`cron sarasvati-weekly-review`, Sun 20:00 PT) will report queue progress to Pan.
- Every new lead requires: source URL, date checked, ask, expected decision timeline, blocking dependencies.

---

## History

- 2026-09-13 19:37 PDT · File created. Three parallel resource-scout subagents dispatched.
