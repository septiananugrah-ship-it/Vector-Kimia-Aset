"""Poster edukasi kimia jilid 34: membaca meniskus dan alat ukur volume, serta langkah menyetarakan reaksi.
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
LIQ = "#7FB8E8"


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


def _cylinder_zoom(cx, cy, concave=True):
    """Tampilan dekat tabung ukur: garis skala, meniskus, dan mata pengamat sejajar."""
    w, h = 120, 220
    x0, y0 = cx - w / 2, cy - h / 2
    lvl = cy + 6
    d = 14 if concave else -14
    out = [f'<clipPath id="mz{int(cx)}"><rect x="{x0}" y="{y0}" width="{w}" height="{h}"/></clipPath>'
           f'<g clip-path="url(#mz{int(cx)})"><path d="M{x0} {lvl - d}Q{cx} {lvl + d} {x0 + w} {lvl - d}V{y0 + h}H{x0}Z" '
           f'fill="{LIQ if concave else "#B9C2CC"}"/></g>']
    out.append(f'<path d="M{x0} {y0}V{y0 + h}M{x0 + w} {y0}V{y0 + h}" stroke="{INK}" stroke-width="4"/>')
    for k in range(11):
        y = y0 + 10 + k * 20
        major = k % 5 == 0
        out.append(f'<path d="M{x0} {y}h{26 if major else 14}" stroke="{INK}" stroke-width="{2.5 if major else 1.6}"/>')
    out.append(text("50", x0 + 34, y0 + 15, 12, INK, "Bold", "start"))
    out.append(text("45", x0 + 34, y0 + 115, 12, INK, "Bold", "start"))
    # garis pandang
    ly = lvl  # titik terendah (cekung) / tertinggi (cembung) kurva Bezier kuadrat ada di lvl
    out.append(f'<path d="M{x0 - 70} {ly}H{x0 + w + 20}" stroke="#E8573F" stroke-width="2.5" stroke-dasharray="7 5"/>')
    ex = x0 - 86
    out.append(f'<path d="M{ex - 16} {ly}q16 -14 32 0q-16 14 -32 0z" fill="#FFFFFF" stroke="{INK}" stroke-width="2.5"/>'
               f'<circle cx="{ex}" cy="{ly}" r="5" fill="{INK}"/>')
    return "".join(out)


def meniscus(th):
    W = 1226
    top = 122
    H = top + 400 + 20 + 290 + 30
    out = [header(W, th, "READING A MENISCUS", "Read volumes at eye level for accurate measurements")]
    cw = (W - 2 * MX - 20) / 2
    for k, (title, desc, concave) in enumerate((
            ("Water: read the BOTTOM", "Water curves downward (concave); read the lowest point of the curve", True),
            ("Mercury: read the TOP", "Mercury curves upward (convex); read the highest point of the curve", False))):
        x = MX + k * (cw + 20)
        out.append(_card(x, top, cw, 400, th))
        out.append(text(title, x + cw / 2, top + 40, 19, th["ink"]))
        out.append(f'<rect x="{x + 20}" y="{top + 58}" width="{cw - 40}" height="260" rx="14" fill="{th["plate"]}"/>')
        out.append(_cylinder_zoom(x + cw / 2 + 40, top + 188, concave))
        for j, ln in enumerate(_wrap(desc, 15, cw - 50)):
            out.append(text(ln, x + cw / 2, top + 350 + j * 22, 15, th["sub"], "SemiBold"))
    y = top + 420
    out.append(_card(MX, y, W - 2 * MX, 290, th))
    out.append(text("Choosing the right tool", W / 2, y + 40, 18, th["ink"]))
    tools = [("Beaker", "± 5%", "Rough volumes only", R), ("Measuring cylinder", "± 0.5 mL", "Everyday measuring", O),
             ("Burette", "± 0.05 mL", "Titrations", P), ("Volumetric pipette", "± 0.02 mL", "Exact fixed volumes", T)]
    tw = (W - 2 * MX - 40 - 3 * 14) / 4
    for k, (name, acc, use, col) in enumerate(tools):
        tx = MX + 20 + k * (tw + 14)
        out.append(f'<rect x="{tx:.1f}" y="{y + 62}" width="{tw:.1f}" height="200" rx="14" '
                   f'fill="{mix(th["card"], col, .18)}"/>')
        out.append(f'<rect x="{tx:.1f}" y="{y + 62}" width="{tw:.1f}" height="8" rx="4" fill="{col}"/>')
        out.append(fit_text(name, tx + tw / 2, y + 108, 17, th["ink"], tw - 20))
        out.append(text(acc, tx + tw / 2, y + 162, 28, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3)))
        out.append(fit_text(use, tx + tw / 2, y + 214, 14, th["sub"], tw - 20, "SemiBold"))
    out.append(text("More accurate →", W - MX - 30, y + 40, 14, th["sub"], "Bold", "end"))
    return W, H, "".join(out)


STEPS = [
    ("Write the unbalanced equation", "Fe + O_{2} → Fe_{2}O_{3}"),
    ("Count atoms of each element on both sides", "Left: Fe = 1, O = 2 · Right: Fe = 2, O = 3"),
    ("Balance one element at a time with coefficients", "Fe + 3O_{2} → 2Fe_{2}O_{3}"),
    ("Balance the remaining elements", "4Fe + 3O_{2} → 2Fe_{2}O_{3}"),
    ("Check that every element is equal on both sides", "Fe: 4 = 4 · O: 6 = 6 ✓"),
]


def balancing(th):
    W = 1226
    top = 122
    rh = 96
    H = top + len(STEPS) * (rh + 14) + 20 + 150 + 30
    out = [header(W, th, "BALANCING CHEMICAL EQUATIONS", "Atoms are never created or destroyed in a reaction")]
    cols = [T, O, P, R, "#4BB04A"]
    for i, (step, ex) in enumerate(STEPS):
        y = top + i * (rh + 14)
        out.append(_card(MX, y, W - 2 * MX, rh, th))
        out.append(f'<circle cx="{MX + 46}" cy="{y + rh / 2}" r="24" fill="{cols[i]}"/>'
                   + text(str(i + 1), MX + 46, y + rh / 2 + 8, 22, "#FFFFFF"))
        out.append(fit_text(step, MX + 88, y + rh / 2 + 6, 18, th["ink"], 420, anchor="start"))
        bx = MX + 540
        bw = W - MX - 20 - bx
        out.append(f'<rect x="{bx}" y="{y + 16}" width="{bw}" height="{rh - 32}" rx="12" fill="{th["plate"]}"/>')
        out.append(chem(tr(ex), bx + bw / 2, y + rh / 2 + 8, 22, INK, "middle"))
    for i in range(len(STEPS) - 1):
        y = top + i * (rh + 14)
        out.append(arrow_line(MX + 46, y + rh / 2 + 26, MX + 46, y + rh + 14 + rh / 2 - 26, th["accent"], 3))
    y = top + len(STEPS) * (rh + 14) + 10
    out.append(_card(MX, y, W - 2 * MX, 150, th))
    out.append(text("Golden rules", W / 2, y + 38, 18, th["ink"]))
    rules = ["Change only the coefficients, never the subscripts", "Balance O and H last",
             "Use the smallest whole-number ratio"]
    rw = (W - 2 * MX - 40 - 2 * 14) / 3
    for k, r_ in enumerate(rules):
        rx = MX + 20 + k * (rw + 14)
        out.append(f'<rect x="{rx:.1f}" y="{y + 60}" width="{rw:.1f}" height="66" rx="12" '
                   f'fill="{mix(th["card"], th["accent"], .16)}"/>')
        out.append(fit_text(r_, rx + rw / 2, y + 99, 15, th["ink"], rw - 24, "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("reading-meniscus", meniscus, "Reading a meniscus chart, eye level, concave and convex, measuring tool accuracy",
     ["meniscus", "measuring cylinder", "volume", "measurement", "accuracy", "burette", "pipette", "beaker",
      "lab skills", "practical chemistry", "eye level", "graduated cylinder", "lab technique", "laboratory"]),
    ("balancing-equations", balancing, "Balancing chemical equations chart, step by step method with example",
     ["balancing equations", "chemical equation", "coefficients", "law of conservation of mass", "stoichiometry",
      "reaction", "atoms", "step by step", "iron oxide", "chemistry skills", "worksheet", "reactants", "products",
      "rusting"]),
]

TR.update({
    "READING A MENISCUS": "MEMBACA MENISKUS",
    "Read volumes at eye level for accurate measurements": "Baca volume sejajar mata agar pengukuran akurat",
    "Water: read the BOTTOM": "Air: baca bagian BAWAH", "Mercury: read the TOP": "Raksa: baca bagian ATAS",
    "Water curves downward (concave); read the lowest point of the curve":
        "Permukaan air melengkung ke bawah (cekung); baca titik terendah lengkungan",
    "Mercury curves upward (convex); read the highest point of the curve":
        "Permukaan raksa melengkung ke atas (cembung); baca titik tertinggi lengkungan",
    "Choosing the right tool": "Memilih alat yang tepat", "Beaker": "Gelas kimia",
    "Measuring cylinder": "Gelas ukur", "Burette": "Buret", "Volumetric pipette": "Pipet volume",
    "Rough volumes only": "Hanya untuk perkiraan", "Everyday measuring": "Pengukuran sehari-hari",
    "Titrations": "Titrasi", "± 0.5 mL": "± 0,5 mL", "± 0.05 mL": "± 0,05 mL", "± 0.02 mL": "± 0,02 mL", "Exact fixed volumes": "Volume tetap yang tepat", "More accurate →": "Makin akurat →",
    "BALANCING CHEMICAL EQUATIONS": "MENYETARAKAN PERSAMAAN REAKSI",
    "Atoms are never created or destroyed in a reaction": "Atom tidak pernah diciptakan atau dimusnahkan dalam reaksi",
    "Write the unbalanced equation": "Tulis persamaan yang belum setara",
    "Count atoms of each element on both sides": "Hitung atom tiap unsur di kedua ruas",
    "Balance one element at a time with coefficients": "Setarakan satu unsur demi satu dengan koefisien",
    "Balance the remaining elements": "Setarakan unsur yang tersisa",
    "Check that every element is equal on both sides": "Periksa jumlah setiap unsur sama di kedua ruas",
    "Left: Fe = 1, O = 2 · Right: Fe = 2, O = 3": "Kiri: Fe = 1, O = 2 · Kanan: Fe = 2, O = 3",
    "Golden rules": "Aturan emas",
    "Change only the coefficients, never the subscripts": "Ubah koefisien saja, jangan ubah indeks",
    "Balance O and H last": "Setarakan O dan H paling akhir",
    "Use the smallest whole-number ratio": "Gunakan perbandingan bilangan bulat terkecil",
})
