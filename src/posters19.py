"""Poster edukasi kimia jilid 19: deret keaktifan logam (deret Volta) dan waktu paruh.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters3 import arrow_line, mix
from posters4 import chem

SERIES = ["Li", "K", "Ba", "Ca", "Na", "Mg", "Al", "Mn", "Zn", "Cr", "Fe", "Cd", "Co", "Ni", "Sn", "Pb", "H", "Sb",
          "Bi", "Cu", "Hg", "Ag", "Pt", "Au"]


def reactivity(th):
    W = 1226
    top = 122
    H = top + 250 + 24 + 2 * (150 + 16) + 10
    out = [header(W, th, "METAL REACTIVITY SERIES", "Metals ordered from most to least reactive (the Volta series)")]
    out.append(_card(MX, top, W - 2 * MX, 250, th))
    n = len(SERIES)
    gap = 5
    tw = (W - 2 * MX - 40 - (n - 1) * gap) / n
    for i, sym in enumerate(SERIES):
        x = MX + 20 + i * (tw + gap)
        col = "#8A97A8" if sym == "H" else mix(R, "#3D62C4", i / (n - 1))
        if sym == "Au":
            col = "#D9A520"
        out.append(f'<rect x="{x:.1f}" y="{top + 40}" width="{tw:.1f}" height="96" rx="9" fill="{col}"/>')
        out.append(text(sym, x + tw / 2, top + 96, 18 if len(sym) == 2 else 21, "#FFFFFF"))
    y = top + 170
    out.append(arrow_line(W / 2 - 40, y, MX + 30, y, R, 4))
    out.append(arrow_line(W / 2 + 40, y, W - MX - 30, y, "#3D62C4" if th["bg"] == "#FFFFFF" else "#6F8FE0", 4))
    out.append(fit_text("More reactive · easily oxidized · strong reducing agent", MX + 30, y + 40, 15, th["ink"],
                        W / 2 - MX - 50, "SemiBold", anchor="start"))
    out.append(fit_text("Less reactive · hard to oxidize · noble metals", W - MX - 30, y + 40, 15, th["ink"],
                        W / 2 - MX - 50, "SemiBold", anchor="end"))
    rules = [
        ("A metal displaces any metal to its right from a solution of its salt", T,
         [("Zn(s) + CuSO_{4}(aq) → ZnSO_{4}(aq) + Cu(s)", True), ("Cu(s) + ZnSO_{4}(aq) → no reaction", False)]),
        ("Metals to the left of H react with dilute acids and release hydrogen gas", O,
         [("Mg(s) + 2HCl(aq) → MgCl_{2}(aq) + H_{2}(g)", True), ("Ag(s) + HCl(aq) → no reaction", False)]),
    ]
    for k, (rule, col, eqs) in enumerate(rules):
        y = top + 274 + k * (150 + 16)
        out.append(_card(MX, y, W - 2 * MX, 150, th))
        out.append(f'<rect x="{MX}" y="{y}" width="10" height="150" rx="5" fill="{col}"/>')
        out.append(fit_text(rule, MX + 34, y + 42, 19, th["ink"], W - 2 * MX - 60, anchor="start"))
        for j, (eq, ok) in enumerate(eqs):
            bx = MX + 34 + j * ((W - 2 * MX - 68) / 2 + 0)
            bw = (W - 2 * MX - 68) / 2 - 10
            out.append(f'<rect x="{bx:.1f}" y="{y + 66}" width="{bw:.1f}" height="60" rx="10" fill="{th["plate"]}"/>')
            mark = "#4BB04A" if ok else R
            out.append(f'<circle cx="{bx + 30:.1f}" cy="{y + 96}" r="14" fill="{mark}"/>')
            if ok:
                out.append(f'<path d="M{bx + 23:.1f} {y + 96}l5 5l9 -10" fill="none" stroke="#FFFFFF" '
                           'stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>')
            else:
                out.append(f'<path d="M{bx + 25:.1f} {y + 91}l10 10M{bx + 35:.1f} {y + 91}l-10 10" stroke="#FFFFFF" '
                           'stroke-width="3.2" stroke-linecap="round"/>')
            out.append(chem(tr(eq), bx + 56, y + 103, 17, "#1E2A3A", "start"))
    return W, H, "".join(out)


ISOTOPES = [("Radon-222", "3.8 days", P), ("Iodine-131", "8 days", O), ("Cobalt-60", "5.3 years", T),
            ("Carbon-14", "5,730 years", R), ("Uranium-238", "4.5 billion years", "#3D62C4")]


def half_life(th):
    W = 1226
    top = 122
    ch = 470
    H = top + ch + 24 + 120
    out = [header(W, th, "HALF-LIFE", "The time it takes for half of the radioactive nuclei in a sample to decay")]
    lw = 760
    out.append(_card(MX, top, lw, ch, th))
    gx0, gy0 = MX + 90, top + 400
    gw, gh = lw - 140, 320
    acc = th["accent"]
    out.append(f'<path d="M{gx0} {gy0 - gh - 10}V{gy0}H{gx0 + gw + 10}" fill="none" stroke="{th["sub"]}" '
               'stroke-width="2.4" stroke-linecap="round"/>')
    step = gw / 5
    for k in range(6):
        x = gx0 + k * step
        out.append(text(str(k), x, gy0 + 26, 14, th["sub"], "SemiBold"))
        if k:
            frac = .5 ** k
            out.append(f'<path d="M{x:.1f} {gy0}V{gy0 - gh * frac:.1f}H{gx0}" fill="none" stroke="{th["card_stroke"]}" '
                       'stroke-width="1.6" stroke-dasharray="5 5"/>')
    for k, lab in enumerate(("100%", "50%", "25%", "12.5%")):
        out.append(text(lab, gx0 - 12, gy0 - gh * .5 ** k + 5, 13, th["sub"], "SemiBold", "end"))
    d = "M" + " L".join(f"{gx0 + t / 40 * gw:.1f} {gy0 - gh * .5 ** (t / 40 * 5):.1f}" for t in range(41))
    out.append(f'<path d="{d}" fill="none" stroke="{acc}" stroke-width="5" stroke-linecap="round" '
               'stroke-linejoin="round"/>')
    for k in range(5):
        out.append(f'<circle cx="{gx0 + k * step:.1f}" cy="{gy0 - gh * .5 ** k:.1f}" r="8" fill="{acc}" '
                   f'stroke="{th["card"]}" stroke-width="3"/>')
    out.append(text("Number of half-lives", gx0 + gw / 2, gy0 + 54, 15, th["ink"], "SemiBold"))
    out.append(text("Remaining", gx0 + 4, top + 44, 15, th["ink"], "SemiBold", "start"))
    rx = MX + lw + 24
    rw = W - MX - rx
    out.append(_card(rx, top, rw, ch, th))
    out.append(text("Examples", rx + rw / 2, top + 44, 19, th["ink"]))
    for i, (iso, t, col) in enumerate(ISOTOPES):
        y = top + 70 + i * 78
        out.append(f'<rect x="{rx + 20}" y="{y}" width="{rw - 40}" height="66" rx="12" '
                   f'fill="{mix(th["card"], col, .16)}"/>')
        out.append(f'<rect x="{rx + 20}" y="{y}" width="8" height="66" rx="4" fill="{col}"/>')
        out.append(fit_text(iso, rx + 44, y + 28, 17, th["ink"], rw - 80, anchor="start"))
        out.append(fit_text(t, rx + 44, y + 52, 15, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .35),
                            rw - 80, "SemiBold", anchor="start"))
    y = top + ch + 24
    out.append(_card(MX, y, W - 2 * MX, 96, th))
    out.append(chem("N = N_{0} × (1/2)^{t / T}", W / 2 - 160, y + 58, 28, acc, "middle"))
    out.append(fit_text("N₀ = starting amount · t = time · T = half-life", W / 2 + 230, y + 56, 15, th["sub"], 420,
                        "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("metal-reactivity-series", reactivity, "Metal reactivity series chart, Volta series with displacement reactions",
     ["reactivity series", "activity series", "volta series", "metals", "displacement reaction", "redox",
      "electrochemistry", "zinc", "copper", "magnesium", "noble metals", "gold", "hydrogen", "single replacement"]),
    ("half-life", half_life, "Radioactive half-life chart with decay curve and isotope examples",
     ["half-life", "radioactive decay", "radioactivity", "decay curve", "isotope", "carbon-14", "carbon dating",
      "uranium", "iodine-131", "nuclear chemistry", "exponential decay", "radon", "cobalt-60", "nucleus"]),
]

TR.update({
    "METAL REACTIVITY SERIES": "DERET VOLTA (KEREAKTIFAN LOGAM)",
    "Metals ordered from most to least reactive (the Volta series)":
        "Logam diurutkan dari yang paling reaktif hingga paling tidak reaktif",
    "More reactive · easily oxidized · strong reducing agent": "Makin reaktif · mudah teroksidasi · reduktor kuat",
    "Less reactive · hard to oxidize · noble metals": "Kurang reaktif · sukar teroksidasi · logam mulia",
    "A metal displaces any metal to its right from a solution of its salt":
        "Logam dapat mendesak logam di sebelah kanannya dari larutan garamnya",
    "Metals to the left of H react with dilute acids and release hydrogen gas":
        "Logam di sebelah kiri H bereaksi dengan asam encer menghasilkan gas hidrogen",
    "Cu(s) + ZnSO_{4}(aq) → no reaction": "Cu(s) + ZnSO_{4}(aq) → tidak bereaksi",
    "Ag(s) + HCl(aq) → no reaction": "Ag(s) + HCl(aq) → tidak bereaksi",
    "HALF-LIFE": "WAKTU PARUH",
    "The time it takes for half of the radioactive nuclei in a sample to decay":
        "Waktu yang diperlukan agar separuh inti radioaktif dalam sampel meluruh",
    "Number of half-lives": "Jumlah waktu paruh", "Remaining": "Sisa zat", "Examples": "Contoh",
    "Radon-222": "Radon-222", "Iodine-131": "Iodin-131", "Cobalt-60": "Kobalt-60", "Carbon-14": "Karbon-14",
    "Uranium-238": "Uranium-238", "3.8 days": "3,8 hari", "8 days": "8 hari", "5.3 years": "5,3 tahun",
    "5,730 years": "5.730 tahun", "4.5 billion years": "4,5 miliar tahun",
    "N₀ = starting amount · t = time · T = half-life": "N₀ = jumlah awal · t = waktu · T = waktu paruh",
    "12.5%": "12,5%",
})
