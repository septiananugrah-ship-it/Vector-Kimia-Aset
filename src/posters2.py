"""Poster edukasi kimia jilid 2: gugus fungsi organik, deret alkana, struktur
atom, jenis ikatan kimia, dan aturan keselamatan laboratorium.

Didaftarkan ke posters.py lewat POSTERS, jadi ikut dibuat dalam 2 tema x 2 bahasa.
"""
import math

import icons_lab2
import icons_lab_flat
from icons_lab_flat import L, O, P, R
from poster_kit import MX, fit_text, header, icon_at, particle, text, tr
from render import style_attrs
from textpath import formula, width

EL_COLOR = {"O": R, "N": "#3D7DDB", "X": L, "Cl": L}


def _card(x, y, w, h, th, rx=14):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{th["card"]}" '
            f'stroke="{th["card_stroke"]}" stroke-width="1.2"/>')


# ------------------------------------------------------------ gugus fungsi

def structure(nodes, bonds, cx, cy, unit, th, ring=None):
    """Rumus struktur: nodes = [(label, x, y)], bonds = [(i, j, orde)] dalam satuan `unit`."""
    xs = [n[1] for n in nodes]
    ys = [n[2] for n in nodes]
    if ring:
        xs += [ring[0] - ring[2], ring[0] + ring[2]]
        ys += [ring[1] - ring[2], ring[1] + ring[2]]
    ox = cx - (min(xs) + max(xs)) / 2 * unit
    oy = cy - (min(ys) + max(ys)) / 2 * unit
    P_ = [(lab, ox + x * unit, oy + y * unit) for lab, x, y in nodes]
    out = []
    col = th["ink"]
    for i, j, order in bonds:
        (_, x1, y1), (_, x2, y2) = P_[i], P_[j]
        d = math.hypot(x2 - x1, y2 - y1)
        ux, uy = (x2 - x1) / d, (y2 - y1) / d
        trim1 = 11 if P_[i][0] else 0
        trim2 = 11 if P_[j][0] else 0
        a = (x1 + ux * trim1, y1 + uy * trim1)
        b = (x2 - ux * trim2, y2 - uy * trim2)
        offs = {1: [0], 2: [-3.2, 3.2], 3: [-4.6, 0, 4.6]}[order]
        for o in offs:
            out.append(f'<path d="M{a[0] - uy * o:.2f} {a[1] + ux * o:.2f}L{b[0] - uy * o:.2f} {b[1] + ux * o:.2f}" '
                       f'stroke="{col}" stroke-width="2.4" stroke-linecap="round" fill="none"/>')
    if ring:
        rx, ry, rr = ox + ring[0] * unit, oy + ring[1] * unit, ring[2] * unit
        pts = [(rx + rr * math.cos(math.radians(60 * k)), ry + rr * math.sin(math.radians(60 * k)))
               for k in range(6)]
        out.append('<path d="M' + "L".join(f"{x:.2f} {y:.2f}" for x, y in pts) + f'z" stroke="{col}" '
                   'stroke-width="2.4" fill="none" stroke-linejoin="round"/>'
                   f'<circle cx="{rx:.2f}" cy="{ry:.2f}" r="{rr * .55:.2f}" stroke="{col}" stroke-width="2.2" fill="none"/>')
    for lab, x, y in P_:
        if not lab:
            continue
        c = EL_COLOR.get(lab[0] if lab[0] in "ONX" else lab, None)
        if lab.startswith("R"):
            c = th["accent"]
        elif lab in ("C",):
            c = th["ink"]
        elif lab == "H":
            c = th["sub"]
        out.append(text(lab, x, y + 6, 17, c or th["ink"]))
    return "".join(out)


FG = [
    ("Alcohol", "R–OH", "Ethanol", [("R", 0, 0), ("O", 1, 0), ("H", 2, 0)], [(0, 1, 1), (1, 2, 1)]),
    ("Ether", "R–O–R'", "Diethyl ether", [("R", 0, 0), ("O", 1, 0), ("R'", 2, 0)], [(0, 1, 1), (1, 2, 1)]),
    ("Aldehyde", "R–CHO", "Methanal", [("R", 0, 0), ("C", 1, 0), ("O", 1.6, -.8), ("H", 1.6, .8)],
     [(0, 1, 1), (1, 2, 2), (1, 3, 1)]),
    ("Ketone", "R–CO–R'", "Acetone", [("R", 0, 0), ("C", 1, 0), ("R'", 2, 0), ("O", 1, -1)],
     [(0, 1, 1), (1, 2, 1), (1, 3, 2)]),
    ("Carboxylic acid", "R–COOH", "Acetic acid",
     [("R", 0, 0), ("C", 1, 0), ("O", 1.6, -.8), ("O", 1.6, .8), ("H", 2.5, .8)],
     [(0, 1, 1), (1, 2, 2), (1, 3, 1), (3, 4, 1)]),
    ("Ester", "R–COO–R'", "Ethyl acetate",
     [("R", 0, 0), ("C", 1, 0), ("O", 1.6, -.8), ("O", 1.6, .8), ("R'", 2.6, .8)],
     [(0, 1, 1), (1, 2, 2), (1, 3, 1), (3, 4, 1)]),
    ("Amine", "R–NH2", "Methylamine", [("R", 0, 0), ("N", 1, 0), ("H", 1.6, -.8), ("H", 1.6, .8)],
     [(0, 1, 1), (1, 2, 1), (1, 3, 1)]),
    ("Amide", "R–CONH2", "Acetamide",
     [("R", 0, 0), ("C", 1, 0), ("O", 1, -1), ("N", 2, 0), ("H", 2.6, -.8), ("H", 2.6, .8)],
     [(0, 1, 1), (1, 2, 2), (1, 3, 1), (3, 4, 1), (3, 5, 1)]),
    ("Alkene", "CnH2n", "Ethene",
     [("R", -.6, -.8), ("R", -.6, .8), ("C", 0, 0), ("C", 1, 0), ("R", 1.6, -.8), ("R", 1.6, .8)],
     [(0, 2, 1), (1, 2, 1), (2, 3, 2), (3, 4, 1), (3, 5, 1)]),
    ("Alkyne", "CnH2n–2", "Ethyne", [("R", -1, 0), ("C", 0, 0), ("C", 1, 0), ("R'", 2, 0)],
     [(0, 1, 1), (1, 2, 3), (2, 3, 1)]),
    ("Haloalkane", "R–X", "Chloromethane", [("R", 0, 0), ("X", 1, 0)], [(0, 1, 1)]),
    ("Arene (aromatic)", "C6H5–R", "Toluene", [("", .62, 0), ("R", 1.5, 0)], [(0, 1, 1)]),
]


def functional_groups(th):
    cols, cw, ch, gap = 4, 270, 200, 14
    W = cols * (cw + gap) - gap + 2 * MX
    top = 122
    rows = -(-len(FG) // cols)
    H = top + rows * (ch + gap) - gap + 44
    out = [header(W, th, "ORGANIC FUNCTIONAL GROUPS",
                  "Structural formulas of 12 important functional groups with examples")]
    for i, (name, gen, ex, nodes, bonds) in enumerate(FG):
        x = MX + (i % cols) * (cw + gap)
        y = top + (i // cols) * (ch + gap)
        out.append(_card(x, y, cw, ch, th))
        out.append(fit_text(name, x + 18, y + 34, 18, th["ink"], cw - 36, anchor="start"))
        out.append(formula(gen, x + 18, y + 56, 14, th["accent"], anchor="start"))
        ring = (0, 0, .62) if name.startswith("Arene") else None
        unit = 44
        out.append(structure(nodes, bonds, x + cw / 2, y + 116, unit, th, ring=ring))
        out.append(text(f"{tr('Example')}: {tr(ex)}", x + 18, y + ch - 16, 11.5, th["sub"], "Regular", "start"))
    out.append(text("R = alkyl group  ·  X = halogen (F, Cl, Br, I)", W / 2, H - 16, 11, th["sub"], "Regular"))
    return W, H, "".join(out)


# ------------------------------------------------------------ deret alkana

ALKANES = [("Methane", -162), ("Ethane", -89), ("Propane", -42), ("Butane", -1), ("Pentane", 36),
           ("Hexane", 69), ("Heptane", 98), ("Octane", 126), ("Nonane", 151), ("Decane", 174)]


def alkanes(th):
    cols, cw, ch, gap = 5, 220, 214, 14
    W = cols * (cw + gap) - gap + 2 * MX
    top = 122
    H = top + 2 * (ch + gap) - gap + 46
    out = [header(W, th, "ALKANE HOMOLOGOUS SERIES",
                  "The first ten straight-chain alkanes with formulas, carbon chains and boiling points")]
    carbon = "#4A4F5C"
    for i, (name, bp) in enumerate(ALKANES):
        n = i + 1
        x = MX + (i % cols) * (cw + gap)
        y = top + (i // cols) * (ch + gap)
        out.append(_card(x, y, cw, ch, th))
        out.append(f'<rect x="{x + 8}" y="{y + 8}" width="{cw - 16}" height="86" rx="10" fill="{th["plate"]}"/>')
        # rantai karbon zig-zag
        sp = min(30, (cw - 50) / max(n - 1, 1))
        x0 = x + cw / 2 - sp * (n - 1) / 2
        pts = [(x0 + k * sp, y + 51 + (8 if k % 2 else -8) * (n > 1)) for k in range(n)]
        r = 10 if n < 8 else 8.5
        chain = "".join(f'<path d="M{a[0]:.2f} {a[1]:.2f}L{b[0]:.2f} {b[1]:.2f}" stroke="#9AA5B1" stroke-width="4" '
                        'stroke-linecap="round"/>' for a, b in zip(pts, pts[1:]))
        chain += "".join(particle(px, py, r, carbon, f"alk{n}-{k}") for k, (px, py) in enumerate(pts))
        out.append(f'<g {style_attrs(1.4)}>{chain}</g>')
        f = "CH4" if n == 1 else f"C{n}H{2 * n + 2}"
        out.append(text(name, x + cw / 2, y + 124, 18, th["ink"]))
        out.append(formula(f, x + cw / 2, y + 148, 16, th["accent"]))
        sign = "−" if bp < 0 else ""
        out.append(text(f"{tr('Boiling point')}: {sign}{abs(bp)} °C", x + cw / 2, y + 172, 11, th["sub"], "Regular"))
        phase = "Gas" if n <= 4 else "Liquid"
        pc = O if phase == "Gas" else "#2E9BDA"
        label = tr(phase)
        pw = width(label, 10.5, "SemiBold") + 20
        out.append(f'<rect x="{x + cw / 2 - pw / 2:.2f}" y="{y + 182}" width="{pw:.2f}" height="20" rx="10" fill="{pc}"/>')
        out.append(text(label, x + cw / 2, y + 196, 10.5, "#FFFFFF", "SemiBold"))
    out.append(text("General formula CnH2n+2  ·  state at room temperature (25 °C)", W / 2, H - 16, 11, th["sub"],
                    "Regular"))
    return W, H, "".join(out)


# ------------------------------------------------------------ struktur atom

def _sign(cx, cy, s, col, minus=False):
    d = f"M{cx - s:.2f} {cy:.2f}h{2 * s:.2f}" + ("" if minus else f"M{cx:.2f} {cy - s:.2f}v{2 * s:.2f}")
    return f'<path d="{d}" stroke="{col}" stroke-width="{s * .55:.2f}" stroke-linecap="round" fill="none"/>'


def atom_structure(th):
    W, H = 1226, 720
    cx, cy = 300, 420
    out = [header(W, th, "STRUCTURE OF AN ATOM",
                  "Protons, neutrons and electrons in a carbon-12 atom (6 protons, 6 neutrons, 6 electrons)")]
    blue = "#3D7DDB"
    out.append(f'<circle cx="{cx}" cy="{cy}" r="110" fill="none" stroke="{th["sub"]}" stroke-width="2" '
               'stroke-dasharray="6 5"/>'
               f'<circle cx="{cx}" cy="{cy}" r="190" fill="none" stroke="{th["sub"]}" stroke-width="2" '
               'stroke-dasharray="6 5"/>')
    # inti: 12 bola dari kisi heksagonal, terdekat ke pusat
    r = 19
    lat = []
    for i in range(-3, 4):
        for j in range(-3, 4):
            px = (i + j * .5) * r * 1.75
            py = j * r * 1.75 * math.sqrt(3) / 2
            lat.append((math.hypot(px, py), px, py))
    lat = sorted(lat)[:12]
    mx_ = sum(p[1] for p in lat) / 12
    my_ = sum(p[2] for p in lat) / 12
    lat = [(d, px - mx_, py - my_) for d, px, py in lat]  # pusatkan gugus inti
    nuc, protons, neutrons = [], [], []
    for k, (_, px, py) in enumerate(sorted(lat, key=lambda t: -t[0])):
        proton = k % 2 == 0
        (protons if proton else neutrons).append((cx + px, cy + py))
        nuc.append(particle(cx + px, cy + py, r, R if proton else "#9AA5B1", f"n{k}", shine=False))
        nuc.append(_sign(cx + px, cy + py, 6.5, "#FFFFFF") if proton else
                   f'<circle cx="{cx + px:.2f}" cy="{cy + py:.2f}" r="3" fill="#FFFFFF" stroke="none"/>')
    elec = []
    epos = [(110, a) for a in (-90, 90)] + [(190, a) for a in (-10, 80, 170, 260)]
    for k, (rr, a) in enumerate(epos):
        ex, ey = cx + rr * math.cos(math.radians(a)), cy + rr * math.sin(math.radians(a))
        elec.append(particle(ex, ey, 13, blue, f"e{k}", shine=False) + _sign(ex, ey, 5, "#FFFFFF", minus=True))
    out.append(f'<circle cx="{cx}" cy="{cy}" r="74" fill="none" stroke="{th["accent"]}" stroke-width="2" '
               'stroke-dasharray="3 4"/>')
    out.append(f'<g {style_attrs(1.6)}>' + "".join(nuc) + "".join(elec) + "</g>")
    # label penunjuk
    lab_x = 540
    marks = [
        ("Electron shell", "energy level of the electrons", (cx + 190 * math.cos(math.radians(-40)),
                                                             cy + 190 * math.sin(math.radians(-40))), 200),
        ("Electron", "negative charge (−)", (cx + 190 * math.cos(math.radians(-10)) + 12,
                                              cy + 190 * math.sin(math.radians(-10))), 300),
        ("Nucleus", "contains protons and neutrons", (cx + 74 * math.cos(math.radians(-35)),
                                                       cy + 74 * math.sin(math.radians(-35))), 420),
        ("Proton", "positive charge (+)", max(protons, key=lambda q: q[0] + q[1]), 520),
        ("Neutron", "no charge (0)", max(neutrons, key=lambda q: q[0] + q[1]), 610),
    ]
    for name, desc, (tx, ty), ly in marks:
        out.append(f'<path d="M{tx:.2f} {ty:.2f}L{lab_x - 30} {ly - 5}H{lab_x - 8}" stroke="{th["accent"]}" '
                   'stroke-width="1.6" fill="none"/>'
                   f'<circle cx="{tx:.2f}" cy="{ty:.2f}" r="3.5" fill="{th["accent"]}"/>')
        out.append(text(name, lab_x, ly, 16, th["ink"], "Bold", "start"))
        out.append(text(desc, lab_x, ly + 17, 11, th["sub"], "Regular", "start"))
    # tabel partikel
    tx0, ty0, tw = 790, 190, W - MX - 790
    colw = [0, .27, .47, .72]
    rows = [("Particle", "Charge", "Relative mass", "Location"),
            ("Proton", "+1", "1", "Nucleus"), ("Neutron", "0", "1", "Nucleus"),
            ("Electron", "−1", "1/1836", "Electron shell")]
    out.append(_card(tx0, ty0, tw, 4 * 44 + 10, th))
    for k, row in enumerate(rows):
        y = ty0 + 34 + k * 44
        if k:
            out.append(f'<path d="M{tx0 + 14} {y - 28}H{tx0 + tw - 14}" stroke="{th["card_stroke"]}" stroke-width="1.2"/>')
        for c, cell in enumerate(row):
            col = th["accent"] if k == 0 else [R, "#9AA5B1", blue][k - 1] if c == 0 else th["ink"]
            out.append(fit_text(cell, tx0 + 18 + colw[c] * (tw - 30), y, 13 if k else 12, col,
                                (colw[c + 1] - colw[c]) * (tw - 30) - 8 if c < 3 else (1 - colw[3]) * (tw - 30) - 4,
                                "Bold" if k == 0 or c == 0 else "SemiBold", anchor="start"))
    fy = ty0 + 4 * 44 + 40
    for k, (a, b) in enumerate((("Atomic number (Z)", "= number of protons"),
                                ("Mass number (A)", "= protons + neutrons"))):
        y = fy + k * 70
        out.append(_card(tx0, y, tw, 58, th, rx=12))
        out.append(text(a, tx0 + 20, y + 36, 16, th["accent"], "Bold", "start"))
        out.append(text(b, tx0 + 20 + width(tr(a), 16, "Bold") + 10, y + 36, 15, th["ink"], "SemiBold", "start"))
    out.append(text("For carbon-12: Z = 6, A = 12", tx0 + tw / 2, fy + 160, 12, th["sub"], "Regular"))
    return W, H, "".join(out)


# ------------------------------------------------------------ ikatan kimia

def _ion(label, charge, x, y, size, col):
    w = width(label, size, "Bold")
    s = text(label, x, y, size, col)
    sx, sy = x + w / 2 + size * .28, y - size * .62
    return s + _sign(sx, sy, size * .17, col, minus=charge < 0)


def bonding(th):
    W, cw, ch, gap = 1226, 366, 470, 18
    top = 122
    H = top + ch + 40
    blue = "#3D7DDB"
    out = [header(W, th, "TYPES OF CHEMICAL BONDS",
                  "Ionic, covalent and metallic bonding explained with particle models")]
    titles = [("Ionic bond", "Electrons are transferred from a metal to a nonmetal", "Example: NaCl (table salt)"),
              ("Covalent bond", "Electron pairs are shared between nonmetal atoms", "Example: H2, H2O, CH4"),
              ("Metallic bond", "Metal ions in a sea of delocalized electrons", "Example: Cu, Fe, Al")]
    for k, (name, desc, ex) in enumerate(titles):
        x = MX + k * (cw + gap)
        out.append(_card(x, top, cw, ch, th))
        out.append(f'<rect x="{x + 10}" y="{top + 10}" width="{cw - 20}" height="300" rx="10" fill="{th["plate"]}"/>')
        out.append(text(name, x + cw / 2, top + 352, 22, th["ink"]))
        out.append(fit_text(desc, x + cw / 2, top + 380, 12, th["sub"], cw - 30, "Regular"))
        ex_t = tr(ex.split(":")[0]) + ":" + ex.split(":", 1)[1]
        if "NaCl" in ex:
            ex_t = ex_t.replace("table salt", tr("table salt"))
        out.append(formula(ex_t, x + cw / 2, top + 420, 14, th["accent"]))
    ink = "#1E2A3A"
    g = []
    # ion
    x = MX
    cy = top + 110
    g.append(particle(x + 110, cy, 34, P, "na", shine=False) + text("Na", x + 110, cy + 7, 20, "#FFFFFF"))
    g.append(particle(x + 250, cy, 44, L, "cl", shine=False) + text("Cl", x + 250, cy + 7, 22, "#FFFFFF"))
    g.append(f'<path d="M{x + 130} {cy - 40}Q{x + 180} {cy - 95} {x + 228} {cy - 52}" stroke="{blue}" '
             'stroke-width="3" fill="none" stroke-dasharray="6 5"/>'
             f'<path d="M{x + 232} {cy - 46}l-12-2 6-9z" fill="{blue}" stroke="{blue}"/>')
    g.append(particle(x + 180, cy - 82, 9, blue, "ie", shine=False) + _sign(x + 180, cy - 82, 4, "#FFFFFF", True))
    y2 = top + 245
    g.append(f'<path d="M{x + 183} {top + 165}v28" stroke="{ink}" stroke-width="3"/>'
             f'<path d="M{x + 183} {top + 200}l-7-10h14z" fill="{ink}" stroke="{ink}"/>')
    g.append(particle(x + 120, y2, 32, P, "na2", shine=False) + _ion("Na", 1, x + 120, y2 + 7, 19, "#FFFFFF"))
    g.append(particle(x + 248, y2, 46, L, "cl2", shine=False) + _ion("Cl", -1, x + 244, y2 + 7, 21, "#FFFFFF"))
    # kovalen: dua atom H berbagi pasangan elektron
    x = MX + cw + gap
    cy = top + 150
    for dx in (-48, 48):
        g.append(f'<circle cx="{x + cw / 2 + dx}" cy="{cy}" r="70" fill="none" stroke="{blue}" stroke-width="2.4" '
                 'stroke-dasharray="7 5"/>')
        g.append(particle(x + cw / 2 + dx * 1.5, cy, 20, R, f"h{dx}", shine=False) +
                 text("H", x + cw / 2 + dx * 1.5, cy + 7, 19, "#FFFFFF"))
    for dy in (-14, 14):
        g.append(particle(x + cw / 2, cy + dy, 8, blue, f"sp{dy}", shine=False))
    g.append(text("H–H", x + cw / 2, top + 270, 26, ink))
    # logam: ion positif dalam lautan elektron
    x = MX + 2 * (cw + gap)
    for i in range(4):
        for j in range(3):
            px, py = x + 70 + i * 76, top + 75 + j * 82
            g.append(particle(px, py, 24, O, f"m{i}{j}", shine=False) + _sign(px, py, 7, "#FFFFFF"))
    for i in range(5):
        for j in range(4):
            px = x + 32 + i * 76 + ((i * 7 + j * 3) % 5 - 2) * 3
            py = top + 34 + j * 82 + ((i * 5 + j * 11) % 5 - 2) * 3
            g.append(particle(px, py, 6.5, blue, f"md{i}{j}", shine=False))
    out.append(f'<g {style_attrs(1.5)}>' + "".join(g) + "</g>")
    return W, H, "".join(out)


# ------------------------------------------------------------ keselamatan lab

SAFETY = [
    ("Wear safety goggles", "Protect your eyes from splashes and fumes", "safety-goggles"),
    ("Wear a lab coat", "Keep chemicals off your skin and clothes", "lab-coat"),
    ("Wear protective gloves", "Never touch chemicals with bare hands", "protective-gloves"),
    ("Read every label", "Check hazard warnings before using a chemical", "toxic-chemical-bottle"),
    ("Never leave a flame unattended", "Turn off burners as soon as you are done", "bunsen-burner"),
    ("Point test tubes away", "Never aim a heated test tube at anyone", "test-tube"),
    ("Use a spatula", "Transfer solids with clean tools, not fingers", "spatula"),
    ("Know the fire extinguisher", "Learn where all safety equipment is located", "fire-extinguisher"),
    ("Clean up spills", "Report and clean any spill immediately", "wash-bottle"),
    ("Record your work", "Follow instructions and write down every result", "clipboard-notes"),
]


def lab_safety(th):
    cols, cw, ch, gap = 2, 560, 96, 14
    W = cols * (cw + gap) - gap + 2 * MX
    top = 122
    H = top + 5 * (ch + gap) - gap + 40
    icons = {ic["id"]: (ic["body"], m.STROKE) for m in (icons_lab_flat, icons_lab2) for ic in m.ICONS}
    out = [header(W, th, "LABORATORY SAFETY RULES", "Ten essential rules for working safely in the chemistry lab")]
    for i, (rule, desc, icon) in enumerate(SAFETY):
        x = MX + (i % cols) * (cw + gap)
        y = top + (i // cols) * (ch + gap)
        out.append(_card(x, y, cw, ch, th))
        out.append(f'<rect x="{x + 8}" y="{y + 8}" width="80" height="80" rx="10" fill="{th["plate"]}"/>')
        body, stroke = icons[icon]
        out.append(icon_at(body, stroke, x + 16, y + 16, 64))
        out.append(f'<circle cx="{x + 118}" cy="{y + ch / 2}" r="16" fill="{th["accent"]}"/>'
                   + text(str(i + 1), x + 118, y + ch / 2 + 6, 16, "#FFFFFF"))
        out.append(fit_text(rule, x + 146, y + 44, 18, th["ink"], cw - 160, anchor="start"))
        out.append(fit_text(desc, x + 146, y + 66, 12, th["sub"], cw - 160, "Regular", anchor="start"))
    return W, H, "".join(out)


POSTERS = [
    ("functional-groups", functional_groups, "Organic chemistry functional groups chart with structural formulas",
     ["functional groups", "organic chemistry", "structural formula", "alcohol", "aldehyde", "ketone",
      "carboxylic acid", "ester", "amine", "amide", "alkene", "alkyne", "ether", "haloalkane", "benzene"]),
    ("alkanes", alkanes, "Alkane homologous series chart, methane to decane with formulas and boiling points",
     ["alkane", "alkanes", "homologous series", "hydrocarbon", "methane", "ethane", "propane", "butane",
      "octane", "organic chemistry", "carbon chain", "boiling point", "fuel", "petroleum"]),
    ("atom-structure", atom_structure, "Structure of an atom diagram with protons, neutrons and electrons",
     ["atom", "atomic structure", "proton", "neutron", "electron", "nucleus", "electron shell", "atomic number",
      "mass number", "carbon", "physics", "subatomic particles", "particle", "model"]),
    ("chemical-bonds", bonding, "Types of chemical bonds diagram, ionic, covalent and metallic bonding",
     ["chemical bond", "ionic bond", "covalent bond", "metallic bond", "electron transfer", "shared electrons",
      "sodium chloride", "ion", "electrons", "atoms", "molecule", "physics", "bonding", "nacl"]),
    ("lab-safety", lab_safety, "Laboratory safety rules poster with ten illustrated rules",
     ["lab safety", "safety rules", "laboratory rules", "safety", "goggles", "lab coat", "gloves", "ppe",
      "fire extinguisher", "hazard", "warning", "rules", "school lab", "precautions"]),
]
