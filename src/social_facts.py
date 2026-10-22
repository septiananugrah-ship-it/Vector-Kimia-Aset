"""Paket post Instagram "Chemistry Fact": 28 fakta kimia nyata dengan ikon, tema navy & ungu gelap, EN dan ID."""
import poster_kit
from poster_i18n import TR
from poster_kit import text, tr
from social import KEYWORDS, PALETTES, handle, hexes, para, pill, place

# (ikon, fakta EN, fakta ID)
FACTS = [
    ("water", "Water expands by about 9% when it freezes, which is why ice floats.",
     "Air memuai sekitar 9% saat membeku, itulah sebabnya es mengapung."),
    ("crystal", "Diamond and graphite are both made only of carbon atoms, just arranged differently.",
     "Intan dan grafit sama-sama hanya tersusun dari atom karbon, hanya susunannya berbeda."),
    ("thermometer", "Gallium melts at about 30°C, so it can melt in the palm of your hand.",
     "Galium meleleh pada sekitar 30°C, sehingga bisa meleleh di telapak tanganmu."),
    ("reagent-bottle", "Mercury is the only metal that is liquid at room temperature.",
     "Raksa adalah satu-satunya logam yang berwujud cair pada suhu kamar."),
    ("gas-cloud", "Air is about 78% nitrogen and 21% oxygen.", "Udara terdiri atas sekitar 78% nitrogen dan 21% oksigen."),
    ("01-hydrogen", "Hydrogen is the most abundant element in the universe.",
     "Hidrogen adalah unsur yang paling melimpah di alam semesta."),
    ("radioactive", "Bananas are slightly radioactive because they contain potassium-40.",
     "Pisang sedikit radioaktif karena mengandung kalium-40."),
    ("oxygen", "Liquid oxygen has a pale blue color.", "Oksigen cair berwarna biru pucat."),
    ("09-fluorine", "Fluorine is the most reactive of all the elements.",
     "Fluorin adalah unsur yang paling reaktif di antara semua unsur."),
    ("lightning", "Lightning turns nitrogen in the air into nitrates that fertilize the soil.",
     "Petir mengubah nitrogen di udara menjadi nitrat yang menyuburkan tanah."),
    ("watch-glass-crystals", "Glass is made mainly from sand, which is silicon dioxide.",
     "Kaca terbuat terutama dari pasir, yaitu silikon dioksida."),
    ("sodium-chloride", "Table salt is made from a reactive metal, sodium, and a toxic gas, chlorine.",
     "Garam dapur tersusun dari logam reaktif natrium dan gas beracun klorin."),
    ("molecule", "Carbon forms more compounds than any other element: over ten million are known.",
     "Karbon membentuk senyawa paling banyak dibanding unsur lain: lebih dari sepuluh juta senyawa."),
    ("magnet", "Rust is iron oxide, formed when iron reacts with oxygen and water.",
     "Karat adalah besi oksida yang terbentuk saat besi bereaksi dengan oksigen dan air."),
    ("protective-gloves", "Stainless steel contains at least 10.5% chromium, which stops it from rusting.",
     "Baja tahan karat mengandung paling sedikit 10,5% kromium yang mencegahnya berkarat."),
    ("carbon-dioxide", "Dry ice is solid carbon dioxide at −78°C. It turns straight into gas without melting.",
     "Es kering adalah karbon dioksida padat bersuhu −78°C yang langsung menyublim menjadi gas."),
    ("dropper-bottle", "Onions make you cry because they release a sulfur compound that irritates your eyes.",
     "Bawang membuat mata perih karena melepaskan senyawa belerang yang mengiritasi mata."),
    ("erlenmeyer-flask", "Baking soda and vinegar react to produce carbon dioxide bubbles.",
     "Soda kue dan cuka bereaksi menghasilkan gelembung karbon dioksida."),
    ("element-tile", "The Statue of Liberty is green because its copper skin reacted with the air.",
     "Patung Liberty berwarna hijau karena lapisan tembaganya bereaksi dengan udara."),
    ("idea-bulb", "Tungsten has the highest melting point of all metals: about 3,422°C.",
     "Tungsten (wolfram) memiliki titik leleh tertinggi di antara logam: sekitar 3.422°C."),
    ("chemistry-book", "The periodic table now has 118 confirmed elements.",
     "Tabel periodik kini memiliki 118 unsur yang telah dikonfirmasi."),
    ("02-helium", "Helium was discovered in the Sun's light in 1868, before it was found on Earth.",
     "Helium ditemukan pada cahaya Matahari tahun 1868, sebelum ditemukan di Bumi."),
    ("water-drop", "A water molecule is bent, with an angle of about 104.5° between its bonds.",
     "Molekul air berbentuk bengkok dengan sudut ikatan sekitar 104,5°."),
    ("battery", "Silver conducts electricity better than any other metal.",
     "Perak menghantarkan listrik lebih baik daripada logam lain mana pun."),
    ("ph-strip", "Pure water has a pH of 7 at 25°C: it is neither acidic nor basic.",
     "Air murni memiliki pH 7 pada 25°C: tidak asam dan tidak basa."),
    ("fire", "Fire needs three things: fuel, oxygen and heat. Remove one and it goes out.",
     "Api membutuhkan tiga hal: bahan bakar, oksigen, dan panas. Hilangkan satu, api padam."),
    ("dna", "DNA is made from just five elements: carbon, hydrogen, oxygen, nitrogen and phosphorus.",
     "DNA tersusun hanya dari lima unsur: karbon, hidrogen, oksigen, nitrogen, dan fosfor."),
    ("ozone", "The ozone layer absorbs most of the Sun's harmful UV-B radiation.",
     "Lapisan ozon menyerap sebagian besar radiasi UV-B berbahaya dari Matahari."),
]


def fact_post(p, W, H, k, icon, fact):
    m = W * .08
    out = [hexes(W - 60, 80, 70, 3, p["line"], k + 5, 4)]
    out.append(pill(f"{tr('CHEMISTRY FACT')} #{k + 1}", m, H * .08, W * .026, p["accent"], "#FFFFFF"))
    out.append(text("DID YOU KNOW?", m, H * .25, W * .07, p["accent2"], "Bold", "start"))
    out.append(para(fact, m, H * .36, W * .047, p["ink"], W * .84, "SemiBold", lh=1.32))
    out.append(f'<circle cx="{W * .76}" cy="{H * .76}" r="{W * .17}" fill="{p["card"]}"/>')
    out.append(place(icon, W * .76, H * .76, W * .22))
    out.append(handle(p, m, H - m * .8, W * .026))
    return out


def assets():
    sets = []
    for lang in ("en", "id"):
        poster_kit.set_lang(lang)
        sid = "social-fact-posts" + ("" if lang == "en" else "-indonesian")
        posts = []
        for pname in ("navy", "purple"):
            p = PALETTES[pname]
            for k, (icon, en, idn) in enumerate(FACTS):
                inner = "".join(fact_post(p, 1080, 1080, k, icon, idn if lang == "id" else en))
                svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="2160" height="2160" viewBox="0 0 1080 1080">\n'
                       f'<rect x="-1" y="-1" width="1082" height="1082" fill="{p["bg"]}"/>'
                       f'<clipPath id="sm"><rect width="1080" height="1080"/></clipPath><g clip-path="url(#sm)">{inner}'
                       '</g>\n</svg>\n')
                note = " in Indonesian language" if lang == "id" else ""
                posts.append(dict(name=f"{sid}-{pname}-{k + 1:02d}", svg=svg, size=4000, png=False,
                                  title=f"Chemistry fact social media post{note}, did you know fun science fact, "
                                        f"{p['mood']} Instagram template",
                                  keywords=(["indonesian", "bahasa indonesia"] if lang == "id" else [])
                                  + ["fun fact", "did you know", "chemistry fact", "science fact", "trivia"] + KEYWORDS))
        sets.append((sid, posts))
    poster_kit.set_lang("en")
    return sets


TR.update({"DID YOU KNOW?": "TAHUKAH KAMU?"})
