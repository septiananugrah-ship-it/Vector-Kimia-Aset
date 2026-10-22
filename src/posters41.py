"""Poster edukasi kimia jilid 41: kimia di dapur (memasak) dan cara kerja sabun (misel).
Didaftarkan ke posters.py lewat POSTERS (semua tema x 2 bahasa).
"""
import math

from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters3 import arrow_line
from textpath import width

INK = "#1E2A3A"


def _wrap(s, size, max_w, weight="SemiBold"):
    lines, cur = [], ""
    for w_ in tr(s).split():
        t = (cur + " " + w_).strip()
        if width(t, size, weight) > max_w and cur:
            lines.append(cur)
            cur = w_
        else:
            cur = t
    return lines + [cur]


def _icon(kind, cx, cy, col):
    """Ilustrasi sederhana untuk tiap proses memasak."""
    if kind == "maillard":  # roti panggang
        return (f'<path d="M{cx - 44} {cy + 34}V{cy - 14}a26 26 0 0 1 20-34h48a26 26 0 0 1 20 34V{cy + 34}Z" '
                f'fill="#C98A4B" stroke="{INK}" stroke-width="3"/><path d="M{cx - 32} {cy + 24}V{cy - 8}a16 16 0 0 1 '
                f'14-22h36a16 16 0 0 1 14 22V{cy + 24}Z" fill="#8B5A2B"/>')
    if kind == "caramel":  # kubus gula -> tetes karamel
        return (f'<rect x="{cx - 62}" y="{cy - 16}" width="38" height="38" rx="6" fill="#FFFFFF" stroke="{INK}" '
                f'stroke-width="3"/><path d="M{cx - 62} {cy - 4}h38M{cx - 43} {cy - 16}v38" stroke="#C9D3DE" '
                f'stroke-width="2"/>' + arrow_line(cx - 16, cy + 3, cx + 12, cy + 3, INK, 3)
                + f'<path d="M{cx + 40} {cy - 30}C{cx + 58} {cy - 4} {cx + 64} {cy + 8} {cx + 64} {cy + 18}a24 24 0 0 1-48 0'
                f'C{cx + 16} {cy + 8} {cx + 22} {cy - 4} {cx + 40} {cy - 30}Z" fill="#B5651D" stroke="{INK}" '
                'stroke-width="3"/>')
    if kind == "egg":  # protein terdenaturasi
        return (f'<ellipse cx="{cx}" cy="{cy + 8}" rx="54" ry="38" fill="#FFFFFF" stroke="{INK}" stroke-width="3"/>'
                f'<circle cx="{cx + 6}" cy="{cy + 4}" r="18" fill="#F2B21C" stroke="{INK}" stroke-width="2.5"/>')
    if kind == "bread":  # ragi + CO2
        out = (f'<path d="M{cx - 54} {cy + 30}Q{cx - 54} {cy - 30} {cx} {cy - 30}Q{cx + 54} {cy - 30} {cx + 54} '
               f'{cy + 30}Z" fill="#E0A458" stroke="{INK}" stroke-width="3"/>')
        for dx, dy, r in ((-24, 6, 6), (0, -6, 5), (20, 10, 7), (-6, 16, 4), (30, -8, 4)):
            out += f'<circle cx="{cx + dx}" cy="{cy + dy}" r="{r}" fill="#F6D9A8"/>'
        return out
    if kind == "baking":  # soda kue
        out = (f'<path d="M{cx - 40} {cy - 30}h80l-8 66h-64z" fill="#F4F5F7" stroke="{INK}" stroke-width="3"/>'
               + text("NaHCO₃", cx, cy + 10, 15, INK))
        for k in range(4):
            out += f'<circle cx="{cx - 24 + k * 16}" cy="{cy - 44 - (k % 2) * 8}" r="5" fill="none" stroke="{col}" stroke-width="2.5"/>'
        return out
    # acar / asam
    return (f'<rect x="{cx - 34}" y="{cy - 30}" width="68" height="70" rx="12" fill="#C9E4A5" stroke="{INK}" '
            f'stroke-width="3"/><rect x="{cx - 38}" y="{cy - 44}" width="76" height="16" rx="5" fill="#E8573F" '
            f'stroke="{INK}" stroke-width="3"/>' + text("pH 3", cx, cy + 12, 18, INK))


COOKING = [("maillard", "Maillard reaction", "Proteins and sugars brown above about 140°C, giving toast and steak flavor", R),
           ("caramel", "Caramelization", "Sugar breaks down with heat into brown, sweet-bitter caramel", O),
           ("egg", "Protein denaturation", "Heat unfolds egg proteins, turning the clear white solid and white", "#E0B23A"),
           ("bread", "Fermentation", "Yeast turns sugar into CO₂ gas, which makes bread dough rise", T),
           ("baking", "Baking soda", "NaHCO₃ releases CO₂ bubbles when heated or mixed with acid", "#3D7DDB"),
           ("pickle", "Pickling", "Acid (low pH) stops bacteria from growing, so food keeps longer", "#4BB04A")]


def cooking(th):
    W = 1226
    top = 122
    gap = 18
    cw = (W - 2 * MX - 2 * gap) / 3
    ch = 330
    H = top + 2 * (ch + gap) + 40
    out = [header(W, th, "CHEMISTRY IN THE KITCHEN", "Cooking is full of chemical reactions")]
    for i, (kind, name, desc, col) in enumerate(COOKING):
        x = MX + (i % 3) * (cw + gap)
        y = top + (i // 3) * (ch + gap)
        out.append(_card(x, y, cw, ch, th))
        out.append(f'<rect x="{x}" y="{y}" width="{cw}" height="8" rx="4" fill="{col}"/>')
        out.append(f'<circle cx="{x + cw / 2}" cy="{y + 110}" r="78" fill="{th["plate"]}"/>')
        out.append(_icon(kind, x + cw / 2, y + 110, col))
        out.append(fit_text(name, x + cw / 2, y + 226, 20, th["ink"], cw - 24))
        for j, ln in enumerate(_wrap(desc, 14.5, cw - 40)):
            out.append(text(ln, x + cw / 2, y + 258 + j * 21, 14.5, th["sub"], "SemiBold"))
    out.append(text("Every recipe is an experiment: heat, acids and microbes change the molecules in food", W / 2,
                    H - 16, 13, th["sub"], "SemiBold"))
    return W, H, "".join(out)


def _soap_molecule(x, y, ang, col_head, tail="#F2A541", scale=1.0):
    a = math.radians(ang)
    pts = []
    for k in range(7):
        d = (10 + k * 7) * scale
        off = (3 if k % 2 else -3) * scale
        px = x + math.cos(a) * d - math.sin(a) * off
        py = y + math.sin(a) * d + math.cos(a) * off
        pts.append(f"{px:.1f} {py:.1f}")
    return (f'<path d="M{x:.1f} {y:.1f}L{" L".join(pts)}" fill="none" stroke="{tail}" stroke-width="{3 * scale:.1f}" '
            'stroke-linejoin="round" stroke-linecap="round"/>'
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{8 * scale:.1f}" fill="{col_head}" stroke="{INK}" '
            f'stroke-width="{1.5 * scale:.1f}"/>')


def soap(th):
    W = 1226
    top = 122
    H = top + 300 + 20 + 380 + 20 + 120 + 30
    out = [header(W, th, "HOW SOAP WORKS", "Soap molecules have a water-loving head and an oil-loving tail")]
    out.append(_card(MX, top, W - 2 * MX, 300, th))
    out.append(f'<rect x="{MX + 30}" y="{top + 30}" width="420" height="240" rx="14" fill="{th["plate"]}"/>')
    out.append(_soap_molecule(MX + 110, top + 150, 0, "#3D7DDB", scale=3.2))
    out.append(text("Hydrophilic head", MX + 110, top + 90, 15, "#3D62C4", "Bold"))
    out.append(text("(loves water, −)", MX + 110, top + 110, 13, "#5B6878", "SemiBold"))
    out.append(text("Hydrophobic tail", MX + 300, top + 90, 15, "#C26A12", "Bold"))
    out.append(text("(loves oil and grease)", MX + 300, top + 110, 13, "#5B6878", "SemiBold"))
    rx = MX + 480
    rw = W - MX - 30 - rx
    steps = ["The tails dig into the grease while the heads stay in the water",
             "Many soap molecules surround the grease, forming a ball called a micelle",
             "The micelles stay suspended in water and are rinsed away"]
    for k, s_ in enumerate(steps):
        y = top + 34 + k * 80
        out.append(f'<circle cx="{rx + 22}" cy="{y + 30}" r="18" fill="{(T, O, P)[k]}"/>'
                   + text(str(k + 1), rx + 22, y + 37, 18, "#FFFFFF"))
        for j, ln in enumerate(_wrap(s_, 16, rw - 60)):
            out.append(text(ln, rx + 54, y + 26 + j * 22, 16, th["ink"], "SemiBold", "start"))
    y = top + 320
    out.append(_card(MX, y, W - 2 * MX, 380, th))
    out.append(text("A micelle trapping grease", W / 2, y + 40, 18, th["ink"]))
    cx, cy = W / 2, y + 210
    out.append(f'<rect x="{MX + 30}" y="{y + 60}" width="{W - 2 * MX - 60}" height="300" rx="14" fill="#CFE8F7"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="58" fill="#F2C94C" stroke="#C99A1C" stroke-width="3"/>')
    out.append(text("Grease", cx, cy + 6, 18, INK))
    for k in range(18):
        ang = k * 20
        a = math.radians(ang)
        hx, hy = cx + math.cos(a) * 118, cy + math.sin(a) * 118
        out.append(_soap_molecule(hx, hy, ang + 180, "#3D7DDB", scale=1.1))
    for k in range(8):
        wx, wy = MX + 90 + (k % 4) * 60 + (k // 4) * 760, y + 110 + (k % 2) * 140 + (k // 4) * 40
        out.append(f'<circle cx="{wx}" cy="{wy}" r="9" fill="#E8573F"/><circle cx="{wx - 10}" cy="{wy + 8}" r="5" '
                   f'fill="#FFFFFF" stroke="{INK}" stroke-width="1"/><circle cx="{wx + 10}" cy="{wy + 8}" r="5" '
                   f'fill="#FFFFFF" stroke="{INK}" stroke-width="1"/>')
    out.append(text("Water", MX + 70, y + 92, 15, "#3D62C4", "Bold", "start"))
    y += 400
    out.append(_card(MX, y, W - 2 * MX, 120, th))
    out.append(text("Soap vs detergent", W / 2, y + 40, 18, th["ink"]))
    out.append(fit_text("Soap is made from fats and NaOH (saponification); detergents are synthetic and still work in "
                        "hard water", W / 2, y + 84, 15, th["sub"], W - 2 * MX - 60, "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("chemistry-in-the-kitchen", cooking, "Chemistry in the kitchen chart, Maillard reaction, caramelization, "
                                          "fermentation",
     ["kitchen chemistry", "cooking", "maillard reaction", "caramelization", "fermentation", "baking soda",
      "denaturation", "pickling", "food chemistry", "everyday chemistry", "yeast", "protein", "sugar", "food"]),
    ("how-soap-works", soap, "How soap works chart, hydrophilic head, hydrophobic tail and micelles",
     ["soap", "how soap works", "micelle", "hydrophilic", "hydrophobic", "detergent", "surfactant", "grease",
      "saponification", "cleaning", "hygiene", "everyday chemistry", "handwashing", "molecules"]),
]

TR.update({
    "CHEMISTRY IN THE KITCHEN": "KIMIA DI DAPUR", "Cooking is full of chemical reactions": "Memasak penuh dengan reaksi kimia",
    "Maillard reaction": "Reaksi Maillard", "Caramelization": "Karamelisasi", "Protein denaturation": "Denaturasi protein",
    "Fermentation": "Fermentasi", "Baking soda": "Soda kue", "Pickling": "Pengasaman (acar)",
    "Proteins and sugars brown above about 140°C, giving toast and steak flavor":
        "Protein dan gula menjadi cokelat di atas sekitar 140°C, memberi aroma roti panggang dan daging bakar",
    "Sugar breaks down with heat into brown, sweet-bitter caramel":
        "Gula terurai oleh panas menjadi karamel cokelat yang manis-pahit",
    "Heat unfolds egg proteins, turning the clear white solid and white":
        "Panas mengubah struktur protein telur sehingga putih telur yang bening menjadi padat dan putih",
    "Yeast turns sugar into CO₂ gas, which makes bread dough rise": "Ragi mengubah gula menjadi gas CO₂ sehingga adonan roti mengembang",
    "NaHCO₃ releases CO₂ bubbles when heated or mixed with acid": "NaHCO₃ melepaskan gelembung CO₂ saat dipanaskan atau dicampur asam",
    "Acid (low pH) stops bacteria from growing, so food keeps longer":
        "Asam (pH rendah) menghambat pertumbuhan bakteri sehingga makanan lebih awet",
    "Every recipe is an experiment: heat, acids and microbes change the molecules in food":
        "Setiap resep adalah percobaan: panas, asam, dan mikroba mengubah molekul dalam makanan",
    "HOW SOAP WORKS": "CARA KERJA SABUN",
    "Soap molecules have a water-loving head and an oil-loving tail":
        "Molekul sabun memiliki kepala yang suka air dan ekor yang suka minyak",
    "Hydrophilic head": "Kepala hidrofilik", "(loves water, −)": "(suka air, −)", "Hydrophobic tail": "Ekor hidrofobik",
    "(loves oil and grease)": "(suka minyak dan lemak)",
    "The tails dig into the grease while the heads stay in the water":
        "Ekor masuk ke dalam lemak, sementara kepala tetap berada di air",
    "Many soap molecules surround the grease, forming a ball called a micelle":
        "Banyak molekul sabun mengepung lemak dan membentuk bola yang disebut misel",
    "The micelles stay suspended in water and are rinsed away": "Misel tetap melayang di air lalu terbilas",
    "A micelle trapping grease": "Misel yang menjebak lemak", "Grease": "Lemak", "Water": "Air",
    "Soap vs detergent": "Sabun vs deterjen",
    "Soap is made from fats and NaOH (saponification); detergents are synthetic and still work in hard water":
        "Sabun dibuat dari lemak dan NaOH (saponifikasi); deterjen bersifat sintetis dan tetap bekerja di air sadah",
})
