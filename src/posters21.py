"""Poster edukasi kimia jilid 21: biomolekul (makromolekul) dan hibridisasi orbital.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
import math

from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, particle, text, tr
from posters2 import _card
from posters3 import mix
from posters4 import chem
from render import style_attrs
from textpath import width

BIO = [
    ("Carbohydrates", "C, H, O", "Monosaccharides (glucose)", "Quick energy source", "Rice, bread, sugar",
     "Benedict's: brick red (sugars) · Iodine: blue-black (starch)", O),
    ("Proteins", "C, H, O, N (S)", "Amino acids", "Growth and repair, enzymes", "Eggs, meat, tofu",
     "Biuret: purple", R),
    ("Lipids", "C, H, O", "Fatty acids + glycerol", "Energy storage, cell membranes", "Oil, butter, nuts",
     "Sudan III: red layer · paper: translucent spot", "#E0B23A"),
    ("Nucleic acids", "C, H, O, N, P", "Nucleotides", "Store genetic information", "DNA, RNA",
     "Diphenylamine: blue (DNA)", P),
]


def _wrap(s, size, max_w, weight="SemiBold"):
    lines, cur = [], ""
    for w_ in s.split():
        t = (cur + " " + w_).strip()
        if width(t, size, weight) > max_w and cur:
            lines.append(cur)
            cur = w_
        else:
            cur = t
    return lines + [cur]


def _bio_icon(i, cx, cy, col, key):
    out = [f'<g {style_attrs(1.6)}>']
    if i == 0:  # cincin glukosa (heksagon)
        pts = [(cx + 30 * math.cos(math.radians(a)), cy + 30 * math.sin(math.radians(a))) for a in range(-90, 270, 60)]
        out.append(f'<path d="M{"L".join(f"{x:.1f} {y:.1f}" for x, y in pts)}z" fill="{mix(col, "#FFFFFF", .55)}" '
                   f'stroke="{col}" stroke-width="5" stroke-linejoin="round"/>')
        out.append(particle(pts[1][0], pts[1][1], 8, "#E8573F", f"{key}o"))
    elif i == 1:  # rantai asam amino
        for k in range(5):
            out.append(particle(cx - 44 + k * 22, cy + (8 if k % 2 else -8), 11,
                                ["#E8573F", "#F2A541", "#4FB3C9", "#7FD14F", "#9B7FE0"][k], f"{key}{k}"))
    elif i == 2:  # trigliserida: kepala + 3 ekor
        out.append(f'<rect x="{cx - 40}" y="{cy - 26}" width="20" height="52" rx="8" fill="{col}"/>')
        for k in range(3):
            y = cy - 18 + k * 18
            out.append(f'<path d="M{cx - 20} {y}l10 -6l10 6l10 -6l10 6l10 -6l10 6" fill="none" stroke="{col}" '
                       'stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/>')
    else:  # heliks ganda DNA
        for k in range(9):
            t = k / 8
            x = cx - 40 + t * 80
            y1 = cy + 22 * math.sin(t * 2 * math.pi)
            y2 = cy - 22 * math.sin(t * 2 * math.pi)
            out.append(f'<path d="M{x:.1f} {y1:.1f}L{x:.1f} {y2:.1f}" stroke="{mix(col, "#FFFFFF", .4)}" '
                       'stroke-width="3"/>')
        for sgn, c in ((1, col), (-1, "#4FB3C9")):
            d = "M" + " L".join(f"{cx - 40 + t / 20 * 80:.1f} {cy + sgn * 22 * math.sin(t / 20 * 2 * math.pi):.1f}"
                                for t in range(21))
            out.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round"/>')
    out.append('</g>')
    return "".join(out)


def biomolecules(th):
    W = 1226
    top = 122
    gap = 18
    cw = (W - 2 * MX - 3 * gap) / 4
    ch = 540
    H = top + ch + 30
    out = [header(W, th, "BIOMOLECULES", "The four big molecules of life and how to test for them")]
    for i, (name, elems, mono, func, ex, test, col) in enumerate(BIO):
        x = MX + i * (cw + gap)
        out.append(_card(x, top, cw, ch, th))
        out.append(f'<rect x="{x}" y="{top}" width="{cw}" height="58" rx="14" fill="{col}"/>'
                   f'<rect x="{x}" y="{top + 32}" width="{cw}" height="26" fill="{col}"/>')
        out.append(fit_text(name, x + cw / 2, top + 38, 21, "#FFFFFF", cw - 20))
        out.append(f'<circle cx="{x + cw / 2}" cy="{top + 128}" r="54" fill="{th["plate"]}"/>')
        out.append(_bio_icon(i, x + cw / 2, top + 128, col, f"bm{i}"))
        rows = [("Elements", elems), ("Building blocks", mono), ("Main function", func), ("Examples", ex),
                ("Food test", test)]
        y = top + 204
        for k, v in rows:
            lines = _wrap(tr(v), 14.5, cw - 44)
            hh = 30 + 20 * len(lines)
            out.append(f'<rect x="{x + 14}" y="{y}" width="{cw - 28}" height="{hh}" rx="10" '
                       f'fill="{mix(th["card"], col, .14)}"/>')
            out.append(text(k, x + cw / 2, y + 20, 12, th["sub"], "SemiBold"))
            for j, ln in enumerate(lines):
                out.append(text(ln, x + cw / 2, y + 42 + j * 20, 14.5, th["ink"], "Bold"))
            y += hh + 10
    return W, H, "".join(out)


HYB = [
    ("sp", "2 hybrid orbitals", "Linear", "180°", "BeCl_{2}, C_{2}H_{2}", [180, 0], T),
    ("sp^{2}", "3 hybrid orbitals", "Trigonal planar", "120°", "BF_{3}, C_{2}H_{4}", [-90, 30, 150], O),
    ("sp^{3}", "4 hybrid orbitals", "Tetrahedral", "109.5°", "CH_{4}, H_{2}O, NH_{3}", [-90, 20, 160, 70], P),
]


def _hybrid(cx, cy, angles, col):
    out = []
    for k, a in enumerate(angles):
        r = math.radians(a)
        back = k == 3
        L = 74 if not back else 52
        tx, ty = cx + math.cos(r) * L, cy + math.sin(r) * L
        nx, ny = -math.sin(r) * 28, math.cos(r) * 28
        c = mix(col, "#FFFFFF", .35) if back else col
        out.append(f'<path d="M{cx} {cy}C{cx + math.cos(r) * L * .5 + nx:.1f} {cy + math.sin(r) * L * .5 + ny:.1f} '
                   f'{tx + nx * .8:.1f} {ty + ny * .8:.1f} {tx:.1f} {ty:.1f}C{tx - nx * .8:.1f} {ty - ny * .8:.1f} '
                   f'{cx + math.cos(r) * L * .5 - nx:.1f} {cy + math.sin(r) * L * .5 - ny:.1f} {cx} {cy}z" '
                   f'fill="{c}" stroke="#1E2A3A" stroke-width="1.6"/>')
        # cuping kecil di belakang
        bx, by = cx - math.cos(r) * 14, cy - math.sin(r) * 14
        out.append(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="7" fill="{mix(col, "#FFFFFF", .55)}" stroke="#1E2A3A" '
                   'stroke-width="1.4"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="7" fill="#1E2A3A"/>')
    return "".join(out)


def hybridization(th):
    W = 1226
    top = 122
    gap = 20
    cw = (W - 2 * MX - 2 * gap) / 3
    ch = 520
    H = top + ch + 24 + 110
    out = [header(W, th, "ORBITAL HYBRIDIZATION", "Atomic orbitals mix to form new, equal hybrid orbitals for "
                                                  "bonding")]
    for i, (name, n, geo, ang, ex, angles, col) in enumerate(HYB):
        x = MX + i * (cw + gap)
        out.append(_card(x, top, cw, ch, th))
        out.append(f'<rect x="{x}" y="{top}" width="{cw}" height="8" rx="4" fill="{col}"/>')
        out.append(chem(name, x + cw / 2, top + 66, 44, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3),
                        "middle"))
        out.append(text(n, x + cw / 2, top + 100, 15, th["sub"], "SemiBold"))
        out.append(f'<rect x="{x + 24}" y="{top + 122}" width="{cw - 48}" height="170" rx="14" fill="{th["plate"]}"/>')
        out.append(_hybrid(x + cw / 2, top + 207, angles, col))
        rows = [("Geometry", geo), ("Bond angle", ang), ("Examples", ex)]
        for j, (k, v) in enumerate(rows):
            y = top + 312 + j * 66
            out.append(f'<rect x="{x + 18}" y="{y}" width="{cw - 36}" height="56" rx="10" '
                       f'fill="{mix(th["card"], col, .14)}"/>')
            out.append(text(k, x + 36, y + 34, 14, th["sub"], "SemiBold", "start"))
            out.append(chem(tr(v), x + cw - 36, y + 35, 17, th["ink"], "end"))
    y = top + ch + 24
    out.append(_card(MX, y, W - 2 * MX, 86, th))
    out.append(fit_text("Count the electron domains around the central atom: 2 → sp, 3 → sp², 4 → sp³", W / 2, y + 52,
                        18, th["ink"], W - 2 * MX - 60, "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("biomolecules", biomolecules, "Biomolecules chart, carbohydrates, proteins, lipids and nucleic acids with food tests",
     ["biomolecules", "macromolecules", "carbohydrates", "proteins", "lipids", "nucleic acids", "dna", "glucose",
      "amino acids", "fatty acids", "food test", "benedict", "biuret", "biochemistry"]),
    ("orbital-hybridization", hybridization, "Orbital hybridization chart, sp, sp2 and sp3 with geometry and examples",
     ["hybridization", "hybrid orbitals", "sp", "sp2", "sp3", "orbital", "molecular geometry", "bond angle",
      "tetrahedral", "trigonal planar", "linear", "methane", "covalent bond", "valence bond theory"]),
]

TR.update({
    "BIOMOLECULES": "BIOMOLEKUL",
    "The four big molecules of life and how to test for them": "Empat makromolekul penyusun makhluk hidup dan cara mengujinya",
    "Carbohydrates": "Karbohidrat", "Proteins": "Protein", "Lipids": "Lipid (lemak)", "Nucleic acids": "Asam nukleat",
    "Elements": "Unsur penyusun", "Building blocks": "Monomer", "Main function": "Fungsi utama", "Examples": "Contoh",
    "Food test": "Uji makanan",
    "Monosaccharides (glucose)": "Monosakarida (glukosa)", "Amino acids": "Asam amino",
    "Fatty acids + glycerol": "Asam lemak + gliserol", "Nucleotides": "Nukleotida",
    "Quick energy source": "Sumber energi cepat", "Growth and repair, enzymes": "Pertumbuhan, perbaikan sel, enzim",
    "Energy storage, cell membranes": "Cadangan energi, membran sel",
    "Store genetic information": "Menyimpan informasi genetik",
    "Rice, bread, sugar": "Nasi, roti, gula", "Eggs, meat, tofu": "Telur, daging, tahu",
    "Oil, butter, nuts": "Minyak, mentega, kacang",
    "Benedict's: brick red (sugars) · Iodine: blue-black (starch)":
        "Benedict: merah bata (gula) · Iodin: biru kehitaman (amilum)",
    "Biuret: purple": "Biuret: ungu", "Diphenylamine: blue (DNA)": "Difenilamina: biru (DNA)",
    "Sudan III: red layer · paper: translucent spot": "Sudan III: lapisan merah · kertas: noda transparan",
    "ORBITAL HYBRIDIZATION": "HIBRIDISASI ORBITAL",
    "Atomic orbitals mix to form new, equal hybrid orbitals for bonding":
        "Orbital-orbital atom bercampur membentuk orbital hibrida baru yang setara untuk berikatan",
    "2 hybrid orbitals": "2 orbital hibrida", "3 hybrid orbitals": "3 orbital hibrida",
    "4 hybrid orbitals": "4 orbital hibrida",
    "Geometry": "Bentuk", "Bond angle": "Sudut ikatan", "Linear": "Linear", "Trigonal planar": "Segitiga datar",
    "Tetrahedral": "Tetrahedral",
    "Count the electron domains around the central atom: 2 → sp, 3 → sp², 4 → sp³":
        "Hitung domain elektron di sekitar atom pusat: 2 → sp, 3 → sp², 4 → sp³",
})
