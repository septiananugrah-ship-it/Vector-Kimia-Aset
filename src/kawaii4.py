"""Set stiker kawaii molekul: model molekul bola-dan-batang diberi wajah lucu pada atom terbesar
dan bingkai putih die-cut. Atom gelap (karbon, iodin) memakai wajah putih supaya terlihat.
"""
import kawaii
import molecules
import molecules2
import molecules3
from kawaii import die_cut, face
from molecules import RADIUS, molecule

SET_ID = "kawaii-molecule-stickers"
STROKE = 1.6
SHADOW = False
PATTERNS = [("#EEF6FF", "#3D7DDB", "cute pastel blue molecules"), ("#FFF0F4", "#E85D7A", "cute pastel pink molecules")]
THEME = "cute kawaii chemistry molecule"
COMMON_KEYWORDS = kawaii.COMMON_KEYWORDS + ["molecule", "atom"]

PICK = ["water", "ammonia", "methane", "carbon-dioxide", "ozone", "sulfur-dioxide", "hydrogen-peroxide",
        "hydrogen-chloride", "oxygen", "hydrogen-sulfide", "nitrogen-dioxide", "sulfur-trioxide", "phosphine",
        "silane", "hydrogen-fluoride", "chlorine", "boron-trifluoride", "sulfur-hexafluoride", "iodine",
        "phosphoric-acid"]
SET_TITLE = f"Cute kawaii molecule stickers set, {len(PICK)} happy chemistry molecule cartoon characters vector"
SET_KEYWORDS = [
    "kawaii", "cute", "sticker", "stickers", "molecule", "molecules", "atom", "character", "mascot", "happy",
    "smile", "face", "cartoon", "chemistry", "science", "kids", "school", "education", "funny", "adorable",
    "water molecule", "ammonia", "methane", "carbon dioxide", "ozone", "die cut", "printable", "clipart", "vector",
    "illustration", "isolated", "colorful", "emoji",
]
DARK = {"C", "I", "Br"}


def _face(el, x, y):
    r = RADIUS[el]
    f = face(x, y + r * .24, r * .12)
    if el in DARK:
        f = f.replace('fill="#1E2A3A"', 'fill="#FFFFFF"').replace('stroke="#1E2A3A"', 'stroke="#FFFFFF"')
    return f


DATA = {}
for mod in (molecules, molecules2, molecules3):
    spread = getattr(mod, "SPREAD", {})
    for mid, name, kw, atoms_, bonds in mod.MOLS:
        k = spread.get(mid, 1)
        DATA[mid] = (name, kw, [(el, x * k, y * k) for el, x, y in atoms_], bonds)

ICONS = []
for mid in PICK:
    name, kw, atoms_, bonds = DATA[mid]
    el, x, y = max(atoms_, key=lambda a: RADIUS[a[0]])
    body = molecule(atoms_, bonds).replace("{p}", f"kw-{mid}")
    short = name.split(" molecule")[0]
    ICONS.append({
        "id": mid,
        "title": f"Cute kawaii {short.lower()} molecule sticker with happy face, chemistry cartoon character vector",
        "keywords": kw[:6] + ["kawaii molecule", "cute " + short.lower()],
        "body": die_cut(body) + body + _face(el, x, y),
        "plain": body, "face": _face(el, x, y),
    })
