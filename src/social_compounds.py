"""Paket post Instagram "Compound of the day": 40 senyawa (model molekul dari molecules + molecules2),
tema navy, bahasa Inggris & Indonesia.
"""
import molecules
import molecules2
import poster_kit
from poster_i18n import TR
from poster_kit import text
from posters4 import chem
from render import GRID, fitted, style_attrs
from social import KEYWORDS, PALETTES, handle, hexes, para, pill

# id: (nama EN, nama ID, rumus, massa molar g/mol, kegunaan EN, kegunaan ID)
DATA = {
    "water": ("Water", "Air", "H_{2}O", "18.02", "The universal solvent, essential for all life",
              "Pelarut universal, penting bagi semua makhluk hidup"),
    "carbon-dioxide": ("Carbon dioxide", "Karbon dioksida", "CO_{2}", "44.01",
                       "Used by plants in photosynthesis and in fizzy drinks",
                       "Dipakai tumbuhan untuk fotosintesis dan dalam minuman bersoda"),
    "methane": ("Methane", "Metana", "CH_{4}", "16.04", "Main component of natural gas fuel",
                "Komponen utama bahan bakar gas alam"),
    "ammonia": ("Ammonia", "Amonia", "NH_{3}", "17.03", "Used to make fertilizers and cleaning products",
                "Bahan pembuat pupuk dan cairan pembersih"),
    "oxygen": ("Oxygen", "Oksigen", "O_{2}", "32.00", "Needed for breathing and for burning",
               "Diperlukan untuk bernapas dan pembakaran"),
    "nitrogen": ("Nitrogen", "Nitrogen", "N_{2}", "28.01", "Makes up 78% of the air; keeps snacks fresh",
                 "Menyusun 78% udara; menjaga camilan tetap renyah"),
    "hydrogen": ("Hydrogen", "Hidrogen", "H_{2}", "2.02", "The lightest gas, a clean fuel for the future",
                 "Gas paling ringan, bahan bakar bersih masa depan"),
    "hydrogen-chloride": ("Hydrochloric acid", "Asam klorida", "HCl", "36.46",
                          "Found in stomach acid; used to clean steel",
                          "Terdapat dalam asam lambung; untuk membersihkan baja"),
    "ethanol": ("Ethanol", "Etanol", "C_{2}H_{5}OH", "46.07", "Used in hand sanitizer and as biofuel",
                "Dipakai dalam hand sanitizer dan sebagai bioetanol"),
    "benzene": ("Benzene", "Benzena", "C_{6}H_{6}", "78.11", "Raw material for plastics, dyes and detergents",
                "Bahan baku plastik, zat warna, dan deterjen"),
    "ethylene": ("Ethylene", "Etilena", "C_{2}H_{4}", "28.05", "Makes polyethylene and helps fruit ripen",
                 "Bahan polietilena dan membantu buah matang"),
    "acetylene": ("Acetylene", "Asetilena", "C_{2}H_{2}", "26.04", "Burns very hot in welding torches",
                  "Nyalanya sangat panas untuk mengelas logam"),
    "sulfur-dioxide": ("Sulfur dioxide", "Belerang dioksida", "SO_{2}", "64.07",
                       "Food preservative; a cause of acid rain", "Pengawet makanan; penyebab hujan asam"),
    "hydrogen-peroxide": ("Hydrogen peroxide", "Hidrogen peroksida", "H_{2}O_{2}", "34.01",
                          "Antiseptic for wounds and a bleaching agent", "Antiseptik luka dan zat pemutih"),
    "sodium-chloride": ("Sodium chloride", "Natrium klorida", "NaCl", "58.44", "Table salt that seasons and preserves "
                        "food", "Garam dapur untuk membumbui dan mengawetkan makanan"),
    "formaldehyde": ("Formaldehyde", "Formaldehida", "CH_{2}O", "30.03", "Used to make resins and preserve specimens",
                     "Bahan resin dan pengawet spesimen"),
    "methanol": ("Methanol", "Metanol", "CH_{3}OH", "32.04", "Solvent and fuel; toxic if swallowed",
                 "Pelarut dan bahan bakar; beracun bila tertelan"),
    "ozone": ("Ozone", "Ozon", "O_{3}", "48.00", "The ozone layer blocks harmful UV rays",
              "Lapisan ozon menahan sinar UV berbahaya"),
    "carbon-monoxide": ("Carbon monoxide", "Karbon monoksida", "CO", "28.01",
                        "A colorless, odorless and very toxic gas", "Gas tak berwarna, tak berbau, dan sangat beracun"),
    "sulfuric-acid": ("Sulfuric acid", "Asam sulfat", "H_{2}SO_{4}", "98.08",
                      "Used in car batteries and fertilizers", "Dipakai dalam aki mobil dan pupuk"),
    "hydrogen-sulfide": ("Hydrogen sulfide", "Hidrogen sulfida", "H_{2}S", "34.08",
                         "The gas that smells like rotten eggs", "Gas yang berbau seperti telur busuk"),
    "hydrogen-cyanide": ("Hydrogen cyanide", "Hidrogen sianida", "HCN", "27.03",
                         "Used to make acrylic plastics; highly toxic", "Bahan plastik akrilik; sangat beracun"),
    "nitrogen-dioxide": ("Nitrogen dioxide", "Nitrogen dioksida", "NO_{2}", "46.01",
                         "The brown gas seen in city smog", "Gas cokelat penyebab kabut asap kota"),
    "sulfur-trioxide": ("Sulfur trioxide", "Belerang trioksida", "SO_{3}", "80.06",
                        "Key step in making sulfuric acid", "Tahap penting pembuatan asam sulfat"),
    "carbon-tetrachloride": ("Carbon tetrachloride", "Karbon tetraklorida", "CCl_{4}", "153.82",
                             "A former cleaning solvent, now restricted", "Bekas pelarut pembersih, kini dibatasi"),
    "chloroform": ("Chloroform", "Kloroform", "CHCl_{3}", "119.38", "Laboratory solvent; once used as an anesthetic",
                   "Pelarut laboratorium; dulu dipakai sebagai obat bius"),
    "chloromethane": ("Chloromethane", "Klorometana", "CH_{3}Cl", "50.49", "Used to make silicones",
                      "Bahan pembuat silikon"),
    "sodium-hydroxide": ("Sodium hydroxide", "Natrium hidroksida", "NaOH", "40.00",
                         "Used to make soap and unclog drains", "Bahan pembuat sabun dan pembersih saluran"),
    "nitric-acid": ("Nitric acid", "Asam nitrat", "HNO_{3}", "63.01", "Used to make fertilizers and explosives",
                    "Bahan pembuat pupuk dan bahan peledak"),
    "formic-acid": ("Formic acid", "Asam format", "HCOOH", "46.03", "The acid in ant stings",
                    "Asam yang ada pada sengatan semut"),
    "acetic-acid": ("Acetic acid", "Asam asetat", "CH_{3}COOH", "60.05", "Gives vinegar its sour taste",
                    "Memberi rasa asam pada cuka"),
    "acetone": ("Acetone", "Aseton", "CH_{3}COCH_{3}", "58.08", "The solvent in nail polish remover",
                "Pelarut dalam penghapus cat kuku"),
    "urea": ("Urea", "Urea", "CO(NH_{2})_{2}", "60.06", "A popular nitrogen fertilizer", "Pupuk nitrogen yang populer"),
    "propane": ("Propane", "Propana", "C_{3}H_{8}", "44.10", "LPG fuel for cooking and grills",
                "Bahan bakar elpiji untuk memasak"),
    "propene": ("Propene", "Propena", "C_{3}H_{6}", "42.08", "Used to make polypropylene plastic",
                "Bahan pembuat plastik polipropilena"),
    "butane": ("Butane", "Butana", "C_{4}H_{10}", "58.12", "Fuel in lighters and LPG", "Bahan bakar korek gas dan elpiji"),
    "nitric-oxide": ("Nitric oxide", "Nitrogen monoksida", "NO", "30.01", "A signaling molecule in the human body",
                     "Molekul pembawa sinyal dalam tubuh manusia"),
    "phosphine": ("Phosphine", "Fosfin", "PH_{3}", "34.00", "Fumigant that protects stored grain",
                  "Fumigan pelindung biji-bijian di gudang"),
    "hydrazine": ("Hydrazine", "Hidrazin", "N_{2}H_{4}", "32.05", "Rocket and satellite fuel",
                  "Bahan bakar roket dan satelit"),
    "silane": ("Silane", "Silana", "SiH_{4}", "32.12", "Used to make computer chips and solar cells",
               "Bahan pembuat chip komputer dan sel surya"),
}

ICONS = {ic["id"]: (ic["body"], m.STROKE) for m in (molecules, molecules2) for ic in m.ICONS}


def _icon(icon_id, cx, cy, size):
    body, stroke = ICONS[icon_id]
    return (f'<g transform="translate({cx - size / 2:.1f} {cy - size / 2:.1f}) scale({size / GRID:.4f})">'
            f'<g {style_attrs(stroke)}>{fitted(body, stroke)}</g></g>')


def compound_post(p, W, H, icon_id, lang):
    en, idn, f, mass, use_en, use_id = DATA[icon_id]
    name, use = (idn, use_id) if lang == "id" else (en, use_en)
    if lang == "id":
        mass = mass.replace(".", ",")
    m = W * .08
    out = [hexes(W - 70, H - 80, 70, 3, p["line"], 3, 4)]
    out.append(pill("COMPOUND OF THE DAY", m, H * .08, W * .026, p["accent"], "#FFFFFF"))
    out.append(f'<circle cx="{W / 2}" cy="{H * .37}" r="{W * .2}" fill="{p["card"]}"/>')
    out.append(_icon(icon_id, W / 2, H * .37, W * .3))
    out.append(text(name, W / 2, H * .66, W * .062, p["ink"], "Bold"))
    cw = (W - 2 * m - 20) / 2
    y = H * .7
    for k, (lab, val) in enumerate((("Formula", None), ("Molar mass", f"{mass} g/mol"))):
        x = m + k * (cw + 20)
        out.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{cw:.1f}" height="{H * .1:.1f}" rx="18" fill="{p["card"]}"/>')
        if val is None:
            out.append(chem(f, x + cw / 2, y + H * .058, W * .04, p["accent2"], "middle"))
        else:
            out.append(text(val, x + cw / 2, y + H * .058, W * .036, p["accent2"], "Bold"))
        out.append(text(lab, x + cw / 2, y + H * .087, W * .019, p["sub"], "SemiBold"))
    out.append(para(use, W / 2, H * .86, W * .03, p["ink"], W - 2 * m, "SemiBold", "middle", lh=1.3))
    out.append(handle(p, W / 2, H - m * .55, W * .024, "middle"))
    return out


def assets():
    p = PALETTES["navy"]
    sets = []
    for lang in ("en", "id"):
        poster_kit.set_lang(lang)
        sid = "social-compound-posts" + ("" if lang == "en" else "-indonesian")
        posts = []
        for k, icon_id in enumerate(DATA):
            inner = "".join(compound_post(p, 1080, 1080, icon_id, lang))
            svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="2160" height="2160" viewBox="0 0 1080 1080">\n'
                   f'<rect x="-1" y="-1" width="1082" height="1082" fill="{p["bg"]}"/>'
                   f'<clipPath id="sm"><rect width="1080" height="1080"/></clipPath><g clip-path="url(#sm)">{inner}</g>'
                   '\n</svg>\n')
            name = DATA[icon_id][0]
            note = " in Indonesian language" if lang == "id" else ""
            posts.append(dict(name=f"{sid}-{k + 1:02d}-{icon_id}", svg=svg, size=4000, png=False,
                              title=f"{name} compound of the day social media post{note}, chemistry Instagram "
                                    "template with molecule model",
                              keywords=(["indonesian", "bahasa indonesia"] if lang == "id" else [])
                              + [name.lower(), "compound of the day", "molecule", "chemical compound"] + KEYWORDS))
        sets.append((sid, posts))
    poster_kit.set_lang("en")
    return sets


TR.update({"COMPOUND OF THE DAY": "SENYAWA HARI INI", "Formula": "Rumus", "Molar mass": "Massa molar"})
