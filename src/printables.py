"""Barang cetak: sertifikat prestasi kimia (A4 lanskap) dan lembar kerja
"beri nama alat laboratorium" (A4 potret), bahasa Inggris & Indonesia."""
import math

import icons_concepts
import icons_lab2
import icons_lab_flat
import poster_kit
from poster_i18n import TR
from poster_kit import text, tr
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


def lab_report():
    """Template laporan praktikum A4."""
    W, H = 800, 1131
    ink, sub, acc = "#1E2A3A", "#5B6878", "#1F9AA8"
    out = [f'<rect x="-1" y="-1" width="{W + 2}" height="{H + 2}" fill="#FFFFFF"/>',
           f'<rect x="0" y="0" width="{W}" height="120" fill="#16213A"/>',
           text("LAB REPORT", 50, 70, 40, "#FFFFFF", "Bold", "start"),
           text("Chemistry practical", 50, 100, 16, "#AEB9C9", "SemiBold", "start"),
           icon("erlenmeyer-flask", W - 90, 60, 80)]
    y = 160
    fields = [("Name", 50), ("Class", 430), ("Date", 50), ("Group", 430)]
    for k, (lab, x) in enumerate(fields):
        yy = y + (k // 2) * 40
        out.append(text(f"{lab}:", x, yy, 15, ink, "SemiBold", "start"))
        out.append(f'<path d="M{x + 70} {yy + 3}H{x + 320}" stroke="#C9D1DA" stroke-width="1.4"/>')
    sections = [("Title", 1), ("Objective", 2), ("Materials and equipment", 3), ("Procedure", 4),
                ("Observations and data", 0), ("Conclusion", 3)]
    y = 270
    for name, lines in sections:
        out.append(f'<rect x="50" y="{y - 22}" width="6" height="28" rx="3" fill="{acc}"/>'
                   + text(name, 66, y, 18, ink, "Bold", "start"))
        y += 22
        if lines == 0:  # tabel data
            cols, rows, tw = 4, 5, W - 100
            for r in range(rows + 1):
                out.append(f'<path d="M50 {y + r * 30}H{50 + tw}" stroke="#C9D1DA" stroke-width="1.4"/>')
            for c in range(cols + 1):
                out.append(f'<path d="M{50 + c * tw / cols} {y}V{y + rows * 30}" stroke="#C9D1DA" stroke-width="1.4"/>')
            out.append(f'<rect x="50" y="{y}" width="{tw}" height="30" fill="#EAF6F8"/>')
            for c, h in enumerate(("No.", "Observation", "Result", "Notes")):
                out.append(text(h, 50 + c * tw / cols + tw / cols / 2, y + 20, 13, sub, "SemiBold"))
            y += rows * 30 + 34
        else:
            for k in range(lines):
                out.append(f'<path d="M50 {y + 14 + k * 28}H{W - 50}" stroke="#C9D1DA" stroke-width="1.4"/>')
            y += lines * 28 + 34
    out.append(text("Teacher's signature: ____________________", W - 50, H - 40, 14, sub, "SemiBold", "end"))
    return W, H, "".join(out)


def bottle_labels():
    """Lembar 12 label botol bahan kimia (A4)."""
    W, H = 800, 1131
    ink = "#1E2A3A"
    cols_ = ["#E85D4A", "#F28C28", "#3FB6C4", "#5CBF7A", "#8E6CC9", "#3D7DDB"]
    out = [f'<rect x="-1" y="-1" width="{W + 2}" height="{H + 2}" fill="#FFFFFF"/>']
    m, cw, ch = 30, (800 - 60) / 2, (1131 - 60) / 6
    for i in range(12):
        x, y = m + (i % 2) * cw, m + (i // 2) * ch
        col = cols_[i % 6]
        out.append(f'<rect x="{x + 8}" y="{y + 8}" width="{cw - 16}" height="{ch - 16}" rx="14" fill="#FFFFFF" '
                   f'stroke="{col}" stroke-width="3"/>'
                   f'<rect x="{x + 8}" y="{y + 8}" width="{cw - 16}" height="36" rx="14" fill="{col}"/>'
                   f'<rect x="{x + 8}" y="{y + 30}" width="{cw - 16}" height="14" fill="{col}"/>')
        out.append(text("CHEMICAL", x + 24, y + 33, 15, "#FFFFFF", "Bold", "start"))
        out.append(icon("toxic-chemical-bottle", x + cw - 40, y + 26, 26, outline=True, ink="FFFFFF"))
        for k, lab in enumerate(("Name", "Formula", "Concentration", "Date")):
            yy = y + 72 + k * 24
            out.append(text(f"{lab}:", x + 24, yy, 12.5, ink, "SemiBold", "start"))
            out.append(f'<path d="M{x + 132} {yy + 3}H{x + cw - 24}" stroke="#C9D1DA" stroke-width="1.2"/>')
    return W, H, "".join(out)


def safety_sign(rule, desc, icon_id, color):
    """Rambu A4 satu aturan keselamatan: pita judul, ikon besar dalam lingkaran, teks besar."""
    W, H = 800, 1131
    ink = "#1E2A3A"
    out = [f'<rect x="-1" y="-1" width="{W + 2}" height="{H + 2}" fill="#FFFFFF"/>',
           f'<rect x="24" y="24" width="{W - 48}" height="{H - 48}" rx="28" fill="none" stroke="{color}" stroke-width="10"/>',
           f'<rect x="24" y="24" width="{W - 48}" height="150" rx="28" fill="{color}"/>',
           f'<rect x="24" y="120" width="{W - 48}" height="54" fill="{color}"/>',
           text("LAB SAFETY", W / 2, 120, 64, "#FFFFFF"),
           f'<circle cx="{W / 2}" cy="500" r="240" fill="#F2F6FA" stroke="{color}" stroke-width="12"/>',
           icon(icon_id, W / 2, 500, 330)]
    lines = wrap_words(tr(rule), 18)
    for k, line in enumerate(lines):
        out.append(text(line, W / 2, 860 + k * 70, 60, ink, "Bold"))
    dl = wrap_words(tr(desc), 34)
    for k, line in enumerate(dl):
        out.append(text(line, W / 2, 870 + len(lines) * 70 + k * 40, 30, "#5B6878", "SemiBold"))
    return W, H, "".join(out)


QUIZ = [
    ("What is the chemical symbol for gold?", "Au"), ("What is the common name of H₂O?", "Water"),
    ("Which gas do plants absorb for photosynthesis?", "Carbon dioxide"), ("What is the pH of pure water?", "7"),
    ("Which gas makes up most of the air?", "Nitrogen"), ("What is the symbol for sodium?", "Na"),
    ("What is the atomic number of carbon?", "6"), ("What is the lightest element?", "Hydrogen"),
    ("What is the formula of table salt?", "NaCl"), ("What is the charge of an electron?", "Negative"),
    ("Which noble gas is used in party balloons?", "Helium"), ("What is the symbol for iron?", "Fe"),
    ("What does a catalyst do?", "Speeds up a reaction"), ("Acid + base produces salt and...?", "Water"),
    ("Which state of matter has a fixed shape?", "Solid"), ("Which element has the symbol K?", "Potassium"),
]


def quiz_sheet(items, start, answers=False):
    """Lembar 8 kartu kuis (2x4); answers=True mencetak kunci jawaban."""
    W, H = 800, 1131
    ink = "#1E2A3A"
    m = 30
    cw, ch = (W - 2 * m) / 2, (H - 2 * m) / 4
    head = "#5CBF7A" if answers else "#8E6CC9"
    out = [f'<rect x="-1" y="-1" width="{W + 2}" height="{H + 2}" fill="#FFFFFF"/>']
    for i, (q, a) in enumerate(items):
        x = m + (i % 2) * cw
        y = m + (i // 2) * ch
        out.append(f'<rect x="{x + 10}" y="{y + 10}" width="{cw - 20}" height="{ch - 20}" rx="18" fill="#FFFFFF" '
                   f'stroke="{head}" stroke-width="3"/>'
                   f'<rect x="{x + 10}" y="{y + 10}" width="{cw - 20}" height="44" rx="18" fill="{head}"/>'
                   f'<rect x="{x + 10}" y="{y + 36}" width="{cw - 20}" height="18" fill="{head}"/>')
        label = tr("ANSWER") if answers else tr("QUESTION")
        out.append(text(f"{label} {start + i}", x + 30, y + 41, 17, "#FFFFFF", "Bold", "start"))
        out.append(icon("idea-bulb" if not answers else "chemistry-book", x + cw - 46, y + 32, 34))
        body = tr(a) if answers else tr(q)
        size = 26 if answers else 19
        lines = wrap_words(body, 24 if not answers else 18)
        for k, line in enumerate(lines):
            out.append(text(line, x + cw / 2, y + ch / 2 + 22 + (k - (len(lines) - 1) / 2) * size * 1.3, size,
                            ink, "Bold" if answers else "SemiBold"))
    dash = 'stroke="#9AA5B1" stroke-width="1.2" stroke-dasharray="6 6"'
    out.append(f'<path d="M{W / 2} {m}V{H - m}" {dash}/>')
    for k in range(1, 4):
        out.append(f'<path d="M{m} {m + k * ch}H{W - m}" {dash}/>')
    return W, H, "".join(out)


def wrap_words(s, n):
    lines, cur = [], ""
    for w_ in s.split():
        if len(cur) + len(w_) + 1 > n and cur:
            lines.append(cur)
            cur = w_
        else:
            cur = (cur + " " + w_).strip()
    return lines + [cur]


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
    "CHEMISTRY ELEMENT BINGO": "BINGO UNSUR KIMIA", "LAB SAFETY": "KESELAMATAN LAB", "QUESTION": "SOAL", "ANSWER": "JAWABAN",
    "What is the chemical symbol for gold?": "Apa lambang kimia emas?",
    "What is the common name of H₂O?": "Apa nama umum dari H₂O?",
    "Which gas do plants absorb for photosynthesis?": "Gas apa yang diserap tumbuhan untuk fotosintesis?",
    "What is the pH of pure water?": "Berapa pH air murni?",
    "Which gas makes up most of the air?": "Gas apa yang paling banyak di udara?",
    "What is the symbol for sodium?": "Apa lambang unsur natrium?",
    "What is the atomic number of carbon?": "Berapa nomor atom karbon?",
    "What is the lightest element?": "Unsur apa yang paling ringan?",
    "What is the formula of table salt?": "Apa rumus kimia garam dapur?",
    "What is the charge of an electron?": "Apa muatan elektron?",
    "Which noble gas is used in party balloons?": "Gas mulia apa yang dipakai untuk balon pesta?",
    "What is the symbol for iron?": "Apa lambang unsur besi?",
    "What does a catalyst do?": "Apa fungsi katalis?",
    "Acid + base produces salt and...?": "Asam + basa menghasilkan garam dan...?",
    "Which state of matter has a fixed shape?": "Wujud zat apa yang bentuknya tetap?",
    "Which element has the symbol K?": "Unsur apa yang lambangnya K?",
    "Negative": "Negatif", "Speeds up a reaction": "Mempercepat reaksi", "Solid": "Padat",
    "Potassium": "Kalium",
    "LAB REPORT": "LAPORAN PRAKTIKUM", "Chemistry practical": "Praktikum kimia", "Name:": "Nama:",
    "Class:": "Kelas:", "Date:": "Tanggal:", "Group:": "Kelompok:", "Title": "Judul", "Objective": "Tujuan",
    "Materials and equipment": "Alat dan bahan", "Procedure": "Langkah kerja",
    "Observations and data": "Data pengamatan", "Conclusion": "Kesimpulan", "No.": "No.",
    "Observation": "Pengamatan", "Result": "Hasil", "Notes": "Keterangan",
    "Teacher's signature: ____________________": "Paraf guru: ____________________",
    "CHEMICAL": "BAHAN KIMIA", "Formula:": "Rumus:", "Concentration:": "Konsentrasi:",
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
        for key, fn, title, kw in (
                ("lab-report-template", lab_report, "Chemistry lab report template",
                 ["lab report", "laboratory report", "template", "practical", "experiment", "worksheet", "form"]),
                ("chemical-bottle-labels", bottle_labels, "Chemical bottle labels sheet template",
                 ["labels", "bottle labels", "chemical labels", "stickers", "template", "laboratory", "storage"])):
            W, H, inner = fn()
            out.append(dict(
                name=f"{SET_ID}-{key}{sfx}", size=3508, png=False,
                svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * 3}" height="{H * 3}" viewBox="0 0 {W} {H}">{inner}</svg>',
                title=f"{title}{note}, printable A4 vector for chemistry class",
                keywords=kw_lang + kw + ["chemistry", "science", "school", "student", "teacher", "printable", "a4",
                                         "education", "classroom", "vector", "editable", "lab", "experiment"]))
        for k in range(2):
            for ans in (False, True):
                W, H, inner = quiz_sheet(QUIZ[k * 8:(k + 1) * 8], k * 8 + 1, ans)
                kind = "answers" if ans else "questions"
                out.append(dict(
                    name=f"{SET_ID}-quiz-cards-{k + 1}-{kind}{sfx}", size=3508, png=False,
                    svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * 3}" height="{H * 3}" viewBox="0 0 {W} {H}">{inner}</svg>',
                    title=f"Chemistry quiz cards sheet {k + 1} ({kind}){note}, printable A4 classroom trivia game",
                    keywords=kw_lang + ["quiz", "quiz cards", "trivia", "questions", "answers", "flashcards",
                                        "chemistry", "science", "game", "classroom", "printable", "school",
                                        "student", "teacher", "a4", "education", "learning", "review",
                                        "test", "vector"]))
        from posters2 import SAFETY
        sign_cols = ["#2E6FD8", "#2E6FD8", "#2E6FD8", "#E8A317", "#D93A2B", "#E8A317", "#2E6FD8", "#D93A2B",
                     "#1E9C6A", "#1E9C6A"]
        for k, (rule, desc, icon_id) in enumerate(SAFETY):
            W, H, inner = safety_sign(rule, desc, icon_id, sign_cols[k])
            slug = rule.lower().replace(" ", "-").replace("'", "")
            out.append(dict(
                name=f"{SET_ID}-safety-sign-{k + 1:02d}-{slug}{sfx}", size=3508, png=False,
                svg=f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * 3}" height="{H * 3}" viewBox="0 0 {W} {H}">{inner}</svg>',
                title=f"Laboratory safety sign: {rule.lower()}{note}, printable A4 chemistry lab poster vector",
                keywords=kw_lang + ["lab safety", "safety sign", "laboratory sign", "warning", "rules", "school lab",
                                    "chemistry", "science", "poster", "printable", "a4", "classroom", "safety",
                                    "ppe", "notice", "signage", "vector", "precaution", "education", "teacher"]))
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
