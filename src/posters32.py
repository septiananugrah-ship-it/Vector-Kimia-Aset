"""Poster edukasi kimia jilid 32: uji nyala ion logam dan sifat logam transisi (warna larutan ion).
Didaftarkan ke posters.py lewat POSTERS (semua tema x 2 bahasa).
"""
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters3 import mix
from posters4 import chem
from textpath import width

INK = "#1E2A3A"

FLAMES = [("Li^{+}", "Lithium", "Crimson red", "#D81B3C"), ("Na^{+}", "Sodium", "Bright yellow", "#FFC21A"),
          ("K^{+}", "Potassium", "Lilac", "#B57BFF"), ("Ca^{2+}", "Calcium", "Orange-red", "#FF6A2B"),
          ("Sr^{2+}", "Strontium", "Red", "#E53935"), ("Ba^{2+}", "Barium", "Pale green", "#9CCC65"),
          ("Cu^{2+}", "Copper", "Blue-green", "#26A69A"), ("Rb^{+}", "Rubidium", "Red-violet", "#C2185B")]


def _burner(cx, base, col):
    out = []
    # nyala api: lapisan luar berwarna + inti terang
    out.append(f'<path d="M{cx} {base - 150}C{cx + 34} {base - 100} {cx + 30} {base - 62} {cx} {base - 52}'
               f'C{cx - 30} {base - 62} {cx - 34} {base - 100} {cx} {base - 150}Z" fill="{col}"/>')
    out.append(f'<path d="M{cx} {base - 112}C{cx + 15} {base - 88} {cx + 13} {base - 66} {cx} {base - 58}'
               f'C{cx - 13} {base - 66} {cx - 15} {base - 88} {cx} {base - 112}Z" fill="{mix(col, "#FFFFFF", .6)}"/>')
    # pembakar bunsen
    out.append(f'<rect x="{cx - 9}" y="{base - 54}" width="18" height="40" fill="#9AA5B1" stroke="{INK}" '
               'stroke-width="2.5"/>')
    out.append(f'<path d="M{cx - 30} {base}H{cx + 30}L{cx + 22} {base - 14}H{cx - 22}Z" fill="#7C8B9C" '
               f'stroke="{INK}" stroke-width="2.5" stroke-linejoin="round"/>')
    # kawat nikrom
    out.append(f'<path d="M{cx + 50} {base - 140}L{cx + 6} {base - 96}" stroke="#5B6878" stroke-width="3" '
               'stroke-linecap="round"/><circle cx="{0}" cy="{1}" r="5" fill="none" stroke="#5B6878" '
               'stroke-width="2.5"/>'.format(cx + 3, base - 93))
    return "".join(out)


def flame_test(th):
    W = 1226
    top = 122
    gap = 14
    cw = (W - 2 * MX - 3 * gap) / 4
    ch = 300
    H = top + 2 * (ch + gap) + 60
    out = [header(W, th, "FLAME TEST", "Metal ions give characteristic colors when heated in a flame")]
    for i, (ion, name, color, col) in enumerate(FLAMES):
        x = MX + (i % 4) * (cw + gap)
        y = top + (i // 4) * (ch + gap)
        out.append(_card(x, y, cw, ch, th))
        out.append(f'<rect x="{x + 14}" y="{y + 14}" width="{cw - 28}" height="190" rx="12" fill="#16213A"/>')
        out.append(_burner(x + cw / 2, y + 196, col))
        out.append(chem(ion, x + cw / 2, y + 240, 24, th["ink"], "middle"))
        out.append(fit_text(f"{tr(name)} · {tr(color)}", x + cw / 2, y + 274, 15,
                            mix(col, "#000000", .3) if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .25), cw - 20,
                            "Bold"))
    out.append(text("Dip a clean nichrome wire in the sample, then hold it in a hot, blue Bunsen flame", W / 2,
                    H - 22, 14, th["sub"], "SemiBold"))
    return W, H, "".join(out)


IONS = [("Cu^{2+}", "Blue", "#2F80ED"), ("Fe^{2+}", "Pale green", "#B8E0A0"), ("Fe^{3+}", "Yellow-brown", "#D4A017"),
        ("Ni^{2+}", "Green", "#3FAE5A"), ("Co^{2+}", "Pink", "#F48FB1"), ("Cr^{3+}", "Dark green", "#2E7D5B"),
        ("MnO_{4}^{−}", "Purple", "#7B1FA2"), ("Cr_{2}O_{7}^{2−}", "Orange", "#F57C00")]


def _beaker(cx, base, col, w=86, h=110):
    x0 = cx - w / 2
    return (f'<path d="M{x0 + 4} {base - h * .7}H{x0 + w - 4}V{base - 8}a8 8 0 0 1-8 8H{x0 + 12}a8 8 0 0 1-8-8Z" '
            f'fill="{col}"/>'
            f'<path d="M{x0 - 6} {base - h}H{x0}V{base - 8}a8 8 0 0 0 8 8H{x0 + w - 8}a8 8 0 0 0 8-8V{base - h}" '
            f'fill="none" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>'
            f'<path d="M{x0 + 14} {base - h * .62}V{base - 18}" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" '
            'stroke-opacity="1"/>')


def transition(th):
    W = 1226
    top = 122
    gap = 14
    cw = (W - 2 * MX - 3 * gap) / 4
    ch = 210
    H = top + 2 * (ch + gap) + 20 + 150 + 30
    out = [header(W, th, "TRANSITION METALS", "Colored ions, variable oxidation states and useful catalysts")]
    for i, (ion, color, col) in enumerate(IONS):
        x = MX + (i % 4) * (cw + gap)
        y = top + (i // 4) * (ch + gap)
        out.append(_card(x, y, cw, ch, th))
        out.append(f'<rect x="{x + 14}" y="{y + 12}" width="{cw - 28}" height="134" rx="12" fill="{th["plate"]}"/>')
        out.append(_beaker(x + cw / 2, y + 134, col))
        out.append(chem(ion, x + cw / 2, y + 172, 22, th["ink"], "middle"))
        out.append(fit_text(color, x + cw / 2, y + 196, 14, th["sub"], cw - 20, "SemiBold"))
    y = top + 2 * (ch + gap) + 20
    out.append(_card(MX, y, W - 2 * MX, 150, th))
    props = [("Colored compounds", "Ions absorb some wavelengths of visible light"),
             ("Variable oxidation states", "Fe²⁺ / Fe³⁺, Cu⁺ / Cu²⁺, Mn²⁺ to Mn⁷⁺"),
             ("Good catalysts", "Fe in the Haber process, V₂O₅ in the contact process"),
             ("Strong, dense metals", "High melting points; used in alloys such as steel")]
    pw = (W - 2 * MX - 40 - 3 * 14) / 4
    for k, (head, desc) in enumerate(props):
        px = MX + 20 + k * (pw + 14)
        out.append(f'<rect x="{px:.1f}" y="{y + 20}" width="{pw:.1f}" height="110" rx="14" '
                   f'fill="{mix(th["card"], "#F2C94C", .2)}"/>')
        out.append(fit_text(head, px + pw / 2, y + 50, 17, th["ink"], pw - 20))
        lines, cur = [], ""
        for w_ in tr(desc).split():
            t = (cur + " " + w_).strip()
            if width(t, 14, "SemiBold") > pw - 30 and cur:
                lines.append(cur)
                cur = w_
            else:
                cur = t
        lines.append(cur)
        for j, ln in enumerate(lines[:3]):
            out.append(text(ln, px + pw / 2, y + 80 + j * 20, 14, th["sub"], "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("flame-test", flame_test, "Flame test chart, colors of metal ions in a Bunsen burner flame",
     ["flame test", "flame colors", "metal ions", "bunsen burner", "lithium", "sodium", "potassium", "calcium",
      "copper", "barium", "strontium", "qualitative analysis", "fireworks", "spectroscopy"]),
    ("transition-metals", transition, "Transition metals chart, colored ion solutions, oxidation states and catalysts",
     ["transition metals", "colored ions", "copper sulfate", "iron", "nickel", "cobalt", "chromium",
      "permanganate", "dichromate", "oxidation states", "catalyst", "d block", "inorganic chemistry",
      "solutions"]),
]

TR.update({
    "FLAME TEST": "UJI NYALA",
    "Metal ions give characteristic colors when heated in a flame": "Ion logam memberi warna khas saat dipanaskan dalam nyala api",
    "Lithium": "Litium", "Sodium": "Natrium", "Potassium": "Kalium", "Calcium": "Kalsium", "Strontium": "Stronsium",
    "Barium": "Barium", "Copper": "Tembaga", "Rubidium": "Rubidium", "Crimson red": "Merah tua",
    "Bright yellow": "Kuning terang", "Lilac": "Ungu muda", "Orange-red": "Merah jingga", "Red": "Merah",
    "Pale green": "Hijau pucat", "Blue-green": "Hijau kebiruan", "Red-violet": "Merah-ungu",
    "Dip a clean nichrome wire in the sample, then hold it in a hot, blue Bunsen flame":
        "Celupkan kawat nikrom bersih ke sampel, lalu panaskan di nyala biru pembakar Bunsen",
    "TRANSITION METALS": "LOGAM TRANSISI",
    "Colored ions, variable oxidation states and useful catalysts":
        "Ion berwarna, bilangan oksidasi beragam, dan katalis yang berguna",
    "Blue": "Biru", "Yellow-brown": "Kuning kecokelatan", "Green": "Hijau", "Pink": "Merah muda",
    "Dark green": "Hijau tua", "Purple": "Ungu", "Orange": "Jingga",
    "Colored compounds": "Senyawa berwarna", "Ions absorb some wavelengths of visible light":
        "Ion menyerap sebagian panjang gelombang cahaya tampak",
    "Variable oxidation states": "Bilangan oksidasi beragam",
    "Fe²⁺ / Fe³⁺, Cu⁺ / Cu²⁺, Mn²⁺ to Mn⁷⁺": "Fe²⁺ / Fe³⁺, Cu⁺ / Cu²⁺, Mn²⁺ hingga Mn⁷⁺",
    "Good catalysts": "Katalis yang baik",
    "Fe in the Haber process, V₂O₅ in the contact process": "Fe pada proses Haber, V₂O₅ pada proses kontak",
    "Strong, dense metals": "Logam kuat dan padat",
    "High melting points; used in alloys such as steel": "Titik leleh tinggi; dipakai dalam paduan seperti baja",
})
