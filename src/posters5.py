"""Poster edukasi kimia jilid 5: perubahan fisika vs kimia, sifat asam vs basa,
klasifikasi materi, dan awalan tata nama IUPAC.

Didaftarkan ke posters.py lewat POSTERS (2 tema x 2 bahasa).
"""
import icons_concepts
import icons_lab2
import icons_lab_flat
import molecules
from icons_lab_flat import L, O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, icon_at, text, tr
from posters2 import _card
from posters3 import arrow_line, mix
from posters4 import chem

ICONS = {ic["id"]: (ic["body"], m.STROKE) for m in (icons_lab_flat, icons_lab2, icons_concepts, molecules)
         for ic in m.ICONS}


def _icon(th, key, x, y, size):
    body, stroke = ICONS[key]
    return (f'<circle cx="{x + size / 2}" cy="{y + size / 2}" r="{size / 2 + 6}" fill="{th["plate"]}"/>'
            + icon_at(body, stroke, x + size * .12, y + size * .12, size * .76))


def comparison(th, title, subtitle, left, right, rows):
    """Poster dua kolom: left/right = (judul, warna, ikon); rows = [(sifat kiri, sifat kanan)]."""
    W = 1226
    top = 122
    cw = (W - 2 * MX - 24) / 2
    rh = 62
    H = top + 150 + len(rows) * rh + 50
    out = [header(W, th, title, subtitle)]
    for k, (name, col, icon) in enumerate((left, right)):
        x = MX + k * (cw + 24)
        out.append(_card(x, top, cw, H - top - 30, th))
        out.append(f'<rect x="{x}" y="{top}" width="{cw}" height="10" rx="5" fill="{col}"/>')
        out.append(_icon(th, icon, x + 24, top + 30, 90))
        out.append(text(name, x + 140, top + 88, 28, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .2),
                        "Bold", "start"))
        for i, row in enumerate(rows):
            y = top + 150 + i * rh
            out.append(f'<rect x="{x + 18}" y="{y}" width="{cw - 36}" height="{rh - 10}" rx="10" '
                       f'fill="{mix(th["card"], col, .1)}"/>')
            out.append(f'<circle cx="{x + 42}" cy="{y + (rh - 10) / 2}" r="7" fill="{col}"/>')
            out.append(fit_text(row[k], x + 62, y + (rh - 10) / 2 + 5, 14.5, th["ink"], cw - 100, "SemiBold",
                                anchor="start"))
    return W, H, "".join(out)


def physical_chemical(th):
    return comparison(
        th, "PHYSICAL VS CHEMICAL CHANGES", "How to tell whether a new substance is formed",
        ("Physical change", T, "water-drop"), ("Chemical change", R, "reaction-flask-smoke"),
        [("No new substance is formed", "A new substance is formed"),
         ("Usually easy to reverse", "Usually hard to reverse"),
         ("Changes shape, size or state", "Changes the chemical composition"),
         ("Example: melting ice", "Example: burning wood"),
         ("Example: dissolving sugar", "Example: rusting iron"),
         ("Example: cutting paper", "Example: baking a cake"),
         ("Example: boiling water", "Signs: gas, color change, heat or light")])


def acids_bases(th):
    return comparison(
        th, "ACIDS VS BASES", "Comparing the properties of acids and bases",
        ("Acids", R, "ph-strip"), ("Bases", "#3D62C4", "dropper-bottle"),
        [("pH less than 7", "pH greater than 7"),
         ("Taste sour", "Taste bitter and feel slippery"),
         ("Turn blue litmus red", "Turn red litmus blue"),
         ("Release H⁺ ions in water", "Release OH⁻ ions in water"),
         ("React with metals to form hydrogen", "React with acids in neutralization"),
         ("Example: HCl, vinegar, lemon juice", "Example: NaOH, soap, ammonia"),
         ("Acid + base → salt + water", "Acid + base → salt + water")])


def classification(th):
    """Bagan pohon klasifikasi materi."""
    W, H = 1226, 790
    top = 122
    out = [header(W, th, "CLASSIFICATION OF MATTER",
                  "Matter is either a pure substance or a mixture")]
    nodes = {
        "matter": ("Matter", W / 2, top + 30, th["accent"], None, "flask"),
        "pure": ("Pure substance", W * .27, top + 190, P, "Fixed composition", None),
        "mix": ("Mixture", W * .73, top + 190, O, "Variable composition", None),
        "el": ("Element", W * .14, top + 380, P, "One type of atom", "Examples: O2, Fe, Au"),
        "cmp": ("Compound", W * .4, top + 380, P, "Two or more elements bonded", "Examples: H2O, NaCl, CO2"),
        "hom": ("Homogeneous", W * .6, top + 380, O, "Uniform throughout", "Examples: salt water, air"),
        "het": ("Heterogeneous", W * .86, top + 380, O, "Parts can be seen", "Examples: sand and water, salad"),
    }
    edges = [("matter", "pure"), ("matter", "mix"), ("pure", "el"), ("pure", "cmp"), ("mix", "hom"), ("mix", "het")]
    bw, bh = 236, 118
    for a, b in edges:
        _, x1, y1, *_ = nodes[a]
        _, x2, y2, col, *_ = nodes[b]
        y_start = y1 + (64 if a == "matter" else bh if nodes[a][5] else 86)
        out.append(arrow_line(x1, y_start, x2, y2 - 8, col, 3))
    for key, (name, x, y, col, desc, ex) in nodes.items():
        if key == "matter":
            out.append(f'<rect x="{x - 130}" y="{y}" width="260" height="64" rx="32" fill="{col}"/>'
                       + text(name, x, y + 42, 28, "#FFFFFF"))
            continue
        h = bh if ex else 86
        out.append(_card(x - bw / 2, y, bw, h, th))
        out.append(f'<rect x="{x - bw / 2}" y="{y}" width="{bw}" height="8" rx="4" fill="{col}"/>')
        out.append(text(name, x, y + 40, 20, th["ink"]))
        out.append(fit_text(desc, x, y + 64, 12, th["sub"], bw - 20, "Regular"))
        if ex:
            lab, rest = tr(ex).split(":", 1)
            out.append(chem(lab + ":" + rest.replace("O2", "O_{2}").replace("H2O", "H_{2}O")
                            .replace("CO2", "CO_{2}"), x, y + 94, 13, th["accent"], "middle", "SemiBold"))
    icons = [("water", W * .14 - 50), ("sodium-chloride", W * .4 - 50), ("beaker", W * .6 - 50),
             ("petri-dish", W * .86 - 50)]
    for key, x in icons:
        out.append(_icon(th, key, x, top + 530, 100))
    return W, H, "".join(out)


PREFIXES = [(1, "meth-", "Methane", "CH4"), (2, "eth-", "Ethane", "C2H6"), (3, "prop-", "Propane", "C3H8"),
            (4, "but-", "Butane", "C4H10"), (5, "pent-", "Pentane", "C5H12"), (6, "hex-", "Hexane", "C6H14"),
            (7, "hept-", "Heptane", "C7H16"), (8, "oct-", "Octane", "C8H18"), (9, "non-", "Nonane", "C9H20"),
            (10, "dec-", "Decane", "C10H22")]
SUFFIXES = [("-ane", "Alkane", "single bonds only (C–C)"), ("-ene", "Alkene", "one C=C double bond"),
            ("-yne", "Alkyne", "one triple bond"), ("-ol", "Alcohol", "–OH group"),
            ("-oic acid", "Carboxylic acid", "–COOH group")]


def iupac(th):
    W = 1226
    top = 122
    H = top + 5 * 92 + 40 + 60
    out = [header(W, th, "IUPAC NAMING: PREFIXES AND SUFFIXES",
                  "Prefixes count the carbon atoms in the main chain; suffixes show the type of compound")]
    lw = 700
    out.append(_card(MX, top, lw, 5 * 92 + 30, th))
    out.append(text("Number of carbons", MX + 24, top + 36, 18, th["ink"], "Bold", "start"))
    cw = (lw - 48 - 12) / 2
    for i, (n, pre, name, f) in enumerate(PREFIXES):
        x = MX + 24 + (i // 5) * (cw + 12)
        y = top + 56 + (i % 5) * 84
        out.append(f'<rect x="{x}" y="{y}" width="{cw}" height="72" rx="12" fill="{mix(th["card"], T, .12)}"/>')
        out.append(f'<circle cx="{x + 36}" cy="{y + 36}" r="24" fill="{T}"/>'
                   + text(str(n), x + 36, y + 44, 22, "#FFFFFF"))
        out.append(text(pre, x + 74, y + 33, 22, th["accent"], "Bold", "start"))
        out.append(text(name, x + 74, y + 56, 12.5, th["sub"], "SemiBold", "start"))
        out.append(chem(_sub_formula(f), x + cw - 16, y + 46, 16, th["ink"], "end"))
    rx = MX + lw + 24
    rw = W - MX - rx
    out.append(_card(rx, top, rw, 5 * 92 + 30, th))
    out.append(text("Common suffixes", rx + 24, top + 36, 18, th["ink"], "Bold", "start"))
    cols = [T, O, P, L, R]
    for i, (suf, fam, desc) in enumerate(SUFFIXES):
        y = top + 56 + i * 84
        out.append(f'<rect x="{rx + 24}" y="{y}" width="{rw - 48}" height="72" rx="12" '
                   f'fill="{mix(th["card"], cols[i], .12)}"/>')
        out.append(f'<rect x="{rx + 24}" y="{y}" width="8" height="72" rx="4" fill="{cols[i]}"/>')
        out.append(text(suf, rx + 46, y + 34, 22, cols[i] if th["bg"] == "#FFFFFF" else mix(cols[i], "#FFFFFF", .2),
                        "Bold", "start"))
        out.append(fit_text(f"{tr(fam)}: {tr(desc)}", rx + 46, y + 57, 12.5, th["sub"], rw - 90, "SemiBold",
                            anchor="start"))
    out.append(text("Example: but- + -ene = butene (4 carbons, one double bond)", W / 2, H - 26, 13, th["sub"],
                    "SemiBold"))
    return W, H, "".join(out)


def _sub_formula(f):
    import re
    return re.sub(r"(\d+)", r"_{\1}", f)


POSTERS = [
    ("physical-vs-chemical-change", physical_chemical, "Physical versus chemical changes comparison chart",
     ["physical change", "chemical change", "comparison", "new substance", "melting", "burning", "rusting",
      "dissolving", "reversible", "irreversible", "matter", "properties", "examples", "versus"]),
    ("acids-vs-bases", acids_bases, "Acids versus bases properties comparison chart",
     ["acid", "base", "acids and bases", "alkali", "ph", "litmus", "neutralization", "properties", "comparison",
      "hydrogen ion", "hydroxide", "sour", "bitter", "versus"]),
    ("classification-of-matter", classification, "Classification of matter flowchart, pure substances and mixtures",
     ["classification of matter", "matter", "pure substance", "mixture", "element", "compound", "homogeneous",
      "heterogeneous", "flowchart", "tree diagram", "chart", "solution", "substances", "types"]),
    ("iupac-prefixes", iupac, "IUPAC organic nomenclature prefixes and suffixes chart",
     ["iupac", "nomenclature", "naming", "organic chemistry", "prefixes", "suffixes", "alkane", "alkene", "alkyne",
      "alcohol", "carboxylic acid", "carbon chain", "methane", "hydrocarbon"]),
]

TR.update({
    "PHYSICAL VS CHEMICAL CHANGES": "PERUBAHAN FISIKA VS KIMIA",
    "How to tell whether a new substance is formed": "Cara membedakan: apakah terbentuk zat baru?",
    "Physical change": "Perubahan fisika", "Chemical change": "Perubahan kimia",
    "No new substance is formed": "Tidak terbentuk zat baru", "A new substance is formed": "Terbentuk zat baru",
    "Usually easy to reverse": "Umumnya mudah dikembalikan", "Usually hard to reverse": "Umumnya sulit dikembalikan",
    "Changes shape, size or state": "Berubah bentuk, ukuran, atau wujud",
    "Changes the chemical composition": "Susunan kimianya berubah",
    "Example: melting ice": "Contoh: es mencair", "Example: burning wood": "Contoh: kayu terbakar",
    "Example: dissolving sugar": "Contoh: gula larut", "Example: rusting iron": "Contoh: besi berkarat",
    "Example: cutting paper": "Contoh: kertas digunting", "Example: baking a cake": "Contoh: kue dipanggang",
    "Example: boiling water": "Contoh: air mendidih",
    "Signs: gas, color change, heat or light": "Ciri: gas, perubahan warna, panas, atau cahaya",
    "ACIDS VS BASES": "ASAM VS BASA", "Comparing the properties of acids and bases": "Perbandingan sifat asam dan basa",
    "Acids": "Asam", "Bases": "Basa", "pH less than 7": "pH kurang dari 7", "pH greater than 7": "pH lebih dari 7",
    "Taste sour": "Rasanya masam", "Taste bitter and feel slippery": "Rasanya pahit dan terasa licin",
    "Turn blue litmus red": "Mengubah lakmus biru menjadi merah",
    "Turn red litmus blue": "Mengubah lakmus merah menjadi biru",
    "Release H⁺ ions in water": "Melepas ion H⁺ dalam air", "Release OH⁻ ions in water": "Melepas ion OH⁻ dalam air",
    "React with metals to form hydrogen": "Bereaksi dengan logam menghasilkan hidrogen",
    "React with acids in neutralization": "Bereaksi dengan asam (netralisasi)",
    "Example: HCl, vinegar, lemon juice": "Contoh: HCl, cuka, air lemon",
    "Example: NaOH, soap, ammonia": "Contoh: NaOH, sabun, amonia",
    "Acid + base → salt + water": "Asam + basa → garam + air",
    "CLASSIFICATION OF MATTER": "PENGGOLONGAN MATERI",
    "Matter is either a pure substance or a mixture": "Materi dibedakan menjadi zat tunggal dan campuran",
    "Matter": "Materi", "Pure substance": "Zat tunggal", "Mixture": "Campuran",
    "Fixed composition": "Susunan tetap", "Variable composition": "Susunan tidak tetap",
    "Element": "Unsur", "Compound": "Senyawa", "Homogeneous": "Homogen", "Heterogeneous": "Heterogen",
    "One type of atom": "Hanya satu jenis atom", "Two or more elements bonded": "Dua unsur atau lebih yang terikat",
    "Uniform throughout": "Merata di seluruh bagian", "Parts can be seen": "Komponennya dapat dibedakan",
    "Examples: O2, Fe, Au": "Contoh: O2, Fe, Au", "Examples: H2O, NaCl, CO2": "Contoh: H2O, NaCl, CO2",
    "Examples: salt water, air": "Contoh: air garam, udara",
    "Examples: sand and water, salad": "Contoh: pasir dan air, salad",
    "IUPAC NAMING: PREFIXES AND SUFFIXES": "TATA NAMA IUPAC: AWALAN DAN AKHIRAN",
    "Prefixes count the carbon atoms in the main chain; suffixes show the type of compound":
        "Awalan menunjukkan jumlah atom karbon rantai utama; akhiran menunjukkan jenis senyawa",
    "Number of carbons": "Jumlah atom karbon", "Common suffixes": "Akhiran umum",
    "single bonds only (C–C)": "hanya ikatan tunggal (C–C)", "one C=C double bond": "satu ikatan rangkap dua C=C",
    "one triple bond": "satu ikatan rangkap tiga", "–OH group": "gugus –OH", "–COOH group": "gugus –COOH",
    "Alkane": "Alkana", "meth-": "met-", "eth-": "et-", "hex-": "heks-", "oct-": "okt-", "dec-": "dek-",
    "-ane": "-ana", "-ene": "-ena", "-yne": "-una", "-oic acid": "asam -oat",
    "Example: but- + -ene = butene (4 carbons, one double bond)":
        "Contoh: but- + -ena = butena (4 karbon, satu ikatan rangkap dua)",
})
