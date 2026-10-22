"""Poster edukasi kimia jilid 40: katalis & enzim serta kromatografi kertas (nilai Rf).
Didaftarkan ke posters.py lewat POSTERS (semua tema x 2 bahasa).
"""
from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters3 import arrow_line, mix
from posters4 import chem
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


def catalysts(th):
    W = 1226
    top = 122
    H = top + 420 + 20 + 250 + 30
    out = [header(W, th, "CATALYSTS AND ENZYMES", "A catalyst speeds up a reaction without being used up")]
    out.append(_card(MX, top, 660, 420, th))
    gx, gy, gw, gh = MX + 80, top + 360, 540, 270
    out.append(f'<path d="M{gx} {gy - gh}V{gy}H{gx + gw}" fill="none" stroke="{th["sub"]}" stroke-width="2.4"/>')
    out.append(text("Energy", gx - 14, gy - gh - 10, 14, th["ink"], "SemiBold", "start"))
    out.append(text("Reaction progress", gx + gw / 2, gy + 30, 14, th["ink"], "SemiBold"))
    r_y, p_y = gy - 120, gy - 40
    out.append(f'<path d="M{gx + 20} {r_y}H{gx + 120}C{gx + 210} {r_y} {gx + 220} {gy - 250} {gx + 270} {gy - 250}'
               f'C{gx + 320} {gy - 250} {gx + 330} {p_y} {gx + 420} {p_y}H{gx + 520}" fill="none" stroke="{R}" '
               'stroke-width="5" stroke-linecap="round"/>')
    out.append(f'<path d="M{gx + 120} {r_y}C{gx + 200} {r_y} {gx + 220} {gy - 175} {gx + 270} {gy - 175}'
               f'C{gx + 320} {gy - 175} {gx + 340} {p_y} {gx + 420} {p_y}" fill="none" stroke="#3FB6C4" '
               'stroke-width="5" stroke-dasharray="12 7" stroke-linecap="round"/>')
    out.append(arrow_line(gx + 270, r_y, gx + 270, gy - 254, R, 3))
    out.append(arrow_line(gx + 240, r_y, gx + 240, gy - 166, "#3FB6C4", 3))
    out.append(f'<path d="M{gx + 230} {r_y}H{gx + 280}" stroke="{th["sub"]}" stroke-width="2" stroke-dasharray="4 4"/>')
    out.append(text("Ea", gx + 280, gy - 205, 16, R, "Bold", "start"))
    out.append(text("Ea", gx + 232, gy - 132, 16, "#3FB6C4", "Bold", "end"))
    out.append(text("Reactants", gx + 70, r_y - 12, 14, th["ink"], "SemiBold"))
    out.append(text("Products", gx + 470, p_y - 12, 14, th["ink"], "SemiBold"))
    out.append(f'<path d="M{gx + 330} {gy - gh + 10}h34" stroke="{R}" stroke-width="5"/>'
               + text("Without catalyst", gx + 372, gy - gh + 15, 13, th["ink"], "SemiBold", "start"))
    out.append(f'<path d="M{gx + 330} {gy - gh + 34}h34" stroke="#3FB6C4" stroke-width="5" stroke-dasharray="10 6"/>'
               + text("With catalyst", gx + 372, gy - gh + 39, 13, th["ink"], "SemiBold", "start"))
    rx = MX + 680
    rw = W - MX - rx
    out.append(_card(rx, top, rw, 420, th))
    out.append(text("Enzymes: biological catalysts", rx + rw / 2, top + 40, 17, th["ink"]))
    ex, ey = rx + rw / 2, top + 160
    out.append(f'<path d="M{ex - 110} {ey + 60}V{ey - 20}Q{ex - 110} {ey - 60} {ex - 60} {ey - 60}H{ex - 34}V{ey - 18}'
               f'H{ex + 34}V{ey - 60}H{ex + 60}Q{ex + 110} {ey - 60} {ex + 110} {ey - 20}V{ey + 60}Z" fill="{P}" '
               f'stroke="{INK}" stroke-width="3" stroke-linejoin="round"/>')
    out.append(f'<rect x="{ex - 30}" y="{ey - 104}" width="60" height="70" rx="10" fill="#F2C94C" stroke="{INK}" '
               'stroke-width="3"/>')
    out.append(text("Substrate", ex + 46, ey - 74, 14, th["ink"], "SemiBold", "start"))
    out.append(text("Enzyme", ex, ey + 30, 16, "#FFFFFF"))
    out.append(text("Active site", ex - 46, ey - 26, 13, th["ink"], "SemiBold", "end"))
    for j, ln in enumerate(_wrap("Lock and key: the substrate fits the active site like a key in a lock", 14, rw - 50)):
        out.append(text(ln, rx + rw / 2, top + 268 + j * 20, 14, th["sub"], "SemiBold"))
    for j, ln in enumerate(_wrap("Enzymes work best at an optimum temperature (about 37 °C in the body) and pH", 14,
                                 rw - 50)):
        out.append(text(ln, rx + rw / 2, top + 330 + j * 20, 14, th["sub"], "SemiBold"))
    y = top + 440
    out.append(_card(MX, y, W - 2 * MX, 250, th))
    out.append(text("Catalysts in action", W / 2, y + 40, 18, th["ink"]))
    items = [("Iron (Fe)", "Haber process: making ammonia", T), ("V_{2}O_{5}", "Contact process: sulfuric acid", O),
             ("Pt, Pd, Rh", "Catalytic converters in cars", "#7C8B9C"), ("Amylase", "Digests starch into sugar", P),
             ("Yeast enzymes", "Fermentation: bread and ethanol", R)]
    iw = (W - 2 * MX - 40 - 4 * 12) / 5
    for k, (cat, use, col) in enumerate(items):
        ix = MX + 20 + k * (iw + 12)
        out.append(f'<rect x="{ix:.1f}" y="{y + 62}" width="{iw:.1f}" height="160" rx="14" '
                   f'fill="{mix(th["card"], col, .18)}"/>')
        out.append(chem(tr(cat), ix + iw / 2, y + 112, 20, th["ink"], "middle"))
        for j, ln in enumerate(_wrap(use, 13.5, iw - 20)):
            out.append(text(ln, ix + iw / 2, y + 152 + j * 19, 13.5, th["sub"], "SemiBold"))
    return W, H, "".join(out)


def chromatography(th):
    W = 1226
    top = 122
    H = top + 470 + 20 + 200 + 30
    out = [header(W, th, "PAPER CHROMATOGRAPHY", "Separating the dyes in an ink and identifying them with Rf values")]
    out.append(_card(MX, top, 640, 470, th))
    px, py, pw, ph = MX + 90, top + 40, 340, 360
    out.append(f'<rect x="{px - 40}" y="{py + ph - 70}" width="{pw + 80}" height="90" rx="8" fill="#BFE3F5" '
               f'stroke="{INK}" stroke-width="3"/>')
    out.append(f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" fill="#FFFFFF" stroke="{INK}" stroke-width="2.5"/>')
    base, front = py + ph - 40, py + 60
    out.append(f'<path d="M{px} {base}H{px + pw}" stroke="#7C8B9C" stroke-width="2" stroke-dasharray="6 5"/>')
    out.append(f'<path d="M{px} {front}H{px + pw}" stroke="#3D7DDB" stroke-width="2" stroke-dasharray="6 5"/>')
    samples = [("A", [("#E8573F", .62), ("#F2C94C", .35)]), ("B", [("#3D62C4", .78)]),
               ("C", [("#E8573F", .62), ("#F2C94C", .35), ("#3D62C4", .78), ("#4BB04A", .18)]), ("D", [("#F2C94C", .35)])]
    for k, (lab, spots) in enumerate(samples):
        sx = px + 46 + k * 82
        out.append(f'<circle cx="{sx}" cy="{base}" r="5" fill="{INK}"/>')
        out.append(text(lab, sx, base + 26, 14, INK, "Bold"))
        for col, rf in spots:
            sy = base - (base - front) * rf
            out.append(f'<ellipse cx="{sx}" cy="{sy:.1f}" rx="13" ry="10" fill="{col}"/>')
    out.append(text("Solvent front", px + pw + 8, front + 5, 13, "#3D7DDB", "Bold", "start"))
    out.append(text("Baseline (pencil)", px + pw + 48, base + 5, 13, th["sub"], "Bold", "start"))
    out.append(text("Solvent", px + pw / 2, py + ph + 46, 13, th["sub"], "Bold"))
    rx = MX + 660
    rw = W - MX - rx
    out.append(_card(rx, top, rw, 470, th))
    out.append(text("Rf value", rx + rw / 2, top + 44, 18, th["ink"]))
    out.append(f'<rect x="{rx + 24}" y="{top + 64}" width="{rw - 48}" height="110" rx="14" fill="{th["plate"]}"/>')
    fx = rx + rw / 2 + 30
    out.append(text("Rf =", fx - 150, top + 128, 26, INK, "Bold", "start"))
    out.append(fit_text("distance moved by spot", fx + 30, top + 108, 16, INK, 240))
    out.append(f'<path d="M{fx - 90} {top + 120}H{fx + 150}" stroke="{INK}" stroke-width="2.4"/>')
    out.append(fit_text("distance moved by solvent", fx + 30, top + 148, 16, INK, 240))
    notes = ["Rf is always between 0 and 1", "Same substance, same solvent → same Rf",
             "Sample C contains the dyes of A and B, plus one more", "Draw the baseline in pencil: ink would dissolve"]
    for k, n_ in enumerate(notes):
        y = top + 200 + k * 64
        out.append(f'<rect x="{rx + 24}" y="{y}" width="{rw - 48}" height="54" rx="12" '
                   f'fill="{mix(th["card"], th["accent"], .14)}"/>')
        out.append(fit_text(n_, rx + rw / 2, y + 33, 15, th["ink"], rw - 70, "SemiBold"))
    y = top + 490
    out.append(_card(MX, y, W - 2 * MX, 200, th))
    out.append(text("Example calculation", W / 2, y + 40, 18, th["ink"]))
    out.append(fit_text("Red spot moved 6.2 cm, solvent front moved 10 cm", W / 2, y + 88, 17, th["ink"],
                        W - 2 * MX - 60, "SemiBold"))
    out.append(f'<rect x="{W / 2 - 160}" y="{y + 112}" width="320" height="56" rx="28" fill="{th["accent"]}"/>')
    out.append(text("Rf = 6.2 ÷ 10 = 0.62" if tr("Example calculation") == "Example calculation" else
                    "Rf = 6,2 ÷ 10 = 0,62", W / 2, y + 148, 22, "#FFFFFF"))
    return W, H, "".join(out)


POSTERS = [
    ("catalysts-enzymes", catalysts, "Catalysts and enzymes chart, activation energy diagram and lock and key model",
     ["catalyst", "enzyme", "activation energy", "energy diagram", "lock and key", "active site", "reaction rate",
      "haber process", "catalytic converter", "biochemistry", "kinetics", "amylase", "fermentation", "substrate"]),
    ("paper-chromatography", chromatography, "Paper chromatography chart, separating dyes and calculating Rf values",
     ["chromatography", "paper chromatography", "rf value", "separation", "dyes", "ink", "solvent front",
      "baseline", "mixtures", "analysis", "experiment", "calculation", "pigments", "lab technique"]),
]

TR.update({
    "CATALYSTS AND ENZYMES": "KATALIS DAN ENZIM",
    "A catalyst speeds up a reaction without being used up": "Katalis mempercepat reaksi tanpa ikut habis bereaksi",
    "Energy": "Energi", "Reaction progress": "Jalannya reaksi", "Ea (catalyst)": "Ea (dengan katalis)",
    "Reactants": "Pereaksi", "Products": "Hasil reaksi", "Without catalyst": "Tanpa katalis",
    "With catalyst": "Dengan katalis", "Enzymes: biological catalysts": "Enzim: katalis biologis",
    "Substrate": "Substrat", "Enzyme": "Enzim", "Active site": "Sisi aktif",
    "Lock and key: the substrate fits the active site like a key in a lock":
        "Model kunci-gembok: substrat pas dengan sisi aktif seperti kunci pada gembok",
    "Enzymes work best at an optimum temperature (about 37 °C in the body) and pH":
        "Enzim bekerja optimal pada suhu (sekitar 37 °C dalam tubuh) dan pH tertentu",
    "Catalysts in action": "Contoh penggunaan katalis", "Iron (Fe)": "Besi (Fe)",
    "Haber process: making ammonia": "Proses Haber: pembuatan amonia",
    "Contact process: sulfuric acid": "Proses kontak: asam sulfat",
    "Catalytic converters in cars": "Konverter katalitik mobil", "Amylase": "Amilase",
    "Digests starch into sugar": "Mencerna amilum menjadi gula", "Yeast enzymes": "Enzim ragi",
    "Fermentation: bread and ethanol": "Fermentasi: roti dan etanol",
    "PAPER CHROMATOGRAPHY": "KROMATOGRAFI KERTAS",
    "Separating the dyes in an ink and identifying them with Rf values":
        "Memisahkan zat warna dalam tinta dan mengenalinya dengan nilai Rf",
    "Solvent front": "Batas pelarut", "Baseline (pencil)": "Garis awal (pensil)", "Solvent": "Pelarut",
    "Rf value": "Nilai Rf", "distance moved by spot": "jarak tempuh noda", "distance moved by solvent": "jarak tempuh pelarut",
    "Rf is always between 0 and 1": "Nilai Rf selalu antara 0 dan 1",
    "Same substance, same solvent → same Rf": "Zat sama, pelarut sama → Rf sama",
    "Sample C contains the dyes of A and B, plus one more": "Sampel C mengandung zat warna A dan B, ditambah satu lagi",
    "Draw the baseline in pencil: ink would dissolve": "Garis awal dibuat dengan pensil karena tinta akan ikut larut",
    "Example calculation": "Contoh perhitungan",
    "Red spot moved 6.2 cm, solvent front moved 10 cm": "Noda merah bergerak 6,2 cm, batas pelarut bergerak 10 cm",
})
