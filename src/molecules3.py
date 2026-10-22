"""Set 20 model molekul bola-dan-batang jilid 3, gaya semi-flat."""
import molecules
from molecules import molecule
from molecules2 import COLOR, RADIUS  # kamus bersama yang sudah memuat warna P dan Si

COLOR.update({"F": "#9BE07A", "Br": "#A8432F", "I": "#7B4FB0", "B": "#F2B48A"})
RADIUS.update({"F": 5.4, "Br": 7.2, "I": 7.8, "B": 5.8})

SET_ID = "molecule3-icons"
STROKE = 1.6
SHADOW = False
GLYPH = True
THEME = "chemistry molecule model"
PATTERNS = [("#FFF5F0", "#E85D4A", "colorful molecules on peach")]

SET_TITLE = "Molecule ball and stick models icons set vol. 3, 20 colorful chemistry vector illustrations"
SET_KEYWORDS = molecules.SET_KEYWORDS[:20] + ["ethane", "glycine", "phosphoric acid", "carbonic acid",
                                              "sulfur hexafluoride", "isopropanol", "chlorine", "iodine",
                                              "boron trifluoride", "nitrous oxide", "methylamine"]
COMMON_KEYWORDS = molecules.COMMON_KEYWORDS

MOLS = [
    ("ethane", "Ethane molecule C2H6", ["ethane", "c2h6", "alkane", "hydrocarbon", "gas", "fuel"],
     [("C", -6, -2), ("C", 6, 2), ("H", -14, -7), ("H", -10, 8), ("H", -2, -11), ("H", 14, 7), ("H", 10, -8),
      ("H", 2, 11)],
     [(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1), (1, 5, 1), (1, 6, 1), (1, 7, 1)]),
    ("dimethyl-ether", "Dimethyl ether molecule CH3OCH3", ["dimethyl ether", "ether", "c2h6o", "propellant", "isomer",
                                                          "organic"],
     [("C", -12, 4), ("O", 0, -2), ("C", 12, 4), ("H", -20, -1), ("H", -16, 12), ("H", -8, 12), ("H", 20, -1),
      ("H", 16, 12), ("H", 8, 12)],
     [(0, 1, 1), (1, 2, 1), (0, 3, 1), (0, 4, 1), (0, 5, 1), (2, 6, 1), (2, 7, 1), (2, 8, 1)]),
    ("acetaldehyde", "Acetaldehyde molecule CH3CHO", ["acetaldehyde", "ethanal", "aldehyde", "ch3cho", "organic",
                                                      "carbonyl"],
     [("C", -8, 3), ("C", 5, -3), ("O", 5, -15), ("H", 14, 2), ("H", -16, -2), ("H", -12, 11), ("H", -3, 11)],
     [(0, 1, 1), (1, 2, 2), (1, 3, 1), (0, 4, 1), (0, 5, 1), (0, 6, 1)]),
    ("hydrogen-fluoride", "Hydrogen fluoride molecule HF", ["hydrogen fluoride", "hf", "hydrofluoric acid", "fluorine",
                                                            "acid", "gas"],
     [("H", -6, 0), ("F", 5, 0)], [(0, 1, 1)]),
    ("chlorine", "Chlorine molecule Cl2", ["chlorine", "cl2", "halogen", "disinfectant", "gas", "diatomic"],
     [("Cl", -6.5, 0), ("Cl", 6.5, 0)], [(0, 1, 1)]),
    ("fluorine", "Fluorine molecule F2", ["fluorine", "f2", "halogen", "reactive", "gas", "diatomic"],
     [("F", -6, 0), ("F", 6, 0)], [(0, 1, 1)]),
    ("nitrous-oxide", "Nitrous oxide molecule N2O", ["nitrous oxide", "n2o", "laughing gas", "anesthetic", "gas",
                                                      "linear"],
     [("N", -12, 0), ("N", 0, 0), ("O", 12, 0)], [(0, 1, 2), (1, 2, 2)]),
    ("carbonic-acid", "Carbonic acid molecule H2CO3", ["carbonic acid", "h2co3", "soda", "acid", "carbon dioxide",
                                                       "weak acid"],
     [("C", 0, 0), ("O", 0, -12), ("O", -11, 6), ("O", 11, 6), ("H", -19, 1), ("H", 19, 1)],
     [(0, 1, 2), (0, 2, 1), (0, 3, 1), (2, 4, 1), (3, 5, 1)]),
    ("phosphoric-acid", "Phosphoric acid molecule H3PO4", ["phosphoric acid", "h3po4", "acid", "phosphorus",
                                                           "fertilizer", "cola"],
     [("P", 0, 0), ("O", 0, -13), ("O", -12, 6), ("O", 12, 6), ("O", 0, 13), ("H", -20, 1), ("H", 20, 1),
      ("H", 8, 18)],
     [(0, 1, 2), (0, 2, 1), (0, 3, 1), (0, 4, 1), (2, 5, 1), (3, 6, 1), (4, 7, 1)]),
    ("methylamine", "Methylamine molecule CH3NH2", ["methylamine", "ch3nh2", "amine", "organic base", "nitrogen",
                                                    "gas"],
     [("C", -6, 0), ("N", 7, 0), ("H", -13, -7), ("H", -13, 7), ("H", -4, 11), ("H", 13, -7), ("H", 13, 7)],
     [(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1), (1, 5, 1), (1, 6, 1)]),
    ("ethylene-glycol", "Ethylene glycol molecule C2H6O2", ["ethylene glycol", "antifreeze", "diol", "alcohol",
                                                            "coolant", "c2h6o2"],
     [("C", -6, -3), ("C", 6, 3), ("O", -18, 2), ("O", 18, -2), ("H", -24, -4), ("H", 24, 4), ("H", -2, -13),
      ("H", -6, 8), ("H", 2, 13), ("H", 6, -8)],
     [(0, 1, 1), (0, 2, 1), (1, 3, 1), (2, 4, 1), (3, 5, 1), (0, 6, 1), (0, 7, 1), (1, 8, 1), (1, 9, 1)]),
    ("boron-trifluoride", "Boron trifluoride molecule BF3", ["boron trifluoride", "bf3", "boron", "lewis acid",
                                                              "trigonal planar", "fluorine"],
     [("B", 0, 0), ("F", 0, -12), ("F", -10.4, 6), ("F", 10.4, 6)], [(0, 1, 1), (0, 2, 1), (0, 3, 1)]),
    ("sulfur-hexafluoride", "Sulfur hexafluoride molecule SF6", ["sulfur hexafluoride", "sf6", "octahedral",
                                                                  "insulating gas", "fluorine", "sulfur"],
     [("S", 0, 0), ("F", 0, -14), ("F", 0, 14), ("F", -14, 0), ("F", 14, 0), ("F", -8, 8), ("F", 8, -8)],
     [(0, i, 1) for i in range(1, 7)]),
    ("phosphorus-pentachloride", "Phosphorus pentachloride molecule PCl5", ["phosphorus pentachloride", "pcl5",
                                                                            "trigonal bipyramidal", "chlorine",
                                                                            "phosphorus", "reagent"],
     [("P", 0, 0), ("Cl", 0, -15), ("Cl", 0, 15), ("Cl", -15, 2), ("Cl", 10, 8), ("Cl", 11, -6)],
     [(0, i, 1) for i in range(1, 6)]),
    ("glycine", "Glycine molecule NH2CH2COOH", ["glycine", "amino acid", "protein", "biochemistry", "c2h5no2",
                                                "organic"],
     [("N", -15, 3), ("C", -4, -2), ("C", 8, 3), ("O", 8, 15), ("O", 19, -2), ("H", 27, 1), ("H", -4, -13),
      ("H", -2, 9), ("H", -22, -2), ("H", -18, 12)],
     [(0, 1, 1), (1, 2, 1), (2, 3, 2), (2, 4, 1), (4, 5, 1), (1, 6, 1), (1, 7, 1), (0, 8, 1), (0, 9, 1)]),
    ("isopropanol", "Isopropyl alcohol molecule C3H8O", ["isopropyl alcohol", "isopropanol", "rubbing alcohol",
                                                         "propan-2-ol", "disinfectant", "alcohol"],
     [("C", 0, 0), ("C", -12, -6), ("C", 12, -6), ("O", 0, 12), ("H", 8, 17), ("H", 0, -11), ("H", -20, -1),
      ("H", -14, -15), ("H", -21, -12), ("H", 20, -1), ("H", 14, -15), ("H", 21, -12)],
     [(0, 1, 1), (0, 2, 1), (0, 3, 1), (3, 4, 1), (0, 5, 1), (1, 6, 1), (1, 7, 1), (1, 8, 1), (2, 9, 1),
      (2, 10, 1), (2, 11, 1)]),
    ("hypochlorous-acid", "Hypochlorous acid molecule HOCl", ["hypochlorous acid", "hocl", "disinfectant", "bleach",
                                                              "chlorine", "acid"],
     [("H", -12, 4), ("O", -3, -2), ("Cl", 10, 2)], [(0, 1, 1), (1, 2, 1)]),
    ("hydrogen-bromide", "Hydrogen bromide molecule HBr", ["hydrogen bromide", "hbr", "hydrobromic acid", "bromine",
                                                           "acid", "gas"],
     [("H", -7, 0), ("Br", 5, 0)], [(0, 1, 1)]),
    ("iodine", "Iodine molecule I2", ["iodine", "i2", "halogen", "antiseptic", "purple", "diatomic"],
     [("I", -7, 0), ("I", 7, 0)], [(0, 1, 1)]),
    ("carbon-disulfide", "Carbon disulfide molecule CS2", ["carbon disulfide", "cs2", "solvent", "sulfur", "linear",
                                                           "carbon"],
     [("S", -13, 0), ("C", 0, 0), ("S", 13, 0)], [(0, 1, 2), (1, 2, 2)]),
]

# molekul yang atomnya terlalu rapat: panjangkan ikatan
SPREAD = {"ethane": 1.5, "methylamine": 1.4, "sulfur-hexafluoride": 1.35, "phosphorus-pentachloride": 1.3,
          "isopropanol": 1.3, "acetaldehyde": 1.25, "ethylene-glycol": 1.15, "glycine": 1.15}

ICONS = []
for mid, name, kw, atoms_, bonds in MOLS:
    k = SPREAD.get(mid, 1)
    atoms_ = [(el, x * k, y * k) for el, x, y in atoms_]
    ICONS.append({
        "id": mid,
        "name": f"{name} ball and stick model",
        "title": f"{name} ball and stick model icon, chemistry vector illustration",
        "keywords": kw,
        "body": molecule(atoms_, bonds).replace("{p}", mid),
    })
