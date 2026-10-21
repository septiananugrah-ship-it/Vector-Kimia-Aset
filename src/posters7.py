"""Poster edukasi kimia jilid 7: perkembangan model atom dan hukum-hukum dasar kimia.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
import math
import random

from icons_lab_flat import O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, particle, text, tr
from posters2 import _card, _sign
from posters3 import arrow_line, mix
from posters4 import chem
from render import style_attrs

BLUE = "#3D7DDB"


def _dalton(cx, cy):
    return particle(cx, cy, 48, "#9AA5B1", "dal")


def _thomson(cx, cy):
    out = [particle(cx, cy, 52, "#F7A1B5", "tho", shine=False)]
    rnd = random.Random(3)
    for k in range(9):
        a = k * 40 + rnd.uniform(-10, 10)
        r = 18 + (k % 3) * 11
        x, y = cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))
        out.append(particle(x, y, 6.5, BLUE, f"te{k}", shine=False) + _sign(x, y, 3, "#FFFFFF", True))
    return "".join(out)


def _rutherford(cx, cy):
    out = []
    for a in (0, 60, 120):
        out.append(f'<ellipse cx="{cx}" cy="{cy}" rx="54" ry="20" transform="rotate({a} {cx} {cy})" fill="none" '
                   'stroke="#7C8B9C" stroke-width="2"/>')
    out.append(particle(cx, cy, 9, R, "rn", shine=False) + _sign(cx, cy, 4, "#FFFFFF"))
    for k, a in enumerate((0, 60, 120)):
        x = cx + 54 * math.cos(math.radians(a + 20))
        y = cy + 20 * math.sin(math.radians(a + 20))
        rx, ry = cx + (x - cx) * math.cos(math.radians(a)) - (y - cy) * math.sin(math.radians(a)), \
            cy + (x - cx) * math.sin(math.radians(a)) + (y - cy) * math.cos(math.radians(a))
        out.append(particle(rx, ry, 6, BLUE, f"re{k}", shine=False))
    return "".join(out)


def _bohr(cx, cy):
    out = []
    for r in (26, 44, 60):
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="#7C8B9C" stroke-width="2"/>')
    out.append(particle(cx, cy, 12, O, "bn", shine=False) + _sign(cx, cy, 5, "#FFFFFF"))
    for k, (r, a) in enumerate(((26, -90), (26, 90), (44, -30), (44, 150), (60, 20), (60, 200))):
        out.append(particle(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a)), 5.5, BLUE,
                            f"be{k}", shine=False))
    return "".join(out)


def _quantum(cx, cy):
    rnd = random.Random(7)
    out = []
    for k in range(260):
        r = abs(rnd.gauss(0, 24))
        a = rnd.uniform(0, 2 * math.pi)
        x, y = cx + r * math.cos(a), cy + r * math.sin(a)
        if math.hypot(x - cx, y - cy) > 62:
            continue
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.6" fill="{P}" stroke="none"/>')
    out.append(particle(cx, cy, 8, O, "qn", shine=False))
    return "".join(out)


MODELS = [
    ("Dalton", "1803", "Solid sphere model", "Atoms are tiny, indivisible solid spheres", _dalton),
    ("Thomson", "1904", "Plum pudding model", "Electrons embedded in a positive sphere", _thomson),
    ("Rutherford", "1911", "Nuclear model", "A tiny dense positive nucleus, electrons around it", _rutherford),
    ("Bohr", "1913", "Planetary model", "Electrons move in fixed energy levels (shells)", _bohr),
    ("Schrödinger", "1926", "Quantum mechanical model", "Electrons found in probability clouds (orbitals)",
     _quantum),
]


def atomic_models(th):
    W = 1226
    top = 122
    n = len(MODELS)
    cw = (W - 2 * MX - (n - 1) * 14) / n
    ch = 420
    H = top + 60 + ch + 40
    out = [header(W, th, "HISTORY OF ATOMIC MODELS", "How our picture of the atom developed from Dalton to quantum mechanics")]
    ty = top + 26
    out.append(f'<path d="M{MX + 20} {ty}H{W - MX - 20}" stroke="{th["accent"]}" stroke-width="3"/>')
    g = []
    for i, (who, year, model, desc, fn) in enumerate(MODELS):
        x = MX + i * (cw + 14)
        cx = x + cw / 2
        out.append(f'<circle cx="{cx}" cy="{ty}" r="9" fill="{th["accent"]}" stroke="{th["bg"]}" stroke-width="3"/>')
        y = top + 60
        out.append(_card(x, y, cw, ch, th))
        out.append(text(year, cx, y + 38, 24, th["accent"]))
        out.append(text(who, cx, y + 66, 19, th["ink"]))
        out.append(f'<circle cx="{cx}" cy="{y + 170}" r="78" fill="{th["plate"]}"/>')
        g.append(fn(cx, y + 170))
        out.append(fit_text(model, cx, y + 288, 15, th["ink"], cw - 20, "Bold"))
        words = tr(desc).split()
        lines, cur = [], ""
        for w_ in words:
            if len(cur) + len(w_) > 24 and cur:
                lines.append(cur)
                cur = w_
            else:
                cur = (cur + " " + w_).strip()
        lines.append(cur)
        for k, line in enumerate(lines[:4]):
            out.append(text(line, cx, y + 318 + k * 19, 12.5, th["sub"], "Regular"))
        if i < n - 1:
            out.append(arrow_line(x + cw - 4, y + 170, x + cw + 18, y + 170, th["accent"], 2.4))
    out.append(f'<g {style_attrs(1.3)}>' + "".join(g) + "</g>")
    return W, H, "".join(out)


LAWS = [
    ("Law of conservation of mass", "Lavoisier", "Total mass of reactants = total mass of products",
     "C + O_{2} → CO_{2}   12 g + 32 g = 44 g", T),
    ("Law of definite proportions", "Proust", "A compound always contains its elements in a fixed mass ratio",
     "H_{2}O → mass H : O = 1 : 8", O),
    ("Law of multiple proportions", "Dalton", "Masses of one element combining with a fixed mass of another are in "
     "small whole-number ratios", "CO and CO_{2} → O mass ratio 1 : 2", P),
    ("Law of combining volumes", "Gay-Lussac", "Volumes of reacting gases are in small whole-number ratios",
     "2H_{2} + O_{2} → 2H_{2}O (gas)   2 : 1 : 2", R),
    ("Avogadro's law", "Avogadro", "Equal volumes of gases at the same temperature and pressure contain the same "
     "number of molecules", "V_{1}/n_{1} = V_{2}/n_{2}", BLUE),
]


def basic_laws(th):
    W = 1226
    top = 122
    rh = 112
    H = top + len(LAWS) * (rh + 12) + 26
    out = [header(W, th, "BASIC LAWS OF CHEMISTRY", "Five fundamental laws describing how substances combine")]
    for i, (name, who, desc, ex, col) in enumerate(LAWS):
        y = top + i * (rh + 12)
        out.append(_card(MX, y, W - 2 * MX, rh, th))
        out.append(f'<rect x="{MX}" y="{y}" width="10" height="{rh}" rx="5" fill="{col}"/>')
        out.append(text(name, MX + 32, y + 38, 20, th["ink"], "Bold", "start"))
        out.append(text(who, MX + 32, y + 62, 13, col if th["bg"] == "#FFFFFF" else mix(col, "#FFFFFF", .3),
                        "Bold", "start"))
        out.append(fit_text(desc, MX + 32, y + 90, 13, th["sub"], 560, "Regular", anchor="start"))
        bx = MX + 640
        out.append(f'<rect x="{bx}" y="{y + 22}" width="{W - MX - 22 - bx}" height="{rh - 44}" rx="12" '
                   f'fill="{th["plate"]}"/>')
        out.append(chem(tr(ex), bx + (W - MX - 22 - bx) / 2, y + rh / 2 + 7, 18, "#1E2A3A", "middle"))
    return W, H, "".join(out)


POSTERS = [
    ("atomic-models", atomic_models, "History of atomic models timeline, Dalton, Thomson, Rutherford, Bohr and "
     "quantum model",
     ["atomic model", "history of atom", "dalton", "thomson", "rutherford", "bohr", "schrodinger", "quantum model",
      "plum pudding", "nucleus", "electron", "timeline", "atomic theory", "physics"]),
    ("basic-laws", basic_laws, "Basic laws of chemistry chart, conservation of mass, definite and multiple "
     "proportions, Gay-Lussac and Avogadro",
     ["laws of chemistry", "conservation of mass", "lavoisier", "proust", "definite proportions",
      "multiple proportions", "dalton", "gay-lussac", "avogadro", "stoichiometry", "chemical laws",
      "combining volumes", "mass ratio", "fundamental laws"]),
]

TR.update({
    "HISTORY OF ATOMIC MODELS": "PERKEMBANGAN MODEL ATOM",
    "How our picture of the atom developed from Dalton to quantum mechanics":
        "Perkembangan gambaran tentang atom dari Dalton hingga mekanika kuantum",
    "Solid sphere model": "Model bola pejal", "Plum pudding model": "Model roti kismis",
    "Nuclear model": "Model inti atom", "Planetary model": "Model tata surya",
    "Quantum mechanical model": "Model mekanika kuantum",
    "Atoms are tiny, indivisible solid spheres": "Atom adalah bola pejal kecil yang tidak dapat dibagi",
    "Electrons embedded in a positive sphere": "Elektron tersebar dalam bola bermuatan positif",
    "A tiny dense positive nucleus, electrons around it": "Inti positif yang kecil dan padat dikelilingi elektron",
    "Electrons move in fixed energy levels (shells)": "Elektron bergerak pada tingkat energi (kulit) tertentu",
    "Electrons found in probability clouds (orbitals)": "Elektron berada dalam awan kebolehjadian (orbital)",
    "BASIC LAWS OF CHEMISTRY": "HUKUM-HUKUM DASAR KIMIA",
    "Five fundamental laws describing how substances combine": "Lima hukum dasar tentang cara zat-zat bergabung",
    "Law of conservation of mass": "Hukum kekekalan massa", "Law of definite proportions": "Hukum perbandingan tetap",
    "Law of multiple proportions": "Hukum perbandingan berganda",
    "Law of combining volumes": "Hukum perbandingan volume", "Avogadro's law": "Hukum Avogadro",
    "Total mass of reactants = total mass of products": "Massa zat sebelum reaksi = massa zat sesudah reaksi",
    "A compound always contains its elements in a fixed mass ratio":
        "Perbandingan massa unsur-unsur dalam suatu senyawa selalu tetap",
    "Masses of one element combining with a fixed mass of another are in small whole-number ratios":
        "Perbandingan massa unsur yang bergabung dengan massa tetap unsur lain berupa bilangan bulat sederhana",
    "Volumes of reacting gases are in small whole-number ratios":
        "Perbandingan volume gas-gas yang bereaksi berupa bilangan bulat sederhana",
    "H_{2}O → mass H : O = 1 : 8": "H_{2}O → massa H : O = 1 : 8",
    "CO and CO_{2} → O mass ratio 1 : 2": "CO dan CO_{2} → perbandingan massa O = 1 : 2",
    "Equal volumes of gases at the same temperature and pressure contain the same number of molecules":
        "Pada suhu dan tekanan sama, gas bervolume sama mengandung jumlah molekul yang sama",
})
