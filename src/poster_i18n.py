"""Kamus terjemahan Inggris -> Indonesia untuk teks poster.

Kunci harus sama persis dengan teks bahasa Inggris di modul poster.
Teks yang tidak ada di sini tetap tampil dalam bahasa Inggris.
"""
from atoms import ELEMENTS
from periodic import NAMES_ID

TR = {
    # umum
    "Example": "Contoh", "electrons": "elektron", "Boiling point": "Titik didih", "Gas": "Gas", "Liquid": "Cair",
    "table salt": "garam dapur",
    # bagan alat lab
    "LABORATORY EQUIPMENT": "ALAT-ALAT LABORATORIUM",
    "40 common chemistry laboratory tools and what they are used for": "40 alat laboratorium kimia dan kegunaannya",
    "Erlenmeyer Flask": "Labu Erlenmeyer", "Beaker": "Gelas Kimia", "Test Tube": "Tabung Reaksi",
    "Test Tube Rack": "Rak Tabung Reaksi", "Round-Bottom Flask": "Labu Dasar Bulat", "Volumetric Flask": "Labu Ukur",
    "Microscope": "Mikroskop", "Bunsen Burner": "Pembakar Bunsen", "Pipette": "Pipet Volume", "Dropper": "Pipet Tetes",
    "Graduated Cylinder": "Gelas Ukur", "Petri Dish": "Cawan Petri", "Funnel": "Corong",
    "Mortar & Pestle": "Mortar & Alu", "Thermometer": "Termometer", "Burette & Stand": "Buret & Statif",
    "Safety Goggles": "Kacamata Pelindung", "Retort": "Retort", "Analytical Balance": "Neraca Analitik",
    "Wash Bottle": "Botol Semprot", "Reagent Bottle": "Botol Reagen", "Dropper Bottle": "Botol Tetes",
    "Separatory Funnel": "Corong Pisah", "Liebig Condenser": "Kondensor Liebig", "Crucible": "Cawan Krus",
    "Tripod & Gauze": "Kaki Tiga & Kasa", "Spirit Lamp": "Lampu Spiritus", "Syringe": "Suntikan",
    "Lab Coat": "Jas Lab", "Gloves": "Sarung Tangan", "Centrifuge": "Sentrifus",
    "Magnetic Stirrer": "Pengaduk Magnetik", "Watch Glass": "Kaca Arloji", "Spatula": "Spatula",
    "Magnifying Glass": "Kaca Pembesar", "Hazard Bottle": "Botol Bahan Berbahaya", "Gas Cylinder": "Tabung Gas",
    "Fire Extinguisher": "Alat Pemadam Api", "Lab Notebook": "Buku Catatan Lab", "Reaction Flask": "Labu Reaksi",
    "mixing & swirling": "mencampur & menggoyang", "holding liquids": "menampung cairan",
    "small reactions": "reaksi skala kecil", "holding test tubes": "menyimpan tabung reaksi",
    "heating & boiling": "memanaskan & mendidihkan", "exact volumes": "volume yang tepat",
    "magnifying samples": "memperbesar sampel", "heating": "memanaskan", "measuring liquid": "mengukur cairan",
    "adding drops": "meneteskan cairan", "measuring volume": "mengukur volume",
    "growing cultures": "membiakkan mikroba", "pouring & filtering": "menuang & menyaring",
    "grinding solids": "menghaluskan padatan", "temperature": "mengukur suhu", "titration": "titrasi",
    "eye protection": "melindungi mata", "distillation": "distilasi", "weighing mass": "menimbang massa",
    "rinsing": "membilas", "storing chemicals": "menyimpan bahan kimia", "dispensing drops": "mengeluarkan tetesan",
    "separating liquids": "memisahkan cairan", "cooling vapor": "mendinginkan uap",
    "high-heat melting": "pemanasan suhu tinggi", "supporting & heating": "penyangga saat memanaskan",
    "gentle heating": "pemanasan ringan", "measuring & injecting": "mengukur & menyuntik",
    "body protection": "melindungi badan", "hand protection": "melindungi tangan",
    "separating by spinning": "memisahkan dengan putaran", "stirring & heating": "mengaduk & memanaskan",
    "evaporating samples": "menguapkan sampel", "transferring solids": "memindahkan padatan",
    "close inspection": "mengamati detail", "hazardous chemicals": "bahan kimia berbahaya",
    "storing gas": "menyimpan gas", "fire safety": "keselamatan kebakaran", "recording data": "mencatat data",
    "chemical reactions": "reaksi kimia",
    # molekul
    "COMMON MOLECULES": "MOLEKUL SEHARI-HARI",
    "Ball and stick models of 20 everyday molecules and compounds":
        "Model bola dan batang 20 molekul dan senyawa sehari-hari",
    "Water": "Air", "Carbon dioxide": "Karbon dioksida", "Methane": "Metana", "Ammonia": "Amonia",
    "Hydrogen chloride": "Hidrogen klorida", "Ethanol": "Etanol", "Benzene": "Benzena", "Ethylene": "Etena",
    "Acetylene": "Etuna", "Sulfur dioxide": "Belerang dioksida", "Hydrogen peroxide": "Hidrogen peroksida",
    "Sodium chloride": "Natrium klorida", "Formaldehyde": "Metanal", "Methanol": "Metanol", "Ozone": "Ozon",
    "Carbon monoxide": "Karbon monoksida", "Sulfuric acid": "Asam sulfat",
    # atom Bohr
    "BOHR ATOMIC MODELS": "MODEL ATOM BOHR",
    "Electron shell arrangement of the first 20 elements": "Susunan kulit elektron 20 unsur pertama",
    # skala pH
    "THE pH SCALE": "SKALA pH",
    "Acidic, neutral and alkaline substances from 0 to 14 with everyday examples":
        "Zat asam, netral, dan basa dari 0 sampai 14 beserta contoh sehari-hari",
    "ACIDIC": "ASAM", "NEUTRAL": "NETRAL", "ALKALINE (BASIC)": "BASA",
    "stronger acid": "asam lebih kuat", "stronger base": "basa lebih kuat",
    "Example values are typical approximations.": "Nilai contoh merupakan perkiraan umum.",
    "Battery acid": "Air aki", "Stomach acid": "Asam lambung", "Lemon juice": "Air lemon", "Vinegar": "Cuka",
    "Tomato juice": "Jus tomat", "Black coffee": "Kopi hitam", "Milk": "Susu", "Pure water": "Air murni",
    "Sea water": "Air laut", "Baking soda": "Soda kue", "Milk of magnesia": "Susu magnesia",
    "Soapy water": "Air sabun", "Bleach": "Pemutih", "Drain cleaner": "Pembersih saluran",
    # wujud zat
    "STATES OF MATTER": "WUJUD ZAT",
    "Particle arrangement in solids, liquids and gases and the changes between them":
        "Susunan partikel zat padat, cair, dan gas serta perubahan wujudnya",
    "SOLID": "PADAT", "LIQUID": "CAIR", "GAS": "GAS",
    "Fixed shape and fixed volume": "Bentuk dan volume tetap",
    "Fixed volume, takes the shape of its container": "Volume tetap, bentuk mengikuti wadah",
    "No fixed shape or volume, fills its container": "Bentuk dan volume tidak tetap, memenuhi wadah",
    "Melting": "Mencair", "Evaporation": "Menguap", "Freezing": "Membeku", "Condensation": "Mengembun",
    "Sublimation": "Menyublim", "Deposition": "Mengkristal",
    "Heat added (energy in)": "Menyerap kalor (energi masuk)",
    "Heat removed (energy out)": "Melepas kalor (energi keluar)",
    # jenis reaksi
    "TYPES OF CHEMICAL REACTIONS": "JENIS-JENIS REAKSI KIMIA",
    "Synthesis, decomposition, replacement and combustion reactions explained with particle models":
        "Reaksi sintesis, penguraian, pergantian, dan pembakaran dengan model partikel",
    "Synthesis": "Sintesis (penggabungan)", "Decomposition": "Penguraian",
    "Single replacement": "Pergantian tunggal", "Double replacement": "Pergantian ganda", "Combustion": "Pembakaran",
    "Two or more substances combine into one": "Dua zat atau lebih bergabung menjadi satu zat",
    "One compound breaks down into simpler substances": "Satu senyawa terurai menjadi zat yang lebih sederhana",
    "One element replaces another in a compound": "Satu unsur menggantikan unsur lain dalam senyawa",
    "Two compounds exchange partners": "Dua senyawa saling bertukar pasangan",
    "A fuel reacts with oxygen releasing energy": "Bahan bakar bereaksi dengan oksigen dan melepaskan energi",
    # gugus fungsi
    "ORGANIC FUNCTIONAL GROUPS": "GUGUS FUNGSI SENYAWA ORGANIK",
    "Structural formulas of 12 important functional groups with examples":
        "Rumus struktur 12 gugus fungsi penting beserta contohnya",
    "Alcohol": "Alkohol", "Ether": "Eter", "Aldehyde": "Aldehida", "Ketone": "Keton",
    "Carboxylic acid": "Asam karboksilat", "Ester": "Ester", "Amine": "Amina", "Amide": "Amida",
    "Alkene": "Alkena", "Alkyne": "Alkuna", "Haloalkane": "Haloalkana", "Arene (aromatic)": "Arena (aromatik)",
    "Diethyl ether": "Dietil eter", "Methanal": "Metanal", "Acetone": "Aseton", "Acetic acid": "Asam asetat",
    "Ethyl acetate": "Etil asetat", "Methylamine": "Metilamina", "Acetamide": "Asetamida", "Ethene": "Etena",
    "Ethyne": "Etuna", "Chloromethane": "Klorometana", "Toluene": "Toluena",
    "R = alkyl group  ·  X = halogen (F, Cl, Br, I)": "R = gugus alkil  ·  X = halogen (F, Cl, Br, I)",
    # alkana
    "ALKANE HOMOLOGOUS SERIES": "DERET HOMOLOG ALKANA",
    "The first ten straight-chain alkanes with formulas, carbon chains and boiling points":
        "Sepuluh alkana rantai lurus pertama beserta rumus, rantai karbon, dan titik didihnya",
    "Ethane": "Etana", "Propane": "Propana", "Butane": "Butana", "Pentane": "Pentana", "Hexane": "Heksana",
    "Heptane": "Heptana", "Octane": "Oktana", "Nonane": "Nonana", "Decane": "Dekana",
    "General formula CnH2n+2  ·  state at room temperature (25 °C)":
        "Rumus umum CnH2n+2  ·  wujud pada suhu ruang (25 °C)",
    # struktur atom
    "STRUCTURE OF AN ATOM": "STRUKTUR ATOM",
    "Protons, neutrons and electrons in a carbon-12 atom (6 protons, 6 neutrons, 6 electrons)":
        "Proton, neutron, dan elektron pada atom karbon-12 (6 proton, 6 neutron, 6 elektron)",
    "Electron shell": "Kulit elektron", "energy level of the electrons": "tingkat energi elektron",
    "Electron": "Elektron", "negative charge (−)": "bermuatan negatif (−)", "Nucleus": "Inti atom",
    "contains protons and neutrons": "berisi proton dan neutron", "Proton": "Proton",
    "positive charge (+)": "bermuatan positif (+)", "Neutron": "Neutron", "no charge (0)": "tidak bermuatan (0)",
    "Particle": "Partikel", "Charge": "Muatan", "Relative mass": "Massa relatif", "Location": "Letak",
    "Atomic number (Z)": "Nomor atom (Z)", "= number of protons": "= jumlah proton",
    "Mass number (A)": "Nomor massa (A)", "= protons + neutrons": "= proton + neutron",
    "For carbon-12: Z = 6, A = 12": "Untuk karbon-12: Z = 6, A = 12",
    # ikatan kimia
    "TYPES OF CHEMICAL BONDS": "JENIS-JENIS IKATAN KIMIA",
    "Ionic, covalent and metallic bonding explained with particle models":
        "Ikatan ion, kovalen, dan logam dijelaskan dengan model partikel",
    "Ionic bond": "Ikatan ion", "Covalent bond": "Ikatan kovalen", "Metallic bond": "Ikatan logam",
    "Electrons are transferred from a metal to a nonmetal": "Elektron berpindah dari logam ke nonlogam",
    "Electron pairs are shared between nonmetal atoms": "Pasangan elektron dipakai bersama antaratom nonlogam",
    "Metal ions in a sea of delocalized electrons": "Ion logam dalam lautan elektron yang bebas bergerak",
    # keselamatan lab
    "LABORATORY SAFETY RULES": "TATA TERTIB KESELAMATAN LABORATORIUM",
    "Ten essential rules for working safely in the chemistry lab":
        "Sepuluh aturan penting agar aman bekerja di laboratorium kimia",
    "Wear safety goggles": "Pakai kacamata pelindung",
    "Protect your eyes from splashes and fumes": "Lindungi mata dari percikan dan uap bahan kimia",
    "Wear a lab coat": "Pakai jas laboratorium",
    "Keep chemicals off your skin and clothes": "Jaga kulit dan pakaian dari bahan kimia",
    "Wear protective gloves": "Pakai sarung tangan",
    "Never touch chemicals with bare hands": "Jangan menyentuh bahan kimia dengan tangan kosong",
    "Read every label": "Baca setiap label",
    "Check hazard warnings before using a chemical": "Periksa tanda bahaya sebelum memakai bahan kimia",
    "Never leave a flame unattended": "Jangan tinggalkan api menyala",
    "Turn off burners as soon as you are done": "Matikan pembakar segera setelah selesai",
    "Point test tubes away": "Arahkan tabung reaksi menjauh",
    "Never aim a heated test tube at anyone": "Jangan arahkan tabung yang dipanaskan ke orang lain",
    "Use a spatula": "Gunakan spatula",
    "Transfer solids with clean tools, not fingers": "Pindahkan padatan dengan alat bersih, bukan jari",
    "Know the fire extinguisher": "Kenali alat pemadam api",
    "Learn where all safety equipment is located": "Ketahui letak semua peralatan keselamatan",
    "Clean up spills": "Bersihkan tumpahan",
    "Report and clean any spill immediately": "Laporkan dan bersihkan tumpahan dengan segera",
    "Record your work": "Catat pekerjaanmu",
    "Follow instructions and write down every result": "Ikuti petunjuk dan catat setiap hasil",
}

# nama unsur 1-20 (bagan atom Bohr); "Hydrogen", "Oxygen", dll. juga dipakai bagan molekul
TR.update(zip((name for _, name in ELEMENTS), NAMES_ID[:20]))
