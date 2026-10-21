"""Poster edukasi kimia jilid 15: hidrolisis garam dan larutan penyangga.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters3 import mix
from posters4 import chem

SALTS = [
    ("Strong acid + strong base", "NaCl", "Neutral", "pH = 7", "#4BB04A", "no hydrolysis"),
    ("Strong acid + weak base", "NH_{4}Cl", "Acidic", "pH < 7", R, "the cation hydrolyzes"),
    ("Weak acid + strong base", "CH_{3}COONa", "Basic", "pH > 7", "#3D62C4", "the anion hydrolyzes"),
    ("Weak acid + weak base", "CH_{3}COONH_{4}", "Depends on Ka and Kb", "pH ≈ 7", P, "both ions hydrolyze"),
]


def hydrolysis(th):
    W = 1226
    top = 122
    rh = 112
    H = top + 4 * (rh + 14) + 20
    out = [header(W, th, "SALT HYDROLYSIS", "Whether a salt solution is acidic, basic or neutral depends on its parent "
                                            "acid and base")]
    for i, (pair, salt, nature, ph, col, note) in enumerate(SALTS):
        y = top + i * (rh + 14)
        out.append(_card(MX, y, W - 2 * MX, rh, th))
        out.append(f'<rect x="{MX}" y="{y}" width="10" height="{rh}" rx="5" fill="{col}"/>')
        out.append(fit_text(pair, MX + 34, y + 44, 20, th["ink"], 430, anchor="start"))
        out.append(fit_text(note, MX + 34, y + 76, 14, th["sub"], 430, "Regular", anchor="start"))
        bx = MX + 490
        out.append(f'<rect x="{bx}" y="{y + 22}" width="260" height="{rh - 44}" rx="12" fill="{th["plate"]}"/>')
        out.append(chem(salt, bx + 130, y + rh / 2 + 8, 22, "#1E2A3A", "middle"))
        px = bx + 280
        pw = W - MX - 22 - px
        out.append(f'<rect x="{px}" y="{y + 22}" width="{pw}" height="{rh - 44}" rx="12" fill="{col}"/>')
        out.append(fit_text(nature, px + pw / 2, y + rh / 2 - 2, 18, "#FFFFFF", pw - 20))
        out.append(text(ph, px + pw / 2, y + rh / 2 + 20, 15, "#FFFFFF", "SemiBold"))
    return W, H, "".join(out)


def buffers(th):
    W = 1226
    top = 122
    cw = (W - 2 * MX - 24) / 2
    ch = 400
    H = top + ch + 24 + 150
    out = [header(W, th, "BUFFER SOLUTIONS", "Solutions that resist changes in pH when a little acid or base is added")]
    data = [("Acidic buffer", T, "Weak acid + its conjugate base (salt)", "CH_{3}COOH + CH_{3}COONa",
             "[H^{+}] = K_{a} × " + tr("(mol acid / mol salt)"), "pH < 7"),
            ("Basic buffer", O, "Weak base + its conjugate acid (salt)", "NH_{3} + NH_{4}Cl",
             "[OH^{−}] = K_{b} × " + tr("(mol base / mol salt)"), "pH > 7")]
    for k, (name, col, desc, ex, f, ph) in enumerate(data):
        x = MX + k * (cw + 24)
        out.append(_card(x, top, cw, ch, th))
        out.append(f'<rect x="{x}" y="{top}" width="{cw}" height="60" rx="14" fill="{col}"/>'
                   f'<rect x="{x}" y="{top + 34}" width="{cw}" height="26" fill="{col}"/>')
        out.append(text(name, x + cw / 2, top + 40, 24, "#FFFFFF"))
        out.append(fit_text(desc, x + cw / 2, top + 104, 16, th["ink"], cw - 40, "SemiBold"))
        out.append(text("Example", x + cw / 2, top + 150, 13, th["sub"], "SemiBold"))
        out.append(f'<rect x="{x + 24}" y="{top + 164}" width="{cw - 48}" height="64" rx="12" fill="{th["plate"]}"/>')
        out.append(chem(ex, x + cw / 2, top + 205, 21, "#1E2A3A", "middle"))
        out.append(text("Formula", x + cw / 2, top + 262, 13, th["sub"], "SemiBold"))
        out.append(f'<rect x="{x + 24}" y="{top + 276}" width="{cw - 48}" height="64" rx="12" '
                   f'fill="{mix(th["card"], col, .16)}"/>')
        out.append(chem(f, x + cw / 2, top + 316, 18, th["ink"], "middle"))
        out.append(text(ph, x + cw / 2, top + 376, 18, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3)))
    y = top + ch + 24
    out.append(_card(MX, y, W - 2 * MX, 120, th))
    out.append(text("In the body: blood is kept at pH ≈ 7.4 by the carbonic acid–bicarbonate buffer", W / 2, y + 48, 16,
                    th["ink"], "SemiBold"))
    out.append(chem("H_{2}CO_{3} / HCO_{3}^{−}", W / 2, y + 88, 22, th["accent"], "middle"))
    return W, H, "".join(out)


POSTERS = [
    ("salt-hydrolysis", hydrolysis, "Salt hydrolysis chart, acidic, basic and neutral salt solutions",
     ["salt hydrolysis", "hydrolysis", "salt", "acidic salt", "basic salt", "neutral salt", "ammonium chloride",
      "sodium acetate", "sodium chloride", "ph", "acids and bases", "ions", "solution", "weak acid"]),
    ("buffer-solutions", buffers, "Buffer solutions chart, acidic and basic buffers with formulas",
     ["buffer", "buffer solution", "acidic buffer", "basic buffer", "ph", "henderson", "conjugate base",
      "acetic acid", "ammonia", "blood ph", "bicarbonate", "equilibrium", "weak acid", "weak base"]),
]

TR.update({
    "SALT HYDROLYSIS": "HIDROLISIS GARAM",
    "Whether a salt solution is acidic, basic or neutral depends on its parent acid and base":
        "Sifat larutan garam (asam, basa, atau netral) bergantung pada asam dan basa pembentuknya",
    "Strong acid + strong base": "Asam kuat + basa kuat", "Strong acid + weak base": "Asam kuat + basa lemah",
    "Weak acid + strong base": "Asam lemah + basa kuat", "Weak acid + weak base": "Asam lemah + basa lemah",
    "Neutral": "Netral", "Acidic": "Asam", "Basic": "Basa", "Depends on Ka and Kb": "Bergantung pada Ka dan Kb",
    "no hydrolysis": "tidak terhidrolisis", "the cation hydrolyzes": "kation terhidrolisis (hidrolisis parsial)",
    "the anion hydrolyzes": "anion terhidrolisis (hidrolisis parsial)",
    "both ions hydrolyze": "kedua ion terhidrolisis (hidrolisis total)",
    "BUFFER SOLUTIONS": "LARUTAN PENYANGGA",
    "Solutions that resist changes in pH when a little acid or base is added":
        "Larutan yang mampu mempertahankan pH saat ditambah sedikit asam atau basa",
    "Acidic buffer": "Penyangga asam", "Basic buffer": "Penyangga basa",
    "Weak acid + its conjugate base (salt)": "Asam lemah + basa konjugasinya (garam)",
    "Weak base + its conjugate acid (salt)": "Basa lemah + asam konjugasinya (garam)", "Formula": "Rumus",
    "(mol acid / mol salt)": "(mol asam / mol garam)", "(mol base / mol salt)": "(mol basa / mol garam)",
    "In the body: blood is kept at pH ≈ 7.4 by the carbonic acid–bicarbonate buffer":
        "Dalam tubuh: pH darah dijaga ≈ 7,4 oleh penyangga asam karbonat–bikarbonat",
})
