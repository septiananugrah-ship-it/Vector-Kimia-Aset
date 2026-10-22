"""Poster edukasi kimia jilid 35: rumus perhitungan pH dan langkah menentukan rumus empiris & molekul.
Didaftarkan ke posters.py lewat POSTERS (semua tema x 2 bahasa).
"""
from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters3 import arrow_line, mix
from posters4 import chem

INK = "#1E2A3A"


def _formula_card(x, y, w, h, title, formula, note, col, th, size=24):
    out = [_card(x, y, w, h, th),
           f'<rect x="{x}" y="{y}" width="{w}" height="8" rx="4" fill="{col}"/>',
           fit_text(title, x + w / 2, y + 40, 17, th["ink"], w - 24),
           f'<rect x="{x + 18}" y="{y + 56}" width="{w - 36}" height="62" rx="12" fill="{th["plate"]}"/>',
           chem(tr(formula), x + w / 2, y + 96, size, INK, "middle")]
    if note:
        out.append(fit_text(note, x + w / 2, y + h - 18, 13.5, th["sub"], w - 24, "SemiBold"))
    return "".join(out)


def ph_calc(th):
    W = 1226
    top = 122
    gap = 18
    cw = (W - 2 * MX - 2 * gap) / 3
    ch = 160
    H = top + 2 * (ch + gap) + 20 + 280 + 30
    out = [header(W, th, "CALCULATING pH", "Key formulas for acids, bases and water")]
    cards = [("pH", "pH = −log[H^{+}]", "[H⁺] in mol/L", T), ("pOH", "pOH = −log[OH^{−}]", "[OH⁻] in mol/L", "#3D62C4"),
             ("Water at 25 °C", "K_{w} = [H^{+}][OH^{−}] = 10^{−14}", "pH + pOH = 14", P),
             ("Strong acid", "[H^{+}] = a × M", "a = number of H⁺ released", R),
             ("Strong base", "[OH^{−}] = b × M", "b = number of OH⁻ released", O),
             ("Weak acid", "[H^{+}] = √(K_{a} × M)", "Weak base: [OH⁻] = √(Kb × M)", "#4BB04A")]
    for i, (title, f, note, col) in enumerate(cards):
        x = MX + (i % 3) * (cw + gap)
        y = top + (i // 3) * (ch + gap)
        out.append(_formula_card(x, y, cw, ch, title, f, note, col, th, 21))
    y = top + 2 * (ch + gap) + 20
    out.append(_card(MX, y, W - 2 * MX, 280, th))
    out.append(text("Worked examples", W / 2, y + 40, 18, th["ink"]))
    ex = [("0.01 M HCl", "[H⁺] = 1 × 0.01 = 10⁻² M", "pH = 2", R),
          ("0.001 M NaOH", "[OH⁻] = 10⁻³ M → pOH = 3", "pH = 11", O),
          ("0.1 M CH₃COOH (Ka = 10⁻⁵)", "[H⁺] = √(10⁻⁵ × 0.1) = 10⁻³ M", "pH = 3", "#4BB04A")]
    ew = (W - 2 * MX - 40 - 2 * 14) / 3
    for k, (q, step, ans, col) in enumerate(ex):
        exx = MX + 20 + k * (ew + 14)
        out.append(f'<rect x="{exx:.1f}" y="{y + 62}" width="{ew:.1f}" height="190" rx="14" '
                   f'fill="{mix(th["card"], col, .16)}"/>')
        out.append(fit_text(q, exx + ew / 2, y + 100, 17, th["ink"], ew - 20))
        out.append(fit_text(step, exx + ew / 2, y + 150, 15, th["sub"], ew - 20, "SemiBold"))
        out.append(f'<rect x="{exx + ew / 2 - 70:.1f}" y="{y + 182}" width="140" height="46" rx="23" fill="{col}"/>')
        out.append(text(ans, exx + ew / 2, y + 213, 20, "#FFFFFF"))
    return W, H, "".join(out)


STEPS = [
    ("Write the mass of each element", "C: 40 g   H: 6.7 g   O: 53.3 g", T),
    ("Divide by the atomic mass to get moles", "C: 40/12 = 3.33   H: 6.7/1 = 6.7   O: 53.3/16 = 3.33", O),
    ("Divide by the smallest number of moles", "C: 1   H: 2   O: 1", P),
    ("Write the empirical formula", "CH_{2}O", R),
    ("Find n = Mr ÷ empirical formula mass", "Mr = 180 → n = 180 ÷ 30 = 6", "#3D7DDB"),
    ("Multiply to get the molecular formula", "(CH_{2}O)_{6} = C_{6}H_{12}O_{6}  (glucose)", "#4BB04A"),
]


def empirical(th):
    W = 1226
    top = 122
    rh = 86
    H = top + len(STEPS) * (rh + 12) + 50
    out = [header(W, th, "EMPIRICAL AND MOLECULAR FORMULAS", "Finding a compound's formula from its composition "
                                                            "(example: glucose)")]
    for i, (step, ex, col) in enumerate(STEPS):
        y = top + i * (rh + 12)
        out.append(_card(MX, y, W - 2 * MX, rh, th))
        out.append(f'<circle cx="{MX + 44}" cy="{y + rh / 2}" r="22" fill="{col}"/>'
                   + text(str(i + 1), MX + 44, y + rh / 2 + 8, 21, "#FFFFFF"))
        out.append(fit_text(step, MX + 84, y + rh / 2 + 6, 17, th["ink"], 400, anchor="start"))
        bx = MX + 500
        bw = W - MX - 20 - bx
        out.append(f'<rect x="{bx}" y="{y + 14}" width="{bw}" height="{rh - 28}" rx="12" fill="{th["plate"]}"/>')
        out.append(chem(tr(ex), bx + bw / 2, y + rh / 2 + 7, 18, INK, "middle"))
    for i in range(len(STEPS) - 1):
        y = top + i * (rh + 12)
        out.append(arrow_line(MX + 44, y + rh / 2 + 24, MX + 44, y + rh + 12 + rh / 2 - 24, th["accent"], 3))
    out.append(text("Empirical formula = simplest whole-number ratio · Molecular formula = actual number of atoms", W / 2,
                    H - 20, 13, th["sub"], "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("calculating-ph", ph_calc, "Calculating pH chart, formulas for strong and weak acids and bases with examples",
     ["ph calculation", "ph formula", "poh", "kw", "strong acid", "weak acid", "strong base", "hydrogen ion",
      "logarithm", "acids and bases", "worked examples", "concentration", "ka", "chemistry formulas"]),
    ("empirical-molecular-formula", empirical, "Empirical and molecular formula chart, step by step glucose example",
     ["empirical formula", "molecular formula", "percent composition", "moles", "stoichiometry", "glucose",
      "molar mass", "step by step", "calculation", "chemistry skills", "ratio", "mole concept", "formula",
      "worked example"]),
]

TR.update({
    "CALCULATING pH": "MENGHITUNG pH", "Key formulas for acids, bases and water": "Rumus penting untuk asam, basa, dan air",
    "Water at 25 °C": "Air pada 25 °C", "Strong acid": "Asam kuat", "Strong base": "Basa kuat", "Weak acid": "Asam lemah",
    "[H⁺] in mol/L": "[H⁺] dalam mol/L", "[OH⁻] in mol/L": "[OH⁻] dalam mol/L",
    "a = number of H⁺ released": "a = jumlah ion H⁺ yang dilepas", "b = number of OH⁻ released": "b = jumlah ion OH⁻ yang dilepas",
    "Weak base: [OH⁻] = √(Kb × M)": "Basa lemah: [OH⁻] = √(Kb × M)", "Worked examples": "Contoh soal",
    "0.01 M HCl": "HCl 0,01 M", "0.001 M NaOH": "NaOH 0,001 M", "0.1 M CH₃COOH (Ka = 10⁻⁵)": "CH₃COOH 0,1 M (Ka = 10⁻⁵)",
    "[H⁺] = 1 × 0.01 = 10⁻² M": "[H⁺] = 1 × 0,01 = 10⁻² M", "[OH⁻] = 10⁻³ M → pOH = 3": "[OH⁻] = 10⁻³ M → pOH = 3",
    "[H⁺] = √(10⁻⁵ × 0.1) = 10⁻³ M": "[H⁺] = √(10⁻⁵ × 0,1) = 10⁻³ M",
    "EMPIRICAL AND MOLECULAR FORMULAS": "RUMUS EMPIRIS DAN RUMUS MOLEKUL",
    "Finding a compound's formula from its composition (example: glucose)":
        "Menentukan rumus senyawa dari komposisinya (contoh: glukosa)",
    "Write the mass of each element": "Tulis massa setiap unsur",
    "Divide by the atomic mass to get moles": "Bagi dengan massa atom relatif untuk mendapat mol",
    "Divide by the smallest number of moles": "Bagi dengan jumlah mol terkecil",
    "Write the empirical formula": "Tulis rumus empiris",
    "Find n = Mr ÷ empirical formula mass": "Cari n = Mr ÷ massa rumus empiris",
    "Multiply to get the molecular formula": "Kalikan untuk mendapat rumus molekul",
    "C: 40 g   H: 6.7 g   O: 53.3 g": "C: 40 g   H: 6,7 g   O: 53,3 g",
    "C: 40/12 = 3.33   H: 6.7/1 = 6.7   O: 53.3/16 = 3.33": "C: 40/12 = 3,33   H: 6,7/1 = 6,7   O: 53,3/16 = 3,33",
    "(CH_{2}O)_{6} = C_{6}H_{12}O_{6}  (glucose)": "(CH_{2}O)_{6} = C_{6}H_{12}O_{6}  (glukosa)",
    "Empirical formula = simplest whole-number ratio · Molecular formula = actual number of atoms":
        "Rumus empiris = perbandingan bilangan bulat paling sederhana · Rumus molekul = jumlah atom sebenarnya",
})
