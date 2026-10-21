"""Poster edukasi kimia jilid 11: rumus konsentrasi larutan dan perbandingan
alkana, alkena, alkuna. Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
import molecules
from icons_lab_flat import L, O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, icon_at, text, tr
from posters2 import _card
from posters3 import mix
from posters4 import chem

CONC = [
    ("Molarity", "M = n / V", "n = moles of solute, V = volume of solution (L)", "mol/L", T),
    ("Molality", "m = n / kg solvent", "moles of solute per kilogram of solvent", "mol/kg", O),
    ("Mass percent", "% = (mass solute / mass solution) × 100", "grams of solute per 100 g of solution", "%", P),
    ("Parts per million", "ppm = (mass solute / mass solution) × 10^{6}", "used for very dilute solutions", "ppm", R),
    ("Dilution", "M_{1}V_{1} = M_{2}V_{2}", "moles of solute stay the same when water is added", "", L),
]


def concentration(th):
    W = 1226
    top = 122
    rh = 104
    H = top + len(CONC) * (rh + 12) + 26
    out = [header(W, th, "SOLUTION CONCENTRATION", "Formulas for expressing how much solute is dissolved")]
    for i, (name, f, desc, unit, col) in enumerate(CONC):
        y = top + i * (rh + 12)
        out.append(_card(MX, y, W - 2 * MX, rh, th))
        out.append(f'<rect x="{MX}" y="{y}" width="10" height="{rh}" rx="5" fill="{col}"/>')
        out.append(text(name, MX + 32, y + 44, 21, th["ink"], "Bold", "start"))
        out.append(fit_text(desc, MX + 32, y + 74, 13, th["sub"], 400, "Regular", anchor="start"))
        bx = MX + 470
        bw = W - MX - 22 - bx - (110 if unit else 0)
        out.append(f'<rect x="{bx}" y="{y + 20}" width="{bw}" height="{rh - 40}" rx="12" fill="{th["plate"]}"/>')
        out.append(chem(tr(f), bx + bw / 2, y + rh / 2 + 8, 20, "#1E2A3A", "middle"))
        if unit:
            out.append(f'<rect x="{bx + bw + 12}" y="{y + 30}" width="96" height="{rh - 60}" rx="22" fill="{col}"/>'
                       + text(unit, bx + bw + 60, y + rh / 2 + 7, 17, "#FFFFFF"))
    return W, H, "".join(out)


HC = [
    ("Alkane", "C_{n}H_{2n+2}", "single bonds only", "-ane", "Methane", "CH_{4}", "substitution", T, "methane"),
    ("Alkene", "C_{n}H_{2n}", "one C=C double bond", "-ene", "Ethene", "C_{2}H_{4}", "addition", O, "ethylene"),
    ("Alkyne", "C_{n}H_{2n−2}", "one triple bond", "-yne", "Ethyne", "C_{2}H_{2}", "addition", P, "acetylene"),
]


def hydrocarbons(th):
    W = 1226
    top = 122
    cw = (W - 2 * MX - 2 * 18) / 3
    ch = 520
    H = top + ch + 30
    mols = {ic["id"]: ic["body"] for ic in molecules.ICONS}
    out = [header(W, th, "ALKANES, ALKENES AND ALKYNES", "Comparing the three families of simple hydrocarbons")]
    rows = ("General formula", "Bond type", "Name ending", "Example", "Typical reaction")
    for k, (fam, gen, bond, suf, ex, exf, rxn, col, mol) in enumerate(HC):
        x = MX + k * (cw + 18)
        out.append(_card(x, top, cw, ch, th))
        out.append(f'<rect x="{x}" y="{top}" width="{cw}" height="60" rx="14" fill="{col}"/>'
                   f'<rect x="{x}" y="{top + 34}" width="{cw}" height="26" fill="{col}"/>')
        out.append(text(fam, x + cw / 2, top + 40, 24, "#FFFFFF"))
        out.append(f'<circle cx="{x + cw / 2}" cy="{top + 140}" r="62" fill="{th["plate"]}"/>')
        out.append(icon_at(mols[mol], molecules.STROKE, x + cw / 2 - 48, top + 92, 96))
        vals = [(gen, True), (bond, False), (suf, False), (f"{ex} ({exf})", None), (rxn, False)]
        for i, (lab, (v, is_f)) in enumerate(zip(rows, vals)):
            y = top + 226 + i * 56
            out.append(f'<rect x="{x + 14}" y="{y}" width="{cw - 28}" height="48" rx="10" '
                       f'fill="{mix(th["card"], col, .1)}"/>')
            out.append(text(lab, x + 28, y + 19, 11, th["sub"], "SemiBold", "start"))
            if is_f is None:
                name, f = v.split(" (")
                out.append(chem(f"{tr(name)} ({f}", x + 28, y + 39, 15, th["ink"], "start"))
            elif is_f:
                out.append(chem(v, x + 28, y + 40, 16, th["accent"], "start"))
            else:
                out.append(fit_text(v, x + 28, y + 39, 15, th["ink"], cw - 56, "Bold", anchor="start"))
    return W, H, "".join(out)


POSTERS = [
    ("solution-concentration", concentration, "Solution concentration formulas chart, molarity, molality, "
     "percent, ppm and dilution",
     ["concentration", "molarity", "molality", "mass percent", "ppm", "dilution", "solution", "solute", "solvent",
      "formula", "stoichiometry", "calculation", "mol per liter", "chemistry math"]),
    ("hydrocarbons", hydrocarbons, "Alkanes, alkenes and alkynes comparison chart",
     ["hydrocarbons", "alkane", "alkene", "alkyne", "general formula", "single bond", "double bond", "triple bond",
      "ethane", "ethene", "ethyne", "organic chemistry", "addition reaction", "substitution"]),
]

TR.update({
    "SOLUTION CONCENTRATION": "KONSENTRASI LARUTAN",
    "Formulas for expressing how much solute is dissolved": "Rumus untuk menyatakan banyaknya zat terlarut",
    "Molarity": "Molaritas", "Molality": "Molalitas", "Mass percent": "Persen massa",
    "Parts per million": "Bagian per sejuta (bpj)", "Dilution": "Pengenceran",
    "n = moles of solute, V = volume of solution (L)": "n = mol zat terlarut, V = volume larutan (L)",
    "moles of solute per kilogram of solvent": "mol zat terlarut per kilogram pelarut",
    "grams of solute per 100 g of solution": "gram zat terlarut dalam 100 g larutan",
    "used for very dilute solutions": "dipakai untuk larutan yang sangat encer",
    "moles of solute stay the same when water is added": "mol zat terlarut tetap saat air ditambahkan",
    "m = n / kg solvent": "m = n / kg pelarut",
    "% = (mass solute / mass solution) × 100": "% = (massa terlarut / massa larutan) × 100",
    "ppm = (mass solute / mass solution) × 10^{6}": "bpj = (massa terlarut / massa larutan) × 10^{6}",
    "ALKANES, ALKENES AND ALKYNES": "ALKANA, ALKENA, DAN ALKUNA",
    "Comparing the three families of simple hydrocarbons": "Perbandingan tiga golongan hidrokarbon sederhana",
    "General formula": "Rumus umum", "Bond type": "Jenis ikatan", "Name ending": "Akhiran nama",
    "Typical reaction": "Reaksi khas", "single bonds only": "hanya ikatan tunggal",
    "one C=C double bond": "satu ikatan rangkap dua C=C", "one triple bond": "satu ikatan rangkap tiga C≡C",
    "substitution": "substitusi", "addition": "adisi",
})
