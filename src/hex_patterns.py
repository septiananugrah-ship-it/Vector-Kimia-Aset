"""Pola seamless sarang lebah / cincin benzena bergaya garis.

Ubin berisi kisi heksagon; heksagon tertentu diberi lingkaran (benzena),
isian lembut, atau titik atom di sudut. Pilihan acak ditentukan oleh posisi
heksagon modulo ukuran ubin, sehingga salinan di tepi identik dan ubin
menyambung tanpa sambungan.
"""
import math
import random

SET_ID = "hexagon-patterns"

VARIANTS = [
    ("#FFFFFF", "#C9D6E3", "#3FB6C4", "#E3F4F6", "light blue on white"),
    ("#1E2A3A", "#34506D", "#3FB6C4", "#24364B", "teal on dark navy"),
    ("#EAF7F2", "#B7DCCD", "#3E9E68", "#D3EFE2", "mint green"),
    ("#FFF4E6", "#F2C9A0", "#E07B1F", "#FDE6CC", "warm orange on cream"),
]


def hexagon(cx, cy, s):
    pts = [(cx + s * math.cos(math.radians(60 * i)), cy + s * math.sin(math.radians(60 * i))) for i in range(6)]
    return pts, "M" + "L".join(f"{x:.2f} {y:.2f}" for x, y in pts) + "z"


def pattern(bg, line, accent, soft, seed, s=20, n=8, m=5):
    W, H = 1.5 * s * n, math.sqrt(3) * s * m
    # latar sedikit melebihi ubin supaya piksel tepi raster tidak tembus putih
    out = [f'<rect x="-1" y="-1" width="{W + 2:.2f}" height="{H + 2:.2f}" fill="{bg}"/>',
           f'<clipPath id="t"><rect width="{W:.2f}" height="{H:.2f}"/></clipPath><g clip-path="url(#t)">']
    fills, lines, marks = [], [], []
    for c in range(-1, n + 1):
        for r in range(-1, m + 1):
            cx = 1.5 * s * c
            cy = math.sqrt(3) * s * (r + (0.5 if c % 2 else 0))
            pts, d = hexagon(cx, cy, s)
            rnd = random.Random(f"{seed}-{c % n}-{r % m}")
            roll = rnd.random()
            if roll < .14:
                fills.append(f'<path d="{d}" fill="{soft}"/>')
            lines.append(d)
            if .14 <= roll < .30:
                marks.append(f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{s * .55:.2f}" fill="none" '
                             f'stroke="{accent}" stroke-width="1.8"/>')
            elif .30 <= roll < .40:
                for x, y in pts[::2]:
                    marks.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="2.6" fill="{accent}"/>')
    out += fills
    out.append(f'<path d="{"".join(lines)}" fill="none" stroke="{line}" stroke-width="1.4" '
               'stroke-linejoin="round"/>')
    out += marks
    out.append("</g>")
    return W, H, "".join(out)


def assets():
    out = []
    for i, (bg, line, accent, soft, mood) in enumerate(VARIANTS, start=1):
        W, H, inner = pattern(bg, line, accent, soft, seed=i)
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * 10:.0f}" height="{H * 10:.0f}" '
               f'viewBox="0 0 {W:.3f} {H:.3f}">\n{inner}\n</svg>\n')
        out.append(dict(
            name=f"{SET_ID}-{i:02d}", svg=svg, size=4000, png=False,
            title=f"Hexagon honeycomb and benzene ring seamless pattern, {mood} chemistry vector background",
            keywords=["seamless pattern", "hexagon", "honeycomb", "benzene", "benzene ring", "molecule",
                      "chemistry", "chemical", "science", "pattern", "background", "seamless", "repeat",
                      "geometric", "texture", "wallpaper", "abstract", "grid", "line", "network",
                      "molecular structure", "organic chemistry", "biology", "medical", "pharmacy",
                      "technology", "education", "print", "fabric", "textile", "wrapping paper", "backdrop",
                      "vector", "illustration", "minimal", "modern", "tile", "cells"]))
    return [(SET_ID, out)]
