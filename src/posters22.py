"""Poster edukasi kimia jilid 22: simbol bahaya GHS dan tabel potensial reduksi standar.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
Piktogram GHS digambar ulang secara sederhana dalam kotak 100 x 100.
"""
import math

from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters3 import mix
from posters4 import chem
from textpath import width

K = "#1A1A1A"
RED = "#E3141B"


def _flame(dx=0, dy=0, s=1):
    return (f'<path transform="translate({dx} {dy}) scale({s})" d="M50 10C60 26 74 36 72 58C71 73 61 82 50 82'
            'C38 82 28 73 29 59C30 46 40 41 41 28C47 37 46 46 51 50C56 40 55 25 50 10Z" fill="' + K + '"/>')


def _sym(kind):
    if kind == "explosive":
        rays = "".join(f'<path d="M{60 + 12 * math.cos(math.radians(a)):.1f} {40 + 12 * math.sin(math.radians(a)):.1f}'
                       f'L{60 + 30 * math.cos(math.radians(a)):.1f} {40 + 30 * math.sin(math.radians(a)):.1f}" '
                       f'stroke="{K}" stroke-width="5" stroke-linecap="round"/>' for a in (-110, -70, -30, 10, 50))
        frags = "".join(f'<rect x="{x}" y="{y}" width="7" height="7" transform="rotate({r} {x + 3.5} {y + 3.5})" '
                        f'fill="{K}"/>' for x, y, r in ((82, 22, 20), (88, 46, 50), (70, 10, 10), (40, 18, 35)))
        return (rays + frags + f'<circle cx="38" cy="66" r="20" fill="{K}"/>'
                f'<rect x="46" y="38" width="10" height="12" rx="2" transform="rotate(40 51 44)" fill="{K}"/>')
    if kind == "flammable":
        return _flame(4, -2, .92) + f'<rect x="18" y="84" width="64" height="7" fill="{K}"/>'
    if kind == "oxidizing":
        return (_flame(17, -4, .66) + f'<circle cx="50" cy="66" r="15" fill="none" stroke="{K}" stroke-width="7"/>'
                f'<rect x="18" y="86" width="64" height="7" fill="{K}"/>')
    if kind == "gas":
        return (f'<g transform="rotate(-28 50 56)"><rect x="14" y="44" width="62" height="24" rx="12" fill="{K}"/>'
                f'<rect x="74" y="49" width="10" height="14" fill="{K}"/><rect x="84" y="45" width="6" height="22" '
                f'rx="2" fill="{K}"/></g>')
    if kind == "corrosive":
        tubes = (f'<g transform="rotate(55 30 26)"><rect x="22" y="6" width="14" height="38" rx="7" fill="none" '
                 f'stroke="{K}" stroke-width="4"/><rect x="24" y="26" width="10" height="16" rx="5" fill="{K}"/></g>'
                 f'<g transform="rotate(-55 70 26)"><rect x="63" y="6" width="14" height="38" rx="7" fill="none" '
                 f'stroke="{K}" stroke-width="4"/><rect x="65" y="26" width="10" height="16" rx="5" fill="{K}"/></g>')
        drops = "".join(f'<path d="M{x} {y}c-3 5 -4 7 -4 9a4 4 0 0 0 8 0c0 -2 -1 -4 -4 -9z" fill="{K}"/>'
                        for x, y in ((24, 46), (24, 58), (76, 46), (76, 58)))
        metal = f'<path d="M6 76H34L32 80L36 84L31 88L34 92H6Z" fill="{K}"/>'
        hand = (f'<path d="M60 92V80C60 76 62 74 65 74H90C93 74 94 76 94 79C94 82 92 83 90 83H84L86 88L80 86'
                f'L82 92Z" fill="{K}"/>')
        return tubes + drops + metal + hand
    if kind == "toxic":
        bones = "".join(f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{K}" stroke-width="7" stroke-linecap="round"/>'
                        f'<circle cx="{x1}" cy="{y1 - 3}" r="4.5" fill="{K}"/><circle cx="{x1 - 3}" cy="{y1 + 3}" r="4.5" '
                        f'fill="{K}"/><circle cx="{x2}" cy="{y2 - 3}" r="4.5" fill="{K}"/>'
                        f'<circle cx="{x2 + 3}" cy="{y2 + 3}" r="4.5" fill="{K}"/>'
                        for x1, y1, x2, y2 in ((24, 64, 76, 88), (24, 88, 76, 64)))
        skull = (f'<circle cx="50" cy="38" r="21" fill="{K}"/><rect x="39" y="48" width="22" height="16" rx="5" '
                 f'fill="{K}"/><circle cx="42" cy="38" r="6" fill="#FFFFFF"/><circle cx="58" cy="38" r="6" '
                 f'fill="#FFFFFF"/><path d="M50 45L46 52H54Z" fill="#FFFFFF"/>'
                 f'<path d="M44 58V64M50 58V64M56 58V64" stroke="#FFFFFF" stroke-width="2.4"/>')
        return bones + skull
    if kind == "irritant":
        return (f'<path d="M43 16H57L54 64H46Z" fill="{K}" stroke="{K}" stroke-width="3" stroke-linejoin="round"/>'
                f'<circle cx="50" cy="78" r="7.5" fill="{K}"/>')
    if kind == "health":
        star = " ".join(f"{50 + (15 if k % 2 == 0 else 6) * math.cos(math.radians(k * 22.5 - 90)):.1f},"
                        f"{66 + (15 if k % 2 == 0 else 6) * math.sin(math.radians(k * 22.5 - 90)):.1f}"
                        for k in range(16))
        return (f'<circle cx="50" cy="22" r="11" fill="{K}"/><path d="M20 92C20 56 33 40 50 40C67 40 80 56 80 92Z" '
                f'fill="{K}"/><polygon points="{star}" fill="#FFFFFF"/>')
    # environment
    tree = (f'<path d="M30 86L32 30M31 52L18 40M31 44L44 32M32 34L24 22M31 62L42 54" fill="none" stroke="{K}" '
            'stroke-width="4.5" stroke-linecap="round"/>')
    fish = (f'<ellipse cx="64" cy="80" rx="16" ry="8" fill="{K}"/><path d="M78 80L92 72V88Z" fill="{K}"/>'
            f'<path d="M54 77l4 4M58 77l-4 4" stroke="#FFFFFF" stroke-width="2"/>')
    return tree + fish + f'<path d="M10 90H92" stroke="{K}" stroke-width="4" stroke-linecap="round"/>'


def pictogram(kind, cx, cy, s):
    """Belah ketupat GHS (setengah diagonal s) dengan simbolnya."""
    d = f"M{cx} {cy - s}L{cx + s} {cy}L{cx} {cy + s}L{cx - s} {cy}Z"
    k = s * 1.2 / 100
    return (f'<path d="{d}" fill="#FFFFFF" stroke="{RED}" stroke-width="{s * .11:.1f}" stroke-linejoin="round"/>'
            f'<g transform="translate({cx - 50 * k:.2f} {cy - 50 * k:.2f}) scale({k:.4f})">{_sym(kind)}</g>')


GHS = [
    ("explosive", "Explosive", "Explosives and self-reactive substances", "Fireworks, TNT"),
    ("flammable", "Flammable", "Flammable gases, liquids and solids", "Ethanol, acetone, petrol"),
    ("oxidizing", "Oxidizing", "Can cause or intensify a fire", "H₂O₂, KMnO₄"),
    ("gas", "Gas under pressure", "Compressed, liquefied or dissolved gas", "Oxygen tank, CO₂ cylinder"),
    ("corrosive", "Corrosive", "Burns skin, damages eyes, corrodes metal", "Sulfuric acid, NaOH"),
    ("toxic", "Acute toxicity", "Toxic or fatal if swallowed, inhaled or touched", "Methanol, cyanide"),
    ("irritant", "Irritant / harmful", "Irritates skin and eyes, harmful", "Citric acid, CaCl₂"),
    ("health", "Health hazard", "Can cause cancer or damage organs", "Benzene, formaldehyde"),
    ("environment", "Environmental hazard", "Toxic to aquatic life", "Copper sulfate, pesticides"),
]


def ghs(th):
    W = 1226
    top = 122
    gap = 18
    cw = (W - 2 * MX - 2 * gap) / 3
    ch = 196
    H = top + 3 * (ch + gap) + 40
    out = [header(W, th, "GHS HAZARD SYMBOLS", "Learn the warning pictograms found on chemical labels")]
    for i, (kind, name, desc, ex) in enumerate(GHS):
        x = MX + (i % 3) * (cw + gap)
        y = top + (i // 3) * (ch + gap)
        out.append(_card(x, y, cw, ch, th))
        out.append(pictogram(kind, x + 92, y + ch / 2, 70))
        tx = x + 182
        tw = cw - 196
        out.append(fit_text(name, tx, y + 58, 20, th["ink"], tw, anchor="start"))
        lines, cur = [], ""
        for w_ in tr(desc).split():
            t = (cur + " " + w_).strip()
            if width(t, 14, "SemiBold") > tw and cur:
                lines.append(cur)
                cur = w_
            else:
                cur = t
        lines.append(cur)
        for j, ln in enumerate(lines[:3]):
            out.append(text(ln, tx, y + 88 + j * 20, 14, th["sub"], "SemiBold", "start"))
        out.append(f'<rect x="{tx}" y="{y + ch - 54}" width="{tw}" height="36" rx="10" '
                   f'fill="{mix(th["card"], RED, .12)}"/>')
        out.append(fit_text(ex, tx + 12, y + ch - 30, 14, th["ink"], tw - 24, anchor="start"))
    out.append(text("GHS = Globally Harmonized System of Classification and Labelling of Chemicals", W / 2, H - 18, 13,
                    th["sub"], "SemiBold"))
    return W, H, "".join(out)


POTENTIALS = [
    ("Li^{+} + e^{−} → Li", -3.04), ("K^{+} + e^{−} → K", -2.93), ("Ca^{2+} + 2e^{−} → Ca", -2.87),
    ("Na^{+} + e^{−} → Na", -2.71), ("Mg^{2+} + 2e^{−} → Mg", -2.37), ("Al^{3+} + 3e^{−} → Al", -1.66),
    ("Zn^{2+} + 2e^{−} → Zn", -0.76), ("Fe^{2+} + 2e^{−} → Fe", -0.44), ("Ni^{2+} + 2e^{−} → Ni", -0.25),
    ("Pb^{2+} + 2e^{−} → Pb", -0.13), ("2H^{+} + 2e^{−} → H_{2}", 0.00), ("Cu^{2+} + 2e^{−} → Cu", 0.34),
    ("I_{2} + 2e^{−} → 2I^{−}", 0.54), ("Ag^{+} + e^{−} → Ag", 0.80), ("Br_{2} + 2e^{−} → 2Br^{−}", 1.07),
    ("Cl_{2} + 2e^{−} → 2Cl^{−}", 1.36), ("Au^{3+} + 3e^{−} → Au", 1.50), ("F_{2} + 2e^{−} → 2F^{−}", 2.87),
]


def potentials(th):
    W = 1226
    top = 122
    rh = 38
    n = len(POTENTIALS)
    H = top + 60 + n * (rh + 6) + 120
    out = [header(W, th, "STANDARD REDUCTION POTENTIALS", "Half-reactions at 25 °C, 1 M and 1 atm, from the "
                                                          "strongest reducing agent to the strongest oxidizing agent")]
    tx, tw = MX + 90, 760
    out.append(_card(MX, top, W - 2 * MX, H - top - 24, th))
    out.append(text("Half-reaction", tx + 30, top + 40, 15, th["sub"], "Bold", "start"))
    out.append(text("E° (V)", tx + tw - 20, top + 40, 15, th["sub"], "Bold", "end"))
    zero_x = tx + tw + 150
    scale = 44
    for i, (eq, e) in enumerate(POTENTIALS):
        y = top + 60 + i * (rh + 6)
        col = mix("#3D62C4", "#E8573F", (e + 3.04) / 5.91)
        out.append(f'<rect x="{tx}" y="{y}" width="{tw}" height="{rh}" rx="9" fill="{mix(th["card"], col, .14)}"/>')
        out.append(chem(eq, tx + 30, y + rh / 2 + 7, 17, th["ink"], "start"))
        out.append(text(f"{e:+.2f}".replace("-", "−") if e else "0.00", tx + tw - 20, y + rh / 2 + 7, 17, th["ink"], "Bold", "end"))
        bw = e * scale
        x0 = min(zero_x, zero_x + bw)
        out.append(f'<rect x="{x0:.1f}" y="{y + 8}" width="{max(abs(bw), 3):.1f}" height="{rh - 16}" rx="5" '
                   f'fill="{col}"/>')
    yb = top + 60 + n * (rh + 6)
    out.append(f'<path d="M{zero_x} {top + 52}V{yb}" stroke="{th["sub"]}" stroke-width="2"/>')
    # panah samping
    ax = MX + 45
    out.append(f'<path d="M{ax} {top + 74}V{yb - 20}" stroke="#3D62C4" stroke-width="5" stroke-linecap="round"/>'
               f'<path d="M{ax} {top + 60}l-9 16h18z" fill="#3D62C4"/>')
    out.append(f'<path d="M{ax + 12} {top + 74}V{yb - 20}" stroke="#E8573F" stroke-width="5" stroke-linecap="round"/>'
               f'<path d="M{ax + 12} {yb - 6}l-9 -16h18z" fill="#E8573F"/>')
    out.append(fit_text("↑ Stronger reducing agent (metal is oxidized more easily)", tx, yb + 40, 15,
                        "#3D62C4" if th["bg"] == "#FFFFFF" else "#7FA0F0", W - 2 * MX - 120, "SemiBold", "start"))
    out.append(fit_text("↓ Stronger oxidizing agent (species is reduced more easily)", tx, yb + 68, 15,
                        "#E8573F" if th["bg"] == "#FFFFFF" else "#F28C78", W - 2 * MX - 120, "SemiBold", "start"))
    return W, H, "".join(out)


POSTERS = [
    ("ghs-hazard-symbols", ghs, "GHS hazard symbols chart, chemical warning pictograms with meanings",
     ["ghs", "hazard symbols", "hazard pictograms", "warning signs", "chemical safety", "flammable", "corrosive",
      "toxic", "explosive", "oxidizing", "health hazard", "environmental hazard", "lab safety", "safety labels"]),
    ("standard-reduction-potentials", potentials, "Standard reduction potentials table chart for electrochemistry",
     ["standard reduction potential", "electrode potential", "electrochemistry", "redox", "half reaction",
      "oxidizing agent", "reducing agent", "electrochemical series", "volts", "galvanic cell", "voltaic cell",
      "hydrogen electrode", "table", "reference"]),
]

TR.update({
    "GHS HAZARD SYMBOLS": "SIMBOL BAHAYA GHS",
    "Learn the warning pictograms found on chemical labels": "Kenali piktogram peringatan pada label bahan kimia",
    "Explosive": "Mudah meledak", "Flammable": "Mudah terbakar", "Oxidizing": "Pengoksidasi",
    "Gas under pressure": "Gas bertekanan", "Corrosive": "Korosif", "Acute toxicity": "Beracun (toksik akut)",
    "Irritant / harmful": "Iritan / berbahaya", "Health hazard": "Bahaya kesehatan",
    "Environmental hazard": "Berbahaya bagi lingkungan",
    "Explosives and self-reactive substances": "Bahan peledak dan zat yang reaktif sendiri",
    "Flammable gases, liquids and solids": "Gas, cairan, dan padatan yang mudah menyala",
    "Can cause or intensify a fire": "Dapat menyebabkan atau memperbesar kebakaran",
    "Compressed, liquefied or dissolved gas": "Gas yang dimampatkan, dicairkan, atau dilarutkan",
    "Burns skin, damages eyes, corrodes metal": "Membakar kulit, merusak mata, mengikis logam",
    "Toxic or fatal if swallowed, inhaled or touched": "Beracun atau mematikan bila tertelan, terhirup, atau tersentuh",
    "Irritates skin and eyes, harmful": "Mengiritasi kulit dan mata, berbahaya",
    "Can cause cancer or damage organs": "Dapat menyebabkan kanker atau merusak organ",
    "Toxic to aquatic life": "Beracun bagi kehidupan akuatik",
    "Fireworks, TNT": "Kembang api, TNT", "Ethanol, acetone, petrol": "Etanol, aseton, bensin",
    "Oxygen tank, CO₂ cylinder": "Tabung oksigen, tabung CO₂", "Sulfuric acid, NaOH": "Asam sulfat, NaOH",
    "Methanol, cyanide": "Metanol, sianida", "Citric acid, CaCl₂": "Asam sitrat, CaCl₂",
    "Benzene, formaldehyde": "Benzena, formaldehida", "Copper sulfate, pesticides": "Tembaga sulfat, pestisida",
    "GHS = Globally Harmonized System of Classification and Labelling of Chemicals":
        "GHS = Sistem Harmonisasi Global Klasifikasi dan Pelabelan Bahan Kimia",
    "STANDARD REDUCTION POTENTIALS": "POTENSIAL REDUKSI STANDAR",
    "Half-reactions at 25 °C, 1 M and 1 atm, from the strongest reducing agent to the strongest oxidizing agent":
        "Setengah reaksi pada 25 °C, 1 M, dan 1 atm, dari reduktor terkuat hingga oksidator terkuat",
    "Half-reaction": "Setengah reaksi",
    "↑ Stronger reducing agent (metal is oxidized more easily)": "↑ Reduktor makin kuat (logam makin mudah teroksidasi)",
    "↓ Stronger oxidizing agent (species is reduced more easily)": "↓ Oksidator makin kuat (zat makin mudah tereduksi)",
})
