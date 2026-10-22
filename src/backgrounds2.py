"""Latar presentasi jilid 2 (16:9) dan wallpaper HP (9:16), memakai set ikon yang lebih baru:
molekul jilid 2-3, atom Bohr jilid 2-3, stiker kawaii, ikon konsep, dan ubin unsur tema gelap.
Hiasan di tepi, sisanya copy space; tanpa transparansi (warna pudar = campuran ke warna latar).
"""
import atoms2
import atoms3
import element_tiles_dark1
import element_tiles_dark2
import icons_concepts
import kawaii
import kawaii2
import kawaii3
import kawaii4
import molecules2
import molecules3
from backgrounds import KEYWORDS, PH, PW, H, W, _items, hex_field, mix, phone_wall, scatter

SET_ID = "chemistry-vol2-backgrounds"  # akhiran "backgrounds" -> kategori 5-latar-presentasi


def bg_hex(bg, mods, accent, line_f, seed, side="right"):
    """Kisi heksagon memudar ke arah copy space + ikon di satu sisi."""
    line = mix(bg, accent, line_f)
    if side == "right":
        hexes = hex_field(bg, line, (W * .45, -60, W + 60, H + 60), seed=seed,
                          keep=lambda x, y: max(0, min(1, (x - W * .45) / (W * .4))))
        region = (W * .58, 30, W - 30, H - 30)
    else:
        hexes = hex_field(bg, line, (-60, -60, W * .55, H + 60), seed=seed,
                          keep=lambda x, y: max(0, min(1, (W * .55 - x) / (W * .4))))
        region = (30, 30, W * .42, H - 30)
    return hexes + scatter(_items(*mods), region, 8, (190, 290), seed)


def bg_band(bg, mods, accent, seed, n=9):
    """Pita ikon di bagian bawah, kisi heksagon tipis di atasnya."""
    hexes = hex_field(bg, mix(bg, accent, .14), (-60, H * .45, W + 60, H + 60), seed=seed,
                      keep=lambda x, y: max(0, min(1, (y - H * .45) / (H * .4))))
    return hexes + scatter(_items(*mods), (30, H * .64, W - 30, H - 20), n, (190, 250), seed, rot=15)


def bg_corners(bg, mods, seed, size=(220, 290), n=5):
    """Ikon berkumpul di sudut kanan atas dan kiri bawah (isi tiap sudut berbeda)."""
    items = _items(*mods)
    return (scatter(items[::2], (W * .6, 20, W - 20, H * .52), n, size, seed) +
            scatter(items[1::2], (20, H * .48, W * .4, H - 20), n, size, seed + 50))


MOLS = (molecules2, molecules3)
KAWAII = (kawaii, kawaii2, kawaii3)
VARIANTS = [
    ("hex-molecules-midnight", "#1A1530", lambda: bg_hex("#1A1530", MOLS, "#9B7FE0", .26, 31),
     "deep midnight purple with hexagon grid and molecules"),
    ("hex-molecules-white-left", "#FFFFFF", lambda: bg_hex("#FFFFFF", MOLS, "#3FB6C4", .3, 32, "left"),
     "white with hexagon grid and molecules on the left"),
    ("hex-molecules-mint", "#EEF8F4", lambda: bg_hex("#EEF8F4", MOLS, "#4BB04A", .3, 33),
     "soft mint with hexagon grid and molecules"),
    ("bohr-atoms-navy", "#16213A", lambda: bg_corners("#16213A", (atoms2, atoms3), 34, (250, 310)),
     "dark navy with Bohr atom models in the corners"),
    ("science-icons-teal", "#0F3B47", lambda: bg_hex("#0F3B47", (icons_concepts,), "#3FB6C4", .3, 35),
     "deep teal with hexagon grid and science icons"),
    ("element-tiles-dark", "#111A2E", lambda: bg_hex("#111A2E", (element_tiles_dark1, element_tiles_dark2),
                                                     "#3FB6C4", .2, 36, "left"),
     "very dark navy with dark periodic element tiles"),
    ("kawaii-lab-pink", "#FFF0F4", lambda: bg_band("#FFF0F4", KAWAII, "#F28CA8", 37),
     "cute pastel pink with kawaii lab stickers"),
    ("kawaii-molecules-blue", "#EEF6FF", lambda: bg_corners("#EEF6FF", (kawaii4,), 38),
     "cute pastel blue with kawaii molecule stickers"),
    ("kawaii-science-yellow", "#FFF9E0", lambda: bg_hex("#FFF9E0", (kawaii3, kawaii4), "#E0B23A", .3, 39),
     "cute pastel yellow with kawaii science stickers"),
    ("molecules-band-navy", "#16213A", lambda: bg_band("#16213A", MOLS, "#3FB6C4", 40),
     "dark navy with a band of molecules at the bottom"),
]

PHONE = [
    ("phone-kawaii-pink", "#FFF0F4", lambda: phone_wall("#FFF0F4", _items(*KAWAII, kawaii4), 41, .14),
     "cute kawaii chemistry stickers on pastel pink"),
    ("phone-molecules-midnight", "#1A1530", lambda: phone_wall("#1A1530", _items(*MOLS), 42, .22),
     "molecules on deep midnight purple"),
    ("phone-element-tiles-dark", "#111A2E",
     lambda: phone_wall("#111A2E", _items(element_tiles_dark1, element_tiles_dark2), 43, .16),
     "dark periodic element tiles on navy"),
    ("phone-bohr-atoms-teal", "#0F3B47", lambda: phone_wall("#0F3B47", _items(atoms2, atoms3), 44, .3),
     "Bohr atom models on deep teal"),
    ("phone-science-cream", "#FFF6E8", lambda: phone_wall("#FFF6E8", _items(icons_concepts), 45, .2),
     "science icons on cream"),
]


def assets():
    out = []
    for key, bg, fn, mood in VARIANTS:
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * 2}" height="{H * 2}" viewBox="0 0 {W} {H}">\n'
               f'<rect x="-1" y="-1" width="{W + 2}" height="{H + 2}" fill="{bg}"/>'
               f'<clipPath id="bgc"><rect width="{W}" height="{H}"/></clipPath><g clip-path="url(#bgc)">{fn()}</g>'
               '\n</svg>\n')
        out.append(dict(name=f"{SET_ID}-{key}", svg=svg, size=6000, png=False,
                        title=f"Chemistry science presentation background, {mood}, copy space vector banner",
                        keywords=KEYWORDS))
    for key, bg, fn, mood in PHONE:
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{PW * 2}" height="{PH * 2}" viewBox="0 0 {PW} {PH}">\n'
               f'<rect x="-1" y="-1" width="{PW + 2}" height="{PH + 2}" fill="{bg}"/>'
               f'<clipPath id="bgc"><rect width="{PW}" height="{PH}"/></clipPath><g clip-path="url(#bgc)">{fn()}</g>'
               '\n</svg>\n')
        out.append(dict(name=f"{SET_ID}-{key}", svg=svg, size=3000, png=False,
                        title=f"Chemistry phone wallpaper, {mood}, vertical 9:16 mobile background vector",
                        keywords=["phone wallpaper", "mobile wallpaper", "lock screen", "vertical", "9:16", "story",
                                  "background", "pattern"] + KEYWORDS[:30]))
    return [(SET_ID, out)]
