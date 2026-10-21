"""Poster edukasi kimia jilid 8: bahan kimia sehari-hari dan langkah titrasi.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
import icons_concepts
import icons_lab2
import icons_lab_flat
import molecules
from icons_lab_flat import G, L, O, P, R, T, Y, bubbles, solid, vessel
from poster_i18n import TR
from poster_kit import MX, fit_text, header, icon_at, text
from posters2 import _card
from posters3 import arrow_line, mix
from posters4 import chem

ICONS = {ic["id"]: (ic["body"], m.STROKE) for m in (icons_lab_flat, icons_lab2, icons_concepts, molecules)
         for ic in m.ICONS}

EVERYDAY = [
    ("Table salt", "NaCl", "Sodium chloride", "sodium-chloride"),
    ("Baking soda", "NaHCO_{3}", "Sodium bicarbonate", "beaker"),
    ("Vinegar", "CH_{3}COOH", "Acetic acid", "reagent-bottle"),
    ("Bleach", "NaOCl", "Sodium hypochlorite", "wash-bottle"),
    ("Chalk", "CaCO_{3}", "Calcium carbonate", "crystal"),
    ("Sugar", "C_{12}H_{22}O_{11}", "Sucrose", "watch-glass-crystals"),
    ("Rust", "Fe_{2}O_{3}", "Iron(III) oxide", "magnet"),
    ("Alcohol", "C_{2}H_{5}OH", "Ethanol", "ethanol"),
    ("Water", "H_{2}O", "Dihydrogen monoxide", "water"),
    ("Ammonia cleaner", "NH_{3}", "Ammonia", "ammonia"),
    ("Sand", "SiO_{2}", "Silicon dioxide", "mortar-and-pestle"),
    ("Hydrogen peroxide", "H_{2}O_{2}", "Antiseptic", "hydrogen-peroxide"),
]


def everyday(th):
    cols, cw, ch, gap = 4, 270, 230, 14
    W = cols * (cw + gap) - gap + 2 * MX
    top = 122
    rows = -(-len(EVERYDAY) // cols)
    H = top + rows * (ch + gap) - gap + 40
    out = [header(W, th, "CHEMISTRY IN EVERYDAY LIFE", "Common household substances and their chemical formulas")]
    cols_ = [T, O, R, P, L, Y]
    for i, (name, f, chem_name, icon) in enumerate(EVERYDAY):
        x = MX + (i % cols) * (cw + gap)
        y = top + (i // cols) * (ch + gap)
        col = cols_[i % len(cols_)]
        out.append(_card(x, y, cw, ch, th))
        out.append(f'<rect x="{x}" y="{y}" width="{cw}" height="8" rx="4" fill="{col}"/>')
        out.append(f'<circle cx="{x + cw / 2}" cy="{y + 70}" r="46" fill="{th["plate"]}"/>')
        body, stroke = ICONS[icon]
        out.append(icon_at(body, stroke, x + cw / 2 - 34, y + 36, 68))
        out.append(fit_text(name, x + cw / 2, y + 150, 19, th["ink"], cw - 24))
        out.append(chem(f, x + cw / 2, y + 180, 18, th["accent"], "middle"))
        out.append(fit_text(chem_name, x + cw / 2, y + 206, 12, th["sub"], cw - 24, "Regular"))
    return W, H, "".join(out)


STEPS = [
    ("Prepare the burette", "Rinse and fill it with the titrant of known concentration"),
    ("Measure the sample", "Pipette an exact volume of the solution into a conical flask"),
    ("Add indicator", "Add a few drops of indicator, e.g. phenolphthalein"),
    ("Titrate", "Open the tap and add titrant drop by drop while swirling"),
    ("Find the end point", "Stop when the color changes permanently"),
    ("Record and repeat", "Read the volume used and repeat for concordant results"),
]


def titration(th):
    W = 1226
    top = 122
    H = top + 6 * 84 + 50
    out = [header(W, th, "ACID–BASE TITRATION", "Step-by-step procedure to find the concentration of a solution")]
    lw = 420
    out.append(_card(MX, top, lw, H - top - 30, th))
    out.append(f'<rect x="{MX + 14}" y="{top + 14}" width="{lw - 28}" height="{H - top - 58}" rx="10" fill="{th["plate"]}"/>')
    body, stroke = ICONS["burette-stand"]
    out.append(icon_at(body, stroke, MX + 40, top + 40, 300))
    # labu dengan perubahan warna di bawah buret
    pink = (solid("M24 5h16v5H24z", G, 24, 40) +
            vessel("M27 10v14L13 52a4 4 0 0 0 3.6 5.8h30.8A4 4 0 0 0 51 52L37 24V10z", (13, 10, 51, 58), 38,
                   "#F06EAA", bubbles((27, 48, 2.2), (36, 44, 1.5)))).replace("{p}", "pinkflask")
    out.append(icon_at(pink, 1.6, MX + 190, top + 300, 120))
    out.append(text("pink = end point", MX + lw / 2, H - 56, 14, "#1E2A3A", "Bold"))
    x0 = MX + lw + 24
    sw = W - MX - x0
    for i, (name, desc) in enumerate(STEPS):
        y = top + i * 84
        out.append(_card(x0, y, sw, 72, th, rx=12))
        out.append(f'<circle cx="{x0 + 38}" cy="{y + 36}" r="20" fill="{th["accent"]}"/>'
                   + text(str(i + 1), x0 + 38, y + 43, 19, "#FFFFFF"))
        out.append(text(name, x0 + 74, y + 32, 17, th["ink"], "Bold", "start"))
        out.append(fit_text(desc, x0 + 74, y + 55, 12.5, th["sub"], sw - 96, "Regular", anchor="start"))
        if i < len(STEPS) - 1:
            out.append(arrow_line(x0 + 38, y + 58, x0 + 38, y + 96, mix(th["accent"], th["bg"], .2), 2))
    return W, H, "".join(out)


POSTERS = [
    ("everyday-chemicals", everyday, "Chemistry in everyday life chart, household substances and chemical formulas",
     ["everyday chemistry", "household chemicals", "chemical formula", "table salt", "baking soda", "vinegar",
      "bleach", "sugar", "rust", "water", "ammonia", "nacl", "compounds", "daily life"]),
    ("titration", titration, "Acid base titration procedure chart with burette and conical flask",
     ["titration", "acid base titration", "burette", "conical flask", "indicator", "phenolphthalein", "end point",
      "procedure", "analytical chemistry", "concentration", "volumetric analysis", "steps", "laboratory method",
      "neutralization"]),
]

TR.update({
    "CHEMISTRY IN EVERYDAY LIFE": "KIMIA DALAM KEHIDUPAN SEHARI-HARI",
    "Common household substances and their chemical formulas": "Bahan-bahan di rumah dan rumus kimianya",
    "Table salt": "Garam dapur", "Baking soda": "Soda kue", "Chalk": "Kapur tulis", "Sugar": "Gula pasir",
    "Rust": "Karat besi", "Alcohol": "Alkohol", "Ammonia cleaner": "Pembersih amonia", "Sand": "Pasir",
    "Hydrogen peroxide": "Hidrogen peroksida", "Sodium bicarbonate": "Natrium bikarbonat",
    "Sodium hypochlorite": "Natrium hipoklorit", "Calcium carbonate": "Kalsium karbonat", "Sucrose": "Sukrosa",
    "Iron(III) oxide": "Besi(III) oksida", "Dihydrogen monoxide": "Dihidrogen monoksida",
    "Silicon dioxide": "Silikon dioksida", "Antiseptic": "Antiseptik", "Acetic acid": "Asam asetat",
    "ACID–BASE TITRATION": "TITRASI ASAM–BASA",
    "Step-by-step procedure to find the concentration of a solution":
        "Langkah-langkah menentukan konsentrasi suatu larutan",
    "Prepare the burette": "Siapkan buret",
    "Rinse and fill it with the titrant of known concentration": "Bilas dan isi dengan titran yang konsentrasinya diketahui",
    "Measure the sample": "Ukur sampel",
    "Pipette an exact volume of the solution into a conical flask":
        "Pipet volume larutan yang tepat ke dalam labu Erlenmeyer",
    "Add indicator": "Tambahkan indikator",
    "Add a few drops of indicator, e.g. phenolphthalein": "Teteskan beberapa tetes indikator, mis. fenolftalein",
    "Titrate": "Titrasi", "Open the tap and add titrant drop by drop while swirling":
        "Buka keran dan teteskan titran sambil labu digoyang",
    "Find the end point": "Temukan titik akhir", "Stop when the color changes permanently":
        "Hentikan saat warna berubah dan tidak hilang lagi",
    "Record and repeat": "Catat dan ulangi",
    "Read the volume used and repeat for concordant results": "Baca volume yang terpakai dan ulangi hingga hasil konsisten",
    "pink = end point": "merah muda = titik akhir",
})
