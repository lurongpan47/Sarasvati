#!/usr/bin/env python3
"""Build Chinese-only PDF of the Jonang catalog translation."""
import pathlib, re, textwrap
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor, black
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle,
)

ROOT = pathlib.Path(__file__).parent
# Try common CJK fonts on macOS
FONT = None
for candidate in [
    '/Users/lucy/Library/Fonts/NotoSansSC[wght].ttf',
    '/opt/homebrew/Caskroom/font-noto-sans-sc/latest/NotoSansSC[wght].ttf',
]:
    if pathlib.Path(candidate).exists():
        try:
            pdfmetrics.registerFont(TTFont('CJK', candidate))
            FONT = 'CJK'
            print(f'Using font: {candidate}')
            break
        except Exception as e:
            print(f'  skip {candidate}: {e}')

if not FONT:
    # Fallback: download/install wqy
    raise SystemExit('No CJK font found. Install one or adjust the list.')

# Styles
styles = getSampleStyleSheet()
cjk_title = ParagraphStyle(
    'CJKTitle', parent=styles['Title'],
    fontName=FONT, fontSize=22, leading=28, textColor=HexColor('#8B2500'),
    alignment=1, spaceAfter=12,
)
cjk_subtitle = ParagraphStyle(
    'CJKSubtitle', parent=styles['Normal'],
    fontName=FONT, fontSize=12, leading=16, alignment=1,
    textColor=HexColor('#555555'), spaceAfter=6,
)
cjk_h1 = ParagraphStyle(
    'CJKH1', fontName=FONT, fontSize=15, leading=22, textColor=HexColor('#8B2500'),
    spaceBefore=10, spaceAfter=4,
)
cjk_h2 = ParagraphStyle(
    'CJKH2', fontName=FONT, fontSize=12, leading=18, textColor=HexColor('#333333'),
    spaceBefore=4,
)
cjk_body = ParagraphStyle(
    'CJKBody', fontName=FONT, fontSize=10, leading=15, textColor=black,
)
cjk_page_marker = ParagraphStyle(
    'CJKPageMarker', fontName=FONT, fontSize=9, leading=12,
    textColor=HexColor('#999999'), spaceBefore=8, spaceAfter=2, alignment=1,
)
cjk_note = ParagraphStyle(
    'CJKNote', fontName=FONT, fontSize=8, leading=12,
    textColor=HexColor('#888888'), alignment=2,
)

# Load translated markdown
raw = (ROOT / 'jonang-catalog_zh.md').read_text()

doc = SimpleDocTemplate(
    str(ROOT / 'jonang-catalog_zh.pdf'),
    pagesize=A4,
    leftMargin=20*mm, rightMargin=20*mm,
    topMargin=20*mm, bottomMargin=20*mm,
    title='觉囊大宝藏目录（汉译草稿）',
    author='Sarasvatī · AI first-draft',
)

story = []

# Cover
story.append(Spacer(1, 60*mm))
story.append(Paragraph('觉囊·大智慧藏总目录', cjk_title))
story.append(Paragraph('ཇོ་ནང་རིག་མཛོད་ཆེན་མོའི་དཀར་ཆག', cjk_subtitle))
story.append(Spacer(1, 10*mm))
story.append(Paragraph('汉译草稿 · AI 一稿 · 待复核', cjk_subtitle))
story.append(Spacer(1, 60*mm))
cover_info = [
    ['原本', '觉囊文丛 · 第 216 册'],
    ['页数', '449 页藏文原本'],
    ['字符数', '约 99 万字藏文'],
    ['翻译', 'Claude Opus 4.7'],
    ['日期', '2026-10-17'],
    ['许可', 'CC BY-SA 4.0'],
    ['状态', 'AI 一稿 ⟨བརྟག⟩ · 所有译文待具名藏传学者复核'],
    ['归属', 'Sarasvatī 第八支（藏传佛典）档案项目'],
]
t = Table(cover_info, colWidths=[30*mm, 110*mm])
t.setStyle(TableStyle([
    ('FONT', (0,0), (-1,-1), FONT, 10),
    ('TEXTCOLOR', (0,0), (0,-1), HexColor('#8B2500')),
    ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ('TOPPADDING', (0,0), (-1,-1), 2),
    ('LEFTPADDING', (0,0), (-1,-1), 4),
]))
story.append(t)
story.append(PageBreak())

# Body: process each page
sections = re.split(r'<!-- ============ Source PDF page (\d+) ============ -->', raw)
# sections[0] = header (frontmatter), then pairs (num, content)
frontmatter = sections[0]
pairs = list(zip(sections[1::2], sections[2::2]))

def esc(s):
    return (s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;'))

for pnum, content in pairs:
    # Add thin source-page marker at bottom (we'll append after)
    text = content.strip()
    if not text or '（空白页）' in text:
        story.append(Paragraph(f'— 源 PDF 第 {pnum} 页（空白）—', cjk_page_marker))
        continue

    for raw_line in text.split('\n'):
        line = raw_line.rstrip()
        if not line:
            story.append(Spacer(1, 2))
            continue
        # Handle markdown-ish headings
        if line.startswith('**') and line.endswith('**'):
            # Section header
            inner = line.strip('*').strip()
            story.append(Paragraph(esc(inner), cjk_h1))
        elif line.startswith('【') and '】' in line and len(line) < 20:
            # Internal page number marker like 【第 88 页】
            story.append(Paragraph(esc(line), cjk_page_marker))
        else:
            # Convert **bold** inline
            # Replace **x** with <b>x</b>
            html = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', esc(line))
            # Preserve indentation (full-width spaces)
            html = html.replace(' ', '&nbsp;')
            story.append(Paragraph(html, cjk_body))
    # Thin source-page footer
    story.append(Paragraph(f'— 源 PDF p.{pnum} —', cjk_note))
    story.append(Spacer(1, 4))

doc.build(story)
import os
size = os.path.getsize(ROOT / 'jonang-catalog_zh.pdf')
print(f'built jonang-catalog_zh.pdf: {size:,} bytes')
