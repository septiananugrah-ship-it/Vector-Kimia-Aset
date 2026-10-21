"""Poster edukasi kimia jilid 23: orde reaksi (hukum laju) dan tetapan kesetimbangan.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
import math

from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters12 import eq_arrow
from posters2 import _card
from posters3 import mix
from posters4 import chem

ORDERS = [
    ("Zero order", "rate = k", "[A] = [A]_{0} − kt", "Rate does not depend on [A]", lambda t: max(0.0, 1 - t), T),
    ("First order", "rate = k[A]", "ln[A] = ln[A]_{0} − kt", "Rate doubles when [A] doubles",
     lambda t: math.exp(-2.2 * t), O),
    ("Second order", "rate = k[A]^{2}", "1/[A] = 1/[A]_{0} + kt", "Rate quadruples when [A] doubles",
     lambda t: 1 / (1 + 6 * t), P),
]


def orders(th):
    W = 1226
    top = 122
    gap = 20
    cw = (W - 2 * MX - 2 * gap) / 3
    ch = 560
    H = top + ch + 24 + 100
    out = [header(W, th, "REACTION ORDER AND RATE LAW", "How the concentration of a reactant affects the reaction "
                                                        "rate")]
    for i, (name, law, integ, note, f, col) in enumerate(ORDERS):
        x = MX + i * (cw + gap)
        out.append(_card(x, top, cw, ch, th))
        out.append(f'<rect x="{x}" y="{top}" width="{cw}" height="58" rx="14" fill="{col}"/>'
                   f'<rect x="{x}" y="{top + 32}" width="{cw}" height="26" fill="{col}"/>')
        out.append(text(name, x + cw / 2, top + 39, 23, "#FFFFFF"))
        out.append(f'<rect x="{x + 22}" y="{top + 78}" width="{cw - 44}" height="64" rx="12" fill="{th["plate"]}"/>')
        out.append(chem(law, x + cw / 2, top + 120, 26, "#1E2A3A", "middle"))
        # grafik [A] terhadap waktu
        gx, gy, gw, gh = x + 62, top + 340, cw - 100, 170
        out.append(f'<path d="M{gx} {gy - gh - 10}V{gy}H{gx + gw + 8}" fill="none" stroke="{th["sub"]}" '
                   'stroke-width="2.4" stroke-linecap="round"/>')
        d = "M" + " L".join(f"{gx + t / 40 * gw:.1f} {gy - gh * f(t / 40):.1f}" for t in range(41))
        out.append(f'<path d="{d}" fill="none" stroke="{col}" stroke-width="5" stroke-linecap="round" '
                   'stroke-linejoin="round"/>')
        out.append(text("[A]", gx - 12, gy - gh + 4, 14, th["sub"], "Bold", "end"))
        out.append(text("time", gx + gw, gy + 24, 13, th["sub"], "SemiBold", "end"))
        out.append(text("Integrated rate law", x + cw / 2, top + 392, 13, th["sub"], "SemiBold"))
        out.append(f'<rect x="{x + 22}" y="{top + 404}" width="{cw - 44}" height="56" rx="12" '
                   f'fill="{mix(th["card"], col, .16)}"/>')
        out.append(chem(integ, x + cw / 2, top + 440, 19, th["ink"], "middle"))
        out.append(fit_text(note, x + cw / 2, top + 506, 15, th["ink"], cw - 40, "SemiBold"))
    y = top + ch + 24
    out.append(_card(MX, y, W - 2 * MX, 76, th))
    out.append(chem(tr("General rate law:  rate = k[A]^{m}[B]^{n}   ·   overall order = m + n"), W / 2, y + 47, 20,
                    th["accent"], "middle"))
    return W, H, "".join(out)


def equilibrium_constant(th):
    W = 1226
    top = 122
    H = top + 190 + 20 + 250 + 20 + 190 + 30
    out = [header(W, th, "EQUILIBRIUM CONSTANT", "Kc and Kp describe the position of a chemical equilibrium")]
    out.append(_card(MX, top, W - 2 * MX, 190, th))
    cx = W / 2
    out.append(chem("aA + bB", cx - 34, top + 62, 30, th["accent"], "end"))
    out.append(eq_arrow(cx - 24, cx + 24, top + 52, th["accent"]))
    out.append(chem("cC + dD", cx + 34, top + 62, 30, th["accent"], "start"))
    out.append(f'<rect x="{cx - 330}" y="{top + 92}" width="300" height="80" rx="14" fill="{th["plate"]}"/>')
    out.append(f'<rect x="{cx + 30}" y="{top + 92}" width="300" height="80" rx="14" fill="{th["plate"]}"/>')
    for k, (lab, num, den) in enumerate((("K_{c} =", "[C]^{c}[D]^{d}", "[A]^{a}[B]^{b}"),
                                         ("K_{p} =", "(P_{C})^{c}(P_{D})^{d}", "(P_{A})^{a}(P_{B})^{b}"))):
        bx = cx - 330 + k * 360
        out.append(chem(lab, bx + 24, top + 140, 22, "#1E2A3A", "start"))
        fx = bx + 190
        out.append(chem(num, fx, top + 124, 18, "#1E2A3A", "middle"))
        out.append(f'<path d="M{fx - 82} {top + 132}H{fx + 82}" stroke="#1E2A3A" stroke-width="2.2"/>')
        out.append(chem(den, fx, top + 158, 18, "#1E2A3A", "middle"))
    y = top + 210
    cw = (W - 2 * MX - 2 * 18) / 3
    for k, (cond, meaning, col) in enumerate((("K > 1", "Products are favored at equilibrium", T),
                                              ("K ≈ 1", "Reactants and products are similar", O),
                                              ("K < 1", "Reactants are favored at equilibrium", P))):
        x = MX + k * (cw + 18)
        out.append(_card(x, y, cw, 250, th))
        out.append(f'<rect x="{x}" y="{y}" width="{cw}" height="8" rx="4" fill="{col}"/>')
        out.append(text(cond, x + cw / 2, y + 70, 36, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3)))
        # timbangan sederhana: batang miring ke arah yang diunggulkan
        tilt = (14, 0, -14)[k]  # sisi yang diunggulkan lebih berat (turun)
        bx, by = x + cw / 2, y + 140
        a = math.radians(tilt)
        lx, ly = bx - 90 * math.cos(a), by - 90 * math.sin(a)
        rx, ry = bx + 90 * math.cos(a), by + 90 * math.sin(a)
        out.append(f'<path d="M{bx} {by}L{bx - 16} {by + 34}H{bx + 16}Z" fill="{th["sub"]}"/>')
        out.append(f'<path d="M{lx:.1f} {ly:.1f}L{rx:.1f} {ry:.1f}" stroke="{th["ink"]}" stroke-width="5" '
                   'stroke-linecap="round"/>')
        out.append(f'<rect x="{lx - 34:.1f}" y="{ly - 34:.1f}" width="68" height="30" rx="8" fill="{R}"/>'
                   + text("R", lx, ly - 13, 16, "#FFFFFF"))
        out.append(f'<rect x="{rx - 34:.1f}" y="{ry - 34:.1f}" width="68" height="30" rx="8" fill="#3D62C4"/>'
                   + text("P", rx, ry - 13, 16, "#FFFFFF"))
        out.append(fit_text(meaning, x + cw / 2, y + 222, 15, th["ink"], cw - 30, "SemiBold"))
    y += 270
    out.append(_card(MX, y, W - 2 * MX, 190, th))
    out.append(text("Reaction quotient Q (same expression, any moment)", W / 2, y + 40, 18, th["ink"]))
    rows = [("Q < K", "Reaction shifts right, toward products"), ("Q = K", "System is at equilibrium"),
            ("Q > K", "Reaction shifts left, toward reactants")]
    for k, (q, m) in enumerate(rows):
        ry = y + 66 + k * 38
        out.append(f'<rect x="{MX + 60}" y="{ry}" width="{W - 2 * MX - 120}" height="32" rx="8" '
                   f'fill="{mix(th["card"], th["accent"], .12)}"/>')
        out.append(text(q, MX + 130, ry + 23, 17, th["accent"], "Bold"))
        out.append(fit_text(m, MX + 220, ry + 23, 16, th["ink"], W - 2 * MX - 300, "SemiBold", "start"))
    out.append(text("Pure solids and liquids are left out of K expressions", W / 2, H - 14, 13, th["sub"],
                    "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("reaction-order-rate-law", orders, "Reaction order and rate law chart, zero, first and second order graphs",
     ["rate law", "reaction order", "zero order", "first order", "second order", "chemical kinetics",
      "rate constant", "integrated rate law", "concentration", "reaction rate", "graph", "physical chemistry",
      "kinetics", "rate equation"]),
    ("equilibrium-constant", equilibrium_constant, "Equilibrium constant chart, Kc, Kp and reaction quotient Q",
     ["equilibrium constant", "kc", "kp", "reaction quotient", "chemical equilibrium", "reversible reaction",
      "law of mass action", "products", "reactants", "partial pressure", "concentration", "physical chemistry",
      "equilibrium", "formula"]),
]

TR.update({
    "REACTION ORDER AND RATE LAW": "ORDE REAKSI DAN PERSAMAAN LAJU",
    "How the concentration of a reactant affects the reaction rate":
        "Pengaruh konsentrasi pereaksi terhadap laju reaksi",
    "Zero order": "Orde nol", "First order": "Orde satu", "Second order": "Orde dua",
    "Rate does not depend on [A]": "Laju tidak bergantung pada [A]",
    "Rate doubles when [A] doubles": "Laju naik 2× saat [A] dinaikkan 2×",
    "Rate quadruples when [A] doubles": "Laju naik 4× saat [A] dinaikkan 2×",
    "Integrated rate law": "Persamaan laju terintegrasi", "time": "waktu",
    "General rate law:  rate = k[A]^{m}[B]^{n}   ·   overall order = m + n":
        "Persamaan laju umum:  v = k[A]^{m}[B]^{n}   ·   orde total = m + n",
    "EQUILIBRIUM CONSTANT": "TETAPAN KESETIMBANGAN",
    "Kc and Kp describe the position of a chemical equilibrium":
        "Kc dan Kp menyatakan posisi suatu kesetimbangan kimia",
    "Products are favored at equilibrium": "Hasil reaksi lebih banyak saat setimbang",
    "Reactants and products are similar": "Jumlah pereaksi dan hasil reaksi sebanding",
    "Reactants are favored at equilibrium": "Pereaksi lebih banyak saat setimbang",
    "Reaction quotient Q (same expression, any moment)": "Kuosien reaksi Q (rumus sama, pada saat tertentu)",
    "Reaction shifts right, toward products": "Reaksi bergeser ke kanan, ke arah hasil reaksi",
    "System is at equilibrium": "Sistem dalam keadaan setimbang",
    "Reaction shifts left, toward reactants": "Reaksi bergeser ke kiri, ke arah pereaksi",
    "Pure solids and liquids are left out of K expressions": "Zat padat dan cair murni tidak dimasukkan ke rumus K",
})
