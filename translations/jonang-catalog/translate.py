#!/usr/bin/env python3
"""
Jonang catalog translator (Tibetan → Chinese).
Resumable: writes pages_zh/pXXX.md as it goes.
Model: Claude Opus 4.7 via Anthropic SDK.
Glossary: enforces Jonang-lineage proper nouns from glossary.json.
"""
import os, sys, json, time, pathlib, re, hashlib
from anthropic import Anthropic

ROOT = pathlib.Path(__file__).parent
PAGES_TIB = ROOT / 'pages_tib'
PAGES_ZH  = ROOT / 'pages_zh'
PAGES_ZH.mkdir(exist_ok=True)
STATE = ROOT / 'state.json'
GLOSS = ROOT / 'glossary.json'
LOG   = ROOT / 'translate.log'

MODEL = os.getenv('TRANSLATE_MODEL', 'claude-fable-5-1')  # Fable 5.1 default ($10/$50/M, 1M ctx)
# Pricing per million tokens (input, output) — update when model changes
PRICE = {
    'claude-fable-5-1':   (10,  50),
    'claude-opus-4-7':    (15,  75),
}.get(MODEL, (15, 75))

client = Anthropic()

def load_json(p, default):
    if p.exists():
        return json.loads(p.read_text())
    return default

def save_json(p, obj):
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=2))

glossary = load_json(GLOSS, {})
state    = load_json(STATE, {'done': [], 'failed': [], 'cost_in': 0, 'cost_out': 0})

def log(msg):
    line = f'[{time.strftime("%H:%M:%S")}] {msg}'
    print(line, flush=True)
    with open(LOG, 'a') as f:
        f.write(line + '\n')

SYSTEM = """You are a Tibetan Buddhist text translator specializing in the Jonang (ཇོ་ནང་ · 觉囊) lineage.
Your task: translate a page from the catalog (དཀར་ཆག) of the Jonang Great Treasury of Knowledge (ཇོ་ནང་རིག་མཛོད་ཆེན་མོ) from Classical Tibetan into Simplified Chinese.

STRICT OUTPUT FORMAT per entry:
  <chinese translation of title> …… <page number from source>

RULES:
1. This is a catalog/table of contents. Each line is a title + leader dots + page number. Preserve the page numbers EXACTLY.
2. Author names and lineage holders: use the standard Chinese transliteration + Sanskrit/Tibetan in parentheses when first introduced.
   Known mapping (follow strictly if present):
     ཇོ་ནང་ = 觉囊
     དོལ་པོ་པ་ཤེས་རབ་རྒྱལ་མཚན་ = 多波巴·喜饶坚赞 (Dolpopa Śes-rab rGyal-mtshan)
     ཏཱ་ར་ནཱ་ཐ་ = 多罗那他 (Tāranātha)
     ཡུ་མོ་མི་བསྐྱོད་རྡོ་རྗེ་ = 域摩·弥觉多杰 (Yumo Mi-bskyod rDo-rje)
     དུས་ཀྱི་འཁོར་ལོ་ = 时轮 (Kālacakra)
     གཞན་སྟོང་ = 他空 (Śentong / Zhentong)
     རྗེ་བཙུན་ = 至尊
     བླ་མ་ = 上师
     རྒྱལ་བ་ = 胜者 / 佛
     ཆོས་རྗེ་ = 法主
     ཀུན་མཁྱེན་ = 遍知
     གྲུབ་ཆེན་ = 大成就者
     གྲུབ་ཐོབ་ = 成就者
     སྐུ་ཞབས་ = 尊者
     གསུང་འབུམ་ = 文集 (collected works)
     གསུང་ = 教法 / 教言
     དཀར་ཆག་ = 目录
     རྣམ་ཐར་ = 传记
     མདོ་ = 经
     རྒྱུད་ = 续
     འགྲེལ་པ་ = 释论
     ཊཱིཀ་ = 疏
     བསྟན་བཅོས་ = 论
3. For Sanskrit-origin names (eg དྷརྨེ་ཤྭ་ར), give Chinese + Sanskrit: 达磨伊什瓦拉 (Dharmeśvara).
4. If a line is unclear or garbled, mark it ⟨བརྟག⟩ at the end — this signals pending human review.
5. The source has some corrupted dot runs (���). Treat them as leader dots and output …… instead.
6. Page-number markers at the top of the page like `.39.` are page numbers of the TOC itself — preserve as `【第 39 页】` on its own line.
7. Section headings (lines without page numbers that act as grouping titles) — translate and bold with **…**.
8. OUTPUT ONLY the translation. No commentary, no "Here is the translation", no preamble.
"""

def translate_page(tib_text, page_num):
    """Translate one page. Returns (zh_text, in_tokens, out_tokens)."""
    user = f"""Page {page_num} of 449 from the Jonang catalog. Source Tibetan text follows between the markers.

=====SOURCE=====
{tib_text}
=====END=====

Produce the Chinese translation now, following all format rules."""

    msg = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        system=SYSTEM,
        messages=[{'role': 'user', 'content': user}],
    )
    # Pick the first text block (skip ThinkingBlocks that Fable/reasoning models emit first)
    zh = ''
    for block in msg.content:
        if getattr(block, 'type', None) == 'text':
            zh = block.text.strip()
            break
    if not zh:
        raise RuntimeError(f'no text block in response: {[getattr(b, "type", type(b).__name__) for b in msg.content]}')
    return zh, msg.usage.input_tokens, msg.usage.output_tokens

def main():
    pages = sorted(PAGES_TIB.glob('p*.txt'))
    log(f'=== translate run: model={MODEL}, pages={len(pages)}, done={len(state["done"])} ===')
    for p in pages:
        n = int(p.stem[1:])
        out = PAGES_ZH / f'p{n:03d}.md'
        if out.exists() and n in state['done']:
            continue
        tib = p.read_text().strip()
        if not tib:
            out.write_text(f'【第 {n} 页】\n\n（空白页）\n')
            state['done'].append(n)
            save_json(STATE, state)
            log(f'page {n}: empty, skipped')
            continue
        for attempt in range(3):
            try:
                t0 = time.time()
                zh, ti, to = translate_page(tib, n)
                dt = time.time() - t0
                state['cost_in']  += ti
                state['cost_out'] += to
                header = f'<!-- source page {n}, {len(tib)} chars Tibetan, {ti}in/{to}out tokens, {dt:.1f}s -->\n\n'
                out.write_text(header + zh + '\n')
                state['done'].append(n)
                save_json(STATE, state)
                in_cost  = state['cost_in']  * PRICE[0] / 1_000_000
                out_cost = state['cost_out'] * PRICE[1] / 1_000_000
                log(f'page {n:3d}/449 ok ({len(tib)}→{len(zh)} chars, {dt:.1f}s, ${in_cost+out_cost:.2f} total)')
                break
            except Exception as e:
                log(f'page {n} attempt {attempt+1} failed: {e}')
                time.sleep(10 * (attempt + 1))
        else:
            state['failed'].append(n)
            save_json(STATE, state)
            log(f'page {n}: GAVE UP after 3 attempts')
    log(f'=== run complete. done={len(state["done"])} failed={len(state["failed"])} ===')

if __name__ == '__main__':
    main()
