"""Poster edukasi kimia jilid 6: jenis-jenis koloid dan daya tembus radiasi
alfa, beta, gamma. Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
import math
import random

from icons_lab_flat import R
from poster_i18n import TR
from poster_kit import MX, fit_text, header, particle, text, tr
from posters2 import _card
from posters3 import arrow_line, mix
from render import style_attrs

PHASE = {"gas": ("#E6F4FB", "#FFFFFF"), "liquid": ("#4F9BD9", "#2F6FB0"), "solid": ("#D9B48A", "#8A5A2E")}


def _phase_box(x, y, s, medium, dispersed, seed):
    """Kotak medium pendispersi berisi partikel fase terdispersi."""
    rnd = random.Random(seed)
    bg = PHASE[medium][0]
    out = [f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="12" fill="{bg}" stroke="#1E2A3A" stroke-width="2"/>']
    placed, tries = [], 0
    while len(placed) < 11 and tries < 3000:
        tries += 1
        px, py = rnd.uniform(x + 14, x + s - 14), rnd.uniform(y + 14, y + s - 14)
        if all(abs(px - a) + abs(py - b) > 26 for a, b in placed):
            placed.append((px, py))
    for k, (px, py) in enumerate(placed):
        r = rnd.uniform(5, 8)
        if dispersed == "gas":
            out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r:.1f}" fill="#FFFFFF" stroke="#1E2A3A" stroke-width="1.6"/>')
        elif dispersed == "liquid":
            out.append(particle(px, py, r, "#2F6FB0" if medium != "liquid" else "#F2C14E", f"cl{seed}{k}", shine=False))
        else:
            out.append(f'<rect x="{px - r:.1f}" y="{py - r:.1f}" width="{2 * r:.1f}" height="{2 * r:.1f}" rx="2" '
                       f'fill="{PHASE["solid"][1]}" stroke="#1E2A3A" stroke-width="1.6"/>')
    return "".join(out)


COLLOIDS = [
    ("Foam", "gas", "liquid", "whipped cream, soap suds"),
    ("Solid foam", "gas", "solid", "marshmallow, pumice stone"),
    ("Liquid aerosol", "liquid", "gas", "fog, clouds, hair spray"),
    ("Emulsion", "liquid", "liquid", "milk, mayonnaise"),
    ("Gel", "liquid", "solid", "jelly, cheese, butter"),
    ("Solid aerosol", "solid", "gas", "smoke, dust in air"),
    ("Sol", "solid", "liquid", "paint, ink, blood"),
    ("Solid sol", "solid", "solid", "colored glass, gemstones"),
]


def colloids(th):
    cols, cw, ch, gap = 4, 270, 300, 14
    W = cols * (cw + gap) - gap + 2 * MX
    top = 122
    H = top + 2 * (ch + gap) - gap + 50
    out = [header(W, th, "TYPES OF COLLOIDS",
                  "Colloids classified by dispersed phase and dispersion medium, with everyday examples")]
    g = []
    for i, (name, disp, med, ex) in enumerate(COLLOIDS):
        x = MX + (i % cols) * (cw + gap)
        y = top + (i // cols) * (ch + gap)
        out.append(_card(x, y, cw, ch, th))
        s = 130
        g.append(_phase_box(x + cw / 2 - s / 2, y + 20, s, med, disp, i))
        out.append(text(name, x + cw / 2, y + 186, 20, th["ink"]))
        out.append(fit_text(f"{tr(disp.capitalize())} {tr('in')} {tr(med)}", x + cw / 2, y + 212, 13.5,
                            th["accent"], cw - 24, "SemiBold"))
        out.append(fit_text(f"{tr('Example')}: {tr(ex)}", x + cw / 2, y + 268, 12, th["sub"], cw - 24, "Regular"))
        out.append(fit_text(f"{tr('dispersed phase')}: {tr(disp)} · {tr('medium')}: {tr(med)}", x + cw / 2, y + 238,
                            10.5, th["sub"], cw - 24, "Regular"))
    out.append(f'<g {style_attrs(1.4)}>' + "".join(g) + "</g>")
    out.append(text("Particle size of colloids: about 1–1000 nm", W / 2, H - 20, 12, th["sub"], "SemiBold"))
    return W, H, "".join(out)


def radiation(th):
    W = 1226
    top = 122
    out = [header(W, th, "PENETRATING POWER OF RADIATION",
                  "How far alpha, beta and gamma radiation travel through different materials")]
    out.append(f'<rect x="{MX}" y="{top}" width="{W - 2 * MX}" height="380" rx="16" fill="{th["plate"]}"/>')
    ink = "#1E2A3A"
    sx = MX + 90
    barriers = [("Paper", "#F4EFE2", 470, 14), ("Aluminium", "#C9D1DA", 690, 26), ("Lead", "#6B7684", 910, 60)]
    rays = [("α", "Alpha", R, 470), ("β", "Beta", "#3D7DDB", 690), ("γ", "Gamma", "#8E6CC9", 910 + 60 + 40)]
    g = [f'<circle cx="{sx}" cy="{top + 190}" r="54" fill="#FFC845" stroke="{ink}" stroke-width="2.4"/>']
    for k in range(3):
        a1 = -90 + k * 120
        g.append(f'<path d="M{sx} {top + 190}L{sx + 40 * math.cos(math.radians(a1 - 30)):.1f} '
                 f'{top + 190 + 40 * math.sin(math.radians(a1 - 30)):.1f}'
                 f'A40 40 0 0 1 {sx + 40 * math.cos(math.radians(a1 + 30)):.1f} '
                 f'{top + 190 + 40 * math.sin(math.radians(a1 + 30)):.1f}z" fill="{ink}"/>')
    g.append(f'<circle cx="{sx}" cy="{top + 190}" r="8" fill="#FFC845" stroke="{ink}" stroke-width="2"/>')
    for name, col, x, w in barriers:
        g.append(f'<rect x="{x}" y="{top + 40}" width="{w}" height="300" rx="4" fill="{col}" stroke="{ink}" '
                 'stroke-width="2"/>')
    def wave(x, end, y, col, w):
        path = f"M{x} {y}"
        k = 0
        while x < end - 12:
            x2 = min(x + 24, end - 12)
            path += f"Q{(x + x2) / 2:.1f} {y - 12 if k % 2 else y + 12} {x2:.1f} {y}"
            x, k = x2, k + 1
        return f'<path d="{path}" stroke="{col}" stroke-width="{w}" fill="none" stroke-linecap="round"/>'

    for i, (sym, name, col, stop) in enumerate(rays):
        y = top + 110 + i * 80
        if i < 2:
            end = stop - 6
            g.append(wave(sx + 64, end, y, col, 3.4))
            g.append(arrow_line(end - 14, y, end, y, col, 3.4))
        else:  # gamma melemah setelah menembus timbal
            lead_end = 910 + 60
            g.append(wave(sx + 64, lead_end + 12, y, col, 3.4))
            end = W - MX - 50
            g.append(wave(lead_end, end, y, mix(col, "#FFFFFF", .45), 1.8))
            g.append(arrow_line(end - 14, y, end, y, mix(col, "#FFFFFF", .45), 1.8))
        g.append(f'<circle cx="{sx + 120}" cy="{y - 24}" r="15" fill="{col}"/>'
                 + text(sym, sx + 120, y - 18, 17, "#FFFFFF"))
    out.append(f'<g {style_attrs(1.4)}>' + "".join(g) + "</g>")
    for name, col, x, w in barriers:
        out.append(text(name, x + w / 2, top + 368, 14, ink, "Bold"))
    ty = top + 404
    descs = [("Alpha (α)", "Stopped by a sheet of paper", R),
             ("Beta (β)", "Stopped by a few millimetres of aluminium", "#3D7DDB"),
             ("Gamma (γ)", "Reduced by thick lead or concrete", "#8E6CC9")]
    cw = (W - 2 * MX - 2 * 16) / 3
    for k, (n, d, col) in enumerate(descs):
        x = MX + k * (cw + 16)
        out.append(_card(x, ty, cw, 92, th))
        out.append(f'<rect x="{x}" y="{ty}" width="8" height="92" rx="4" fill="{col}"/>')
        out.append(text(n, x + 24, ty + 38, 18, th["ink"], "Bold", "start"))
        out.append(fit_text(d, x + 24, ty + 66, 12.5, th["sub"], cw - 40, "SemiBold", anchor="start"))
    return W, ty + 92 + 30, "".join(out)


POSTERS = [
    ("colloids", colloids, "Types of colloids chart, foam, emulsion, aerosol, gel and sol with examples",
     ["colloid", "colloids", "emulsion", "foam", "aerosol", "gel", "sol", "dispersed phase", "dispersion medium",
      "mixture", "milk", "mayonnaise", "fog", "smoke"]),
    ("radiation-penetration", radiation, "Penetrating power of alpha, beta and gamma radiation diagram",
     ["radiation", "alpha", "beta", "gamma", "radioactivity", "nuclear", "penetration", "shielding", "lead",
      "aluminium", "paper", "radioactive", "physics", "ionizing radiation"]),
]

TR.update({
    "TYPES OF COLLOIDS": "JENIS-JENIS KOLOID",
    "Colloids classified by dispersed phase and dispersion medium, with everyday examples":
        "Penggolongan koloid berdasarkan fase terdispersi dan medium pendispersi, beserta contohnya",
    "Foam": "Buih", "Solid foam": "Busa padat", "Liquid aerosol": "Aerosol cair", "Emulsion": "Emulsi",
    "Gel": "Gel (emulsi padat)", "Solid aerosol": "Aerosol padat", "Sol": "Sol", "Solid sol": "Sol padat",
    "Gas": "Gas", "Liquid": "Cair", "Solid": "Padat", "in": "dalam", "gas": "gas", "liquid": "cair",
    "solid": "padat", "dispersed phase": "fase terdispersi", "medium": "medium",
    "whipped cream, soap suds": "krim kocok, busa sabun", "marshmallow, pumice stone": "marshmallow, batu apung",
    "fog, clouds, hair spray": "kabut, awan, hair spray", "milk, mayonnaise": "susu, mayones",
    "jelly, cheese, butter": "agar-agar, keju, mentega", "smoke, dust in air": "asap, debu di udara",
    "paint, ink, blood": "cat, tinta, darah", "colored glass, gemstones": "kaca berwarna, batu permata",
    "Particle size of colloids: about 1–1000 nm": "Ukuran partikel koloid: sekitar 1–1000 nm",
    "PENETRATING POWER OF RADIATION": "DAYA TEMBUS RADIASI",
    "How far alpha, beta and gamma radiation travel through different materials":
        "Seberapa jauh radiasi alfa, beta, dan gamma menembus berbagai bahan",
    "Paper": "Kertas", "Aluminium": "Aluminium", "Lead": "Timbal",
    "Alpha (α)": "Alfa (α)", "Beta (β)": "Beta (β)", "Gamma (γ)": "Gamma (γ)",
    "Stopped by a sheet of paper": "Tertahan oleh selembar kertas",
    "Stopped by a few millimetres of aluminium": "Tertahan oleh aluminium setebal beberapa milimeter",
    "Reduced by thick lead or concrete": "Berkurang oleh timbal atau beton yang tebal",
})
