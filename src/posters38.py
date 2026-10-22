"""Poster edukasi kimia jilid 38: unsur dalam kehidupan sehari-hari dan unsur penyusun tubuh manusia.
Didaftarkan ke posters.py lewat POSTERS (semua tema x 2 bahasa).
"""
from periodic import CAT, ELEMENTS
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters3 import mix

INK = "#1E2A3A"
SYM = {sym: (z, name, cat) for z, (sym, name, _m, cat) in enumerate(ELEMENTS, start=1)}

EVERYDAY = [("Fe", "Steel, bridges, cars"), ("Cu", "Electrical wires"), ("Al", "Drink cans, foil"),
            ("Si", "Computer chips, solar cells"), ("Au", "Jewelry, electronics"), ("Ag", "Mirrors, jewelry"),
            ("Ti", "Implants, aircraft"), ("He", "Party balloons"), ("Ne", "Glowing signs"), ("Cl", "Pool disinfectant"),
            ("F", "Toothpaste (fluoride)"), ("Li", "Rechargeable batteries"), ("Na", "Table salt"),
            ("Ca", "Bones, cement, chalk"), ("C", "Pencils, diamonds, life"), ("W", "Light bulb filaments")]


def _tile(x, y, s, sym):
    z, name, cat = SYM[sym]
    col = CAT[cat][1]
    return (f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="12" fill="{col}" stroke="{INK}" stroke-width="2.5"/>'
            + (text(str(z), x + 9, y + 18, 12, INK, "SemiBold", "start") if s >= 60 else "")  # ubin kecil: tanpa nomor
            + text(sym, x + s / 2, y + s * (.66 if s >= 60 else .68), s * (.4 if s >= 60 else .46), INK, "Bold"))


def everyday(th):
    W = 1226
    top = 122
    gap = 14
    cw = (W - 2 * MX - 3 * gap) / 4
    ch = 112
    H = top + 4 * (ch + gap) + 40
    out = [header(W, th, "ELEMENTS IN EVERYDAY LIFE", "Where we use common chemical elements around us")]
    for i, (sym, use) in enumerate(EVERYDAY):
        x = MX + (i % 4) * (cw + gap)
        y = top + (i // 4) * (ch + gap)
        out.append(_card(x, y, cw, ch, th))
        out.append(_tile(x + 14, y + 14, ch - 28, sym))
        out.append(fit_text(SYM[sym][1], x + ch + 4, y + 46, 18, th["ink"], cw - ch - 16, anchor="start"))
        out.append(fit_text(use, x + ch + 4, y + 76, 14, th["sub"], cw - ch - 16, "SemiBold", "start"))
    out.append(text("Tile colors follow the element categories of the periodic table", W / 2, H - 16, 13, th["sub"],
                    "SemiBold"))
    return W, H, "".join(out)


BODY = [("O", 65, "In water and most biomolecules"), ("C", 18.5, "Backbone of all organic molecules"),
        ("H", 9.5, "In water, fats and proteins"), ("N", 3.2, "In proteins and DNA"),
        ("Ca", 1.5, "Bones and teeth"), ("P", 1.0, "Bones, DNA and ATP"), ("K", .4, "Nerve signals"),
        ("S", .3, "In some amino acids"), ("Na", .2, "Fluid balance"), ("Cl", .2, "Stomach acid (HCl)"),
        ("Mg", .1, "Muscles and enzymes")]


def body(th):
    W = 1226
    top = 122
    rh = 56
    H = top + len(BODY) * (rh + 8) + 20 + 110 + 30
    out = [header(W, th, "ELEMENTS OF THE HUMAN BODY", "Percentage by mass of the main elements in the body")]
    maxw = W - 2 * MX - 620
    for i, (sym, pct, role) in enumerate(BODY):
        y = top + i * (rh + 8)
        out.append(_card(MX, y, W - 2 * MX, rh, th, rx=12))
        out.append(_tile(MX + 10, y + 6, rh - 12, sym))
        out.append(fit_text(SYM[sym][1], MX + 70, y + rh / 2 + 6, 17, th["ink"], 140, anchor="start"))
        bx = MX + 220
        col = CAT[SYM[sym][2]][1]
        bw = max(6, maxw * pct / 65)
        out.append(f'<rect x="{bx}" y="{y + 14}" width="{maxw}" height="{rh - 28}" rx="8" '
                   f'fill="{mix(th["card"], th["sub"], .15)}"/>')
        out.append(f'<rect x="{bx}" y="{y + 14}" width="{bw:.1f}" height="{rh - 28}" rx="8" fill="{col}"/>')
        label = (f"{pct:g}%").replace(".", ",") if tr("Oxygen") != "Oxygen" else f"{pct:g}%"
        out.append(text(label, bx + maxw + 14, y + rh / 2 + 7, 18, th["ink"], "Bold", "start"))
        out.append(fit_text(role, bx + maxw + 90, y + rh / 2 + 6, 13.5, th["sub"], W - MX - 20 - (bx + maxw + 90),
                            "SemiBold", "start"))
    y = top + len(BODY) * (rh + 8) + 12
    out.append(_card(MX, y, W - 2 * MX, 110, th))
    out.append(fit_text("O, C, H and N make up about 96% of your body mass, mostly as water and organic molecules",
                        W / 2, y + 48, 17, th["ink"], W - 2 * MX - 60, "SemiBold"))
    out.append(fit_text("Trace elements such as Fe, Zn, I and Cu are needed in tiny amounts but are still essential",
                        W / 2, y + 82, 14, th["sub"], W - 2 * MX - 60, "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("elements-everyday-life", everyday, "Elements in everyday life chart, uses of common chemical elements",
     ["elements", "uses of elements", "everyday chemistry", "iron", "copper", "aluminium", "silicon", "gold",
      "helium", "neon", "chlorine", "periodic table", "materials", "applications"]),
    ("elements-human-body", body, "Elements of the human body chart, percentage by mass with biological roles",
     ["human body", "elements", "body composition", "oxygen", "carbon", "hydrogen", "nitrogen", "calcium",
      "phosphorus", "biochemistry", "trace elements", "nutrition", "biology", "percentage"]),
]

TR.update({
    "ELEMENTS IN EVERYDAY LIFE": "UNSUR DALAM KEHIDUPAN SEHARI-HARI",
    "Where we use common chemical elements around us": "Kegunaan unsur-unsur kimia di sekitar kita",
    "Steel, bridges, cars": "Baja, jembatan, mobil", "Electrical wires": "Kabel listrik", "Drink cans, foil": "Kaleng minuman, foil",
    "Computer chips, solar cells": "Chip komputer, sel surya", "Jewelry, electronics": "Perhiasan, elektronik",
    "Mirrors, jewelry": "Cermin, perhiasan", "Implants, aircraft": "Implan, pesawat", "Party balloons": "Balon pesta",
    "Glowing signs": "Lampu reklame", "Pool disinfectant": "Disinfektan kolam renang",
    "Toothpaste (fluoride)": "Pasta gigi (fluorida)", "Rechargeable batteries": "Baterai isi ulang", "Table salt": "Garam dapur",
    "Bones, cement, chalk": "Tulang, semen, kapur", "Pencils, diamonds, life": "Pensil, intan, makhluk hidup",
    "Light bulb filaments": "Filamen bola lampu",
    "Tile colors follow the element categories of the periodic table":
        "Warna ubin mengikuti kategori unsur pada tabel periodik",
    "Iron": "Besi", "Copper": "Tembaga", "Aluminium": "Aluminium", "Silicon": "Silikon", "Gold": "Emas", "Silver": "Perak",
    "Titanium": "Titanium", "Helium": "Helium", "Neon": "Neon", "Chlorine": "Klorin", "Fluorine": "Fluorin",
    "Lithium": "Litium", "Sodium": "Natrium", "Calcium": "Kalsium", "Carbon": "Karbon", "Tungsten": "Wolfram",
    "Oxygen": "Oksigen", "Hydrogen": "Hidrogen", "Nitrogen": "Nitrogen", "Phosphorus": "Fosfor", "Potassium": "Kalium",
    "Sulfur": "Belerang", "Magnesium": "Magnesium",
    "ELEMENTS OF THE HUMAN BODY": "UNSUR PENYUSUN TUBUH MANUSIA",
    "Percentage by mass of the main elements in the body": "Persentase massa unsur-unsur utama dalam tubuh",
    "In water and most biomolecules": "Dalam air dan sebagian besar biomolekul",
    "Backbone of all organic molecules": "Kerangka semua molekul organik", "In water, fats and proteins": "Dalam air, lemak, dan protein",
    "In proteins and DNA": "Dalam protein dan DNA", "Bones and teeth": "Tulang dan gigi", "Bones, DNA and ATP": "Tulang, DNA, dan ATP",
    "Nerve signals": "Sinyal saraf", "In some amino acids": "Dalam beberapa asam amino", "Fluid balance": "Keseimbangan cairan",
    "Stomach acid (HCl)": "Asam lambung (HCl)", "Muscles and enzymes": "Otot dan enzim",
    "O, C, H and N make up about 96% of your body mass, mostly as water and organic molecules":
        "O, C, H, dan N menyusun sekitar 96% massa tubuh, terutama sebagai air dan molekul organik",
    "Trace elements such as Fe, Zn, I and Cu are needed in tiny amounts but are still essential":
        "Unsur renik seperti Fe, Zn, I, dan Cu dibutuhkan dalam jumlah sangat kecil tetapi tetap penting",
})
