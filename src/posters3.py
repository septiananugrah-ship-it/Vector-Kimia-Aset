"""Poster edukasi kimia jilid 3: tren periodik, konfigurasi elektron (Aufbau),
indikator asam-basa, teknik pemisahan campuran, dan hukum gas.

Didaftarkan ke posters.py lewat POSTERS (2 tema x 2 bahasa).
"""
import math

import icons_lab2
import icons_lab_flat
import poster_kit
from icons_lab_flat import M, N, O, P, R, T, W, Y, solid, vessel
from periodic import ELEMENTS, position
from poster_i18n import TR
from poster_kit import MX, fit_text, header, icon_at, particle, text, tr
from posters2 import _card
from render import style_attrs
from textpath import formula, width
from textpath import text as raw_text


def mix(a, b, f):
    ca = [int(a[i:i + 2], 16) for i in (1, 3, 5)]
    cb = [int(b[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * f):02X}" for x, y in zip(ca, cb))


def arrow_line(x1, y1, x2, y2, col, w=3):
    ang = math.atan2(y2 - y1, x2 - x1)
    hx, hy = x2 - 11 * math.cos(ang), y2 - 11 * math.sin(ang)
    px, py = 6 * math.sin(ang), -6 * math.cos(ang)
    return (f'<path d="M{x1:.1f} {y1:.1f}L{hx:.1f} {hy:.1f}" stroke="{col}" stroke-width="{w}" '
            'stroke-linecap="round" fill="none"/>'
            f'<path d="M{x2:.1f} {y2:.1f}L{hx + px:.1f} {hy + py:.1f}L{hx - px:.1f} {hy - py:.1f}z" fill="{col}"/>')


# ------------------------------------------------------------ tren periodik

TRENDS = [
    ("Atomic radius", "radius", "#F28C28", "left", "down"),
    ("Ionization energy", "ie", "#E85D4A", "right", "up"),
    ("Electronegativity", "en", "#8E6CC9", "right", "up"),
    ("Metallic character", "metal", "#3FB6C4", "left", "down"),
]


def periodic_trends(th):
    W = 1226
    pw = (W - 2 * MX - 30) / 2
    tile = (pw - 60) / 18
    top = 122
    ph = 7 * tile + 104
    H = top + 2 * (ph + 22) + 20
    out = [header(W, th, "PERIODIC TABLE TRENDS",
                  "How atomic radius, ionization energy, electronegativity and metallic character change")]
    for k, (name, key, col, hdir, vdir) in enumerate(TRENDS):
        px = MX + (k % 2) * (pw + 30)
        py = top + (k // 2) * (ph + 22)
        out.append(_card(px, py, pw, ph, th))
        out.append(text(name, px + 22, py + 34, 19, th["ink"], "Bold", "start"))
        gx, gy = px + 40, py + 56
        light_c = mix(th["card"], col, .12)
        for z, (sym, _n, _m, cat) in enumerate(ELEMENTS, start=1):
            c, r = position(z)
            if r > 6:
                continue
            if key in ("radius", "metal"):
                s = (r / 6) * .55 + (1 - c / 17) * .45
            else:
                s = (1 - r / 6) * .5 + (c / 17) * .5
            fill = mix(light_c, col, s)
            if key == "en" and cat == "ng":
                fill = mix(th["card"], "#9AA5B1", .35)
            x, y = gx + c * tile, gy + r * tile
            out.append(f'<rect x="{x + .8:.2f}" y="{y + .8:.2f}" width="{tile - 1.6:.2f}" height="{tile - 1.6:.2f}" '
                       f'rx="2.5" fill="{fill}"/>')
            if tile > 22:
                out.append(raw_text(sym, x + tile / 2, y + tile / 2 + 4, 10, "#1E2A3A" if s < .55 else "#FFFFFF",
                                    "SemiBold"))
        # panah arah kenaikan
        ay = gy + 7 * tile + 18
        xa, xb = gx, gx + 18 * tile
        if hdir == "left":
            xa, xb = xb, xa
        out.append(arrow_line(xa, ay, xb, ay, col))
        lab = tr("increases across a period")
        out.append(raw_text(lab, (gx + gx + 18 * tile) / 2, ay + 22, 11.5, th["sub"], "SemiBold"))
        vx = gx - 18
        ya, yb = gy, gy + 7 * tile
        if vdir == "up":
            ya, yb = yb, ya
        out.append(arrow_line(vx, ya, vx, yb, col))
        out.append(f'<g transform="translate({vx - 10} {gy + 3.5 * tile}) rotate(-90)">'
                   + raw_text(tr("down a group") if vdir == "down" else tr("up a group"), 0, 0, 10.5, th["sub"],
                              "SemiBold") + "</g>")
    return W, H, "".join(out)


# ------------------------------------------------------------ konfigurasi elektron

def sup_text(s, x, y, size, fill, anchor="start", weight="SemiBold"):
    """Teks dengan superskrip: angka setelah huruf s/p/d/f dinaikkan (mis. 2p6)."""
    runs, prev_orb = [], False
    for ch in s:
        is_sup = ch.isdigit() and prev_orb
        runs.append((ch, size * (.62 if is_sup else 1), -size * .42 if is_sup else 0))
        if ch in "spdf":
            prev_orb = True
        elif not ch.isdigit():
            prev_orb = False
    total = sum(width(c, sz, weight) for c, sz, _ in runs)
    cx = x - (total / 2 if anchor == "middle" else 0)
    out = []
    for c, sz, dy in runs:
        out.append(raw_text(c, cx, y + dy, sz, fill, weight, "start"))
        cx += width(c, sz, weight)
    return "".join(out)


SUB_COL = {"s": "#3FB6C4", "p": "#F28C28", "d": "#8E6CC9", "f": "#E85D4A"}
ORDER = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p", "7s", "5f",
         "6d", "7p"]


def electron_config(th):
    W, H = 1226, 760
    top = 122
    out = [header(W, th, "ELECTRON CONFIGURATION",
                  "The Aufbau principle: the order in which electrons fill atomic subshells")]
    # diagram diagonal
    lw, lh = 500, H - top - 40
    out.append(_card(MX, top, lw, lh, th))
    out.append(text("Diagonal rule", MX + 22, top + 36, 19, th["ink"], "Bold", "start"))
    cell, x0, y0 = 92, MX + 70, top + 78
    pos = {}
    for n in range(1, 8):
        for li, l in enumerate("spdf"):
            if li >= n or (n >= 6 and li >= 9 - n):
                continue
            name = f"{n}{l}"
            cx, cy = x0 + li * cell + 30, y0 + (n - 1) * 72 + 26
            pos[name] = (cx, cy)
    for k in range(1, 9):  # garis diagonal n + l = konstan
        chain = [s for s in ORDER if int(s[0]) + "spdf".index(s[1]) == k]
        if not chain:
            continue
        pts = [pos[s] for s in chain]
        # panah mengikuti urutan pengisian: dari kanan atas ke kiri bawah
        (xa, ya), (xb, yb) = pts[0], pts[-1]
        dx, dy = xb - xa, yb - ya
        d = math.hypot(dx, dy) or 1
        ux, uy = (dx / d, dy / d) if len(pts) > 1 else (-.79, .62)
        out.append(arrow_line(xa - ux * 30, ya - uy * 30, xb + ux * 34, yb + uy * 34, mix(th["card"], th["sub"], .55), 2.4))
    for name, (cx, cy) in pos.items():
        col = SUB_COL[name[1]]
        out.append(f'<circle cx="{cx}" cy="{cy}" r="23" fill="{col}"/>'
                   + raw_text(name, cx, cy + 6, 17, "#FFFFFF", "Bold"))
    # urutan pengisian
    rx = MX + lw + 24
    rw = W - MX - rx
    out.append(_card(rx, top, rw, 236, th))
    out.append(text("Filling order", rx + 22, top + 36, 19, th["ink"], "Bold", "start"))
    x, y = rx + 22, top + 74
    for i, s in enumerate(ORDER):
        w = 46
        if x + w > rx + rw - 16:
            x, y = rx + 22, y + 46
        out.append(f'<rect x="{x}" y="{y - 22}" width="{w}" height="32" rx="16" fill="{SUB_COL[s[1]]}"/>'
                   + raw_text(s, x + w / 2, y, 15, "#FFFFFF", "Bold"))
        x += w + 8
        if i < len(ORDER) - 1 and x + 10 < rx + rw - 16:
            out.append(raw_text("›", x - 1, y, 15, th["sub"], "Bold"))
            x += 8
    # kapasitas subkulit
    cy_ = top + 254
    out.append(_card(rx, cy_, rw, 108, th))
    out.append(text("Maximum electrons per subshell", rx + 22, cy_ + 34, 16, th["ink"], "Bold", "start"))
    for i, (l, n) in enumerate((("s", 2), ("p", 6), ("d", 10), ("f", 14))):
        bx = rx + 22 + i * (rw - 44) / 4
        out.append(f'<rect x="{bx}" y="{cy_ + 52}" width="{(rw - 44) / 4 - 12:.1f}" height="38" rx="10" '
                   f'fill="{SUB_COL[l]}"/>' + raw_text(f"{l} = {n}", bx + ((rw - 44) / 4 - 12) / 2, cy_ + 77, 17,
                                                      "#FFFFFF", "Bold"))
    # contoh
    ey = cy_ + 126
    out.append(_card(rx, ey, rw, H - 40 - ey, th))
    out.append(text("Examples", rx + 22, ey + 34, 16, th["ink"], "Bold", "start"))
    for i, (el, z, conf) in enumerate((("Oxygen (O)", 8, "1s2 2s2 2p4"), ("Sodium (Na)", 11, "1s2 2s2 2p6 3s1"),
                                       ("Iron (Fe)", 26, "1s2 2s2 2p6 3s2 3p6 4s2 3d6"))):
        yy = ey + 74 + i * 52
        nm, sym = el.split(" (")
        out.append(raw_text(f"{tr(nm)} ({sym}  Z = {z}", rx + 22, yy, 13, th["sub"], "SemiBold", "start"))
        out.append(sup_text(conf, rx + 22, yy + 24, 17, th["accent"], weight="Bold"))
    return W, H, "".join(out)


# ------------------------------------------------------------ indikator asam-basa

PH_COLORS = ["#D7262B", "#E9452A", "#F27A24", "#F7A823", "#F5C922", "#C9D52A", "#8DC63F", "#4BB04A", "#2DA36B",
             "#1E9C9A", "#2384C6", "#3062AE", "#4B4A9E", "#5E3B8F", "#4A2A73"]
INDICATORS = [
    ("Methyl orange", "#E2412E", "#F6C523", 3.1, 4.4, "red → yellow"),
    ("Methyl red", "#D9303B", "#F4C430", 4.4, 6.2, "red → yellow"),
    ("Litmus", "#D3384A", "#3B5FC0", 4.5, 8.3, "red → blue"),
    ("Bromothymol blue", "#F2D33C", "#2E5FB8", 6.0, 7.6, "yellow → blue"),
    ("Phenolphthalein", "#F4F5F7", "#E0479E", 8.2, 10.0, "colorless → pink"),
]


def indicators(th):
    W = 1226
    top = 122
    lx = MX + 230
    bw = W - MX - 150 - lx
    step = bw / 28
    rh = 74
    H = top + 60 + (len(INDICATORS) + 1) * rh + 70
    out = [header(W, th, "ACID–BASE INDICATORS", "Color changes of common indicators across the pH scale")]
    # sumbu pH
    for v in range(15):
        x = lx + v * bw / 14
        out.append(raw_text(str(v), x, top + 30, 13, th["sub"], "SemiBold"))
        out.append(f'<path d="M{x:.1f} {top + 38}v8" stroke="{th["sub"]}" stroke-width="1.6"/>')
    out.append(raw_text("pH", lx - 30, top + 30, 13, th["ink"], "Bold"))
    rows = [(tr("Universal indicator"), None, None, None, None, "")] + INDICATORS
    for i, (name, ca, cb, a, b, change) in enumerate(rows):
        y = top + 60 + i * rh
        out.append(_card(MX, y, W - 2 * MX, rh - 12, th, rx=12))
        out.append(fit_text(name, MX + 20, y + 30, 16, th["ink"], 200, "Bold", anchor="start"))
        if change:
            out.append(raw_text(tr(change), MX + 20, y + 49, 11, th["sub"], "Regular", "start"))
            rng = f"pH {a} – {b}"
            if poster_kit._lang[0] == "id":
                rng = rng.replace(".", ",")
            out.append(raw_text(rng, W - MX - 20, y + 38, 13, th["accent"], "Bold", "end"))
        for s in range(28):
            v = (s + .5) / 2
            if ca is None:
                col = PH_COLORS[min(14, int(v))]
            else:
                f = 0 if v <= a else 1 if v >= b else (v - a) / (b - a)
                col = mix(ca, cb, f)
            # tiap blok memanjang sampai ujung kanan agar tidak ada celah antarblok
            out.append(f'<rect x="{lx + s * step:.2f}" y="{y + 12}" width="{bw - s * step:.2f}" height="{rh - 36}" '
                       f'fill="{col}"/>')
        out.append(f'<rect x="{lx}" y="{y + 12}" width="{bw:.1f}" height="{rh - 36}" rx="4" fill="none" '
                   f'stroke="{th["card_stroke"]}" stroke-width="1.5"/>')
    ny = top + 60 + len(rows) * rh + 20
    out.append(text("Transition ranges are typical values; exact colors depend on concentration.", W / 2, ny, 11,
                    th["sub"], "Regular"))
    return W, H, "".join(out)


# ------------------------------------------------------------ pemisahan campuran

def _chromatography():
    return (vessel("M16 20v34a5 5 0 0 0 5 5h22a5 5 0 0 0 5-5V20z", (16, 20, 48, 59), 48, T) +
            '<path d="M12 20h40"/><path d="M32 4v6"/>' +
            solid("M26 10h12v42H26z", W, 26, 38) +
            f'<circle cx="32" cy="18" r="2.6" fill="{P}" stroke="none"/><circle cx="32" cy="26" r="2.6" fill="{R}" stroke="none"/>'
            f'<circle cx="32" cy="34" r="2.6" fill="{Y}" stroke="none"/><path d="M28 44h8" stroke="{N}"/>')


def _magnet():
    return (solid("M12 8h12v26a8 8 0 0 0 16 0V8h12v26a20 20 0 0 1-40 0z", R, 12, 52) +
            solid("M12 8h12v8H12z", M, 12, 24) + solid("M40 8h12v8H40z", M, 40, 52) +
            "".join(f'<path d="M{x} {y}l3 -1.5" stroke="{N}" stroke-width="1.6"/>'
                    for x, y in ((10, 62), (20, 60), (30, 63), (40, 61), (50, 62), (16, 56), (46, 57))))


def _decant():
    return ('<g transform="rotate(28 32 32)">' +
            vessel("M18 12v36a5 5 0 0 0 5 5h18a5 5 0 0 0 5-5V12z", (18, 12, 46, 53), 30, T,
                   '<rect x="10" y="46" width="44" height="10" fill="#B5651D"/>') +
            '<path d="M15 12h34"/></g>' +
            f'<path d="M50 22c3 6 4 14 4 30" stroke="{T}" stroke-width="3" fill="none"/>')


SEPARATION = [
    ("Filtration", "insoluble solid from a liquid", "sand and water", "funnel"),
    ("Evaporation to dryness", "dissolved solid from a solution", "salt from seawater", "tripod-burner-beaker"),
    ("Distillation", "liquids with different boiling points", "ethanol and water", "retort"),
    ("Chromatography", "mixtures of dyes or pigments", "ink colors", "_chrom"),
    ("Decantation", "liquid from a settled solid", "muddy water", "_decant"),
    ("Magnetic separation", "magnetic metals from a mixture", "iron filings and sulfur", "_magnet"),
    ("Centrifugation", "solids by spinning at high speed", "blood cells and plasma", "centrifuge"),
    ("Separating funnel", "immiscible liquids", "oil and water", "separatory-funnel"),
]


def separation(th):
    cols, cw, ch, gap = 4, 270, 270, 14
    W = cols * (cw + gap) - gap + 2 * MX
    top = 122
    H = top + 2 * (ch + gap) - gap + 30
    icons = {ic["id"]: (ic["body"], m.STROKE) for m in (icons_lab_flat, icons_lab2) for ic in m.ICONS}
    icons["_chrom"] = (_chromatography().replace("{p}", "chrom"), 1.6)
    icons["_magnet"] = (_magnet().replace("{p}", "mag"), 1.6)
    icons["_decant"] = (_decant().replace("{p}", "dec"), 1.6)
    out = [header(W, th, "SEPARATION TECHNIQUES", "Methods for separating mixtures and what each one separates")]
    for i, (name, what, ex, icon) in enumerate(SEPARATION):
        x = MX + (i % cols) * (cw + gap)
        y = top + (i // cols) * (ch + gap)
        out.append(_card(x, y, cw, ch, th))
        out.append(f'<rect x="{x + 10}" y="{y + 10}" width="{cw - 20}" height="140" rx="10" fill="{th["plate"]}"/>')
        body, stroke = icons[icon]
        out.append(icon_at(body, stroke, x + cw / 2 - 58, y + 22, 116))
        out.append(fit_text(name, x + cw / 2, y + 182, 18, th["ink"], cw - 24))
        out.append(fit_text(f"{tr('Separates')} {tr(what)}", x + cw / 2, y + 206, 11.5, th["sub"], cw - 24,
                            "Regular"))
        out.append(fit_text(f"{tr('Example')}: {tr(ex)}", x + cw / 2, y + 240, 12, th["accent"], cw - 24, "SemiBold"))
    return W, H, "".join(out)


# ------------------------------------------------------------ hukum gas

def _cylinder(x, y, w, h, piston_y, n_part, col, seed, hot=False):
    import random
    rnd = random.Random(seed)
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="#E9F1F7" stroke="#1E2A3A" stroke-width="2"/>',
           f'<rect x="{x + 3}" y="{piston_y - 8}" width="{w - 6}" height="14" rx="3" fill="#9AA5B1" stroke="#1E2A3A" '
           'stroke-width="2"/>',
           f'<rect x="{x + w / 2 - 4}" y="{y - 26}" width="8" height="{piston_y - y + 18}" fill="#C9D1DA" '
           'stroke="#1E2A3A" stroke-width="2"/>']
    placed, tries = [], 0
    while len(placed) < n_part and tries < 5000:
        tries += 1
        px, py = rnd.uniform(x + 10, x + w - 10), rnd.uniform(piston_y + 14, y + h - 9)
        if all(math.hypot(px - a, py - b) > 13 for a, b in placed):
            placed.append((px, py))
    for k, (px, py) in enumerate(placed):
        out.append(particle(px, py, 6, col, f"gl{seed}{k}", shine=False))
    if hot:
        for k in range(3):
            fx = x + w * (k + 1) / 4
            out.append(f'<path d="M{fx} {y + h + 22}c5 -6 6 -10 0 -16c-6 6 -5 10 0 16z" fill="{O}" stroke="#1E2A3A" '
                       'stroke-width="1.4"/>')
    return "".join(out)


def _graph(x, y, w, h, kind, th, xl, yl):
    out = [f'<path d="M{x} {y}V{y + h}H{x + w}" stroke="{th["ink"]}" stroke-width="2" fill="none"/>']
    if kind == "hyper":
        pts = [(x + 10 + t * (w - 20), y + h - 8 - (h - 20) * (.12 / (t + .12))) for t in [i / 20 for i in range(1, 21)]]
    else:
        pts = [(x + 8, y + h - 12), (x + w - 10, y + 12)]
    out.append('<path d="M' + "L".join(f"{a:.1f} {b:.1f}" for a, b in pts) + f'" stroke="{th["accent"]}" '
               'stroke-width="3" fill="none" stroke-linecap="round"/>')
    out.append(raw_text(xl, x + w, y + h + 16, 12, th["sub"], "SemiBold", "end"))
    out.append(raw_text(yl, x - 8, y + 4, 12, th["sub"], "SemiBold", "end"))
    return "".join(out)


def gas_laws(th):
    W = 1226
    top = 122
    cw = (W - 2 * MX - 2 * 18) / 3
    ch = 470
    H = top + ch + 18 + 110 + 30
    out = [header(W, th, "THE GAS LAWS", "How pressure, volume and temperature of a gas are related")]
    laws = [
        ("Boyle's law", "P1V1 = P2V2", "Constant temperature: pressure up, volume down", "hyper", "V", "P"),
        ("Charles's law", "V1/T1 = V2/T2", "Constant pressure: temperature up, volume up", "line", "T", "V"),
        ("Gay-Lussac's law", "P1/T1 = P2/T2", "Constant volume: temperature up, pressure up", "line", "T", "P"),
    ]
    for k, (name, eq, desc, kind, xl, yl) in enumerate(laws):
        x = MX + k * (cw + 18)
        out.append(_card(x, top, cw, ch, th))
        out.append(text(name, x + cw / 2, top + 38, 21, th["ink"]))
        out.append(formula(eq, x + cw / 2, top + 70, 20, th["accent"], "Bold"))
        out.append(f'<rect x="{x + 12}" y="{top + 88}" width="{cw - 24}" height="190" rx="10" fill="{th["plate"]}"/>')
        g = []
        c1, c2 = x + cw / 2 - 80, x + cw / 2 + 30
        if k == 0:
            g.append(_cylinder(c1, top + 130, 60, 120, top + 150, 8, T, 1))
            g.append(_cylinder(c2, top + 130, 60, 120, top + 200, 8, T, 2))
        elif k == 1:
            g.append(_cylinder(c1, top + 130, 60, 120, top + 200, 6, O, 3))
            g.append(_cylinder(c2, top + 130, 60, 120, top + 150, 6, R, 4, hot=True))
        else:
            g.append(_cylinder(c1, top + 130, 60, 120, top + 165, 7, O, 5))
            g.append(_cylinder(c2, top + 130, 60, 120, top + 165, 7, R, 6, hot=True))
        g.append(arrow_line(c1 + 66, top + 200, c2 - 6, top + 200, "#1E2A3A", 2.4))
        out.append(f'<g {style_attrs(1.4)}>' + "".join(g) + "</g>")
        out.append(_graph(x + 70, top + 300, cw - 120, 100, kind, th, xl, yl))
        out.append(fit_text(desc, x + cw / 2, top + ch - 26, 12, th["sub"], cw - 30, "Regular"))
    by = top + ch + 18
    out.append(_card(MX, by, W - 2 * MX, 110, th))
    out.append(text("Ideal gas law", MX + 30, by + 46, 21, th["ink"], "Bold", "start"))
    out.append(formula("PV = nRT", MX + 30, by + 82, 26, th["accent"], "Bold", "start"))
    out.append(text("P = pressure · V = volume · n = moles of gas · T = temperature (K)", MX + 300, by + 48, 13,
                    th["sub"], "SemiBold", "start"))
    out.append(text("R = 8.314 J/(mol·K), the ideal gas constant", MX + 300, by + 76, 13, th["sub"], "SemiBold",
                    "start"))
    return W, H, "".join(out)


POSTERS = [
    ("periodic-trends", periodic_trends, "Periodic table trends chart, atomic radius, ionization energy, "
     "electronegativity and metallic character",
     ["periodic trends", "periodic table", "atomic radius", "ionization energy", "electronegativity",
      "metallic character", "group", "period", "elements", "trend", "arrows", "atom", "physics", "properties"]),
    ("electron-configuration", electron_config, "Electron configuration Aufbau principle diagram with filling order",
     ["electron configuration", "aufbau principle", "diagonal rule", "orbitals", "subshell", "s p d f", "electrons",
      "energy levels", "quantum", "atom", "madelung rule", "atomic structure", "physics", "orbital"]),
    ("acid-base-indicators", indicators, "Acid base indicators color chart across the pH scale",
     ["indicator", "acid base indicator", "ph", "phenolphthalein", "litmus", "methyl orange", "bromothymol blue",
      "methyl red", "universal indicator", "titration", "color change", "acid", "base", "ph scale"]),
    ("separation-techniques", separation, "Separation techniques of mixtures chart, filtration, distillation, "
     "chromatography and more",
     ["separation", "mixtures", "filtration", "evaporation", "distillation", "chromatography", "decantation",
      "magnet", "centrifugation", "separating funnel", "purification", "methods", "techniques", "mixture"]),
    ("gas-laws", gas_laws, "Gas laws chart, Boyle, Charles, Gay-Lussac and ideal gas law",
     ["gas laws", "boyle's law", "charles's law", "gay-lussac", "ideal gas law", "pressure", "volume",
      "temperature", "pv=nrt", "gas", "piston", "physics", "thermodynamics", "particles"]),
]

TR.update({
    "PERIODIC TABLE TRENDS": "TREN SIFAT PERIODIK",
    "How atomic radius, ionization energy, electronegativity and metallic character change":
        "Perubahan jari-jari atom, energi ionisasi, keelektronegatifan, dan sifat logam",
    "Atomic radius": "Jari-jari atom", "Ionization energy": "Energi ionisasi",
    "Electronegativity": "Keelektronegatifan", "Metallic character": "Sifat logam",
    "increases across a period": "makin besar ke arah panah dalam satu periode",
    "down a group": "makin besar ke bawah dalam golongan", "up a group": "makin besar ke atas dalam golongan",
    "ELECTRON CONFIGURATION": "KONFIGURASI ELEKTRON",
    "The Aufbau principle: the order in which electrons fill atomic subshells":
        "Prinsip Aufbau: urutan elektron mengisi subkulit atom",
    "Diagonal rule": "Aturan diagonal", "Filling order": "Urutan pengisian",
    "Maximum electrons per subshell": "Jumlah elektron maksimum tiap subkulit", "Examples": "Contoh",
    "Sodium": "Natrium", "Iron": "Besi",
    "ACID–BASE INDICATORS": "INDIKATOR ASAM–BASA",
    "Color changes of common indicators across the pH scale": "Perubahan warna indikator umum pada skala pH",
    "Universal indicator": "Indikator universal", "Methyl orange": "Metil jingga", "Methyl red": "Metil merah",
    "Litmus": "Lakmus", "Bromothymol blue": "Bromtimol biru", "Phenolphthalein": "Fenolftalein",
    "red → yellow": "merah → kuning", "red → blue": "merah → biru", "yellow → blue": "kuning → biru",
    "colorless → pink": "tak berwarna → merah muda",
    "Transition ranges are typical values; exact colors depend on concentration.":
        "Trayek perubahan adalah nilai umum; warna sebenarnya bergantung pada konsentrasi.",
    "SEPARATION TECHNIQUES": "TEKNIK PEMISAHAN CAMPURAN",
    "Methods for separating mixtures and what each one separates": "Metode pemisahan campuran dan kegunaannya",
    "Filtration": "Filtrasi (penyaringan)", "Evaporation to dryness": "Penguapan", "Distillation": "Distilasi (penyulingan)",
    "Chromatography": "Kromatografi", "Decantation": "Dekantasi", "Magnetic separation": "Pemisahan magnetik",
    "Centrifugation": "Sentrifugasi", "Separating funnel": "Corong pisah", "Separates": "Memisahkan",
    "insoluble solid from a liquid": "padatan tak larut dari cairan",
    "dissolved solid from a solution": "zat terlarut dari larutannya",
    "liquids with different boiling points": "cairan dengan titik didih berbeda",
    "mixtures of dyes or pigments": "campuran zat warna atau pigmen",
    "liquid from a settled solid": "cairan dari endapan", "magnetic metals from a mixture": "logam magnetik dari campuran",
    "solids by spinning at high speed": "padatan dengan putaran cepat", "immiscible liquids": "cairan yang tidak bercampur",
    "sand and water": "pasir dan air", "salt from seawater": "garam dari air laut", "ethanol and water": "etanol dan air",
    "ink colors": "warna tinta", "muddy water": "air berlumpur", "iron filings and sulfur": "serbuk besi dan belerang",
    "blood cells and plasma": "sel darah dan plasma", "oil and water": "minyak dan air",
    "THE GAS LAWS": "HUKUM-HUKUM GAS",
    "How pressure, volume and temperature of a gas are related": "Hubungan tekanan, volume, dan suhu gas",
    "Boyle's law": "Hukum Boyle", "Charles's law": "Hukum Charles", "Gay-Lussac's law": "Hukum Gay-Lussac",
    "Constant temperature: pressure up, volume down": "Suhu tetap: tekanan naik, volume turun",
    "Constant pressure: temperature up, volume up": "Tekanan tetap: suhu naik, volume naik",
    "Constant volume: temperature up, pressure up": "Volume tetap: suhu naik, tekanan naik",
    "Ideal gas law": "Persamaan gas ideal",
    "P = pressure · V = volume · n = moles of gas · T = temperature (K)":
        "P = tekanan · V = volume · n = mol gas · T = suhu (K)",
    "R = 8.314 J/(mol·K), the ideal gas constant": "R = 8,314 J/(mol·K), tetapan gas ideal",
})
