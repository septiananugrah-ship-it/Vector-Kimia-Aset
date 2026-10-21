"""Poster edukasi kimia jilid 12: sifat koligatif larutan dan asas Le Chatelier.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
from icons_lab_flat import L, O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text
from posters2 import _card
from posters3 import mix
from posters4 import chem

COLLIGATIVE = [
    ("Vapor pressure lowering", "ΔP = X_{solute} × P°", "Dissolved particles lower the vapor pressure of the solvent", T),
    ("Boiling point elevation", "ΔT_{b} = K_{b} × m", "A solution boils at a higher temperature than the pure solvent", R),
    ("Freezing point depression", "ΔT_{f} = K_{f} × m", "A solution freezes at a lower temperature than the pure solvent",
     "#3D7DDB"),
    ("Osmotic pressure", "π = M × R × T", "Pressure needed to stop solvent flowing through a membrane", P),
]


def colligative(th):
    W = 1226
    top = 122
    cw = (W - 2 * MX - 24) / 2
    ch = 250
    H = top + 2 * (ch + 24) + 60
    out = [header(W, th, "COLLIGATIVE PROPERTIES", "Properties that depend on the number of dissolved particles, "
                                                   "not on their identity")]
    for i, (name, f, desc, col) in enumerate(COLLIGATIVE):
        x = MX + (i % 2) * (cw + 24)
        y = top + (i // 2) * (ch + 24)
        out.append(_card(x, y, cw, ch, th))
        out.append(f'<rect x="{x}" y="{y}" width="{cw}" height="8" rx="4" fill="{col}"/>')
        out.append(f'<circle cx="{x + 46}" cy="{y + 54}" r="22" fill="{col}"/>'
                   + text(str(i + 1), x + 46, y + 62, 20, "#FFFFFF"))
        out.append(fit_text(name, x + 82, y + 62, 22, th["ink"], cw - 100, anchor="start"))
        out.append(f'<rect x="{x + 24}" y="{y + 96}" width="{cw - 48}" height="76" rx="12" fill="{th["plate"]}"/>')
        out.append(chem(f, x + cw / 2, y + 144, 28, "#1E2A3A", "middle"))
        out.append(fit_text(desc, x + cw / 2, y + 212, 13, th["sub"], cw - 40, "Regular"))
    out.append(text("m = molality · M = molarity · X = mole fraction · K = solvent constant · R = 0.082 L·atm/(mol·K)",
                    W / 2, H - 28, 12.5, th["sub"], "SemiBold"))
    return W, H, "".join(out)


CHATELIER = [
    ("Add reactant", "→", "Shifts toward products", T),
    ("Remove product", "→", "Shifts toward products", T),
    ("Increase pressure", "⇄", "Shifts toward fewer gas molecules", O),
    ("Increase temperature", "⇄", "Shifts in the endothermic direction", R),
    ("Decrease temperature", "⇄", "Shifts in the exothermic direction", "#3D7DDB"),
    ("Add a catalyst", "=", "No shift; equilibrium is reached faster", L),
]


def eq_arrow(x1, x2, y, col):
    """Panah kesetimbangan ⇌ (dua panah setengah), digambar sebagai vektor."""
    return (f'<path d="M{x1} {y - 4}H{x2}l-8 -7M{x2} {y + 4}H{x1}l8 7" fill="none" stroke="{col}" '
            'stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>')


def chatelier(th):
    W = 1226
    top = 122
    rh = 82
    H = top + 110 + len(CHATELIER) * (rh + 10) + 30
    out = [header(W, th, "LE CHATELIER'S PRINCIPLE",
                  "When an equilibrium is disturbed, it shifts to reduce the change")]
    out.append(_card(MX, top, W - 2 * MX, 90, th))
    cx, cy = W / 2 - 120, top + 47
    out.append(chem("N_{2}(g) + 3H_{2}(g)", cx - 34, cy + 9, 26, th["accent"], "end"))
    out.append(eq_arrow(cx - 24, cx + 24, cy, th["accent"]))
    out.append(chem("2NH_{3}(g)    ΔH = −92 kJ", cx + 34, cy + 9, 26, th["accent"], "start"))
    for i, (change, _sym, effect, col) in enumerate(CHATELIER):
        y = top + 110 + i * (rh + 10)
        out.append(_card(MX, y, W - 2 * MX, rh, th, rx=12))
        out.append(f'<rect x="{MX}" y="{y}" width="10" height="{rh}" rx="5" fill="{col}"/>')
        out.append(fit_text(change, MX + 34, y + rh / 2 + 7, 20, th["ink"], 380, anchor="start"))
        bx = MX + 440
        out.append(f'<rect x="{bx}" y="{y + 14}" width="{W - MX - 18 - bx}" height="{rh - 28}" rx="10" '
                   f'fill="{mix(th["card"], col, .14)}"/>')
        out.append(fit_text(effect, bx + 24, y + rh / 2 + 6, 17, th["ink"], W - MX - 60 - bx, "SemiBold",
                            anchor="start"))
    return W, H, "".join(out)


POSTERS = [
    ("colligative-properties", colligative, "Colligative properties of solutions chart with formulas",
     ["colligative properties", "boiling point elevation", "freezing point depression", "osmotic pressure",
      "vapor pressure", "solution", "molality", "raoult's law", "solute", "solvent", "physical chemistry",
      "formula", "osmosis", "antifreeze"]),
    ("le-chatelier", chatelier, "Le Chatelier's principle chart, factors that shift chemical equilibrium",
     ["le chatelier", "chemical equilibrium", "equilibrium shift", "haber process", "ammonia", "pressure",
      "temperature", "concentration", "catalyst", "reversible reaction", "exothermic", "endothermic",
      "physical chemistry", "dynamic equilibrium"]),
]

TR.update({
    "COLLIGATIVE PROPERTIES": "SIFAT KOLIGATIF LARUTAN",
    "Properties that depend on the number of dissolved particles, not on their identity":
        "Sifat yang bergantung pada jumlah partikel zat terlarut, bukan pada jenisnya",
    "Vapor pressure lowering": "Penurunan tekanan uap", "Boiling point elevation": "Kenaikan titik didih",
    "Freezing point depression": "Penurunan titik beku", "Osmotic pressure": "Tekanan osmotik",
    "Dissolved particles lower the vapor pressure of the solvent":
        "Partikel terlarut menurunkan tekanan uap pelarut",
    "A solution boils at a higher temperature than the pure solvent":
        "Larutan mendidih pada suhu lebih tinggi daripada pelarut murni",
    "A solution freezes at a lower temperature than the pure solvent":
        "Larutan membeku pada suhu lebih rendah daripada pelarut murni",
    "Pressure needed to stop solvent flowing through a membrane":
        "Tekanan yang diperlukan untuk menghentikan aliran pelarut melalui membran",
    "m = molality · M = molarity · X = mole fraction · K = solvent constant · R = 0.082 L·atm/(mol·K)":
        "m = molalitas · M = molaritas · X = fraksi mol · K = tetapan pelarut · R = 0,082 L·atm/(mol·K)",
    "LE CHATELIER'S PRINCIPLE": "ASAS LE CHATELIER",
    "When an equilibrium is disturbed, it shifts to reduce the change":
        "Jika kesetimbangan diganggu, kesetimbangan bergeser untuk mengurangi pengaruh gangguan",
    "Add reactant": "Menambah pereaksi", "Remove product": "Mengurangi hasil reaksi",
    "Increase pressure": "Memperbesar tekanan", "Increase temperature": "Menaikkan suhu",
    "Decrease temperature": "Menurunkan suhu", "Add a catalyst": "Menambah katalis",
    "Shifts toward products": "Bergeser ke arah hasil reaksi",
    "Shifts toward fewer gas molecules": "Bergeser ke arah jumlah molekul gas lebih sedikit",
    "Shifts in the endothermic direction": "Bergeser ke arah reaksi endoterm",
    "Shifts in the exothermic direction": "Bergeser ke arah reaksi eksoterm",
    "No shift; equilibrium is reached faster": "Tidak bergeser; kesetimbangan tercapai lebih cepat",
})
