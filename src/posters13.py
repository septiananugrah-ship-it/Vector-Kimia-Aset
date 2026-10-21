"""Poster edukasi kimia jilid 13: aturan bilangan oksidasi dan reaksi redoks.
Didaftarkan ke posters.py lewat POSTERS (3 tema x 2 bahasa).
"""
from icons_lab_flat import L, O, P, R, T
from poster_i18n import TR
from poster_kit import MX, fit_text, header, text, tr
from posters2 import _card
from posters4 import chem

RULES = [
    ("Free elements have an oxidation number of 0", "Fe, O_{2}, N_{2} → 0"),
    ("A monatomic ion equals its charge", "Na^{+} = +1, Cl^{−} = −1"),
    ("Oxygen is usually −2 (−1 in peroxides)", "H_{2}O: O = −2"),
    ("Hydrogen is usually +1 (−1 in metal hydrides)", "HCl: H = +1"),
    ("Fluorine is always −1", "HF: F = −1"),
    ("Group 1 metals are +1, group 2 metals are +2", "Na = +1, Mg = +2"),
    ("The sum in a neutral compound is 0", "H_{2}SO_{4}: 2(+1) + S + 4(−2) = 0"),
    ("The sum in a polyatomic ion equals its charge", "SO_{4}^{2−}: S + 4(−2) = −2"),
]


def ox_rules(th):
    W = 1226
    top = 122
    rh = 70
    H = top + len(RULES) * (rh + 10) + 30
    cols = [T, O, R, "#3D7DDB", P, L, T, O]
    out = [header(W, th, "OXIDATION NUMBER RULES", "Eight rules for assigning oxidation numbers to atoms")]
    for i, (rule, ex) in enumerate(RULES):
        y = top + i * (rh + 10)
        out.append(_card(MX, y, W - 2 * MX, rh, th, rx=12))
        out.append(f'<circle cx="{MX + 36}" cy="{y + rh / 2}" r="19" fill="{cols[i]}"/>'
                   + text(str(i + 1), MX + 36, y + rh / 2 + 7, 18, "#FFFFFF"))
        out.append(fit_text(rule, MX + 70, y + rh / 2 + 6, 17, th["ink"], 600, "SemiBold", anchor="start"))
        bx = MX + 700
        out.append(f'<rect x="{bx}" y="{y + 12}" width="{W - MX - 14 - bx}" height="{rh - 24}" rx="10" '
                   f'fill="{th["plate"]}"/>')
        out.append(chem(ex, bx + (W - MX - 14 - bx) / 2, y + rh / 2 + 7, 17, "#1E2A3A", "middle"))
    return W, H, "".join(out)


def redox(th):
    W = 1226
    top = 122
    H = top + 560
    out = [header(W, th, "REDOX REACTIONS", "Oxidation and reduction always happen together")]
    cw = (W - 2 * MX - 24) / 2
    for k, (name, lines, col) in enumerate((
            ("Oxidation", ["Loss of electrons", "Oxidation number increases", "Happens to the reducing agent"], R),
            ("Reduction", ["Gain of electrons", "Oxidation number decreases", "Happens to the oxidizing agent"],
             "#3D7DDB"))):
        x = MX + k * (cw + 24)
        out.append(_card(x, top, cw, 220, th))
        out.append(f'<rect x="{x}" y="{top}" width="{cw}" height="58" rx="14" fill="{col}"/>'
                   f'<rect x="{x}" y="{top + 32}" width="{cw}" height="26" fill="{col}"/>')
        out.append(text(name, x + cw / 2, top + 39, 24, "#FFFFFF"))
        for i, line in enumerate(lines):
            y = top + 96 + i * 40
            out.append(f'<circle cx="{x + 34}" cy="{y - 6}" r="6" fill="{col}"/>')
            out.append(text(line, x + 52, y, 17, th["ink"], "SemiBold", "start"))
    ey = top + 248
    out.append(_card(MX, ey, W - 2 * MX, 280, th))
    out.append(text("Example", W / 2, ey + 40, 18, th["ink"]))
    out.append(chem("Zn(s) + Cu^{2+}(aq) → Zn^{2+}(aq) + Cu(s)", W / 2, ey + 92, 30, th["accent"], "middle"))
    out.append(fit_text("Zn is oxidized (0 → +2) and acts as the reducing agent", W / 2, ey + 150, 16, R,
                        W - 2 * MX - 60, "SemiBold"))
    out.append(fit_text("Cu²⁺ is reduced (+2 → 0) and acts as the oxidizing agent", W / 2, ey + 186, 16, "#3D7DDB",
                        W - 2 * MX - 60, "SemiBold"))
    out.append(text("Memory aid: OIL RIG = Oxidation Is Loss, Reduction Is Gain (of electrons)", W / 2, ey + 256, 13,
                    th["sub"], "SemiBold") if tr("Example") == "Example" else
               text("Oksidasi = melepas elektron · Reduksi = menerima elektron", W / 2, ey + 256, 13, th["sub"],
                    "SemiBold"))
    return W, H, "".join(out)


POSTERS = [
    ("oxidation-number-rules", ox_rules, "Oxidation number rules chart with examples",
     ["oxidation number", "oxidation state", "rules", "redox", "electrochemistry", "valence", "charge", "compound",
      "polyatomic ion", "peroxide", "hydride", "assigning oxidation numbers", "chemistry rules", "examples"]),
    ("redox-reactions", redox, "Redox reactions chart, oxidation and reduction with zinc and copper example",
     ["redox", "oxidation", "reduction", "electrons", "oxidizing agent", "reducing agent", "oil rig", "zinc",
      "copper", "electron transfer", "oxidation number", "electrochemistry", "reaction", "chemical change"]),
]

TR.update({
    "OXIDATION NUMBER RULES": "ATURAN BILANGAN OKSIDASI",
    "Eight rules for assigning oxidation numbers to atoms": "Delapan aturan menentukan bilangan oksidasi atom",
    "Free elements have an oxidation number of 0": "Unsur bebas memiliki bilangan oksidasi 0",
    "A monatomic ion equals its charge": "Ion monoatom = muatan ionnya",
    "Oxygen is usually −2 (−1 in peroxides)": "Oksigen umumnya −2 (−1 pada peroksida)",
    "Hydrogen is usually +1 (−1 in metal hydrides)": "Hidrogen umumnya +1 (−1 pada hidrida logam)",
    "Fluorine is always −1": "Fluorin selalu −1",
    "Group 1 metals are +1, group 2 metals are +2": "Logam golongan IA = +1, golongan IIA = +2",
    "The sum in a neutral compound is 0": "Jumlah biloks dalam senyawa netral = 0",
    "The sum in a polyatomic ion equals its charge": "Jumlah biloks dalam ion poliatom = muatan ionnya",
    "REDOX REACTIONS": "REAKSI REDOKS",
    "Oxidation and reduction always happen together": "Oksidasi dan reduksi selalu terjadi bersamaan",
    "Loss of electrons": "Melepas elektron", "Gain of electrons": "Menerima elektron",
    "Oxidation number increases": "Bilangan oksidasi naik", "Oxidation number decreases": "Bilangan oksidasi turun",
    "Happens to the reducing agent": "Dialami oleh reduktor", "Happens to the oxidizing agent": "Dialami oleh oksidator",
    "Zn is oxidized (0 → +2) and acts as the reducing agent": "Zn teroksidasi (0 → +2) dan berperan sebagai reduktor",
    "Cu²⁺ is reduced (+2 → 0) and acts as the oxidizing agent": "Cu²⁺ tereduksi (+2 → 0) dan berperan sebagai oksidator",
})
