"""Barang cetak: sertifikat prestasi kimia (A4 lanskap) dan lembar kerja
"beri nama alat laboratorium" (A4 potret), bahasa Inggris & Indonesia."""
import math

import icons_concepts
import icons_lab2
import icons_lab_flat
import poster_kit
from poster_i18n import TR
from poster_kit import text
from render import GRID, fitted, outlinify, style_attrs

SET_ID = "chemistry-printables"
ICONS = {ic["id"]: (ic["body"], m.STROKE) for m in (icons_lab_flat, icons_lab2, icons_concepts) for ic in m.ICONS}

CERT_THEMES = [
    ("navy-gold", "#16213A", "#E2B14A", "#FFFFFF", "#AEB9C9", "navy and gold"),
    ("white-teal", "#FFFFFF", "#1F9AA8", "#1E2A3A", "#5B6878", "white and teal"),
]


def icon(key, x, y, size, outline=False, ink="1E2A3A"):
    body, stroke = ICONS[key]
    if outline:
        body = outlinify(body)
    return (f'<g transform="translate({x - size / 2:.1f} {y - size / 2:.1f}) scale({size / GRID:.4f})">'
            f'<g {style_attrs(stroke, ink)}>{fitted(body, stroke)}</g></g>')


def hex_corner(cx, cy, s, col, n=3):
    out = []
    for i in range(n):
        for j in range(n - i):
            x = cx + (i * 1.5) * s * (1 if cx < 500 else -1)
            y = cy + (j * math.sqrt(3) + (math.sqrt(3) / 2 if i % 2 else 0)) * s * (1 if cy < 400 else -1)
            pts = [(x + s * math.cos(math.radians(60 * k)), y + s * math.sin(math.radians(60 * k))) for k in range(6)]
            out.append("M" + "L".join(f"{a:.1f} {b:.1f}" for a, b in pts) + "z")
    return f'<path d="{"".join(out)}" fill="none" stroke="{col}" stroke-width="2.4"/>'


def certificate(bg, gold, ink, sub):
    W, H = 1131, 800
    out = [f'<rect x="-1" y="-1" width="{W + 2}" height="{H + 2}" fill="{bg}"/>',
           f'<rect x="28" y="28" width="{W - 56}" height="{H - 56}" rx="6" fill="none" stroke="{gold}" stroke-width="6"/>',
           f'<rect x="44" y="44" width="{W - 88}" height="{H - 88}" rx="4" fill="none" stroke="{gold}" stroke-width="1.6"/>',
           hex_corner(70, 70, 26, gold), hex_corner(W - 70, 70, 26, gold),
           hex_corner(70, H - 70, 26, gold), hex_corner(W - 70, H - 70, 26, gold)]
    out.append(f'<circle cx="{W / 2}" cy="150" r="58" fill="{gold}"/>'
               f'<circle cx="{W / 2}" cy="150" r="50" fill="{bg}" stroke="{gold}" stroke-width="2"/>')
    out.append(icon("atom", W / 2, 150, 78))
    out.append(text("CERTIFICATE", W / 2, 278, 64, ink))
    out.append(text("OF ACHIEVEMENT", W / 2, 322, 26, gold, "SemiBold"))
    out.append(text("This certificate is proudly presented to", W / 2, 386, 18, sub, "Regular"))
    out.append(f'<path d="M{W / 2 - 280} 470H{W / 2 + 280}" stroke="{gold}" stroke-width="2"/>')
    out.append(text("for outstanding achievement in Chemistry", W / 2, 516, 18, sub, "Regular"))
    for k, lab in enumerate(("Date", "Signature")):
        x = W / 2 + (-260 if k == 0 else 260)
        out.append(f'<path d="M{x - 130} 660H{x + 130}" stroke="{ink}" stroke-width="1.6"/>'
                   + text(lab, x, 688, 15, sub, "SemiBold"))
    out.append(icon("erlenmeyer-flask", 150, H / 2 + 40, 110))
    out.append(icon("microscope", W - 150, H / 2 + 40, 110))
    return W, H, "".join(out)


WORKSHEETS = [
    ("label-lab-equipment-1", ["erlenmeyer-flask", "beaker", "test-tube", "microscope", "bunsen-burner",
                               "funnel", "thermometer", "graduated-cylinder"]),
    ("label-lab-equipment-2", ["round-bottom-flask", "volumetric-flask", "pipette", "dropper", "petri-dish",
                               "mortar-and-pestle", "safety-goggles", "burette-stand"]),
]


def worksheet(ids):
    W, H = 800, 1131
    ink = "#1E2A3A"
    out = [f'<rect x="-1" y="-1" width="{W + 2}" height="{H + 2}" fill="#FFFFFF"/>',
           f'<rect x="24" y="24" width="{W - 48}" height="{H - 48}" rx="20" fill="none" stroke="{ink}" stroke-width="3"/>',
           text("LABEL THE LAB EQUIPMENT", W / 2, 96, 36, ink),
           text("Write the name of each laboratory tool on the line.", W / 2, 128, 16, "#5B6878", "Regular"),
           text("Name: ____________________   Class: ________", 60, 178, 16, ink, "SemiBold", "start")]
    cw, ch = (W - 120) / 2, (H - 280) / 4
    for i, key in enumerate(ids):
        x = 60 + (i % 2) * cw
        y = 210 + (i // 2) * ch
        out.append(f'<rect x="{x + 6}" y="{y}" width="{cw - 12}" height="{ch - 14}" rx="14" fill="none" '
                   f'stroke="#C9D1DA" stroke-width="1.6"/>')
        out.append(icon(key, x + cw / 2, y + (ch - 14) / 2 - 22, ch - 90, outline=True))
        out.append(text(f"{i + 1}.", x + 26, y + ch - 36, 16, ink, "Bold", "start"))
        out.append(f'<path d="M{x + 50} {y + ch - 36}H{x + cw - 26}" stroke="{ink}" stroke-width="1.4"/>')
    return W, H, "".join(out)


def flashcards(ids, start):
    """Lembar A4 berisi 8 kartu (2x4) ikon berwarna + nama, dengan garis potong putus-putus."""
    from posters import LAB_NAMES
    W, H = 800, 1131
    ink = "#1E2A3A"
    m = 30
    cw, ch = (W - 2 * m) / 2, (H - 2 * m) / 4
    out = [f'<rect x="-1" y="-1" width="{W + 2}" height="{H + 2}" fill="#FFFFFF"/>']
    for i, key in enumerate(ids):
        x = m + (i % 2) * cw
        y = m + (i // 2) * ch
        out.append(f'<rect x="{x + 10}" y="{y + 10}" width="{cw - 20}" height="{ch - 20}" rx="18" fill="#F2F8FB" '
                   'stroke="#3FB6C4" stroke-width="3"/>')
        out.append(f'<circle cx="{x + 36}" cy="{y + 36}" r="14" fill="#3FB6C4"/>'
                   + text(str(start + i), x + 36, y + 41, 13, "#FFFFFF"))
        out.append(icon(key, x + cw / 2, y + ch / 2 - 18, ch - 110))
        name = LAB_NAMES.get(key) or key.replace("-", " ").title()
        out.append(text(name, x + cw / 2, y + ch - 34, 22, ink))
    dash = 'stroke="#9AA5B1" stroke-width="1.2" stroke-dasharray="6 6"'
    out.append(f'<path d="M{W / 2} {m}V{H - m}" {dash}/>')
    for k in range(1, 4):
        out.append(f'<path d="M{m} {m + k * ch}H{W - m}" {dash}/>')
    return W, H, "".join(out)


BINGO = ["H", "He", "Li", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Fe",
         "Cu", "Zn", "Ag", "Au", "Hg", "Pb", "Sn", "I", "Ni", "Ti", "U"]


def bingo(seed):
    import random
    rnd = random.Random(seed)
    W, H = 800, 1000
    ink = "#1E2A3A"
    cols = ["#FF9E8A", "#FFC98A", "#FFE38A", "#B9E28C", "#8FD9C4", "#8ACBEF", "#A9B8F5", "#C3A6F2"]
    out = [f'<rect x="-1" y="-1" width="{W + 2}" height="{H + 2}" fill="#FFFFFF"/>',
           f'<rect x="20" y="20" width="{W - 40}" height="{H - 40}" rx="26" fill="none" stroke="{ink}" stroke-width="4"/>']
    for k, ch in enumerate("BINGO"):
        x = 80 + k * 128
        out.append(f'<rect x="{x}" y="70" width="112" height="90" rx="16" fill="{cols[k * 2 % 8]}" stroke="{ink}" '
                   'stroke-width="3"/>' + text(ch, x + 56, 140, 60, ink))
    syms = rnd.sample(BINGO, 24)
    k = 0
    for r in range(5):
        for c in range(5):
            x, y = 80 + c * 128, 190 + r * 128
            if r == 2 and c == 2:
                out.append(f'<rect x="{x}" y="{y}" width="112" height="112" rx="16" fill="#FFC845" stroke="{ink}" '
                           'stroke-width="3"/>')
                out.append(icon("atom", x + 56, y + 50, 64))
                out.append(text("FREE", x + 56, y + 100, 16, ink))
                continue
            out.append(f'<rect x="{x}" y="{y}" width="112" height="112" rx="16" fill="#FFFFFF" stroke="{ink}" '
                       'stroke-width="3"/>' + text(syms[k], x + 56, y + 74, 46, ink))
            k += 1
    out.append(text("CHEMISTRY ELEMENT BINGO", W / 2, H - 50, 26, ink))
    return W, H, "".join(out)


TR.update({
    "CERTIFICATE": "SERTIFIKAT", "OF ACHIEVEMENT": "PENGHARGAAN",
    "This certificate is proudly presented to": "Dengan bangga diberikan kepada",
    "for outstanding achievement in Chemistry": "atas prestasi luar biasa dalam bidang Kimia",
    "Date": "Tanggal", "Signature": "Tanda tangan",
    "LABEL THE LAB EQUIPMENT": "TULIS NAMA ALAT LAB",
    "Write the name of each laboratory tool on the line.": "Tuliskan nama setiap alat laboratorium pada garis.",
    "Name: ____________________   Class: ________": "Nama: ____________________   Kelas: ________",
    "CHEMISTRY ELEMENT BINGO": "BINGO UNSUR KIMIA",
})


def assets():
    out = []
    for lang, sfx in (("en", ""), ("id", "-indonesian")):
        poster_kit.set_lang(lang)
        note = " in Indonesian language" if lang == "id" else ""
        kw_lang = ["indonesian", "bahasa indonesia"] if lang == "id" else []
        for key, bg, gold, ink, sub, mood in CERT_THEMES:
            W, H, inner = certificate(bg, gold, ink, sub)
            out.append(dict(
                name=f"{SET_ID}-certificate-{key}{sfx}", size=6000, png=False,
                svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * 3}" height="{H * 3}" viewBox="0 0 {W} {H}">{inner}</svg>',
                title=f"Chemistry certificate of achievement template{note}, {mood}, A4 vector award",
                keywords=kw_lang + ["certificate", "award", "achievement", "diploma", "template", "chemistry",
                                    "science", "school", "student", "education", "printable", "a4", "border",
                                    "frame", "winner", "olympiad", "competition", "prize", "recognition",
                                    "laboratory", "atom", "vector", "illustration", "elegant", "gold"]))
        for key, ids in WORKSHEETS:
            W, H, inner = worksheet(ids)
            out.append(dict(
                name=f"{SET_ID}-worksheet-{key}{sfx}", size=3508, png=False,
                svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * 3}" height="{H * 3}" viewBox="0 0 {W} {H}">{inner}</svg>',
                title=f"Label the laboratory equipment worksheet{note}, chemistry printable A4 activity for students",
                keywords=kw_lang + ["worksheet", "label", "laboratory equipment", "lab tools", "activity",
                                    "printable", "chemistry", "science", "school", "student", "exercise",
                                    "homework", "quiz", "classroom", "teacher", "a4", "black and white", "outline",
                                    "education", "learning", "test", "assessment", "vector", "illustration"]))
        lab_ids = [ic["id"] for ic in icons_lab_flat.ICONS] + [ic["id"] for ic in icons_lab2.ICONS]
        for k in range(5):
            W, H, inner = flashcards(lab_ids[k * 8:(k + 1) * 8], k * 8 + 1)
            out.append(dict(
                name=f"{SET_ID}-flashcards-lab-{k + 1}{sfx}", size=3508, png=False,
                svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * 3}" height="{H * 3}" viewBox="0 0 {W} {H}">{inner}</svg>',
                title=f"Laboratory equipment flashcards sheet {k + 1}{note}, printable A4 chemistry cards for students",
                keywords=kw_lang + ["flashcards", "flash cards", "cards", "laboratory equipment", "lab tools",
                                    "printable", "chemistry", "science", "school", "classroom", "teacher",
                                    "vocabulary", "learning", "education", "a4", "cut out", "game", "kids",
                                    "student", "glassware", "colorful", "vector", "illustration"]))
    poster_kit.set_lang("en")
    for k in range(4):
        W, H, inner = bingo(k + 1)
        out.append(dict(
            name=f"{SET_ID}-element-bingo-{k + 1}", size=3500, png=False,
            svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * 3}" height="{H * 3}" viewBox="0 0 {W} {H}">{inner}</svg>',
            title=f"Chemistry element bingo card {k + 1}, printable periodic table classroom game vector",
            keywords=["bingo", "bingo card", "game", "classroom game", "periodic table", "chemical elements",
                      "element symbols", "chemistry", "science", "printable", "school", "teacher", "activity",
                      "fun", "learning", "education", "kids", "student", "vector", "template"]))
    return [(SET_ID, out)]
