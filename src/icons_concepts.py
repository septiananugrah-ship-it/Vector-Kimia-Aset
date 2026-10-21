"""Set 06: 20 ikon konsep sains & kimia, gaya semi-flat (sama dengan set 02/03)."""
import math

from icons_lab2 import flame
from icons_lab_flat import G, L, M, N, O, P, R, T, W, Y, bubbles, light, solid, vessel
from molecules import molecule
from textpath import text

SET_ID = "concept-flat-icons"
STROKE = 1.6
SHADOW = True
GLYPH = True
THEME = "chemistry and science concept"
PATTERNS = [("#F4F1FF", "#8E6CC9", "colorful science on lavender"),
            ("#13293D", "#F28C28", "colorful science on dark blue")]

SET_TITLE = "Chemistry and science concept icons set, 20 colorful cartoon vector clipart"
SET_KEYWORDS = [
    "icon set", "collection", "science", "chemistry", "physics", "biology", "concept", "atom", "dna",
    "radioactive", "element", "battery", "magnet", "crystal", "water drop", "fire", "energy", "molecule",
    "green chemistry", "recycling", "ph", "benzene", "gas", "idea", "book", "medicine", "reaction",
    "education", "school", "research", "flat", "colorful", "cartoon", "clipart", "vector", "illustration",
    "isolated", "sticker", "symbol",
]
COMMON_KEYWORDS = [
    "icon", "science", "chemistry", "scientific", "concept", "education", "school", "research", "flat",
    "colorful", "cartoon", "clipart", "vector", "illustration", "isolated", "sticker", "symbol", "sign",
    "design", "element", "graphic",
]


def ring_line(d, col, w=3.4):
    """Garis tebal berwarna dengan tepi gelap (dua lapis stroke)."""
    return (f'<path d="{d}" stroke="{N}" stroke-width="{w + 2.6}" fill="none" stroke-linecap="round"/>'
            f'<path d="{d}" stroke="{col}" stroke-width="{w}" fill="none" stroke-linecap="round"/>')


def circle(x, y, r):
    return f"M{x - r} {y}a{r} {r} 0 1 0 {2 * r} 0a{r} {r} 0 1 0 {-2 * r} 0z"


def _atom():
    out = ""
    for a in (0, 60, 120):
        out += (f'<ellipse cx="32" cy="32" rx="28" ry="10.5" transform="rotate({a} 32 32)" fill="none" '
                f'stroke="{N}" stroke-width="5.6"/>'
                f'<ellipse cx="32" cy="32" rx="28" ry="10.5" transform="rotate({a} 32 32)" fill="none" '
                f'stroke="{T}" stroke-width="3"/>')
    for a in (0, 60, 120):
        ex = 32 + 28 * math.cos(math.radians(a))
        ey = 32 + 28 * math.sin(math.radians(a))
        out += solid(circle(round(ex, 2), round(ey, 2), 3.6), O, ex - 3.6, ex + 3.6)
    return out + solid(circle(32, 32, 7.5), R, 24.5, 39.5)


def _dna():
    s1, s2, rungs = [], [], ""
    for k in range(57):
        y = 4 + k
        t = (y - 4) / 56 * 2.2 * math.pi
        s1.append((32 + 15 * math.sin(t), y))
        s2.append((32 - 15 * math.sin(t), y))
    for k in range(4, 57, 7):
        (x1, y1), (x2, _) = s1[k], s2[k]
        col = (Y, L, O, P)[(k // 7) % 4]
        rungs += ring_line(f"M{x1:.1f} {y1:.1f}H{x2:.1f}", col, 2.4)
    d1 = "M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in s1)
    d2 = "M" + "L".join(f"{x:.1f} {y:.1f}" for x, y in s2)
    return rungs + ring_line(d2, T, 4) + ring_line(d1, P, 4)


def _radioactive():
    out = solid(circle(32, 32, 29), Y, 3, 61)
    for c in (-150, -30, 90):
        a1, a2 = math.radians(c - 30), math.radians(c + 30)
        ri, ro = 7.5, 24
        p = (f"M{32 + ri * math.cos(a1):.2f} {32 + ri * math.sin(a1):.2f}"
             f"L{32 + ro * math.cos(a1):.2f} {32 + ro * math.sin(a1):.2f}"
             f"A{ro} {ro} 0 0 1 {32 + ro * math.cos(a2):.2f} {32 + ro * math.sin(a2):.2f}"
             f"L{32 + ri * math.cos(a2):.2f} {32 + ri * math.sin(a2):.2f}"
             f"A{ri} {ri} 0 0 0 {32 + ri * math.cos(a1):.2f} {32 + ri * math.sin(a1):.2f}z")
        out += f'<path d="{p}" fill="{N}"/>'
    return out + f'<circle cx="32" cy="32" r="4.6" fill="{N}"/>'


def _element_tile():
    return (solid("M8 12a6 6 0 0 1 6-6h36a6 6 0 0 1 6 6v40a6 6 0 0 1-6 6H14a6 6 0 0 1-6-6z", "#8ACBEF", 8, 56) +
            text("6", 14, 18, 8, N, "SemiBold", "start") + text("C", 32, 40, 24, N) +
            text("Carbon", 32, 49, 6.5, N, "SemiBold") + text("12.011", 32, 55.5, 5, N, "Regular"))


def _battery():
    return (solid("M52 24h5v16h-5z", N, 52, 57) +
            solid("M6 22a5 5 0 0 1 5-5h36a5 5 0 0 1 5 5v20a5 5 0 0 1-5 5H11a5 5 0 0 1-5-5z", L, 6, 52) +
            solid("M9 20h14v24H9z", "#2E8F5A", 9, 23) +
            '<path d="M38 26v12M32 32h12" stroke="#FFFFFF" stroke-width="2.6"/>'
            '<path d="M12 32h8" stroke="#FFFFFF" stroke-width="2.6"/>')


def _magnet():
    return (solid("M12 8h12v26a8 8 0 0 0 16 0V8h12v26a20 20 0 0 1-40 0z", R, 12, 52) +
            solid("M12 8h12v8H12z", M, 12, 24) + solid("M40 8h12v8H40z", M, 40, 52) +
            '<path d="M6 4l-3-3M58 4l3-3M2 12H-2M62 12h4" stroke-width="2"/>')


def _crystal():
    return (solid("M32 3l19 13v32L32 61 13 48V16z", P, 13, 51) +
            f'<path d="M32 3v58M13 16l19 13 19-13M32 29v32" stroke="{N}" stroke-width="1.4"/>'
            f'<path d="M13 16l19 13v32L13 48z" fill="{light(P, .3)}" stroke="{N}" stroke-width="1.4"/>'
            f'<path d="M19 22l4 3v12" stroke="{W}" stroke-width="2"/>')


def _drop():
    return (solid("M32 3c12 15 20 26 20 36a20 20 0 0 1-40 0c0-10 8-21 20-36z", T, 12, 52) +
            f'<path d="M20 40a12 12 0 0 0 7 11" stroke="{W}" stroke-width="2.6"/>'
            + bubbles((38, 30, 2.4), (34, 22, 1.5)))


def _molecule():
    return molecule([("C", 0, 0), ("O", 14, -9), ("N", 13, 11), ("H", -12, 8), ("Cl", -11, -12)],
                    [(0, 1, 2), (0, 2, 1), (0, 3, 1), (0, 4, 1)])


def _green():
    return (vessel("M24 14v34a8 8 0 0 0 16 0V14z", (24, 14, 40, 56), 32, L, bubbles((30, 46, 1.8), (34, 40, 1.2))) +
            solid("M21 10h22v5H21z", G, 21, 43) +
            solid("M38 10c0-6 6-9 18-8-1 9-6 14-14 12", L, 38, 56) +
            '<path d="M38 12c4-3 8-5 13-6"/>' +
            solid("M26 10c0-5-5-8-14-7 1 7 5 11 11 10", "#2E8F5A", 12, 26))


def _cycle():
    out = ""
    for a0, col in ((-160, L), (20, T)):
        a1 = a0 + 140
        r = 22
        x1, y1 = 32 + r * math.cos(math.radians(a0)), 32 + r * math.sin(math.radians(a0))
        x2, y2 = 32 + r * math.cos(math.radians(a1)), 32 + r * math.sin(math.radians(a1))
        out += ring_line(f"M{x1:.2f} {y1:.2f}A{r} {r} 0 0 1 {x2:.2f} {y2:.2f}", col, 5)
        t = math.radians(a1)
        tx, ty = -math.sin(t), math.cos(t)  # arah garis singgung (searah jarum jam)
        nx, ny = math.cos(t), math.sin(t)
        hx, hy = x2 + tx * 9, y2 + ty * 9
        out += (f'<path d="M{hx:.2f} {hy:.2f}L{x2 + nx * 8:.2f} {y2 + ny * 8:.2f}L{x2 - nx * 8:.2f} {y2 - ny * 8:.2f}z" '
                f'fill="{col}"/>')
    return out + solid(circle(32, 32, 7), Y, 25, 39)


def _ph_strip():
    out = solid("M22 4h20v56H22z", W, 22, 42)
    for k, c in enumerate((R, O, Y, L, T)):
        out += f'<path d="M25 {20 + k * 8}h14v6H25z" fill="{c}"/>'
    return out + '<path d="M22 14h20"/>'


def _benzene():
    pts = [(32 + 26 * math.cos(math.radians(30 + 60 * k)), 32 + 26 * math.sin(math.radians(30 + 60 * k)))
           for k in range(6)]
    d = "M" + "L".join(f"{x:.2f} {y:.2f}" for x, y in pts) + "z"
    return (solid(d, G, 9.5, 54.5) +
            f'<circle cx="32" cy="32" r="14" fill="none" stroke="{N}" stroke-width="6"/>'
            f'<circle cx="32" cy="32" r="14" fill="none" stroke="{T}" stroke-width="3.2"/>')


def _cloud():
    return (solid("M18 46a11 11 0 0 1-1-22 15 15 0 0 1 28-5 12 12 0 0 1 4 27z", M, 6, 61) +
            f'<path d="M14 34a7 7 0 0 1 6-8" stroke="{W}" stroke-width="2.4"/>' +
            "".join(solid(circle(x, y, r), T, x - r, x + r) for x, y, r in ((22, 54, 3.4), (33, 58, 2.6), (43, 53, 3))))


def _bulb():
    return (solid("M32 3a20 20 0 0 0-11 36v7h22v-7A20 20 0 0 0 32 3z", Y, 12, 52) +
            solid("M21 46h22v10a4 4 0 0 1-4 4H25a4 4 0 0 1-4-4z", M, 21, 43) +
            '<path d="M21 51h22"/>' +
            f'<ellipse cx="32" cy="23" rx="9" ry="3.5" fill="none" stroke="{O}" stroke-width="1.8"/>'
            f'<ellipse cx="32" cy="23" rx="9" ry="3.5" transform="rotate(60 32 23)" fill="none" stroke="{O}" '
            'stroke-width="1.8"/>'
            f'<ellipse cx="32" cy="23" rx="9" ry="3.5" transform="rotate(120 32 23)" fill="none" stroke="{O}" '
            'stroke-width="1.8"/>'
            f'<circle cx="32" cy="23" r="2.2" fill="{R}" stroke="none"/>')


def _book():
    return (solid("M14 52h38v8H18a4 4 0 0 1-4-4z", W, 14, 52) +
            solid("M14 8a4 4 0 0 1 4-4h34v48H18a4 4 0 0 0-4 4z", R, 14, 52) +
            f'<path d="M30 16v8l-7 13a2 2 0 0 0 2 3h16a2 2 0 0 0 2-3l-7-13v-8z" fill="{W}" stroke="{W}" '
            'stroke-width="1"/><path d="M28 16h10" stroke="#FFFFFF" stroke-width="2"/>'
            f'<path d="M26 33h14l3 5a2 2 0 0 1-2 3H25a2 2 0 0 1-2-3z" fill="{T}" stroke="none"/>')


def _capsule():
    return ('<g transform="rotate(-40 32 32)">' +
            solid("M32 18h12a14 14 0 0 1 0 28H32z", W, 32, 58) +
            solid("M32 18H20a14 14 0 0 0 0 28h12z", R, 6, 32) +
            f'<path d="M14 26a7 7 0 0 1 6-4" stroke="{W}" stroke-width="2.4"/></g>')


def _equation():
    def ball(x, y, r, c):
        return solid(circle(x, y, r), c, x - r, x + r)
    return (ball(14, 14, 9, R) + '<path d="M27 14h10M32 9v10" stroke-width="3"/>' + ball(50, 14, 9, "#3D7DDB") +
            '<path d="M32 28v12M26 35l6 6 6-6" stroke-width="3"/>' +
            ball(24, 52, 10, R) + ball(40, 52, 10, "#3D7DDB"))


ICONS = [
    ("atom", "Atom symbol icon, science and physics cartoon vector", ["atom", "atomic", "nucleus", "electron", "orbit", "nuclear", "physics"], _atom),
    ("dna", "DNA double helix icon, genetics and biology cartoon vector", ["dna", "double helix", "genetics", "gene", "biology", "biotechnology", "genome"], _dna),
    ("radioactive", "Radioactive warning symbol icon, radiation cartoon vector", ["radioactive", "radiation", "nuclear", "hazard", "warning", "danger", "trefoil"], _radioactive),
    ("element-tile", "Carbon chemical element tile icon, periodic table cartoon vector", ["chemical element", "carbon", "periodic table", "element tile", "symbol", "atomic number", "c"], _element_tile),
    ("battery", "Battery icon, electrochemistry and energy cartoon vector", ["battery", "electrochemistry", "energy", "power", "charge", "electricity", "cell"], _battery),
    ("magnet", "Horseshoe magnet icon, magnetism physics cartoon vector", ["magnet", "magnetism", "magnetic", "horseshoe magnet", "attraction", "physics", "force"], _magnet),
    ("crystal", "Purple crystal icon, mineral and crystallography cartoon vector", ["crystal", "mineral", "gem", "crystallography", "quartz", "gemstone", "geology"], _crystal),
    ("water-drop", "Water drop icon, H2O liquid cartoon vector", ["water drop", "water", "drop", "h2o", "liquid", "droplet", "aqua"], _drop),
    ("fire", "Fire flame icon, combustion and heat cartoon vector", ["fire", "flame", "combustion", "heat", "burn", "hot", "energy"], lambda: flame(32, 2, 60)),
    ("lightning", "Lightning bolt icon, electricity and energy cartoon vector", ["lightning", "bolt", "electricity", "energy", "power", "electrolysis", "voltage"], lambda: solid("M37 2L11 37h18l-6 25 31-37H36z", Y, 11, 54)),
    ("molecule", "Molecule structure icon, chemistry cartoon vector", ["molecule", "molecular structure", "compound", "chemical bond", "atoms", "ball and stick", "structure"], _molecule),
    ("green-chemistry", "Green chemistry test tube with leaves icon, eco science cartoon vector", ["green chemistry", "eco", "sustainable", "organic", "biotechnology", "natural", "leaf"], _green),
    ("chemical-cycle", "Cycle arrows icon, chemical cycle and recycling cartoon vector", ["cycle", "recycling", "reversible reaction", "equilibrium", "renewable", "loop", "arrows"], _cycle),
    ("ph-strip", "pH test strip icon, litmus paper cartoon vector", ["ph test", "litmus paper", "ph strip", "indicator", "acid", "base", "test strip"], _ph_strip),
    ("benzene-ring", "Benzene ring icon, organic chemistry hexagon cartoon vector", ["benzene", "benzene ring", "hexagon", "aromatic", "organic chemistry", "ring", "c6h6"], _benzene),
    ("gas-cloud", "Gas cloud with bubbles icon, vapor and fumes cartoon vector", ["gas", "cloud", "vapor", "fumes", "smoke", "air", "emission"], _cloud),
    ("idea-bulb", "Light bulb with atom icon, science idea cartoon vector", ["light bulb", "idea", "innovation", "science idea", "creativity", "invention", "atom"], _bulb),
    ("chemistry-book", "Chemistry textbook icon, science education cartoon vector", ["book", "textbook", "chemistry book", "study", "learning", "knowledge", "reading"], _book),
    ("capsule", "Medicine capsule pill icon, pharmacy cartoon vector", ["capsule", "pill", "medicine", "pharmacy", "drug", "tablet", "pharmaceutical"], _capsule),
    ("chemical-equation", "Chemical reaction equation icon, A plus B gives AB cartoon vector", ["chemical equation", "reaction", "synthesis", "reactants", "products", "formula", "combine"], _equation),
]
ICONS = [{"id": i, "title": t, "keywords": k, "body": f().replace("{p}", i)} for i, t, k, f in ICONS]
# warna yang tetap terang di varian glyph agar bentuknya terbaca
for _ic in ICONS:
    _ic["glyph_light"] = {"radioactive": [Y], "element-tile": ["#8ACBEF"]}.get(_ic["id"], [])
