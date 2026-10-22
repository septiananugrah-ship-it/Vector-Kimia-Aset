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
    k, m = 6, 64  # piksel per satuan, margin (cukup lebar untuk ikon yang berpusat di 0, mis. atom 4-5 kulit)
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


def outlinify(body):
    """Varian outline (siap diwarnai): semua isi jadi putih, garis jadi gelap.

    - Teks (grup dari textpath) tetap gelap agar terbaca.
    - Garis berlapis bertanda data-ring (garis tebal berwarna di atas garis
      gelap) dijadikan putih, sehingga tampil sebagai tabung berongga.
    """
    import re
    body = re.sub(r'<g fill="#[0-9A-Fa-f]{6}" stroke="none"><path transform',
                  '<g fill="#1E2A3A" stroke="none" data-text="1"><path transform', body)
    body = re.sub(r'stroke="#[0-9A-Fa-f]{6}"([^>]*data-ring)', r'stroke="#FFFFFF"\1', body)

    def sub(m):
        attr, col = m.group(1), m.group(2).upper()
        if attr == "fill":
            return 'fill="#FFFFFF"'
        return f'stroke="{"#FFFFFF" if col == "#FFFFFF" else "#1E2A3A"}"'
    body = re.sub(r'(fill|stroke)="(#[0-9A-Fa-f]{6})"', sub, body)
    return body.replace('<g fill="#FFFFFF" stroke="none" data-text="1">', '<g fill="#1E2A3A" stroke="none">')


def chalkify(body, bg, chalk="#F2F1EA"):
    """Gaya kapur di papan tulis: isi sewarna papan, garis dan teks berwarna kapur."""
    import re
    body = re.sub(r'<g fill="#[0-9A-Fa-f]{6}" stroke="none"><path transform',
                  '<g fill="@CHALK@" stroke="none"><path transform', body)

    def sub(m):
        attr = m.group(1)
        return f'{attr}="{bg if attr == "fill" else chalk}"'
    body = re.sub(r'(fill|stroke)="(#[0-9A-Fa-f]{6})"', sub, body)
    body = re.sub(r'stroke="#[0-9A-Fa-f]{6}"([^>]*data-ring)', f'stroke="{bg}"\\1', body)
    return body.replace("@CHALK@", chalk)


def doodlify(body):
    """Gaya doodle/sketsa: outline dengan garis kedua yang sedikit bergeser seperti coretan tangan."""
    import re
    base = outlinify(body)
    sketch = re.sub(r'fill="#[0-9A-Fa-f]{6}"', 'fill="none"', base)
    sketch = re.sub(r'<g fill="none" stroke="none"><path transform', '<g fill="none" stroke="none" display="none"><path transform', sketch)
    return (base + '<g transform="translate(1.3 .9) rotate(2.2 32 32)" stroke-width="1.1">'
            + sketch.replace('stroke-width="', 'data-sw="') + "</g>")
