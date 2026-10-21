"""Set ubin unsur: 30 unsur populer sebagai ikon ubin tabel periodik, gaya semi-flat."""
from icons_lab_flat import solid
from periodic import CAT, ELEMENTS
from textpath import text

SET_ID = "element-tile-icons"
STROKE = 1.6
SHADOW = True
GLYPH = False
THEME = "chemical element tile"
PATTERNS = [("#16213A", "#FFC845", "element tiles on dark navy")]

SYMBOLS = ["H", "He", "Li", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
           "Ti", "Fe", "Ni", "Cu", "Zn", "Ag", "Sn", "Pt", "Au", "Hg", "Pb", "U"]

SET_TITLE = "Chemical element tiles icons set from the periodic table, 30 colorful vector symbols"
SET_KEYWORDS = [
    "periodic table", "chemical element", "element", "elements", "tile", "symbol", "atomic number", "atomic mass",
    "chemistry", "science", "education", "school", "icon set", "collection", "hydrogen", "oxygen", "carbon",
    "gold", "silver", "iron", "copper", "sodium", "metal", "nonmetal", "noble gas", "vector", "illustration",
    "isolated", "colorful", "flat",
]
COMMON_KEYWORDS = ["periodic table", "chemical element", "element", "tile", "symbol", "atomic number",
                   "atomic mass", "chemistry", "science", "education", "school", "icon", "vector", "illustration",
                   "isolated", "colorful", "flat", "sign"]


def tile(z, sym, name, mass, cat):
    col = CAT[cat][1]
    return (solid("M4 10a6 6 0 0 1 6-6h44a6 6 0 0 1 6 6v44a6 6 0 0 1-6 6H10a6 6 0 0 1-6-6z", col, 4, 60) +
            text(str(z), 10, 15, 8, "#1E2A3A", "SemiBold", "start") +
            text(sym, 32, 40, 24 if len(sym) == 1 else 21, "#1E2A3A") +
            text(name, 32, 50, 6.8 if len(name) < 10 else 6, "#1E2A3A", "SemiBold") +
            text(mass, 32, 56.5, 5, "#1E2A3A", "Regular"))


ICONS = []
for z, (sym, name, mass, cat) in enumerate(ELEMENTS, start=1):
    if sym not in SYMBOLS:
        continue
    kind = CAT[cat][0].lower().rstrip("s")
    ICONS.append({
        "id": f"{z:02d}-{name.lower()}",
        "title": f"{name} chemical element tile icon, {sym} atomic number {z}, periodic table vector",
        "keywords": [name.lower(), sym.lower(), f"{name.lower()} element", kind, f"atomic number {z}"],
        "body": tile(z, sym, name, mass, cat).replace("{p}", f"el{z}"),
    })
