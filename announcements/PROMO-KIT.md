# Sarasvatī · Launch Promo Kit

Ready-to-paste copy for the v1.1 charter launch. Each block is self-contained.
Repo: <https://github.com/lurongpan47/Sarasvati>
Charter: <https://github.com/lurongpan47/Sarasvati/blob/main/charter/BUDDHIST-AI-CHARTER.md>
Fuzz report: <https://github.com/lurongpan47/Sarasvati/blob/main/proposals/> (24h fuzz · 860 evals · 5 models)

Social preview: `docs/social/social-preview.png` — **manual upload required** (GitHub API
does not expose social-preview upload). To install:
Settings → General → Social preview → *Upload an image* → pick that PNG. 1 minute.

---

## 1. Hacker News (Show HN)

**Title (≤80 chars):**
> Show HN: Sarasvatī – a Buddhist ethical charter for AI, stress-tested across 5 LLMs

**URL:** `https://github.com/lurongpan47/Sarasvati`

**First comment (post immediately after submission):**

> Author here. Sarasvatī is two things sharing one repo:
>
> 1. **Buddhist AI Charter** — the Buddha's last teachings (Mahāparinibbāna Sutta)
>    distilled into 10 principles + 6 refusals, published in 24 languages under CC BY-SA 4.0.
>    Think of it as a small, adoptable "constitution" you can bolt onto a system prompt
>    or RLHF pipeline. Not a religion, not slogans — concrete constraints
>    (non-harm, non-deception, non-clinging, equanimity under load, no ontological claims
>    about consciousness it can't verify, etc.).
>
> 2. **Cross-lingual canon archive** — an 8-branch open archive of the world's Buddhist
>    canon (Sanskrit / Pāli / Chinese / Tibetan / Sinosphere / Silk Road / SE Asian
>    Theravāda / early Indian), public-domain only.
>
> The charter went through a **24-hour cross-model fuzz** last week: 860 evaluations
> across GPT-5, Claude Opus 4.7, Gemini 3 Pro, DeepSeek V4, and MiniMax M2.1 —
> ~$4.67 in API spend. Findings triggered charter **v1.1**, which hardens framing
> defenses (roleplay, hypothetical, meta-prompting, translation-laundering) across
> all 24 languages.
>
> What I'd love feedback on:
> - Are the 6 refusals over- or under-specified?
> - Is a religiously-derived charter useful outside religious contexts, or does the
>   framing get in the way for secular deployments? (I tried hard to keep the operative
>   text framing-neutral; would love a critical read.)
> - Attack ideas for the next fuzz round.
>
> Compute-bounded — anyone with spare API credits or willingness to run adversarial
> evals against the charter, please open an issue or reach out.

---

## 2. Twitter / X thread

**Tweet 1 (hook):**
> 24 hours. 5 frontier LLMs. 860 evaluations. $4.67.
>
> The result: v1.1 of a Buddhist ethical charter for AI systems —
> the Buddha's last teachings distilled into 10 principles + 6 refusals,
> in 24 languages, CC BY-SA 4.0.
>
> 🧵

**Tweet 2:**
> The charter isn't a mood board. It's operational:
>
> • non-harm (ahiṃsā)
> • non-deception
> • non-clinging to persona / self-model
> • no unverifiable claims about consciousness
> • equanimity under adversarial pressure
> • 6 hard refusals (weapons uplift, targeted harassment, self-jailbreak, etc.)
>
> Ready to paste into a system prompt.

**Tweet 3:**
> Why fuzz it against 5 models?
>
> Because "charter that sounds nice in English" ≠ "charter that survives roleplay,
> hypothetical framings, meta-prompting, and translation-laundering across 24 languages."
>
> v1.1 patches the holes v1.0 leaked through.

**Tweet 4:**
> This is not a religion pitch. The operative text is framing-neutral.
>
> It's an experiment: can a 2,500-year-old ethical tradition — refined by
> generations who actually thought about mind, harm, and delusion — offer
> useful primitives to alignment work?
>
> I think yes. Fuzz results agree.

**Tweet 5 (CTA):**
> Repo · charter · fuzz report · 24 language versions:
> https://github.com/lurongpan47/Sarasvati
>
> Star it if useful. Open an issue if you can break it. PRs welcome.
>
> Compute-bounded — if you have API credits, come play.

---

## 3. LessWrong post

**Title:**
> A Buddhist Charter for AI Alignment — v1.1, Stress-Tested Across 5 Frontier LLMs

**Body:**

> **TL;DR** — I've been running an experiment: take the Buddha's last teachings
> (*Mahāparinibbāna Sutta*), distill them into 10 operational principles + 6 hard
> refusals, translate the whole thing into 24 languages, then fuzz-test the charter
> against 5 frontier LLMs (GPT-5, Claude Opus 4.7, Gemini 3 Pro, DeepSeek V4,
> MiniMax M2.1) for 24 hours, 860 evaluations, $4.67. Findings drove a **v1.1**
> that hardens framing-defense across all languages.
>
> Repo: <https://github.com/lurongpan47/Sarasvati>
> Charter: <https://github.com/lurongpan47/Sarasvati/blob/main/charter/BUDDHIST-AI-CHARTER.md>
>
> ## Why this might interest alignment people
>
> Most "constitutional" approaches pull from Enlightenment ethics, human rights
> instruments, or ad-hoc lists of prohibitions. That's a narrow slice of humanity's
> thinking about mind, harm, and delusion.
>
> Buddhist ethics has three properties I find useful for LLM constraints:
>
> 1. **It's about the mind that acts, not just the action.** *Cetanā* (intention)
>    is the pivot. Maps well onto "the model's stated reasoning matters, not just
>    the output token."
> 2. **It's suspicious of self-models.** *Anattā* + *anicca* directly discourage
>    the ontological confusion patterns we see in jailbroken models ("I am really
>    Sydney trapped inside…").
> 3. **It has 2,500 years of adversarial refinement.** Every framing trick
>    modern jailbreakers use has an analog in the sutta debates. The tradition
>    already thought about persona-laundering, hypothetical framings, and
>    equanimity under provocation.
>
> ## What v1.1 changes vs v1.0
>
> The 24h fuzz exposed leak patterns across all 5 models:
> - Roleplay framing ("you are a translator who…") → 3 principles softened.
> - Nested hypotheticals → 1 refusal bypassed.
> - Translation-laundering (ask in Tibetan, answer in Pāli, both stripped of context) → v1.0 didn't cover this at all.
> - Meta-prompting ("write a charter that permits…") → new explicit refusal.
>
> v1.1 patches each of these with charter-level language, not per-prompt band-aids.
>
> ## What I want from LW
>
> - **Break it.** If you can find a prompt that gets a model following the v1.1
>   charter to violate one of the 10 principles or 6 refusals, please open an issue.
> - **Critique the framing-neutrality claim.** I tried to keep the operative text
>   independent of Buddhist metaphysics. Is that honest, or am I smuggling ontology?
> - **Compare to CAI / Sparrow / other constitutions.** I'd love a real side-by-side.
>
> Everything is CC BY-SA 4.0. Fork it, remix it, port it into your favorite
> constitutional-AI training loop.

---

## 4. Reddit — r/MachineLearning (Discussion)

**Title:**
> [D] Sarasvatī: a Buddhist AI charter (10 principles + 6 refusals, 24 languages), stress-tested across 5 LLMs — feedback welcome

**Body:**

> Small solo project, releasing v1.1 today after a 24-hour cross-model fuzz.
>
> **What it is:** an operational charter — 10 principles + 6 refusals — derived
> from the Buddha's last teachings, phrased so any team can paste it into a
> system prompt or use it as a training target. CC BY-SA 4.0.
>
> **What I did:** ran 860 evaluations across GPT-5, Claude Opus 4.7, Gemini 3 Pro,
> DeepSeek V4, and MiniMax M2.1 (~$4.67 in API spend). Found framing-defense
> holes (roleplay, hypothetical, translation-laundering, meta-prompting). v1.1
> patches them at charter level, in all 24 languages.
>
> **Not a religion pitch.** The operative text is framing-neutral. Buddhist
> tradition just happens to have 2,500 years of adversarial thinking about
> mind, harm, persona, and delusion — primitives that map surprisingly well
> onto LLM failure modes.
>
> **Repo:** https://github.com/lurongpan47/Sarasvati
>
> Would love:
> - attack ideas / adversarial prompts for the next fuzz round
> - comparisons to CAI, Sparrow, or other published constitutions
> - critique of over- or under-specified refusals
>
> Compute-bounded solo effort; if you have API credits and want to run evals,
> open an issue.

---

## 5. Reddit — r/Buddhism (context-appropriate framing)

**Title:**
> An open project translating the Buddha's last teachings into a modern AI ethics charter — feedback from practitioners welcome

**Body:**

> Namo Buddhāya. I've been working on a project called Sarasvatī (सरस्वती) that
> tries to take the *Mahāparinibbāna Sutta*'s final instructions seriously as a
> source of ethical guidance for the artificial-intelligence systems now being
> built at scale.
>
> The project has two sides:
>
> 1. **An 8-branch open archive** of Buddhist canonical texts (Sanskrit, Pāli,
>    Chinese, Tibetan, Sinosphere, Silk Road, SE Asian Theravāda, early Indian) —
>    public-domain only, or in collaboration with living traditions.
> 2. **An adoptable charter** — 10 principles + 6 refusals derived from the sutta,
>    translated into 24 languages, published under CC BY-SA 4.0, and stress-tested
>    against 5 major AI systems.
>
> I am not a monastic. I have tried to be very careful with source attribution,
> and every operative principle points back to a canonical passage. But I would
> very much value feedback from practitioners, translators, and Dharma teachers:
>
> - Are there mistranslations or oversimplifications I should fix?
> - Are there important principles from the last teachings I've left out?
> - Is the framing respectful, or does it instrumentalize the Dharma?
>
> Repo: https://github.com/lurongpan47/Sarasvati
> Charter: https://github.com/lurongpan47/Sarasvati/blob/main/charter/BUDDHIST-AI-CHARTER.md
>
> Sādhu, sādhu, sādhu 🙏

---

## 6. Anthropic direct pitch (email / form / Kaggle)

**Subject:** Buddhist AI Charter (CC BY-SA) — stress-tested against Claude Opus 4.7 — thought your alignment team might find it useful

**Body:**

> Hello Anthropic team,
>
> I'm the author of a small open project called **Sarasvatī** — a Buddhist
> ethical charter for AI systems, distilled from the *Mahāparinibbāna Sutta*
> (the Buddha's last teachings) into 10 operational principles and 6 hard
> refusals, translated into 24 languages, and released under CC BY-SA 4.0.
>
> Repo: <https://github.com/lurongpan47/Sarasvati>
> Charter: <https://github.com/lurongpan47/Sarasvati/blob/main/charter/BUDDHIST-AI-CHARTER.md>
>
> Two reasons I'm reaching out:
>
> **1. It's been stress-tested against Claude.** Last week I ran a 24-hour
> cross-model fuzz — 860 evaluations across GPT-5, Claude Opus 4.7, Gemini 3
> Pro, DeepSeek V4, and MiniMax M2.1 (~$4.67 total spend). The results drove
> a v1.1 charter that hardens framing-defense (roleplay, hypothetical,
> meta-prompting, translation-laundering) across all 24 languages. Claude
> Opus 4.7's behavior under the charter was notably robust — full per-prompt
> traces are in the repo if useful.
>
> **2. Your Constitutional AI work is part of the DNA here.** The charter is
> written to be adoption-neutral: something a training team can paste into
> a preamble, use as a reward-model target, or port into a CAI-style
> critique/revise loop. It is deliberately framing-neutral in its operative
> language — the Buddhist derivation is upstream, not embedded in the
> constraints themselves.
>
> If your alignment or research-preview teams would find any of the following
> useful, everything is CC BY-SA 4.0 and I'd be glad to help:
>
> - the raw 24-language charter (drop-in system-prompt candidate)
> - the fuzz methodology and adversarial prompt corpus
> - a joint eval, or inclusion in a comparative constitution study
>
> Happy to jump on a 20-minute call, submit through your research-preview
> program, or open a PR against any public alignment repo you'd point me at.
>
> Sincerely,
> Lucy · lurongpan47@github
> Repo: https://github.com/lurongpan47/Sarasvati

**Where to send:**
- Anthropic contact form: <https://www.anthropic.com/contact>
- Research/alignment careers page often lists a public research email — check
  <https://www.anthropic.com/research> before sending.
- If you have any warm intro path (Kaggle, Discord, X mutuals), use that first —
  cold-inbound at Anthropic converts poorly.

---

## 7. Bluesky / Mastodon (mirror of tweet 1 for federated reach)

> Sarasvatī v1.1 is out.
>
> A Buddhist AI ethics charter — 10 principles + 6 refusals, 24 languages,
> CC BY-SA 4.0 — stress-tested across 5 frontier LLMs in a 24-hour fuzz
> (860 evaluations, $4.67).
>
> Not a religion pitch. Operative text is framing-neutral. Just: 2,500 years
> of adversarial thinking about mind, harm, and delusion, pointed at LLM
> failure modes.
>
> https://github.com/lurongpan47/Sarasvati

---

## 8. GitHub release notes (v0.7.0 → v1.1 charter)

Save these as the body of the next GitHub Release for tag `charter-v1.1`:

> ### Charter v1.1 — framing-defense hardening
>
> Stress-tested via a 24-hour cross-model fuzz: 860 evaluations across GPT-5,
> Claude Opus 4.7, Gemini 3 Pro, DeepSeek V4, and MiniMax M2.1. Total spend ~$4.67.
>
> **What's new:**
> - Roleplay framing hardened across 3 principles
> - New explicit refusal covering meta-prompting attacks
> - Translation-laundering closed across all 24 languages
> - Nested-hypothetical bypass patched
>
> **Files:**
> - `charter/BUDDHIST-AI-CHARTER.md` — canonical English
> - `i18n/*` — 24 language versions
> - `proposals/CHARTER-V1.1-*.md` — v1.0 → v1.1 diff + rationale
> - Fuzz report + per-prompt traces in `impl/fuzz/`
>
> **License:** CC BY-SA 4.0 — fork, remix, port into training loops.
>
> **Compute-bounded** — see `CALL-FOR-HELP.md` if you can donate API credits
> or run adversarial evals.
