"""Poster edukasi kimia jilid 36: kalorimetri dan perhitungan entalpi dari energi ikatan.
Didaftarkan ke posters.py lewat POSTERS (semua tema x 2 bahasa).
"""
from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters3 import mix
from posters4 import chem

INK = "#1E2A3A"


def _calorimeter(cx, cy):
    out = []
    # cangkir styrofoam berlapis + tutup + termometer + pengaduk
    out.append(f'<path d="M{cx - 90} {cy - 70}L{cx - 74} {cy + 90}H{cx + 74}L{cx + 90} {cy - 70}Z" fill="#F4F5F7" '
               f'stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>')
    out.append(f'<path d="M{cx - 70} {cy - 54}L{cx - 58} {cy + 76}H{cx + 58}L{cx + 70} {cy - 54}Z" fill="#E9EEF3" '
               f'stroke="#9AA5B1" stroke-width="2" stroke-linejoin="round"/>')
    out.append(f'<path d="M{cx - 66} {cy - 20}L{cx - 58} {cy + 76}H{cx + 58}L{cx + 66} {cy - 20}Z" fill="#9FD3EC"/>')
    out.append(f'<rect x="{cx - 100}" y="{cy - 86}" width="200" height="18" rx="6" fill="#C9D3DE" stroke="{INK}" '
               'stroke-width="3"/>')
    out.append(f'<rect x="{cx + 14}" y="{cy - 170}" width="12" height="200" rx="6" fill="#FFFFFF" stroke="{INK}" '
               f'stroke-width="2.5"/><rect x="{cx + 17}" y="{cy - 90}" width="6" height="116" fill="#E8573F"/>'
               f'<circle cx="{cx + 20}" cy="{cy + 34}" r="10" fill="#E8573F" stroke="{INK}" stroke-width="2.5"/>')
    out.append(f'<path d="M{cx - 30} {cy - 150}V{cy + 50}M{cx - 46} {cy + 50}H{cx - 14}" stroke="#7C8B9C" '
               'stroke-width="5" stroke-linecap="round"/>')
    return "".join(out)


def calorimetry(th):
    W = 1226
    top = 122
    H = top + 430 + 20 + 230 + 30
    out = [header(W, th, "CALORIMETRY", "Measuring the heat released or absorbed by a reaction")]
    out.append(_card(MX, top, 520, 430, th))
    out.append(f'<rect x="{MX + 20}" y="{top + 20}" width="480" height="390" rx="14" fill="{th["plate"]}"/>')
    out.append(_calorimeter(MX + 260, top + 250))
    labels = [("Thermometer", MX + 300, top + 70, "start"), ("Stirrer", MX + 220, top + 110, "end"),
              ("Lid", MX + 380, top + 168, "start"), ("Insulated cup", MX + 350, top + 330, "start")]
    for lab, lx, ly, anc in labels:
        out.append(text(lab, lx, ly, 15, INK, "Bold", anc))
    rx = MX + 540
    rw = W - MX - rx
    out.append(_card(rx, top, rw, 430, th))
    out.append(text("Heat formula", rx + rw / 2, top + 44, 18, th["ink"]))
    out.append(f'<rect x="{rx + 24}" y="{top + 62}" width="{rw - 48}" height="80" rx="14" fill="{th["plate"]}"/>')
    out.append(chem("q = m × c × ΔT", rx + rw / 2, top + 114, 34, INK, "middle"))
    terms = [("q", "heat energy (J)", T), ("m", "mass of water (g)", O), ("c", "specific heat of water = 4.18 J/g·°C", P),
             ("ΔT", "temperature change (°C)", R)]
    for k, (sym, desc, col) in enumerate(terms):
        y = top + 166 + k * 54
        out.append(f'<rect x="{rx + 24}" y="{y}" width="{rw - 48}" height="44" rx="10" '
                   f'fill="{mix(th["card"], col, .18)}"/>')
        out.append(text(sym, rx + 64, y + 30, 20, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3)))
        out.append(fit_text(desc, rx + 104, y + 29, 15, th["ink"], rw - 150, "SemiBold", "start"))
    out.append(chem(tr("ΔH = −q ÷ n  (kJ/mol)"), rx + rw / 2, top + 400, 20, th["accent"], "middle"))
    y = top + 450
    out.append(_card(MX, y, W - 2 * MX, 230, th))
    out.append(text("Worked example", W / 2, y + 40, 18, th["ink"]))
    steps = ["50 g of water warms from 25 °C to 35 °C", "q = 50 × 4.18 × 10 = 2,090 J = 2.09 kJ",
             "Temperature rises → the reaction is exothermic (ΔH < 0)"]
    for k, s_ in enumerate(steps):
        out.append(f'<rect x="{MX + 30}" y="{y + 62 + k * 52}" width="{W - 2 * MX - 60}" height="42" rx="10" '
                   f'fill="{mix(th["card"], th["accent"], .12)}"/>')
        out.append(fit_text(s_, W / 2, y + 90 + k * 52, 16, th["ink"], W - 2 * MX - 100, "SemiBold"))
    return W, H, "".join(out)


BONDS = [("H–H", "436"), ("Cl–Cl", "243"), ("H–Cl", "432"), ("O=O", "498"), ("O–H", "463"), ("C–H", "413"),
         ("C=O", "799"), ("C–C", "347")]


def bond_energy(th):
    W = 1226
    top = 122
    H = top + 180 + 20 + 330 + 20 + 150 + 30
    out = [header(W, th, "BOND ENERGIES", "Breaking bonds absorbs energy, making bonds releases energy")]
    out.append(_card(MX, top, W - 2 * MX, 180, th))
    out.append(f'<rect x="{MX + 30}" y="{top + 30}" width="{W - 2 * MX - 60}" height="76" rx="14" '
               f'fill="{th["plate"]}"/>')
    out.append(chem(tr("ΔH = Σ bonds broken − Σ bonds formed"), W / 2, top + 80, 30, INK, "middle"))
    for k, (lab, col) in enumerate((("Bonds broken: endothermic (+)", R), ("Bonds formed: exothermic (−)", T))):
        bx = MX + 30 + k * ((W - 2 * MX - 60) / 2 + 0)
        out.append(fit_text(lab, bx + (W - 2 * MX - 60) / 4, top + 148, 16,
                            col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3), (W - 2 * MX - 60) / 2 - 20))
    y = top + 200
    out.append(_card(MX, y, W - 2 * MX, 330, th))
    out.append(text("Example: H₂ + Cl₂ → 2HCl", W / 2, y + 42, 20, th["ink"]))
    cw = (W - 2 * MX - 60 - 20) / 2
    for k, (title, rows, total, col) in enumerate((
            ("Bonds broken", ["1 × H–H = 436", "1 × Cl–Cl = 243"], "Total = +679 kJ", R),
            ("Bonds formed", ["2 × H–Cl = 2 × 432"], "Total = −864 kJ", T))):
        x = MX + 30 + k * (cw + 20)
        out.append(f'<rect x="{x}" y="{y + 66}" width="{cw}" height="170" rx="14" fill="{mix(th["card"], col, .16)}"/>')
        out.append(text(title, x + cw / 2, y + 100, 17, th["ink"]))
        for j, r_ in enumerate(rows):
            out.append(text(r_, x + cw / 2, y + 140 + j * 30, 17, th["ink"], "SemiBold"))
        out.append(text(total, x + cw / 2, y + 220, 19, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3)))
    out.append(f'<rect x="{W / 2 - 220}" y="{y + 254}" width="440" height="52" rx="26" fill="{th["accent"]}"/>')
    out.append(text("ΔH = 679 − 864 = −185 kJ", W / 2, y + 288, 20, "#FFFFFF"))
    y += 350
    out.append(_card(MX, y, W - 2 * MX, 150, th))
    out.append(text("Average bond energies (kJ/mol)", W / 2, y + 36, 17, th["ink"]))
    bw = (W - 2 * MX - 40 - 7 * 10) / 8
    for k, (b, e) in enumerate(BONDS):
        bx = MX + 20 + k * (bw + 10)
        out.append(f'<rect x="{bx:.1f}" y="{y + 54}" width="{bw:.1f}" height="74" rx="12" fill="{th["plate"]}"/>')
        out.append(text(b, bx + bw / 2, y + 84, 17, INK))
        out.append(text(e, bx + bw / 2, y + 114, 16, "#5B6878", "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("calorimetry", calorimetry, "Calorimetry chart, coffee cup calorimeter, q = mcΔT formula and worked example",
     ["calorimetry", "calorimeter", "specific heat", "heat energy", "enthalpy", "thermochemistry", "temperature change",
      "exothermic", "endothermic", "q mcat", "joule", "experiment", "energy", "formula"]),
    ("bond-energies", bond_energy, "Bond energies chart, calculating enthalpy change from bonds broken and formed",
     ["bond energy", "bond enthalpy", "enthalpy change", "thermochemistry", "bonds broken", "bonds formed",
      "exothermic", "endothermic", "hydrogen chloride", "calculation", "energy", "chemical bonds", "kj/mol",
      "worked example"]),
]

TR.update({
    "CALORIMETRY": "KALORIMETRI", "Measuring the heat released or absorbed by a reaction":
        "Mengukur kalor yang dilepas atau diserap suatu reaksi",
    "Thermometer": "Termometer", "Stirrer": "Pengaduk", "Lid": "Tutup", "Insulated cup": "Gelas berinsulasi",
    "Heat formula": "Rumus kalor", "heat energy (J)": "kalor (J)", "mass of water (g)": "massa air (g)",
    "specific heat of water = 4.18 J/g·°C": "kalor jenis air = 4,18 J/g·°C", "temperature change (°C)": "perubahan suhu (°C)",
    "ΔH = −q ÷ n  (kJ/mol)": "ΔH = −q ÷ n  (kJ/mol)", "Worked example": "Contoh soal",
    "50 g of water warms from 25 °C to 35 °C": "50 g air memanas dari 25 °C menjadi 35 °C",
    "q = 50 × 4.18 × 10 = 2,090 J = 2.09 kJ": "q = 50 × 4,18 × 10 = 2.090 J = 2,09 kJ",
    "Temperature rises → the reaction is exothermic (ΔH < 0)": "Suhu naik → reaksi bersifat eksoterm (ΔH < 0)",
    "BOND ENERGIES": "ENERGI IKATAN",
    "Breaking bonds absorbs energy, making bonds releases energy":
        "Pemutusan ikatan menyerap energi, pembentukan ikatan melepas energi",
    "ΔH = Σ bonds broken − Σ bonds formed": "ΔH = Σ ikatan diputus − Σ ikatan dibentuk",
    "Bonds broken: endothermic (+)": "Ikatan diputus: endoterm (+)", "Bonds formed: exothermic (−)": "Ikatan dibentuk: eksoterm (−)",
    "Example: H₂ + Cl₂ → 2HCl": "Contoh: H₂ + Cl₂ → 2HCl", "Bonds broken": "Ikatan diputus", "Bonds formed": "Ikatan dibentuk",
    "Average bond energies (kJ/mol)": "Energi ikatan rata-rata (kJ/mol)",
})
