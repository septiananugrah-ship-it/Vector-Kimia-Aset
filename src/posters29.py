"""Poster edukasi kimia jilid 29: alotrop karbon dan penyepuhan listrik (electroplating).
Didaftarkan ke posters.py lewat POSTERS (semua tema x 2 bahasa).
"""
import math

from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, particle, text, tr
from posters2 import _card
from posters3 import arrow_line, mix
from posters4 import chem
from render import style_attrs
from textpath import width

INK = "#1E2A3A"
CARB = "#4A4F5C"


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


def _net(pts, max_d, key, r=7, col=CARB, bond="#7C8B9C", bw=4):
    out = [f'<g {style_attrs(1.2)}>']
    for i, (x1, y1) in enumerate(pts):
        for x2, y2 in pts[i + 1:]:
            if math.hypot(x2 - x1, y2 - y1) < max_d:
                out.append(f'<path d="M{x1:.1f} {y1:.1f}L{x2:.1f} {y2:.1f}" stroke="{bond}" stroke-width="{bw}"/>')
    for k, (x, y) in enumerate(pts):
        out.append(particle(x, y, r, col, f"{key}{k}", shine=False))
    out.append('</g>')
    return "".join(out)


def _hex_sheet(cx, cy, cols, rows, s, skew=0):
    pts = []
    for r in range(rows):
        for c in range(cols):
            x = cx + (c - cols / 2) * s * math.sqrt(3) + (s * math.sqrt(3) / 2 if r % 2 else 0)
            y = cy + (r - rows / 2) * s * 1.5
            pts.append((x + skew * (y - cy), y))
            pts.append((x + skew * (y - s / 2 - cy), y - s / 2))
    return pts


def _diamond(cx, cy):
    pts = []
    for i in range(-2, 3):
        for j in range(-2, 3):
            x, y = cx + i * 34 + (17 if j % 2 else 0), cy + j * 30
            if math.hypot(x - cx, (y - cy) * 1.2) < 80:
                pts.append((x, y))
    return _net(pts, 40, "dia", r=8)


def _graphite(cx, cy):
    out = []
    for k, dy in enumerate((-56, 0, 56)):
        pts = []
        for c in range(5):
            x = cx - 76 + c * 30 + (15 if k % 2 else 0)
            pts += [(x, cy + dy - 9), (x + 16, cy + dy + 9)]
        out.append(_net(pts, 28, f"gr{k}", r=6))
    for x in (cx - 64, cx + 32):
        out.append(f'<path d="M{x} {cy - 44}V{cy + 44}" stroke="#B9C2CC" stroke-width="2" stroke-dasharray="4 5"/>')
    return "".join(out)


def _graphene(cx, cy):
    pts = []
    for r in range(4):
        for c in range(5):
            x = cx - 72 + c * 34 + (17 if r % 2 else 0)
            y = cy - 45 + r * 30
            pts += [(x, y - 10), (x, y + 10)]
    return _net(pts, 22, "gp", r=5)


def _fullerene(cx, cy):
    out = [f'<circle cx="{cx}" cy="{cy}" r="66" fill="#E9EEF3" stroke="#B9C2CC" stroke-width="2"/>']
    pts = []
    for ring, (rr, n, off) in enumerate(((0, 1, 0), (24, 5, 0), (44, 10, 18), (62, 10, 0))):
        for k in range(n):
            a = math.radians(off + k * 360 / n - 90)
            pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    out.append(_net(pts, 25, "c60", r=5))
    return "".join(out)


def _nanotube(cx, cy):
    out = []
    pts = []
    for c in range(7):
        for r in range(4):
            x = cx - 84 + c * 28 + (14 if r % 2 else 0)
            y = cy - 30 + r * 20
            pts.append((x, y))
    out.append(f'<rect x="{cx - 96}" y="{cy - 42}" width="192" height="84" rx="42" fill="#E9EEF3" '
               'stroke="#B9C2CC" stroke-width="2"/>')
    out.append(_net(pts, 25, "nt", r=5))
    return "".join(out)


ALLOTROPES = [
    ("Diamond", _diamond, "Each C bonded to 4 others in a rigid 3D network",
     "Hardest natural material; does not conduct electricity", "Jewelry, cutting tools", T),
    ("Graphite", _graphite, "Layers of hexagons held by weak forces",
     "Soft and slippery; conducts electricity", "Pencils, lubricants, electrodes", O),
    ("Graphene", _graphene, "A single layer of graphite, one atom thick",
     "Very strong, light and an excellent conductor", "Electronics, sensors, batteries", P),
    ("Fullerene (C₆₀)", _fullerene, "60 carbon atoms shaped like a football",
     "Hollow molecular cages", "Medicine delivery, lubricants", R),
    ("Carbon nanotube", _nanotube, "A sheet of graphene rolled into a tube",
     "Extremely strong and conductive", "Light sports gear, nanotechnology", "#3D7DDB"),
]


def allotropes(th):
    W = 1226
    top = 122
    gap = 16
    cw = (W - 2 * MX - 4 * gap) / 5
    ch = 540
    H = top + ch + 30
    out = [header(W, th, "ALLOTROPES OF CARBON", "The same element, carbon, arranged in different structures")]
    for i, (name, draw, struct, prop, use, col) in enumerate(ALLOTROPES):
        x = MX + i * (cw + gap)
        out.append(_card(x, top, cw, ch, th))
        out.append(f'<rect x="{x}" y="{top}" width="{cw}" height="56" rx="14" fill="{col}"/>'
                   f'<rect x="{x}" y="{top + 30}" width="{cw}" height="26" fill="{col}"/>')
        out.append(fit_text(name, x + cw / 2, top + 37, 18, "#FFFFFF", cw - 16))
        out.append(f'<rect x="{x + 12}" y="{top + 70}" width="{cw - 24}" height="180" rx="12" fill="{th["plate"]}"/>')
        out.append(f'<g transform="translate({x + cw / 2:.1f} {top + 160}) scale(.92) '
                   f'translate({-(x + cw / 2):.1f} {-(top + 160)})">{draw(x + cw / 2, top + 160)}</g>')
        y = top + 270
        for lab, val in (("Structure", struct), ("Properties", prop), ("Uses", use)):
            out.append(text(lab, x + cw / 2, y + 18, 12, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .35),
                            "Bold"))
            lines = _wrap(val, 13.5, cw - 22)
            for j, ln in enumerate(lines[:4]):
                out.append(text(ln, x + cw / 2, y + 40 + j * 19, 13.5, th["ink"], "SemiBold"))
            y += 34 + 19 * min(len(lines), 4) + 14
    return W, H, "".join(out)


def electroplating(th):
    W = 1226
    top = 122
    H = top + 470 + 20 + 200 + 30
    out = [header(W, th, "ELECTROPLATING", "Coating an object with a thin layer of metal using electricity")]
    out.append(_card(MX, top, 640, 470, th))
    x0, y0 = MX + 20, top + 20
    out.append(f'<rect x="{x0}" y="{y0}" width="600" height="430" rx="14" fill="{th["plate"]}"/>')
    # baterai
    bx, by = x0 + 300, y0 + 50
    out.append(f'<rect x="{bx - 50}" y="{by - 22}" width="100" height="44" rx="8" fill="#F2C94C" stroke="{INK}" '
               'stroke-width="3"/>' + text("+", bx - 30, by + 8, 22, INK) + text("−", bx + 30, by + 8, 22, INK))
    # gelas kimia
    gx, gy, gw, gh = x0 + 90, y0 + 150, 420, 250
    out.append(f'<rect x="{gx}" y="{gy + 60}" width="{gw}" height="{gh - 60}" fill="#7FB8E8"/>')
    out.append(f'<path d="M{gx} {gy}V{gy + gh}H{gx + gw}V{gy}" fill="none" stroke="{INK}" stroke-width="4"/>')
    # anoda tembaga (kiri) dan kunci (katoda, kanan)
    ax, kx = gx + 90, gx + gw - 110
    out.append(f'<rect x="{ax - 18}" y="{gy - 30}" width="36" height="230" rx="4" fill="#C8743A" stroke="{INK}" '
               'stroke-width="3"/>')
    out.append(f'<g transform="translate({kx} {gy + 110})"><circle cx="0" cy="-40" r="26" fill="#D9A55A" '
               f'stroke="{INK}" stroke-width="3"/><circle cx="0" cy="-40" r="9" fill="#7FB8E8" stroke="{INK}" '
               f'stroke-width="2"/><path d="M-8 -14H8V70H-8Z M8 30h16v10H8z M8 50h12v10H8z" fill="#D9A55A" '
               f'stroke="{INK}" stroke-width="3" stroke-linejoin="round"/></g>')
    out.append(f'<path d="M{ax} {gy - 30}V{by}H{bx - 50}" fill="none" stroke="#E8573F" stroke-width="4"/>')
    out.append(f'<path d="M{kx} {gy + 44}V{by}H{bx + 50}" fill="none" stroke="#3D62C4" stroke-width="4"/>')
    for k in range(5):  # ion Cu2+ bergerak ke katoda
        ix = ax + 50 + k * 34
        iy = gy + 110 + (k % 2) * 50
        out.append(f'<g {style_attrs(1.2)}>' + particle(ix, iy, 8, "#C8743A", f"cu{k}") + '</g>')
        out.append(text("2+", ix + 14, iy - 6, 10, INK))
    out.append(arrow_line(ax + 40, gy + 215, kx - 40, gy + 215, INK, 3))
    out.append(text("Cu²⁺ ions move to the cathode", gx + gw / 2, gy + 238, 13, INK, "SemiBold"))
    out.append(text("Anode (+): copper", ax - 26, gy - 4, 14, "#B5562B", "Bold", "end"))
    out.append(text("Cathode (−): object", kx + 14, gy - 16, 14, "#3D62C4", "Bold", "start"))
    out.append(text("CuSO₄ solution", (ax + kx) / 2, gy + 86, 13, INK, "SemiBold"))
    rx = MX + 660
    rw = W - MX - rx
    out.append(_card(rx, top, rw, 470, th))
    out.append(text("At the electrodes", rx + rw / 2, top + 44, 18, th["ink"]))
    for k, (lab, eq, col) in enumerate((("Anode (oxidation)", "Cu → Cu^{2+} + 2e^{−}", "#B5562B"),
                                        ("Cathode (reduction)", "Cu^{2+} + 2e^{−} → Cu", "#3D62C4"))):
        y = top + 70 + k * 120
        out.append(f'<rect x="{rx + 20}" y="{y}" width="{rw - 40}" height="100" rx="14" '
                   f'fill="{mix(th["card"], col, .2)}"/>')
        out.append(text(lab, rx + rw / 2, y + 34, 16, th["ink"]))
        out.append(chem(eq, rx + rw / 2, y + 74, 22, th["ink"], "middle"))
    for j, ln in enumerate(_wrap("The copper anode dissolves while an even layer of copper builds up on the object",
                                 15, rw - 50)):
        out.append(text(ln, rx + rw / 2, top + 340 + j * 24, 15, th["sub"], "SemiBold"))
    y = top + 490
    out.append(_card(MX, y, W - 2 * MX, 200, th))
    out.append(text("Uses of electroplating", W / 2, y + 40, 18, th["ink"]))
    uses = [("Silver-plated cutlery", "#B9C2CC"), ("Gold-plated jewelry", "#E0B23A"),
            ("Chrome car parts", "#7C8B9C"), ("Tin-plated food cans", "#9AA5B1"), ("Rust protection", "#B5562B")]
    uw = (W - 2 * MX - 40 - 4 * 12) / 5
    for k, (u, col) in enumerate(uses):
        ux = MX + 20 + k * (uw + 12)
        out.append(f'<rect x="{ux:.1f}" y="{y + 62}" width="{uw:.1f}" height="110" rx="14" '
                   f'fill="{mix(th["card"], col, .25)}"/>')
        out.append(f'<circle cx="{ux + uw / 2:.1f}" cy="{y + 98}" r="18" fill="{col}" stroke="{INK}" stroke-width="2"/>')
        out.append(fit_text(u, ux + uw / 2, y + 150, 14, th["ink"], uw - 16, "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("allotropes-of-carbon", allotropes, "Allotropes of carbon chart, diamond, graphite, graphene, fullerene, nanotube",
     ["allotropes", "carbon", "diamond", "graphite", "graphene", "fullerene", "carbon nanotube", "buckyball",
      "crystal structure", "nanotechnology", "materials science", "covalent network", "c60", "element"]),
    ("electroplating", electroplating, "Electroplating chart, copper plating cell with electrode reactions and uses",
     ["electroplating", "electrolysis", "copper plating", "anode", "cathode", "electrochemistry", "metal coating",
      "copper sulfate", "redox", "gold plating", "chrome plating", "industrial chemistry", "ions", "electrode"]),
]

TR.update({
    "ALLOTROPES OF CARBON": "ALOTROP KARBON",
    "The same element, carbon, arranged in different structures": "Unsur yang sama, karbon, tersusun dalam struktur berbeda",
    "Diamond": "Intan", "Graphite": "Grafit", "Graphene": "Grafena", "Fullerene (C₆₀)": "Fulerena (C₆₀)",
    "Carbon nanotube": "Nanotabung karbon", "Structure": "Struktur", "Properties": "Sifat", "Uses": "Kegunaan",
    "Each C bonded to 4 others in a rigid 3D network": "Tiap C terikat pada 4 C lain dalam jaringan 3D yang kaku",
    "Hardest natural material; does not conduct electricity": "Bahan alami terkeras; tidak menghantarkan listrik",
    "Jewelry, cutting tools": "Perhiasan, alat pemotong",
    "Layers of hexagons held by weak forces": "Lapisan heksagon yang terikat gaya lemah",
    "Soft and slippery; conducts electricity": "Lunak dan licin; menghantarkan listrik",
    "Pencils, lubricants, electrodes": "Pensil, pelumas, elektrode",
    "A single layer of graphite, one atom thick": "Satu lapisan grafit setebal satu atom",
    "Very strong, light and an excellent conductor": "Sangat kuat, ringan, dan penghantar yang sangat baik",
    "Electronics, sensors, batteries": "Elektronik, sensor, baterai",
    "60 carbon atoms shaped like a football": "60 atom karbon berbentuk seperti bola sepak",
    "Hollow molecular cages": "Molekul berbentuk sangkar berongga",
    "Medicine delivery, lubricants": "Penghantar obat, pelumas",
    "A sheet of graphene rolled into a tube": "Lembaran grafena yang digulung menjadi tabung",
    "Extremely strong and conductive": "Sangat kuat dan konduktif",
    "Light sports gear, nanotechnology": "Alat olahraga ringan, nanoteknologi",
    "ELECTROPLATING": "PENYEPUHAN LISTRIK (ELECTROPLATING)",
    "Coating an object with a thin layer of metal using electricity":
        "Melapisi benda dengan lapisan logam tipis menggunakan listrik",
    "Cu²⁺ ions move to the cathode": "Ion Cu²⁺ bergerak ke katode", "Anode (+): copper": "Anode (+): tembaga",
    "Cathode (−): object": "Katode (−): benda", "CuSO₄ solution": "Larutan CuSO₄",
    "At the electrodes": "Reaksi di elektrode", "Anode (oxidation)": "Anode (oksidasi)",
    "Cathode (reduction)": "Katode (reduksi)",
    "The copper anode dissolves while an even layer of copper builds up on the object":
        "Anode tembaga melarut, sementara lapisan tembaga yang rata terbentuk pada benda",
    "Uses of electroplating": "Kegunaan penyepuhan listrik", "Silver-plated cutlery": "Sendok garpu berlapis perak",
    "Gold-plated jewelry": "Perhiasan berlapis emas", "Chrome car parts": "Suku cadang mobil berlapis krom",
    "Tin-plated food cans": "Kaleng makanan berlapis timah", "Rust protection": "Pelindung karat",
})
