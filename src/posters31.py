"""Poster edukasi kimia jilid 31: golongan VIIIA gas mulia dan perbandingan logam vs nonlogam.
Didaftarkan ke posters.py lewat POSTERS (semua tema x 2 bahasa).
"""
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text
from posters2 import _card
from posters3 import mix
from posters30 import _tile

INK = "#1E2A3A"

NOBLE = [("He", "Helium", 2, "−269", "Balloons, airships", "#F7E07A"),
         ("Ne", "Neon", 10, "−246", "Bright red-orange signs", "#FF6B4A"),
         ("Ar", "Argon", 18, "−186", "Light bulbs, welding shield gas", "#B57BFF"),
         ("Kr", "Krypton", 36, "−153", "Camera flashes, lasers", "#E0E0F0"),
         ("Xe", "Xenon", 54, "−108", "Car headlights, ion engines", "#7FB8F0"),
         ("Rn", "Radon", 86, "−62", "Radioactive; once used in cancer treatment", "#9AD08A")]


def noble(th):
    W = 1226
    top = 122
    rh = 84
    n = len(NOBLE)
    H = top + n * (rh + 10) + 50 + 150 + 30
    out = [header(W, th, "GROUP 18: NOBLE GASES", "Colorless, unreactive gases with a full outer electron shell")]
    out.append(_card(MX, top, W - 2 * MX, n * (rh + 10) + 40, th))
    hx = [MX + 180, MX + 400, MX + 560, MX + 760]
    for lab, xx in zip(("Element", "Boiling point (°C)", "Glow in a discharge tube", "Uses"), hx):
        out.append(text(lab, xx, top + 30, 13, th["sub"], "Bold", "start"))
    for i, (sym, name, z, bp, use, glow) in enumerate(NOBLE):
        y = top + 44 + i * (rh + 10)
        out.append(_tile(MX + 30, y, rh - 12, sym, z, "#C9B8F5"))
        out.append(fit_text(name, hx[0], y + rh / 2, 20, th["ink"], 200, anchor="start"))
        out.append(text(bp, hx[1] + 50, y + rh / 2, 21, th["ink"], "Bold"))
        out.append(f'<rect x="{hx[2]}" y="{y + rh / 2 - 26}" width="150" height="26" rx="13" fill="{glow}" '
                   f'stroke="{mix(glow, "#FFFFFF", .5)}" stroke-width="5"/>')
        out.append(fit_text(use, hx[3], y + rh / 2, 15, th["ink"], W - MX - 30 - hx[3], "SemiBold", "start"))
    y = top + n * (rh + 10) + 60
    out.append(_card(MX, y, W - 2 * MX, 150, th))
    out.append(text("Why are they unreactive?", W / 2, y + 38, 18, th["ink"]))
    facts = ["Full outer shell (He: 2, others: 8 electrons)", "Exist as single atoms (monatomic)",
             "Very hard to gain, lose or share electrons"]
    fw = (W - 2 * MX - 40 - 2 * 14) / 3
    for k, f in enumerate(facts):
        fx = MX + 20 + k * (fw + 14)
        out.append(f'<rect x="{fx:.1f}" y="{y + 60}" width="{fw:.1f}" height="66" rx="12" '
                   f'fill="{mix(th["card"], "#C9B8F5", .25)}"/>')
        out.append(fit_text(f, fx + fw / 2, y + 99, 15, th["ink"], fw - 24, "SemiBold"))
    return W, H, "".join(out)


COMPARE = [
    ("Appearance", "Shiny (lustrous)", "Dull"),
    ("State at room temperature", "Solid (except mercury)", "Gas, liquid or solid"),
    ("Electrical conductivity", "Good conductors", "Poor conductors (insulators)"),
    ("Heat conductivity", "Good conductors", "Poor conductors"),
    ("Malleability", "Malleable and ductile", "Brittle when solid"),
    ("Density", "Usually high", "Usually low"),
    ("Ions formed", "Positive ions (lose electrons)", "Negative ions (gain electrons)"),
    ("Oxides", "Basic oxides", "Acidic oxides"),
]


def metals_nonmetals(th):
    W = 1226
    top = 122
    rh = 62
    H = top + 80 + len(COMPARE) * (rh + 8) + 140 + 30
    out = [header(W, th, "METALS VS NONMETALS", "Comparing the physical and chemical properties of the two main "
                                                "groups of elements")]
    cw = (W - 2 * MX - 300 - 28 - 12) / 2
    x1 = MX + 300 + 14
    x2 = x1 + cw + 14
    for x, lab, col in ((x1, "Metals", "#F2A541"), (x2, "Nonmetals", "#4FB3C9")):
        out.append(f'<rect x="{x}" y="{top}" width="{cw}" height="64" rx="14" fill="{col}"/>')
        out.append(text(lab, x + cw / 2, top + 42, 26, "#FFFFFF"))
    for i, (prop, m, nm) in enumerate(COMPARE):
        y = top + 80 + i * (rh + 8)
        out.append(_card(MX, y, W - 2 * MX, rh, th, rx=12))
        out.append(fit_text(prop, MX + 22, y + rh / 2 + 6, 16, th["ink"], 270, anchor="start"))
        for x, val, col in ((x1, m, "#F2A541"), (x2, nm, "#4FB3C9")):
            out.append(f'<rect x="{x}" y="{y + 9}" width="{cw}" height="{rh - 18}" rx="10" '
                       f'fill="{mix(th["card"], col, .2)}"/>')
            out.append(fit_text(val, x + cw / 2, y + rh / 2 + 6, 16, th["ink"], cw - 24, "SemiBold"))
    y = top + 80 + len(COMPARE) * (rh + 8) + 12
    out.append(_card(MX, y, W - 2 * MX, 120, th))
    for k, (lab, items, col) in enumerate((("Metal examples", "Fe · Cu · Al · Na · Au · Ag", "#F2A541"),
                                           ("Nonmetal examples", "C · O · N · S · Cl · He", "#4FB3C9"))):
        bx = MX + 20 + k * ((W - 2 * MX - 40) / 2)
        out.append(text(lab, bx + (W - 2 * MX - 40) / 4, y + 42, 15, col if th["bg"] == "#FFFFFF" else
                        mix(col, "#FFFFFF", .3), "Bold"))
        out.append(text(items, bx + (W - 2 * MX - 40) / 4, y + 84, 26, th["ink"], "Bold"))
    out.append(text("Metalloids such as Si and Ge have properties in between", W / 2, H - 14, 13, th["sub"],
                    "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("group-18-noble-gases", noble, "Group 18 noble gases chart, boiling points, glowing colors and uses",
     ["noble gases", "group 18", "helium", "neon", "argon", "krypton", "xenon", "radon", "inert gases",
      "periodic table", "neon sign", "full outer shell", "periodic trends", "inorganic chemistry"]),
    ("metals-vs-nonmetals", metals_nonmetals, "Metals vs nonmetals comparison chart of physical and chemical "
                                              "properties",
     ["metals", "nonmetals", "metalloids", "properties of metals", "conductivity", "malleability", "comparison",
      "periodic table", "elements", "physical properties", "chemical properties", "ions", "oxides",
      "classification"]),
]

TR.update({
    "GROUP 18: NOBLE GASES": "GOLONGAN VIIIA: GAS MULIA",
    "Colorless, unreactive gases with a full outer electron shell":
        "Gas tak berwarna dan sukar bereaksi dengan kulit terluar yang penuh",
    "Boiling point (°C)": "Titik didih (°C)", "Glow in a discharge tube": "Nyala dalam tabung lucutan",
    "Uses": "Kegunaan", "Helium": "Helium", "Neon": "Neon", "Argon": "Argon", "Krypton": "Kripton", "Xenon": "Xenon",
    "Radon": "Radon", "Balloons, airships": "Balon udara, kapal udara", "Bright red-orange signs": "Lampu reklame merah-jingga",
    "Light bulbs, welding shield gas": "Bola lampu, gas pelindung las", "Camera flashes, lasers": "Lampu kilat kamera, laser",
    "Car headlights, ion engines": "Lampu depan mobil, mesin ion",
    "Radioactive; once used in cancer treatment": "Radioaktif; dulu dipakai untuk terapi kanker",
    "Why are they unreactive?": "Mengapa sukar bereaksi?",
    "Full outer shell (He: 2, others: 8 electrons)": "Kulit terluar penuh (He: 2, lainnya: 8 elektron)",
    "Exist as single atoms (monatomic)": "Berupa atom tunggal (monoatomik)",
    "Very hard to gain, lose or share electrons": "Sangat sulit menerima, melepas, atau berbagi elektron",
    "METALS VS NONMETALS": "LOGAM VS NONLOGAM",
    "Comparing the physical and chemical properties of the two main groups of elements":
        "Perbandingan sifat fisika dan kimia dua kelompok utama unsur",
    "Metals": "Logam", "Nonmetals": "Nonlogam", "Appearance": "Penampilan", "Shiny (lustrous)": "Mengilap",
    "Dull": "Kusam", "State at room temperature": "Wujud pada suhu kamar",
    "Solid (except mercury)": "Padat (kecuali raksa)", "Gas, liquid or solid": "Gas, cair, atau padat",
    "Electrical conductivity": "Daya hantar listrik", "Good conductors": "Penghantar baik",
    "Poor conductors (insulators)": "Penghantar buruk (isolator)", "Heat conductivity": "Daya hantar panas",
    "Poor conductors": "Penghantar buruk", "Malleability": "Kelenturan", "Malleable and ductile": "Dapat ditempa dan ditarik",
    "Brittle when solid": "Rapuh bila padat", "Density": "Massa jenis", "Usually high": "Umumnya tinggi",
    "Usually low": "Umumnya rendah", "Ions formed": "Ion yang dibentuk",
    "Positive ions (lose electrons)": "Ion positif (melepas elektron)",
    "Negative ions (gain electrons)": "Ion negatif (menerima elektron)", "Oxides": "Oksida",
    "Basic oxides": "Oksida basa", "Acidic oxides": "Oksida asam", "Metal examples": "Contoh logam",
    "Nonmetal examples": "Contoh nonlogam",
    "Metalloids such as Si and Ge have properties in between": "Metaloid seperti Si dan Ge memiliki sifat di antara keduanya",
})
