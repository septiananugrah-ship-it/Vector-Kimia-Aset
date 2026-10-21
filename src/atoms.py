"""Set 05: model atom Bohr untuk unsur nomor 1-20, gaya semi-flat.

Inti berwarna dengan lambang unsur (teks sudah dikonversi ke outline),
kulit elektron sebagai lingkaran, elektron tersebar merata di tiap kulit.
"""
import math

from icons_lab_flat import O, R, T, solid
from textpath import text

SET_ID = "bohr-atom-icons"
STROKE = 1.4
SHADOW = False
GLYPH = True
THEME = "bohr atom model"
PATTERNS = [("#F3F7FF", "#E85D4A", "colorful atoms on light blue"),
            ("#1E2A3A", "#3FB6C4", "colorful atoms on dark navy")]

SET_TITLE = "Bohr atomic models of the first 20 chemical elements, colorful vector icons set"
SET_KEYWORDS = [
    "bohr model", "atom", "atoms", "atomic structure", "atomic model", "electron", "electron shell",
    "electron configuration", "nucleus", "proton", "neutron", "orbit", "element", "chemical element",
    "periodic table", "chemistry", "physics", "science", "education", "school", "icon set",
    "collection", "hydrogen", "helium", "carbon", "oxygen", "nitrogen", "sodium", "calcium",
    "vector", "illustration", "isolated", "colorful", "diagram", "scientific",
]
COMMON_KEYWORDS = [
    "bohr model", "atom", "atomic structure", "atomic model", "electron", "electron shell",
    "electron configuration", "nucleus", "orbit", "element", "chemical element", "periodic table",
    "chemistry", "physics", "science", "education", "school", "icon", "vector", "illustration",
    "isolated", "diagram", "scientific",
]

ELEMENTS = [
    ("H", "Hydrogen"), ("He", "Helium"), ("Li", "Lithium"), ("Be", "Beryllium"), ("B", "Boron"),
    ("C", "Carbon"), ("N", "Nitrogen"), ("O", "Oxygen"), ("F", "Fluorine"), ("Ne", "Neon"),
    ("Na", "Sodium"), ("Mg", "Magnesium"), ("Al", "Aluminium"), ("Si", "Silicon"), ("P", "Phosphorus"),
    ("S", "Sulfur"), ("Cl", "Chlorine"), ("Ar", "Argon"), ("K", "Potassium"), ("Ca", "Calcium"),
]
ORBIT = "#7C8B9C"


def shells(z):
    out, caps = [], [2, 8, 8, 2]
    for c in caps:
        if z <= 0:
            break
        out.append(min(c, z))
        z -= c
    return out


def bohr(z, sym):
    sh = shells(z)
    rn = 7.5 + 2.6 * (len(sh) - 1)  # inti ikut membesar agar lambang tetap terbaca
    body = ""
    for k, n in enumerate(sh):
        r = rn + 7 + 7.5 * k
        body += f'<circle cx="0" cy="0" r="{r}" stroke="{ORBIT}"/>'
        start = -90 + k * 22
        for i in range(n):
            a = math.radians(start + i * 360 / n)
            x, y = r * math.cos(a), r * math.sin(a)
            body += solid(f"M{x - 2.6:.2f} {y:.2f}a2.6 2.6 0 1 0 5.2 0a2.6 2.6 0 1 0-5.2 0z", T, x - 2.6, x + 2.6)
    body += solid(f"M{-rn} 0a{rn} {rn} 0 1 0 {2 * rn} 0a{rn} {rn} 0 1 0 {-2 * rn} 0z", R if z % 2 else O, -rn, rn)
    size = rn * (1.1 if len(sym) == 1 else .95)
    body += text(sym, 0, size * 0.36, size, "#FFFFFF")
    return body


ICONS = []
for z, (sym, name) in enumerate(ELEMENTS, start=1):
    n_e = "electron" if z == 1 else "electrons"
    ICONS.append({
        "id": f"{z:02d}-{name.lower()}",
        "name": f"{name} atom Bohr model",
        "title": f"{name} atom Bohr model icon, {sym} with {z} {n_e}, chemistry vector illustration",
        "keywords": [name.lower(), sym.lower(), f"{name.lower()} atom", f"atomic number {z}"],
        "body": bohr(z, sym).replace("{p}", f"{z:02d}-{name.lower()}"),
    })
