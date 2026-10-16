---
layout: page
title: "Free Translation · 免费翻译 · རིན་མེད་ཡིག་སྒྱུར"
permalink: /translate/
description: >-
  A free Buddhist-text translation tool, offered by DeerPress.ai in dāna to the Sangha.
  Integrated into Sarasvatī so researchers, practitioners, and scholars worldwide can
  translate sūtras, śāstras, and primary sources across 30+ languages — including Tibetan,
  Sanskrit, Pāli, Classical Chinese, and modern languages — without cost or signup.
---

<style>
  .dharma-note {
    background: #f8f4e8;
    border-left: 4px solid #c9a04a;
    padding: 1rem 1.25rem;
    margin: 1.5rem 0;
    border-radius: 4px;
    font-size: 0.95rem;
  }
  .dharma-note p { margin: 0.4rem 0; }
  .translate-iframe-wrap {
    position: relative;
    width: 100%;
    margin: 2rem 0;
    border: 1px solid #e5e5e5;
    border-radius: 8px;
    overflow: hidden;
    background: #fff;
    box-shadow: 0 2px 12px rgba(0,0,0,0.06);
  }
  .translate-iframe-wrap iframe {
    width: 100%;
    height: 1400px;
    border: 0;
    display: block;
  }
  @media (max-width: 768px) {
    .translate-iframe-wrap iframe { height: 1800px; }
  }
  .translate-cta-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin: 1rem 0 1.5rem;
    font-size: 0.9rem;
  }
  .translate-cta-row a {
    padding: 0.5rem 1rem;
    background: #2a5885;
    color: #fff;
    text-decoration: none;
    border-radius: 4px;
    font-weight: 500;
  }
  .translate-cta-row a.secondary {
    background: #fff;
    color: #2a5885;
    border: 1px solid #2a5885;
  }
</style>

# Free Translation · 免费翻译 · རིན་མེད་ཡིག་སྒྱུར

**A gift to the Sangha.** Translate Buddhist texts between **30+ languages** — Tibetan,
Sanskrit, Pāli, Classical Chinese, Japanese, Korean, Mongolian, Thai, Burmese, Khmer,
Hindi, Tamil, English, French, German, Spanish, Russian, Arabic, Hebrew, and more.
No signup, no cost. Terminology trained for sūtras, śāstras, commentarial literature,
and primary scholarly sources.

<div class="dharma-note">
  <p><strong>Dāna statement.</strong> This tool is operated by
  <a href="https://deerpress.ai" target="_blank" rel="noopener">DeerPress.ai</a>
  and offered without charge to Buddhists and Buddhist studies scholars worldwide.
  Translations are AI first-drafts — accuracy for terminology is strong, but
  <em>any passage prepared for publication, ritual, or citation must be reviewed by a
  qualified human translator</em>.
  Sarasvatī embeds this tool as a convenience; we do not store, log, or transmit
  the text you translate.</p>
  <p><strong>供养三宝。</strong>此工具由
  <a href="https://deerpress.ai" target="_blank" rel="noopener">DeerPress.ai</a>
  免费提供，供全世界佛教徒及佛学研究者使用。AI 为初稿，正式出版、仪轨或引用前请由合格译师校订。</p>
</div>

<div class="translate-cta-row">
  <a href="https://deerpress.ai/free" target="_blank" rel="noopener">Open in new tab ↗</a>
  <a href="https://deerpress.ai/about/" class="secondary" target="_blank" rel="noopener">About DeerPress</a>
  <a href="https://deerpress.ai/privacy-policy/" class="secondary" target="_blank" rel="noopener">Privacy Policy</a>
</div>

<div class="translate-iframe-wrap">
  <iframe
    src="https://deerpress.ai/free"
    title="DeerPress.ai Free Buddhist Translation"
    loading="lazy"
    allow="clipboard-read; clipboard-write"
    sandbox="allow-forms allow-scripts allow-same-origin allow-popups allow-downloads"
  ></iframe>
</div>

## What this translator does well

- **Buddhist terminology**: handles standard glossary (Bodhisattva / 菩薩 / བྱང་ཆུབ་སེམས་དཔའ་, Dharma / 法 / ཆོས་, Saṅgha / 僧 / དགེ་འདུན་) with scholarly convention
- **Classical languages**: Tibetan (classical and modern), Sanskrit (Devanāgarī and romanized), Pāli, Classical Chinese 文言文
- **Scanned documents**: PDF and DOCX upload supports OCR, including historical scans and traditional block-print editions
- **Modern languages**: 11 European, 9 South and Southeast Asian, 5 East Asian, 3 Middle Eastern languages for diffusion

## What it does *not* do (yet)

- No manuscript variant adjudication — gives you one translation, not a critical apparatus
- No automatic citation generation — you'll still need to cite the source edition yourself
- Not a substitute for a trained lotsāwa, pandit, or professor — treat every output as a **first draft requiring human review**

## For Sarasvatī contributors

If you use this tool while preparing translations for the
[eight-branch canon archive]({{ '/' | relative_url }}#mission),
please add your name and the specific text to
[`CONTRIBUTORS.md`](https://github.com/lurongpan47/Sarasvati/blob/main/CONTRIBUTORS.md)
with the reviewer scope marked clearly (what you drafted vs. what you reviewed vs. what
remains AI-generated). The archive's integrity depends on this transparency —
no passage is ever labeled "attested" without a named human sign-off.

---

<small>
Tool availability monitored weekly by Sarasvatī CI; last status at
<a href="https://github.com/lurongpan47/Sarasvati/blob/main/manifests/translate-health.json">
manifests/translate-health.json</a>.
Report issues to
<a href="mailto:info@aidd.one">info@aidd.one</a>
(DeerPress team) or open a Sarasvatī
<a href="https://github.com/lurongpan47/Sarasvati/issues">GitHub issue</a>.
</small>
