"""Set 07: 20 model molekul bola-dan-batang jilid 2, gaya semi-flat."""
import molecules
from molecules import COLOR, RADIUS, molecule

COLOR.update({"P": "#F28C28", "Si": "#D9B48A"})
RADIUS.update({"P": 6.6, "Si": 6.8})

SET_ID = "molecule2-icons"
STROKE = 1.6
SHADOW = False
GLYPH = True
THEME = "chemistry molecule model"
PATTERNS = [("#F2FBF6", "#5CBF7A", "colorful molecules on mint")]

SET_TITLE = "Molecule ball and stick models icons set vol. 2, 20 colorful chemistry vector illustrations"
SET_KEYWORDS = molecules.SET_KEYWORDS[:20] + ["acetic acid", "acetone", "urea", "propane", "butane",
                                              "hydrogen sulfide", "nitrogen dioxide", "sulfur trioxide",
                                              "chloroform", "sodium hydroxide", "nitric acid", "phosphine"]
COMMON_KEYWORDS = molecules.COMMON_KEYWORDS

MOLS = [
    ("hydrogen-sulfide", "Hydrogen sulfide molecule H2S", ["hydrogen sulfide", "h2s", "rotten egg gas", "sulfur", "toxic gas", "gas"],
     [("S", 0, -2), ("H", -11, 7), ("H", 11, 7)], [(0, 1, 1), (0, 2, 1)]),
    ("hydrogen-cyanide", "Hydrogen cyanide molecule HCN", ["hydrogen cyanide", "hcn", "cyanide", "poison", "toxic", "triple bond"],
     [("H", -17, 0), ("C", -7, 0), ("N", 6, 0)], [(0, 1, 1), (1, 2, 3)]),
    ("nitrogen-dioxide", "Nitrogen dioxide molecule NO2", ["nitrogen dioxide", "no2", "air pollution", "smog", "nitrogen", "gas"],
     [("N", 0, -3), ("O", -11, 5), ("O", 11, 5)], [(0, 1, 2), (0, 2, 1)]),
    ("sulfur-trioxide", "Sulfur trioxide molecule SO3", ["sulfur trioxide", "so3", "acid rain", "sulfur", "oxide", "pollution"],
     [("S", 0, 0), ("O", 0, -13), ("O", -11.3, 6.5), ("O", 11.3, 6.5)], [(0, 1, 2), (0, 2, 2), (0, 3, 2)]),
    ("carbon-tetrachloride", "Carbon tetrachloride molecule CCl4", ["carbon tetrachloride", "ccl4", "solvent", "chlorine", "tetrahedral", "halogen"],
     [("C", 0, 0), ("Cl", 0, -14), ("Cl", -13, 7), ("Cl", 13, 7), ("Cl", 4, 13)], [(0, i, 1) for i in range(1, 5)]),
    ("chloroform", "Chloroform molecule CHCl3", ["chloroform", "chcl3", "trichloromethane", "solvent", "anesthetic", "chlorine"],
     [("C", 0, 0), ("H", 0, -11), ("Cl", -13, 6), ("Cl", 13, 6), ("Cl", 3, 13)], [(0, i, 1) for i in range(1, 5)]),
    ("chloromethane", "Chloromethane molecule CH3Cl", ["chloromethane", "ch3cl", "methyl chloride", "haloalkane", "chlorine", "gas"],
     [("C", -4, 0), ("Cl", 10, 0), ("H", -12, -7), ("H", -12, 7), ("H", -2, 11)], [(0, i, 1) for i in range(1, 5)]),
    ("sodium-hydroxide", "Sodium hydroxide NaOH", ["sodium hydroxide", "naoh", "caustic soda", "lye", "base", "alkali"],
     [("Na", -13, 0), ("O", 0, 0), ("H", 9, -5)], [(0, 1, 1), (1, 2, 1)]),
    ("nitric-acid", "Nitric acid molecule HNO3", ["nitric acid", "hno3", "acid", "nitrogen", "corrosive", "fertilizer"],
     [("N", 0, 0), ("O", -10, -7), ("O", 10, -7), ("O", 0, 12), ("H", 8, 17)], [(0, 1, 2), (0, 2, 1), (0, 3, 1), (3, 4, 1)]),
    ("formic-acid", "Formic acid molecule HCOOH", ["formic acid", "hcooh", "methanoic acid", "ant", "carboxylic acid", "acid"],
     [("C", 0, 0), ("O", 0, -12), ("O", 11, 6), ("H", 19, 1), ("H", -10, 6)], [(0, 1, 2), (0, 2, 1), (2, 3, 1), (0, 4, 1)]),
    ("acetic-acid", "Acetic acid molecule CH3COOH", ["acetic acid", "ch3cooh", "vinegar", "ethanoic acid", "carboxylic acid", "acid"],
     [("C", -11, 3), ("C", 1, -3), ("O", 1, -15), ("O", 12, 3), ("H", 20, -1), ("H", -19, -2), ("H", -15, 11), ("H", -6, 11)],
     [(0, 1, 1), (1, 2, 2), (1, 3, 1), (3, 4, 1), (0, 5, 1), (0, 6, 1), (0, 7, 1)]),
    ("acetone", "Acetone molecule C3H6O", ["acetone", "propanone", "ketone", "nail polish remover", "solvent", "c3h6o"],
     [("C", 0, -2), ("O", 0, -14), ("C", -12, 5), ("C", 12, 5), ("H", -20, 0), ("H", -16, 13), ("H", -8, 13),
      ("H", 20, 0), ("H", 16, 13), ("H", 8, 13)],
     [(0, 1, 2), (0, 2, 1), (0, 3, 1), (2, 4, 1), (2, 5, 1), (2, 6, 1), (3, 7, 1), (3, 8, 1), (3, 9, 1)]),
    ("urea", "Urea molecule CO(NH2)2", ["urea", "carbamide", "fertilizer", "nitrogen", "organic compound", "amide"],
     [("C", 0, 0), ("O", 0, -12), ("N", -11, 6), ("N", 11, 6), ("H", -19, 1), ("H", -12, 15), ("H", 19, 1), ("H", 12, 15)],
     [(0, 1, 2), (0, 2, 1), (0, 3, 1), (2, 4, 1), (2, 5, 1), (3, 6, 1), (3, 7, 1)]),
    ("propane", "Propane molecule C3H8", ["propane", "c3h8", "lpg", "alkane", "fuel gas", "hydrocarbon"],
     [("C", -12, 3), ("C", 0, -3), ("C", 12, 3), ("H", -20, -2), ("H", -16, 12), ("H", -8, 12), ("H", -4, -12),
      ("H", 4, -12), ("H", 20, -2), ("H", 16, 12), ("H", 8, 12)],
     [(0, 1, 1), (1, 2, 1), (0, 3, 1), (0, 4, 1), (0, 5, 1), (1, 6, 1), (1, 7, 1), (2, 8, 1), (2, 9, 1), (2, 10, 1)]),
    ("propene", "Propene molecule C3H6", ["propene", "propylene", "c3h6", "alkene", "plastic", "hydrocarbon"],
     [("C", -12, 3), ("C", 0, -3), ("C", 12, 3), ("H", -20, -2), ("H", -14, 13), ("H", 0, -14), ("H", 20, -2),
      ("H", 16, 12), ("H", 8, 12)],
     [(0, 1, 2), (1, 2, 1), (0, 3, 1), (0, 4, 1), (1, 5, 1), (2, 6, 1), (2, 7, 1), (2, 8, 1)]),
    ("butane", "Butane molecule C4H10", ["butane", "c4h10", "lighter fuel", "alkane", "lpg", "hydrocarbon"],
     [("C", -18, 3), ("C", -6, -3), ("C", 6, 3), ("C", 18, -3), ("H", -26, -2), ("H", -22, 12), ("H", -14, 12),
      ("H", -10, -12), ("H", -2, -12), ("H", 2, 12), ("H", 10, 12), ("H", 26, 2), ("H", 22, -12), ("H", 14, -12)],
     [(0, 1, 1), (1, 2, 1), (2, 3, 1), (0, 4, 1), (0, 5, 1), (0, 6, 1), (1, 7, 1), (1, 8, 1), (2, 9, 1), (2, 10, 1),
      (3, 11, 1), (3, 12, 1), (3, 13, 1)]),
    ("nitric-oxide", "Nitric oxide molecule NO", ["nitric oxide", "no", "nitrogen monoxide", "gas", "radical", "signaling"],
     [("N", -6.5, 0), ("O", 6.5, 0)], [(0, 1, 2)]),
    ("phosphine", "Phosphine molecule PH3", ["phosphine", "ph3", "phosphorus", "toxic gas", "hydride", "gas"],
     [("P", 0, -3), ("H", -11, 4), ("H", 11, 4), ("H", 0, 10)], [(0, 1, 1), (0, 2, 1), (0, 3, 1)]),
    ("hydrazine", "Hydrazine molecule N2H4", ["hydrazine", "n2h4", "rocket fuel", "nitrogen", "propellant", "chemical"],
     [("N", -6, 0), ("N", 6, 0), ("H", -12, -8), ("H", -12, 8), ("H", 12, -8), ("H", 12, 8)],
     [(0, 1, 1), (0, 2, 1), (0, 3, 1), (1, 4, 1), (1, 5, 1)]),
    ("silane", "Silane molecule SiH4", ["silane", "sih4", "silicon", "hydride", "semiconductor", "gas"],
     [("Si", 0, 0), ("H", 0, -12), ("H", -11, 5), ("H", 11, 5), ("H", 3, 11)], [(0, i, 1) for i in range(1, 5)]),
]

ICONS = []
for mid, name, kw, atoms_, bonds in MOLS:
    ICONS.append({
        "id": mid,
        "name": f"{name} ball and stick model",
        "title": f"{name} ball and stick model icon, chemistry vector illustration",
        "keywords": kw,
        "body": molecule(atoms_, bonds).replace("{p}", mid),
    })
