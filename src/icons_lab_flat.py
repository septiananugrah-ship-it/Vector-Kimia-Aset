"""Set 02: 20 ikon alat laboratorium, gaya semi-flat berwarna.

Grid 64x64. Garis tepi (stroke) tipis diterapkan oleh build.py; build.py juga
menskalakan tiap ikon agar mengisi bingkai dan menambah bayangan di bawahnya.
Kedalaman dibuat dengan warna dua tone (sisi kanan lebih gelap), kilau kaca
dan permukaan cairan, tanpa gradien/transparansi agar aman untuk EPS 10.
`{p}` diganti id ikon supaya id clipPath unik.
"""

SET_ID = "lab-flat-icons"
STROKE = 1.6
SHADOW = True
GLYPH = True
THEME = "chemistry laboratory equipment"
# (latar, warna aksen, suasana) untuk pola seamless
PATTERNS = [("#FFFFFF", "#3FB6C4", "colorful science on white"),
            ("#1E2A3A", "#FFC845", "colorful science on dark navy"),
            ("#E6F6F8", "#F28C28", "colorful science on light blue")]
SET_TITLE = "Colorful chemistry laboratory equipment icons set, 20 cartoon vector clipart"
SET_KEYWORDS = [
    "icon set", "collection", "clipart", "flat", "colorful", "cartoon",
    "vector", "chemistry", "laboratory", "lab", "science", "scientific",
    "equipment", "glassware", "research", "experiment", "education",
    "school", "kids", "biology", "pharmacy", "medical", "chemical",
    "flask", "beaker", "test tube", "microscope", "pipette", "burner",
    "thermometer", "petri dish", "funnel", "potion", "liquid", "isolated",
    "illustration", "sticker", "element", "design", "graphic",
]

COMMON_KEYWORDS = [
    "icon", "flat", "colorful", "cartoon", "clipart", "vector", "illustration",
    "chemistry", "laboratory", "lab", "science", "scientific", "equipment",
    "research", "experiment", "education", "school", "chemical", "liquid",
    "isolated", "sticker", "element", "graphic", "design", "symbol",
]

N = "#2B3A4E"   # gelap
G = "#DDF3F6"   # kaca
T = "#3FB6C4"   # tosca
O = "#F28C28"   # oranye
Y = "#FFC845"   # kuning
P = "#8E6CC9"   # ungu
R = "#E85D4A"   # merah
L = "#5CBF7A"   # hijau
M = "#C9D1DA"   # logam
W = "#FFFFFF"

_uid = [0]


def _mix(c, other, f):
    a = [int(c[i:i + 2], 16) for i in (1, 3, 5)]
    b = [int(other[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x + (y - x) * f):02X}" for x, y in zip(a, b))


def dark(c, f=0.22):
    return _mix(c, "#000000", f)


def light(c, f=0.45):
    return _mix(c, "#FFFFFF", f)


def _cid():
    _uid[0] += 1
    return f"{{p}}-c{_uid[0]}"


def solid(shape, color, x0, x1):
    """Bentuk padat dua tone: sepertiga kanan lebih gelap."""
    cid = _cid()
    xs = x0 + (x1 - x0) * 0.64
    return (f'<clipPath id="{cid}"><path d="{shape}"/></clipPath>'
            f'<path d="{shape}" fill="{color}" stroke="none"/>'
            f'<rect x="{xs:.2f}" y="-10" width="84" height="84" fill="{dark(color, .14)}" '
            f'stroke="none" clip-path="url(#{cid})"/>'
            f'<path d="{shape}"/>')


def vessel(shape, box, top, liquid, extra=""):
    """Wadah kaca berisi cairan: dua tone, permukaan cairan, kilau."""
    x0, y0, x1, y1 = box
    w, h = x1 - x0, y1 - y0
    cid = _cid()
    xs = x0 + w * 0.64
    hx, hw = x0 + w * 0.16, max(1.4, w * 0.09)
    return (f'<clipPath id="{cid}"><path d="{shape}"/></clipPath>'
            f'<path d="{shape}" fill="{G}" stroke="none"/>'
            f'<g clip-path="url(#{cid})" stroke="none">'
            f'<rect x="{xs:.2f}" y="-10" width="84" height="84" fill="{dark(G, .07)}"/>'
            f'<rect x="-10" y="{top}" width="84" height="84" fill="{liquid}"/>'
            f'<rect x="{xs:.2f}" y="{top}" width="84" height="84" fill="{dark(liquid, .16)}"/>'
            f'<rect x="-10" y="{top}" width="84" height="1.6" fill="{light(liquid)}"/>'
            f'{extra}'
            f'<rect x="{hx:.2f}" y="{y0 + h * .1:.2f}" width="{hw:.2f}" height="{h * .55:.2f}" '
            f'rx="{hw / 2:.2f}" fill="{W}"/>'
            f'</g><path d="{shape}"/>')


def bubbles(*cs):
    return "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{W}" stroke="none"/>' for x, y, r in cs)


ICONS = [
    {
        "id": "erlenmeyer-flask",
        "title": "Erlenmeyer flask with orange liquid icon, chemistry cartoon clipart vector",
        "keywords": ["erlenmeyer", "flask", "conical flask", "glassware", "bubbles", "reaction", "orange"],
        "body": solid("M24 5h16v5H24z", G, 24, 40) + vessel(
            "M27 10v14L13 52a4 4 0 0 0 3.6 5.8h30.8A4 4 0 0 0 51 52L37 24V10z", (13, 10, 51, 58), 38, O,
            bubbles((27, 48, 2.2), (36, 44, 1.5), (31, 53, 1.2))),
    },
    {
        "id": "beaker",
        "title": "Laboratory beaker with blue liquid icon, chemistry cartoon clipart vector",
        "keywords": ["beaker", "glass", "measuring", "scale", "glassware", "blue", "volume"],
        "body": vessel("M14 10v44a5 5 0 0 0 5 5h26a5 5 0 0 0 5-5V10z", (14, 10, 50, 59), 32, T,
                       bubbles((24, 44, 2.2), (31, 51, 1.4))) +
                '<path d="M10 10h44M50 18h-7M50 24h-5M50 30h-7"/>',
    },
    {
        "id": "test-tube",
        "title": "Test tube with purple liquid icon, chemistry cartoon clipart vector",
        "keywords": ["test tube", "tube", "sample", "glassware", "purple", "potion", "bubbles"],
        "body": vessel("M25 10v38a7 7 0 0 0 14 0V10z", (25, 10, 39, 55), 28, P,
                       bubbles((31, 40, 2), (34, 47, 1.3))) + solid("M22 5h20v5H22z", G, 22, 42),
    },
    {
        "id": "test-tube-rack",
        "title": "Test tubes in wooden rack icon, chemistry cartoon clipart vector",
        "keywords": ["test tubes", "rack", "holder", "samples", "tubes", "glassware", "stand"],
        "body": solid("M8 28h4v24H8z", Y, 8, 12) + solid("M52 28h4v24h-4z", Y, 52, 56) +
                solid("M4 52h56v6H4z", Y, 4, 60) +
                vessel("M11 8v34a5 5 0 0 0 10 0V8z", (11, 8, 21, 47), 32, R) +
                vessel("M27 8v34a5 5 0 0 0 10 0V8z", (27, 8, 37, 47), 26, T) +
                vessel("M43 8v34a5 5 0 0 0 10 0V8z", (43, 8, 53, 47), 36, L) +
                solid("M6 22h52v6H6z", Y, 6, 58),
    },
    {
        "id": "round-bottom-flask",
        "title": "Round bottom flask with green liquid icon, chemistry cartoon clipart vector",
        "keywords": ["round bottom flask", "flask", "boiling flask", "glassware", "green", "potion"],
        "body": solid("M25 4h14v4H25z", G, 25, 39) + vessel(
            "M28 8v16.5A16 16 0 1 0 36 24.5V8z", (16, 8, 48, 56), 38, L,
            bubbles((25, 46, 2.2), (37, 43, 1.6), (31, 51, 1.3))),
    },
    {
        "id": "volumetric-flask",
        "title": "Volumetric flask with yellow solution icon, chemistry cartoon clipart vector",
        "keywords": ["volumetric flask", "flask", "measuring", "calibration", "glassware", "solution", "yellow"],
        "body": vessel("M29 8v22L16 46a10 10 0 0 0 8 14h16a10 10 0 0 0 8-14L35 30V8z", (15, 8, 49, 60), 44, Y,
                       bubbles((27, 52, 1.8))) +
                '<path d="M27 17h10"/>' + solid("M27.5 2h9v6h-9z", N, 27.5, 36.5),
    },
    {
        "id": "microscope",
        "title": "Microscope icon, science laboratory cartoon clipart vector",
        "keywords": ["microscope", "magnification", "biology", "microbiology", "optics", "lens", "study"],
        "body": solid("M40 52V25a9 9 0 0 0-9-9h-2v-6h2a15 15 0 0 1 15 15v27z", M, 29, 46) +
                solid("M21 10h10v19H21z", T, 21, 31) +
                solid("M19 3h14v7H19z", N, 19, 33) +
                solid("M23 29h6v6h-6z", N, 23, 29) +
                solid("M12 38h32v5H12z", N, 12, 44) +
                solid("M10 52h44v7H10z", N, 10, 54) +
                f'<circle cx="43" cy="32" r="4.5" fill="{O}"/>',
    },
    {
        "id": "bunsen-burner",
        "title": "Bunsen burner with flame icon, chemistry cartoon clipart vector",
        "keywords": ["bunsen burner", "burner", "flame", "fire", "gas", "heating", "heat"],
        "body": f'<path d="M32 1c6 7 8 11 8 15a8 8 0 0 1-16 0c0-4 2-8 8-15z" fill="{O}"/>'
                f'<path d="M32 9c2.5 3 3.5 5 3.5 7a3.5 3.5 0 0 1-7 0c0-2 1-4 3.5-7z" fill="{Y}" stroke="none"/>' +
                solid("M14 37h12v7H14z", O, 14, 26) +
                solid("M26 24h12v25H26z", M, 26, 38) +
                solid("M14 58h36l-5-10H19z", N, 14, 50),
    },
    {
        "id": "pipette",
        "title": "Volumetric pipette with red liquid icon, chemistry cartoon clipart vector",
        "keywords": ["pipette", "volumetric pipette", "measuring", "dosing", "red", "sample", "transfer"],
        "body": vessel("M29 4v17c-4 1.5-6 4-6 8v10c0 4 2 6.5 6 8v12l3 4 3-4V47c4-1.5 6-4 6-8V29c0-4-2-6.5-6-8V4z",
                       (23, 4, 41, 63), 26, R, bubbles((29, 36, 1.6))) +
                '<path d="M27 12h10"/>',
    },
    {
        "id": "dropper",
        "title": "Dropper with purple drop icon, chemistry cartoon clipart vector",
        "keywords": ["dropper", "eyedropper", "drop", "serum", "dose", "medicine", "purple"],
        "body": solid("M25 20v-9a7 7 0 0 1 14 0v9z", R, 25, 39) +
                vessel("M27 26v20l5 7 5-7V26z", (27, 26, 37, 53), 34, P) +
                solid("M22 20h20v6H22z", N, 22, 42) +
                f'<path d="M32 55c-2.4 3-3.6 5-3.6 6.5a3.6 3.6 0 0 0 7.2 0c0-1.5-1.2-3.5-3.6-6.5z" fill="{P}"/>',
    },
    {
        "id": "graduated-cylinder",
        "title": "Graduated cylinder with blue liquid icon, chemistry cartoon clipart vector",
        "keywords": ["graduated cylinder", "measuring cylinder", "cylinder", "scale", "volume", "measuring", "blue"],
        "body": vessel("M22 8v46h20V8z", (22, 8, 42, 54), 28, T, bubbles((30, 42, 1.8), (34, 48, 1.2))) +
                '<path d="M19 8h26M42 15h-6M42 21h-4M42 27h-6"/>' +
                solid("M20 54h24v4H20z", N, 20, 44) + solid("M15 58h34v4H15z", N, 15, 49),
    },
    {
        "id": "petri-dish",
        "title": "Petri dish with bacteria colonies icon, microbiology cartoon clipart vector",
        "keywords": ["petri dish", "bacteria", "culture", "microbiology", "colony", "biology", "agar"],
        "body": solid("M4 30v8a28 10 0 0 0 56 0v-8z", G, 4, 60) +
                f'<ellipse cx="32" cy="30" rx="28" ry="10" fill="#FFE7A3"/>'
                f'<ellipse cx="32" cy="31" rx="22" ry="6.5" fill="#FFD978" stroke="none"/>'
                f'<circle cx="22" cy="30" r="3.4" fill="{R}" stroke="none"/>'
                f'<circle cx="35" cy="27" r="2.6" fill="{P}" stroke="none"/>'
                f'<circle cx="42" cy="32" r="2" fill="{L}" stroke="none"/>'
                f'<circle cx="30" cy="34" r="1.6" fill="{O}" stroke="none"/>'
                f'<path d="M14 26c3-2 6-3 10-3.4" stroke="{W}"/>',
    },
    {
        "id": "funnel",
        "title": "Laboratory funnel with blue liquid icon, chemistry cartoon clipart vector",
        "keywords": ["funnel", "filter", "filtration", "pouring", "glassware", "separation", "blue"],
        "body": vessel("M8 10h48L37 34v24H27V34z", (8, 10, 56, 58), 18, T),
    },
    {
        "id": "mortar-and-pestle",
        "title": "Mortar and pestle icon, pharmacy and chemistry cartoon clipart vector",
        "keywords": ["mortar", "pestle", "grinding", "pharmacy", "apothecary", "powder", "herbal"],
        "body": solid("M34 30L47 7a3.5 3.5 0 0 1 6 3.4L41 30z", Y, 34, 53) +
                solid("M23 48l-3 10h24l-3-10z", N, 20, 44) +
                solid("M6 28h52a26 21 0 0 1-52 0z", M, 6, 58) +
                f'<path d="M11 28c4-5 8-6 12-6s7 2 9 6z" fill="{L}"/>',
    },
    {
        "id": "thermometer",
        "title": "Thermometer with red mercury icon, temperature cartoon clipart vector",
        "keywords": ["thermometer", "temperature", "heat", "measuring", "degree", "scale", "hot"],
        "body": vessel("M27 42V10a5 5 0 0 1 10 0v32a10 10 0 1 1-10 0z", (22, 5, 42, 61), 80, R,
                       f'<path d="M30 18h4v32h-4z" fill="{R}"/>'
                       f'<circle cx="32" cy="50.7" r="6.5" fill="{R}"/>'
                       f'<circle cx="30" cy="48.5" r="1.8" fill="{light(R)}"/>') +
                '<path d="M41 14h5M41 20h3.5M41 26h5M41 32h3.5"/>',
    },
    {
        "id": "burette-stand",
        "title": "Burette on stand icon, titration chemistry cartoon clipart vector",
        "keywords": ["burette", "titration", "stand", "clamp", "stopcock", "analysis", "purple"],
        "body": '<g transform="translate(10 0)">' +
                solid("M13 6h4v48h-4z", M, 13, 17) + solid("M2 54h36v6H2z", N, 2, 38) +
                solid("M17 18h13v4H17z", O, 17, 30) +
                vessel("M30 6v36l2 4h4l2-4V6z", (30, 6, 38, 46), 14, P) +
                '<path d="M30 20h3M30 26h3M30 32h3"/>' +
                solid("M27 46h14v3H27z", N, 27, 41) +
                '<path d="M34 49v3"/></g>',
    },
    {
        "id": "safety-goggles",
        "title": "Safety goggles icon, laboratory protective equipment cartoon clipart vector",
        "keywords": ["safety goggles", "goggles", "glasses", "protection", "safety", "ppe", "eye protection"],
        "body": solid("M1 25h8v8H1z", N, 1, 9) + solid("M55 25h8v8h-8z", N, 55, 63) +
                solid("M8 23c0-4 3-6 6-6h36c3 0 6 2 6 6v12c0 5-4 8-8 8h-9c-3 0-5-2-6-5h-2c-1 3-3 5-6 5h-9c-4 0-8-3-8-8z",
                      T, 8, 56) +
                f'<path d="M13 24c0-2 1-3 3-3h12v17h-8c-4 0-7-2-7-6zM36 21h12c2 0 3 1 3 3v8c0 4-3 6-7 6h-8z" fill="{G}" stroke="none"/>'
                f'<path d="M17 30l6-6M40 30l6-6" stroke="{W}" stroke-width="2.2"/>',
    },
    {
        "id": "retort",
        "title": "Retort distillation flask icon, alchemy and chemistry cartoon clipart vector",
        "keywords": ["retort", "distillation", "alchemy", "flask", "glassware", "vintage", "potion"],
        "body": '<g transform="translate(-1.5 -10)">' +
                '<path d="M22 53v4"/>' + solid("M11 57h22v4H11z", N, 11, 33) +
                vessel("M31.19 30.81A13 13 0 1 0 34.56 36.64L56 48l2-4z", (9, 25, 58, 53), 43, O,
                       bubbles((17, 49, 2), (26, 47, 1.4))) + "</g>",
    },
    {
        "id": "laboratory-scale",
        "title": "Analytical laboratory scale icon, weighing cartoon clipart vector",
        "keywords": ["scale", "balance", "weighing", "analytical balance", "weight", "digital scale", "measurement"],
        "body": vessel("M25 20v16h14V20z", (25, 20, 39, 36), 27, R) +
                '<path d="M23 20h18"/>' + solid("M29 39h6v6h-6z", N, 29, 35) +
                solid("M14 36h36v3H14z", N, 14, 50) +
                solid("M6 45h52v14H6z", M, 6, 58) +
                solid("M36 48h16v8H36z", N, 36, 52) + f'<path d="M39.5 52h9" stroke="{Y}"/>'
                f'<circle cx="14" cy="52" r="2.4" fill="{O}"/><circle cx="22" cy="52" r="2.4" fill="{T}"/>',
    },
    {
        "id": "wash-bottle",
        "title": "Laboratory wash bottle icon, chemistry cartoon clipart vector",
        "keywords": ["wash bottle", "squeeze bottle", "bottle", "rinse", "solvent", "plastic", "nozzle"],
        "body": '<path d="M32 16V8c0-2 1-3 3-3h12l5 5" stroke-width="2.4"/>' +
                solid("M25 22v-6h14v6z", O, 25, 39) +
                vessel("M18 26a4 4 0 0 1 4-4h20a4 4 0 0 1 4 4v30a4 4 0 0 1-4 4H22a4 4 0 0 1-4-4z", (18, 22, 46, 60),
                       40, T) +
                f'<path d="M24 30h16v8H24z" fill="{W}"/><path d="M27 34h10" stroke="{M}"/>',
    },
]

# Isi placeholder dengan id ikon (setiap ikon punya clipPath sendiri).
for _ic in ICONS:
    _ic["body"] = _ic["body"].replace("{p}", _ic["id"])
