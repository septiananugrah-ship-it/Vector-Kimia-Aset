"""Set model atom Bohr jilid 3, unsur nomor 37-54 (Rb sampai Xe).

Susunan elektron per kulit ditulis eksplisit karena logam transisi tidak
mengikuti pola 2, 8, 8 (mis. Mo = 2, 8, 18, 13, 1; Pd = 2, 8, 18, 18).
"""
import atoms
from atoms import bohr

SET_ID = "bohr-atom3-icons"
STROKE = atoms.STROKE
SHADOW = False
GLYPH = True
THEME = "bohr atom model"
PATTERNS = [("#EEF8F4", "#E85D4A", "colorful atoms on mint")]

SET_TITLE = "Bohr atomic models of chemical elements 37 to 54, colorful vector icons set"
SET_KEYWORDS = atoms.SET_KEYWORDS[:24] + ["silver", "tin", "iodine", "xenon", "palladium", "transition metal",
                                          "bromine", "krypton"]
COMMON_KEYWORDS = atoms.COMMON_KEYWORDS

ELEMENTS = [
    ("Rb", "Rubidium", [2, 8, 18, 8, 1]), ("Sr", "Strontium", [2, 8, 18, 8, 2]), ("Y", "Yttrium", [2, 8, 18, 9, 2]),
    ("Zr", "Zirconium", [2, 8, 18, 10, 2]), ("Nb", "Niobium", [2, 8, 18, 12, 1]),
    ("Mo", "Molybdenum", [2, 8, 18, 13, 1]), ("Tc", "Technetium", [2, 8, 18, 13, 2]),
    ("Ru", "Ruthenium", [2, 8, 18, 15, 1]), ("Rh", "Rhodium", [2, 8, 18, 16, 1]), ("Pd", "Palladium", [2, 8, 18, 18]),
    ("Ag", "Silver", [2, 8, 18, 18, 1]), ("Cd", "Cadmium", [2, 8, 18, 18, 2]), ("In", "Indium", [2, 8, 18, 18, 3]),
    ("Sn", "Tin", [2, 8, 18, 18, 4]), ("Sb", "Antimony", [2, 8, 18, 18, 5]), ("Te", "Tellurium", [2, 8, 18, 18, 6]),
    ("I", "Iodine", [2, 8, 18, 18, 7]), ("Xe", "Xenon", [2, 8, 18, 18, 8]),
]

ICONS = []
for z, (sym, name, sh) in enumerate(ELEMENTS, start=37):
    assert sum(sh) == z, sym
    key = f"{z:02d}-{name.lower()}"
    ICONS.append({
        "id": key,
        "name": f"{name} atom Bohr model",
        "title": f"{name} atom Bohr model icon, {sym} with {z} electrons ({', '.join(map(str, sh))}), "
                 "chemistry vector illustration",
        "keywords": [name.lower(), sym.lower(), f"{name.lower()} atom", f"atomic number {z}"],
        "body": '<g transform="translate(32 32)">' + bohr(z, sym, sh).replace("{p}", key) + "</g>",  # 5 kulit: geser agar muat
    })
