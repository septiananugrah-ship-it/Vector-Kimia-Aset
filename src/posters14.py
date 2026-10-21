"""Poster edukasi kimia jilid 14: teori asam-basa dan daftar asam/basa kuat & lemah.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text
from posters12 import eq_arrow
from posters2 import _card
from posters3 import mix
from posters4 import chem

THEORIES = [
    ("Arrhenius", "1884", "Acid: releases H⁺ in water", "Base: releases OH⁻ in water",
     ("HCl", "H^{+} + Cl^{−}", False), T),
    ("Brønsted–Lowry", "1923", "Acid: proton (H⁺) donor", "Base: proton (H⁺) acceptor",
     ("NH_{3} + H_{2}O", "NH_{4}^{+} + OH^{−}", True), O),
    ("Lewis", "1923", "Acid: electron pair acceptor", "Base: electron pair donor",
     ("BF_{3} + NH_{3}", "F_{3}B–NH_{3}", False), P),
]


def theories(th):
    W = 1226
    top = 122
    rh = 170
    H = top + 3 * (rh + 16) + 20
    out = [header(W, th, "ACID–BASE THEORIES", "Three ways chemists define acids and bases")]
    for i, (name, year, a, b, (lhs, rhs, eq), col) in enumerate(THEORIES):
        y = top + i * (rh + 16)
        out.append(_card(MX, y, W - 2 * MX, rh, th))
        out.append(f'<rect x="{MX}" y="{y}" width="10" height="{rh}" rx="5" fill="{col}"/>')
        out.append(text(name, MX + 34, y + 48, 26, th["ink"], "Bold", "start"))
        out.append(text(year, MX + 34, y + 76, 15, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3),
                        "Bold", "start"))
        out.append(fit_text(a, MX + 34, y + 116, 16, th["ink"], 420, "SemiBold", anchor="start"))
        out.append(fit_text(b, MX + 34, y + 146, 16, th["ink"], 420, "SemiBold", anchor="start"))
        bx = MX + 500
        bw = W - MX - 24 - bx
        cx = bx + bw / 2
        out.append(f'<rect x="{bx}" y="{y + 30}" width="{bw}" height="{rh - 60}" rx="14" fill="{th["plate"]}"/>')
        out.append(chem(lhs, cx - 36, y + rh / 2 + 9, 24, "#1E2A3A", "end"))
        if eq:
            out.append(eq_arrow(cx - 24, cx + 24, y + rh / 2, "#1E2A3A"))
        else:
            out.append(text("→", cx, y + rh / 2 + 9, 26, "#1E2A3A"))
        out.append(chem(rhs, cx + 36, y + rh / 2 + 9, 24, "#1E2A3A", "start"))
    return W, H, "".join(out)


STRONG_WEAK = [
    ("Strong acids", R, ["HCl", "HBr", "HI", "HNO_{3}", "H_{2}SO_{4}", "HClO_{4}"], "ionize completely in water"),
    ("Weak acids", "#F2A541", ["CH_{3}COOH", "HF", "H_{2}CO_{3}", "HCN", "H_{3}PO_{4}", "HCOOH"],
     "ionize only partially"),
    ("Strong bases", "#3D62C4", ["NaOH", "KOH", "LiOH", "Ca(OH)_{2}", "Ba(OH)_{2}", "Sr(OH)_{2}"],
     "dissociate completely in water"),
    ("Weak bases", "#6FA8DC", ["NH_{3}", "NH_{4}OH", "CH_{3}NH_{2}", "Al(OH)_{3}", "Mg(OH)_{2}", "N_{2}H_{4}"],
     "ionize only partially"),
]


def strong_weak(th):
    W = 1226
    top = 122
    cw = (W - 2 * MX - 24) / 2
    ch = 300
    H = top + 2 * (ch + 24) + 20
    out = [header(W, th, "STRONG AND WEAK ACIDS AND BASES", "Common examples grouped by how much they ionize in water")]
    for i, (name, col, items, note) in enumerate(STRONG_WEAK):
        x = MX + (i % 2) * (cw + 24)
        y = top + (i // 2) * (ch + 24)
        out.append(_card(x, y, cw, ch, th))
        out.append(f'<rect x="{x}" y="{y}" width="{cw}" height="58" rx="14" fill="{col}"/>'
                   f'<rect x="{x}" y="{y + 32}" width="{cw}" height="26" fill="{col}"/>')
        out.append(text(name, x + cw / 2, y + 39, 23, "#FFFFFF"))
        bw = (cw - 24 * 2 - 2 * 12) / 3
        for k, f in enumerate(items):
            bx = x + 24 + (k % 3) * (bw + 12)
            by = y + 82 + (k // 3) * 78
            out.append(f'<rect x="{bx}" y="{by}" width="{bw}" height="64" rx="12" fill="{mix(th["card"], col, .16)}"/>')
            out.append(chem(f, bx + bw / 2, by + 41, 21, th["ink"], "middle"))
        out.append(fit_text(note, x + cw / 2, y + ch - 26, 14, th["sub"], cw - 40, "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("acid-base-theories", theories, "Acid base theories chart, Arrhenius, Bronsted-Lowry and Lewis definitions",
     ["acid base theory", "arrhenius", "bronsted lowry", "lewis acid", "lewis base", "proton donor", "proton acceptor",
      "electron pair", "acid", "base", "definitions", "ammonia", "hydrogen ion", "hydroxide"]),
    ("strong-weak-acids-bases", strong_weak, "Strong and weak acids and bases chart with common examples",
     ["strong acid", "weak acid", "strong base", "weak base", "ionization", "dissociation", "hydrochloric acid",
      "sulfuric acid", "acetic acid", "sodium hydroxide", "ammonia", "acids and bases", "electrolyte", "ph"]),
]

TR.update({
    "ACID–BASE THEORIES": "TEORI ASAM–BASA",
    "Three ways chemists define acids and bases": "Tiga cara para ahli kimia mendefinisikan asam dan basa",
    "Acid: releases H⁺ in water": "Asam: melepas H⁺ dalam air", "Base: releases OH⁻ in water": "Basa: melepas OH⁻ dalam air",
    "Acid: proton (H⁺) donor": "Asam: donor proton (H⁺)", "Base: proton (H⁺) acceptor": "Basa: akseptor proton (H⁺)",
    "Acid: electron pair acceptor": "Asam: akseptor pasangan elektron",
    "Base: electron pair donor": "Basa: donor pasangan elektron",
    "STRONG AND WEAK ACIDS AND BASES": "ASAM DAN BASA KUAT SERTA LEMAH",
    "Common examples grouped by how much they ionize in water":
        "Contoh umum dikelompokkan berdasarkan derajat ionisasinya dalam air",
    "Strong acids": "Asam kuat", "Weak acids": "Asam lemah", "Strong bases": "Basa kuat", "Weak bases": "Basa lemah",
    "ionize completely in water": "terionisasi sempurna dalam air", "ionize only partially": "terionisasi sebagian",
    "dissociate completely in water": "terdisosiasi sempurna dalam air",
})
