"""Poster edukasi kimia jilid 26: efek rumah kaca dan jenis peluruhan radioaktif.
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


def greenhouse(th):
    W = 1226
    top = 122
    H = top + 420 + 20 + 230 + 30
    out = [header(W, th, "THE GREENHOUSE EFFECT", "Greenhouse gases trap heat and keep the Earth warm")]
    out.append(_card(MX, top, W - 2 * MX, 420, th))
    x0, y0, w, h = MX + 20, top + 20, W - 2 * MX - 40, 380
    ink = "#1E2A3A"
    out.append(f'<clipPath id="gh"><rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="14"/></clipPath>'
               f'<g clip-path="url(#gh)"><rect x="{x0}" y="{y0}" width="{w}" height="{h}" fill="#13203B"/>')
    for k in range(40):  # bintang
        out.append(f'<circle cx="{x0 + (k * 97) % w}" cy="{y0 + (k * 53) % 150}" r="1.6" fill="#FFFFFF"/>')
    # matahari
    sx, sy = x0 + 90, y0 + 80
    for k in range(12):
        a = math.radians(k * 30)
        out.append(f'<path d="M{sx + 52 * math.cos(a):.1f} {sy + 52 * math.sin(a):.1f}L{sx + 70 * math.cos(a):.1f} '
                   f'{sy + 70 * math.sin(a):.1f}" stroke="#FFC845" stroke-width="5" stroke-linecap="round"/>')
    out.append(f'<circle cx="{sx}" cy="{sy}" r="42" fill="#FFC845" stroke="#F2A541" stroke-width="4"/>')
    # bumi (busur besar di bawah) + atmosfer
    ex, ey, er = x0 + w / 2 + 60, y0 + h + 520, 640
    out.append(f'<circle cx="{ex}" cy="{ey}" r="{er + 120}" fill="#2F4E7A"/>')
    out.append(f'<circle cx="{ex}" cy="{ey}" r="{er}" fill="#4BB04A"/>')
    out.append(f'<path d="M{ex - er} {ey}A{er} {er} 0 0 1 {ex + er} {ey}" fill="none" stroke="{ink}" '
               'stroke-width="3"/>')
    for k in range(18):  # molekul gas rumah kaca di atmosfer
        a = math.radians(-160 + k * 8)
        rr = er + 40 + (k % 3) * 25
        gx, gy = ex + rr * math.cos(a), ey + rr * math.sin(a)
        if gy < y0 + h:
            out.append(f'<g {style_attrs(1.2)}>' + particle(gx - 7, gy, 5, "#E8573F", f"gh{k}a", shine=False)
                       + particle(gx + 4, gy, 6.5, "#4A4F5C", f"gh{k}b", shine=False)
                       + particle(gx + 15, gy, 5, "#E8573F", f"gh{k}c", shine=False) + '</g>')
    out.append('</g>')
    # sinar
    out.append(arrow_line(sx + 50, sy + 40, x0 + 420, y0 + 300, "#FFC845", 6))
    out.append(arrow_line(x0 + 440, y0 + 300, x0 + 520, y0 + 40, "#FFE9A8", 4))
    out.append(arrow_line(x0 + 600, y0 + 320, x0 + 700, y0 + 175, "#E8573F", 5))
    out.append(arrow_line(x0 + 700, y0 + 175, x0 + 790, y0 + 320, "#E8573F", 5))
    out.append(arrow_line(x0 + 820, y0 + 320, x0 + 870, y0 + 40, "#F28C78", 3))
    labels = [("1  Sunlight reaches Earth", x0 + 60, y0 + 300, "#FFC845"),
              ("2  Some is reflected to space", x0 + 540, y0 + 62, "#FFE9A8"),
              ("3  Heat is trapped by gases", x0 + 610, y0 + 150, "#F28C78"),
              ("4  Some heat escapes", x0 + 888, y0 + 62, "#F28C78")]
    for lab, lx, ly, col in labels:
        out.append(text(lab, lx, ly, 15, col, "Bold", "start"))
    y = top + 440
    out.append(_card(MX, y, W - 2 * MX, 230, th))
    out.append(text("Main greenhouse gases", W / 2, y + 38, 18, th["ink"]))
    gases = [("CO_{2}", "Burning fossil fuels", R), ("CH_{4}", "Livestock, landfills", O),
             ("N_{2}O", "Fertilizers", P), ("H_{2}O", "Water vapor", T), ("CFCs", "Old fridges, aerosols", "#7C8B9C")]
    gw = (W - 2 * MX - 40 - 4 * 12) / 5
    for k, (f, src, col) in enumerate(gases):
        gx = MX + 20 + k * (gw + 12)
        out.append(f'<rect x="{gx:.1f}" y="{y + 58}" width="{gw:.1f}" height="140" rx="14" '
                   f'fill="{mix(th["card"], col, .18)}"/>')
        out.append(f'<rect x="{gx:.1f}" y="{y + 58}" width="{gw:.1f}" height="8" rx="4" fill="{col}"/>')
        out.append(chem(f, gx + gw / 2, y + 120, 30, th["ink"], "middle"))
        out.append(fit_text(src, gx + gw / 2, y + 168, 14, th["sub"], gw - 16, "SemiBold"))
    return W, H, "".join(out)


def nuclide(sym, a, z, x, y, size, col):
    """Notasi nuklida: nomor massa di atas, nomor atom di bawah, rata kanan di kiri lambang."""
    small = size * .55
    a, z = str(a), str(z).replace("-", "−")
    wa, wz = width(a, small, "Bold"), width(z, small, "Bold")
    wl = max(wa, wz)
    return (text(a, x + wl, y - size * .42, small, col, "Bold", "end")
            + text(z, x + wl, y + size * .22, small, col, "Bold", "end")
            + text(sym, x + wl + 2, y, size, col, "Bold", "start")), wl + 2 + width(sym, size, "Bold")


def _equation(parts, cx, y, size, col):
    """parts: daftar (sym, A, Z) atau string penghubung; dirender di tengah cx."""
    pieces = []
    total = 0
    for p in parts:
        if isinstance(p, tuple):
            svg, w = nuclide(*p, 0, 0, size, col)
        else:
            w = width(p, size, "Bold")
            svg = None
        pieces.append((p, w))
        total += w + 14
    x = cx - total / 2
    out = []
    for p, w in pieces:
        if isinstance(p, tuple):
            svg, _ = nuclide(*p, x, y, size, col)
        else:
            svg = text(p, x, y, size, col, "Bold", "start")
        out.append(svg)
        x += w + 14
    return "".join(out)


DECAYS = [
    ("Alpha decay (α)", "A helium nucleus is emitted: mass number −4, atomic number −2",
     [("U", 238, 92), "→", ("Th", 234, 90), "+", ("He", 4, 2)], R),
    ("Beta decay (β⁻)", "A neutron turns into a proton and an electron is emitted: atomic number +1",
     [("C", 14, 6), "→", ("N", 14, 7), "+", ("e", 0, -1)], "#3D62C4"),
    ("Positron emission (β⁺)", "A proton turns into a neutron and a positron is emitted: atomic number −1",
     [("Na", 22, 11), "→", ("Ne", 22, 10), "+", ("e", 0, "+1")], P),
    ("Gamma emission (γ)", "High-energy radiation leaves an excited nucleus: no change in A or Z",
     [("Tc*", 99, 43), "→", ("Tc", 99, 43), "+", ("γ", 0, 0)], O),
]


def decay(th):
    W = 1226
    top = 122
    rh = 150
    H = top + 4 * (rh + 14) + 50
    out = [header(W, th, "TYPES OF RADIOACTIVE DECAY", "Unstable nuclei release particles or energy to become "
                                                       "more stable")]
    for i, (name, desc, parts, col) in enumerate(DECAYS):
        y = top + i * (rh + 14)
        out.append(_card(MX, y, W - 2 * MX, rh, th))
        out.append(f'<rect x="{MX}" y="{y}" width="10" height="{rh}" rx="5" fill="{col}"/>')
        out.append(fit_text(name, MX + 34, y + 46, 22, th["ink"], 380, anchor="start"))
        lines, cur = [], ""
        for w_ in tr(desc).split():
            t = (cur + " " + w_).strip()
            if width(t, 14, "SemiBold") > 370 and cur:
                lines.append(cur)
                cur = w_
            else:
                cur = t
        lines.append(cur)
        for j, ln in enumerate(lines[:3]):
            out.append(text(ln, MX + 34, y + 76 + j * 20, 14, th["sub"], "SemiBold", "start"))
        bx = MX + 440
        bw = W - MX - 24 - bx
        out.append(f'<rect x="{bx}" y="{y + 22}" width="{bw}" height="{rh - 44}" rx="14" fill="{th["plate"]}"/>')
        out.append(_equation(parts, bx + bw / 2, y + rh / 2 + 12, 34, "#1E2A3A"))
    out.append(text("Mass number (top) and atomic number (bottom) are conserved on both sides of the equation",
                    W / 2, H - 22, 13, th["sub"], "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("greenhouse-effect", greenhouse, "Greenhouse effect chart, how greenhouse gases trap heat, CO2 and methane",
     ["greenhouse effect", "global warming", "climate change", "greenhouse gases", "carbon dioxide", "methane",
      "atmosphere", "infrared", "environment", "environmental chemistry", "earth", "sun", "cfc", "ecology"]),
    ("radioactive-decay-types", decay, "Types of radioactive decay chart, alpha, beta, positron and gamma equations",
     ["radioactive decay", "alpha decay", "beta decay", "gamma radiation", "positron emission", "nuclear chemistry",
      "nuclear equation", "radioactivity", "isotope", "uranium", "carbon-14", "nucleus", "mass number",
      "atomic number"]),
]

TR.update({
    "THE GREENHOUSE EFFECT": "EFEK RUMAH KACA",
    "Greenhouse gases trap heat and keep the Earth warm": "Gas rumah kaca menahan panas sehingga Bumi tetap hangat",
    "1  Sunlight reaches Earth": "1  Sinar matahari sampai ke Bumi",
    "2  Some is reflected to space": "2  Sebagian dipantulkan ke angkasa",
    "3  Heat is trapped by gases": "3  Panas tertahan oleh gas",
    "4  Some heat escapes": "4  Sebagian panas lolos",
    "Main greenhouse gases": "Gas rumah kaca utama", "Burning fossil fuels": "Pembakaran bahan bakar fosil",
    "Livestock, landfills": "Peternakan, TPA sampah", "Fertilizers": "Pupuk", "Water vapor": "Uap air",
    "Old fridges, aerosols": "Kulkas lama, aerosol",
    "TYPES OF RADIOACTIVE DECAY": "JENIS-JENIS PELURUHAN RADIOAKTIF",
    "Unstable nuclei release particles or energy to become more stable":
        "Inti tidak stabil melepaskan partikel atau energi agar menjadi lebih stabil",
    "Alpha decay (α)": "Peluruhan alfa (α)", "Beta decay (β⁻)": "Peluruhan beta (β⁻)",
    "Positron emission (β⁺)": "Emisi positron (β⁺)", "Gamma emission (γ)": "Emisi gamma (γ)",
    "A helium nucleus is emitted: mass number −4, atomic number −2":
        "Inti helium dipancarkan: nomor massa −4, nomor atom −2",
    "A neutron turns into a proton and an electron is emitted: atomic number +1":
        "Neutron berubah menjadi proton dan elektron dipancarkan: nomor atom +1",
    "A proton turns into a neutron and a positron is emitted: atomic number −1":
        "Proton berubah menjadi neutron dan positron dipancarkan: nomor atom −1",
    "High-energy radiation leaves an excited nucleus: no change in A or Z":
        "Radiasi berenergi tinggi keluar dari inti tereksitasi: A dan Z tidak berubah",
    "Mass number (top) and atomic number (bottom) are conserved on both sides of the equation":
        "Nomor massa (atas) dan nomor atom (bawah) sama jumlahnya di kedua ruas persamaan",
})
