"""Shared type, colour and SVG helpers for the profile artwork."""
from pathlib import Path
from html import escape
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parents[1]
FONTS = ROOT / 'assets/fonts'

def load_font(name, weight=500):
    font = TTFont(FONTS / name)
    if 'fvar' in font:
        axes = {a.axisTag: a.defaultValue for a in font['fvar'].axes}
        if 'wght' in axes:
            axes['wght'] = weight
        font = instantiateVariableFont(font, axes)
    return font

SANS = load_font('instrument-sans.woff2', 550)
SERIF = load_font('instrument-serif-italic.woff2')

def lettering(text, font, size, x, y, color, tracking=0):
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    scale = size / font['head'].unitsPerEm
    parts = []
    for character in text:
        glyph = glyphs[cmap[ord(character)]]
        pen = SVGPathPen(glyphs)
        glyph.draw(pen)
        parts.append(f'<path d="{pen.getCommands()}" transform="translate({x:.3f} {y}) scale({scale:.6f} {-scale:.6f})"/>')
        x += glyph.width * scale + tracking
    return f'<g fill="{color}" aria-hidden="true">{"".join(parts)}</g>'

THEMES = {
    'light': {'paper': '#f6f4ef', 'ink': '#202127', 'muted': '#5e5a60', 'red': '#c83d29', 'rule': '#d3cec5'},
    'dark': {'paper': '#202127', 'ink': '#f6f4ef', 'muted': '#c6c1b8', 'red': '#ed7865', 'rule': '#4a484c'},
}


def text(value, x, y, size=22, color='#202127', serif=False, tracking=0):
    return lettering(value, SERIF if serif else SANS, size, x, y, color, tracking)

def document(title, desc, body, c, height=360, css='', defs=''):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="960" height="{height}" viewBox="0 0 960 {height}" role="img" aria-labelledby="title desc">
<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>
<defs>{defs}</defs><style>
.floating{{transform-box:fill-box;transform-origin:center}}
@media(prefers-reduced-motion:no-preference){{
.floating{{animation:float 6s ease-in-out infinite}}
.flow{{stroke-dasharray:8 22;animation:flow 3s linear infinite}}
.spark{{transform-box:fill-box;transform-origin:center;animation:spark 3s ease-in-out infinite}}
}}
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-7px)}}}}
@keyframes flow{{to{{stroke-dashoffset:-120}}}}
@keyframes spark{{0%,100%{{opacity:.5;transform:scale(.8)}}50%{{opacity:1;transform:scale(1.15)}}}}
{css}</style><rect width="960" height="{height}" rx="8" fill="{c['paper']}"/>{body}</svg>'''

def save(name, theme, svg):
    p=ROOT/f'assets/{name}-{theme}.svg';p.write_text(svg);print(f'{p.name}: {len(svg.encode()):,} bytes')
