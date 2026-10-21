"""Set 04: 20 model molekul bola-dan-batang (ball and stick), gaya semi-flat.

Molekul ditulis sebagai daftar atom (unsur, x, y) dan ikatan (i, j, orde).
Warna atom mengikuti konvensi CPK. Koordinat 2D bebas skala; build.py
menskalakan setiap molekul agar mengisi bingkai.
"""
import math

from icons_lab_flat import M, P, R, W, Y, L, dark, solid

SET_ID = "molecule-icons"
STROKE = 1.6
SHADOW = False
GLYPH = True
THEME = "chemistry molecule model"
PATTERNS = [("#FFFFFF", "#3FB6C4", "colorful molecules on white"),
            ("#16324F", "#FFC845", "colorful molecules on dark blue"),
            ("#FDEEEE", "#8E6CC9", "colorful molecules on soft pink")]

SET_TITLE = "Molecule ball and stick models icons set, 20 colorful chemistry vector illustrations"
SET_KEYWORDS = [
    "molecule", "molecules", "molecular model", "ball and stick", "icon set", "collection",
    "chemistry", "chemical", "chemical formula", "chemical structure", "atom", "atoms",
    "bond", "chemical bond", "compound", "science", "scientific", "education", "school",
    "biology", "physics", "research", "laboratory", "water", "carbon dioxide", "methane",
    "ammonia", "oxygen", "benzene", "ethanol", "vector", "illustration", "isolated",
    "colorful", "3d", "structure", "cartoon", "flat",
]
COMMON_KEYWORDS = [
    "molecule", "molecular model", "ball and stick", "chemistry", "chemical", "chemical formula",
    "chemical structure", "atom", "bond", "compound", "science", "scientific", "education",
    "school", "research", "laboratory", "icon", "vector", "illustration", "isolated", "colorful",
    "structure", "physics",
]

COLOR = {"H": W, "C": "#4A4F5C", "O": R, "N": "#3D7DDB", "Cl": L, "S": Y, "Na": P}
RADIUS = {"H": 4.2, "C": 6.0, "O": 5.6, "N": 5.8, "Cl": 6.6, "S": 6.8, "Na": 6.6}
BOND = 1.35  # setengah tebal batang ikatan


def _circle(x, y, r):
    return f"M{x - r:.2f} {y:.2f}a{r:.2f} {r:.2f} 0 1 0 {2 * r:.2f} 0a{r:.2f} {r:.2f} 0 1 0 {-2 * r:.2f} 0z"


def _bond(a, b, order):
    (x1, y1), (x2, y2) = a, b
    dx, dy = x2 - x1, y2 - y1
    d = math.hypot(dx, dy)
    nx, ny = -dy / d, dx / d
    offs = {1: [0], 2: [-1.9, 1.9], 3: [-3.2, 0, 3.2]}[order]
    out = ""
    for o in offs:
        cx, cy = nx * o, ny * o
        px, py = nx * BOND, ny * BOND
        pts = [(x1 + cx + px, y1 + cy + py), (x2 + cx + px, y2 + cy + py),
               (x2 + cx - px, y2 + cy - py), (x1 + cx - px, y1 + cy - py)]
        out += '<path d="M' + "L".join(f"{x:.2f} {y:.2f}" for x, y in pts) + f'z" fill="{M}"/>'
    return out


def molecule(atoms, bonds):
    body = "".join(_bond(atoms[i][1:], atoms[j][1:], o) for i, j, o in bonds)
    # atom di belakang (kecil/H) digambar dulu supaya tumpang tindih terlihat wajar
    for el, x, y in sorted(atoms, key=lambda a: RADIUS[a[0]]):
        r = RADIUS[el]
        body += solid(_circle(x, y, r), COLOR[el], x - r, x + r)
        body += (f'<ellipse cx="{x - r * .36:.2f}" cy="{y - r * .38:.2f}" rx="{r * .3:.2f}" ry="{r * .2:.2f}" '
                 f'transform="rotate(-35 {x - r * .36:.2f} {y - r * .38:.2f})" fill="#FFFFFF" stroke="none"/>')
    return body


def ring(n, r, start=-90):
    return [(r * math.cos(math.radians(start + i * 360 / n)), r * math.sin(math.radians(start + i * 360 / n)))
            for i in range(n)]


def _benzene():
    cs, hs = ring(6, 14), ring(6, 25)
    atoms = [("C", x, y) for x, y in cs] + [("H", x, y) for x, y in hs]
    bonds = [(i, (i + 1) % 6, 2 if i % 2 == 0 else 1) for i in range(6)] + [(i, i + 6, 1) for i in range(6)]
    return atoms, bonds


def _nacl():
    atoms, bonds = [], []
    for r in range(3):
        for c in range(3):
            atoms.append(("Na" if (r + c) % 2 else "Cl", c * 18, r * 18))
    for r in range(3):
        for c in range(3):
            i = r * 3 + c
            if c < 2:
                bonds.append((i, i + 1, 1))
            if r < 2:
                bonds.append((i, i + 3, 1))
    return atoms, bonds


MOLS = [
    ("water", "Water molecule H2O", ["water", "h2o", "hydrogen", "oxygen", "liquid", "aqua"],
     [("O", 0, 0), ("H", -9, 7), ("H", 9, 7)], [(0, 1, 1), (0, 2, 1)]),
    ("carbon-dioxide", "Carbon dioxide molecule CO2", ["carbon dioxide", "co2", "greenhouse gas", "emission", "climate", "carbon"],
     [("C", 0, 0), ("O", -14, 0), ("O", 14, 0)], [(0, 1, 2), (0, 2, 2)]),
    ("methane", "Methane molecule CH4", ["methane", "ch4", "natural gas", "greenhouse gas", "hydrocarbon", "fuel"],
     [("C", 0, 0), ("H", 0, -12), ("H", -11, 5), ("H", 11, 5), ("H", 3, 11)], [(0, i, 1) for i in range(1, 5)]),
    ("ammonia", "Ammonia molecule NH3", ["ammonia", "nh3", "nitrogen", "fertilizer", "gas", "base"],
     [("N", 0, -3), ("H", -11, 4), ("H", 11, 4), ("H", 0, 9)], [(0, i, 1) for i in range(1, 4)]),
    ("oxygen", "Oxygen molecule O2", ["oxygen", "o2", "air", "gas", "breathing", "diatomic"],
     [("O", -6.5, 0), ("O", 6.5, 0)], [(0, 1, 2)]),
    ("nitrogen", "Nitrogen molecule N2", ["nitrogen", "n2", "air", "gas", "diatomic", "triple bond"],
     [("N", -6.5, 0), ("N", 6.5, 0)], [(0, 1, 3)]),
    ("hydrogen", "Hydrogen molecule H2", ["hydrogen", "h2", "gas", "fuel", "clean energy", "diatomic"],
     [("H", -5, 0), ("H", 5, 0)], [(0, 1, 1)]),
    ("hydrogen-chloride", "Hydrogen chloride molecule HCl", ["hydrogen chloride", "hcl", "hydrochloric acid", "acid", "chlorine", "gas"],
     [("Cl", 3, 0), ("H", -9, 0)], [(0, 1, 1)]),
    ("ethanol", "Ethanol molecule C2H5OH", ["ethanol", "alcohol", "c2h5oh", "biofuel", "drink", "solvent"],
     [("C", -10, 3), ("C", 1, -3), ("O", 12, 3), ("H", 19, -2), ("H", -19, -1), ("H", -14, 12),
      ("H", -6, 12), ("H", -2, -13), ("H", 7, -12)],
     [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 4, 1), (0, 5, 1), (0, 6, 1), (1, 7, 1), (1, 8, 1)]),
    ("benzene", "Benzene molecule C6H6", ["benzene", "c6h6", "aromatic", "ring", "hexagon", "hydrocarbon"],
     *_benzene()),
    ("ethylene", "Ethylene molecule C2H4", ["ethylene", "ethene", "c2h4", "alkene", "plastic", "hydrocarbon"],
     [("C", -7, 0), ("C", 7, 0), ("H", -14, -9), ("H", -14, 9), ("H", 14, -9), ("H", 14, 9)],
     [(0, 1, 2), (0, 2, 1), (0, 3, 1), (1, 4, 1), (1, 5, 1)]),
    ("acetylene", "Acetylene molecule C2H2", ["acetylene", "ethyne", "c2h2", "alkyne", "welding", "gas"],
     [("C", -7, 0), ("C", 7, 0), ("H", -18, 0), ("H", 18, 0)], [(0, 1, 3), (0, 2, 1), (1, 3, 1)]),
    ("sulfur-dioxide", "Sulfur dioxide molecule SO2", ["sulfur dioxide", "so2", "pollution", "acid rain", "sulfur", "gas"],
     [("S", 0, -2), ("O", -12, 6), ("O", 12, 6)], [(0, 1, 2), (0, 2, 2)]),
    ("hydrogen-peroxide", "Hydrogen peroxide molecule H2O2", ["hydrogen peroxide", "h2o2", "peroxide", "disinfectant", "bleach", "antiseptic"],
     [("O", -6, 0), ("O", 6, 0), ("H", -11, -9), ("H", 11, 9)], [(0, 1, 1), (0, 2, 1), (1, 3, 1)]),
    ("sodium-chloride", "Sodium chloride crystal lattice NaCl", ["sodium chloride", "nacl", "salt", "crystal lattice", "ionic", "table salt"],
     *_nacl()),
    ("formaldehyde", "Formaldehyde molecule CH2O", ["formaldehyde", "ch2o", "methanal", "aldehyde", "preservative", "formalin"],
     [("C", 0, 3), ("O", 0, -10), ("H", -10, 10), ("H", 10, 10)], [(0, 1, 2), (0, 2, 1), (0, 3, 1)]),
    ("methanol", "Methanol molecule CH3OH", ["methanol", "ch3oh", "methyl alcohol", "alcohol", "fuel", "solvent"],
     [("C", -5, 0), ("O", 8, 0), ("H", 14, -7), ("H", -12, -7), ("H", -12, 7), ("H", -3, 11)],
     [(0, 1, 1), (1, 2, 1), (0, 3, 1), (0, 4, 1), (0, 5, 1)]),
    ("ozone", "Ozone molecule O3", ["ozone", "o3", "ozone layer", "atmosphere", "oxygen", "gas"],
     [("O", 0, -4), ("O", -11, 4), ("O", 11, 4)], [(0, 1, 2), (0, 2, 1)]),
    ("carbon-monoxide", "Carbon monoxide molecule CO", ["carbon monoxide", "co", "poison gas", "toxic", "carbon", "gas"],
     [("C", -6.5, 0), ("O", 6.5, 0)], [(0, 1, 3)]),
    ("sulfuric-acid", "Sulfuric acid molecule H2SO4", ["sulfuric acid", "h2so4", "acid", "sulfur", "corrosive", "battery acid"],
     [("S", 0, 0), ("O", 0, -13), ("O", 0, 13), ("O", -13, 0), ("O", 13, 0), ("H", -20, -6), ("H", 20, 6)],
     [(0, 1, 2), (0, 2, 2), (0, 3, 1), (0, 4, 1), (3, 5, 1), (4, 6, 1)]),
]

ICONS = []
for mid, name, kw, atoms, bonds in MOLS:
    ICONS.append({
        "id": mid,
        "name": f"{name} ball and stick model",
        "title": f"{name} ball and stick model icon, chemistry vector illustration",
        "keywords": kw,
        "body": molecule(atoms, bonds).replace("{p}", mid),
    })
