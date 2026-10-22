"""Poster edukasi kimia jilid 28: proses industri Haber (amonia) dan proses kontak (asam sulfat).
Didaftarkan ke posters.py lewat POSTERS (semua tema x 2 bahasa).
"""
from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters12 import eq_arrow
from posters2 import _card
from posters3 import arrow_line, mix
from posters4 import chem

INK = "#1E2A3A"


def _box(x, y, w, h, title, sub, col, th):
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{mix(th["card"], col, .22)}" '
           f'stroke="{col}" stroke-width="3"/>']
    out.append(fit_text(title, x + w / 2, y + h / 2 - (4 if sub else -6), 17, th["ink"], w - 20))
    if sub:
        out.append(chem(tr(sub), x + w / 2, y + h / 2 + 20, 14, th["sub"], "middle", "SemiBold"))
    return "".join(out)


def _cond(items, y, th):
    """Deretan kartu kondisi reaksi."""
    out = []
    n = len(items)
    cw = (W_ - 2 * MX - 40 - (n - 1) * 14) / n
    for k, (lab, val, col) in enumerate(items):
        x = MX + 20 + k * (cw + 14)
        out.append(f'<rect x="{x:.1f}" y="{y}" width="{cw:.1f}" height="92" rx="14" fill="{th["plate"]}"/>')
        out.append(f'<rect x="{x:.1f}" y="{y}" width="{cw:.1f}" height="8" rx="4" fill="{col}"/>')
        out.append(chem(tr(val), x + cw / 2, y + 50, 24, INK, "middle"))
        out.append(fit_text(lab, x + cw / 2, y + 76, 13, "#5B6878", cw - 16, "SemiBold"))
    return "".join(out)


W_ = 1226


def haber(th):
    W = W_
    top = 122
    H = top + 110 + 20 + 330 + 20 + 160 + 50
    out = [header(W, th, "THE HABER PROCESS", "Making ammonia from nitrogen and hydrogen for fertilizers")]
    out.append(_card(MX, top, W - 2 * MX, 110, th))
    cx = W / 2
    out.append(chem("N_{2}(g) + 3H_{2}(g)", cx - 34, top + 66, 30, th["accent"], "end"))
    out.append(eq_arrow(cx - 24, cx + 24, top + 56, th["accent"]))
    out.append(chem("2NH_{3}(g)    ΔH = −92 kJ", cx + 34, top + 66, 30, th["accent"], "start"))
    y = top + 130
    out.append(_card(MX, y, W - 2 * MX, 330, th))
    bw, bh = 190, 86
    xs = [MX + 30, MX + 270, MX + 510, MX + 760]
    by = y + 60
    out.append(_box(xs[0], by - 30, bw, bh - 10, "Nitrogen", "from the air", T, th))
    out.append(_box(xs[0], by + 80, bw, bh - 10, "Hydrogen", "from natural gas", O, th))
    out.append(_box(xs[1], by + 20, bw, bh, "Compressor", "200 atm", "#7C8B9C", th))
    out.append(_box(xs[2], by + 20, bw, bh, "Reactor", "Fe catalyst, 450 °C", R, th))
    out.append(_box(xs[3], by + 20, bw + 76, bh, "Condenser", "cools the gases", "#3D7DDB", th))
    out.append(_box(xs[3] + 40, by + 170, bw, bh - 10, "Liquid ammonia", "NH_{3}(l)", P, th))
    acc = th["accent"]
    out.append(arrow_line(xs[0] + bw + 4, by + 8, xs[1] - 6, by + 50, acc, 4))
    out.append(arrow_line(xs[0] + bw + 4, by + 118, xs[1] - 6, by + 74, acc, 4))
    out.append(arrow_line(xs[1] + bw + 4, by + 63, xs[2] - 6, by + 63, acc, 4))
    out.append(arrow_line(xs[2] + bw + 4, by + 63, xs[3] - 6, by + 63, acc, 4))
    out.append(arrow_line(xs[3] + 135, by + bh + 22, xs[3] + 135, by + 166, acc, 4))
    # daur ulang gas yang belum bereaksi
    ry = by + 222
    out.append(f'<path d="M{xs[3] + 20} {by + bh + 20}V{ry}H{xs[2] + bw / 2}V{by + bh + 30}" fill="none" '
               f'stroke="{th["sub"]}" stroke-width="3.5" stroke-dasharray="9 6"/>')
    out.append(arrow_line(xs[2] + bw / 2, by + bh + 50, xs[2] + bw / 2, by + bh + 26, th["sub"], 3.5))
    out.append(fit_text("Unreacted N₂ and H₂ are recycled", (xs[2] + bw / 2 + xs[3]) / 2 - 10, ry + 24, 14,
                        th["sub"], 230, "SemiBold"))
    y += 350
    out.append(_card(MX, y, W - 2 * MX, 160, th))
    out.append(text("Compromise conditions", W / 2, y + 36, 17, th["ink"]))
    out.append(_cond([("Temperature", "450 °C", R), ("Pressure", "200 atm", "#7C8B9C"),
                      ("Catalyst", "Iron (Fe)", T), ("Yield per pass", "≈ 15%", P)], y + 54, th))
    out.append(text("Higher pressure and lower temperature give more NH₃, but a moderate temperature keeps the "
                    "reaction fast", W / 2, H - 22, 13, th["sub"], "SemiBold"))
    return W, H, "".join(out)


def contact(th):
    W = W_
    top = 122
    H = top + 4 * 104 + 20 + 160 + 50
    out = [header(W, th, "THE CONTACT PROCESS", "Industrial production of sulfuric acid in four steps")]
    steps = [("Burning sulfur", "S(s) + O_{2}(g) → SO_{2}(g)", T),
             ("Catalytic oxidation", "2SO_{2}(g) + O_{2}(g) ⇌ 2SO_{3}(g)", R),
             ("Making oleum", "SO_{3}(g) + H_{2}SO_{4}(l) → H_{2}S_{2}O_{7}(l)", O),
             ("Diluting oleum", "H_{2}S_{2}O_{7}(l) + H_{2}O(l) → 2H_{2}SO_{4}(l)", P)]
    for i, (name, eq, col) in enumerate(steps):
        y = top + i * 104
        out.append(_card(MX, y, W - 2 * MX, 90, th))
        out.append(f'<circle cx="{MX + 44}" cy="{y + 45}" r="22" fill="{col}"/>'
                   + text(str(i + 1), MX + 44, y + 53, 22, "#FFFFFF"))
        out.append(fit_text(name, MX + 84, y + 53, 20, th["ink"], 300, anchor="start"))
        bx = MX + 400
        bw = W - MX - 20 - bx
        out.append(f'<rect x="{bx}" y="{y + 16}" width="{bw}" height="58" rx="12" fill="{th["plate"]}"/>')
        if "⇌" in eq:
            lhs, rhs = eq.split(" ⇌ ")
            cx = bx + bw / 2
            out.append(chem(lhs, cx - 30, y + 54, 21, INK, "end"))
            out.append(eq_arrow(cx - 20, cx + 20, y + 45, INK))
            out.append(chem(rhs, cx + 30, y + 54, 21, INK, "start"))
        else:
            out.append(chem(eq, bx + bw / 2, y + 54, 21, INK, "middle"))
    for i in range(3):  # penghubung antartahap, digambar setelah kartu agar tidak tertutup
        y = top + i * 104
        out.append(arrow_line(MX + 44, y + 69, MX + 44, y + 125, th["accent"], 3))
    y = top + 4 * 104 + 10
    out.append(_card(MX, y, W - 2 * MX, 160, th))
    out.append(text("Conditions for step 2", W / 2, y + 36, 17, th["ink"]))
    out.append(_cond([("Temperature", "450 °C", R), ("Pressure", "1–2 atm", "#7C8B9C"),
                      ("Catalyst", "V_{2}O_{5}", T), ("Conversion", "≈ 99%", P)], y + 54, th))
    out.append(text("SO₃ is not added straight to water because it forms a corrosive mist of acid droplets", W / 2,
                    H - 22, 13, th["sub"], "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("haber-process", haber, "Haber process chart, industrial ammonia production with flow diagram and conditions",
     ["haber process", "ammonia", "industrial chemistry", "nitrogen", "hydrogen", "fertilizer", "catalyst", "iron",
      "equilibrium", "le chatelier", "flow diagram", "chemical industry", "reversible reaction", "nh3"]),
    ("contact-process", contact, "Contact process chart, industrial sulfuric acid production in four steps",
     ["contact process", "sulfuric acid", "industrial chemistry", "sulfur dioxide", "sulfur trioxide", "oleum",
      "vanadium pentoxide", "catalyst", "equilibrium", "chemical industry", "h2so4", "reaction steps",
      "manufacturing", "acid"]),
]

TR.update({
    "THE HABER PROCESS": "PROSES HABER",
    "Making ammonia from nitrogen and hydrogen for fertilizers": "Pembuatan amonia dari nitrogen dan hidrogen untuk pupuk",
    "Nitrogen": "Nitrogen", "Hydrogen": "Hidrogen", "from the air": "dari udara", "from natural gas": "dari gas alam",
    "Compressor": "Kompresor", "Reactor": "Reaktor", "Fe catalyst, 450 °C": "katalis Fe, 450 °C",
    "Condenser": "Kondensor", "cools the gases": "mendinginkan gas", "Liquid ammonia": "Amonia cair",
    "Unreacted N₂ and H₂ are recycled": "N₂ dan H₂ sisa dialirkan kembali",
    "Compromise conditions": "Kondisi optimum (kompromi)", "Temperature": "Suhu", "Pressure": "Tekanan",
    "Catalyst": "Katalis", "Yield per pass": "Hasil per siklus", "Iron (Fe)": "Besi (Fe)",
    "Higher pressure and lower temperature give more NH₃, but a moderate temperature keeps the reaction fast":
        "Tekanan tinggi dan suhu rendah menghasilkan NH₃ lebih banyak, tetapi suhu sedang menjaga reaksi tetap cepat",
    "THE CONTACT PROCESS": "PROSES KONTAK",
    "Industrial production of sulfuric acid in four steps": "Pembuatan asam sulfat di industri dalam empat tahap",
    "Burning sulfur": "Pembakaran belerang", "Catalytic oxidation": "Oksidasi dengan katalis",
    "Making oleum": "Pembentukan oleum", "Diluting oleum": "Pengenceran oleum",
    "Conditions for step 2": "Kondisi tahap 2", "Conversion": "Konversi",
    "SO₃ is not added straight to water because it forms a corrosive mist of acid droplets":
        "SO₃ tidak langsung dilarutkan ke air karena membentuk kabut asam yang korosif",
})
