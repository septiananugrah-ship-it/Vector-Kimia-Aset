"""Poster edukasi kimia jilid 20: distilasi bertingkat minyak bumi dan jenis-jenis padatan kristal.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
import math

from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, particle, text, tr
from posters2 import _card
from posters3 import arrow_line, mix
from render import style_attrs
from textpath import width

FRACTIONS = [
    ("Refinery gas", "< 30 °C", "C₁–C₄", "LPG, bottled gas"),
    ("Gasoline", "30–180 °C", "C₅–C₁₀", "Fuel for cars"),
    ("Kerosene", "180–250 °C", "C₁₁–C₁₄", "Jet fuel, stoves"),
    ("Diesel oil", "250–350 °C", "C₁₅–C₂₀", "Fuel for trucks and buses"),
    ("Lubricating oil", "350–500 °C", "C₂₀–C₄₀", "Engine oil, wax, grease"),
    ("Residue", "> 500 °C", "> C₄₀", "Asphalt for roads, bitumen"),
]


def distillation(th):
    W = 1226
    top = 122
    ch = 640
    H = top + ch + 50
    out = [header(W, th, "FRACTIONAL DISTILLATION OF CRUDE OIL", "Crude oil is separated into fractions by their "
                                                                 "boiling points")]
    out.append(_card(MX, top, W - 2 * MX, ch, th))
    n = len(FRACTIONS)
    tx, tw = MX + 250, 170
    ty, th_ = top + 50, ch - 100
    cool, hot = "#4F8FE0", "#E8573F"
    g = []
    seg = th_ / n
    for k in range(n):
        g.append(f'<rect x="{tx}" y="{ty + k * seg:.1f}" width="{tw}" height="{seg + .5:.1f}" '
                 f'fill="{mix(cool, hot, k / (n - 1))}"/>')
    out.append(f'<clipPath id="tower"><rect x="{tx}" y="{ty}" width="{tw}" height="{th_}" rx="40"/></clipPath>'
               f'<g clip-path="url(#tower)">{"".join(g)}</g>')
    for k in range(1, n):
        y = ty + k * seg
        out.append(f'<path d="M{tx + 10} {y:.1f}H{tx + tw - 10}" stroke="#FFFFFF" stroke-width="4" '
                   'stroke-linecap="round"/>')
    out.append(f'<rect x="{tx}" y="{ty}" width="{tw}" height="{th_}" rx="40" fill="none" stroke="{th["ink"]}" '
               'stroke-width="3"/>')
    # bubble cap di setiap baki
    for k in range(1, n):
        y = ty + k * seg
        for j in range(3):
            cx = tx + 34 + j * 42
            out.append(f'<path d="M{cx - 11} {y:.1f}a11 9 0 0 1 22 0z" fill="#FFFFFF"/>')
    out.append(text("Cool", tx + tw / 2, ty - 14, 15, cool if th["bg"] == "#FFFFFF" else "#8DB8F0", "Bold"))
    out.append(text("Hot", tx + tw / 2, ty + th_ + 30, 15, hot, "Bold"))
    # pipa masuk: minyak mentah + tungku
    fy = ty + th_ - seg / 2
    fx = MX + 40
    out.append(f'<rect x="{fx}" y="{fy - 70}" width="120" height="96" rx="16" fill="{th["plate"]}"/>')
    flames = "".join(f'<path d="M{fx + 30 + j * 30} {fy + 14}c-12 -14 -2 -24 0 -36c6 12 14 20 0 36z" fill="{hot}"/>'
                     for j in range(3))
    out.append(flames)
    out.append(text("Furnace", fx + 60, fy - 44, 15, "#1E2A3A"))
    out.append(text("Crude oil", fx + 60, fy + 56, 15, th["ink"], "SemiBold"))
    out.append(arrow_line(fx + 124, fy - 20, tx - 6, fy - 20, th["ink"], 5))
    out.append(arrow_line(tx - 40, fy - 120, tx - 40, ty + 60, th["accent"], 4))
    lines, cur = [], ""
    for w_ in tr("Vapor rises and cools; each fraction condenses at its boiling point").split():
        t = (cur + " " + w_).strip()
        if width(t, 15, "SemiBold") > 150 and cur:
            lines.append(cur)
            cur = w_
        else:
            cur = t
    lines.append(cur)
    for j, line in enumerate(lines):
        out.append(text(line, tx - 60, ty + 120 + j * 24, 15, th["ink"], "SemiBold", "end"))
    # pipa keluar + kartu fraksi
    cx0 = tx + tw + 70
    cw = W - MX - 24 - cx0
    for k, (name, bp, carbon, use) in enumerate(FRACTIONS):
        y = ty + k * seg + seg / 2
        col = mix(cool, hot, k / (n - 1))
        out.append(arrow_line(tx + tw + 4, y, cx0 - 8, y, col, 6))
        out.append(f'<rect x="{cx0}" y="{y - seg / 2 + 8:.1f}" width="{cw}" height="{seg - 16:.1f}" rx="12" '
                   f'fill="{mix(th["card"], col, .16)}"/>')
        out.append(f'<rect x="{cx0}" y="{y - seg / 2 + 8:.1f}" width="8" height="{seg - 16:.1f}" rx="4" '
                   f'fill="{col}"/>')
        out.append(fit_text(name, cx0 + 28, y - 4, 20, th["ink"], 250, anchor="start"))
        out.append(fit_text(use, cx0 + 28, y + 22, 14, th["sub"], 250, "SemiBold", anchor="start"))
        out.append(text(bp, cx0 + 360, y + 7, 18, th["ink"], "Bold"))
        out.append(f'<rect x="{cx0 + cw - 150}" y="{y - 20:.1f}" width="130" height="40" rx="20" fill="{col}"/>')
        out.append(text(carbon, cx0 + cw - 85, y + 7, 16, "#FFFFFF"))
    out.append(text("Boiling ranges and carbon numbers are approximate", W / 2, H - 20, 13, th["sub"], "SemiBold"))
    return W, H, "".join(out)


def _lattice(kind, cx, cy, key):
    out = [f'<g {style_attrs(1.4)}>']
    if kind == 0:  # ionik: Na+ Cl- berselang-seling
        for i in range(4):
            for j in range(4):
                big = (i + j) % 2 == 0
                out.append(particle(cx - 54 + i * 36, cy - 54 + j * 36, 15 if big else 10,
                                    "#7FD14F" if big else "#9B7FE0", f"{key}{i}{j}"))
    elif kind == 1:  # logam: ion positif dalam lautan elektron
        out.append(f'<rect x="{cx - 76}" y="{cy - 76}" width="152" height="152" rx="18" fill="#CFE3F5" stroke="none"/>')
        for i in range(4):
            for j in range(4):
                x, y = cx - 54 + i * 36, cy - 54 + j * 36
                out.append(particle(x, y, 14, "#F2A541", f"{key}{i}{j}"))
                out.append(f'<path d="M{x - 5} {y}h10M{x} {y - 5}v10" stroke="#FFFFFF" stroke-width="2.6" '
                           'stroke-linecap="round"/>')
        for k in range(9):
            a = k * 2.4
            out.append(f'<circle cx="{cx - 36 + (k % 3) * 36 + math.cos(a) * 4:.1f}" '
                       f'cy="{cy - 36 + (k // 3) * 36 + math.sin(a) * 4:.1f}" r="4" fill="#3D62C4" stroke="none"/>')
    elif kind == 2:  # kovalen raksasa: jaringan heksagonal
        pts = []
        for r in range(3):
            for c in range(4):
                x = cx - 66 + c * 44 + (22 if r % 2 else 0)
                y = cy - 50 + r * 50
                pts.append((x, y))
        for i, (x1, y1) in enumerate(pts):
            for x2, y2 in pts[i + 1:]:
                if math.hypot(x2 - x1, y2 - y1) < 58:
                    out.append(f'<path d="M{x1} {y1}L{x2} {y2}" stroke="#5B6878" stroke-width="5"/>')
        for k, (x, y) in enumerate(pts):
            out.append(particle(x, y, 12, "#5B6878", f"{key}{k}"))
    else:  # molekul: molekul-molekul kecil terpisah
        mols = [(-40, -56, 20), (42, -50, -35), (-44, 2, 70), (38, 6, 10), (-36, 58, -25), (44, 60, 55)]
        for k, (dx, dy, a) in enumerate(mols):
            ux, uy = math.cos(math.radians(a)) * 11, math.sin(math.radians(a)) * 11
            out.append(particle(cx + dx - ux, cy + dy - uy, 12, "#E8573F", f"{key}a{k}"))
            out.append(particle(cx + dx + ux, cy + dy + uy, 12, "#E8573F", f"{key}b{k}"))
    out.append('</g>')
    return "".join(out)


SOLIDS = [
    ("Ionic", "Positive and negative ions held by ionic bonds", "High", "Only when molten or dissolved", "NaCl, MgO", T),
    ("Metallic", "Metal ions in a sea of free electrons", "Usually high", "Yes, as solid and liquid", "Cu, Fe, Al", O),
    ("Covalent network", "Atoms joined by covalent bonds in a giant network", "Very high", "No (except graphite)",
     "Diamond, SiO₂", P),
    ("Molecular", "Separate molecules held by weak intermolecular forces", "Low", "No", "Ice, I₂, dry ice", R),
]


def solids(th):
    W = 1226
    top = 122
    gap = 18
    cw = (W - 2 * MX - 3 * gap) / 4
    ch = 590
    H = top + ch + 30
    out = [header(W, th, "TYPES OF CRYSTALLINE SOLIDS", "How the particles are held together decides the properties "
                                                        "of a solid")]
    for i, (name, desc, mp, cond, ex, col) in enumerate(SOLIDS):
        x = MX + i * (cw + gap)
        out.append(_card(x, top, cw, ch, th))
        out.append(f'<rect x="{x}" y="{top}" width="{cw}" height="58" rx="14" fill="{col}"/>'
                   f'<rect x="{x}" y="{top + 32}" width="{cw}" height="26" fill="{col}"/>')
        out.append(fit_text(name, x + cw / 2, top + 38, 21, "#FFFFFF", cw - 20))
        out.append(f'<rect x="{x + 20}" y="{top + 76}" width="{cw - 40}" height="190" rx="14" fill="{th["plate"]}"/>')
        out.append(_lattice(i, x + cw / 2, top + 171, f"cs{i}"))
        lines, cur = [], ""
        for w_ in tr(desc).split():
            t = (cur + " " + w_).strip()
            if width(t, 14, "SemiBold") > cw - 36 and cur:
                lines.append(cur)
                cur = w_
            else:
                cur = t
        lines.append(cur)
        for j, ln in enumerate(lines[:3]):
            out.append(text(ln, x + cw / 2, top + 300 + j * 21, 14, th["ink"], "SemiBold"))
        rows = [("Melting point", mp), ("Conducts electricity", cond), ("Examples", ex)]
        for j, (k, v) in enumerate(rows):
            y = top + 378 + j * 68
            out.append(f'<rect x="{x + 16}" y="{y}" width="{cw - 32}" height="58" rx="10" '
                       f'fill="{mix(th["card"], col, .14)}"/>')
            out.append(text(k, x + cw / 2, y + 22, 12.5, th["sub"], "SemiBold"))
            out.append(fit_text(v, x + cw / 2, y + 45, 15, th["ink"], cw - 50))
    return W, H, "".join(out)


POSTERS = [
    ("fractional-distillation-crude-oil", distillation,
     "Fractional distillation of crude oil chart, refinery column with petroleum fractions",
     ["fractional distillation", "crude oil", "petroleum", "refinery", "fractionating column", "gasoline", "kerosene",
      "diesel", "lpg", "bitumen", "hydrocarbons", "boiling point", "fossil fuel", "oil refining"]),
    ("types-of-solids", solids, "Types of crystalline solids chart, ionic, metallic, covalent network and molecular",
     ["crystalline solids", "ionic solid", "metallic bond", "covalent network", "molecular solid", "crystal lattice",
      "sodium chloride", "diamond", "melting point", "conductivity", "sea of electrons", "solid state",
      "properties of matter", "chemical bonding"]),
]

TR.update({
    "FRACTIONAL DISTILLATION OF CRUDE OIL": "DISTILASI BERTINGKAT MINYAK BUMI",
    "Crude oil is separated into fractions by their boiling points":
        "Minyak mentah dipisahkan menjadi fraksi-fraksi berdasarkan titik didihnya",
    "Refinery gas": "Gas", "Gasoline": "Bensin", "Kerosene": "Kerosin (minyak tanah)", "Diesel oil": "Solar",
    "Lubricating oil": "Oli (pelumas)", "Residue": "Residu",
    "LPG, bottled gas": "Elpiji (LPG), gas tabung", "Fuel for cars": "Bahan bakar mobil dan motor",
    "Jet fuel, stoves": "Avtur, bahan bakar kompor", "Fuel for trucks and buses": "Bahan bakar truk dan bus",
    "Engine oil, wax, grease": "Oli mesin, lilin, gemuk", "Asphalt for roads, bitumen": "Aspal jalan, bitumen",
    "Vapor rises and cools; each fraction condenses at its boiling point":
        "Uap naik dan mendingin; tiap fraksi mengembun pada titik didihnya",
    "Cool": "Dingin", "Hot": "Panas", "Furnace": "Pemanas", "Crude oil": "Minyak mentah",
    "Boiling ranges and carbon numbers are approximate": "Rentang titik didih dan jumlah atom C merupakan perkiraan",
    "TYPES OF CRYSTALLINE SOLIDS": "JENIS-JENIS PADATAN KRISTAL",
    "How the particles are held together decides the properties of a solid":
        "Cara partikel saling terikat menentukan sifat suatu padatan",
    "Ionic": "Ionik", "Metallic": "Logam", "Covalent network": "Kovalen raksasa", "Molecular": "Molekuler",
    "Positive and negative ions held by ionic bonds": "Ion positif dan negatif yang terikat oleh ikatan ion",
    "Metal ions in a sea of free electrons": "Ion logam dalam lautan elektron bebas",
    "Atoms joined by covalent bonds in a giant network": "Atom-atom terikat kovalen membentuk jaringan raksasa",
    "Separate molecules held by weak intermolecular forces": "Molekul-molekul terpisah yang terikat gaya antarmolekul lemah",
    "Melting point": "Titik leleh", "Conducts electricity": "Daya hantar listrik", "Examples": "Contoh",
    "High": "Tinggi", "Usually high": "Umumnya tinggi", "Very high": "Sangat tinggi", "Low": "Rendah",
    "Only when molten or dissolved": "Hanya saat lelehan/larutan", "Yes, as solid and liquid": "Ya, padat maupun cair",
    "No (except graphite)": "Tidak (kecuali grafit)", "No": "Tidak",
    "Diamond, SiO₂": "Intan, SiO₂", "Ice, I₂, dry ice": "Es, I₂, es kering",
})
