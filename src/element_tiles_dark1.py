"""Set ubin unsur tema gelap jilid 1 (Z 1–40): ubin navy dengan bingkai dan nomor berwarna kategori."""
import element_tiles as base
from element_tiles_dark import dark_tile
from periodic import CAT, ELEMENTS

SET_ID = "element-tile-dark-icons-1"
STROKE, THEME = base.STROKE, "dark chemical element tile"
SET_KEYWORDS = base.SET_KEYWORDS + ["dark", "navy", "dark mode"]
COMMON_KEYWORDS = base.COMMON_KEYWORDS + ["dark", "navy"]
SHADOW = True
GLYPH = False
LO, HI = 1, 40

ICONS = []
for z, (sym, name, mass, cat) in enumerate(ELEMENTS, start=1):
    if not LO <= z <= HI:
        continue
    kind = CAT[cat][0].lower().rstrip("s")
    ICONS.append({
        "id": f"{z:03d}-{name.lower()}",
        "title": f"{name} chemical element tile icon in dark style, {sym} atomic number {z}, periodic table vector",
        "keywords": [name.lower(), sym.lower(), f"{name.lower()} element", kind, f"atomic number {z}"],
        "body": dark_tile(z, sym, name, mass, cat),
    })
SET_TITLE = (f"Dark chemical element tiles icons set, atomic numbers {LO} to {HI}, {len(ICONS)} periodic table "
             "vector symbols on navy")
