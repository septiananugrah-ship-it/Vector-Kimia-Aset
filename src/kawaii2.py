"""Set stiker kawaii jilid 2: alat & perlengkapan lab jilid 2 (icons_lab2) diberi wajah lucu
dan bingkai putih die-cut. Posisi wajah awal dihitung dari kotak pembatas ikon; FACES menimpa
posisi untuk ikon yang bentuknya tidak simetris.
"""
import icons_lab2
import kawaii
from kawaii import die_cut, face
from render import bbox

SET_ID = "kawaii-lab-stickers-2"
STROKE = 1.6
SHADOW = False
PATTERNS = [("#FFF7E6", "#F2A541", "cute pastel orange"), ("#F1ECFF", "#9B7FE0", "cute pastel purple")]
THEME = "cute kawaii chemistry lab"
COMMON_KEYWORDS = kawaii.COMMON_KEYWORDS

SET_TITLE = "Cute kawaii chemistry lab stickers set 2, 20 happy laboratory supplies cartoon characters vector"
SET_KEYWORDS = [
    "kawaii", "cute", "sticker", "stickers", "character", "mascot", "happy", "smile", "face", "cartoon",
    "chemistry", "laboratory", "lab", "science", "kids", "children", "school", "education", "funny", "adorable",
    "reagent bottle", "syringe", "lab coat", "gloves", "centrifuge", "fire extinguisher", "die cut", "printable",
    "clipart", "vector", "illustration", "isolated", "colorful", "planner", "emoji",
]

# (cx, cy, skala) dalam koordinat grid ikon asli; None = hitung otomatis
FACES = {
    "liebig-condenser": (33, 30, .55), "tripod-burner-beaker": (32, 15, .75), "syringe": (31, 30.5, .55),
    "lab-coat": (19, 46, .75), "centrifuge": (32, 18, .62), "magnetic-stirrer": (32, 19, .95),
    "spatula": (35, 28.5, .5), "magnifying-glass": (29.5, 26, 1.1), "toxic-chemical-bottle": (32, 23.5, .85),
    "fire-extinguisher": (32.5, 48, .72), "clipboard-notes": (32, 37.5, .68), "reaction-flask-smoke": (32, 47.5, .8),
}
NAMES = {"tripod-burner-beaker": "beaker on tripod", "watch-glass-crystals": "watch glass",
         "toxic-chemical-bottle": "hazard bottle", "clipboard-notes": "clipboard",
         "reaction-flask-smoke": "smoking flask", "liebig-condenser": "condenser"}


def _auto(body):
    x0, y0, x1, y1 = bbox(body, STROKE)
    w, h = x1 - x0, y1 - y0
    return (x0 + x1) / 2, y0 + h * .62, max(.45, min(1.1, min(w, h) / 30))


ICONS = []
for ic in icons_lab2.ICONS:
    cx, cy, s = FACES.get(ic["id"]) or _auto(ic["body"])
    s *= 1.35
    name = NAMES.get(ic["id"], ic["id"].replace("-", " "))
    ICONS.append({
        "id": ic["id"],
        "title": f"Cute kawaii {name} sticker with happy face, chemistry lab cartoon character vector",
        "keywords": [w for w in ic["keywords"] if w not in ("isolated",)][:6] + ["kawaii " + name],
        "body": die_cut(ic["body"]) + ic["body"] + face(cx, cy, s),
    })
