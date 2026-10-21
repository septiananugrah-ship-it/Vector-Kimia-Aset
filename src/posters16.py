"""Poster edukasi kimia jilid 16: bentuk molekul (VSEPR) dan bilangan kuantum.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
import math

from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, particle, text
from render import style_attrs
from posters2 import _card
from posters3 import mix
from posters4 import chem

# vektor ikatan (x, y, kedalaman): kedalaman > 0 = ke depan, < 0 = ke belakang
_TETRA = [(0, -1, 0), (-.88, .42, 0), (.3, .72, .8), (.78, .22, -.8)]
SHAPES = [
    ("Linear", "CO_{2}", "180°", "AX_{2}", "#5B6878", "#E8573F", [(-1, 0, 0), (1, 0, 0)], []),
    ("Trigonal planar", "BF_{3}", "120°", "AX_{3}", "#F2A541", "#7FD14F",
     [(0, -1, 0), (-.87, .5, 0), (.87, .5, 0)], []),
    ("Tetrahedral", "CH_{4}", "109.5°", "AX_{4}", "#5B6878", "#E9EEF3", _TETRA, []),
    ("Trigonal pyramidal", "NH_{3}", "107°", "AX_{3}E", "#3D62C4", "#E9EEF3", _TETRA[1:], [(0, -1)]),
    ("Bent", "H_{2}O", "104.5°", "AX_{2}E_{2}", "#E8573F", "#E9EEF3", [(-.8, .6, 0), (.8, .6, 0)],
     [(-.62, -.78), (.62, -.78)]),
    ("Trigonal bipyramidal", "PCl_{5}", "90° / 120°", "AX_{5}", "#F28C38", "#7FD14F",
     [(0, -1, 0), (0, 1, 0), (-.95, .1, 0), (.5, .5, .8), (.78, -.32, -.8)], []),
    ("Octahedral", "SF_{6}", "90°", "AX_{6}", "#F2D541", "#9BE07A",
     [(0, -1, 0), (0, 1, 0), (-1, 0, 0), (1, 0, 0), (-.5, .5, .8), (.5, -.5, -.8)], []),
    ("Square planar", "XeF_{4}", "90°", "AX_{4}E_{2}", "#4FB3C9", "#9BE07A",
     [(-1, 0, 0), (1, 0, 0), (-.5, .5, .8), (.5, -.5, -.8)], [(0, -1), (0, 1)]),
]


def _molecule(cx, cy, s, center, ligand, bonds, lone, key, th):
    out = [f'<g {style_attrs(1.6)}>']
    for j, (ux, uy) in enumerate(lone):
        a = math.degrees(math.atan2(uy, ux))
        ex, ey = cx + ux * s * .62, cy + uy * s * .62
        out.append(f'<ellipse cx="{ex:.1f}" cy="{ey:.1f}" rx="{s * .42:.1f}" ry="{s * .24:.1f}" '
                   f'transform="rotate({a:.1f} {ex:.1f} {ey:.1f})" fill="{mix(th["card"], th["accent"], .28)}" '
                   f'stroke="{th["accent"]}" stroke-width="1.6" stroke-dasharray="4 4"/>')
        px, py = -uy * 6, ux * 6
        for sgn in (1, -1):
            out.append(f'<circle cx="{ex + sgn * px:.1f}" cy="{ey + sgn * py:.1f}" r="3.6" fill="{th["ink"]}"/>')
    order = sorted(range(len(bonds)), key=lambda i: bonds[i][2])
    back = [i for i in order if bonds[i][2] < 0]
    front = [i for i in order if bonds[i][2] >= 0]
    bond_col = th["sub"]

    def draw(i):
        ux, uy, d = bonds[i]
        r = s * .26 * (1 + .18 * d)
        lx, ly = cx + ux * s, cy + uy * s
        dash = ' stroke-dasharray="5 5"' if d < 0 else ""
        wdt = 7 if d > 0 else 5
        return (f'<path d="M{cx} {cy}L{lx:.1f} {ly:.1f}" stroke="{bond_col}" stroke-width="{wdt}" '
                f'stroke-linecap="round"{dash}/>' + particle(lx, ly, r, ligand, f"{key}l{i}"))

    out += [draw(i) for i in back]
    out.append(particle(cx, cy, s * .36, center, f"{key}c"))
    out += [draw(i) for i in front]
    out.append('</g>')
    return "".join(out)


def vsepr(th):
    W = 1226
    top = 122
    gap = 18
    cw = (W - 2 * MX - 3 * gap) / 4
    ch = 360
    H = top + 2 * (ch + gap) + 44
    out = [header(W, th, "MOLECULAR SHAPES (VSEPR)", "Electron pairs around the central atom repel each other and "
                                                     "set the shape of the molecule")]
    for i, (name, f, angle, axe, cc, lc, bonds, lone) in enumerate(SHAPES):
        x = MX + (i % 4) * (cw + gap)
        y = top + (i // 4) * (ch + gap)
        out.append(_card(x, y, cw, ch, th))
        out.append(fit_text(name, x + cw / 2, y + 38, 19, th["ink"], cw - 24))
        out.append(chem(f, x + cw / 2, y + 66, 17, th["accent"], "middle"))
        out.append(_molecule(x + cw / 2, y + 180, 76, cc, lc, bonds, lone, f"vs{i}", th))
        out.append(f'<rect x="{x + 16}" y="{y + ch - 74}" width="{cw - 32}" height="58" rx="10" '
                   f'fill="{th["plate"]}"/>')
        out.append(text(angle, x + cw / 2, y + ch - 46, 17, "#1E2A3A"))
        out.append(chem(axe, x + cw / 2, y + ch - 24, 13, "#5B6878", "middle", "SemiBold"))
    out.append(text("A = central atom · X = bonded atom · E = lone pair · dashed = behind the page, thick = in front",
                    W / 2, H - 18, 12.5, th["sub"], "SemiBold"))
    return W, H, "".join(out)


QN = [
    ("n", "Principal", "1, 2, 3, …", "Shell: energy level and size of the orbital", T),
    ("l", "Azimuthal", "0 … (n − 1)", "Subshell shape: 0 = s, 1 = p, 2 = d, 3 = f", O),
    ("m_{l}", "Magnetic", "−l … 0 … +l", "Orientation of the orbital in space", P),
    ("m_{s}", "Spin", "+1/2 or −1/2", "Spin direction of the electron (↑ or ↓)", R),
]


def _orbital_s(cx, cy, r, col):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" fill-opacity=".85"/>'
            f'<ellipse cx="{cx - r * .3:.1f}" cy="{cy - r * .35:.1f}" rx="{r * .3:.1f}" ry="{r * .18:.1f}" '
            f'transform="rotate(-35 {cx - r * .3:.1f} {cy - r * .35:.1f})" fill="#FFFFFF" fill-opacity=".6"/>')


def _lobe(cx, cy, length, wdt, ang, col):
    a = math.radians(ang)
    tx, ty = cx + math.cos(a) * length, cy + math.sin(a) * length
    nx, ny = -math.sin(a) * wdt, math.cos(a) * wdt
    c1 = (cx + math.cos(a) * length * .7 + nx, cy + math.sin(a) * length * .7 + ny)
    c2 = (cx + math.cos(a) * length * .7 - nx, cy + math.sin(a) * length * .7 - ny)
    return (f'<path d="M{cx} {cy}C{c1[0]:.1f} {c1[1]:.1f} {tx + nx * .9:.1f} {ty + ny * .9:.1f} {tx:.1f} {ty:.1f}'
            f'C{tx - nx * .9:.1f} {ty - ny * .9:.1f} {c2[0]:.1f} {c2[1]:.1f} {cx} {cy}z" fill="{col}" '
            f'fill-opacity=".85"/>')


def quantum(th):
    W = 1226
    top = 122
    rh = 86
    H = top + 4 * (rh + 12) + 24 + 250
    out = [header(W, th, "QUANTUM NUMBERS", "Four numbers describe the address of every electron in an atom")]
    for i, (sym, name, values, desc, col) in enumerate(QN):
        y = top + i * (rh + 12)
        out.append(_card(MX, y, W - 2 * MX, rh, th, rx=12))
        out.append(f'<rect x="{MX + 18}" y="{y + 14}" width="{rh - 28 + 30}" height="{rh - 28}" rx="12" '
                   f'fill="{col}"/>')
        out.append(chem(sym, MX + 18 + (rh + 2) / 2, y + rh / 2 + 10, 28, "#FFFFFF", "middle"))
        out.append(fit_text(name, MX + 130, y + 38, 20, th["ink"], 230, anchor="start"))
        out.append(fit_text(values, MX + 130, y + 66, 15, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3),
                            230, anchor="start"))
        bx = MX + 390
        out.append(f'<rect x="{bx}" y="{y + 14}" width="{W - MX - 18 - bx}" height="{rh - 28}" rx="10" '
                   f'fill="{mix(th["card"], col, .14)}"/>')
        out.append(fit_text(desc, bx + 22, y + rh / 2 + 6, 17, th["ink"], W - MX - 62 - bx, "SemiBold",
                            anchor="start"))
    y = top + 4 * (rh + 12) + 12
    out.append(_card(MX, y, W - 2 * MX, 238, th))
    out.append(text("Orbital shapes", W / 2, y + 36, 18, th["ink"]))
    cw = (W - 2 * MX) / 4
    for k, (lab, info, col) in enumerate((("s", "l = 0 · 1 orbital", T), ("p", "l = 1 · 3 orbitals", O),
                                          ("d", "l = 2 · 5 orbitals", P), ("f", "l = 3 · 7 orbitals", R))):
        cx, cy = MX + cw * k + cw / 2, y + 122
        out.append(f'<circle cx="{cx}" cy="{cy}" r="62" fill="{th["plate"]}"/>')
        if lab == "s":
            out.append(_orbital_s(cx, cy, 34, col))
        elif lab == "p":
            out.append(_lobe(cx, cy, 52, 22, -90, col) + _lobe(cx, cy, 52, 22, 90, col))
        elif lab == "d":
            out.append("".join(_lobe(cx, cy, 50, 18, a, col) for a in (-135, -45, 45, 135)))
        else:
            out.append("".join(_lobe(cx, cy, 50, 12, a, col) for a in range(0, 360, 60)))
        out.append(f'<circle cx="{cx}" cy="{cy}" r="4" fill="#1E2A3A"/>')
        out.append(text(lab, cx, y + 210, 20, th["ink"]))
        out.append(text(info, cx, y + 230, 12.5, th["sub"], "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("molecular-shapes-vsepr", vsepr, "Molecular shapes VSEPR chart, linear, tetrahedral, bent, octahedral geometry",
     ["vsepr", "molecular geometry", "molecular shape", "linear", "trigonal planar", "tetrahedral", "bent",
      "trigonal pyramidal", "octahedral", "bond angle", "lone pair", "methane", "water molecule", "ammonia"]),
    ("quantum-numbers", quantum, "Quantum numbers chart with s, p, d and f orbital shapes",
     ["quantum numbers", "principal quantum number", "azimuthal", "magnetic quantum number", "spin", "orbital",
      "s orbital", "p orbital", "d orbital", "f orbital", "electron", "atomic structure", "shell", "subshell"]),
]

TR.update({
    "MOLECULAR SHAPES (VSEPR)": "BENTUK MOLEKUL (VSEPR)",
    "Electron pairs around the central atom repel each other and set the shape of the molecule":
        "Pasangan elektron di sekitar atom pusat saling tolak-menolak dan menentukan bentuk molekul",
    "Linear": "Linear", "Trigonal planar": "Segitiga datar", "Tetrahedral": "Tetrahedral",
    "Trigonal pyramidal": "Piramida segitiga", "Bent": "Bentuk V (bengkok)",
    "Trigonal bipyramidal": "Bipiramida segitiga", "Octahedral": "Oktahedral", "Square planar": "Segi empat datar",
    "A = central atom · X = bonded atom · E = lone pair · dashed = behind the page, thick = in front":
        "A = atom pusat · X = atom terikat · E = pasangan elektron bebas · putus-putus = di belakang, tebal = di depan",
    "QUANTUM NUMBERS": "BILANGAN KUANTUM",
    "Four numbers describe the address of every electron in an atom":
        "Empat bilangan yang menyatakan \"alamat\" setiap elektron dalam atom",
    "Principal": "Utama", "Azimuthal": "Azimut", "Magnetic": "Magnetik", "Spin": "Spin",
    "1, 2, 3, …": "1, 2, 3, …", "+1/2 or −1/2": "+1/2 atau −1/2",
    "Shell: energy level and size of the orbital": "Kulit: tingkat energi dan ukuran orbital",
    "Subshell shape: 0 = s, 1 = p, 2 = d, 3 = f": "Bentuk subkulit: 0 = s, 1 = p, 2 = d, 3 = f",
    "Orientation of the orbital in space": "Orientasi orbital dalam ruang",
    "Spin direction of the electron (↑ or ↓)": "Arah putaran elektron (↑ atau ↓)",
    "Orbital shapes": "Bentuk orbital", "l = 0 · 1 orbital": "l = 0 · 1 orbital",
    "l = 1 · 3 orbitals": "l = 1 · 3 orbital", "l = 2 · 5 orbitals": "l = 2 · 5 orbital",
    "l = 3 · 7 orbitals": "l = 3 · 7 orbital",
})
