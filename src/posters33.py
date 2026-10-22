"""Poster edukasi kimia jilid 33: jenis reaksi organik dan jenis baterai (sel elektrokimia).
Didaftarkan ke posters.py lewat POSTERS (semua tema x 2 bahasa).
"""
from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters3 import mix
from posters4 import chem
from textpath import width

INK = "#1E2A3A"

ORGANIC = [
    ("Substitution", "One atom or group is replaced by another", "CH_{4} + Cl_{2} → CH_{3}Cl + HCl", "UV light", T),
    ("Addition", "Atoms add across a C=C double bond", "C_{2}H_{4} + Br_{2} → C_{2}H_{4}Br_{2}", "Bromine water decolorizes", O),
    ("Elimination", "A small molecule is removed to form a double bond", "C_{2}H_{5}OH → C_{2}H_{4} + H_{2}O",
     "Conc. H₂SO₄, heat", P),
    ("Esterification", "An acid and an alcohol form an ester and water",
     "CH_{3}COOH + C_{2}H_{5}OH → CH_{3}COOC_{2}H_{5} + H_{2}O", "Acid catalyst; fruity smell", R),
    ("Combustion", "Burning in oxygen releases carbon dioxide and water", "CH_{4} + 2O_{2} → CO_{2} + 2H_{2}O",
     "Exothermic", "#E0B23A"),
    ("Polymerization", "Many monomers join into a long chain", "n CH_{2}=CH_{2} → (–CH_{2}–CH_{2}–)_{n}",
     "High pressure, catalyst", "#3D7DDB"),
]


def organic(th):
    W = 1226
    top = 122
    rh = 108
    H = top + len(ORGANIC) * (rh + 12) + 20
    out = [header(W, th, "TYPES OF ORGANIC REACTIONS", "Six key reactions of carbon compounds with examples")]
    for i, (name, desc, eq, cond, col) in enumerate(ORGANIC):
        y = top + i * (rh + 12)
        out.append(_card(MX, y, W - 2 * MX, rh, th))
        out.append(f'<rect x="{MX}" y="{y}" width="10" height="{rh}" rx="5" fill="{col}"/>')
        out.append(fit_text(name, MX + 34, y + 42, 21, th["ink"], 300, anchor="start"))
        lines, cur = [], ""
        for w_ in tr(desc).split():
            t = (cur + " " + w_).strip()
            if width(t, 13.5, "SemiBold") > 300 and cur:
                lines.append(cur)
                cur = w_
            else:
                cur = t
        lines.append(cur)
        for j, ln in enumerate(lines[:2]):
            out.append(text(ln, MX + 34, y + 68 + j * 19, 13.5, th["sub"], "SemiBold", "start"))
        bx = MX + 360
        bw = W - MX - 20 - bx
        out.append(f'<rect x="{bx}" y="{y + 14}" width="{bw}" height="54" rx="12" fill="{th["plate"]}"/>')
        out.append(chem(eq, bx + bw / 2, y + 49, 19, INK, "middle"))
        out.append(fit_text(cond, bx + bw / 2, y + 92, 14, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3),
                            bw - 20, "Bold"))
    return W, H, "".join(out)


CELLS = [
    ("Zinc-carbon (dry cell)", "1.5 V", "Zn anode, MnO₂ / carbon cathode", "Remote controls, clocks", "Not rechargeable",
     "#7C8B9C"),
    ("Alkaline", "1.5 V", "Zn anode, MnO₂ cathode, KOH electrolyte", "Toys, flashlights", "Not rechargeable", T),
    ("Lead-acid", "2 V per cell", "Pb and PbO₂ in sulfuric acid", "Car batteries", "Rechargeable", O),
    ("Lithium-ion", "3.6 V", "Li ions move between graphite and metal oxide", "Phones, laptops, electric cars",
     "Rechargeable", P),
    ("Hydrogen fuel cell", "≈ 0.7 V per cell", "2H₂ + O₂ → 2H₂O, only water is produced", "Buses, spacecraft",
     "Refueled with H₂", R),
]


def _battery(cx, cy, col):
    return (f'<rect x="{cx - 24}" y="{cy - 34}" width="48" height="72" rx="9" fill="{col}" stroke="{INK}" '
            f'stroke-width="3"/><rect x="{cx - 10}" y="{cy - 43}" width="20" height="10" rx="3" fill="#B9C2CC" '
            f'stroke="{INK}" stroke-width="3"/>'
            + text("+", cx, cy - 10, 20, "#FFFFFF") + text("−", cx, cy + 28, 20, "#FFFFFF"))


def batteries(th):
    W = 1226
    top = 122
    rh = 118
    H = top + len(CELLS) * (rh + 12) + 50
    out = [header(W, th, "TYPES OF BATTERIES", "Electrochemical cells turn chemical energy into electrical energy")]
    for i, (name, volt, chem_, use, rech, col) in enumerate(CELLS):
        y = top + i * (rh + 12)
        out.append(_card(MX, y, W - 2 * MX, rh, th))
        out.append(f'<rect x="{MX + 16}" y="{y + 12}" width="96" height="{rh - 24}" rx="12" fill="{th["plate"]}"/>')
        out.append(_battery(MX + 64, y + rh / 2 + 6, col))
        out.append(fit_text(name, MX + 136, y + 44, 21, th["ink"], 330, anchor="start"))
        out.append(text(volt, MX + 136, y + 80, 18, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3), "Bold",
                        "start"))
        bx = MX + 500
        out.append(fit_text(chem_, bx, y + 44, 15, th["ink"], W - MX - 230 - bx, "SemiBold", "start"))
        out.append(fit_text(use, bx, y + 80, 15, th["sub"], W - MX - 230 - bx, "SemiBold", "start"))
        rc = "#4BB04A" if rech.startswith("Rech") else ("#3D7DDB" if "H₂" in rech else "#9AA5B1")
        out.append(f'<rect x="{W - MX - 200}" y="{y + rh / 2 - 20}" width="180" height="40" rx="20" fill="{rc}"/>')
        out.append(fit_text(rech, W - MX - 110, y + rh / 2 + 6, 15, "#FFFFFF", 164))
    out.append(text("Anode = negative terminal (oxidation) · Cathode = positive terminal (reduction)", W / 2, H - 20, 13,
                    th["sub"], "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("organic-reaction-types", organic, "Types of organic reactions chart, substitution, addition, elimination, "
                                        "esterification",
     ["organic reactions", "substitution", "addition reaction", "elimination", "esterification", "combustion",
      "polymerization", "organic chemistry", "alkane", "alkene", "ester", "ethanol", "reaction types",
      "hydrocarbons"]),
    ("types-of-batteries", batteries, "Types of batteries chart, dry cell, alkaline, lead-acid, lithium-ion and fuel "
                                      "cell",
     ["batteries", "electrochemical cell", "lithium-ion", "lead-acid", "alkaline battery", "dry cell", "fuel cell",
      "hydrogen", "rechargeable", "voltage", "electrochemistry", "energy", "anode", "cathode"]),
]

TR.update({
    "TYPES OF ORGANIC REACTIONS": "JENIS-JENIS REAKSI ORGANIK",
    "Six key reactions of carbon compounds with examples": "Enam reaksi penting senyawa karbon beserta contohnya",
    "Substitution": "Substitusi", "Addition": "Adisi", "Elimination": "Eliminasi", "Esterification": "Esterifikasi",
    "Combustion": "Pembakaran", "Polymerization": "Polimerisasi",
    "One atom or group is replaced by another": "Satu atom atau gugus digantikan oleh yang lain",
    "Atoms add across a C=C double bond": "Atom-atom ditambahkan pada ikatan rangkap C=C",
    "A small molecule is removed to form a double bond": "Molekul kecil dilepas sehingga terbentuk ikatan rangkap",
    "An acid and an alcohol form an ester and water": "Asam dan alkohol membentuk ester dan air",
    "Burning in oxygen releases carbon dioxide and water": "Pembakaran dengan oksigen menghasilkan CO₂ dan air",
    "Many monomers join into a long chain": "Banyak monomer bergabung menjadi rantai panjang",
    "UV light": "Sinar UV", "Bromine water decolorizes": "Air brom menjadi tidak berwarna",
    "Conc. H₂SO₄, heat": "H₂SO₄ pekat, dipanaskan", "Acid catalyst; fruity smell": "Katalis asam; berbau buah",
    "Exothermic": "Eksoterm", "High pressure, catalyst": "Tekanan tinggi, katalis",
    "TYPES OF BATTERIES": "JENIS-JENIS BATERAI",
    "Electrochemical cells turn chemical energy into electrical energy":
        "Sel elektrokimia mengubah energi kimia menjadi energi listrik",
    "Zinc-carbon (dry cell)": "Seng-karbon (sel kering)", "Alkaline": "Alkalin", "Lead-acid": "Aki timbal",
    "Lithium-ion": "Litium-ion", "Hydrogen fuel cell": "Sel bahan bakar hidrogen", "2 V per cell": "2 V per sel",
    "≈ 0.7 V per cell": "≈ 0,7 V per sel", "1.5 V": "1,5 V", "3.6 V": "3,6 V",
    "Zn anode, MnO₂ / carbon cathode": "Anode Zn, katode MnO₂ / karbon",
    "Zn anode, MnO₂ cathode, KOH electrolyte": "Anode Zn, katode MnO₂, elektrolit KOH",
    "Pb and PbO₂ in sulfuric acid": "Pb dan PbO₂ dalam asam sulfat",
    "Li ions move between graphite and metal oxide": "Ion Li berpindah antara grafit dan oksida logam",
    "2H₂ + O₂ → 2H₂O, only water is produced": "2H₂ + O₂ → 2H₂O, hanya menghasilkan air",
    "Remote controls, clocks": "Remote, jam dinding", "Toys, flashlights": "Mainan, senter", "Car batteries": "Aki mobil",
    "Phones, laptops, electric cars": "Ponsel, laptop, mobil listrik", "Buses, spacecraft": "Bus, wahana antariksa",
    "Not rechargeable": "Tidak dapat diisi ulang", "Rechargeable": "Dapat diisi ulang", "Refueled with H₂": "Diisi ulang H₂",
    "Anode = negative terminal (oxidation) · Cathode = positive terminal (reduction)":
        "Anode = kutub negatif (oksidasi) · Katode = kutub positif (reduksi)",
})
