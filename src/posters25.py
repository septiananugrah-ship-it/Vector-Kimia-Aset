"""Poster edukasi kimia jilid 25: perkaratan besi dan hujan asam.
Didaftarkan ke posters.py lewat POSTERS (semua tema x 2 bahasa).
"""
from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters3 import mix
from posters4 import chem
from textpath import width

RUST = "#B5562B"


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


def _tube(cx, top, h, liquid, oil, nail_rust, dry, ink):
    """Tabung reaksi berisi paku besi; liquid = tinggi air (0-1), oil = lapisan minyak, dry = CaCl2 di dasar."""
    w = 64
    x0 = cx - w / 2
    out = []
    body = f"M{x0} {top}V{top + h - w / 2}a{w / 2} {w / 2} 0 0 0 {w} 0V{top}"
    if liquid:
        ly = top + h * (1 - liquid)
        out.append(f'<clipPath id="tb{cx:.0f}"><path d="{body}Z"/></clipPath>'
                   f'<g clip-path="url(#tb{cx:.0f})"><rect x="{x0}" y="{ly:.1f}" width="{w}" height="{h}" '
                   f'fill="#9FD3EC"/>' + (f'<rect x="{x0}" y="{ly - 14:.1f}" width="{w}" height="14" fill="#F2C94C"/>'
                                          if oil else "") + '</g>')
    if dry:
        out.append(f'<clipPath id="tb{cx:.0f}"><path d="{body}Z"/></clipPath>'
                   f'<g clip-path="url(#tb{cx:.0f})"><rect x="{x0}" y="{top + h - 46}" width="{w}" height="60" '
                   f'fill="#F4F5F7"/></g>')
        for k in range(7):
            out.append(f'<circle cx="{x0 + 12 + (k % 4) * 13}" cy="{top + h - 30 + (k // 4) * 12}" r="4" '
                       f'fill="#C9D3DE"/>')
    # paku besi
    nail = "#8C96A3"
    ny0, ny1 = top + 30, top + h - (60 if dry else 22)
    out.append(f'<rect x="{cx - 4}" y="{ny0}" width="8" height="{ny1 - ny0}" rx="2" fill="{nail}"/>'
               f'<rect x="{cx - 12}" y="{ny0 - 6}" width="24" height="7" rx="2" fill="{nail}"/>'
               f'<path d="M{cx - 4} {ny1}L{cx} {ny1 + 12}L{cx + 4} {ny1}Z" fill="{nail}"/>')
    if nail_rust:
        for k in range(8):
            out.append(f'<circle cx="{cx + (-3 if k % 2 else 3)}" cy="{ny0 + 20 + k * (ny1 - ny0 - 30) / 7:.1f}" '
                       f'r="4.5" fill="{RUST}"/>')
    out.append(f'<path d="{body}" fill="none" stroke="{ink}" stroke-width="4" stroke-linejoin="round"/>')
    out.append(f'<rect x="{x0 - 8}" y="{top - 14}" width="{w + 16}" height="16" rx="5" fill="#C99A6B" '
               f'stroke="{ink}" stroke-width="3"/>' if (oil or dry) else "")
    return "".join(out)


def rusting(th):
    W = 1226
    top = 122
    H = top + 470 + 20 + 250 + 30
    out = [header(W, th, "RUSTING OF IRON", "Iron rusts only when both water and oxygen are present")]
    out.append(_card(MX, top, W - 2 * MX, 470, th))
    cw = (W - 2 * MX) / 3
    tests = [("Water + air", "Rusts", True, (.45, False, False)),
             ("Boiled water + oil layer (no air)", "No rust", False, (.8, True, False)),
             ("Dry air (calcium chloride)", "No rust", False, (0, False, True))]
    for k, (cond, res, rusty, (liq, oil, dry)) in enumerate(tests):
        cx = MX + cw * k + cw / 2
        out.append(f'<rect x="{cx - 120}" y="{top + 24}" width="240" height="300" rx="16" fill="{th["plate"]}"/>')
        out.append(_tube(cx, top + 60, 240, liq, oil, rusty, dry, "#1E2A3A"))
        col = RUST if rusty else "#4BB04A"
        out.append(f'<rect x="{cx - 70}" y="{top + 344}" width="140" height="38" rx="19" fill="{col}"/>')
        out.append(text(res, cx, top + 370, 17, "#FFFFFF"))
        for j, ln in enumerate(_wrap(cond, 15, cw - 40)):
            out.append(text(ln, cx, top + 412 + j * 21, 15, th["ink"], "SemiBold"))
    y = top + 490
    out.append(_card(MX, y, W - 2 * MX, 250, th))
    out.append(chem("4Fe + 3O_{2} + 2xH_{2}O → 2Fe_{2}O_{3}·xH_{2}O  (rust)", W / 2, y + 44, 22, th["accent"],
                    "middle") if tr("Example") == "Example" else
               chem("4Fe + 3O_{2} + 2xH_{2}O → 2Fe_{2}O_{3}·xH_{2}O  (karat)", W / 2, y + 44, 22, th["accent"],
                    "middle"))
    out.append(text("How to prevent rusting", W / 2, y + 84, 17, th["ink"]))
    ways = [("Painting", T), ("Oiling / greasing", O), ("Galvanizing (zinc coat)", "#7C8B9C"),
            ("Tin plating", "#5B9BD5"), ("Sacrificial metal (Mg)", P), ("Stainless steel alloy", R)]
    bw = (W - 2 * MX - 40 - 2 * 14) / 3
    for k, (way, col) in enumerate(ways):
        bx = MX + 20 + (k % 3) * (bw + 14)
        by = y + 104 + (k // 3) * 64
        out.append(f'<rect x="{bx:.1f}" y="{by}" width="{bw:.1f}" height="52" rx="12" '
                   f'fill="{mix(th["card"], col, .18)}"/>')
        out.append(f'<circle cx="{bx + 28:.1f}" cy="{by + 26}" r="11" fill="{col}"/>')
        out.append(fit_text(way, bx + 50, by + 32, 16, th["ink"], bw - 64, "SemiBold", "start"))
    return W, H, "".join(out)


def _scene(x, y, w, h, th):
    """Ilustrasi pabrik, mobil, awan, dan hujan asam."""
    ink = "#1E2A3A"
    out = [f'<clipPath id="scene"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16"/></clipPath>'
           f'<g clip-path="url(#scene)">',
           f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#DCEEF8"/>',
           f'<rect x="{x}" y="{y + h - 50}" width="{w}" height="50" fill="#9CCB76"/>',
           f'<path d="M{x} {y + h - 50}H{x + w}" stroke="{ink}" stroke-width="3"/>']
    # pabrik
    fx, fy = x + 40, y + h - 50
    out.append(f'<path d="M{fx} {fy}V{fy - 80}L{fx + 50} {fy - 110}V{fy - 80}L{fx + 100} {fy - 110}V{fy - 80}H{fx + 160}'
               f'V{fy}Z" fill="#B8C2CC" stroke="{ink}" stroke-width="3" stroke-linejoin="round"/>')
    out.append(f'<rect x="{fx + 120}" y="{fy - 150}" width="26" height="70" fill="#8C96A3" stroke="{ink}" '
               'stroke-width="3"/>')
    for k in range(4):
        out.append(f'<circle cx="{fx + 140 + k * 30}" cy="{fy - 162 - k * 10}" r="{12 + k * 4}" fill="#7C8B9C"/>')
    out.append(text("SO₂", fx + 270, fy - 196, 20, ink, "Bold", "start"))
    # mobil
    cx, cy = x + 360, y + h - 50
    out.append(f'<path d="M{cx} {cy - 12}V{cy - 40}Q{cx} {cy - 50} {cx + 12} {cy - 50}H{cx + 34}L{cx + 54} {cy - 74}'
               f'H{cx + 104}L{cx + 128} {cy - 50}H{cx + 150}Q{cx + 160} {cy - 50} {cx + 160} {cy - 40}V{cy - 12}Z" '
               f'fill="#E8573F" stroke="{ink}" stroke-width="3" stroke-linejoin="round"/>')
    for wx in (cx + 36, cx + 124):
        out.append(f'<circle cx="{wx}" cy="{cy - 10}" r="14" fill="{ink}"/><circle cx="{wx}" cy="{cy - 10}" r="5" '
                   'fill="#B8C2CC"/>')
    for k in range(3):
        out.append(f'<circle cx="{cx - 14 - k * 18}" cy="{cy - 22 - k * 6}" r="{8 + k * 3}" fill="#9AA5B1"/>')
    out.append(text("NOₓ", cx - 60, cy - 50, 20, ink, "Bold", "end"))
    # awan + hujan
    ax, ay = x + w - 190, y + 70
    out.append(f'<path d="M{ax - 90} {ay + 30}a34 34 0 0 1 20-62a48 48 0 0 1 90-12a40 40 0 0 1 70 30a30 30 0 0 1 0 '
               f'44Z" fill="#7C8B9C" stroke="{ink}" stroke-width="3" stroke-linejoin="round"/>')
    for k in range(10):
        rx = ax - 80 + (k % 5) * 38
        ry = ay + 52 + (k // 5) * 50 + (k % 2) * 16
        out.append(f'<path d="M{rx} {ry}l-8 22" stroke="#3D7DDB" stroke-width="4" stroke-linecap="round"/>')
    # pohon layu + danau
    tx, ty = x + w - 120, y + h - 50
    out.append(f'<path d="M{tx} {ty}V{ty - 70}M{tx} {ty - 40}l-18 -18M{tx} {ty - 52}l16 -16" stroke="#8B5A2B" '
               'stroke-width="6" stroke-linecap="round"/>')
    out.append(f'<ellipse cx="{x + w - 260}" cy="{ty + 22}" rx="70" ry="14" fill="#5B9BD5" stroke="{ink}" '
               'stroke-width="3"/>')
    out.append(text("pH < 5.6" if tr("Example") == "Example" else "pH < 5,6", ax - 150, ay + 40, 22, "#E8573F",
                    "Bold", "end"))
    out.append('</g>')
    return "".join(out)


def acid_rain(th):
    W = 1226
    top = 122
    H = top + 320 + 20 + 330 + 20 + 120 + 30
    out = [header(W, th, "ACID RAIN", "Gases from burning fuels dissolve in rainwater and make it acidic")]
    out.append(_card(MX, top, W - 2 * MX, 320, th))
    out.append(_scene(MX + 20, top + 20, W - 2 * MX - 40, 280, th))
    y = top + 340
    cw = (W - 2 * MX - 20) / 2
    out.append(_card(MX, y, cw, 330, th))
    out.append(text("How it forms", MX + cw / 2, y + 40, 19, th["ink"]))
    eqs = ["S + O_{2} → SO_{2}", "2SO_{2} + O_{2} → 2SO_{3}", "SO_{3} + H_{2}O → H_{2}SO_{4}",
           "4NO_{2} + O_{2} + 2H_{2}O → 4HNO_{3}"]
    for k, e in enumerate(eqs):
        ey = y + 66 + k * 62
        out.append(f'<rect x="{MX + 22}" y="{ey}" width="{cw - 44}" height="50" rx="12" fill="{th["plate"]}"/>')
        out.append(chem(e, MX + cw / 2, ey + 33, 19, "#1E2A3A", "middle"))
    x2 = MX + cw + 20
    out.append(_card(x2, y, cw, 330, th))
    out.append(text("Effects", x2 + cw / 2, y + 40, 19, th["ink"]))
    effects = [("Damages forests and soil", "#8B5A2B"), ("Acidifies lakes, harms fish", "#3D7DDB"),
               ("Corrodes buildings and statues", "#7C8B9C"), ("Speeds up rusting of metals", RUST)]
    for k, (e, col) in enumerate(effects):
        ey = y + 66 + k * 62
        out.append(f'<rect x="{x2 + 22}" y="{ey}" width="{cw - 44}" height="50" rx="12" '
                   f'fill="{mix(th["card"], col, .2)}"/>')
        out.append(f'<circle cx="{x2 + 50}" cy="{ey + 25}" r="10" fill="{col}"/>')
        out.append(fit_text(e, x2 + 72, ey + 31, 16, th["ink"], cw - 110, "SemiBold", "start"))
    y += 350
    out.append(_card(MX, y, W - 2 * MX, 120, th))
    out.append(text("Solutions", W / 2, y + 38, 18, th["ink"]))
    sols = ["Scrubbers in power plants", "Catalytic converters in cars", "Renewable energy", "Liming acidic lakes"]
    sw = (W - 2 * MX - 40 - 3 * 12) / 4
    for k, sname in enumerate(sols):
        sx = MX + 20 + k * (sw + 12)
        out.append(f'<rect x="{sx:.1f}" y="{y + 56}" width="{sw:.1f}" height="44" rx="22" '
                   f'fill="{mix(th["card"], "#4BB04A", .22)}"/>')
        out.append(fit_text(sname, sx + sw / 2, y + 84, 15, th["ink"], sw - 20, "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("rusting-of-iron", rusting, "Rusting of iron chart, test tube experiment and ways to prevent corrosion",
     ["rusting", "rust", "corrosion", "iron", "oxidation", "galvanizing", "prevent rust", "experiment", "test tube",
      "nail", "oxygen", "water", "redox", "metal"]),
    ("acid-rain", acid_rain, "Acid rain chart, causes, chemical reactions, effects and solutions",
     ["acid rain", "pollution", "sulfur dioxide", "nitrogen oxides", "environment", "air pollution",
      "environmental chemistry", "factory", "emissions", "sulfuric acid", "nitric acid", "ph", "climate", "ecology"]),
]

TR.update({
    "RUSTING OF IRON": "PERKARATAN BESI",
    "Iron rusts only when both water and oxygen are present": "Besi berkarat hanya jika ada air dan oksigen sekaligus",
    "Water + air": "Air + udara", "Boiled water + oil layer (no air)": "Air mendidih + lapisan minyak (tanpa udara)",
    "Dry air (calcium chloride)": "Udara kering (kalsium klorida)", "Rusts": "Berkarat", "No rust": "Tidak berkarat",
    "How to prevent rusting": "Cara mencegah perkaratan", "Painting": "Dicat", "Oiling / greasing": "Dilumuri oli / gemuk",
    "Galvanizing (zinc coat)": "Galvanisasi (lapisan seng)", "Tin plating": "Pelapisan timah",
    "Sacrificial metal (Mg)": "Logam pelindung (Mg)", "Stainless steel alloy": "Paduan baja tahan karat",
    "ACID RAIN": "HUJAN ASAM",
    "Gases from burning fuels dissolve in rainwater and make it acidic":
        "Gas hasil pembakaran bahan bakar larut dalam air hujan dan membuatnya asam",
    "How it forms": "Proses terbentuknya", "Effects": "Dampak",
    "Damages forests and soil": "Merusak hutan dan tanah", "Acidifies lakes, harms fish": "Mengasamkan danau, membahayakan ikan",
    "Corrodes buildings and statues": "Mengikis bangunan dan patung",
    "Speeds up rusting of metals": "Mempercepat perkaratan logam", "Solutions": "Solusi",
    "Scrubbers in power plants": "Scrubber di pembangkit listrik", "Catalytic converters in cars": "Konverter katalitik mobil",
    "Renewable energy": "Energi terbarukan", "Liming acidic lakes": "Pengapuran danau asam",
})
