"""Set 03: 20 ikon alat & perlengkapan laboratorium jilid 2, gaya semi-flat.

Memakai palet dan pembantu gambar yang sama dengan set 02 (icons_lab_flat).
"""
from icons_lab_flat import G, L, M, N, O, P, R, T, W, Y, bubbles, light, solid, vessel

SET_ID = "lab2-flat-icons"
STROKE = 1.6
SHADOW = True
GLYPH = True
THEME = "chemistry laboratory tools"
PATTERNS = [("#FFF8EC", "#E85D4A", "colorful laboratory on cream"),
            ("#2B2F4A", "#3FB6C4", "colorful laboratory on dark indigo")]

SET_TITLE = "Chemistry laboratory tools and safety equipment icons set, 20 colorful cartoon vector clipart"
SET_KEYWORDS = [
    "icon set", "collection", "clipart", "flat", "colorful", "cartoon", "vector",
    "chemistry", "laboratory", "lab", "science", "equipment", "tools", "safety",
    "glassware", "research", "experiment", "education", "school", "pharmacy",
    "medical", "chemical", "bottle", "reagent", "syringe", "lab coat", "gloves",
    "centrifuge", "condenser", "crucible", "burner", "isolated", "illustration",
    "sticker", "element", "design",
]
COMMON_KEYWORDS = [
    "icon", "flat", "colorful", "cartoon", "clipart", "vector", "illustration",
    "chemistry", "laboratory", "lab", "science", "scientific", "equipment",
    "research", "experiment", "education", "school", "chemical", "isolated",
    "sticker", "element", "graphic", "design", "symbol",
]

WOOD = "#C98B4E"


def flame(cx, top, h):
    """Nyala api oranye-kuning, ujung di `top`, tinggi `h`."""
    w = h * 0.45
    return (f'<path d="M{cx} {top}c{w * .7:.2f} {h * .3:.2f} {w:.2f} {h * .5:.2f} {w:.2f} {h * .68:.2f}'
            f'a{w:.2f} {w:.2f} 0 0 1-{2 * w:.2f} 0c0-{h * .18:.2f} {w * .3:.2f}-{h * .38:.2f} {w:.2f}-{h * .68:.2f}z" fill="{O}"/>'
            f'<path d="M{cx} {top + h * .42:.2f}c{w * .35:.2f} {h * .15:.2f} {w * .5:.2f} {h * .25:.2f} {w * .5:.2f} {h * .34:.2f}'
            f'a{w * .5:.2f} {w * .5:.2f} 0 0 1-{w:.2f} 0c0-{h * .09:.2f} {w * .15:.2f}-{h * .19:.2f} {w * .5:.2f}-{h * .34:.2f}z" '
            f'fill="{Y}" stroke="none"/>')


ICONS = [
    {
        "id": "reagent-bottle",
        "title": "Brown reagent bottle with label icon, chemistry cartoon clipart vector",
        "keywords": ["reagent bottle", "bottle", "chemical bottle", "amber", "label", "storage", "solution"],
        "body": solid("M25 6h14v12H25z", N, 25, 39) +
                vessel("M17 26a8 8 0 0 1 8-8h14a8 8 0 0 1 8 8v30a4 4 0 0 1-4 4H21a4 4 0 0 1-4-4z",
                       (17, 18, 47, 60), 30, "#B5651D") +
                f'<path d="M22 36h20v14H22z" fill="{W}"/><path d="M26 41h12M26 45h8" stroke="{M}"/>',
    },
    {
        "id": "dropper-bottle",
        "title": "Dropper bottle with purple serum icon, chemistry cartoon clipart vector",
        "keywords": ["dropper bottle", "serum", "dropper", "bottle", "essential oil", "drops", "purple"],
        "body": solid("M27 18v-7a5 5 0 0 1 10 0v7z", R, 27, 37) +
                solid("M24 18h16v8H24z", N, 24, 40) +
                vessel("M18 32a6 6 0 0 1 6-6h16a6 6 0 0 1 6 6v24a4 4 0 0 1-4 4H22a4 4 0 0 1-4-4z",
                       (18, 26, 46, 60), 36, P, bubbles((27, 48, 2), (36, 52, 1.3))),
    },
    {
        "id": "separatory-funnel",
        "title": "Separatory funnel with two liquid layers icon, chemistry cartoon clipart vector",
        "keywords": ["separatory funnel", "separation", "extraction", "layers", "funnel", "glassware", "liquid"],
        "body": solid("M28 0h8v5h-8z", N, 28, 36) +
                vessel("M29 5h6v6c8 4 13 11 13 19 0 6-6 10-13 12v10h-6V42c-7-2-13-6-13-12 0-8 5-15 13-19z",
                       (16, 5, 48, 52), 20, Y,
                       f'<rect x="-10" y="31" width="84" height="40" fill="{T}"/>'
                       f'<rect x="38.5" y="31" width="40" height="40" fill="#35999F"/>'
                       f'<rect x="-10" y="31" width="84" height="1.4" fill="{light(T)}"/>') +
                solid("M23 47h18v4H23z", N, 23, 41) + '<path d="M32 52v8"/>',
    },
    {
        "id": "liebig-condenser",
        "title": "Liebig condenser with cooling water icon, distillation chemistry cartoon clipart vector",
        "keywords": ["condenser", "liebig condenser", "distillation", "cooling", "glassware", "water jacket", "reflux"],
        "body": '<g transform="rotate(-35 32 32)">' +
                solid("M14 38h5v8h-5z", G, 14, 19) + solid("M45 18h5v8h-5z", G, 45, 50) +
                vessel("M8 26h48v12H8z", (8, 26, 56, 38), 29, T) +
                '<path d="M-2 32h66" stroke-width="2.6"/></g>',
    },
    {
        "id": "crucible",
        "title": "Porcelain crucible with lid icon, chemistry cartoon clipart vector",
        "keywords": ["crucible", "porcelain", "lid", "heating", "melting", "ceramic", "furnace"],
        "body": solid("M14 26h36l-4 28a5 5 0 0 1-5 4H23a5 5 0 0 1-5-4z", W, 14, 50) +
                '<path d="M18 34h28"/>' +
                solid("M10 18h44v6H10z", W, 10, 54) + solid("M27 11h10v7H27z", N, 27, 37),
    },
    {
        "id": "tripod-burner-beaker",
        "title": "Beaker heated on tripod with burner flame icon, chemistry experiment cartoon clipart vector",
        "keywords": ["tripod", "wire gauze", "heating", "burner", "flame", "beaker", "boiling"],
        "body": vessel("M20 4v16a4 4 0 0 0 4 4h16a4 4 0 0 0 4-4V4z", (20, 4, 44, 24), 11, T,
                       bubbles((27, 17, 1.6), (34, 14, 1.2), (37, 19, 1.4))) +
                '<path d="M18 4h28"/>' +
                solid("M8 24h48v4H8z", M, 8, 56) +
                solid("M13 28h5l-5 30H8z", N, 8, 18) + solid("M46 28h5l5 30h-5z", N, 46, 56) +
                flame(32, 38, 20),
    },
    {
        "id": "spirit-lamp",
        "title": "Alcohol spirit lamp with flame icon, chemistry cartoon clipart vector",
        "keywords": ["spirit lamp", "alcohol lamp", "burner", "flame", "fire", "heating", "wick"],
        "body": flame(32, 2, 18) + '<path d="M32 19v3"/>' +
                solid("M27 22h10v8H27z", N, 27, 37) +
                vessel("M10 46c0-10 9-16 22-16s22 6 22 16v8a4 4 0 0 1-4 4H14a4 4 0 0 1-4-4z",
                       (10, 30, 54, 58), 44, P),
    },
    {
        "id": "syringe",
        "title": "Syringe with blue liquid icon, laboratory and medical cartoon clipart vector",
        "keywords": ["syringe", "injection", "needle", "vaccine", "medical", "dose", "medicine"],
        "body": '<g transform="rotate(-40 32 32)">' +
                '<path d="M-10 32h14" stroke-width="2"/>' + solid("M4 29h6v6H4z", N, 4, 10) +
                vessel("M10 25h32v14H10z", (10, 25, 42, 39), 80, T,
                       f'<rect x="10" y="20" width="18" height="30" fill="{T}"/>'
                       f'<rect x="10" y="33" width="18" height="10" fill="#35999F"/>') +
                '<path d="M15 25v5M20 25v4M25 25v5M30 25v4M35 25v5"/>' +
                solid("M28 25h4v14h-4z", N, 28, 32) +
                solid("M32 30h20v4H32z", M, 32, 52) + solid("M42 20h3v24h-3z", N, 42, 45) +
                solid("M52 23h4v18h-4z", N, 52, 56) + "</g>",
    },
    {
        "id": "lab-coat",
        "title": "White laboratory coat icon, scientist uniform cartoon clipart vector",
        "keywords": ["lab coat", "coat", "uniform", "scientist", "doctor", "white coat", "clothing"],
        "body": solid("M21 5l11 7 11-7 12 6 7 25h-9l-2-8v32H13V28l-2 8H2l7-25z", W, 2, 62) +
                f'<path d="M21 5l11 15 11-15" fill="{T}"/>'
                '<path d="M32 20v40M40 40h9"/>' +
                f'<circle cx="35" cy="28" r="1.4" fill="{N}"/><circle cx="35" cy="36" r="1.4" fill="{N}"/>'
                f'<circle cx="35" cy="44" r="1.4" fill="{N}"/>' +
                f'<path d="M17 18l4-1 1 5-4 1z" fill="{R}"/>',
    },
    {
        "id": "protective-gloves",
        "title": "Blue nitrile protective glove icon, laboratory safety cartoon clipart vector",
        "keywords": ["gloves", "glove", "nitrile", "latex", "protection", "safety", "ppe"],
        "body": solid("M18 52V34l-6-11a3.2 3.2 0 0 1 5.4-3.4L24 28V10a3 3 0 0 1 6 0v14V7a3 3 0 0 1 6 0v17"
                      "V10a3 3 0 0 1 6 0v16V15a3 3 0 0 1 6 0v23c0 7-3 11-6 14z", T, 12, 48) +
                '<path d="M30 24v-4M36 24v-4M42 26v-4"/>' +
                solid("M16 51h28v9H16z", "#2E8F9A", 16, 44),
    },
    {
        "id": "centrifuge",
        "title": "Laboratory centrifuge machine icon, science cartoon clipart vector",
        "keywords": ["centrifuge", "machine", "rotor", "spin", "sample", "blood test", "biotechnology"],
        "body": solid("M10 22a22 12 0 0 1 44 0z", T, 10, 54) +
                f'<path d="M20 16c3-3 7-4 11-4.5" stroke="{W}"/>' +
                solid("M6 22h52v30a6 6 0 0 1-6 6H12a6 6 0 0 1-6-6z", M, 6, 58) +
                solid("M12 30h22v12H12z", N, 12, 34) +
                f'<path d="M16 36h8" stroke="{L}"/><path d="M27 36h3" stroke="{Y}"/>' +
                f'<circle cx="43" cy="36" r="4" fill="{O}"/><circle cx="52" cy="36" r="2.4" fill="{R}"/>'
                '<path d="M12 50h40"/>',
    },
    {
        "id": "magnetic-stirrer",
        "title": "Magnetic stirrer hot plate with beaker icon, chemistry cartoon clipart vector",
        "keywords": ["magnetic stirrer", "hot plate", "stirring", "heating", "beaker", "mixing", "device"],
        "body": vessel("M18 8v24a4 4 0 0 0 4 4h20a4 4 0 0 0 4-4V8z", (18, 8, 46, 36), 18, R,
                       f'<path d="M24 22c3 2 13 2 16 0" stroke="{light(R)}" stroke-width="1.4" fill="none"/>'
                       f'<rect x="27" y="30" width="10" height="3.4" rx="1.7" fill="{W}"/>') +
                '<path d="M16 8h32"/>' +
                solid("M10 36h44v4H10z", N, 10, 54) +
                solid("M6 40h52v18H6z", M, 6, 58) +
                f'<circle cx="18" cy="49" r="4.2" fill="{O}"/><circle cx="46" cy="49" r="4.2" fill="{T}"/>'
                f'<path d="M27 47h10v4H27z" fill="{N}"/>',
    },
    {
        "id": "watch-glass-crystals",
        "title": "Watch glass with purple crystals icon, chemistry cartoon clipart vector",
        "keywords": ["watch glass", "crystals", "crystal", "sample", "evaporation", "mineral", "salt"],
        "body": f'<path d="M20 34l5-10 5 4 2 6z" fill="{P}"/><path d="M29 34l6-14 6 8 1 6z" fill="{light(P, .25)}"/>'
                f'<path d="M38 34l4-8 5 8z" fill="{P}"/>' +
                vessel("M4 34c4 11 14 16 28 16s24-5 28-16z", (4, 34, 60, 50), 80, T),
    },
    {
        "id": "spatula",
        "title": "Laboratory spatula with powder icon, chemistry cartoon clipart vector",
        "keywords": ["spatula", "scoop", "powder", "sample", "weighing", "metal", "tool"],
        "body": '<g transform="rotate(-35 32 32)">' +
                solid("M14 30h36v4H14z", M, 14, 50) + solid("M24 28.5h16v7H24z", O, 24, 40) +
                solid("M1 32a8 6.5 0 1 0 16 0a8 6.5 0 1 0-16 0z", M, 1, 17) +
                f'<path d="M4 31c2-4 8-4 10 0z" fill="{W}"/>' +
                solid("M50 28h10a4 4 0 0 1 0 8H50z", M, 50, 64) + "</g>",
    },
    {
        "id": "magnifying-glass",
        "title": "Magnifying glass icon, science research cartoon clipart vector",
        "keywords": ["magnifying glass", "magnifier", "lens", "search", "zoom", "investigation", "inspect"],
        "body": solid("M39 41l5-5 17 17a3.5 3.5 0 0 1-5 5z", N, 39, 61) +
                solid("M8 26a18 18 0 1 0 36 0a18 18 0 1 0-36 0z", O, 8, 44) +
                vessel("M13 26a13 13 0 1 0 26 0a13 13 0 1 0-26 0z", (13, 13, 39, 39), 80, T),
    },
    {
        "id": "toxic-chemical-bottle",
        "title": "Chemical bottle with hazard warning label icon, toxic substance cartoon clipart vector",
        "keywords": ["hazard", "warning", "toxic", "dangerous", "chemical bottle", "caution", "poison"],
        "body": solid("M26 6h12v8H26z", N, 26, 38) +
                vessel("M28 14v6c-8 3-12 9-12 16v18a4 4 0 0 0 4 4h24a4 4 0 0 0 4-4V36c0-7-4-13-12-16v-6z",
                       (16, 14, 48, 58), 34, L) +
                f'<path d="M32 33l10 17H22z" fill="{Y}"/><path d="M32 39v5"/>'
                f'<circle cx="32" cy="47" r="1" fill="{N}"/>',
    },
    {
        "id": "gas-cylinder",
        "title": "Compressed gas cylinder icon, laboratory cartoon clipart vector",
        "keywords": ["gas cylinder", "gas tank", "oxygen", "nitrogen", "compressed gas", "tank", "pressure"],
        "body": solid("M28 2h8v8h-8z", N, 28, 36) + '<path d="M28 6h-6M22 3v6"/>' +
                solid("M27 10h10v5H27z", M, 27, 37) +
                solid("M20 22a12 8 0 0 1 24 0v34a4 4 0 0 1-4 4H24a4 4 0 0 1-4-4z", L, 20, 44) +
                f'<path d="M20 28h24v8H20z" fill="{W}"/><path d="M25 32h10" stroke="{M}"/>'
                f'<path d="M24 20c2-3 4-4 7-4.5" stroke="{W}"/>',
    },
    {
        "id": "fire-extinguisher",
        "title": "Red fire extinguisher icon, laboratory safety cartoon clipart vector",
        "keywords": ["fire extinguisher", "extinguisher", "fire safety", "emergency", "safety", "red", "protection"],
        "body": '<path d="M28 10c-9 0-14 6-14 14v14" stroke-width="2.6"/>' +
                solid("M12 37h5v6h-5z", N, 12, 17) +
                solid("M33 6h12l-2 4H33z", N, 33, 45) + solid("M27 4h8v10h-8z", N, 27, 35) +
                solid("M22 22a8 8 0 0 1 8-8h2a8 8 0 0 1 8 8v34a4 4 0 0 1-4 4H26a4 4 0 0 1-4-4z", R, 22, 40) +
                f'<path d="M22 32h18v12H22z" fill="{W}"/><path d="M26 38h10" stroke="{R}"/>',
    },
    {
        "id": "clipboard-notes",
        "title": "Clipboard with chemistry notes icon, laboratory report cartoon clipart vector",
        "keywords": ["clipboard", "notes", "report", "checklist", "lab report", "document", "formula"],
        "body": solid("M10 8h44v54H10z", WOOD, 10, 54) +
                f'<path d="M15 14h34v43H15z" fill="{W}"/>' +
                solid("M23 3h18v9H23z", N, 23, 41) +
                f'<path d="M26 22l6-3.5 6 3.5v7l-6 3.5-6-3.5z" stroke="{T}"/>'
                f'<circle cx="32" cy="25.5" r="2.4" stroke="{T}"/>'
                '<path d="M20 40h24M20 46h24M20 52h14"/>',
    },
    {
        "id": "reaction-flask-smoke",
        "title": "Chemical reaction flask with smoke icon, chemistry experiment cartoon clipart vector",
        "keywords": ["chemical reaction", "smoke", "vapor", "fumes", "flask", "experiment", "potion"],
        "body": f'<path d="M24 14a6 6 0 0 1 4-9 7 7 0 0 1 12 0 6 6 0 0 1 2 10z" fill="{M}"/>'
                f'<path d="M31 8a4 4 0 0 1 5-1" stroke="{W}"/>' +
                vessel("M28 17v11L15 53a4 4 0 0 0 3.6 5.8h26.8A4 4 0 0 0 49 53L36 28V17z",
                       (15, 17, 49, 59), 40, L, bubbles((28, 50, 2.4), (36, 46, 1.6), (32, 54, 1.2))) +
                solid("M25 14h14v4H25z", G, 25, 39),
    },
]

for _ic in ICONS:
    _ic["body"] = _ic["body"].replace("{p}", _ic["id"])
