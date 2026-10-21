"""Poster edukasi kimia jilid 10: tabel ion umum dan elektrolisis air.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
from icons_lab_flat import R
from poster_i18n import TR
from poster_kit import MX, fit_text, header, particle, text
from posters2 import _card
from posters3 import mix
from posters4 import chem
from render import style_attrs

CATIONS = [("Hydrogen", "H^{+}"), ("Sodium", "Na^{+}"), ("Potassium", "K^{+}"), ("Silver", "Ag^{+}"),
           ("Ammonium", "NH_{4}^{+}"), ("Magnesium", "Mg^{2+}"), ("Calcium", "Ca^{2+}"), ("Copper(II)", "Cu^{2+}"),
           ("Zinc", "Zn^{2+}"), ("Iron(II)", "Fe^{2+}"), ("Iron(III)", "Fe^{3+}"), ("Aluminium", "Al^{3+}")]
ANIONS = [("Chloride", "Cl^{−}"), ("Bromide", "Br^{−}"), ("Iodide", "I^{−}"), ("Hydroxide", "OH^{−}"),
          ("Nitrate", "NO_{3}^{−}"), ("Hydrogen carbonate", "HCO_{3}^{−}"), ("Acetate", "CH_{3}COO^{−}"),
          ("Oxide", "O^{2−}"), ("Sulfide", "S^{2−}"), ("Sulfate", "SO_{4}^{2−}"), ("Carbonate", "CO_{3}^{2−}"),
          ("Phosphate", "PO_{4}^{3−}")]


def ions(th):
    W = 1226
    top = 122
    rh = 50
    cw = (W - 2 * MX - 24) / 2
    H = top + 70 + 12 * rh + 70
    out = [header(W, th, "COMMON IONS AND THEIR CHARGES", "Positive ions (cations) and negative ions (anions)")]
    for k, (title, rows, col) in enumerate((("Cations (+)", CATIONS, R), ("Anions (−)", ANIONS, "#3D7DDB"))):
        x = MX + k * (cw + 24)
        out.append(_card(x, top, cw, 70 + 12 * rh + 20, th))
        out.append(f'<rect x="{x}" y="{top}" width="{cw}" height="56" rx="14" fill="{col}"/>'
                   f'<rect x="{x}" y="{top + 30}" width="{cw}" height="26" fill="{col}"/>')
        out.append(text(title, x + cw / 2, top + 37, 22, "#FFFFFF"))
        for i, (name, f) in enumerate(rows):
            y = top + 70 + i * rh
            if i % 2 == 0:
                out.append(f'<rect x="{x + 12}" y="{y}" width="{cw - 24}" height="{rh - 6}" rx="8" '
                           f'fill="{mix(th["card"], col, .1)}"/>')
            out.append(fit_text(name, x + 32, y + 29, 15, th["ink"], cw / 2 - 40, "SemiBold", anchor="start"))
            out.append(chem(f, x + cw - 40, y + 31, 20, th["accent"], "end"))
    out.append(text("Ions combine so that the total charge of a compound is zero, e.g. Ca²⁺ + 2Cl⁻ → CaCl₂",
                    W / 2, H - 28, 13, th["sub"], "SemiBold"))
    return W, H, "".join(out)


def electrolysis(th):
    W = 1226
    top = 122
    ink = "#1E2A3A"
    out = [header(W, th, "ELECTROLYSIS OF WATER", "Electric current splits water into hydrogen and oxygen gas")]
    out.append(f'<rect x="{MX}" y="{top}" width="{W - 2 * MX}" height="430" rx="16" fill="{th["plate"]}"/>')
    g = []
    cx = W / 2 - 150
    # wadah air
    g.append(f'<path d="M{cx - 190} {top + 150}V{top + 380}a14 14 0 0 0 14 14h352a14 14 0 0 0 14-14V{top + 150}" '
             f'fill="#EEF7FA" stroke="{ink}" stroke-width="3"/>')
    g.append(f'<path d="M{cx - 188.5} {top + 190}H{cx + 188.5}V{top + 380}a12 12 0 0 1-12 12H{cx - 176.5}'
             f'a12 12 0 0 1-12-12z" fill="#8CCFF0"/>')
    tubes = [(cx - 95, "H₂", 2, "#E85D4A", "Cathode (−)"), (cx + 95, "O₂", 1, "#3D7DDB", "Anode (+)")]
    for x, gas, vol, col, lab in tubes:
        tw, th_ = 64, 260
        ty = top + 60
        gas_h = 70 * vol
        g.append(f'<rect x="{x - tw / 2}" y="{ty}" width="{tw}" height="{th_}" rx="10" fill="#8CCFF0" '
                 f'stroke="{ink}" stroke-width="3"/>')
        g.append(f'<rect x="{x - tw / 2 + 1.5}" y="{ty + 1.5}" width="{tw - 3}" height="{gas_h}" rx="9" fill="#FFFFFF"/>')
        for k in range(5):
            g.append(particle(x - 14 + (k % 3) * 14, ty + th_ - 30 - k * 26, 4.5, "#FFFFFF", f"bub{x:.0f}{k}",
                              shine=False))
        g.append(f'<rect x="{x - 7}" y="{ty + th_ - 10}" width="14" height="80" fill="#9AA5B1" stroke="{ink}" '
                 'stroke-width="2"/>')
        g.append(text(gas, x, ty + gas_h / 2 + 10, 26, ink))
        g.append(text(lab, x, ty - 14, 15, col, "Bold"))
    # baterai di kiri wadah; kabel lewat bawah wadah
    bx = cx - 360
    g.append(f'<rect x="{bx}" y="{top + 200}" width="110" height="60" rx="8" fill="#5CBF7A" stroke="{ink}" '
             'stroke-width="3"/>' + text("DC", bx + 55, top + 238, 22, "#FFFFFF")
             + text("−", bx + 22, top + 190, 20, ink) + text("+", bx + 88, top + 190, 20, R))
    g.append(f'<path d="M{cx - 95} {top + 390}V{top + 404}H{bx + 22}V{top + 260}" fill="none" stroke="{ink}" '
             'stroke-width="3"/>')
    g.append(f'<path d="M{cx + 95} {top + 390}V{top + 416}H{bx + 88}V{top + 260}" fill="none" stroke="{R}" '
             'stroke-width="3"/>')
    out.append(f'<g {style_attrs(1.4)}>' + "".join(g) + "</g>")
    # keterangan
    rx = W - MX - 300
    out.append(_card(rx, top + 24, 276, 380, th))
    out.append(text("Volume ratio", rx + 138, top + 66, 18, th["ink"]))
    out.append(text("H₂ : O₂ = 2 : 1", rx + 138, top + 100, 22, th["accent"]))
    out.append(text("Cathode (−):", rx + 24, top + 150, 14, th["ink"], "Bold", "start"))
    out.append(text("hydrogen gas forms", rx + 24, top + 172, 13, th["sub"], "Regular", "start"))
    out.append(text("Anode (+):", rx + 24, top + 210, 14, th["ink"], "Bold", "start"))
    out.append(text("oxygen gas forms", rx + 24, top + 232, 13, th["sub"], "Regular", "start"))
    out.append(text("A little acid or salt is added", rx + 24, top + 290, 12, th["sub"], "Regular", "start"))
    out.append(text("so the water conducts electricity.", rx + 24, top + 308, 12, th["sub"], "Regular", "start"))
    out.append(_card(MX, top + 450, W - 2 * MX, 120, th))
    out.append(chem("2H_{2}O(l) → 2H_{2}(g) + O_{2}(g)", W / 2, top + 518, 30, th["accent"], "middle"))
    out.append(text("Overall reaction", W / 2, top + 552, 13, th["sub"], "SemiBold"))
    return W, top + 600, "".join(out)


POSTERS = [
    ("common-ions", ions, "Common ions and their charges chart, cations and anions",
     ["ions", "cations", "anions", "ion charges", "polyatomic ions", "sulfate", "nitrate", "carbonate",
      "ammonium", "chemical formula", "ionic compounds", "valency", "naming", "table"]),
    ("electrolysis-of-water", electrolysis, "Electrolysis of water diagram, hydrogen and oxygen gas",
     ["electrolysis", "water", "hydrogen", "oxygen", "electrolysis of water", "cathode", "anode", "electrochemistry",
      "hoffman apparatus", "gas", "decomposition", "electric current", "battery", "experiment"]),
]

TR.update({
    "COMMON IONS AND THEIR CHARGES": "ION-ION UMUM DAN MUATANNYA",
    "Positive ions (cations) and negative ions (anions)": "Ion positif (kation) dan ion negatif (anion)",
    "Cations (+)": "Kation (+)", "Anions (−)": "Anion (−)", "Silver": "Perak", "Ammonium": "Amonium",
    "Copper(II)": "Tembaga(II)", "Zinc": "Seng", "Iron(II)": "Besi(II)", "Iron(III)": "Besi(III)",
    "Chloride": "Klorida", "Bromide": "Bromida", "Iodide": "Iodida", "Hydroxide": "Hidroksida", "Nitrate": "Nitrat",
    "Hydrogen carbonate": "Hidrogen karbonat", "Acetate": "Asetat", "Oxide": "Oksida", "Sulfide": "Sulfida",
    "Sulfate": "Sulfat", "Carbonate": "Karbonat", "Phosphate": "Fosfat",
    "Ions combine so that the total charge of a compound is zero, e.g. Ca²⁺ + 2Cl⁻ → CaCl₂":
        "Ion bergabung sehingga muatan total senyawa nol, mis. Ca²⁺ + 2Cl⁻ → CaCl₂",
    "ELECTROLYSIS OF WATER": "ELEKTROLISIS AIR",
    "Electric current splits water into hydrogen and oxygen gas": "Arus listrik menguraikan air menjadi gas hidrogen dan oksigen",
    "Cathode (−)": "Katode (−)", "Anode (+)": "Anode (+)", "Volume ratio": "Perbandingan volume",
    "Cathode (−):": "Katode (−):", "Anode (+):": "Anode (+):", "hydrogen gas forms": "terbentuk gas hidrogen",
    "oxygen gas forms": "terbentuk gas oksigen", "A little acid or salt is added": "Sedikit asam atau garam ditambahkan",
    "so the water conducts electricity.": "agar air dapat menghantarkan listrik.", "Overall reaction": "Reaksi keseluruhan",
})
