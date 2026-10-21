"""Set stiker kawaii jilid 3: ikon konsep sains (icons_concepts) diberi wajah lucu
dan bingkai putih die-cut. Posisi wajah awal dihitung dari kotak pembatas ikon; FACES menimpa
posisi untuk ikon yang bentuknya tidak simetris.
"""
import icons_concepts
import kawaii
from kawaii import die_cut, face
from render import bbox

SET_ID = "kawaii-science-stickers"
STROKE = 1.6
SHADOW = False
PATTERNS = [("#EAFBF1", "#4BB04A", "cute pastel green"), ("#FFF9E0", "#E0B23A", "cute pastel yellow")]
THEME = "cute kawaii science"
COMMON_KEYWORDS = kawaii.COMMON_KEYWORDS

SET_TITLE = "Cute kawaii science stickers set, 17 happy chemistry and physics cartoon characters vector"
SET_KEYWORDS = [
    "kawaii", "cute", "sticker", "stickers", "character", "mascot", "happy", "smile", "face", "cartoon",
    "chemistry", "laboratory", "lab", "science", "kids", "children", "school", "education", "funny", "adorable",
    "atom", "dna", "battery", "magnet", "crystal", "water drop", "light bulb", "die cut", "printable",
    "clipart", "vector", "illustration", "isolated", "colorful", "planner", "emoji",
]

# (cx, cy, skala) dalam koordinat grid ikon asli; None = hitung otomatis
FACES = {
    "atom": (31, 29.7, .45), "molecule": (-8.7, -11.3, .35), "element-tile": (43, 16, .62), "lightning": (30.5, 37, .75),
    "ph-strip": (32, 9.5, .4),
}
SKIP = {"dna", "radioactive", "chemical-equation"}  # bentuknya tidak cocok diberi wajah
NAMES = {"element-tile": "element tile", "ph-strip": "ph strip", "idea-bulb": "light bulb",
         "chemistry-book": "chemistry book", "chemical-equation": "chemical equation"}


def _auto(body):
    x0, y0, x1, y1 = bbox(body, STROKE)
    w, h = x1 - x0, y1 - y0
    return (x0 + x1) / 2, y0 + h * .62, max(.45, min(1.1, min(w, h) / 30))


ICONS = []
for ic in icons_concepts.ICONS:
    if ic["id"] in SKIP:
        continue
    cx, cy, s = FACES.get(ic["id"]) or _auto(ic["body"])
    s *= 1.35
    name = NAMES.get(ic["id"], ic["id"].replace("-", " "))
    ICONS.append({
        "id": ic["id"],
        "title": f"Cute kawaii {name} sticker with happy face, science cartoon character vector",
        "keywords": [w for w in ic["keywords"] if w not in ("isolated",)][:6] + ["kawaii " + name],
        "body": die_cut(ic["body"]) + ic["body"] + face(cx, cy, s),
    })
