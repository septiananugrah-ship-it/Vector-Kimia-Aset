"""Poster edukasi kimia jilid 4: faktor laju reaksi, diagram energi
eksoterm/endoterm, sel Volta (Daniell), dan konsep mol.

Didaftarkan ke posters.py lewat POSTERS (2 tema x 2 bahasa).
"""
import math
import random

import poster_kit
from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, particle, text, tr
from posters2 import _card
from posters3 import arrow_line, mix
from render import style_attrs
from textpath import text as raw_text
from textpath import width

COPPER = "#C8733A"
ZINC = "#9AA5B1"


def rich(tokens, x, y, size, fill, anchor="start", weight="Bold"):
    """Teks campuran: tokens = [(teks, 'n'|'sup'|'sub')]."""
    runs = []
    for t, kind in tokens:
        sz = size * (.62 if kind != "n" else 1)
        dy = -size * .42 if kind == "sup" else size * .24 if kind == "sub" else 0
        runs.append((t, sz, dy))
    total = sum(width(t, sz, weight) for t, sz, _ in runs)
    cx = x - (total / 2 if anchor == "middle" else total if anchor == "end" else 0)
    out = []
    for t, sz, dy in runs:
        out.append(raw_text(t, cx, y + dy, sz, fill, weight, "start"))
        cx += width(t, sz, weight)
    return "".join(out)


def parse(s):
    """Notasi singkat: ^{..} superskrip, _{..} subskrip. Contoh: 'Zn^{2+} + 2e^{−}'."""
    out, i, buf = [], 0, ""
    while i < len(s):
        if s[i] in "^_" and i + 1 < len(s) and s[i + 1] == "{":
            if buf:
                out.append((buf, "n"))
                buf = ""
            j = s.index("}", i)
            out.append((s[i + 2:j], "sup" if s[i] == "^" else "sub"))
            i = j + 1
        else:
            buf += s[i]
            i += 1
    if buf:
        out.append((buf, "n"))
    return out


def loc(s):
    """Desimal pakai koma di versi Indonesia."""
    return s.replace(".", ",") if poster_kit._lang[0] == "id" else s


def chem(s, x, y, size, fill, anchor="start", weight="Bold"):
    return rich(parse(s), x, y, size, fill, anchor, weight)


# ------------------------------------------------------------ laju reaksi

def _box_particles(x, y, w, h, n, col, seed, trail, th, r=8):
    rnd = random.Random(seed)
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{th["plate"]}"/>']
    placed, tries = [], 0
    while len(placed) < n and tries < 4000:
        tries += 1
        px, py = rnd.uniform(x + r + 8, x + w - r - 8), rnd.uniform(y + r + 8, y + h - r - 8)
        if all(math.hypot(px - a, py - b) > 2.6 * r for a, b in placed):
            placed.append((px, py))
    for k, (px, py) in enumerate(placed):
        if trail:
            a = rnd.uniform(0, 2 * math.pi)
            tx, ty = math.cos(a), math.sin(a)
            out.append(f'<path d="M{px - tx * (r + 3):.1f} {py - ty * (r + 3):.1f}L{px - tx * (r + 3 + trail):.1f} '
                       f'{py - ty * (r + 3 + trail):.1f}" stroke="#7C8B9C" stroke-width="2.2" stroke-linecap="round"/>')
        out.append(particle(px, py, r, col, f"rr{seed}{k}", shine=False))
    return "".join(out)


def reaction_rate(th):
    W = 1226
    top = 122
    cw = (W - 2 * MX - 24) / 2
    ch = 320
    H = top + 2 * (ch + 24) + 10
    out = [header(W, th, "FACTORS AFFECTING REACTION RATE",
                  "Temperature, concentration, surface area and catalysts change how fast a reaction happens")]
    cards = [
        ("Temperature", "Higher temperature: particles move faster and collide more often"),
        ("Concentration", "Higher concentration: more particles in the same space, more collisions"),
        ("Surface area", "Smaller pieces: more surface exposed for particles to react"),
        ("Catalyst", "A catalyst lowers the activation energy without being used up"),
    ]
    for k, (name, desc) in enumerate(cards):
        x = MX + (k % 2) * (cw + 24)
        y = top + (k // 2) * (ch + 24)
        out.append(_card(x, y, cw, ch, th))
        out.append(text(name, x + 22, y + 36, 20, th["ink"], "Bold", "start"))
        out.append(fit_text(desc, x + 22, y + ch - 20, 12, th["sub"], cw - 44, "Regular", anchor="start"))
        bw, bh = (cw - 44 - 60) / 2, 190
        bx1, bx2, by = x + 22, x + 22 + bw + 60, y + 56
        g = []
        if k == 0:
            g.append(_box_particles(bx1, by, bw, bh, 9, T, 1, 6, th))
            g.append(_box_particles(bx2, by, bw, bh, 9, R, 2, 22, th))
            labels = ("Low", "High")
        elif k == 1:
            g.append(_box_particles(bx1, by, bw, bh, 5, P, 3, 0, th))
            g.append(_box_particles(bx2, by, bw, bh, 18, P, 4, 0, th))
            labels = ("Low", "High")
        elif k == 2:
            g.append(f'<rect x="{bx1}" y="{by}" width="{bw}" height="{bh}" rx="10" fill="{th["plate"]}"/>')
            s = 80
            g.append(f'<rect x="{bx1 + bw / 2 - s / 2}" y="{by + bh / 2 - s / 2}" width="{s}" height="{s}" rx="6" '
                     f'fill="{O}" stroke="#1E2A3A" stroke-width="2"/>')
            g.append(f'<rect x="{bx2}" y="{by}" width="{bw}" height="{bh}" rx="10" fill="{th["plate"]}"/>')
            s2 = 26
            for i in range(3):
                for j in range(3):
                    g.append(f'<rect x="{bx2 + bw / 2 - 52 + i * 38:.1f}" y="{by + bh / 2 - 52 + j * 38:.1f}" '
                             f'width="{s2}" height="{s2}" rx="4" fill="{O}" stroke="#1E2A3A" stroke-width="2"/>')
            labels = ("Large lump", "Small pieces")
        else:
            g.append(f'<rect x="{bx1}" y="{by}" width="{2 * bw + 60}" height="{bh}" rx="10" fill="{th["plate"]}"/>')
            gx, gy, gw, gh = bx1 + 40, by + 20, 2 * bw - 20, bh - 50
            g.append(f'<path d="M{gx} {gy}V{gy + gh}H{gx + gw}" stroke="#1E2A3A" stroke-width="2" fill="none"/>')
            base, prod = gy + gh * .62, gy + gh * .85

            def hump(peak, col, dash=""):
                return (f'<path d="M{gx + 10} {base}C{gx + gw * .3} {base} {gx + gw * .35} {peak} {gx + gw * .5} {peak}'
                        f'S{gx + gw * .7} {prod} {gx + gw - 10} {prod}" stroke="{col}" stroke-width="3.4" fill="none" '
                        f'{dash}stroke-linecap="round"/>')
            g.append(hump(gy + 8, R))
            g.append(hump(gy + gh * .38, T, 'stroke-dasharray="8 6" '))
            g.append(raw_text(tr("without catalyst"), gx + gw * .5 + 50, gy + 14, 12, R, "Bold", "start"))
            g.append(raw_text(tr("with catalyst"), gx + gw * .62, gy + gh * .38 + 4, 12, T, "Bold", "start"))
            g.append(raw_text(tr("Energy"), gx + 8, gy + 4, 11, "#1E2A3A", "SemiBold", "start"))
            g.append(raw_text(tr("Reaction progress"), gx + gw, gy + gh + 18, 11, "#1E2A3A", "SemiBold", "end"))
            labels = None
        out.append(f'<g {style_attrs(1.4)}>' + "".join(g) + "</g>")
        if labels:
            out.append(raw_text(tr(labels[0]), bx1 + bw / 2, by + bh + 20, 12.5, th["ink"], "SemiBold"))
            out.append(raw_text(tr(labels[1]), bx2 + bw / 2, by + bh + 20, 12.5, th["accent"], "Bold"))
            out.append(arrow_line(bx1 + bw + 12, by + bh / 2, bx2 - 12, by + bh / 2, th["accent"], 3))
    return W, H, "".join(out)


# ------------------------------------------------------------ diagram energi

def energy_diagrams(th):
    W = 1226
    top = 122
    cw = (W - 2 * MX - 24) / 2
    ch = 540
    H = top + ch + 30
    out = [header(W, th, "EXOTHERMIC AND ENDOTHERMIC REACTIONS",
                  "Energy profile diagrams showing activation energy and enthalpy change (ΔH)")]
    data = [("Exothermic", "Energy is released to the surroundings", R, .62, .25, "ΔH < 0",
             ["Combustion of fuels", "Respiration", "Neutralization"]),
            ("Endothermic", "Energy is absorbed from the surroundings", "#2E9BDA", .25, .62, "ΔH > 0",
             ["Photosynthesis", "Melting ice", "Thermal decomposition"])]
    for k, (name, desc, col, r_lvl, p_lvl, dh, ex) in enumerate(data):
        x = MX + k * (cw + 24)
        out.append(_card(x, top, cw, ch, th))
        out.append(text(name, x + 24, top + 40, 24, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .25),
                        "Bold", "start"))
        out.append(text(desc, x + 24, top + 64, 12.5, th["sub"], "Regular", "start"))
        gx, gy, gw, gh = x + 70, top + 92, cw - 110, 270
        out.append(f'<rect x="{x + 14}" y="{gy - 14}" width="{cw - 28}" height="{gh + 54}" rx="10" fill="{th["plate"]}"/>')
        ink = "#1E2A3A"
        out.append(f'<path d="M{gx} {gy}V{gy + gh}H{gx + gw}" stroke="{ink}" stroke-width="2.4" fill="none"/>')
        yr, yp = gy + gh * (1 - r_lvl), gy + gh * (1 - p_lvl)
        ypk = gy + 22
        out.append(f'<path d="M{gx + 10} {yr}H{gx + gw * .25}C{gx + gw * .38} {yr} {gx + gw * .4} {ypk} {gx + gw * .5} {ypk}'
                   f'S{gx + gw * .62} {yp} {gx + gw * .75} {yp}H{gx + gw - 10}" stroke="{col}" stroke-width="4" '
                   'fill="none" stroke-linecap="round"/>')
        out.append(raw_text(tr("Reactants"), gx + 14, yr - 10, 12, ink, "Bold", "start"))
        out.append(raw_text(tr("Products"), gx + gw - 14, yp - 10, 12, ink, "Bold", "end"))
        # Ea
        out.append(arrow_line(gx + gw * .5, yr, gx + gw * .5, ypk + 6, "#7C8B9C", 2.2))
        out.append(arrow_line(gx + gw * .5, ypk + 6, gx + gw * .5, yr, "#7C8B9C", 2.2))
        out.append(rich([(tr("Activation energy") + " (E", "n"), ("a", "sub"), (")", "n")], gx + gw * .5 + 10,
                        (yr + ypk) / 2 + 26, 11, ink, "start", "SemiBold"))
        # ΔH
        ax = gx + gw - 40
        out.append(f'<path d="M{gx + gw * .3} {yr}H{ax + 10}" stroke="#7C8B9C" stroke-width="1.6" stroke-dasharray="5 4"/>')
        out.append(arrow_line(ax, yr, ax, yp, col, 3))
        out.append(raw_text(dh, ax - 10, (yr + yp) / 2 + 5, 14, col, "Bold", "end"))
        out.append(raw_text(tr("Energy"), gx + 8, gy + 4, 11, ink, "SemiBold", "start"))
        out.append(raw_text(tr("Reaction progress"), gx + gw, gy + gh + 22, 11, ink, "SemiBold", "end"))
        ey = top + 440
        out.append(text("Examples", x + 24, ey, 14, th["ink"], "Bold", "start"))
        for i, e in enumerate(ex):
            out.append(f'<circle cx="{x + 30}" cy="{ey + 22 + i * 22}" r="4" fill="{col}"/>'
                       + text(e, x + 42, ey + 27 + i * 22, 12.5, th["sub"], "SemiBold", "start"))
    return W, H, "".join(out)


# ------------------------------------------------------------ sel Volta

def galvanic_cell(th):
    W, H = 1226, 760
    top = 122
    out = [header(W, th, "GALVANIC (VOLTAIC) CELL",
                  "The Daniell cell: zinc and copper electrodes produce electricity from a redox reaction")]
    ink = "#1E2A3A"
    out.append(f'<rect x="{MX}" y="{top}" width="{W - 2 * MX}" height="{430}" rx="16" fill="{th["plate"]}"/>')
    cx1, cx2, by, bw, bh = 330, W - 330, top + 190, 230, 210
    g = []
    for cx, sol, rod, lab, rx in ((cx1, "#D9E6EE", ZINC, "Zn", cx1 - 52), (cx2, "#4F8FD6", COPPER, "Cu", cx2 + 18)):
        x0 = cx - bw / 2
        g.append(f'<path d="M{x0} {by}V{by + bh - 12}a12 12 0 0 0 12 12h{bw - 24}a12 12 0 0 0 12-12V{by}" '
                 f'fill="#EEF7FA" stroke="{ink}" stroke-width="2.6"/>')
        g.append(f'<path d="M{x0 + 1.3} {by + 50}H{x0 + bw - 1.3}V{by + bh - 12}a11 11 0 0 1-11 11H{x0 + 12}'
                 f'a11 11 0 0 1-11-11z" fill="{sol}"/>')
        g.append(f'<rect x="{rx}" y="{by - 70}" width="34" height="{bh}" rx="4" fill="{rod}" stroke="{ink}" '
                 'stroke-width="2.4"/>')
        g.append(raw_text(lab, rx + 17 + (-30 if lab == "Zn" else 30), by - 52, 18, ink, "Bold"))
    # jembatan garam
    g.append(f'<path d="M{cx1 + 50} {by + bh - 60}V{by - 40}H{cx2 - 50}V{by + bh - 60}" stroke="{ink}" '
             'stroke-width="30" fill="none" stroke-linejoin="round"/>'
             f'<path d="M{cx1 + 50} {by + bh - 60}V{by - 40}H{cx2 - 50}V{by + bh - 60}" stroke="#F4E2B8" '
             'stroke-width="24" fill="none" stroke-linejoin="round"/>')
    # kawat & voltmeter
    wy = top + 46
    g.append(f'<path d="M{cx1 - 35} {by - 70}V{wy}H{cx2 + 35}V{by - 70}" stroke="{ink}" stroke-width="3" fill="none"/>')
    g.append(f'<circle cx="{W / 2}" cy="{wy}" r="34" fill="#FFFFFF" stroke="{ink}" stroke-width="3"/>'
             + raw_text(loc("1.10 V"), W / 2, wy + 7, 17, ink, "Bold"))
    for k in range(2):
        ex = cx1 + 40 + k * 100
        g.append(arrow_line(ex, wy - 18, ex + 50, wy - 18, R, 2.6))
    g.append(rich([("e", "n"), ("−", "sup"), (" " + tr("flow"), "n")], cx1 + 40, wy - 30, 13, R, "start"))
    out.append(f'<g {style_attrs(1.4)}>' + "".join(g) + "</g>")
    out.append(raw_text(tr("Salt bridge"), W / 2, by - 64, 13, ink, "Bold"))
    out.append(chem("ZnSO_{4}", cx1 - 40, by + bh - 20, 15, ink, "middle"))
    out.append(chem("CuSO_{4}", cx2 + 40, by + bh - 20, 15, "#FFFFFF", "middle"))
    # keterangan anode / katode
    ly = top + 456
    for k, (name, sign, kind, eq, col) in enumerate((
            ("Anode", "(−)", "Oxidation", "Zn → Zn^{2+} + 2e^{−}", ZINC),
            ("Cathode", "(+)", "Reduction", "Cu^{2+} + 2e^{−} → Cu", COPPER))):
        x = MX + k * ((W - 2 * MX) / 2 + 12)
        w = (W - 2 * MX) / 2 - 12
        out.append(_card(x, ly, w, 120, th))
        out.append(f'<rect x="{x + 18}" y="{ly + 22}" width="10" height="76" rx="5" fill="{col}"/>')
        out.append(text(f"{tr(name)} {sign}", x + 44, ly + 46, 20, th["ink"], "Bold", "start"))
        out.append(text(f"{tr(kind)} · {tr('Zinc') if k == 0 else tr('Copper')}", x + 44, ly + 68, 12.5,
                        th["sub"], "SemiBold", "start"))
        out.append(chem(eq, x + 44, ly + 100, 19, th["accent"]))
    out.append(chem(tr("Overall") + ": Zn + Cu^{2+} → Zn^{2+} + Cu", W / 2, ly + 156, 15, th["sub"], "middle",
                    "SemiBold"))
    return W, H, "".join(out)


# ------------------------------------------------------------ konsep mol

def mole_concept(th):
    W, H = 1226, 720
    top = 122
    out = [header(W, th, "THE MOLE CONCEPT", "Converting between moles, mass, number of particles and gas volume")]
    cx, cy = W / 2, top + 250
    boxes = [
        ("Number of particles", "N = n × 6.022 × 10^{23}", "Avogadro's number (N_{A})", cx - 360, top + 70, T),
        ("Mass", "m = n × M", "M = molar mass (g/mol)", cx + 360, top + 70, O),
        ("Gas volume", "V = n × 22.4 L", "at STP (0 °C, 1 atm)", cx, top + 430, P),
    ]
    for _, _, _, bx, byy, col in boxes:
        out.append(f'<path d="M{cx} {cy}L{bx} {byy + 60}" stroke="{col}" stroke-width="4" stroke-dasharray="10 7"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="92" fill="{th["accent"]}"/>'
               f'<circle cx="{cx}" cy="{cy}" r="78" fill="none" stroke="#FFFFFF" stroke-width="2.4"/>'
               + raw_text("1 mol", cx, cy + 4, 40, "#FFFFFF", "Bold")
               + raw_text(tr("amount of substance (n)"), cx, cy + 32, 11, "#FFFFFF", "SemiBold"))
    for name, eq, note, bx, byy, col in boxes:
        bw, bh = 330, 124
        out.append(_card(bx - bw / 2, byy, bw, bh, th))
        out.append(f'<rect x="{bx - bw / 2}" y="{byy}" width="{bw}" height="8" rx="4" fill="{col}"/>')
        out.append(text(name, bx, byy + 40, 18, th["ink"]))
        out.append(chem(loc(eq), bx, byy + 76, 20, th["accent"], "middle"))
        out.append(rich(parse(tr(note)), bx, byy + 104, 12, th["sub"], "middle", "SemiBold"))
    ey = top + 300
    out.append(_card(MX, ey, 330, 120, th))
    out.append(text("Example: water", MX + 165, ey + 34, 16, th["ink"]))
    out.append(chem("1 mol H_{2}O = 18 g", MX + 165, ey + 66, 17, th["accent"], "middle"))
    out.append(chem(loc("= 6.022 × 10^{23} ") + tr("molecules"), MX + 165, ey + 96, 15, th["accent"], "middle"))
    out.append(_card(W - MX - 330, ey, 330, 120, th))
    out.append(text("Example: oxygen gas", W - MX - 165, ey + 34, 16, th["ink"]))
    out.append(chem("1 mol O_{2} = 32 g", W - MX - 165, ey + 66, 17, th["accent"], "middle"))
    out.append(chem(loc("= 22.4 L ") + tr("at STP"), W - MX - 165, ey + 96, 15, th["accent"], "middle"))
    return W, H, "".join(out)


POSTERS = [
    ("reaction-rate", reaction_rate, "Factors affecting the rate of chemical reaction chart",
     ["reaction rate", "rate of reaction", "collision theory", "temperature", "concentration", "surface area",
      "catalyst", "activation energy", "particles", "kinetics", "chemical kinetics", "collisions", "speed",
      "energy"]),
    ("energy-diagrams", energy_diagrams, "Exothermic and endothermic reaction energy profile diagrams",
     ["exothermic", "endothermic", "energy diagram", "enthalpy", "activation energy", "energy profile",
      "thermochemistry", "reactants", "products", "heat", "combustion", "photosynthesis", "delta h", "graph"]),
    ("galvanic-cell", galvanic_cell, "Galvanic voltaic cell Daniell cell diagram with zinc and copper electrodes",
     ["galvanic cell", "voltaic cell", "daniell cell", "electrochemistry", "redox", "anode", "cathode",
      "salt bridge", "zinc", "copper", "battery", "oxidation", "reduction", "electrode"]),
    ("mole-concept", mole_concept, "The mole concept chart, Avogadro number, molar mass and molar volume",
     ["mole", "mole concept", "avogadro", "avogadro number", "molar mass", "molar volume", "stoichiometry",
      "amount of substance", "calculation", "formula", "stp", "particles", "chemistry math", "conversion"]),
]

TR.update({
    "FACTORS AFFECTING REACTION RATE": "FAKTOR-FAKTOR LAJU REAKSI",
    "Temperature, concentration, surface area and catalysts change how fast a reaction happens":
        "Suhu, konsentrasi, luas permukaan, dan katalis memengaruhi cepat lambatnya reaksi",
    "Temperature": "Suhu", "Concentration": "Konsentrasi", "Surface area": "Luas permukaan", "Catalyst": "Katalis",
    "Higher temperature: particles move faster and collide more often":
        "Suhu lebih tinggi: partikel bergerak lebih cepat dan lebih sering bertumbukan",
    "Higher concentration: more particles in the same space, more collisions":
        "Konsentrasi lebih tinggi: lebih banyak partikel dalam ruang yang sama, tumbukan lebih banyak",
    "Smaller pieces: more surface exposed for particles to react":
        "Ukuran lebih kecil: permukaan yang bersentuhan dengan pereaksi lebih luas",
    "A catalyst lowers the activation energy without being used up":
        "Katalis menurunkan energi aktivasi tanpa ikut habis bereaksi",
    "Low": "Rendah", "High": "Tinggi", "Large lump": "Bongkahan", "Small pieces": "Serbuk",
    "without catalyst": "tanpa katalis", "with catalyst": "dengan katalis", "Energy": "Energi",
    "Reaction progress": "Jalannya reaksi",
    "EXOTHERMIC AND ENDOTHERMIC REACTIONS": "REAKSI EKSOTERM DAN ENDOTERM",
    "Energy profile diagrams showing activation energy and enthalpy change (ΔH)":
        "Diagram tingkat energi: energi aktivasi dan perubahan entalpi (ΔH)",
    "Exothermic": "Eksoterm", "Endothermic": "Endoterm",
    "Energy is released to the surroundings": "Kalor dilepaskan ke lingkungan",
    "Energy is absorbed from the surroundings": "Kalor diserap dari lingkungan",
    "Reactants": "Pereaksi", "Products": "Hasil reaksi", "Activation energy": "Energi aktivasi",
    "Combustion of fuels": "Pembakaran bahan bakar", "Respiration": "Respirasi", "Neutralization": "Netralisasi",
    "Photosynthesis": "Fotosintesis", "Melting ice": "Es mencair", "Thermal decomposition": "Penguraian oleh panas",
    "GALVANIC (VOLTAIC) CELL": "SEL VOLTA (GALVANI)",
    "The Daniell cell: zinc and copper electrodes produce electricity from a redox reaction":
        "Sel Daniell: elektrode seng dan tembaga menghasilkan listrik dari reaksi redoks",
    "flow": "mengalir", "Salt bridge": "Jembatan garam", "Anode": "Anode", "Cathode": "Katode",
    "Oxidation": "Oksidasi", "Reduction": "Reduksi", "Zinc": "seng", "Copper": "tembaga",
    "THE MOLE CONCEPT": "KONSEP MOL",
    "Converting between moles, mass, number of particles and gas volume":
        "Hubungan mol dengan massa, jumlah partikel, dan volume gas",
    "Number of particles": "Jumlah partikel", "Mass": "Massa", "Gas volume": "Volume gas",
    "Avogadro's number (N_{A})": "Bilangan Avogadro (N_{A})", "M = molar mass (g/mol)": "M = massa molar (g/mol)",
    "at STP (0 °C, 1 atm)": "pada STP (0 °C, 1 atm)", "amount of substance (n)": "jumlah zat (n)",
    "Example: water": "Contoh: air", "Example: oxygen gas": "Contoh: gas oksigen", "molecules": "molekul",
    "at STP": "pada STP", "Overall": "Reaksi sel",
})
