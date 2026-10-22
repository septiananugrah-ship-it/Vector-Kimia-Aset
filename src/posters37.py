"""Poster edukasi kimia jilid 37: struktur Lewis molekul dan molekul polar vs nonpolar.
Didaftarkan ke posters.py lewat POSTERS (semua tema x 2 bahasa).
"""
import math

from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters4 import chem

INK = "#1E2A3A"
ECOL = {"O": "#E8573F", "N": "#3D62C4", "C": "#1E2A3A", "H": "#5B6878", "Cl": "#2E9E5B", "F": "#4BA36B", "B": "#C26A2E"}


def _atom(sym, x, y, lone=()):
    """Lambang atom + pasangan elektron bebas di arah sudut tertentu (derajat)."""
    out = [text(sym, x, y + 9, 26, ECOL.get(sym, INK))]
    for a in lone:
        r = math.radians(a)
        cx, cy = x + 24 * math.cos(r), y + 24 * math.sin(r)
        px, py = -math.sin(r) * 5, math.cos(r) * 5
        for s_ in (1, -1):
            out.append(f'<circle cx="{cx + s_ * px:.1f}" cy="{cy + s_ * py:.1f}" r="3.2" fill="{INK}"/>')
    return "".join(out)


def _bond(x1, y1, x2, y2, order=1):
    d = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    a = (x1 + ux * 18, y1 + uy * 18)
    b = (x2 - ux * 18, y2 - uy * 18)
    offs = {1: [0], 2: [-4, 4], 3: [-6, 0, 6]}[order]
    return "".join(f'<path d="M{a[0] - uy * o:.1f} {a[1] + ux * o:.1f}L{b[0] - uy * o:.1f} {b[1] + ux * o:.1f}" '
                   f'stroke="{INK}" stroke-width="3" stroke-linecap="round"/>' for o in offs)


def _mol(kind, cx, cy):
    L = 56
    if kind == "H2O":
        return (_bond(cx, cy, cx - 48, cy + 38) + _bond(cx, cy, cx + 48, cy + 38) + _atom("O", cx, cy, (-35, -145))
                + _atom("H", cx - 48, cy + 38) + _atom("H", cx + 48, cy + 38))
    if kind == "NH3":
        return ("".join(_bond(cx, cy, cx + dx, cy + dy) for dx, dy in ((-L, 10), (L, 10), (0, L)))
                + _atom("N", cx, cy, (-90,)) + _atom("H", cx - L, cy + 10) + _atom("H", cx + L, cy + 10)
                + _atom("H", cx, cy + L))
    if kind == "CH4":
        return ("".join(_bond(cx, cy, cx + dx, cy + dy) for dx, dy in ((-L, 0), (L, 0), (0, -L), (0, L)))
                + _atom("C", cx, cy) + "".join(_atom("H", cx + dx, cy + dy) for dx, dy in ((-L, 0), (L, 0), (0, -L),
                                                                                          (0, L))))
    if kind == "CO2":
        return (_bond(cx - L - 8, cy, cx, cy, 2) + _bond(cx, cy, cx + L + 8, cy, 2)
                + _atom("O", cx - L - 8, cy, (135, 225)) + _atom("C", cx, cy) + _atom("O", cx + L + 8, cy, (45, -45)))
    if kind == "N2":
        return (_bond(cx - 34, cy, cx + 34, cy, 3) + _atom("N", cx - 34, cy, (180,)) + _atom("N", cx + 34, cy, (0,)))
    if kind == "O2":
        return (_bond(cx - 34, cy, cx + 34, cy, 2) + _atom("O", cx - 34, cy, (135, 225))
                + _atom("O", cx + 34, cy, (45, -45)))
    if kind == "HCl":
        return _bond(cx - 34, cy, cx + 30, cy) + _atom("H", cx - 34, cy) + _atom("Cl", cx + 30, cy, (-90, 0, 90))
    # Cl2
    return (_bond(cx - 36, cy, cx + 36, cy) + _atom("Cl", cx - 36, cy, (-90, 180, 90))
            + _atom("Cl", cx + 36, cy, (-90, 0, 90)))


LEWIS = [("H2O", "Water", "H_{2}O", "2 bonding pairs, 2 lone pairs"),
         ("NH3", "Ammonia", "NH_{3}", "3 bonding pairs, 1 lone pair"),
         ("CH4", "Methane", "CH_{4}", "4 bonding pairs"),
         ("CO2", "Carbon dioxide", "CO_{2}", "2 double bonds"),
         ("N2", "Nitrogen", "N_{2}", "1 triple bond"),
         ("O2", "Oxygen", "O_{2}", "1 double bond"),
         ("HCl", "Hydrogen chloride", "HCl", "1 single bond, 3 lone pairs on Cl"),
         ("Cl2", "Chlorine", "Cl_{2}", "1 single bond, 6 lone pairs")]


def lewis_structures(th):
    W = 1226
    top = 122
    gap = 14
    cw = (W - 2 * MX - 3 * gap) / 4
    ch = 280
    H = top + 2 * (ch + gap) + 50
    out = [header(W, th, "LEWIS STRUCTURES", "Lines show shared electron pairs, dots show lone pairs")]
    cols = [T, O, P, R, "#3D7DDB", "#E8573F", "#4BB04A", "#E0B23A"]
    for i, (kind, name, f, desc) in enumerate(LEWIS):
        x = MX + (i % 4) * (cw + gap)
        y = top + (i // 4) * (ch + gap)
        out.append(_card(x, y, cw, ch, th))
        out.append(f'<rect x="{x}" y="{y}" width="{cw}" height="8" rx="4" fill="{cols[i]}"/>')
        out.append(fit_text(name, x + cw / 2, y + 40, 18, th["ink"], cw - 20))
        out.append(chem(f, x + cw / 2, y + 66, 16, th["accent"], "middle"))
        out.append(f'<rect x="{x + 16}" y="{y + 80}" width="{cw - 32}" height="140" rx="12" fill="{th["plate"]}"/>')
        out.append(_mol(kind, x + cw / 2, y + 140 if kind in ("H2O",) else y + 150 if kind != "NH3" else y + 130))
        out.append(fit_text(desc, x + cw / 2, y + 250, 13.5, th["sub"], cw - 24, "SemiBold"))
    out.append(text("Atoms share electrons to reach a full outer shell (octet rule; H needs only 2)", W / 2, H - 20,
                    13, th["sub"], "SemiBold"))
    return W, H, "".join(out)


def polarity(th):
    W = 1226
    top = 122
    H = top + 160 + 20 + 360 + 20 + 120 + 30
    out = [header(W, th, "POLAR AND NONPOLAR MOLECULES", "Polarity depends on electronegativity and molecular shape")]
    out.append(_card(MX, top, W - 2 * MX, 160, th))
    out.append(text("Electronegativity difference (ΔEN)", W / 2, top + 36, 17, th["ink"]))
    bands = [("0 – 0.4", "Nonpolar covalent", "#4FB3C9"), ("0.4 – 1.7", "Polar covalent", "#F2A541"),
             ("> 1.7", "Ionic", "#E8573F")]
    bw = (W - 2 * MX - 60) / 3
    for k, (rng, lab, col) in enumerate(bands):
        bx = MX + 30 + k * bw
        out.append(f'<rect x="{bx:.1f}" y="{top + 56}" width="{bw:.1f}" height="80" fill="{col}"'
                   + (' rx="14"' if k != 1 else '') + '/>')
        out.append(text(tr(rng), bx + bw / 2, top + 90, 20, "#FFFFFF"))
        out.append(fit_text(lab, bx + bw / 2, top + 120, 15, "#FFFFFF", bw - 20))
    y = top + 180
    cw = (W - 2 * MX - 20) / 2
    for k, (title, col, mols, note) in enumerate((
            ("Polar molecules", "#F2A541", ["H2O", "NH3", "HCl"], "Uneven charge: has a positive and a negative end"),
            ("Nonpolar molecules", "#4FB3C9", ["CO2", "CH4", "Cl2"], "Even charge, or bond dipoles cancel out"))):
        x = MX + k * (cw + 20)
        out.append(_card(x, y, cw, 360, th))
        out.append(f'<rect x="{x}" y="{y}" width="{cw}" height="56" rx="14" fill="{col}"/>'
                   f'<rect x="{x}" y="{y + 30}" width="{cw}" height="26" fill="{col}"/>')
        out.append(text(title, x + cw / 2, y + 38, 21, "#FFFFFF"))
        mw = (cw - 40) / 3
        for j, m in enumerate(mols):
            mx = x + 20 + j * mw
            out.append(f'<rect x="{mx + 6:.1f}" y="{y + 74}" width="{mw - 12:.1f}" height="200" rx="12" '
                       f'fill="{th["plate"]}"/>')
            g = _mol(m, 0, 0)
            sc = .62 if m in ("CO2",) else .72
            out.append(f'<g transform="translate({mx + mw / 2:.1f} {y + 160}) scale({sc})">{g}</g>')
            if k == 0:
                out.append(text("δ⁻" if m != "HCl" else "δ⁺", mx + mw / 2 - (0 if m != "HCl" else 30), y + 112, 15,
                                "#E8573F" if m != "HCl" else "#3D62C4"))
                out.append(text("δ⁺" if m != "HCl" else "δ⁻", mx + mw / 2 + (0 if m != "HCl" else 30),
                                y + 238 if m != "HCl" else y + 112, 15, "#3D62C4" if m != "HCl" else "#E8573F"))
            out.append(chem({"H2O": "H_{2}O", "NH3": "NH_{3}", "HCl": "HCl", "CO2": "CO_{2}", "CH4": "CH_{4}",
                             "Cl2": "Cl_{2}"}[m], mx + mw / 2, y + 262, 16, INK, "middle"))
        out.append(fit_text(note, x + cw / 2, y + 320, 15, th["ink"], cw - 30, "SemiBold"))
    y += 380
    out.append(_card(MX, y, W - 2 * MX, 120, th))
    out.append(text("Like dissolves like", W / 2, y + 40, 18, th["ink"]))
    out.append(fit_text("Polar substances dissolve in polar solvents (salt in water); nonpolar in nonpolar (oil in "
                        "petrol)", W / 2, y + 82, 15, th["sub"], W - 2 * MX - 60, "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("lewis-structures", lewis_structures, "Lewis structures chart, electron dot diagrams of common molecules",
     ["lewis structure", "electron dot", "covalent bond", "lone pair", "bonding pair", "octet rule", "water",
      "ammonia", "methane", "carbon dioxide", "double bond", "triple bond", "molecules", "chemical bonding"]),
    ("polar-nonpolar-molecules", polarity, "Polar and nonpolar molecules chart, electronegativity difference and "
                                           "dipoles",
     ["polarity", "polar molecule", "nonpolar molecule", "electronegativity", "dipole", "covalent bond", "ionic bond",
      "water", "carbon dioxide", "like dissolves like", "solubility", "chemical bonding", "molecular shape",
      "partial charge"]),
]

TR.update({
    "LEWIS STRUCTURES": "STRUKTUR LEWIS",
    "Lines show shared electron pairs, dots show lone pairs":
        "Garis menunjukkan pasangan elektron ikatan, titik menunjukkan pasangan elektron bebas",
    "Water": "Air", "Ammonia": "Amonia", "Methane": "Metana", "Carbon dioxide": "Karbon dioksida",
    "Nitrogen": "Nitrogen", "Oxygen": "Oksigen", "Hydrogen chloride": "Hidrogen klorida", "Chlorine": "Klorin",
    "2 bonding pairs, 2 lone pairs": "2 PEI, 2 PEB", "3 bonding pairs, 1 lone pair": "3 PEI, 1 PEB",
    "4 bonding pairs": "4 PEI", "2 double bonds": "2 ikatan rangkap dua", "1 triple bond": "1 ikatan rangkap tiga",
    "1 double bond": "1 ikatan rangkap dua", "1 single bond, 3 lone pairs on Cl": "1 ikatan tunggal, 3 PEB pada Cl",
    "1 single bond, 6 lone pairs": "1 ikatan tunggal, 6 PEB",
    "Atoms share electrons to reach a full outer shell (octet rule; H needs only 2)":
        "Atom berbagi elektron agar kulit terluarnya penuh (aturan oktet; H cukup 2) · PEI = pasangan elektron ikatan, "
        "PEB = pasangan elektron bebas",
    "POLAR AND NONPOLAR MOLECULES": "MOLEKUL POLAR DAN NONPOLAR",
    "Polarity depends on electronegativity and molecular shape": "Kepolaran bergantung pada keelektronegatifan dan bentuk molekul",
    "Electronegativity difference (ΔEN)": "Selisih keelektronegatifan (ΔEN)", "0 – 0.4": "0 – 0,4",
    "0.4 – 1.7": "0,4 – 1,7", "> 1.7": "> 1,7", "Nonpolar covalent": "Kovalen nonpolar",
    "Polar covalent": "Kovalen polar", "Ionic": "Ionik", "Polar molecules": "Molekul polar",
    "Nonpolar molecules": "Molekul nonpolar",
    "Uneven charge: has a positive and a negative end": "Muatan tidak merata: memiliki ujung positif dan negatif",
    "Even charge, or bond dipoles cancel out": "Muatan merata, atau dipol ikatan saling meniadakan",
    "Like dissolves like": "Like dissolves like (sejenis melarutkan sejenis)",
    "Polar substances dissolve in polar solvents (salt in water); nonpolar in nonpolar (oil in petrol)":
        "Zat polar larut dalam pelarut polar (garam dalam air); zat nonpolar dalam nonpolar (minyak dalam bensin)",
})
