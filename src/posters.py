"""Poster edukasi kimia (infografis), masing-masing dalam tema gelap & terang.

- Bagan alat laboratorium berlabel (40 alat dari set 02 dan 03)
- Bagan molekul umum dengan rumus kimia
- Bagan model atom Bohr unsur 1-20
- Skala pH dengan contoh zat sehari-hari
- Wujud zat dan perubahan wujudnya
- Jenis-jenis reaksi kimia

Semua teks berupa outline (textpath).
"""
import math

import atoms
import icons_lab2
import icons_lab_flat
import molecules
import posters2
import posters3
import posters4
import posters5
import posters6
import posters7
import posters8
import posters9
import posters10
import posters11
import posters12
import posters13
import posters14
import posters15
import posters16
import posters17
import posters18
import posters19
import posters20
import posters21
import posters22
import posters23
import posters24
import posters25
import posters26
import posters27
import posters28
import posters29
import posters30
import posters31
import posters32
import posters33
import posters34
import posters35
import posters36
from icons_lab_flat import L, O, P, R, T, Y, dark, light, solid
from poster_kit import (COMMON_KW, EXTRA_THEMES, MX, THEMES, arrow, doc, fit_text, header, icon_at, particle, set_lang, text,
                        tr)
from render import style_attrs
from textpath import formula

SET_ID = "chemistry-posters"

# ------------------------------------------------------------ bagan ikon

def icon_chart(th, title, subtitle, items, cols, cw=130, ch=152, gap=14):
    """items: (body, stroke, nama, keterangan). keterangan boleh berupa rumus (diawali '=')."""
    rows = -(-len(items) // cols)
    W = cols * (cw + gap) - gap + 2 * MX
    top = 122
    H = top + rows * (ch + gap) - gap + 40
    out = [header(W, th, title, subtitle)]
    for i, (body, stroke, name, sub) in enumerate(items):
        x = MX + (i % cols) * (cw + gap)
        y = top + (i // cols) * (ch + gap)
        out.append(f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="12" fill="{th["card"]}" '
                   f'stroke="{th["card_stroke"]}" stroke-width="1.2"/>'
                   f'<rect x="{x + 7}" y="{y + 7}" width="{cw - 14}" height="{ch - 52}" rx="9" fill="{th["plate"]}"/>')
        size = min(cw - 14, ch - 52) - 14
        out.append(icon_at(body, stroke, x + cw / 2 - size / 2, y + 7 + (ch - 52 - size) / 2, size))
        out.append(fit_text(name, x + cw / 2, y + ch - 26, 12, th["ink"], cw - 12, "SemiBold"))
        if sub.startswith("="):
            out.append(formula(sub[1:], x + cw / 2, y + ch - 10, 10.5, th["accent"]))
        else:
            out.append(fit_text(sub, x + cw / 2, y + ch - 10, 9.5, th["sub"], cw - 12, "Regular"))
    return W, H, "".join(out)


LAB_NAMES = {
    "test-tube-rack": "Test Tube Rack", "burette-stand": "Burette & Stand", "mortar-and-pestle": "Mortar & Pestle",
    "laboratory-scale": "Analytical Balance", "tripod-burner-beaker": "Tripod & Gauze",
    "toxic-chemical-bottle": "Hazard Bottle", "reaction-flask-smoke": "Reaction Flask",
    "watch-glass-crystals": "Watch Glass", "clipboard-notes": "Lab Notebook", "protective-gloves": "Gloves",
    "round-bottom-flask": "Round-Bottom Flask", "petri-dish": "Petri Dish", "wash-bottle": "Wash Bottle",
}
LAB_USE = {
    "erlenmeyer-flask": "mixing & swirling", "beaker": "holding liquids", "test-tube": "small reactions",
    "test-tube-rack": "holding test tubes", "round-bottom-flask": "heating & boiling",
    "volumetric-flask": "exact volumes", "microscope": "magnifying samples", "bunsen-burner": "heating",
    "pipette": "measuring liquid", "dropper": "adding drops", "graduated-cylinder": "measuring volume",
    "petri-dish": "growing cultures", "funnel": "pouring & filtering", "mortar-and-pestle": "grinding solids",
    "thermometer": "temperature", "burette-stand": "titration", "safety-goggles": "eye protection",
    "retort": "distillation", "laboratory-scale": "weighing mass", "wash-bottle": "rinsing",
    "reagent-bottle": "storing chemicals", "dropper-bottle": "dispensing drops",
    "separatory-funnel": "separating liquids", "liebig-condenser": "cooling vapor", "crucible": "high-heat melting",
    "tripod-burner-beaker": "supporting & heating", "spirit-lamp": "gentle heating", "syringe": "measuring & injecting",
    "lab-coat": "body protection", "protective-gloves": "hand protection", "centrifuge": "separating by spinning",
    "magnetic-stirrer": "stirring & heating", "watch-glass-crystals": "evaporating samples",
    "spatula": "transferring solids", "magnifying-glass": "close inspection",
    "toxic-chemical-bottle": "hazardous chemicals", "gas-cylinder": "storing gas",
    "fire-extinguisher": "fire safety", "clipboard-notes": "recording data", "reaction-flask-smoke": "chemical reactions",
}


def lab_chart(th):
    items = []
    for mod in (icons_lab_flat, icons_lab2):
        for ic in mod.ICONS:
            name = LAB_NAMES.get(ic["id"]) or ic["id"].replace("-", " ").title()
            items.append((ic["body"], mod.STROKE, name, LAB_USE[ic["id"]]))
    return icon_chart(th, "LABORATORY EQUIPMENT", "40 common chemistry laboratory tools and what they are used for",
                      items, cols=8)


def molecule_chart(th):
    items = []
    for ic, (mid, name, *_rest) in zip(molecules.ICONS, molecules.MOLS):
        label, f = name.rsplit(" ", 1)
        label = label.replace(" molecule", "").replace(" crystal lattice", "")
        items.append((ic["body"], molecules.STROKE, label, "=" + f))
    return icon_chart(th, "COMMON MOLECULES", "Ball and stick models of 20 everyday molecules and compounds",
                      items, cols=5, cw=150, ch=160)


def atom_chart(th):
    items = []
    for z, (ic, (sym, name)) in enumerate(zip(atoms.ICONS, atoms.ELEMENTS), start=1):
        conf = ", ".join(str(n) for n in atoms.shells(z))
        items.append((ic["body"], atoms.STROKE, f"{tr(name)} ({sym})", f"Z = {z}  ·  {tr('electrons')} {conf}"))
    return icon_chart(th, "BOHR ATOMIC MODELS", "Electron shell arrangement of the first 20 elements",
                      items, cols=5, cw=150, ch=160)


# ------------------------------------------------------------ skala pH

PH = [
    ("#D7262B", "Battery acid"), ("#E9452A", "Stomach acid"), ("#F27A24", "Lemon juice"),
    ("#F7A823", "Vinegar"), ("#F5C922", "Tomato juice"), ("#C9D52A", "Black coffee"), ("#8DC63F", "Milk"),
    ("#4BB04A", "Pure water"), ("#2DA36B", "Sea water"), ("#1E9C9A", "Baking soda"),
    ("#2384C6", "Milk of magnesia"), ("#3062AE", "Ammonia"), ("#4B4A9E", "Soapy water"),
    ("#5E3B8F", "Bleach"), ("#4A2A73", "Drain cleaner"),
]


def drop(cx, top, h, col):
    w = h * .62
    return solid(f"M{cx} {top}c{w * .55:.2f} {h * .38:.2f} {w / 2:.2f} {h * .52:.2f} {w / 2:.2f} {h * .68:.2f}"
                 f"a{w / 2:.2f} {w / 2:.2f} 0 0 1-{w:.2f} 0c0-{h * .16:.2f}-{w * .05:.2f}-{h * .3:.2f} {w / 2:.2f}-{h * .68:.2f}z",
                 col, cx - w / 2, cx + w / 2).replace("{p}", f"ph{cx:.0f}")


def ph_scale(th):
    W, gap = 1226, 6
    sw = (W - 2 * MX - 14 * gap) / 15
    out = [header(W, th, "THE pH SCALE", "Acidic, neutral and alkaline substances from 0 to 14 with everyday examples")]
    y0 = 150
    # rentang asam / netral / basa
    for a, b, label, col in ((0, 6, "ACIDIC", PH[1][0]), (7, 7, "NEUTRAL", PH[7][0]), (8, 14, "ALKALINE (BASIC)", PH[12][0])):
        x1, x2 = MX + a * (sw + gap) + 4, MX + b * (sw + gap) + sw - 4
        out.append(f'<path d="M{x1} {y0 + 12}v-8h{x2 - x1}v8" fill="none" stroke="{col}" stroke-width="2.4" '
                   'stroke-linecap="round" stroke-linejoin="round"/>')
        out.append(fit_text(label, (x1 + x2) / 2, y0 - 6, 14, col if th["bg"] == "#FFFFFF" else light(col, .35),
                            x2 - x1))
    out.append(f'<g {style_attrs(1.4)}>')
    for i, (col, ex) in enumerate(PH):
        x = MX + i * (sw + gap)
        out.append(drop(x + sw / 2, y0 + 24, 40, col))
    out.append("</g>")
    for i, (col, ex) in enumerate(PH):
        x = MX + i * (sw + gap)
        out.append(f'<rect x="{x:.2f}" y="{y0 + 76}" width="{sw:.2f}" height="140" rx="10" fill="{col}"/>'
                   f'<rect x="{x:.2f}" y="{y0 + 176}" width="{sw:.2f}" height="40" rx="10" fill="{dark(col, .12)}"/>'
                   f'<rect x="{x:.2f}" y="{y0 + 176}" width="{sw:.2f}" height="10" fill="{dark(col, .12)}"/>')
        out.append(text(str(i), x + sw / 2, y0 + 150, 38, "#FFFFFF"))
        words = tr(ex).split(" ", 1)
        out.append(fit_text(words[0], x + sw / 2, y0 + 239, 10.5, th["ink"], sw, "SemiBold"))
        if len(words) > 1:
            out.append(fit_text(words[1], x + sw / 2, y0 + 253, 10.5, th["ink"], sw, "SemiBold"))
    # panah strength
    ay = y0 + 290
    out.append(f'<path d="M{MX + 10} {ay}H{W - MX - 10}" stroke="{th["sub"]}" stroke-width="2" fill="none"/>'
               f'<path d="M{MX} {ay}l12-6v12zM{W - MX} {ay}l-12-6v12z" fill="{th["sub"]}"/>')
    out.append(text("stronger acid", MX + 18, ay - 8, 10.5, th["sub"], "Regular", "start"))
    out.append(text("stronger base", W - MX - 18, ay - 8, 10.5, th["sub"], "Regular", "end"))
    out.append(text("Example values are typical approximations.", W / 2, ay + 30, 9.5, th["sub"], "Regular"))
    return W, ay + 52, "".join(out)


# ------------------------------------------------------------ wujud zat

def states_of_matter(th):
    W, box = 1226, 260
    cxs = [W / 2 - 400, W / 2, W / 2 + 400]
    by = 210
    out = [header(W, th, "STATES OF MATTER", "Particle arrangement in solids, liquids and gases and the changes between them")]
    hot, cold = "#F0663A", "#2E9BDA"
    names = [("SOLID", "Fixed shape and fixed volume", O),
             ("LIQUID", "Fixed volume, takes the shape of its container", T),
             ("GAS", "No fixed shape or volume, fills its container", P)]
    out.append(f'<g {style_attrs(1.6)}>')
    for k, (cx, (nm, desc, col)) in enumerate(zip(cxs, names)):
        x0 = cx - box / 2
        out.append(f'<rect x="{x0}" y="{by}" width="{box}" height="{box}" rx="18" fill="{th["card"]}" '
                   f'stroke="{th["card_stroke"]}" stroke-width="2"/>')
        r = 15
        if k == 0:
            for i in range(5):
                for j in range(5):
                    out.append(particle(cx + (j - 2) * 31, by + 70 + i * 31, r, col, f"s{i}{j}"))
        elif k == 1:
            pts = [(-92, 0), (-58, 4), (-24, -3), (10, 3), (44, -2), (80, 4), (-76, 33), (-42, 30), (-8, 36),
                   (27, 31), (62, 35), (94, 30), (-92, 64), (-58, 66), (-23, 62), (12, 67), (46, 63), (82, 66)]
            for i, (dx, dy) in enumerate(pts):
                out.append(particle(cx + dx, by + 150 + dy, r, col, f"l{i}"))
        else:
            pts = [(-80, -70), (20, -88), (85, -40), (-30, -20), (60, 30), (-90, 40), (-10, 75), (85, 90)]
            for i, (dx, dy) in enumerate(pts):
                gx, gy = cx + dx, by + box / 2 + dy
                ang = (i * 77) % 360
                tx, ty = math.cos(math.radians(ang)), math.sin(math.radians(ang))
                out.append(f'<path d="M{gx - tx * 22:.1f} {gy - ty * 22:.1f}L{gx - tx * 40:.1f} {gy - ty * 40:.1f}'
                           f'M{gx - tx * 22 + ty * 9:.1f} {gy - ty * 22 - tx * 9:.1f}L{gx - tx * 34 + ty * 9:.1f} {gy - ty * 34 - tx * 9:.1f}" '
                           f'stroke="{th["sub"]}" stroke-width="2"/>')
                out.append(particle(gx, gy, r, col, f"g{i}"))
        out.append(text(nm, cx, by + box + 36, 22, th["ink"]))
        out.append(fit_text(desc, cx, by + box + 56, 11, th["sub"], box + 40, "Regular"))
    out.append("</g>")
    # perubahan wujud
    for a, b in ((0, 1), (1, 2)):
        x1, x2 = cxs[a] + box / 2 + 12, cxs[b] - box / 2 - 12
        out.append(arrow(x1, by + 95, x2, by + 95, hot, -14))
        out.append(arrow(x2, by + 170, x1, by + 170, cold, 14))
        mid = (x1 + x2) / 2
        out.append(text(["Melting", "Evaporation"][a], mid, by + 70, 13, hot))
        out.append(text(["Freezing", "Condensation"][a], mid, by + 208, 13, cold))
    out.append(arrow(cxs[0], by - 14, cxs[2], by - 14, hot, -34))
    out.append(text("Sublimation", W / 2, by - 66, 13, hot))
    ly = by + box + 100
    out.append(arrow(cxs[2], ly - 18, cxs[0], ly - 18, cold, 30))
    out.append(text("Deposition", W / 2, ly + 46, 13, cold))
    lg = ly + 86
    out.append(f'<rect x="{W / 2 - 190}" y="{lg - 12}" width="16" height="16" rx="4" fill="{hot}"/>'
               + text("Heat added (energy in)", W / 2 - 166, lg + 1, 12, th["ink"], "SemiBold", "start") +
               f'<rect x="{W / 2 + 30}" y="{lg - 12}" width="16" height="16" rx="4" fill="{cold}"/>'
               + text("Heat removed (energy out)", W / 2 + 54, lg + 1, 12, th["ink"], "SemiBold", "start"))
    return W, lg + 34, "".join(out)


# ------------------------------------------------------------ jenis reaksi

BALL = {"A": R, "B": "#3D7DDB", "C": Y, "D": L}


def balls(seq, x, y, r=22):
    """Gambar senyawa sebagai bola-bola bersinggungan; kembalikan (svg, lebar)."""
    out = ""
    for i, el in enumerate(seq):
        cx = x + r + i * r * 1.55
        out += particle(cx, y, r, BALL[el], f"b{x:.0f}{i}", shine=False)
        out += text(el, cx, y + r * .36, r, "#FFFFFF")
    return out, 2 * r + (len(seq) - 1) * r * 1.55


def reactions(th):
    W, top, rh = 1226, 122, 118
    rows = [
        ("Synthesis", "Two or more substances combine into one", "A + B → AB", [["A"], "+", ["B"], "→", ["A", "B"]]),
        ("Decomposition", "One compound breaks down into simpler substances", "AB → A + B",
         [["A", "B"], "→", ["A"], "+", ["B"]]),
        ("Single replacement", "One element replaces another in a compound", "A + BC → AC + B",
         [["A"], "+", ["B", "C"], "→", ["A", "C"], "+", ["B"]]),
        ("Double replacement", "Two compounds exchange partners", "AB + CD → AD + CB",
         [["A", "B"], "+", ["C", "D"], "→", ["A", "D"], "+", ["C", "B"]]),
        ("Combustion", "A fuel reacts with oxygen releasing energy", "CH4 + 2O2 → CO2 + 2H2O", "combustion"),
    ]
    out = [header(W, th, "TYPES OF CHEMICAL REACTIONS",
                  "Synthesis, decomposition, replacement and combustion reactions explained with particle models")]
    mol = {m[0]: ic["body"] for m, ic in zip(molecules.MOLS, molecules.ICONS)}
    for k, (name, desc, eq, seq) in enumerate(rows):
        y = top + k * (rh + 12)
        out.append(f'<rect x="{MX}" y="{y}" width="{W - 2 * MX}" height="{rh}" rx="16" fill="{th["card"]}" '
                   f'stroke="{th["card_stroke"]}" stroke-width="1.2"/>')
        out.append(f'<circle cx="{MX + 40}" cy="{y + rh / 2}" r="20" fill="{th["accent"]}"/>'
                   + text(str(k + 1), MX + 40, y + rh / 2 + 7, 20, "#FFFFFF"))
        out.append(text(name, MX + 76, y + 44, 21, th["ink"], "Bold", "start"))
        out.append(text(desc, MX + 76, y + 66, 11.5, th["sub"], "Regular", "start"))
        out.append(formula(eq, MX + 76, y + 92, 15, th["accent"], anchor="start"))
        cy = y + rh / 2
        x = 0
        row = []
        if seq == "combustion":
            parts = [("methane", ""), "+", ("oxygen", "2"), "→", ("carbon-dioxide", ""), "+", ("water", "2")]
            for p in parts:
                if isinstance(p, str):
                    row.append(text(p, x + 20, cy + 10, 30, th["sub"]))
                    x += 40
                    continue
                mid, coef = p
                if coef:
                    row.append(text(coef, x + 8, cy + 10, 26, th["ink"]))
                    x += 22
                size = 88
                row.append(f'<circle cx="{x + size / 2}" cy="{cy}" r="{size / 2 + 2}" fill="{th["plate"]}" stroke="none"/>')
                row.append(icon_at(mol[mid], molecules.STROKE, x + 8, cy - size / 2 + 8, size - 16))
                x += size + 12
        else:
            for p in seq:
                if isinstance(p, str):
                    row.append(text(p, x + 20, cy + 10, 30, th["sub"]))
                    x += 40
                else:
                    svg, w = balls(p, x, cy)
                    row.append(svg)
                    x += w + 12
        # pusatkan diagram di area kanan kartu
        area0, area1 = 540, W - MX - 20
        ox = area0 + (area1 - area0 - (x - 12)) / 2
        out.append(f'<g transform="translate({ox:.2f} 0)"><g {style_attrs(1.5)}>' + "".join(row) + "</g></g>")
    H = top + len(rows) * (rh + 12) + 28
    return W, H, "".join(out)


POSTERS = [
    ("lab-equipment", lab_chart, "Laboratory equipment names chart, 40 labeled chemistry lab tools",
     ["laboratory equipment", "lab tools", "glassware", "flask", "beaker", "test tube", "microscope", "burner",
      "pipette", "names", "labeled", "icons", "collection", "set", "apparatus", "safety"]),
    ("molecules", molecule_chart, "Common molecules chart with chemical formulas, ball and stick models",
     ["molecule", "molecules", "chemical formula", "ball and stick", "molecular model", "compound", "water", "h2o",
      "carbon dioxide", "methane", "benzene", "atoms", "bond", "structure"]),
    ("bohr-atoms", atom_chart, "Bohr atomic models of the first 20 elements chart",
     ["bohr model", "atom", "atomic structure", "electron shell", "electron configuration", "periodic table",
      "element", "nucleus", "electron", "physics", "atomic number", "orbit"]),
    ("ph-scale", ph_scale, "pH scale chart with acidic, neutral and alkaline examples",
     ["ph scale", "ph", "acid", "base", "alkaline", "neutral", "acidic", "indicator", "litmus", "universal indicator",
      "rainbow", "color scale", "measurement", "water", "lemon", "bleach"]),
    ("states-of-matter", states_of_matter, "States of matter diagram, solid liquid gas and phase changes",
     ["states of matter", "solid", "liquid", "gas", "phase change", "melting", "freezing", "evaporation",
      "condensation", "sublimation", "deposition", "particles", "molecules", "physics", "matter", "heat"]),
    ("reaction-types", reactions, "Types of chemical reactions chart with particle models",
     ["chemical reaction", "reaction types", "synthesis", "decomposition", "single replacement",
      "double replacement", "combustion", "equation", "reactants", "products", "particles", "molecules",
      "chemical equation", "methane", "oxygen"]),
]


POSTERS += posters2.POSTERS + posters3.POSTERS + posters4.POSTERS + posters5.POSTERS + posters6.POSTERS + posters7.POSTERS + posters8.POSTERS + posters9.POSTERS + posters10.POSTERS + posters11.POSTERS + posters12.POSTERS + posters13.POSTERS + posters14.POSTERS + posters15.POSTERS + posters16.POSTERS + posters17.POSTERS + posters18.POSTERS + posters19.POSTERS + posters20.POSTERS + posters21.POSTERS + posters22.POSTERS + posters23.POSTERS + posters24.POSTERS + posters25.POSTERS + posters26.POSTERS + posters27.POSTERS + posters28.POSTERS + posters29.POSTERS + posters30.POSTERS + posters31.POSTERS + posters32.POSTERS + posters33.POSTERS + posters34.POSTERS + posters35.POSTERS + posters36.POSTERS

def assets():
    """Setiap poster x 2 tema x 2 bahasa. Set Indonesia dipisah agar mudah dipilih."""
    sets = []
    for lang, set_id in (("en", SET_ID), ("id", SET_ID + "-indonesian")):
        set_lang(lang)
        out = []
        for key, fn, title, kw in POSTERS:
            for tname, th in THEMES.items():
                W, H, inner = fn(th)
                note = "" if lang == "en" else " in Indonesian language"
                out.append(dict(
                    name=f"{set_id}-{key}-{tname}", svg=doc(W, H, th, inner), size=7000, png=False,
                    title=f"{title}{note}, {th['mood']}, chemistry education vector infographic",
                    keywords=(["indonesian", "bahasa indonesia"] if lang == "id" else []) + kw + COMMON_KW
                    + {"dark": ["dark background"], "light": ["white background"],
                       "chalkboard": ["chalkboard", "blackboard", "chalk", "green board"]}[tname]))
        sets.append((set_id, out))
        for tname, th in EXTRA_THEMES.items():
            out = []
            for key, fn, title, kw in POSTERS:
                W, H, inner = fn(th)
                note = "" if lang == "en" else " in Indonesian language"
                out.append(dict(
                    name=f"{set_id}-{tname}-{key}", svg=doc(W, H, th, inner), size=7000, png=False,
                    title=f"{title}{note}, {th['mood']}, chemistry education vector infographic",
                    keywords=(["indonesian", "bahasa indonesia"] if lang == "id" else []) + kw + COMMON_KW
                    + ["dark background", "purple", "dark mode"]))
            sets.append((set_id.replace("chemistry-posters", f"chemistry-posters-{tname}"), out))
    set_lang("en")
    return sets
