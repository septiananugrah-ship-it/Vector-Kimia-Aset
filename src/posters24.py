"""Poster edukasi kimia jilid 24: jenis isomer dan reaksi polimerisasi.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, particle, text, tr
from posters2 import _card, structure
from posters3 import arrow_line, mix
from posters4 import chem
from render import style_attrs

Z = .87  # langkah zigzag
ISOMERS = [
    ("Chain isomers", "Different carbon skeleton", "C_{4}H_{10}",
     ("Butane", [("", 0, 0), ("", Z, -.5), ("", 2 * Z, 0), ("", 3 * Z, -.5)], [(0, 1, 1), (1, 2, 1), (2, 3, 1)]),
     ("2-Methylpropane", [("", 0, .5), ("", Z, 0), ("", 2 * Z, .5), ("", Z, -1)], [(0, 1, 1), (1, 2, 1), (1, 3, 1)]),
     T),
    ("Position isomers", "Same group, different position", "C_{3}H_{8}O",
     ("Propan-1-ol", [("", 0, 0), ("", Z, -.5), ("", 2 * Z, 0), ("OH", 3 * Z, -.5)], [(0, 1, 1), (1, 2, 1), (2, 3, 1)]),
     ("Propan-2-ol", [("", 0, 0), ("", Z, -.5), ("", 2 * Z, 0), ("OH", Z, -1.5)], [(0, 1, 1), (1, 2, 1), (1, 3, 1)]),
     O),
    ("Functional group isomers", "Different functional group", "C_{2}H_{6}O",
     ("Ethanol", [("", 0, 0), ("", Z, -.5), ("OH", 2 * Z, 0)], [(0, 1, 1), (1, 2, 1)]),
     ("Dimethyl ether", [("", 0, 0), ("O", Z, -.5), ("", 2 * Z, 0)], [(0, 1, 1), (1, 2, 1)]),
     P),
    ("Geometric (cis–trans) isomers", "Groups fixed on either side of C=C", "C_{4}H_{8}",
     ("cis-But-2-ene", [("", -.5, -Z), ("", 0, 0), ("", 1, 0), ("", 1.5, -Z)], [(0, 1, 1), (1, 2, 2), (2, 3, 1)]),
     ("trans-But-2-ene", [("", -.5, -Z), ("", 0, 0), ("", 1, 0), ("", 1.5, Z)], [(0, 1, 1), (1, 2, 2), (2, 3, 1)]),
     R),
]


def isomers(th):
    W = 1226
    top = 122
    rh = 168
    H = top + 4 * (rh + 14) + 40
    out = [header(W, th, "TYPES OF ISOMERISM", "Isomers share the same molecular formula but have different "
                                               "structures")]
    for i, (name, desc, f, a, b, col) in enumerate(ISOMERS):
        y = top + i * (rh + 14)
        out.append(_card(MX, y, W - 2 * MX, rh, th))
        out.append(f'<rect x="{MX}" y="{y}" width="10" height="{rh}" rx="5" fill="{col}"/>')
        out.append(fit_text(name, MX + 34, y + 50, 21, th["ink"], 330, anchor="start"))
        out.append(fit_text(desc, MX + 34, y + 80, 15, th["sub"], 330, "SemiBold", anchor="start"))
        out.append(f'<rect x="{MX + 34}" y="{y + 102}" width="130" height="40" rx="20" fill="{col}"/>')
        out.append(chem(f, MX + 99, y + 129, 17, "#FFFFFF", "middle"))
        bw = (W - MX - 24 - (MX + 400) - 20) / 2
        for k, (iso, nodes, bonds) in enumerate((a, b)):
            bx = MX + 400 + k * (bw + 20)
            out.append(f'<rect x="{bx:.1f}" y="{y + 14}" width="{bw:.1f}" height="{rh - 28}" rx="12" '
                       f'fill="{mix(th["card"], col, .12)}"/>')
            out.append(structure(nodes, bonds, bx + bw / 2, y + 70, 50, th))
            out.append(text(tr(iso), bx + bw / 2, y + rh - 30, 16, th["ink"], "Bold"))
    out.append(text("Skeletal formulas: every corner or line end is a carbon atom; hydrogens on carbon are not drawn",
                    W / 2, H - 16, 13, th["sub"], "SemiBold"))
    return W, H, "".join(out)


def _beads(x, y, n, col, key, gap=26, linked=True):
    out = [f'<g {style_attrs(1.4)}>']
    if linked and n > 1:
        out.append(f'<path d="M{x} {y}H{x + (n - 1) * gap}" stroke="#5B6878" stroke-width="5"/>')
    for k in range(n):
        out.append(particle(x + k * gap, y, 11, col, f"{key}{k}"))
    out.append('</g>')
    return "".join(out)


def polymerization(th):
    W = 1226
    top = 122
    ch = 300
    H = top + 2 * (ch + 20) + 30
    out = [header(W, th, "POLYMERIZATION", "Small monomers join together to form long polymer chains")]
    rows = [
        ("Addition polymerization", T, "Monomers with a C=C double bond join; no other product is formed",
         "n CH_{2}=CH_{2} → (–CH_{2}–CH_{2}–)_{n}", "Polyethylene, PVC, polystyrene, Teflon", False),
        ("Condensation polymerization", O, "Monomers join and release a small molecule such as water",
         "amino acids → protein + n H_{2}O", "Proteins, nylon, polyester (PET), starch", True),
    ]
    for i, (name, col, desc, eq, ex, water) in enumerate(rows):
        y = top + i * (ch + 20)
        out.append(_card(MX, y, W - 2 * MX, ch, th))
        out.append(f'<rect x="{MX}" y="{y}" width="{W - 2 * MX}" height="58" rx="14" fill="{col}"/>'
                   f'<rect x="{MX}" y="{y + 32}" width="{W - 2 * MX}" height="26" fill="{col}"/>')
        out.append(text(name, W / 2, y + 39, 23, "#FFFFFF"))
        px = MX + 30
        out.append(f'<rect x="{px}" y="{y + 76}" width="{W - 2 * MX - 60}" height="118" rx="14" '
                   f'fill="{th["plate"]}"/>')
        mc = "#E8573F" if water else "#4FB3C9"
        for k in range(4):  # monomer terpisah
            mx = px + 40 + (k % 2) * 70
            my = y + 108 + (k // 2) * 54
            out.append(_beads(mx, my, 2, mc, f"pm{i}{k}", gap=24))
        out.append(arrow_line(px + 210, y + 135, px + 300, y + 135, "#1E2A3A", 4))
        out.append(_beads(px + 340, y + 135, 16 if water else 24, mc, f"pc{i}", gap=24))
        if water:
            for k in range(3):
                wx = px + 800 + k * 56
                out.append(f'<g {style_attrs(1.4)}>' + particle(wx, y + 112, 12, "#E8573F", f"pw{k}")
                           + particle(wx - 13, y + 126, 7, "#E9EEF3", f"ph{k}")
                           + particle(wx + 13, y + 126, 7, "#E9EEF3", f"pi{k}") + '</g>')
            out.append(chem("+ n H_{2}O", px + 856, y + 172, 17, "#1E2A3A", "middle"))
        out.append(chem(tr(eq), W / 2, y + 232, 24, th["accent"], "middle"))
        out.append(fit_text(desc, W / 2, y + 262, 15, th["ink"], W - 2 * MX - 60, "SemiBold"))
        out.append(fit_text(tr("Examples") + ": " + tr(ex), W / 2, y + 288, 14, th["sub"], W - 2 * MX - 60,
                            "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("types-of-isomerism", isomers, "Types of isomerism chart, chain, position, functional group and cis-trans isomers",
     ["isomers", "isomerism", "structural isomers", "chain isomers", "position isomers", "functional group isomers",
      "cis trans", "geometric isomers", "organic chemistry", "skeletal formula", "butane", "propanol", "ethanol",
      "molecular formula"]),
    ("polymerization", polymerization, "Polymerization chart, addition and condensation polymers with examples",
     ["polymerization", "polymer", "monomer", "addition polymerization", "condensation polymerization",
      "polyethylene", "nylon", "protein", "plastic", "macromolecule", "chain", "organic chemistry", "polyester",
      "pvc"]),
]

TR.update({
    "TYPES OF ISOMERISM": "JENIS-JENIS ISOMER",
    "Isomers share the same molecular formula but have different structures":
        "Isomer memiliki rumus molekul yang sama tetapi strukturnya berbeda",
    "Chain isomers": "Isomer rantai", "Position isomers": "Isomer posisi",
    "Functional group isomers": "Isomer gugus fungsi", "Geometric (cis–trans) isomers": "Isomer geometri (cis–trans)",
    "Different carbon skeleton": "Kerangka rantai karbon berbeda",
    "Same group, different position": "Gugus sama, letaknya berbeda",
    "Different functional group": "Gugus fungsinya berbeda",
    "Groups fixed on either side of C=C": "Letak gugus terhadap ikatan rangkap C=C berbeda",
    "Butane": "Butana", "2-Methylpropane": "2-Metilpropana", "Propan-1-ol": "1-Propanol", "Propan-2-ol": "2-Propanol",
    "Ethanol": "Etanol", "Dimethyl ether": "Dimetil eter", "cis-But-2-ene": "cis-2-Butena",
    "trans-But-2-ene": "trans-2-Butena",
    "Skeletal formulas: every corner or line end is a carbon atom; hydrogens on carbon are not drawn":
        "Rumus kerangka: setiap sudut atau ujung garis adalah atom karbon; atom H pada karbon tidak digambar",
    "POLYMERIZATION": "POLIMERISASI",
    "Small monomers join together to form long polymer chains":
        "Monomer-monomer kecil bergabung membentuk rantai polimer yang panjang",
    "Addition polymerization": "Polimerisasi adisi", "Condensation polymerization": "Polimerisasi kondensasi",
    "Monomers with a C=C double bond join; no other product is formed":
        "Monomer berikatan rangkap C=C saling bergabung tanpa menghasilkan zat lain",
    "Monomers join and release a small molecule such as water":
        "Monomer bergabung sambil melepaskan molekul kecil seperti air",
    "amino acids → protein + n H_{2}O": "asam amino → protein + n H_{2}O",
    "Polyethylene, PVC, polystyrene, Teflon": "Polietilena, PVC, polistirena, teflon",
    "Proteins, nylon, polyester (PET), starch": "Protein, nilon, poliester (PET), amilum",
    "Examples": "Contoh",
})
