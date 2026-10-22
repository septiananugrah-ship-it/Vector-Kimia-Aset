"""Lembar mewarnai A4 (potret) bertema kimia untuk anak/siswa, Inggris & Indonesia.

Ikon diambil dari set semi-flat lalu diubah ke outline (render.outlinify).
"""
import icons_concepts
import icons_lab2
import icons_lab_flat
import kawaii
import kawaii2
import kawaii3
import kawaii4
import molecules
import molecules3
import poster_kit
from poster_i18n import TR
from poster_kit import text, tr
from posters import LAB_NAMES
from render import GRID, fitted, outlinify, style_attrs

SET_ID = "chemistry-coloring-pages"
W, H = 800, 1131  # rasio A4

PAGES = [
    ("lab-tools-1", "LET'S COLOR THE LAB!", icons_lab_flat,
     ["erlenmeyer-flask", "microscope", "test-tube-rack", "bunsen-burner", "beaker", "thermometer"]),
    ("lab-tools-2", "LET'S COLOR THE LAB!", icons_lab2,
     ["lab-coat", "magnifying-glass", "spirit-lamp", "dropper-bottle", "gas-cylinder", "reaction-flask-smoke"]),
    ("science", "COLOR THE SCIENCE!", icons_concepts,
     ["atom", "dna", "magnet", "crystal", "idea-bulb", "chemistry-book"]),
    ("molecules", "COLOR THE MOLECULES!", molecules,
     ["water", "carbon-dioxide", "methane", "ammonia", "benzene", "oxygen"]),
    ("lab-tools-3", "LET'S COLOR THE LAB!", icons_lab_flat,
     ["round-bottom-flask", "volumetric-flask", "mortar-and-pestle", "funnel", "graduated-cylinder", "wash-bottle"]),
    ("lab-tools-4", "LET'S COLOR THE LAB!", icons_lab2,
     ["reagent-bottle", "separatory-funnel", "crucible", "syringe", "centrifuge", "magnetic-stirrer"]),
    ("science-2", "COLOR THE SCIENCE!", icons_concepts,
     ["battery", "water-drop", "green-chemistry", "lightning", "capsule", "benzene-ring"]),
    ("kawaii-lab-1", "COLOR THE CUTE LAB!", kawaii,
     ["erlenmeyer-flask", "beaker", "microscope", "test-tube", "round-bottom-flask", "bunsen-burner"]),
    ("kawaii-lab-2", "COLOR THE CUTE LAB!", kawaii2,
     ["reagent-bottle", "dropper-bottle", "spirit-lamp", "protective-gloves", "magnifying-glass", "fire-extinguisher"]),
    ("kawaii-science", "COLOR THE CUTE SCIENCE!", kawaii3,
     ["water-drop", "molecule", "lightning", "crystal", "gas-cloud", "idea-bulb"]),
    ("kawaii-molecules", "COLOR THE CUTE MOLECULES!", kawaii4,
     ["water", "ammonia", "carbon-dioxide", "ozone", "sulfur-dioxide", "hydrogen-chloride"]),
    ("molecules-2", "COLOR THE MOLECULES!", molecules3,
     ["ethane", "carbonic-acid", "boron-trifluoride", "phosphoric-acid", "glycine", "carbon-disulfide"]),
]

MOL_NAMES = {"ethane": "Ethane", "carbonic-acid": "Carbonic acid", "boron-trifluoride": "Boron trifluoride",
             "phosphoric-acid": "Phosphoric acid", "glycine": "Glycine", "carbon-disulfide": "Carbon disulfide",
             "ozone": "Ozone", "sulfur-dioxide": "Sulfur dioxide", "hydrogen-chloride": "Hydrogen chloride",
             "water": "Water", "carbon-dioxide": "Carbon dioxide", "methane": "Methane", "ammonia": "Ammonia",
             "benzene": "Benzene", "oxygen": "Oxygen"}


def name_of(icon_id):
    if icon_id == "dna":
        return "DNA"
    return MOL_NAMES.get(icon_id) or LAB_NAMES.get(icon_id) or icon_id.replace("-", " ").title()


def page(title, mod, ids):
    by_id = {ic["id"]: ic for ic in mod.ICONS}
    ink = "#1E2A3A"
    out = [f'<rect x="20" y="20" width="{W - 40}" height="{H - 40}" rx="28" fill="none" stroke="{ink}" '
           'stroke-width="4"/>',
           f'<rect x="32" y="32" width="{W - 64}" height="{H - 64}" rx="20" fill="none" stroke="{ink}" '
           'stroke-width="1.6" stroke-dasharray="2 8" stroke-linecap="round"/>',
           text(title, W / 2, 112, 46, ink),
           text("Name: ______________________", 70, H - 66, 20, ink, "SemiBold", "start")]
    cw, ch = (W - 140) / 2, (H - 330) / 3
    for i, icon_id in enumerate(ids):
        x = 70 + (i % 2) * cw
        y = 160 + (i // 2) * ch
        size = min(cw, ch) - 60
        ic = by_id[icon_id]
        if "plain" in ic:  # stiker kawaii: outline ikon polos + wajah bergaris, tanpa bingkai die-cut
            body = outlinify(ic["plain"]) + ic["face"].replace(
                'fill="#F7A1B5" stroke="none"', 'fill="#FFFFFF" stroke="#1E2A3A" stroke-width=".7"')
        else:
            body = outlinify(ic["body"])
        stroke = 2.2
        out.append(f'<g transform="translate({x + cw / 2 - size / 2:.1f} {y + 6:.1f}) scale({size / GRID:.4f})">'
                   f'<g {style_attrs(stroke)}>{fitted(body, stroke)}</g></g>')
        out.append(text(name_of(icon_id), x + cw / 2, y + size + 40, 22, ink, "Bold"))
    return "".join(out)


TR.update({
    "LET'S COLOR THE LAB!": "AYO WARNAI ALAT LAB!", "COLOR THE SCIENCE!": "AYO WARNAI SAINS!",
    "COLOR THE MOLECULES!": "AYO WARNAI MOLEKUL!", "Name: ______________________": "Nama: ______________________",
    "Atom": "Atom", "Magnet": "Magnet", "Crystal": "Kristal", "Idea Bulb": "Lampu Ide",
    "Chemistry Book": "Buku Kimia", "COLOR THE CUTE LAB!": "AYO WARNAI LAB LUCU!",
    "COLOR THE CUTE SCIENCE!": "AYO WARNAI SAINS LUCU!", "Battery": "Baterai", "Benzene Ring": "Cincin Benzena",
    "COLOR THE CUTE MOLECULES!": "AYO WARNAI MOLEKUL LUCU!", "Ethane": "Etana", "Carbonic acid": "Asam karbonat",
    "Boron trifluoride": "Boron trifluorida", "Phosphoric acid": "Asam fosfat", "Glycine": "Glisin",
    "Carbon disulfide": "Karbon disulfida", "Ozone": "Ozon", "Sulfur dioxide": "Belerang dioksida",
    "Hydrogen chloride": "Hidrogen klorida",
    "Capsule": "Kapsul", "Green Chemistry": "Kimia Hijau", "Molecule": "Molekul", "Gas Cloud": "Awan Gas", "Lightning": "Petir", "Water Drop": "Tetes Air",
})

KEYWORDS = ["coloring page", "coloring book", "coloring", "kids", "children", "worksheet", "printable",
            "activity", "black and white", "outline", "line art", "chemistry", "science", "laboratory", "education",
            "school", "preschool", "elementary", "classroom", "homeschool", "teacher", "a4", "page", "drawing",
            "cartoon", "vector", "illustration", "fun", "learning", "student"]


def assets():
    out = []
    for lang, suffix in (("en", ""), ("id", "-indonesian")):
        poster_kit.set_lang(lang)
        for key, title, mod, ids in PAGES:
            svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * 3}" height="{H * 3}" viewBox="0 0 {W} {H}">\n'
                   f'<rect x="-1" y="-1" width="{W + 2}" height="{H + 2}" fill="#FFFFFF"/>{page(tr(title), mod, ids)}'
                   '\n</svg>\n')
            note = " in Indonesian language" if lang == "id" else ""
            out.append(dict(name=f"{SET_ID}-{key}{suffix}", svg=svg, size=3508, png=False,
                            title=f"Chemistry coloring page for kids{note}, {key.replace('-', ' ')}, A4 printable "
                                  "black and white vector worksheet",
                            keywords=(["indonesian", "bahasa indonesia"] if lang == "id" else []) + KEYWORDS))
    poster_kit.set_lang("en")
    return [(SET_ID, out)]
