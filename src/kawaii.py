"""Set stiker kawaii: alat lab set 02 diberi wajah lucu dan bingkai putih die-cut.

Posisi wajah (cx, cy, skala) ditulis dalam koordinat grid ikon aslinya.
"""
import re

import icons_lab_flat

SET_ID = "kawaii-lab-stickers"
STROKE = 1.6
SHADOW = False
PATTERNS = [("#FFF1F5", "#F28CA8", "cute pastel pink"), ("#EAF7FF", "#3FB6C4", "cute pastel blue")]
THEME = "cute kawaii chemistry lab"

SET_TITLE = "Cute kawaii chemistry laboratory stickers set, 20 happy lab equipment cartoon characters vector"
SET_KEYWORDS = [
    "kawaii", "cute", "sticker", "stickers", "character", "mascot", "happy", "smile", "face", "cartoon",
    "chemistry", "laboratory", "lab", "science", "kids", "children", "school", "education", "funny", "adorable",
    "flask", "beaker", "test tube", "microscope", "planner", "journal", "die cut", "printable", "clipart",
    "vector", "illustration", "isolated", "colorful", "doodle", "emoji",
]
COMMON_KEYWORDS = ["kawaii", "cute", "sticker", "character", "happy", "smile", "cartoon", "chemistry",
                   "laboratory", "science", "kids", "school", "funny", "adorable", "clipart", "vector",
                   "illustration", "isolated", "die cut", "mascot"]

FACES = {
    "erlenmeyer-flask": (32, 47, 1), "beaker": (32, 42, 1.1), "test-tube": (32, 42, .7),
    "test-tube-rack": (32, 25, .5), "round-bottom-flask": (32, 43, 1), "volumetric-flask": (32, 51, .9),
    "microscope": (26, 19.5, .5), "bunsen-burner": (32, 37, .5), "pipette": (32, 34, .65),
    "dropper": (32, 13, .55), "graduated-cylinder": (32, 41, .75), "petri-dish": (32, 31, .75),
    "funnel": (32, 19, .75), "mortar-and-pestle": (30, 37, .9), "thermometer": (32, 50.5, .6),
    "burette-stand": (44, 33, .38), "safety-goggles": (32, 37, .6), "retort": (20, 30, .75),
    "laboratory-scale": (22, 51, .55), "wash-bottle": (32, 48, .8),
}
NAMES = {"mortar-and-pestle": "mortar and pestle", "laboratory-scale": "lab scale", "burette-stand": "burette"}


def face(cx, cy, s):
    ink = "#1E2A3A"
    out = []
    for dx in (-5, 5):
        out.append(f'<ellipse cx="{cx + dx * s * 1.6:.2f}" cy="{cy + 3.2 * s:.2f}" rx="{2.3 * s:.2f}" '
                   f'ry="{1.3 * s:.2f}" fill="#F7A1B5" stroke="none"/>')
        out.append(f'<circle cx="{cx + dx * s:.2f}" cy="{cy - 1.5 * s:.2f}" r="{1.9 * s:.2f}" fill="{ink}" '
                   'stroke="none"/>')
        out.append(f'<circle cx="{cx + dx * s + .6 * s:.2f}" cy="{cy - 2.2 * s:.2f}" r="{.65 * s:.2f}" '
                   'fill="#FFFFFF" stroke="none"/>')
    out.append(f'<path d="M{cx - 2.6 * s:.2f} {cy + 1.6 * s:.2f}q{2.6 * s:.2f} {2.8 * s:.2f} {5.2 * s:.2f} 0" '
               f'stroke="{ink}" stroke-width="{1.3 * s:.2f}" fill="none" stroke-linecap="round"/>')
    return "".join(out)


def die_cut(body, width=7):
    """Bingkai stiker: salinan bentuk berwarna putih bergaris tebal + bayangan tipis di belakang."""
    # buang isian yang terpotong clipPath (cairan, bayangan): bentuk luarnya sudah cukup
    flat = re.sub(r'<clipPath[^>]*>.*?</clipPath>', "", body)
    flat = re.sub(r'<g clip-path="url\(#[^)]+\)"[^>]*>.*?</g>', "", flat)
    flat = re.sub(r'<rect[^>]*clip-path="url\(#[^)]+\)"[^>]*/>', "", flat)
    flat = re.sub(r'(fill|stroke)="#[0-9A-Fa-f]{6}"', r'\1="#FFFFFF"', flat)
    flat = re.sub(r'stroke-width="[0-9.]+"', f'stroke-width="{width}"', flat)
    flat = flat.replace('stroke="none"', 'stroke="#FFFFFF"')
    shadow = flat.replace("#FFFFFF", "#D5DCE4")
    return (f'<g stroke-width="{width}" stroke="#D5DCE4" transform="translate(.8 1.4)">{shadow}</g>'
            f'<g stroke-width="{width}" stroke="#FFFFFF">{flat}</g>')


ICONS = []
for ic in icons_lab_flat.ICONS:
    cx, cy, s = FACES[ic["id"]]
    s *= 1.35
    name = NAMES.get(ic["id"], ic["id"].replace("-", " "))
    body = ic["body"] + face(cx, cy, s)
    ICONS.append({
        "id": ic["id"],
        "title": f"Cute kawaii {name} sticker with happy face, chemistry lab cartoon character vector",
        "keywords": [w for w in ic["keywords"] if w not in ("isolated",)][:6] + ["kawaii " + name],
        "body": die_cut(ic["body"]) + body,
        "plain": ic["body"], "face": face(cx, cy, s),  # dipakai lembar mewarnai
    })
