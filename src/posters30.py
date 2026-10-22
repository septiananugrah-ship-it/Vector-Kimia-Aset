"""Poster edukasi kimia jilid 30: golongan IA logam alkali dan golongan VIIA halogen.
Didaftarkan ke posters.py lewat POSTERS (semua tema x 2 bahasa).
"""
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters3 import arrow_line, mix
from posters4 import chem
from textpath import width

INK = "#1E2A3A"

ALKALI = [("Li", "Lithium", 3, "181", "Red", "#E8573F"), ("Na", "Sodium", 11, "98", "Yellow", "#F2C94C"),
          ("K", "Potassium", 19, "63", "Lilac", "#B57BFF"), ("Rb", "Rubidium", 37, "39", "Red-violet", "#C2185B"),
          ("Cs", "Caesium", 55, "28", "Blue-violet", "#5C6BC0")]
HALOGEN = [("F", "Fluorine", 9, "Pale yellow gas", "#E9F08A"), ("Cl", "Chlorine", 17, "Yellow-green gas", "#B6D96B"),
           ("Br", "Bromine", 35, "Red-brown liquid", "#A8432F"), ("I", "Iodine", 53, "Grey-black solid", "#4A4258"),
           ("At", "Astatine", 85, "Black solid (radioactive)", "#2A2A2A")]


def _wrap(s, size, max_w, weight="SemiBold"):
    lines, cur = [], ""
    for w_ in tr(s).split():
        t = (cur + " " + w_).strip()
        if width(t, size, weight) > max_w and cur:
            lines.append(cur)
            cur = w_
        else:
            cur = t
    return lines + [cur]


def _tile(x, y, s, sym, z, col, ink=INK):
    return (f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="12" fill="{col}" stroke="{INK}" stroke-width="2.5"/>'
            + text(str(z), x + 10, y + 20, 14, ink, "SemiBold", "start")
            + text(sym, x + s / 2, y + s * .7, s * .42, ink, "Bold"))


def _trend(x, y1, y2, label, col, th):
    out = [arrow_line(x, y1, x, y2, col, 5)]
    for j, ln in enumerate(_wrap(label, 13, 110)):
        out.append(text(ln, x, y2 + 26 + j * 17, 13, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3),
                        "Bold"))
    return "".join(out)


def alkali(th):
    W = 1226
    top = 122
    rh = 92
    H = top + 5 * (rh + 10) + 50 + 200 + 30
    out = [header(W, th, "GROUP 1: ALKALI METALS", "Soft, very reactive metals that react with water to form "
                                                   "alkalis")]
    out.append(_card(MX, top, W - 2 * MX, 5 * (rh + 10) + 40, th))
    hx = [MX + 200, MX + 470, MX + 650, MX + 850]
    for lab, xx in zip(("Element", "Melting point (°C)", "Flame color", "Reaction with water"), hx):
        out.append(text(lab, xx, top + 30, 13, th["sub"], "Bold", "start"))
    for i, (sym, name, z, mp, flame, fcol) in enumerate(ALKALI):
        y = top + 44 + i * (rh + 10)
        out.append(_tile(MX + 30, y, rh - 16, sym, z, "#FF9E8A"))
        out.append(fit_text(name, hx[0], y + rh / 2 - 2, 20, th["ink"], 240, anchor="start"))
        out.append(text(mp, hx[1] + 40, y + rh / 2 - 2, 22, th["ink"], "Bold"))
        out.append(f'<path d="M{hx[2] + 20} {y + rh / 2 + 18}c-14 -16 -6 -30 0 -44c8 14 18 26 0 44z" fill="{fcol}" '
                   f'stroke="{INK}" stroke-width="1.6"/>')
        out.append(fit_text(flame, hx[2] + 44, y + rh / 2 - 2, 15, th["ink"], 140, "SemiBold", "start"))
        level = i + 1
        bw = 30
        for k in range(5):
            fill = "#E8573F" if k < level else mix(th["card"], th["sub"], .25)
            out.append(f'<rect x="{hx[3] + k * (bw + 6)}" y="{y + rh / 2 - 22}" width="{bw}" height="20" rx="6" '
                       f'fill="{fill}"/>')
    out.append(_trend(W - MX - 60, top + 50, top + 5 * (rh + 10) - 60, "More reactive down the group", "#E8573F",
                      th))
    y = top + 5 * (rh + 10) + 60
    cw = (W - 2 * MX - 20) / 2
    out.append(_card(MX, y, cw, 200, th))
    out.append(text("Reaction with water", MX + cw / 2, y + 38, 17, th["ink"]))
    out.append(f'<rect x="{MX + 20}" y="{y + 56}" width="{cw - 40}" height="60" rx="12" fill="{th["plate"]}"/>')
    out.append(chem("2Na + 2H_{2}O → 2NaOH + H_{2}", MX + cw / 2, y + 95, 22, INK, "middle"))
    for j, ln in enumerate(_wrap("The metal fizzes, releases hydrogen gas and leaves an alkaline solution", 14,
                                 cw - 50)):
        out.append(text(ln, MX + cw / 2, y + 146 + j * 20, 14, th["sub"], "SemiBold"))
    x2 = MX + cw + 20
    out.append(_card(x2, y, cw, 200, th))
    out.append(text("Common properties", x2 + cw / 2, y + 38, 17, th["ink"]))
    props = ["1 valence electron, forms 1+ ions", "Soft enough to cut with a knife", "Stored under oil",
             "Low density (Li, Na, K float on water)"]
    for k, ptxt in enumerate(props):
        out.append(f'<circle cx="{x2 + 34}" cy="{y + 66 + k * 34}" r="6" fill="#FF9E8A"/>')
        out.append(fit_text(ptxt, x2 + 50, y + 72 + k * 34, 15, th["ink"], cw - 70, "SemiBold", "start"))
    return W, H, "".join(out)


def halogen(th):
    W = 1226
    top = 122
    rh = 92
    H = top + 5 * (rh + 10) + 50 + 200 + 30
    out = [header(W, th, "GROUP 17: HALOGENS", "Reactive nonmetals that form salts with metals")]
    out.append(_card(MX, top, W - 2 * MX, 5 * (rh + 10) + 40, th))
    hx = [MX + 200, MX + 450, MX + 820]
    for lab, xx in zip(("Element", "State and color at room temperature", "Reactivity"), hx):
        out.append(text(lab, xx, top + 30, 13, th["sub"], "Bold", "start"))
    for i, (sym, name, z, state, col) in enumerate(HALOGEN):
        y = top + 44 + i * (rh + 10)
        out.append(_tile(MX + 30, y, rh - 16, sym, z, "#C4B5FD"))
        out.append(fit_text(name, hx[0], y + rh / 2 - 2, 20, th["ink"], 220, anchor="start"))
        out.append(f'<circle cx="{hx[1] + 18}" cy="{y + rh / 2 - 8}" r="16" fill="{col}" stroke="{INK}" '
                   'stroke-width="2"/>')
        out.append(fit_text(state, hx[1] + 46, y + rh / 2 - 2, 16, th["ink"], 300, "SemiBold", "start"))
        level = 5 - i
        bw = 30
        for k in range(5):
            fill = "#7C5CD6" if k < level else mix(th["card"], th["sub"], .25)
            out.append(f'<rect x="{hx[2] + k * (bw + 6)}" y="{y + rh / 2 - 22}" width="{bw}" height="20" rx="6" '
                       f'fill="{fill}"/>')
    out.append(_trend(W - MX - 60, top + 50, top + 5 * (rh + 10) - 60, "Less reactive down the group", "#7C5CD6",
                      th))
    y = top + 5 * (rh + 10) + 60
    cw = (W - 2 * MX - 20) / 2
    out.append(_card(MX, y, cw, 200, th))
    out.append(text("Displacement reaction", MX + cw / 2, y + 38, 17, th["ink"]))
    out.append(f'<rect x="{MX + 20}" y="{y + 56}" width="{cw - 40}" height="60" rx="12" fill="{th["plate"]}"/>')
    out.append(chem("Cl_{2} + 2KBr → 2KCl + Br_{2}", MX + cw / 2, y + 95, 22, INK, "middle"))
    for j, ln in enumerate(_wrap("A more reactive halogen displaces a less reactive one from its salt", 14, cw - 50)):
        out.append(text(ln, MX + cw / 2, y + 146 + j * 20, 14, th["sub"], "SemiBold"))
    x2 = MX + cw + 20
    out.append(_card(x2, y, cw, 200, th))
    out.append(text("Common properties", x2 + cw / 2, y + 38, 17, th["ink"]))
    props = ["7 valence electrons, form 1− ions", "Exist as diatomic molecules (Cl₂, Br₂)",
             "Melting and boiling points rise down the group", "Toxic; chlorine disinfects water"]
    for k, ptxt in enumerate(props):
        out.append(f'<circle cx="{x2 + 34}" cy="{y + 66 + k * 34}" r="6" fill="#C4B5FD"/>')
        out.append(fit_text(ptxt, x2 + 50, y + 72 + k * 34, 15, th["ink"], cw - 70, "SemiBold", "start"))
    return W, H, "".join(out)


POSTERS = [
    ("group-1-alkali-metals", alkali, "Group 1 alkali metals chart, reactivity trend, flame colors and reaction with "
                                      "water",
     ["alkali metals", "group 1", "lithium", "sodium", "potassium", "flame test", "reactivity", "periodic table",
      "reaction with water", "metals", "rubidium", "caesium", "periodic trends", "inorganic chemistry"]),
    ("group-17-halogens", halogen, "Group 17 halogens chart, states, colors, reactivity and displacement reactions",
     ["halogens", "group 17", "fluorine", "chlorine", "bromine", "iodine", "astatine", "displacement reaction",
      "reactivity", "periodic table", "nonmetals", "diatomic", "periodic trends", "inorganic chemistry"]),
]

TR.update({
    "GROUP 1: ALKALI METALS": "GOLONGAN IA: LOGAM ALKALI",
    "Soft, very reactive metals that react with water to form alkalis":
        "Logam lunak yang sangat reaktif dan bereaksi dengan air membentuk basa",
    "Element": "Unsur", "Melting point (°C)": "Titik leleh (°C)", "Flame color": "Warna nyala",
    "Reaction with water": "Reaksi dengan air", "Lithium": "Litium", "Sodium": "Natrium", "Potassium": "Kalium",
    "Rubidium": "Rubidium", "Caesium": "Sesium", "Red": "Merah", "Yellow": "Kuning", "Lilac": "Ungu muda",
    "Red-violet": "Merah-ungu", "Blue-violet": "Biru-ungu",
    "More reactive down the group": "Makin ke bawah makin reaktif",
    "The metal fizzes, releases hydrogen gas and leaves an alkaline solution":
        "Logam berdesis, melepaskan gas hidrogen, dan menghasilkan larutan basa",
    "Common properties": "Sifat umum", "1 valence electron, forms 1+ ions": "1 elektron valensi, membentuk ion 1+",
    "Soft enough to cut with a knife": "Cukup lunak untuk dipotong pisau", "Stored under oil": "Disimpan dalam minyak",
    "Low density (Li, Na, K float on water)": "Massa jenis rendah (Li, Na, K mengapung di air)",
    "GROUP 17: HALOGENS": "GOLONGAN VIIA: HALOGEN",
    "Reactive nonmetals that form salts with metals": "Nonlogam reaktif yang membentuk garam dengan logam",
    "State and color at room temperature": "Wujud dan warna pada suhu kamar", "Reactivity": "Kereaktifan",
    "Fluorine": "Fluorin", "Chlorine": "Klorin", "Bromine": "Bromin", "Iodine": "Iodin", "Astatine": "Astatin",
    "Pale yellow gas": "Gas kuning pucat", "Yellow-green gas": "Gas kuning kehijauan",
    "Red-brown liquid": "Cairan merah kecokelatan", "Grey-black solid": "Padatan hitam keabuan",
    "Black solid (radioactive)": "Padatan hitam (radioaktif)",
    "Less reactive down the group": "Makin ke bawah makin kurang reaktif",
    "Displacement reaction": "Reaksi pendesakan",
    "A more reactive halogen displaces a less reactive one from its salt":
        "Halogen yang lebih reaktif mendesak halogen yang kurang reaktif dari garamnya",
    "7 valence electrons, form 1− ions": "7 elektron valensi, membentuk ion 1−",
    "Exist as diatomic molecules (Cl₂, Br₂)": "Berupa molekul diatomik (Cl₂, Br₂)",
    "Melting and boiling points rise down the group": "Titik leleh dan titik didih naik dari atas ke bawah",
    "Toxic; chlorine disinfects water": "Beracun; klorin dipakai untuk desinfeksi air",
})
