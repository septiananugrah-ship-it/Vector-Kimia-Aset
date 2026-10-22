"""Poster edukasi kimia jilid 39: kurva kelarutan (larutan jenuh/tak jenuh/lewat jenuh) dan faktor laju pelarutan.
Didaftarkan ke posters.py lewat POSTERS (semua tema x 2 bahasa).
"""
import random

from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, particle, text, tr
from posters2 import _card
from posters3 import mix
from posters4 import chem
from render import style_attrs
from textpath import width

INK = "#1E2A3A"

# gram zat per 100 g air pada 0, 20, 40, 60, 80, 100 °C (nilai pendekatan dari tabel kelarutan umum)
CURVES = [("KNO_{3}", [13, 32, 64, 110, 169, 246], R), ("NaNO_{3}", [73, 88, 104, 124, 148, 180], O),
          ("KCl", [28, 34, 40, 45, 51, 56], T), ("NaCl", [36, 36, 37, 37, 38, 39], P),
          ("Ce_{2}(SO_{4})_{3}", [20, 10, 5, 4, 2.5, 2], "#7C8B9C")]


def solubility_curve(th):
    W = 1226
    top = 122
    H = top + 520 + 20 + 190 + 30
    out = [header(W, th, "SOLUBILITY CURVES", "How much solute dissolves in 100 g of water at different temperatures")]
    out.append(_card(MX, top, 760, 520, th))
    gx, gy, gw, gh = MX + 90, top + 460, 620, 400
    ymax = 250
    for k in range(6):
        y = gy - gh * k * 50 / ymax
        out.append(f'<path d="M{gx} {y:.1f}H{gx + gw}" stroke="{th["card_stroke"]}" stroke-width="1.4"/>')
        out.append(text(str(k * 50), gx - 12, y + 5, 13, th["sub"], "SemiBold", "end"))
    for k in range(6):
        x = gx + gw * k / 5
        out.append(text(str(k * 20), x, gy + 24, 13, th["sub"], "SemiBold"))
    out.append(f'<path d="M{gx} {gy - gh}V{gy}H{gx + gw}" fill="none" stroke="{th["sub"]}" stroke-width="2.4"/>')
    out.append(text("Temperature (°C)", gx + gw / 2, gy + 50, 14, th["ink"], "SemiBold"))
    out.append(text("g / 100 g water", gx - 60, gy - gh - 14, 13, th["ink"], "SemiBold", "start"))
    for name, vals, col in CURVES:
        pts = [(gx + gw * k / 5, gy - gh * v / ymax) for k, v in enumerate(vals)]
        d = "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
        out.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="4.5" stroke-linejoin="round" '
                   'stroke-linecap="round"/>')
        lc = col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3)
        if name.startswith("Ce"):  # label di tengah kurva agar tidak terpotong tepi kartu
            out.append(chem(name, pts[3][0], pts[3][1] - 14, 14, lc, "middle"))
        else:
            lx, ly = pts[-1]
            out.append(chem(name, lx + 8, ly + (6 if name != "KCl" else -6), 14, lc, "start"))
    rx = MX + 780
    rw = W - MX - rx
    out.append(_card(rx, top, rw, 520, th))
    out.append(text("Reading the curve", rx + rw / 2, top + 40, 18, th["ink"]))
    zones = [("Saturated", "A point ON the curve: no more solute can dissolve", "#3D7DDB"),
             ("Unsaturated", "A point BELOW the curve: more solute can dissolve", "#4BB04A"),
             ("Supersaturated", "A point ABOVE the curve: unstable, crystals form easily", R)]
    for k, (name, desc, col) in enumerate(zones):
        y = top + 64 + k * 146
        out.append(f'<rect x="{rx + 20}" y="{y}" width="{rw - 40}" height="130" rx="14" '
                   f'fill="{mix(th["card"], col, .18)}"/>')
        out.append(text(name, rx + rw / 2, y + 36, 19, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3)))
        lines, cur = [], ""
        for w_ in tr(desc).split():
            t = (cur + " " + w_).strip()
            if width(t, 14, "SemiBold") > rw - 70 and cur:
                lines.append(cur)
                cur = w_
            else:
                cur = t
        lines.append(cur)
        for j, ln in enumerate(lines[:3]):
            out.append(text(ln, rx + rw / 2, y + 66 + j * 20, 14, th["ink"], "SemiBold"))
    y = top + 540
    out.append(_card(MX, y, W - 2 * MX, 190, th))
    out.append(text("Example", W / 2, y + 40, 18, th["ink"]))
    for j, ln in enumerate(("At 60 °C, about 110 g of KNO₃ dissolves in 100 g of water.",
                            "Cooling to 20 °C, only 32 g stays dissolved, so about 78 g crystallizes out.")):
        out.append(fit_text(ln, W / 2, y + 86 + j * 36, 17, th["ink"], W - 2 * MX - 60, "SemiBold"))
    out.append(text("Values are approximate", W / 2, y + 170, 12.5, th["sub"], "SemiBold"))
    return W, H, "".join(out)


def _beaker_dissolve(cx, cy, n, size, stir, hot, key):
    rnd = random.Random(key)
    out = [f'<rect x="{cx - 60}" y="{cy - 50}" width="120" height="110" fill="{"#F7C6B8" if hot else "#BFE3F5"}"/>',
           f'<path d="M{cx - 64} {cy - 76}V{cy + 60}H{cx + 64}V{cy - 76}" fill="none" stroke="{INK}" stroke-width="4" '
           'stroke-linejoin="round"/>']
    out.append(f'<g {style_attrs(1.2)}>')
    for k in range(n):
        x = cx + rnd.uniform(-48, 48)
        y = cy + rnd.uniform(10, 50) if size > 6 else cy + rnd.uniform(-40, 50)
        out.append(particle(x, y, size, "#FFFFFF", f"{key}{k}", shine=False))
    out.append('</g>')
    if stir:
        out.append(f'<path d="M{cx + 20} {cy - 100}L{cx - 10} {cy + 46}" stroke="#7C8B9C" stroke-width="6" '
                   'stroke-linecap="round"/><path d="M' + f'{cx - 40} {cy + 10}a40 14 0 1 0 80 0" fill="none" '
                   f'stroke="{INK}" stroke-width="2.5" stroke-dasharray="6 5"/>')
    if hot:
        for k in range(3):
            out.append(f'<path d="M{cx - 30 + k * 30} {cy + 96}c-10 -12 -2 -22 0 -30c6 10 12 18 0 30z" fill="#F28C38"/>')
    return "".join(out)


def dissolving(th):
    W = 1226
    top = 122
    gap = 18
    cw = (W - 2 * MX - 2 * gap) / 3
    ch = 420
    H = top + ch + 20 + 120 + 30
    out = [header(W, th, "FACTORS AFFECTING DISSOLVING", "Three ways to make a solid dissolve faster")]
    factors = [("Stirring", "Moves fresh solvent next to the solid", (False, True, False, 10), T),
               ("Higher temperature", "Particles move faster and collide more often", (False, False, True, 10), R),
               ("Smaller particles", "Crushed solid has more surface area", (True, False, False, 4), P)]
    for k, (name, desc, (fine, stir, hot, size), col) in enumerate(factors):
        x = MX + k * (cw + gap)
        out.append(_card(x, top, cw, ch, th))
        out.append(f'<rect x="{x}" y="{top}" width="{cw}" height="56" rx="14" fill="{col}"/>'
                   f'<rect x="{x}" y="{top + 30}" width="{cw}" height="26" fill="{col}"/>')
        out.append(fit_text(name, x + cw / 2, top + 38, 21, "#FFFFFF", cw - 20))
        out.append(f'<rect x="{x + 20}" y="{top + 72}" width="{cw - 40}" height="250" rx="14" fill="{th["plate"]}"/>')
        out.append(_beaker_dissolve(x + cw / 2, top + 196, 40 if fine else 6, size, stir, hot, f"ds{k}"))
        lines, cur = [], ""
        for w_ in tr(desc).split():
            t = (cur + " " + w_).strip()
            if width(t, 15, "SemiBold") > cw - 50 and cur:
                lines.append(cur)
                cur = w_
            else:
                cur = t
        lines.append(cur)
        for j, ln in enumerate(lines[:3]):
            out.append(text(ln, x + cw / 2, top + 356 + j * 22, 15, th["ink"], "SemiBold"))
    y = top + ch + 20
    out.append(_card(MX, y, W - 2 * MX, 120, th))
    out.append(fit_text("Solute + solvent → solution · e.g. sugar (solute) dissolves in tea (solvent)", W / 2, y + 52,
                        17, th["ink"], W - 2 * MX - 60, "SemiBold"))
    out.append(fit_text("These factors change how FAST it dissolves; only temperature changes how MUCH can dissolve",
                        W / 2, y + 88, 14, th["sub"], W - 2 * MX - 60, "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("solubility-curves", solubility_curve, "Solubility curves chart, saturated, unsaturated and supersaturated "
                                            "solutions",
     ["solubility curve", "solubility", "saturated solution", "unsaturated", "supersaturated", "crystallization",
      "potassium nitrate", "sodium chloride", "temperature", "graph", "solutions", "solute", "solvent",
      "physical chemistry"]),
    ("factors-dissolving", dissolving, "Factors affecting dissolving chart, stirring, temperature and particle size",
     ["dissolving", "rate of dissolving", "solubility", "stirring", "temperature", "particle size", "surface area",
      "solute", "solvent", "solution", "sugar", "mixtures", "science experiment", "kids science"]),
]

TR.update({
    "SOLUBILITY CURVES": "KURVA KELARUTAN",
    "How much solute dissolves in 100 g of water at different temperatures":
        "Banyaknya zat terlarut dalam 100 g air pada berbagai suhu",
    "Temperature (°C)": "Suhu (°C)", "g / 100 g water": "g / 100 g air", "Reading the curve": "Membaca kurva",
    "Saturated": "Jenuh", "Unsaturated": "Tak jenuh", "Supersaturated": "Lewat jenuh",
    "A point ON the curve: no more solute can dissolve": "Titik TEPAT pada kurva: zat tidak dapat larut lagi",
    "A point BELOW the curve: more solute can dissolve": "Titik DI BAWAH kurva: zat masih dapat larut",
    "A point ABOVE the curve: unstable, crystals form easily": "Titik DI ATAS kurva: tidak stabil, mudah mengkristal",
    "Example": "Contoh",
    "At 60 °C, about 110 g of KNO₃ dissolves in 100 g of water.": "Pada 60 °C, sekitar 110 g KNO₃ larut dalam 100 g air.",
    "Cooling to 20 °C, only 32 g stays dissolved, so about 78 g crystallizes out.":
        "Saat didinginkan ke 20 °C, hanya 32 g yang tetap larut, sehingga sekitar 78 g mengkristal.",
    "Values are approximate": "Nilai merupakan perkiraan",
    "FACTORS AFFECTING DISSOLVING": "FAKTOR YANG MEMENGARUHI PELARUTAN",
    "Three ways to make a solid dissolve faster": "Tiga cara agar zat padat lebih cepat larut",
    "Stirring": "Pengadukan", "Higher temperature": "Suhu lebih tinggi", "Smaller particles": "Ukuran partikel lebih kecil",
    "Moves fresh solvent next to the solid": "Pelarut baru terus bersentuhan dengan zat padat",
    "Particles move faster and collide more often": "Partikel bergerak lebih cepat dan lebih sering bertumbukan",
    "Crushed solid has more surface area": "Zat yang dihaluskan memiliki luas permukaan lebih besar",
    "Solute + solvent → solution · e.g. sugar (solute) dissolves in tea (solvent)":
        "Zat terlarut + pelarut → larutan · contoh: gula (zat terlarut) larut dalam teh (pelarut)",
    "These factors change how FAST it dissolves; only temperature changes how MUCH can dissolve":
        "Faktor-faktor ini mengubah seberapa CEPAT zat larut; hanya suhu yang mengubah seberapa BANYAK zat dapat larut",
})
