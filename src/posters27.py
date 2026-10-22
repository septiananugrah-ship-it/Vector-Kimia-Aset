"""Poster edukasi kimia jilid 27: pengolahan air bersih dan penipisan lapisan ozon.
Didaftarkan ke posters.py lewat POSTERS (semua tema x 2 bahasa).
"""
import random

from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters3 import arrow_line, mix
from posters4 import chem
from textpath import width

INK = "#1E2A3A"
WATER = "#9FD3EC"


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


def _tank(kind, x, y, w, h, seed):
    """Penampang tangki untuk tiap tahap pengolahan air."""
    rnd = random.Random(seed)
    out = [f'<clipPath id="wt{seed}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10"/></clipPath>'
           f'<g clip-path="url(#wt{seed})">']
    water = {"intake": "#C9B48A", "coag": "#CDBE94", "floc": "#D6CDA8", "sed": WATER, "filter": WATER,
             "disinfect": "#BFE6F5"}[kind]
    out.append(f'<rect x="{x}" y="{y + 18}" width="{w}" height="{h}" fill="{water}"/>')
    if kind == "intake":
        for k in range(26):
            out.append(f'<circle cx="{x + rnd.uniform(8, w - 8):.1f}" cy="{y + rnd.uniform(28, h - 8):.1f}" '
                       f'r="{rnd.uniform(2, 4.5):.1f}" fill="#8B6B3E"/>')
        for k in range(5):
            out.append(f'<path d="M{x + 12 + k * (w - 24) / 4:.1f} {y + 18}V{y + h}" stroke="#5B6878" stroke-width="3"/>')
    elif kind == "coag":
        for k in range(30):
            out.append(f'<circle cx="{x + rnd.uniform(8, w - 8):.1f}" cy="{y + rnd.uniform(28, h - 8):.1f}" '
                       f'r="2.6" fill="#8B6B3E"/>')
        for k in range(8):
            out.append(f'<circle cx="{x + rnd.uniform(10, w - 10):.1f}" cy="{y + rnd.uniform(30, h - 10):.1f}" '
                       f'r="3.5" fill="#FFFFFF" stroke="#7C8B9C" stroke-width="1.2"/>')
        out.append(f'<path d="M{x + w / 2} {y + 18}V{y + h - 24}M{x + w / 2 - 24} {y + h - 30}h48" stroke="#5B6878" '
                   'stroke-width="4" stroke-linecap="round"/>')
    elif kind == "floc":
        for k in range(7):
            cx, cy = x + rnd.uniform(18, w - 18), y + rnd.uniform(36, h - 16)
            for j in range(5):
                out.append(f'<circle cx="{cx + rnd.uniform(-7, 7):.1f}" cy="{cy + rnd.uniform(-7, 7):.1f}" r="4" '
                           'fill="#8B6B3E"/>')
    elif kind == "sed":
        out.append(f'<rect x="{x}" y="{y + h - 22}" width="{w}" height="22" fill="#8B6B3E"/>')
        for k in range(5):
            out.append(f'<circle cx="{x + rnd.uniform(10, w - 10):.1f}" cy="{y + h - rnd.uniform(26, 44):.1f}" r="3" '
                       'fill="#8B6B3E"/>')
    elif kind == "filter":
        layers = [("#E9D8A6", "sand"), ("#9AA5B1", "gravel"), ("#3E4652", "charcoal")]
        lh = (h - 40) / 3
        for k, (c, _) in enumerate(layers):
            out.append(f'<rect x="{x}" y="{y + 40 + k * lh:.1f}" width="{w}" height="{lh + .5:.1f}" fill="{c}"/>')
            for j in range(14):
                out.append(f'<circle cx="{x + rnd.uniform(6, w - 6):.1f}" cy="{y + 40 + k * lh + rnd.uniform(4, lh - 4):.1f}" '
                           f'r="{2 + k:.1f}" fill="{mix(c, "#000000", .15)}"/>')
    else:
        for k in range(10):
            bx, by = x + rnd.uniform(10, w - 10), y + rnd.uniform(30, h - 10)
            out.append(f'<circle cx="{bx:.1f}" cy="{by:.1f}" r="4" fill="#4BB04A"/>'
                       f'<path d="M{bx - 4:.1f} {by - 4:.1f}l8 8M{bx + 4:.1f} {by - 4:.1f}l-8 8" stroke="#E8573F" '
                       'stroke-width="2"/>')
        out.append(f'<path d="M{x + w - 30} {y - 4}v30" stroke="#7FD14F" stroke-width="6" stroke-linecap="round"/>')
    out.append('</g>')
    out.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="none" stroke="{INK}" stroke-width="3"/>')
    return "".join(out)


STAGES = [
    ("intake", "Screening", "Large debris such as leaves and trash is removed"),
    ("coag", "Coagulation", "Alum, Al_{2}(SO_{4})_{3}, is added so dirt particles stick together"),
    ("floc", "Flocculation", "Gentle mixing forms larger clumps called flocs"),
    ("sed", "Sedimentation", "Heavy flocs settle to the bottom of the tank"),
    ("filter", "Filtration", "Water passes through sand, gravel and activated charcoal"),
    ("disinfect", "Disinfection", "Chlorine or UV light kills remaining germs"),
]


def water_treatment(th):
    W = 1226
    top = 122
    gap = 30
    cw = (W - 2 * MX - 2 * gap) / 3
    ch = 330
    H = top + 2 * (ch + 24) + 70
    out = [header(W, th, "WATER TREATMENT PROCESS", "How dirty river water becomes clean, safe drinking water")]
    cols = [T, O, P, "#3D7DDB", "#8B6B3E", "#4BB04A"]
    for i, (kind, name, desc) in enumerate(STAGES):
        x = MX + (i % 3) * (cw + gap)
        y = top + (i // 3) * (ch + 24)
        out.append(_card(x, y, cw, ch, th))
        out.append(f'<circle cx="{x + 34}" cy="{y + 36}" r="18" fill="{cols[i]}"/>'
                   + text(str(i + 1), x + 34, y + 43, 18, "#FFFFFF"))
        out.append(fit_text(name, x + 62, y + 44, 21, th["ink"], cw - 80, anchor="start"))
        out.append(_tank(kind, x + 30, y + 70, cw - 60, 150, 70 + i))
        for j, ln in enumerate(_wrap(desc, 14.5, cw - 30)):  # chem() juga merender teks biasa
            out.append(chem(ln, x + cw / 2, y + 252 + j * 21, 14.5, th["ink"], "middle", "SemiBold"))
        if i % 3 < 2:
            out.append(arrow_line(x + cw + 4, y + ch / 2 - 20, x + cw + gap - 4, y + ch / 2 - 20, th["accent"], 4))
    out.append(text("Clean water is stored in reservoirs and piped to homes", W / 2, H - 26, 15, th["sub"],
                    "SemiBold"))
    return W, H, "".join(out)


def ozone(th):
    W = 1226
    top = 122
    H = top + 430 + 20 + 290 + 30
    out = [header(W, th, "OZONE LAYER DEPLETION", "How CFCs destroy the ozone layer that shields us from UV rays")]
    out.append(_card(MX, top, W - 2 * MX, 430, th))
    x0, y0, w, h = MX + 20, top + 20, 560, 390
    layers = [("Space", "#0E1630", 0, .18), ("Stratosphere", "#24406E", .18, .62), ("Troposphere", "#6FA8DC", .62, .9)]
    out.append(f'<clipPath id="oz"><rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="14"/></clipPath>'
               f'<g clip-path="url(#oz)">')
    for name, c, a, b in layers:
        out.append(f'<rect x="{x0}" y="{y0 + h * a:.1f}" width="{w}" height="{h * (b - a) + 1:.1f}" fill="{c}"/>')
        out.append(text(name, x0 + 16, y0 + h * a + 26, 15, "#FFFFFF", "Bold", "start"))
    out.append(f'<rect x="{x0}" y="{y0 + h * .9:.1f}" width="{w}" height="{h * .1 + 2:.1f}" fill="#4BB04A"/>')
    # lapisan ozon dengan lubang
    oy = y0 + h * .3
    out.append(f'<path d="M{x0} {oy}H{x0 + 300}M{x0 + 400} {oy}H{x0 + w}" stroke="#7FD1C7" stroke-width="22" '
               'stroke-linecap="butt"/>')
    out.append(text("Ozone layer (O₃)", x0 + 16, oy + 38, 14, "#7FD1C7", "Bold", "start"))
    out.append(text("Ozone hole", x0 + 372, oy + 38, 14, "#FFC845", "Bold", "start"))
    for ux, blocked in ((x0 + 185, True), (x0 + 258, True), (x0 + 350, False), (x0 + 480, True)):
        end = oy - 14 if blocked else y0 + h * .88
        out.append(f'<path d="M{ux - 30} {y0 + 10}L{ux} {end}" stroke="#B57BFF" stroke-width="5" '
                   'stroke-dasharray="10 6" stroke-linecap="round"/>')
    out.append(text("UV", x0 + 296, y0 + 40, 18, "#B57BFF", "Bold"))
    out.append('</g>')
    # reaksi
    rx = x0 + w + 24
    rw = W - MX - 20 - rx
    out.append(text("Ozone forms", rx + rw / 2, top + 50, 17, th["ink"]))
    for k, e in enumerate(("O_{2} + UV → 2O", "O + O_{2} → O_{3}")):
        out.append(f'<rect x="{rx}" y="{top + 64 + k * 54}" width="{rw}" height="44" rx="10" fill="{th["plate"]}"/>')
        out.append(chem(e, rx + rw / 2, top + 93 + k * 54, 18, INK, "middle"))
    out.append(text("CFCs destroy ozone", rx + rw / 2, top + 210, 17, th["ink"]))
    for k, e in enumerate(("CFCl_{3} + UV → CFCl_{2} + Cl", "Cl + O_{3} → ClO + O_{2}", "ClO + O → Cl + O_{2}")):
        out.append(f'<rect x="{rx}" y="{top + 224 + k * 54}" width="{rw}" height="44" rx="10" '
                   f'fill="{mix(th["card"], R, .2)}"/>')
        out.append(chem(e, rx + rw / 2, top + 253 + k * 54, 18, th["ink"], "middle"))
    out.append(fit_text("One Cl atom can destroy about 100,000 ozone molecules", rx + rw / 2, top + 404, 13.5,
                        th["sub"], rw, "SemiBold"))
    y = top + 450
    cw = (W - 2 * MX - 20) / 2
    out.append(_card(MX, y, cw, 290, th))
    out.append(text("Effects of more UV", MX + cw / 2, y + 40, 18, th["ink"]))
    for k, (e, col) in enumerate((("Skin cancer and sunburn", R), ("Eye damage (cataracts)", O),
                                  ("Weaker immune system", P), ("Harm to crops and plankton", "#4BB04A"))):
        ey = y + 62 + k * 52
        out.append(f'<rect x="{MX + 20}" y="{ey}" width="{cw - 40}" height="42" rx="10" '
                   f'fill="{mix(th["card"], col, .2)}"/>')
        out.append(f'<circle cx="{MX + 44}" cy="{ey + 21}" r="9" fill="{col}"/>')
        out.append(fit_text(e, MX + 64, ey + 27, 15, th["ink"], cw - 100, "SemiBold", "start"))
    x2 = MX + cw + 20
    out.append(_card(x2, y, cw, 290, th))
    out.append(text("Protecting the ozone layer", x2 + cw / 2, y + 40, 18, th["ink"]))
    out.append(f'<rect x="{x2 + 20}" y="{y + 62}" width="{cw - 40}" height="80" rx="12" fill="{th["plate"]}"/>')
    out.append(text("Montreal Protocol (1987)", x2 + cw / 2, y + 96, 20, INK))
    out.append(fit_text("Worldwide ban on CFCs and other ozone-depleting gases", x2 + cw / 2, y + 124, 14, "#5B6878",
                        cw - 70, "SemiBold"))
    for j, ln in enumerate(_wrap("The ozone layer is slowly healing and may fully recover around 2066", 15, cw - 60)):
        out.append(text(ln, x2 + cw / 2, y + 186 + j * 24, 15, th["ink"], "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("water-treatment-process", water_treatment, "Water treatment process chart, coagulation, sedimentation, "
                                                 "filtration and disinfection",
     ["water treatment", "water purification", "coagulation", "flocculation", "sedimentation", "filtration",
      "chlorination", "disinfection", "clean water", "alum", "environmental chemistry", "drinking water",
      "separation", "environment"]),
    ("ozone-layer-depletion", ozone, "Ozone layer depletion chart, CFC reactions, UV radiation and Montreal Protocol",
     ["ozone layer", "ozone depletion", "ozone hole", "cfc", "uv radiation", "stratosphere", "chlorine",
      "montreal protocol", "environment", "environmental chemistry", "atmosphere", "o3", "pollution",
      "climate"]),
]

TR.update({
    "WATER TREATMENT PROCESS": "PROSES PENGOLAHAN AIR BERSIH",
    "How dirty river water becomes clean, safe drinking water":
        "Bagaimana air sungai yang kotor menjadi air minum yang bersih dan aman",
    "Screening": "Penyaringan awal", "Coagulation": "Koagulasi", "Flocculation": "Flokulasi",
    "Sedimentation": "Sedimentasi", "Filtration": "Filtrasi", "Disinfection": "Desinfeksi",
    "Large debris such as leaves and trash is removed": "Kotoran besar seperti daun dan sampah disaring",
    "Alum, Al_{2}(SO_{4})_{3}, is added so dirt particles stick together":
        "Tawas, Al_{2}(SO_{4})_{3}, ditambahkan agar partikel kotoran saling menempel",
    "Gentle mixing forms larger clumps called flocs": "Pengadukan pelan membentuk gumpalan besar (flok)",
    "Heavy flocs settle to the bottom of the tank": "Flok yang berat mengendap di dasar bak",
    "Water passes through sand, gravel and activated charcoal": "Air melewati pasir, kerikil, dan arang aktif",
    "Chlorine or UV light kills remaining germs": "Klorin atau sinar UV membunuh kuman yang tersisa",
    "Clean water is stored in reservoirs and piped to homes": "Air bersih ditampung di reservoir lalu dialirkan ke rumah",
    "OZONE LAYER DEPLETION": "PENIPISAN LAPISAN OZON",
    "How CFCs destroy the ozone layer that shields us from UV rays":
        "Bagaimana CFC merusak lapisan ozon yang melindungi kita dari sinar UV",
    "Space": "Luar angkasa", "Stratosphere": "Stratosfer", "Troposphere": "Troposfer",
    "Ozone layer (O₃)": "Lapisan ozon (O₃)", "Ozone hole": "Lubang ozon", "Ozone forms": "Pembentukan ozon",
    "CFCs destroy ozone": "CFC merusak ozon",
    "One Cl atom can destroy about 100,000 ozone molecules": "Satu atom Cl dapat merusak sekitar 100.000 molekul ozon",
    "Effects of more UV": "Dampak UV berlebih", "Skin cancer and sunburn": "Kanker kulit dan kulit terbakar",
    "Eye damage (cataracts)": "Kerusakan mata (katarak)", "Weaker immune system": "Daya tahan tubuh melemah",
    "Harm to crops and plankton": "Merusak tanaman dan plankton",
    "Protecting the ozone layer": "Melindungi lapisan ozon", "Montreal Protocol (1987)": "Protokol Montreal (1987)",
    "Worldwide ban on CFCs and other ozone-depleting gases": "Larangan global CFC dan gas perusak ozon lainnya",
    "The ozone layer is slowly healing and may fully recover around 2066":
        "Lapisan ozon perlahan pulih dan diperkirakan pulih penuh sekitar tahun 2066",
})
