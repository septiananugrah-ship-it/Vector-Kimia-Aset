"""Poster edukasi kimia jilid 9: simbol titik Lewis unsur golongan utama periode 1-4.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
from periodic import CAT, ELEMENTS
from poster_i18n import TR
from poster_kit import header, text, tr
from textpath import width
from posters2 import _card

# (golongan utama 1..8, periode) -> nomor atom
MAIN = {1: (1, 3, 11, 19), 2: (None, 4, 12, 20), 3: (None, 5, 13, 31), 4: (None, 6, 14, 32),
        5: (None, 7, 15, 33), 6: (None, 8, 16, 34), 7: (None, 9, 17, 35), 8: (2, 10, 18, 36)}
GROUP_LABEL = {1: "1", 2: "2", 3: "13", 4: "14", 5: "15", 6: "16", 7: "17", 8: "18"}


def dots(cx, cy, n, rx, ry, col, pair_first=False):
    """Titik elektron valensi di empat sisi; diisi satu-satu dulu, lalu berpasangan
    (helium: satu pasangan)."""
    sides = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    count = [0, 0, 0, 0]
    order = [0, 0] if pair_first else [0, 1, 2, 3, 0, 1, 2, 3]
    for k in range(n):
        count[order[k]] += 1
    out = []
    for (dx, dy), c in zip(sides, count):
        if not c:
            continue
        bx, by = cx + dx * rx, cy + dy * ry
        offs = [0] if c == 1 else [-5.5, 5.5]
        for o in offs:
            x, y = (bx + o, by) if dy else (bx, by + o)
            out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.2" fill="{col}"/>')
    return "".join(out)


def lewis(th):
    W = 1226
    top = 150
    cw, ch, gap = 128, 128, 12
    x0 = (W - 8 * cw - 7 * gap) / 2 + 30
    H = top + 4 * (ch + gap) + 70
    out = [header(W, th, "LEWIS DOT SYMBOLS", "Valence electrons of the main-group elements in periods 1 to 4")]
    for g in range(1, 9):
        x = x0 + (g - 1) * (cw + gap)
        out.append(text(tr("Group") + " " + GROUP_LABEL[g], x + cw / 2, top - 22, 13, th["sub"], "SemiBold"))
    for p in range(4):
        out.append(text(str(p + 1), x0 - 30, top + p * (ch + gap) + ch / 2 + 6, 16, th["sub"], "Bold"))
        for g in range(1, 9):
            z = MAIN[g][p]
            if z is None:
                continue
            sym, name, _, cat = ELEMENTS[z - 1]
            col = CAT[cat][1]
            x = x0 + (g - 1) * (cw + gap)
            y = top + p * (ch + gap)
            out.append(_card(x, y, cw, ch, th, rx=14))
            out.append(f'<rect x="{x}" y="{y}" width="{cw}" height="7" rx="3.5" fill="{col}"/>')
            n = 2 if z == 2 else g
            cx, cy = x + cw / 2, y + ch / 2 + 2
            out.append(text(sym, cx, cy + 12, 34, th["ink"]))
            rx = max(30, width(sym, 34, "Bold") / 2 + 12)
            out.append(dots(cx, cy, n, rx, 33, th["accent"], pair_first=(z == 2)))
            out.append(text(str(z), x + 12, y + 24, 11, th["sub"], "SemiBold", "start"))
    out.append(text("Each dot is one valence electron · helium has 2, the other noble gases have 8",
                    W / 2, H - 26, 12.5, th["sub"], "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("lewis-dot-symbols", lewis, "Lewis dot symbols chart of main group elements, valence electrons",
     ["lewis dot", "lewis structure", "electron dot", "valence electrons", "main group elements", "periodic table",
      "octet rule", "chemical bonding", "elements", "group", "period", "noble gas", "dots", "electron"]),
]

TR.update({
    "LEWIS DOT SYMBOLS": "LAMBANG TITIK ELEKTRON LEWIS",
    "Valence electrons of the main-group elements in periods 1 to 4":
        "Elektron valensi unsur golongan utama periode 1 sampai 4",
    "Group": "Golongan",
    "Each dot is one valence electron · helium has 2, the other noble gases have 8":
        "Setiap titik = satu elektron valensi · helium memiliki 2, gas mulia lainnya 8",
})
