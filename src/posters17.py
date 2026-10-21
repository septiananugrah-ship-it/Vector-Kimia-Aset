"""Poster edukasi kimia jilid 17: aturan kelarutan dan gaya antarmolekul.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, particle, text, tr
from posters2 import _card
from posters3 import mix
from posters4 import chem
from render import style_attrs

SOLUBLE = "#4BB04A"
INSOLUBLE = "#E8573F"
RULES = [
    (True, "Na^{+}, K^{+}, NH_{4}^{+} (group 1) salts", "no common exceptions"),
    (True, "Nitrates NO_{3}^{−} and acetates CH_{3}COO^{−}", "no common exceptions"),
    (True, "Chlorides, bromides, iodides (Cl^{−}, Br^{−}, I^{−})", "except Ag^{+}, Pb^{2+}, Hg_{2}^{2+}"),
    (True, "Sulfates SO_{4}^{2−}", "except Ba^{2+}, Pb^{2+}, Sr^{2+}, Ca^{2+}"),
    (False, "Carbonates CO_{3}^{2−} and phosphates PO_{4}^{3−}", "except group 1 and NH_{4}^{+}"),
    (False, "Hydroxides OH^{−}", "except group 1, Ba^{2+} (Ca^{2+} slightly)"),
    (False, "Sulfides S^{2−}", "except group 1, group 2 and NH_{4}^{+}"),
]


def solubility(th):
    W = 1226
    top = 122
    rh = 78
    H = top + len(RULES) * (rh + 10) + 60
    out = [header(W, th, "SOLUBILITY RULES", "Which ionic compounds dissolve in water")]
    for i, (sol, ions, exc) in enumerate(RULES):
        y = top + i * (rh + 10)
        col = SOLUBLE if sol else INSOLUBLE
        out.append(_card(MX, y, W - 2 * MX, rh, th, rx=12))
        out.append(f'<rect x="{MX + 16}" y="{y + 16}" width="150" height="{rh - 32}" rx="23" fill="{col}"/>')
        out.append(text("Soluble" if sol else "Insoluble", MX + 91, y + rh / 2 + 6, 16, "#FFFFFF"))
        out.append(chem(tr(ions), MX + 192, y + rh / 2 + 7, 19, th["ink"], "start"))
        bx = MX + 690
        out.append(f'<rect x="{bx}" y="{y + 14}" width="{W - MX - 16 - bx}" height="{rh - 28}" rx="10" '
                   f'fill="{mix(th["card"], col, .14)}"/>')
        out.append(chem(tr(exc), bx + (W - MX - 16 - bx) / 2, y + rh / 2 + 6, 16, th["ink"], "middle", "SemiBold"))
    out.append(text("Insoluble compounds form a precipitate when their ions meet in solution", W / 2, H - 26, 14,
                    th["sub"], "SemiBold"))
    return W, H, "".join(out)


FORCES = [
    ("London dispersion", "All molecules, especially nonpolar ones", "Cl_{2}, CH_{4}, I_{2}", 1, T),
    ("Dipole–dipole", "Between polar molecules", "HCl, SO_{2}, CH_{3}Cl", 2, O),
    ("Hydrogen bond", "H bonded to N, O or F", "H_{2}O, NH_{3}, HF", 3, P),
    ("Ion–dipole", "Ions dissolved in a polar solvent", "NaCl in water", 4, R),
]


def _pair(kind, cx, cy, th, key):
    """Ilustrasi dua partikel dan gaya tarik di antaranya."""
    out = [f'<g {style_attrs(1.6)}>']
    dash = f'stroke="{th["accent"]}" stroke-width="3" stroke-dasharray="3 6" stroke-linecap="round" fill="none"'
    if kind == 1:
        for k, dx in enumerate((-48, 48)):
            out.append(particle(cx + dx, cy, 30, "#7FC8D6", f"{key}{k}"))
        out.append(f'<path d="M{cx - 14} {cy}H{cx + 14}" {dash}/>')
        out.append(text("δ⁻ δ⁺", cx - 48, cy + 52, 13, th["sub"], "SemiBold") +
                   text("δ⁻ δ⁺", cx + 48, cy + 52, 13, th["sub"], "SemiBold"))
    elif kind == 2:
        for k, dx in enumerate((-58, 46)):
            out.append(particle(cx + dx - 14, cy, 22, "#F2A541", f"{key}a{k}"))
            out.append(particle(cx + dx + 16, cy, 17, "#E8EEF3", f"{key}b{k}"))
            out.append(text("δ⁻", cx + dx - 14, cy - 30, 14, th["ink"]) + text("δ⁺", cx + dx + 16, cy - 30, 14,
                                                                                th["ink"]))
        out.append(f'<path d="M{cx - 20} {cy}H{cx + 8}" {dash}/>')
    elif kind == 3:
        for k, (dx, dy) in enumerate(((-54, -6), (52, 12))):
            ox, oy = cx + dx, cy + dy
            out.append(f'<path d="M{ox} {oy}L{ox - 20} {oy + 22}M{ox} {oy}L{ox + 22} {oy + 18}" stroke="{th["sub"]}" '
                       'stroke-width="5" stroke-linecap="round"/>')
            out.append(particle(ox - 20, oy + 22, 12, "#E8EEF3", f"{key}h{k}"))
            out.append(particle(ox + 22, oy + 18, 12, "#E8EEF3", f"{key}g{k}"))
            out.append(particle(ox, oy, 21, "#E8573F", f"{key}o{k}"))
        out.append(f'<path d="M{cx - 24} {cy + 14}L{cx + 30} {cy + 10}" {dash}/>')
    else:
        out.append(particle(cx - 46, cy, 26, "#9B7FE0", f"{key}n"))
        out.append(text("+", cx - 46, cy + 9, 26, "#FFFFFF"))
        for k, (dx, dy) in enumerate(((34, -30), (40, 30))):
            ox, oy = cx + dx, cy + dy
            out.append(particle(ox, oy, 17, "#E8573F", f"{key}w{k}"))
            out.append(particle(ox + 22, oy - 10, 9, "#E8EEF3", f"{key}x{k}"))
            out.append(particle(ox + 22, oy + 10, 9, "#E8EEF3", f"{key}y{k}"))
            out.append(f'<path d="M{cx - 18} {cy + dy * .35}L{ox - 18} {oy - dy * .1}" {dash}/>')
    out.append('</g>')
    return "".join(out)


def forces(th):
    W = 1226
    top = 122
    rh = 132
    H = top + 4 * (rh + 14) + 60
    out = [header(W, th, "INTERMOLECULAR FORCES", "Attractions between molecules, from weakest to strongest")]
    for i, (name, where, ex, lvl, col) in enumerate(FORCES):
        y = top + i * (rh + 14)
        out.append(_card(MX, y, W - 2 * MX, rh, th))
        out.append(f'<rect x="{MX}" y="{y}" width="10" height="{rh}" rx="5" fill="{col}"/>')
        out.append(f'<rect x="{MX + 30}" y="{y + 14}" width="230" height="{rh - 28}" rx="12" fill="{th["plate"]}"/>')
        out.append(_pair(lvl, MX + 145, y + rh / 2 - 4, dict(th, sub="#5B6878", ink="#1E2A3A",
                                                              accent="#1E2A3A"), f"im{i}"))
        out.append(fit_text(name, MX + 290, y + 46, 22, th["ink"], 420, anchor="start"))
        out.append(fit_text(where, MX + 290, y + 78, 15, th["sub"], 420, "SemiBold", anchor="start"))
        out.append(chem(tr(ex), MX + 290, y + 108, 16, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3),
                        "start"))
        bx = MX + 760
        bw = W - MX - 30 - bx
        out.append(text("Strength", bx + bw / 2, y + 46, 13, th["sub"], "SemiBold"))
        seg = (bw - 3 * 8) / 4
        for k in range(4):
            fill = col if k < lvl else mix(th["card"], th["sub"], .2)
            out.append(f'<rect x="{bx + k * (seg + 8):.1f}" y="{y + 62}" width="{seg:.1f}" height="26" rx="8" '
                       f'fill="{fill}"/>')
    out.append(text("Stronger forces → higher boiling and melting points", W / 2, H - 26, 15, th["sub"], "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("solubility-rules", solubility, "Solubility rules chart for ionic compounds in water with exceptions",
     ["solubility rules", "solubility", "soluble", "insoluble", "precipitate", "ionic compounds", "salts", "nitrate",
      "chloride", "sulfate", "carbonate", "hydroxide", "precipitation reaction", "aqueous solution"]),
    ("intermolecular-forces", forces, "Intermolecular forces chart, London dispersion, dipole-dipole, hydrogen bond",
     ["intermolecular forces", "london dispersion", "van der waals", "dipole dipole", "hydrogen bond", "ion dipole",
      "polarity", "boiling point", "water molecule", "polar molecule", "nonpolar", "attraction", "molecules",
      "physical properties"]),
]

TR.update({
    "SOLUBILITY RULES": "ATURAN KELARUTAN",
    "Which ionic compounds dissolve in water": "Senyawa ion mana yang larut dalam air",
    "Soluble": "Larut", "Insoluble": "Sukar larut",
    "Na^{+}, K^{+}, NH_{4}^{+} (group 1) salts": "Garam Na^{+}, K^{+}, NH_{4}^{+} (golongan IA)",
    "Nitrates NO_{3}^{−} and acetates CH_{3}COO^{−}": "Nitrat NO_{3}^{−} dan asetat CH_{3}COO^{−}",
    "Chlorides, bromides, iodides (Cl^{−}, Br^{−}, I^{−})": "Klorida, bromida, iodida (Cl^{−}, Br^{−}, I^{−})",
    "Sulfates SO_{4}^{2−}": "Sulfat SO_{4}^{2−}",
    "Carbonates CO_{3}^{2−} and phosphates PO_{4}^{3−}": "Karbonat CO_{3}^{2−} dan fosfat PO_{4}^{3−}",
    "Hydroxides OH^{−}": "Hidroksida OH^{−}", "Sulfides S^{2−}": "Sulfida S^{2−}",
    "no common exceptions": "tanpa pengecualian umum",
    "except Ag^{+}, Pb^{2+}, Hg_{2}^{2+}": "kecuali Ag^{+}, Pb^{2+}, Hg_{2}^{2+}",
    "except Ba^{2+}, Pb^{2+}, Sr^{2+}, Ca^{2+}": "kecuali Ba^{2+}, Pb^{2+}, Sr^{2+}, Ca^{2+}",
    "except group 1 and NH_{4}^{+}": "kecuali golongan IA dan NH_{4}^{+}",
    "except group 1, Ba^{2+} (Ca^{2+} slightly)": "kecuali golongan IA, Ba^{2+} (Ca^{2+} sedikit larut)",
    "except group 1, group 2 and NH_{4}^{+}": "kecuali golongan IA, IIA dan NH_{4}^{+}",
    "Insoluble compounds form a precipitate when their ions meet in solution":
        "Senyawa yang sukar larut membentuk endapan saat ion-ionnya bertemu dalam larutan",
    "INTERMOLECULAR FORCES": "GAYA ANTARMOLEKUL",
    "Attractions between molecules, from weakest to strongest": "Gaya tarik antarmolekul, dari terlemah hingga terkuat",
    "London dispersion": "Gaya London (dispersi)", "Dipole–dipole": "Dipol–dipol", "Hydrogen bond": "Ikatan hidrogen",
    "Ion–dipole": "Ion–dipol",
    "All molecules, especially nonpolar ones": "Semua molekul, terutama molekul nonpolar",
    "Between polar molecules": "Antara molekul-molekul polar", "H bonded to N, O or F": "H yang terikat pada N, O atau F",
    "Ions dissolved in a polar solvent": "Ion yang terlarut dalam pelarut polar", "NaCl in water": "NaCl dalam air",
    "Strength": "Kekuatan",
    "Stronger forces → higher boiling and melting points": "Gaya makin kuat → titik didih dan titik leleh makin tinggi",
})
