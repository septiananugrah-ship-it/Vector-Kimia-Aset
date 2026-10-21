"""Set 08: model atom Bohr jilid 2, unsur nomor 21-36 (Sc sampai Kr).

Susunan elektron per kulit ditulis eksplisit karena logam transisi tidak
mengikuti pola 2, 8, 8 (mis. Fe = 2, 8, 14, 2; Cu = 2, 8, 18, 1).
"""
import atoms
from atoms import bohr

SET_ID = "bohr-atom2-icons"
STROKE = atoms.STROKE
SHADOW = False
GLYPH = True
THEME = "bohr atom model"
PATTERNS = [("#FFF7EC", "#3FB6C4", "colorful atoms on cream")]

SET_TITLE = "Bohr atomic models of chemical elements 21 to 36, colorful vector icons set"
SET_KEYWORDS = atoms.SET_KEYWORDS[:24] + ["iron", "copper", "zinc", "titanium", "nickel", "transition metal",
                                          "bromine", "krypton"]
COMMON_KEYWORDS = atoms.COMMON_KEYWORDS

ELEMENTS = [
    ("Sc", "Scandium", [2, 8, 9, 2]), ("Ti", "Titanium", [2, 8, 10, 2]), ("V", "Vanadium", [2, 8, 11, 2]),
    ("Cr", "Chromium", [2, 8, 13, 1]), ("Mn", "Manganese", [2, 8, 13, 2]), ("Fe", "Iron", [2, 8, 14, 2]),
    ("Co", "Cobalt", [2, 8, 15, 2]), ("Ni", "Nickel", [2, 8, 16, 2]), ("Cu", "Copper", [2, 8, 18, 1]),
    ("Zn", "Zinc", [2, 8, 18, 2]), ("Ga", "Gallium", [2, 8, 18, 3]), ("Ge", "Germanium", [2, 8, 18, 4]),
    ("As", "Arsenic", [2, 8, 18, 5]), ("Se", "Selenium", [2, 8, 18, 6]), ("Br", "Bromine", [2, 8, 18, 7]),
    ("Kr", "Krypton", [2, 8, 18, 8]),
]

ICONS = []
for z, (sym, name, sh) in enumerate(ELEMENTS, start=21):
    assert sum(sh) == z, sym
    key = f"{z:02d}-{name.lower()}"
    ICONS.append({
        "id": key,
        "name": f"{name} atom Bohr model",
        "title": f"{name} atom Bohr model icon, {sym} with {z} electrons ({', '.join(map(str, sh))}), "
                 "chemistry vector illustration",
        "keywords": [name.lower(), sym.lower(), f"{name.lower()} atom", f"atomic number {z}"],
        "body": bohr(z, sym, sh).replace("{p}", key),
    })
