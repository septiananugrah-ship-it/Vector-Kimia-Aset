"""Poster edukasi kimia jilid 42: kimia kembang api dan indikator alami kubis ungu.
Didaftarkan ke posters.py lewat POSTERS (semua tema x 2 bahasa).
"""
import math

from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters3 import mix
from posters4 import chem
from textpath import width

INK = "#1E2A3A"

FIREWORK = [("Red", "Strontium", "SrCO_{3}", "#E53935"), ("Orange", "Calcium", "CaCl_{2}", "#FF7A1A"),
            ("Yellow", "Sodium", "NaNO_{3}", "#FFC21A"), ("Green", "Barium", "BaCl_{2}", "#7CC242"),
            ("Blue", "Copper", "CuCl", "#2F80ED"), ("Purple", "Strontium + copper", "Sr + Cu", "#9B59D0"),
            ("White / silver", "Magnesium, aluminium", "Mg, Al", "#E9EEF5"), ("Gold sparks", "Iron filings", "Fe", "#E0B23A")]


def _burst(cx, cy, r, col):
    out = []
    for k in range(16):
        a = math.radians(k * 22.5)
        x1, y1 = cx + math.cos(a) * r * .28, cy + math.sin(a) * r * .28
        x2, y2 = cx + math.cos(a) * r, cy + math.sin(a) * r
        out.append(f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}" stroke="{col}" stroke-width="4" '
                   'stroke-linecap="round"/>')
        out.append(f'<circle cx="{x2:.1f}" cy="{y2:.1f}" r="4.5" fill="{col}"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r * .16:.1f}" fill="{mix(col, "#FFFFFF", .5)}"/>')
    return "".join(out)


def fireworks(th):
    W = 1226
    top = 122
    gap = 14
    cw = (W - 2 * MX - 3 * gap) / 4
    ch = 270
    H = top + 2 * (ch + gap) + 20 + 150 + 30
    out = [header(W, th, "THE CHEMISTRY OF FIREWORKS", "Metal salts give each firework its color")]
    for i, (color, metal, f, col) in enumerate(FIREWORK):
        x = MX + (i % 4) * (cw + gap)
        y = top + (i // 4) * (ch + gap)
        out.append(_card(x, y, cw, ch, th))
        out.append(f'<rect x="{x + 12}" y="{y + 12}" width="{cw - 24}" height="160" rx="12" fill="#0E1630"/>')
        out.append(_burst(x + cw / 2, y + 92, 64, col))
        out.append(fit_text(color, x + cw / 2, y + 204, 19, th["ink"], cw - 20))
        out.append(fit_text(metal, x + cw / 2, y + 230, 14, th["sub"], cw - 20, "SemiBold"))
        out.append(chem(f, x + cw / 2, y + 256, 15, th["accent"], "middle"))
    y = top + 2 * (ch + gap) + 20
    out.append(_card(MX, y, W - 2 * MX, 150, th))
    out.append(text("What is inside a firework shell?", W / 2, y + 38, 18, th["ink"]))
    parts = [("Fuel", "charcoal, sulfur"), ("Oxidizer", "nitrates, perchlorates"), ("Color", "metal salts"),
             ("Binder", "holds the stars together")]
    pw = (W - 2 * MX - 40 - 3 * 12) / 4
    for k, (head, desc) in enumerate(parts):
        px = MX + 20 + k * (pw + 12)
        out.append(f'<rect x="{px:.1f}" y="{y + 58}" width="{pw:.1f}" height="70" rx="12" '
                   f'fill="{mix(th["card"], th["accent"], .14)}"/>')
        out.append(text(head, px + pw / 2, y + 86, 16, th["ink"]))
        out.append(fit_text(desc, px + pw / 2, y + 112, 13.5, th["sub"], pw - 20, "SemiBold"))
    return W, H, "".join(out)


CABBAGE = [(1, "#D81B3C"), (2, "#E5326A"), (3, "#D94C8A"), (4, "#B85AAE"), (5, "#9C5BBE"), (6, "#7E57C2"),
           (7, "#6A5ACD"), (8, "#4A6FD0"), (9, "#3A86C8"), (10, "#2AA198"), (11, "#3DAA5C"), (12, "#9CC43B"),
           (13, "#E0C431"), (14, "#E8B02A")]


def cabbage(th):
    W = 1226
    top = 122
    H = top + 340 + 20 + 300 + 30
    out = [header(W, th, "RED CABBAGE INDICATOR", "A natural pH indicator you can make in the kitchen")]
    out.append(_card(MX, top, W - 2 * MX, 340, th))
    n = len(CABBAGE)
    tw = (W - 2 * MX - 40 - (n - 1) * 6) / n
    for k, (ph, col) in enumerate(CABBAGE):
        tx = MX + 20 + k * (tw + 6)
        # tabung reaksi berisi larutan berwarna
        out.append(f'<path d="M{tx + 4:.1f} {top + 40}V{top + 190}a{tw / 2 - 4:.1f} {tw / 2 - 4:.1f} 0 0 0 '
                   f'{tw - 8:.1f} 0V{top + 40}" fill="{th["plate"]}" stroke="{th["sub"]}" stroke-width="2"/>')
        out.append(f'<path d="M{tx + 6:.1f} {top + 90}V{top + 190}a{tw / 2 - 6:.1f} {tw / 2 - 6:.1f} 0 0 0 '
                   f'{tw - 12:.1f} 0V{top + 90}Z" fill="{col}"/>')
        out.append(text(str(ph), tx + tw / 2, top + 250, 18, th["ink"]))
    out.append(f'<path d="M{MX + 20} {top + 276}H{W - MX - 20}" stroke="{th["sub"]}" stroke-width="2"/>')
    for lab, x, anc in (("Acid", MX + 20, "start"), ("Neutral", W / 2, "middle"), ("Base", W - MX - 20, "end")):
        out.append(text(lab, x, top + 306, 16, th["ink"], "Bold", anc))
    y = top + 360
    cw = (W - 2 * MX - 20) / 2
    out.append(_card(MX, y, cw, 300, th))
    out.append(text("How to make it", MX + cw / 2, y + 40, 18, th["ink"]))
    steps = ["Chop red cabbage and cover it with hot water", "Leave for 10 minutes, then strain the purple liquid",
             "Add a little to each test sample and compare the color"]
    for k, s_ in enumerate(steps):
        sy = y + 64 + k * 74
        out.append(f'<circle cx="{MX + 44}" cy="{sy + 28}" r="18" fill="{th["accent"]}"/>'
                   + text(str(k + 1), MX + 44, sy + 35, 18, "#FFFFFF"))
        lines, cur = [], ""
        for w_ in tr(s_).split():
            t = (cur + " " + w_).strip()
            if width(t, 15, "SemiBold") > cw - 110 and cur:
                lines.append(cur)
                cur = w_
            else:
                cur = t
        lines.append(cur)
        for j, ln in enumerate(lines[:2]):
            out.append(text(ln, MX + 76, sy + 24 + j * 21, 15, th["ink"], "SemiBold", "start"))
    x2 = MX + cw + 20
    out.append(_card(x2, y, cw, 300, th))
    out.append(text("Try these at home", x2 + cw / 2, y + 40, 18, th["ink"]))
    tests = [("Lemon juice", "#D81B3C"), ("Vinegar", "#E5326A"), ("Tap water", "#7E57C2"), ("Baking soda", "#3A86C8"),
             ("Soap", "#3DAA5C"), ("Bleach (adult only)", "#E0C431")]
    for k, (t_, col) in enumerate(tests):
        tx = x2 + 24 + (k % 2) * ((cw - 48) / 2)
        ty = y + 66 + (k // 2) * 72
        out.append(f'<rect x="{tx:.1f}" y="{ty}" width="{(cw - 48) / 2 - 10:.1f}" height="60" rx="12" '
                   f'fill="{mix(th["card"], col, .2)}"/>')
        out.append(f'<circle cx="{tx + 28:.1f}" cy="{ty + 30}" r="14" fill="{col}"/>')
        out.append(fit_text(t_, tx + 52, ty + 36, 15, th["ink"], (cw - 48) / 2 - 70, "SemiBold", "start"))
    return W, H, "".join(out)


POSTERS = [
    ("chemistry-of-fireworks", fireworks, "Chemistry of fireworks chart, metal salts and the colors they produce",
     ["fireworks", "firework colors", "metal salts", "flame colors", "strontium", "barium", "copper", "sodium",
      "pyrotechnics", "oxidizer", "celebration", "new year", "chemistry fun", "combustion"]),
    ("red-cabbage-indicator", cabbage, "Red cabbage indicator chart, natural pH color scale from 1 to 14",
     ["red cabbage", "natural indicator", "ph indicator", "ph scale", "anthocyanin", "kitchen experiment",
      "acids and bases", "color change", "home experiment", "kids science", "lemon", "vinegar", "baking soda",
      "science project"]),
]

TR.update({
    "THE CHEMISTRY OF FIREWORKS": "KIMIA KEMBANG API", "Metal salts give each firework its color":
        "Garam logam memberi warna pada setiap kembang api",
    "Red": "Merah", "Orange": "Jingga", "Yellow": "Kuning", "Green": "Hijau", "Blue": "Biru", "Purple": "Ungu",
    "White / silver": "Putih / perak", "Gold sparks": "Percikan emas", "Strontium": "Stronsium", "Calcium": "Kalsium",
    "Sodium": "Natrium", "Barium": "Barium", "Copper": "Tembaga", "Strontium + copper": "Stronsium + tembaga",
    "Magnesium, aluminium": "Magnesium, aluminium", "Iron filings": "Serbuk besi",
    "What is inside a firework shell?": "Apa isi selongsong kembang api?", "Fuel": "Bahan bakar",
    "Oxidizer": "Oksidator", "Color": "Pewarna", "Binder": "Perekat", "charcoal, sulfur": "arang, belerang",
    "nitrates, perchlorates": "nitrat, perklorat", "metal salts": "garam logam",
    "holds the stars together": "merekatkan butiran bintang",
    "RED CABBAGE INDICATOR": "INDIKATOR KUBIS UNGU",
    "A natural pH indicator you can make in the kitchen": "Indikator pH alami yang bisa dibuat di dapur",
    "Acid": "Asam", "Neutral": "Netral", "Base": "Basa", "How to make it": "Cara membuat",
    "Chop red cabbage and cover it with hot water": "Iris kubis ungu lalu rendam dengan air panas",
    "Leave for 10 minutes, then strain the purple liquid": "Diamkan 10 menit, lalu saring cairan ungunya",
    "Add a little to each test sample and compare the color": "Teteskan ke setiap sampel uji lalu bandingkan warnanya",
    "Try these at home": "Coba di rumah", "Lemon juice": "Air jeruk nipis", "Vinegar": "Cuka", "Tap water": "Air keran",
    "Baking soda": "Soda kue", "Soap": "Sabun", "Bleach (adult only)": "Pemutih (oleh orang dewasa)",
})
