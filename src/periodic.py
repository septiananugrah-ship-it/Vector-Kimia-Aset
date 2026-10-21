"""Poster tabel periodik unsur (118 unsur), dua tema warna.

Semua teks dikonversi ke outline lewat textpath. Massa atom standar IUPAC
(dibulatkan); tanda kurung = nomor massa isotop paling stabil.
"""
from icons_lab_flat import dark
from textpath import text, width

SET_ID = "periodic-table-posters"

# Z: lambang, nama, massa, kategori
DATA = """
H Hydrogen 1.008 nm|He Helium 4.0026 ng|Li Lithium 6.94 ak|Be Beryllium 9.0122 ae|B Boron 10.81 md
C Carbon 12.011 nm|N Nitrogen 14.007 nm|O Oxygen 15.999 nm|F Fluorine 18.998 hl|Ne Neon 20.180 ng
Na Sodium 22.990 ak|Mg Magnesium 24.305 ae|Al Aluminium 26.982 pt|Si Silicon 28.085 md|P Phosphorus 30.974 nm
S Sulfur 32.06 nm|Cl Chlorine 35.45 hl|Ar Argon 39.948 ng|K Potassium 39.098 ak|Ca Calcium 40.078 ae
Sc Scandium 44.956 tm|Ti Titanium 47.867 tm|V Vanadium 50.942 tm|Cr Chromium 51.996 tm|Mn Manganese 54.938 tm
Fe Iron 55.845 tm|Co Cobalt 58.933 tm|Ni Nickel 58.693 tm|Cu Copper 63.546 tm|Zn Zinc 65.38 tm
Ga Gallium 69.723 pt|Ge Germanium 72.630 md|As Arsenic 74.922 md|Se Selenium 78.971 nm|Br Bromine 79.904 hl
Kr Krypton 83.798 ng|Rb Rubidium 85.468 ak|Sr Strontium 87.62 ae|Y Yttrium 88.906 tm|Zr Zirconium 91.224 tm
Nb Niobium 92.906 tm|Mo Molybdenum 95.95 tm|Tc Technetium (98) tm|Ru Ruthenium 101.07 tm|Rh Rhodium 102.91 tm
Pd Palladium 106.42 tm|Ag Silver 107.87 tm|Cd Cadmium 112.41 tm|In Indium 114.82 pt|Sn Tin 118.71 pt
Sb Antimony 121.76 md|Te Tellurium 127.60 md|I Iodine 126.90 hl|Xe Xenon 131.29 ng|Cs Caesium 132.91 ak
Ba Barium 137.33 ae|La Lanthanum 138.91 ln|Ce Cerium 140.12 ln|Pr Praseodymium 140.91 ln|Nd Neodymium 144.24 ln
Pm Promethium (145) ln|Sm Samarium 150.36 ln|Eu Europium 151.96 ln|Gd Gadolinium 157.25 ln|Tb Terbium 158.93 ln
Dy Dysprosium 162.50 ln|Ho Holmium 164.93 ln|Er Erbium 167.26 ln|Tm Thulium 168.93 ln|Yb Ytterbium 173.05 ln
Lu Lutetium 174.97 ln|Hf Hafnium 178.49 tm|Ta Tantalum 180.95 tm|W Tungsten 183.84 tm|Re Rhenium 186.21 tm
Os Osmium 190.23 tm|Ir Iridium 192.22 tm|Pt Platinum 195.08 tm|Au Gold 196.97 tm|Hg Mercury 200.59 tm
Tl Thallium 204.38 pt|Pb Lead 207.2 pt|Bi Bismuth 208.98 pt|Po Polonium (209) pt|At Astatine (210) hl
Rn Radon (222) ng|Fr Francium (223) ak|Ra Radium (226) ae|Ac Actinium (227) ac|Th Thorium 232.04 ac
Pa Protactinium 231.04 ac|U Uranium 238.03 ac|Np Neptunium (237) ac|Pu Plutonium (244) ac|Am Americium (243) ac
Cm Curium (247) ac|Bk Berkelium (247) ac|Cf Californium (251) ac|Es Einsteinium (252) ac|Fm Fermium (257) ac
Md Mendelevium (258) ac|No Nobelium (259) ac|Lr Lawrencium (266) ac|Rf Rutherfordium (267) tm|Db Dubnium (268) tm
Sg Seaborgium (269) tm|Bh Bohrium (270) tm|Hs Hassium (269) tm|Mt Meitnerium (278) uk|Ds Darmstadtium (281) uk
Rg Roentgenium (282) uk|Cn Copernicium (285) uk|Nh Nihonium (286) uk|Fl Flerovium (290) uk|Mc Moscovium (290) uk
Lv Livermorium (293) uk|Ts Tennessine (294) uk|Og Oganesson (294) uk
"""
ELEMENTS = [tuple(e.split()) for e in DATA.replace("\n", "|").split("|") if e.strip()]
assert len(ELEMENTS) == 118

# Nama unsur dalam Bahasa Indonesia, urut nomor atom.
NAMES_ID = """
Hidrogen Helium Litium Berilium Boron Karbon Nitrogen Oksigen Fluorin Neon
Natrium Magnesium Aluminium Silikon Fosfor Belerang Klorin Argon Kalium Kalsium
Skandium Titanium Vanadium Kromium Mangan Besi Kobalt Nikel Tembaga Seng
Galium Germanium Arsen Selenium Bromin Kripton Rubidium Stronsium Itrium Zirkonium
Niobium Molibdenum Teknesium Rutenium Rodium Paladium Perak Kadmium Indium Timah
Antimon Telurium Iodin Xenon Sesium Barium Lantanum Serium Praseodimium Neodimium
Prometium Samarium Europium Gadolinium Terbium Disprosium Holmium Erbium Tulium Iterbium
Lutesium Hafnium Tantalum Tungsten Renium Osmium Iridium Platina Emas Raksa
Talium Timbal Bismut Polonium Astatin Radon Fransium Radium Aktinium Torium
Protaktinium Uranium Neptunium Plutonium Amerisium Kurium Berkelium Kalifornium Einsteinium Fermium
Mendelevium Nobelium Lawrensium Rutherfordium Dubnium Seaborgium Bohrium Hasium Meitnerium Darmstadtium
Roentgenium Kopernisium Nihonium Flerovium Moskovium Livermorium Tenesin Oganeson
""".split()
assert len(NAMES_ID) == 118

LANG = {
    "en": dict(title="PERIODIC TABLE OF THE ELEMENTS",
               subtitle="118 chemical elements with atomic number, symbol, name and atomic mass"),
    "id": dict(title="TABEL PERIODIK UNSUR",
               subtitle="118 unsur kimia lengkap dengan nomor atom, lambang, nama, dan massa atom"),
}
CAT_ID = {"ak": "Logam alkali", "ae": "Logam alkali tanah", "tm": "Logam transisi", "pt": "Logam pascatransisi",
          "md": "Metaloid", "nm": "Nonlogam reaktif", "hl": "Halogen", "ng": "Gas mulia", "ln": "Lantanida",
          "ac": "Aktinida", "uk": "Sifat belum diketahui"}

CATEGORIES = [
    ("ak", "Alkali metals", "#FF9E8A"), ("ae", "Alkaline earth metals", "#FFC98A"),
    ("tm", "Transition metals", "#FFE38A"), ("pt", "Post-transition metals", "#B9E28C"),
    ("md", "Metalloids", "#8FD9C4"), ("nm", "Reactive nonmetals", "#8ACBEF"),
    ("hl", "Halogens", "#A9B8F5"), ("ng", "Noble gases", "#C3A6F2"),
    ("ln", "Lanthanides", "#F7B6D2"), ("ac", "Actinides", "#E8C7A0"),
    ("uk", "Unknown properties", "#D5DBE3"),
]
CAT = {k: (name, col) for k, name, col in CATEGORIES}

THEMES = [
    dict(key="light", bg="#FFFFFF", ink="#1E2A3A", sub="#5B6878", mood="pastel colors on white"),
    dict(key="dark", bg="#16213A", ink="#FFFFFF", sub="#AEB9C9", mood="pastel colors on dark navy"),
]

C, GAP = 60, 4  # ukuran ubin dan jarak
S = C + GAP


def position(z):
    """(kolom, baris) 0-indeks; lantanida/aktinida di baris 8 dan 9."""
    if z == 1:
        return 0, 0
    if z == 2:
        return 17, 0
    for start, row in ((3, 1), (11, 2)):
        if start <= z < start + 8:
            i = z - start
            return (i if i < 2 else i + 10), row
    for start, row in ((19, 3), (37, 4)):
        if start <= z < start + 18:
            return z - start, row
    for start, row in ((55, 5), (87, 6)):
        if not start <= z < start + 32:
            continue
        i = z - start
        if i < 2:
            return i, row
        if i < 17:
            return i, row + 3  # deret f, kolom 2..16 (di bawah penanda grup 3)
        return i - 14, row
    raise ValueError(z)


def fit_text(s, x, y, size, fill, max_w, weight="Bold"):
    w = width(s, size, weight)
    if w > max_w:
        size *= max_w / w
    return text(s, x, y, size, fill, weight)


def tile(z, sym, name, mass, cat, x, y):
    col = CAT[cat][1]
    cx = x + C / 2
    return (f'<rect x="{x}" y="{y}" width="{C}" height="{C}" rx="6" fill="{col}" '
            f'stroke="{dark(col, .25)}" stroke-width="1.2"/>'
            f'<rect x="{x + 1.5}" y="{y + C - 9}" width="{C - 3}" height="7.5" rx="3" fill="{dark(col, .08)}"/>'
            + text(str(z), x + 6, y + 12, 8.5, "#1E2A3A", "SemiBold", anchor="start")
            + fit_text(sym, cx, y + 35, 21, "#1E2A3A", C - 10)
            + fit_text(name, cx, y + 45, 6.6, "#1E2A3A", C - 7, "SemiBold")
            + fit_text(mass, cx, y + C - 3.3, 5.6, "#1E2A3A", C - 7, "Regular"))


def poster(theme, lang="en"):
    mx, top = 44, 120
    W = 18 * S - GAP + 2 * mx
    fy = top + 7 * S + 26  # baris deret f
    H = fy + 2 * S + 44
    ink, sub = theme["ink"], theme["sub"]
    out = [f'<rect width="{W}" height="{H}" fill="{theme["bg"]}"/>',
           text(LANG[lang]["title"], W / 2, 66, 36, ink),
           text(LANG[lang]["subtitle"], W / 2, 92, 12, sub, "Regular")]
    for z, (sym, name, mass, cat) in enumerate(ELEMENTS, start=1):
        if lang == "id":
            name, mass = NAMES_ID[z - 1], mass.replace(".", ",")
        c, r = position(z)
        x = mx + c * S
        y = top + r * S if r < 7 else fy + (r - 8) * S
        out.append(tile(z, sym, name, mass, cat, x, y))
    # penanda rentang lantanida/aktinida di grup 3
    for r, label, cat in ((5, "57–71", "ln"), (6, "89–103", "ac")):
        x, y = mx + 2 * S, top + r * S
        col = CAT[cat][1]
        out.append(f'<rect x="{x}" y="{y}" width="{C}" height="{C}" rx="6" fill="none" stroke="{col}" '
                   f'stroke-width="2" stroke-dasharray="4 3"/>' + text(label, x + C / 2, y + C / 2 + 4, 11, col))
    # nomor golongan dan periode
    for g in range(18):
        r0 = 0 if g in (0, 17) else 1 if g in (1, 12, 13, 14, 15, 16) else 3
        out.append(text(str(g + 1), mx + g * S + C / 2, top + r0 * S - 7, 9, sub, "SemiBold"))
    for p in range(7):
        out.append(text(str(p + 1), mx - 14, top + p * S + C / 2 + 3.5, 9, sub, "SemiBold"))
    # keterangan kategori di ruang kosong atas
    lx, ly = mx + 2.6 * S, top + 0.15 * S
    for i, (k, nm, col) in enumerate(CATEGORIES):
        nm = CAT_ID[k] if lang == "id" else nm
        cx, cy = lx + (i // 4) * 3.3 * S, ly + (i % 4) * 26
        out.append(f'<rect x="{cx}" y="{cy}" width="18" height="18" rx="4" fill="{col}" '
                   f'stroke="{dark(col, .25)}" stroke-width="1"/>' + text(nm, cx + 26, cy + 13, 11, ink, "SemiBold",
                                                                         anchor="start"))
    return W, H, "".join(out)


KEYWORDS = ["periodic table", "periodic table of elements", "chemical elements", "element", "elements",
            "chemistry", "poster", "infographic", "chart", "table", "atomic number", "atomic mass",
            "symbol", "metal", "nonmetal", "noble gas", "metalloid", "lanthanide", "actinide",
            "science", "education", "school", "classroom", "teaching", "student", "learning",
            "mendeleev", "chemical", "physics", "laboratory", "reference", "vector", "illustration",
            "colorful", "pastel", "background", "wall chart", "scientific", "hydrogen", "oxygen",
            "carbon", "gold"]
KEYWORDS_ID = ["indonesian", "indonesia", "bahasa indonesia", "tabel periodik"]


def assets():
    out = []
    for lang in ("en", "id"):
        for th in THEMES:
            W, H, inner = poster(th, lang)
            svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * 5}" height="{H * 5}" '
                   f'viewBox="0 0 {W} {H}">\n{inner}\n</svg>\n')
            suffix, note = ("", "") if lang == "en" else ("-indonesian", " in Indonesian language")
            out.append(dict(
                name=f"{SET_ID}-{th['key']}{suffix}", svg=svg, size=7000, png=False,
                title=f"Periodic table of the chemical elements poster{note}, {th['mood']}, "
                      "chemistry vector infographic",
                keywords=(KEYWORDS_ID if lang == "id" else []) + KEYWORDS))
    return [(SET_ID, out)]
