"""Poster edukasi kimia jilid 18: plastik/polimer dengan kode daur ulang dan hukum Hess.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
import math

from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters3 import arrow_line, mix
from posters4 import chem

PLASTICS = [
    (1, "PET", "Polyethylene terephthalate", "Ethylene glycol + terephthalic acid", "Drink bottles, food jars",
     "#3D7DDB"),
    (2, "HDPE", "High-density polyethylene", "Ethene  CH_{2}=CH_{2}", "Milk jugs, detergent bottles", "#4BB04A"),
    (3, "PVC", "Polyvinyl chloride", "Vinyl chloride  CH_{2}=CHCl", "Water pipes, cable insulation", R),
    (4, "LDPE", "Low-density polyethylene", "Ethene  CH_{2}=CH_{2}", "Plastic bags, cling film", T),
    (5, "PP", "Polypropylene", "Propene  CH_{2}=CHCH_{3}", "Food containers, bottle caps", O),
    (6, "PS", "Polystyrene", "Styrene  CH_{2}=CHC_{6}H_{5}", "Foam cups, disposable cutlery", P),
]


def _recycle(cx, cy, s, col, num, ink):
    """Segitiga panah daur ulang dengan nomor kode resin."""
    out = []
    pts = [(cx + s * math.cos(math.radians(a)), cy + s * math.sin(math.radians(a))) for a in (-90, 30, 150)]
    for k in range(3):
        (x1, y1), (x2, y2) = pts[k], pts[(k + 1) % 3]
        ax, ay = x1 + (x2 - x1) * .14, y1 + (y2 - y1) * .14
        bx, by = x1 + (x2 - x1) * .82, y1 + (y2 - y1) * .82
        out.append(arrow_line(ax, ay, bx, by, col, 5))
    out.append(text(str(num), cx, cy + s * .26, s * .5, ink))
    return "".join(out)


def plastics(th):
    W = 1226
    top = 122
    gap = 18
    cw = (W - 2 * MX - 2 * gap) / 3
    ch = 300
    H = top + 2 * (ch + gap) + 44
    out = [header(W, th, "PLASTICS AND RECYCLING CODES", "Common polymers, the monomers they are made from and "
                                                         "where we use them")]
    for i, (num, abbr, name, mono, uses, col) in enumerate(PLASTICS):
        x = MX + (i % 3) * (cw + gap)
        y = top + (i // 3) * (ch + gap)
        out.append(_card(x, y, cw, ch, th))
        out.append(f'<circle cx="{x + 70}" cy="{y + 74}" r="50" fill="{th["plate"]}"/>')
        out.append(_recycle(x + 70, y + 80, 40, col, num, "#1E2A3A"))
        out.append(text(abbr, x + 140, y + 70, 30, th["ink"], "Bold", "start"))
        out.append(fit_text(name, x + 140, y + 98, 14, th["sub"], cw - 156, "SemiBold", anchor="start"))
        out.append(f'<path d="M{x + 22} {y + 146}H{x + cw - 22}" stroke="{th["card_stroke"]}" stroke-width="1.4"/>')
        out.append(text("Monomer", x + 24, y + 178, 13, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3),
                        "Bold", "start"))
        m = tr(mono)
        out.append(chem(m, x + 24, y + 206, 15 if len(m) < 34 else 13, th["ink"], "start", "SemiBold"))
        out.append(text("Used for", x + 24, y + 242, 13, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3),
                        "Bold", "start"))
        out.append(fit_text(uses, x + 24, y + 270, 15, th["ink"], cw - 48, "SemiBold", anchor="start"))
    out.append(text("Plastics are polymers: long chains made by joining many small monomer molecules", W / 2, H - 18,
                    13, th["sub"], "SemiBold"))
    return W, H, "".join(out)


def hess(th):
    W = 1226
    top = 122
    H = top + 500 + 24 + 230
    out = [header(W, th, "HESS'S LAW", "The total enthalpy change is the same whichever route the reaction takes")]
    out.append(_card(MX, top, W - 2 * MX, 500, th))
    a = (MX + 200, top + 110)
    b = (W - MX - 200, top + 110)
    c = (W / 2, top + 310)
    box = th["plate"]
    for (x, y), lab in ((a, "C(s) + O_{2}(g)"), (b, "CO_{2}(g)"), (c, "CO(g) + ½O_{2}(g)")):
        out.append(f'<rect x="{x - 130}" y="{y - 34}" width="260" height="68" rx="14" fill="{box}"/>')
        out.append(chem(lab, x, y + 9, 24, "#1E2A3A", "middle"))
    acc = th["accent"]
    out.append(arrow_line(a[0] + 140, a[1], b[0] - 140, b[1], acc, 4))
    out.append(chem("ΔH_{1} = −393.5 kJ", W / 2, a[1] - 18, 20, acc, "middle"))
    c1, c2 = (O, R) if th["bg"] == "#FFFFFF" else (mix(O, "#FFFFFF", .2), mix(R, "#FFFFFF", .2))
    out.append(arrow_line(a[0] + 40, a[1] + 40, c[0] - 140, c[1] - 10, c1, 4))
    out.append(chem("ΔH_{2} = −110.5 kJ", (a[0] + 40 + c[0] - 140) / 2 - 26, (a[1] + c[1]) / 2 + 20, 18, c1, "end"))
    out.append(arrow_line(c[0] + 140, c[1] - 10, b[0] - 40, b[1] + 40, c2, 4))
    out.append(chem("ΔH_{3} = −283.0 kJ", (b[0] - 40 + c[0] + 140) / 2 + 26, (b[1] + c[1]) / 2 + 20, 18, c2, "start"))
    out.append(f'<rect x="{W / 2 - 260}" y="{top + 410}" width="520" height="56" rx="28" '
               f'fill="{mix(th["card"], acc, .18)}"/>')
    out.append(chem("ΔH_{1} = ΔH_{2} + ΔH_{3}", W / 2, top + 447, 24, th["ink"], "middle"))
    y = top + 524
    cw = (W - 2 * MX - 3 * 16) / 4
    for k, (name, sym, desc, col) in enumerate((
            ("Formation", "ΔH°_{f}", "1 mol of compound formed from its elements", T),
            ("Combustion", "ΔH°_{c}", "1 mol of substance burned completely in oxygen", R),
            ("Decomposition", "ΔH°_{d}", "1 mol of compound broken into its elements", O),
            ("Neutralization", "ΔH°_{n}", "1 mol of water formed from an acid and a base", P))):
        x = MX + k * (cw + 16)
        out.append(_card(x, y, cw, 210, th))
        out.append(f'<rect x="{x}" y="{y}" width="{cw}" height="8" rx="4" fill="{col}"/>')
        out.append(chem(sym, x + cw / 2, y + 66, 30, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3),
                        "middle"))
        out.append(fit_text(name, x + cw / 2, y + 112, 19, th["ink"], cw - 24))
        words = tr(desc).split()
        half = (len(words) + 1) // 2
        for j, line in enumerate((" ".join(words[:half]), " ".join(words[half:]))):
            out.append(fit_text(line, x + cw / 2, y + 150 + j * 22, 14, th["sub"], cw - 24, "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("plastics-recycling-codes", plastics, "Plastics and recycling codes chart, PET, HDPE, PVC, LDPE, PP, PS polymers",
     ["plastic", "recycling codes", "resin identification code", "polymer", "monomer", "pet", "hdpe", "pvc", "ldpe",
      "polypropylene", "polystyrene", "recycling", "environment", "polymer chemistry"]),
    ("hess-law", hess, "Hess's law chart with enthalpy cycle and types of standard enthalpy change",
     ["hess's law", "enthalpy", "thermochemistry", "enthalpy change", "energy cycle", "formation", "combustion",
      "decomposition", "neutralization", "carbon dioxide", "carbon monoxide", "kj", "thermodynamics", "reaction"]),
]

TR.update({
    "PLASTICS AND RECYCLING CODES": "PLASTIK DAN KODE DAUR ULANG",
    "Common polymers, the monomers they are made from and where we use them":
        "Polimer yang umum, monomer pembentuknya, dan kegunaannya",
    "Polyethylene terephthalate": "Polietilena tereftalat", "High-density polyethylene": "Polietilena densitas tinggi",
    "Polyvinyl chloride": "Polivinil klorida", "Low-density polyethylene": "Polietilena densitas rendah",
    "Polypropylene": "Polipropilena", "Polystyrene": "Polistirena",
    "Ethylene glycol + terephthalic acid": "Etilena glikol + asam tereftalat",
    "Ethene  CH_{2}=CH_{2}": "Etena  CH_{2}=CH_{2}", "Vinyl chloride  CH_{2}=CHCl": "Vinil klorida  CH_{2}=CHCl",
    "Propene  CH_{2}=CHCH_{3}": "Propena  CH_{2}=CHCH_{3}", "Styrene  CH_{2}=CHC_{6}H_{5}": "Stirena  CH_{2}=CHC_{6}H_{5}",
    "Drink bottles, food jars": "Botol minuman, toples makanan", "Milk jugs, detergent bottles": "Botol susu, botol deterjen",
    "Water pipes, cable insulation": "Pipa air, pelapis kabel", "Plastic bags, cling film": "Kantong plastik, plastik wrap",
    "Food containers, bottle caps": "Wadah makanan, tutup botol", "Foam cups, disposable cutlery": "Gelas styrofoam, alat makan sekali pakai",
    "Monomer": "Monomer", "Used for": "Kegunaan",
    "Plastics are polymers: long chains made by joining many small monomer molecules":
        "Plastik adalah polimer: rantai panjang hasil penggabungan banyak molekul kecil (monomer)",
    "HESS'S LAW": "HUKUM HESS",
    "The total enthalpy change is the same whichever route the reaction takes":
        "Perubahan entalpi total selalu sama, apa pun jalur yang ditempuh reaksi",
    "Formation": "Pembentukan", "Combustion": "Pembakaran", "Decomposition": "Penguraian",
    "Neutralization": "Penetralan",
    "1 mol of compound formed from its elements": "1 mol senyawa dibentuk dari unsur-unsurnya",
    "1 mol of substance burned completely in oxygen": "1 mol zat dibakar sempurna dengan oksigen",
    "1 mol of compound broken into its elements": "1 mol senyawa diuraikan menjadi unsur-unsurnya",
    "1 mol of water formed from an acid and a base": "1 mol air terbentuk dari reaksi asam dan basa",
})
