"""Set ubin unsur jilid 4: unsur Z 89–118 yang belum ada di element_tiles, gaya semi-flat yang sama."""
import element_tiles as base
from element_tiles import SYMBOLS, tile
from periodic import CAT, ELEMENTS

SET_ID = "element-tile-icons-4"
STROKE, THEME = base.STROKE, base.THEME
SET_KEYWORDS, COMMON_KEYWORDS = base.SET_KEYWORDS, base.COMMON_KEYWORDS
SHADOW = True
GLYPH = False
LO, HI = 89, 118

ICONS = []
for z, (sym, name, mass, cat) in enumerate(ELEMENTS, start=1):
    if not LO <= z <= HI or sym in SYMBOLS:
        continue
    kind = CAT[cat][0].lower().rstrip("s")
    ICONS.append({
        "id": f"{z:03d}-{name.lower()}",
        "title": f"{name} chemical element tile icon, {sym} atomic number {z}, periodic table vector",
        "keywords": [name.lower(), sym.lower(), f"{name.lower()} element", kind, f"atomic number {z}"],
        "body": tile(z, sym, name, mass, cat).replace("{p}", f"el{z}"),
    })
SET_TITLE = (f"Chemical element tiles icons set, atomic numbers {LO} to {HI}, {len(ICONS)} colorful periodic "
             "table vector symbols")
