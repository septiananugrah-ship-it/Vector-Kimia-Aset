"""Latar presentasi/banner bertema kimia (16:9) dengan ruang kosong untuk teks.

Hiasan (kisi heksagon, molekul, atom, ikon alat lab, rumus) ditempatkan di
tepi; bagian lain dibiarkan polos sebagai copy space. Tanpa transparansi:
warna "pudar" dibuat dengan mencampur warna hiasan ke warna latar.
"""
import math
import random

import atoms
import icons_lab2
import icons_lab_flat
import molecules
from render import GRID, fitted, style_attrs
from textpath import formula, text, width

SET_ID = "chemistry-backgrounds"
W, H = 1920, 1080


def mix(a, b, f):
    """Campur warna a ke b sebanyak f (0 = a, 1 = b)."""
    ca = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    cb = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * f):02X}" for x, y in zip(ca, cb))


def hex_field(bg, line, region, s=46, seed=1, keep=lambda x, y: 1.0):
    """Kisi heksagon di region (x0, y0, x1, y1); keep(x, y) = peluang heksagon digambar."""
    rnd = random.Random(seed)
    x0, y0, x1, y1 = region
    paths, accents = [], []
    c = 0
    x = x0
    while x < x1 + s:
        y = y0 + (s * math.sqrt(3) / 2 if c % 2 else 0)
        while y < y1 + s:
            if rnd.random() < keep(x, y):
                pts = [(x + s * math.cos(math.radians(60 * k)), y + s * math.sin(math.radians(60 * k))) for k in range(6)]
                paths.append("M" + "L".join(f"{px:.1f} {py:.1f}" for px, py in pts) + "z")
                if rnd.random() < .12:
                    accents.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{s * .52:.1f}"/>')
            y += s * math.sqrt(3)
        x += s * 1.5
        c += 1
    return (f'<path d="{"".join(paths)}" fill="none" stroke="{line}" stroke-width="2.4" stroke-linejoin="round"/>'
            f'<g fill="none" stroke="{line}" stroke-width="2.4">{"".join(accents)}</g>')


def place(body, stroke, x, y, size, rot=0):
    return (f'<g transform="translate({x:.1f} {y:.1f}) rotate({rot:.1f}) scale({size / GRID:.4f}) '
            f'translate({-GRID / 2} {-GRID / 2})"><g {style_attrs(stroke)}>{fitted(body, stroke)}</g></g>')


def scatter(items, region, n, size_rng, seed, rot=25, min_gap=1.05):
    """Sebar ikon acak tanpa saling tumpuk di region."""
    rnd = random.Random(seed)
    x0, y0, x1, y1 = region
    placed, out = [], []
    tries = 0
    while len(placed) < n and tries < 4000:
        tries += 1
        s = rnd.uniform(*size_rng)
        x, y = rnd.uniform(x0 + s / 2, x1 - s / 2), rnd.uniform(y0 + s / 2, y1 - s / 2)
        if any(math.hypot(x - px, y - py) < (s + ps) / 2 * min_gap for px, py, ps in placed):
            continue
        placed.append((x, y, s))
        body, stroke = items[len(placed) % len(items)]
        out.append(place(body, stroke, x, y, s, rnd.uniform(-rot, rot)))
    return "".join(out)


def _items(*mods):
    return [(ic["body"], m.STROKE) for m in mods for ic in m.ICONS]


def bg_hex_molecules(bg, line_f, seed):
    """Kisi heksagon memudar ke kiri + molekul berwarna di sisi kanan."""
    line = mix(bg, "#3FB6C4", line_f)
    hexes = hex_field(bg, line, (W * .45, -60, W + 60, H + 60), seed=seed,
                      keep=lambda x, y: max(0, min(1, (x - W * .45) / (W * .4))))
    mols = scatter(_items(molecules), (W * .58, 30, W - 30, H - 30), 8, (190, 290), seed)
    return hexes + mols


def bg_atoms_corners(bg, seed):
    line = mix(bg, "#FFFFFF", .10)
    rnd = random.Random(seed)
    out = []
    for cx, cy, r in ((W - 120, 140, 420), (140, H - 100, 330)):
        for k in range(3):
            out.append(f'<ellipse cx="{cx}" cy="{cy}" rx="{r}" ry="{r * .38:.0f}" fill="none" stroke="{line}" '
                       f'stroke-width="3" transform="rotate({k * 60 + rnd.uniform(-8, 8):.1f} {cx} {cy})"/>')
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r * .1:.0f}" fill="{line}"/>')
    return "".join(out) + scatter(_items(atoms), (W * .6, 40, W - 40, H - 40), 5, (230, 330), seed, rot=0)


def bg_lab_border(bg, seed, region):
    return scatter(_items(icons_lab_flat, icons_lab2), region, 12, (150, 210), seed, min_gap=1.0)


def bg_formulas(bg, seed):
    col = mix(bg, "#FFFFFF", .09)
    rnd = random.Random(seed)
    words = ["H2O", "CO2", "NaCl", "CH4", "O2", "NH3", "H2SO4", "C6H12O6", "HCl", "NaOH", "C2H5OH", "Fe2O3",
             "CaCO3", "N2", "KMnO4", "H2O2", "Cu", "Au", "pH 7", "E = mc²"]
    out, boxes = [], []
    tries = 0
    while len(out) < 22 and tries < 3000:
        tries += 1
        w_ = rnd.choice(words)
        size = rnd.uniform(30, 64)
        tw = width(w_, size, "SemiBold")
        x, y = rnd.uniform(W * .5 + tw / 2, W - 40 - tw / 2), rnd.uniform(70, H - 30)
        box = (x - tw / 2 - 14, y - size - 10, x + tw / 2 + 14, y + 14)
        if any(not (box[2] < b[0] or box[0] > b[2] or box[3] < b[1] or box[1] > b[3]) for b in boxes):
            continue
        boxes.append(box)
        out.append(formula(w_, x, y, size, col, "SemiBold"))
    hexes = hex_field(bg, mix(bg, "#3FB6C4", .22), (W * .62, -60, W + 60, H + 60), s=70, seed=seed,
                      keep=lambda x, y: .55)
    return "".join(out) + hexes


def bg_element_tiles(bg, seed):
    rnd = random.Random(seed)
    els = [("H", 1), ("He", 2), ("C", 6), ("N", 7), ("O", 8), ("Na", 11), ("Mg", 12), ("Cl", 17), ("Ca", 20),
           ("Fe", 26), ("Cu", 29), ("Zn", 30), ("Ag", 47), ("Au", 79), ("Hg", 80), ("U", 92)]
    cols = ["#FF9E8A", "#FFC98A", "#FFE38A", "#B9E28C", "#8FD9C4", "#8ACBEF", "#A9B8F5", "#C3A6F2"]
    out, placed = [], []
    while len(placed) < 11:
        s = rnd.uniform(110, 160)
        x, y = rnd.uniform(W * .6, W - s - 30), rnd.uniform(30, H - s - 30)
        if any(abs(x - px) < (s + ps) / 2 + 30 and abs(y - py) < (s + ps) / 2 + 30 for px, py, ps in placed):
            continue
        placed.append((x, y, s))
        sym, z = els[len(placed) % len(els)]
        c = rnd.choice(cols)
        rot = rnd.uniform(-12, 12)
        out.append(f'<g transform="rotate({rot:.1f} {x + s / 2:.1f} {y + s / 2:.1f})">'
                   f'<rect x="{x:.1f}" y="{y:.1f}" width="{s:.1f}" height="{s:.1f}" rx="{s * .1:.1f}" fill="{c}" '
                   f'stroke="#1E2A3A" stroke-width="3"/>'
                   + text(str(z), x + s * .12, y + s * .22, s * .14, "#1E2A3A", "SemiBold", "start")
                   + text(sym, x + s / 2, y + s * .66, s * .42, "#1E2A3A") + "</g>")
    return "".join(out)


VARIANTS = [
    ("hex-molecules-navy", "#16213A", lambda: bg_hex_molecules("#16213A", .22, 1), "dark navy with hexagon grid and molecules"),
    ("hex-molecules-white", "#FFFFFF", lambda: bg_hex_molecules("#FFFFFF", .28, 2), "white with hexagon grid and molecules"),
    ("hex-molecules-teal", "#0F3B47", lambda: bg_hex_molecules("#0F3B47", .30, 3), "deep teal with hexagon grid and molecules"),
    ("atoms-purple", "#251B45", lambda: bg_atoms_corners("#251B45", 4), "purple with atom orbits"),
    ("atoms-navy", "#16213A", lambda: bg_atoms_corners("#16213A", 5), "dark navy with atom orbits"),
    ("lab-icons-lightblue", "#EAF5FB",
     lambda: bg_lab_border("#EAF5FB", 6, (W * .52, 20, W - 20, H - 20)), "light blue with laboratory equipment"),
    ("lab-icons-cream", "#FFF6E8",
     lambda: bg_lab_border("#FFF6E8", 7, (W * .52, 20, W - 20, H - 20)), "cream with laboratory equipment"),
    ("formulas-navy", "#16213A", lambda: bg_formulas("#16213A", 8), "dark navy with chemical formulas"),
    ("formulas-green", "#123A2E", lambda: bg_formulas("#123A2E", 9), "dark green with chemical formulas"),
    ("element-tiles-navy", "#16213A", lambda: bg_element_tiles("#16213A", 10), "dark navy with periodic element tiles"),
    ("element-tiles-white", "#F5F7FA", lambda: bg_element_tiles("#F5F7FA", 11), "white with periodic element tiles"),
]

KEYWORDS = ["background", "presentation", "slide", "banner", "copy space", "chemistry", "science", "template",
            "wallpaper", "backdrop", "header", "cover", "education", "school", "laboratory", "molecule",
            "atom", "hexagon", "chemical", "research", "medical", "pharmacy", "biology", "technology", "abstract",
            "modern", "web banner", "social media", "website", "landing page", "youtube", "thumbnail", "vector",
            "illustration", "design", "layout", "16:9", "lesson", "class", "lecture"]


def assets():
    out = []
    for key, bg, fn, mood in VARIANTS:
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * 2}" height="{H * 2}" viewBox="0 0 {W} {H}">\n'
               f'<rect x="-1" y="-1" width="{W + 2}" height="{H + 2}" fill="{bg}"/>'
               f'<clipPath id="bgc"><rect width="{W}" height="{H}"/></clipPath><g clip-path="url(#bgc)">{fn()}</g>'
               '\n</svg>\n')
        out.append(dict(name=f"{SET_ID}-{key}", svg=svg, size=6000, png=False,
                        title=f"Chemistry science presentation background, {mood}, copy space vector banner",
                        keywords=KEYWORDS))
    return [(SET_ID, out)]
