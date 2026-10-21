"""Set 01: 20 ikon alat laboratorium, gaya garis (line art).

Setiap ikon digambar di grid 64x64. `body` berisi elemen SVG tanpa atribut
gaya; gaya garis (stroke) diterapkan seragam oleh build.py.
"""

SET_ID = "lab-line-icons"
SET_TITLE = "Chemistry laboratory equipment line icons set, 20 editable stroke vector icons"
SET_KEYWORDS = [
    "icon set", "collection", "pictogram", "symbol", "line icon", "outline",
    "thin line", "vector", "chemistry", "laboratory", "lab", "science",
    "scientific", "equipment", "glassware", "research", "experiment",
    "education", "school", "biology", "pharmacy", "medical", "test",
    "analysis", "chemical", "flask", "beaker", "test tube", "microscope",
    "pipette", "burner", "thermometer", "petri dish", "funnel", "isolated",
    "simple", "minimal", "flat", "ui", "web", "sign", "illustration",
]

# Keyword umum yang ikut ditempel ke setiap ikon tunggal.
COMMON_KEYWORDS = [
    "icon", "line icon", "outline", "vector", "symbol", "pictogram", "sign",
    "chemistry", "laboratory", "lab", "science", "scientific", "equipment",
    "research", "experiment", "education", "school", "chemical", "isolated",
    "simple", "minimal", "thin line", "illustration", "ui", "web",
]

ICONS = [
    {
        "id": "erlenmeyer-flask",
        "title": "Erlenmeyer flask line icon, chemistry laboratory glassware vector",
        "keywords": ["erlenmeyer", "flask", "conical flask", "glassware", "liquid", "bubbles", "reaction"],
        "body": """
<path d="M26 8h12M28 8v16L14 52a4 4 0 0 0 3.6 5.8h28.8A4 4 0 0 0 50 52L36 24V8"/>
<path d="M19 42h26"/>
<circle cx="29" cy="49" r="1.6"/><circle cx="36" cy="46.5" r="1.1"/>
""",
    },
    {
        "id": "beaker",
        "title": "Laboratory beaker line icon with measurement scale, chemistry vector",
        "keywords": ["beaker", "glass", "measuring", "scale", "glassware", "liquid", "volume"],
        "body": """
<path d="M12 8h40M16 8v46a4 4 0 0 0 4 4h24a4 4 0 0 0 4-4V8"/>
<path d="M48 16h-7M48 22h-5M48 28h-7"/>
<path d="M16 38h32"/>
""",
    },
    {
        "id": "test-tube",
        "title": "Test tube line icon with liquid, chemistry laboratory vector",
        "keywords": ["test tube", "tube", "sample", "glassware", "liquid", "medical test", "bubbles"],
        "body": """
<path d="M24 6h16M27 6v44a5 5 0 0 0 10 0V6"/>
<path d="M27 32h10"/>
<circle cx="32" cy="42" r="1.6"/>
""",
    },
    {
        "id": "test-tube-rack",
        "title": "Test tubes in rack line icon, chemistry laboratory vector",
        "keywords": ["test tubes", "rack", "holder", "samples", "tubes", "glassware", "stand"],
        "body": """
<path d="M14.5 8v36a3.5 3.5 0 0 0 7 0V8M28.5 8v36a3.5 3.5 0 0 0 7 0V8M42.5 8v36a3.5 3.5 0 0 0 7 0V8"/>
<path d="M14.5 34h7M28.5 30h7M42.5 38h7"/>
<path d="M8 24h6.5M21.5 24h7M35.5 24h7M49.5 24h6.5M8 54h48M10 24v32M54 24v32"/>
""",
    },
    {
        "id": "round-bottom-flask",
        "title": "Round bottom flask line icon, chemistry laboratory glassware vector",
        "keywords": ["round bottom flask", "flask", "boiling flask", "glassware", "liquid", "distillation"],
        "body": """
<path d="M26 8h12M28 8v16.5A16 16 0 1 0 36 24.5V8"/>
<path d="M17.2 46h29.6"/>
""",
    },
    {
        "id": "volumetric-flask",
        "title": "Volumetric flask line icon, chemistry measuring glassware vector",
        "keywords": ["volumetric flask", "flask", "measuring", "calibration", "glassware", "solution"],
        "body": """
<path d="M27 6h10M29 6v24L17 46a9 9 0 0 0 7 13h16a9 9 0 0 0 7-13L35 30V6"/>
<path d="M27 16h10"/>
<path d="M19.5 48h25"/>
""",
    },
    {
        "id": "microscope",
        "title": "Microscope line icon, science laboratory research vector",
        "keywords": ["microscope", "magnification", "biology", "microbiology", "optics", "lens", "study"],
        "body": """
<path d="M21 6h10M23 6h6v24h-6z"/>
<path d="M24.5 30h3v5h-3z"/>
<path d="M29 14h5a10 10 0 0 1 10 10v32"/>
<circle cx="44" cy="30" r="3"/>
<path d="M14 40h30"/>
<path d="M21 49h10"/>
<path d="M12 56h40"/>
""",
    },
    {
        "id": "bunsen-burner",
        "title": "Bunsen burner with flame line icon, chemistry laboratory vector",
        "keywords": ["bunsen burner", "burner", "flame", "fire", "gas", "heating", "heat"],
        "body": """
<path d="M32 4c4 5 6 8 6 11a6 6 0 0 1-12 0c0-3 2-6 6-11z"/>
<path d="M32 11c1.5 2 2 3.5 2 4.5a2 2 0 0 1-4 0c0-1 .5-2.5 2-4.5z"/>
<path d="M28 24h8v24h-8z"/>
<path d="M28 40h-10"/>
<path d="M18 56h28l-4-8H22z"/>
""",
    },
    {
        "id": "pipette",
        "title": "Volumetric pipette line icon, chemistry laboratory vector",
        "keywords": ["pipette", "volumetric pipette", "measuring", "dosing", "liquid", "sample", "transfer"],
        "body": """
<path d="M30 4h4"/>
<path d="M30 4v19c-3 1-4 3-4 6v8c0 3 1 5 4 6v14l2 3 2-3V43c3-1 4-3 4-6v-8c0-3-1-5-4-6V4"/>
<path d="M28 12h8"/>
""",
    },
    {
        "id": "dropper",
        "title": "Dropper with drop line icon, chemistry laboratory vector",
        "keywords": ["dropper", "eyedropper", "drop", "liquid", "dose", "medicine", "serum"],
        "body": """
<path d="M27 18v-8a5 5 0 0 1 10 0v8"/>
<path d="M24 18h16v5H24z"/>
<path d="M28 23v21l4 6 4-6V23"/>
<path d="M32 54c-1.5 2-2.2 3.2-2.2 4.2a2.2 2.2 0 0 0 4.4 0c0-1-.7-2.2-2.2-4.2z"/>
""",
    },
    {
        "id": "graduated-cylinder",
        "title": "Graduated cylinder line icon, chemistry measuring vector",
        "keywords": ["graduated cylinder", "measuring cylinder", "cylinder", "scale", "volume", "measuring", "glassware"],
        "body": """
<path d="M22 8h20M24 8v46M40 8v46"/>
<path d="M24 16h6M24 22h4M24 28h6M24 40h4M24 46h6"/>
<path d="M24 34h16"/>
<path d="M22 54h20v4H22zM18 58h28"/>
""",
    },
    {
        "id": "petri-dish",
        "title": "Petri dish with bacteria colonies line icon, microbiology vector",
        "keywords": ["petri dish", "bacteria", "culture", "microbiology", "colony", "biology", "agar"],
        "body": """
<ellipse cx="32" cy="30" rx="24" ry="9"/>
<path d="M8 30v6a24 9 0 0 0 48 0v-6"/>
<circle cx="25" cy="30" r="2.2"/><circle cx="35" cy="27" r="1.6"/><circle cx="39" cy="32" r="1.1"/>
""",
    },
    {
        "id": "funnel",
        "title": "Laboratory funnel line icon, chemistry filtering vector",
        "keywords": ["funnel", "filter", "filtration", "pouring", "glassware", "separation", "liquid"],
        "body": """
<path d="M12 12h40L36 34v22h-8V34z"/>
<path d="M18.4 20h27.2"/>
""",
    },
    {
        "id": "mortar-and-pestle",
        "title": "Mortar and pestle line icon, pharmacy and chemistry vector",
        "keywords": ["mortar", "pestle", "grinding", "pharmacy", "apothecary", "powder", "herbal"],
        "body": """
<path d="M35 30L47 9a3 3 0 0 1 5.2 3L41 30"/>
<path d="M10 30h44a22 18 0 0 1-44 0z"/>
<path d="M24 47l-2 9h20l-2-9"/>
""",
    },
    {
        "id": "thermometer",
        "title": "Laboratory thermometer line icon, temperature measurement vector",
        "keywords": ["thermometer", "temperature", "heat", "measuring", "degree", "scale", "mercury"],
        "body": """
<path d="M28 41V10a4 4 0 0 1 8 0v31a9 9 0 1 1-8 0z"/>
<path d="M32 46V20"/>
<circle cx="32" cy="48.5" r="3"/>
<path d="M40 14h4M40 20h3M40 26h4M40 32h3"/>
""",
    },
    {
        "id": "burette-stand",
        "title": "Burette on stand line icon, titration chemistry vector",
        "keywords": ["burette", "titration", "stand", "clamp", "stopcock", "analysis", "glassware"],
        "body": """
<g transform="translate(9 0)">
<path d="M8 58h30M16 58V6M16 20h14"/>
<path d="M29 6h8M30 6v36l2 4M36 6v36l-2 4"/>
<path d="M30 14h3M30 20h3M30 26h3M30 32h3"/>
<path d="M27 46h12M33 46v6"/>
<circle cx="33" cy="57" r="1.2"/>
</g>
""",
    },
    {
        "id": "safety-goggles",
        "title": "Safety goggles line icon, laboratory protective equipment vector",
        "keywords": ["safety goggles", "goggles", "glasses", "protection", "safety", "ppe", "eye protection"],
        "body": """
<path d="M6 28h4M54 28h4"/>
<path d="M10 24c0-3 2-5 5-5h34c3 0 5 2 5 5v10c0 4-3 7-7 7h-8c-3 0-5-2-6-5h-2c-1 3-3 5-6 5h-8c-4 0-7-3-7-7z"/>
<path d="M16 28l4-4M40 28l4-4"/>
""",
    },
    {
        "id": "retort",
        "title": "Retort distillation flask line icon, alchemy and chemistry vector",
        "keywords": ["retort", "distillation", "alchemy", "flask", "glassware", "vintage", "condensation"],
        "body": """
<g transform="translate(-1.5 -10)">
<path d="M31.19 30.81A13 13 0 1 0 34.56 36.64"/>
<path d="M31.19 30.81L58 44M34.56 36.64L56 48M58 44l-2 4"/>
<path d="M10.47 46h23.06"/>
<path d="M12 58h20M22 53v5"/>
</g>
""",
    },
    {
        "id": "laboratory-scale",
        "title": "Analytical laboratory scale line icon, weighing vector",
        "keywords": ["scale", "balance", "weighing", "analytical balance", "weight", "digital scale", "measurement"],
        "body": """
<path d="M24 24h16M26 24v14M38 24v14"/>
<path d="M16 38h32M32 38v6"/>
<path d="M10 44h44v12H10z"/>
<path d="M38 48h10v4H38z"/>
<circle cx="16" cy="50" r="1.5"/><circle cx="22" cy="50" r="1.5"/>
""",
    },
    {
        "id": "wash-bottle",
        "title": "Laboratory wash bottle line icon, chemistry vector",
        "keywords": ["wash bottle", "squeeze bottle", "bottle", "rinse", "solvent", "plastic", "nozzle"],
        "body": """
<path d="M20 26a4 4 0 0 1 4-4h16a4 4 0 0 1 4 4v28a4 4 0 0 1-4 4H24a4 4 0 0 1-4-4z"/>
<path d="M26 22v-5h12v5"/>
<path d="M32 17V9c0-2 1-3 3-3h11l5 5"/>
<path d="M26 36h12M26 42h8"/>
""",
    },
]
