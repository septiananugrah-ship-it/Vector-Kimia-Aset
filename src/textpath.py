"""Ubah teks menjadi path SVG (outline) memakai font Inter di folder fonts/.

Microstock mewajibkan teks dalam vektor sudah dikonversi menjadi outline,
jadi semua teks dibuat lewat modul ini, bukan elemen <text>.
"""
from functools import lru_cache
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.ttLib import TTFont

FONTS = Path(__file__).parent.parent / "fonts"


@lru_cache(maxsize=None)
def _font(weight):
    f = TTFont(FONTS / f"Inter-{weight}.otf")
    return f, f.getGlyphSet(), f.getBestCmap(), f["head"].unitsPerEm


@lru_cache(maxsize=4096)
def _glyph(weight, ch):
    f, gs, cmap, _ = _font(weight)
    name = cmap.get(ord(ch), ".notdef")
    pen = SVGPathPen(gs)
    gs[name].draw(pen)
    return pen.getCommands(), f["hmtx"][name][0]


def width(s, size, weight="Bold"):
    upm = _font(weight)[3]
    return sum(_glyph(weight, c)[1] for c in s) * size / upm


def text(s, x, y, size, fill, weight="Bold", anchor="middle"):
    """Path SVG untuk teks `s` dengan garis dasar di y. anchor: start|middle|end."""
    upm = _font(weight)[3]
    k = size / upm
    w = width(s, size, weight)
    x0 = x - (w / 2 if anchor == "middle" else w if anchor == "end" else 0)
    parts, adv = [], 0
    for c in s:
        d, a = _glyph(weight, c)
        if d:
            parts.append(f'<path transform="translate({x0 + adv * k:.3f} {y:.3f}) scale({k:.5f} {-k:.5f})" d="{d}"/>')
        adv += a
    return f'<g fill="{fill}" stroke="none">{"".join(parts)}</g>'
