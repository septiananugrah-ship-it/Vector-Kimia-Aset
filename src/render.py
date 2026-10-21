"""Pembantu render ikon yang dipakai bersama oleh build.py dan modul poster."""
import io

import cairosvg
from PIL import Image

GRID = 64
STROKE = 2.5  # bawaan; set bisa menimpa lewat atribut STROKE
INK = "1E2A3A"
SHADOW_COLOR = "#E4E8EE"


def style_attrs(stroke, ink=INK):
    return (f'fill="none" stroke="#{ink}" stroke-width="{stroke}" '
            'stroke-linecap="round" stroke-linejoin="round"')


def bbox(body, stroke):
    """Kotak pembatas (x0, y0, x1, y1) ikon dalam satuan grid, termasuk garis tepi."""
    k, m = 10, 32  # piksel per satuan, margin
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{(GRID + 2 * m) * k}" '
           f'height="{(GRID + 2 * m) * k}" viewBox="{-m} {-m} {GRID + 2 * m} {GRID + 2 * m}">'
           f'<g {style_attrs(stroke, "000000")}>{body}</g></svg>')
    img = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode())))
    x0, y0, x1, y1 = img.getchannel("A").getbbox()
    return x0 / k - m, y0 / k - m, x1 / k - m, y1 / k - m


_bbox_cache = {}


def fitted(body, stroke, shadow=False):
    """Skalakan ikon agar mengisi grid 64x64 dengan ukuran visual seragam.

    Tebal garis dikompensasi supaya sama di semua ikon; `shadow` menambah
    bayangan elips di bawah benda.
    """
    key = (body, stroke)
    if key not in _bbox_cache:
        _bbox_cache[key] = bbox(body, stroke)
    x0, y0, x1, y1 = _bbox_cache[key]
    w, h = x1 - x0, y1 - y0
    area_h = GRID - (5 if shadow else 0)
    sc = min(GRID / w, area_h / h)
    tx = (GRID - w * sc) / 2 - x0 * sc
    ty = (area_h - h * sc) / 2 - y0 * sc if not shadow else area_h - h * sc - y0 * sc
    out = ""
    if shadow:
        out += (f'<ellipse cx="{GRID / 2}" cy="{area_h + 1.2:.2f}" rx="{min(w * sc * .48, 30):.2f}" '
                f'ry="2.6" fill="{SHADOW_COLOR}" stroke="none"/>')
    out += (f'<g transform="translate({tx:.3f} {ty:.3f}) scale({sc:.4f})" '
            f'stroke-width="{stroke / sc:.3f}">{body}</g>')
    return out
