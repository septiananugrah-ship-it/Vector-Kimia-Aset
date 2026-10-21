"""Template media sosial bertema kimia: post persegi, story 9:16, dan thumbnail
YouTube 16:9. Teks contoh berupa placeholder yang bisa diganti pembeli.
"""
import math
import random

import atoms
import icons_concepts
import icons_lab2
import icons_lab_flat
import molecules
from render import GRID, fitted, style_attrs
import poster_kit
from poster_i18n import TR
from poster_kit import text, tr
from textpath import formula, width

SET_ID = "social-media-templates"

PALETTES = {
    "navy": dict(bg="#16213A", card="#1F2C48", line="#2C3D5E", ink="#FFFFFF", sub="#AEB9C9", accent="#3FB6C4",
                 accent2="#FFC845", mood="dark navy"),
    "purple": dict(bg="#251B45", card="#33275C", line="#45387A", ink="#FFFFFF", sub="#C4B9E8", accent="#F28C28",
                   accent2="#5CBF7A", mood="deep purple"),
}


def icons(mod):
    return {ic["id"]: (ic["body"], mod.STROKE) for ic in mod.ICONS}


ALL = {}
for _m in (icons_lab_flat, icons_lab2, molecules, atoms, icons_concepts):
    ALL.update(icons(_m))


def place(icon_id, x, y, size, rot=0):
    body, stroke = ALL[icon_id]
    return (f'<g transform="translate({x:.1f} {y:.1f}) rotate({rot}) scale({size / GRID:.4f}) '
            f'translate({-GRID / 2} {-GRID / 2})"><g {style_attrs(stroke)}>{fitted(body, stroke)}</g></g>')


def wrap(s, size, max_w, weight="Regular"):
    lines, cur = [], ""
    for w_ in s.split():
        t = (cur + " " + w_).strip()
        if width(t, size, weight) > max_w and cur:
            lines.append(cur)
            cur = w_
        else:
            cur = t
    return lines + [cur]


def para(s, x, y, size, fill, max_w, weight="Regular", anchor="start", lh=1.4):
    s = tr(s)
    return "".join(text(line, x, y + i * size * lh, size, fill, weight, anchor)
                   for i, line in enumerate(wrap(s, size, max_w, weight)))


def hexes(cx, cy, s, n, col, seed, w=3):
    rnd = random.Random(seed)
    out = []
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            x = cx + i * s * 1.5
            y = cy + j * s * math.sqrt(3) + (s * math.sqrt(3) / 2 if i % 2 else 0)
            if math.hypot(x - cx, y - cy) > n * s * 1.6 or rnd.random() < .35:
                continue
            pts = [(x + s * math.cos(math.radians(60 * k)), y + s * math.sin(math.radians(60 * k))) for k in range(6)]
            out.append("M" + "L".join(f"{a:.1f} {b:.1f}" for a, b in pts) + "z")
    return f'<path d="{"".join(out)}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round"/>'


def pill(label, x, y, size, bg, fg):
    label = tr(label)
    w = width(label, size, "Bold") + size * 1.6
    h = size * 1.9
    return (f'<rect x="{x}" y="{y}" width="{w:.1f}" height="{h:.1f}" rx="{h / 2:.1f}" fill="{bg}"/>'
            + text(label, x + w / 2, y + h * .68, size, fg, "Bold"))


def handle(p, x, y, size=26, anchor="start"):
    return text("@yourhandle", x, y, size, p["sub"], "SemiBold", anchor)


# ------------------------------------------------------------ desain

def did_you_know(p, W, H):
    out = [hexes(W - 60, 80, 70, 3, p["line"], 1, 4)]
    m = W * .08
    out.append(pill("CHEMISTRY FACT", m, H * .1, W * .026, p["accent"], "#FFFFFF"))
    out.append(text("DID YOU", m, H * .26, W * .11, p["ink"], "Bold", "start"))
    out.append(text("KNOW?", m, H * .26 + W * .12, W * .11, p["accent2"], "Bold", "start"))
    out.append(para("Write your amazing chemistry fact here. Keep it short, clear and easy to read so your "
                    "audience remembers it.", m, H * .26 + W * .25, W * .036, p["sub"], W * .6))
    out.append(place("atom", W * .78, H * .62, W * .3, 0))
    out.append(handle(p, m, H - m * .8, W * .026))
    return out


def element_of_day(p, W, H, z=8):
    from periodic import CAT, ELEMENTS, NAMES_ID, position
    sym, name, mass, cat = ELEMENTS[z - 1]
    key = f"{z:02d}-{name.lower()}"
    if poster_kit._lang[0] == "id":
        name, mass = NAMES_ID[z - 1], mass.replace(".", ",")
    col, row = position(z)
    out = [hexes(80, H - 60, 70, 3, p["line"], 2, 4)]
    m = W * .08
    out.append(pill("ELEMENT OF THE DAY", m, H * .08, W * .026, p["accent"], "#FFFFFF"))
    if key in ALL:
        out.append(place(key, W - m - W * .09, H * .12, W * .17))
    ts = W * .42
    tx, ty = (W - ts) / 2, H * .2
    out.append(f'<rect x="{tx}" y="{ty}" width="{ts}" height="{ts}" rx="{ts * .08}" fill="{CAT[cat][1]}" '
               f'stroke="#1E2A3A" stroke-width="{W * .006}"/>'
               + text(str(z), tx + ts * .1, ty + ts * .18, ts * .12, "#1E2A3A", "SemiBold", "start")
               + text(sym, tx + ts / 2, ty + ts * .66, ts * (.46 if len(sym) == 1 else .4), "#1E2A3A", "Bold")
               + text(name, tx + ts / 2, ty + ts * .82, ts * .1, "#1E2A3A", "SemiBold")
               + text(mass, tx + ts / 2, ty + ts * .93, ts * .07, "#1E2A3A", "Regular"))
    facts = [("Atomic number", str(z)), ("Atomic mass", mass), ("Group", str(col + 1)), ("Period", str(row + 1))]
    fy = ty + ts + H * .07
    cw = (W - 2 * m - 3 * 16) / 4
    for i, (k, v) in enumerate(facts):
        x = m + i * (cw + 16)
        out.append(f'<rect x="{x:.1f}" y="{fy:.1f}" width="{cw:.1f}" height="{H * .12:.1f}" rx="18" fill="{p["card"]}"/>'
                   + text(v, x + cw / 2, fy + H * .065, W * (.045 if len(v) < 7 else .036), p["accent2"], "Bold")
                   + text(k, x + cw / 2, fy + H * .1, W * .02, p["sub"], "SemiBold"))
    out.append(handle(p, W / 2, H - m * .8, W * .026, "middle"))
    return out


def quiz(p, W, H):
    out = []
    m = W * .08
    out.append(pill("CHEMISTRY QUIZ", m, H * .07, W * .026, p["accent"], "#FFFFFF"))
    out.append(place("erlenmeyer-flask", W - m - W * .09, H * .1, W * .16, 10))
    out.append(para("Which gas makes up most of the Earth's atmosphere?", m, H * .22, W * .055, p["ink"], W * .7,
                    "Bold", lh=1.25))
    opts = [("A", "Oxygen"), ("B", "Nitrogen"), ("C", "Carbon dioxide"), ("D", "Argon")]
    oy = H * .44
    oh = (H * .44) / 4 - 18
    for i, (k, v) in enumerate(opts):
        y = oy + i * (oh + 18)
        out.append(f'<rect x="{m}" y="{y:.1f}" width="{W - 2 * m:.1f}" height="{oh:.1f}" rx="{oh / 2:.1f}" '
                   f'fill="{p["card"]}" stroke="{p["line"]}" stroke-width="3"/>'
                   f'<circle cx="{m + oh / 2:.1f}" cy="{y + oh / 2:.1f}" r="{oh * .36:.1f}" fill="{p["accent"]}"/>'
                   + text(k, m + oh / 2, y + oh / 2 + oh * .14, oh * .38, "#FFFFFF", "Bold")
                   + text(v, m + oh * 1.05, y + oh / 2 + oh * .13, oh * .36, p["ink"], "SemiBold", "start"))
    out.append(text("Comment your answer below!", W / 2, H - m * .8, W * .03, p["accent2"], "Bold"))
    return out


def lab_tip(p, W, H):
    out = [hexes(W - 40, H - 40, 70, 3, p["line"], 3, 4)]
    m = W * .08
    out.append(pill("LAB SAFETY TIP", m, H * .1, W * .026, p["accent"], "#FFFFFF"))
    out.append(f'<circle cx="{W / 2}" cy="{H * .38}" r="{W * .17}" fill="{p["card"]}"/>')
    out.append(place("safety-goggles", W / 2, H * .38, W * .26))
    out.append(text("Always wear", W / 2, H * .64, W * .07, p["ink"], "Bold"))
    out.append(text("safety goggles", W / 2, H * .64 + W * .085, W * .07, p["accent2"], "Bold"))
    out.append(para("Replace this text with a short explanation of your lab tip.", W / 2, H * .64 + W * .16,
                    W * .032, p["sub"], W * .7, anchor="middle"))
    out.append(handle(p, W / 2, H - m * .8, W * .026, "middle"))
    return out


def formula_day(p, W, H):
    out = [hexes(60, 60, 70, 3, p["line"], 4, 4)]
    m = W * .08
    out.append(pill("FORMULA OF THE DAY", m, H * .1, W * .026, p["accent"], "#FFFFFF"))
    out.append(f'<circle cx="{W / 2}" cy="{H * .42}" r="{W * .22}" fill="{p["card"]}"/>')
    out.append(place("water", W / 2, H * .42, W * .34))
    out.append(formula("H2O", W / 2, H * .76, W * .12, p["accent2"], "Bold"))
    out.append(text("Water: two hydrogen atoms bonded to one oxygen atom", W / 2, H * .83, W * .03, p["sub"],
                    "SemiBold"))
    out.append(handle(p, W / 2, H - m * .8, W * .026, "middle"))
    return out


def story_fact(p, W, H):
    out = [hexes(W / 2, H * .28, 80, 4, p["line"], 5, 4)]
    m = W * .09
    out.append(place("atom", W / 2, H * .26, W * .42))
    out.append(pill("CHEMISTRY FACT", W / 2 - W * .2, H * .45, W * .032, p["accent"], "#FFFFFF"))
    out.append(text("DID YOU", W / 2, H * .55, W * .12, p["ink"], "Bold"))
    out.append(text("KNOW?", W / 2, H * .55 + W * .14, W * .12, p["accent2"], "Bold"))
    out.append(para("Write your amazing chemistry fact here. Keep it short and easy to read.", W / 2,
                    H * .55 + W * .28, W * .045, p["sub"], W - 2 * m, anchor="middle"))
    out.append(text("Swipe up to learn more", W / 2, H - m * 1.2, W * .036, p["ink"], "SemiBold"))
    return out


def story_quiz(p, W, H):
    out = quiz(p, W, H * .62)
    out = [f'<g transform="translate(0 {H * .2:.1f})">' + "".join(out) + "</g>"]
    out.append(text("QUIZ TIME", W / 2, H * .12, W * .12, p["accent2"], "Bold"))
    out.append(place("idea-bulb", W / 2, H * .9, W * .2))
    return out


def thumb_big(p, W, H):
    out = [hexes(W * .78, H * .5, 70, 4, p["line"], 6, 4)]
    m = W * .05
    out.append(pill("CHEMISTRY", m, H * .1, W * .022, p["accent"], "#FFFFFF"))
    out.append(text("YOUR VIDEO", m, H * .42, W * .085, p["ink"], "Bold", "start"))
    out.append(text("TITLE HERE", m, H * .42 + W * .09, W * .085, p["accent2"], "Bold", "start"))
    out.append(text("Short subtitle or episode number", m, H * .42 + W * .14, W * .028, p["sub"], "SemiBold",
                    "start"))
    out.append(f'<circle cx="{W * .79}" cy="{H * .52}" r="{H * .36}" fill="{p["card"]}"/>')
    out.append(place("reaction-flask-smoke", W * .79, H * .52, H * .52, 8))
    return out


def thumb_vs(p, W, H):
    out = []
    out.append(f'<rect x="{W / 2}" y="0" width="{W / 2}" height="{H}" fill="{p["card"]}"/>')
    out.append(place("erlenmeyer-flask", W * .25, H * .42, H * .48, -8))
    out.append(place("round-bottom-flask", W * .75, H * .42, H * .48, 8))
    out.append(f'<circle cx="{W / 2}" cy="{H * .42}" r="{H * .12}" fill="{p["accent"]}"/>'
               + text("VS", W / 2, H * .42 + H * .045, H * .12, "#FFFFFF", "Bold"))
    out.append(text("ACID", W * .25, H * .86, H * .12, p["ink"], "Bold"))
    out.append(text("BASE", W * .75, H * .86, H * .12, p["accent2"], "Bold"))
    return out


def yt_banner(p, W, H):
    """Banner channel YouTube 2560x1440 (koordinat 1280x720); teks di area aman tengah."""
    out = [hexes(120, H / 2, 80, 4, p["line"], 7, 4), hexes(W - 120, H / 2, 80, 4, p["line"], 8, 4)]
    for key, x, y, sz, rot in (("atom", 150, 230, 150, 0), ("erlenmeyer-flask", 175, 470, 140, -10),
                               ("water", 1060, 220, 150, 0), ("microscope", 1140, 470, 150, 8),
                               ("test-tube-rack", 70, 600, 110, 0), ("dna", 1230, 330, 110, 0)):
        out.append(place(key, x, y, sz, rot))
    out.append(f'<rect x="{W / 2 - 387}" y="{H / 2 - 106}" width="774" height="212" rx="24" fill="{p["card"]}"/>')
    out.append(text("YOUR CHANNEL NAME", W / 2, H / 2 + 4, 58, p["ink"], "Bold"))
    out.append(text("Chemistry made easy · new videos every week", W / 2, H / 2 + 52, 22, p["accent2"], "SemiBold"))
    return out


def yt_endscreen(p, W, H):
    out = [hexes(W - 60, 60, 60, 3, p["line"], 9, 4)]
    out.append(text("THANKS FOR WATCHING!", W / 2, 110, 56, p["ink"], "Bold"))
    for k, x in enumerate((90, 690)):
        out.append(f'<rect x="{x}" y="200" width="500" height="281" rx="18" fill="{p["card"]}" stroke="{p["line"]}" '
                   'stroke-width="4" stroke-dasharray="14 10"/>')
        out.append(text("Video " + str(k + 1), x + 250, 352, 30, p["sub"], "SemiBold"))
    out.append(f'<circle cx="{W / 2}" cy="595" r="70" fill="{p["card"]}" stroke="{p["accent"]}" stroke-width="5"/>')
    out.append(place("atom", W / 2, 595, 100))
    out.append(text("SUBSCRIBE", W / 2 - 110, 608, 34, p["accent2"], "Bold", "end"))
    out.append(text("for more chemistry", W / 2 + 110, 608, 26, p["sub"], "SemiBold", "start"))
    return out


def chapter_card(p, W, H):
    out = [hexes(W - 100, H / 2, 80, 4, p["line"], 10, 4)]
    m = 90
    out.append(pill("CHAPTER 1", m, H * .3, 26, p["accent"], "#FFFFFF"))
    out.append(text("Your Chapter Title", m, H * .5, 80, p["ink"], "Bold", "start"))
    out.append(text("A short description of what this part covers", m, H * .5 + 60, 28, p["sub"], "SemiBold",
                    "start"))
    out.append(f'<rect x="{m}" y="{H * .5 + 100}" width="160" height="8" rx="4" fill="{p["accent2"]}"/>')
    out.append(f'<circle cx="{W * .8}" cy="{H / 2}" r="190" fill="{p["card"]}"/>')
    out.append(place("round-bottom-flask", W * .8, H / 2, 260, 6))
    return out


DESIGNS = [
    ("post-did-you-know", did_you_know, (1080, 1080), "Instagram post template, did you know chemistry fact"),
    ("post-element-of-the-day", element_of_day, (1080, 1080), "Instagram post template, element of the day"),
    ("post-quiz", quiz, (1080, 1080), "Instagram post template, chemistry quiz question with answer options"),
    ("post-lab-tip", lab_tip, (1080, 1080), "Instagram post template, laboratory safety tip"),
    ("post-formula-of-the-day", formula_day, (1080, 1080), "Instagram post template, chemical formula of the day"),
    ("story-did-you-know", story_fact, (1080, 1920), "Instagram story template, did you know chemistry fact"),
    ("story-quiz", story_quiz, (1080, 1920), "Instagram story template, chemistry quiz"),
    ("youtube-thumbnail-title", thumb_big, (1280, 720), "YouTube thumbnail template for chemistry video"),
    ("youtube-thumbnail-versus", thumb_vs, (1280, 720), "YouTube thumbnail template, acid versus base comparison"),
    ("youtube-channel-banner", yt_banner, (1280, 720), "YouTube channel art banner template for chemistry channel"),
    ("youtube-end-screen", yt_endscreen, (1280, 720), "YouTube end screen template for chemistry video"),
    ("video-chapter-title", chapter_card, (1280, 720), "Video chapter title card template for chemistry lesson"),
]

KEYWORDS = ["social media", "template", "instagram", "post", "story", "youtube thumbnail", "chemistry", "science",
            "education", "school", "teacher", "content", "editable", "layout", "banner", "quiz", "fact", "did you know",
            "laboratory", "atom", "molecule", "element", "dark", "modern", "design", "vector", "illustration",
            "marketing", "channel", "learning", "student", "lesson", "infographic", "card", "promo"]


def assets():
    sets = []
    for lang, set_id in (("en", SET_ID), ("id", SET_ID + "-indonesian")):
        poster_kit.set_lang(lang)
        out = []
        for key, fn, (W, H), title in DESIGNS:
            for pname, p in PALETTES.items():
                inner = "".join(fn(p, W, H))
                svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * 2}" height="{H * 2}" '
                       f'viewBox="0 0 {W} {H}">\n<rect x="-1" y="-1" width="{W + 2}" height="{H + 2}" fill="{p["bg"]}"/>'
                       f'<clipPath id="sm"><rect width="{W}" height="{H}"/></clipPath><g clip-path="url(#sm)">{inner}</g>'
                       '\n</svg>\n')
                note = " in Indonesian language" if lang == "id" else ""
                out.append(dict(name=f"{set_id}-{key}-{pname}", svg=svg, size=4000, png=False,
                                title=f"{title}{note}, {p['mood']} background, editable vector layout",
                                keywords=(["indonesian", "bahasa indonesia"] if lang == "id" else []) + KEYWORDS))
        sets.append((set_id, out))
        # paket post "Element of the day" untuk unsur 1-20 (tema navy)
        p = PALETTES["navy"]
        eid = "social-element-posts" + ("" if lang == "en" else "-indonesian")
        posts = []
        from periodic import ELEMENTS
        for z in range(1, 21):
            inner = "".join(element_of_day(p, 1080, 1080, z))
            name = ELEMENTS[z - 1][1]
            svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="2160" height="2160" viewBox="0 0 1080 1080">\n'
                   f'<rect x="-1" y="-1" width="1082" height="1082" fill="{p["bg"]}"/>'
                   f'<clipPath id="sm"><rect width="1080" height="1080"/></clipPath><g clip-path="url(#sm)">{inner}</g>'
                   '\n</svg>\n')
            note = " in Indonesian language" if lang == "id" else ""
            posts.append(dict(name=f"{eid}-{z:02d}-{name.lower()}", svg=svg, size=4000, png=False,
                              title=f"{name} element of the day social media post{note}, chemistry Instagram template",
                              keywords=(["indonesian", "bahasa indonesia"] if lang == "id" else [])
                              + [name.lower(), "element of the day", "chemical element"] + KEYWORDS))
        sets.append((eid, posts))
    poster_kit.set_lang("en")
    return sets


TR.update({
    "CHEMISTRY FACT": "FAKTA KIMIA", "DID YOU": "TAHUKAH", "KNOW?": "KAMU?",
    "Write your amazing chemistry fact here. Keep it short, clear and easy to read so your audience remembers it.":
        "Tulis fakta kimia menarikmu di sini. Buat singkat, jelas, dan mudah dibaca agar mudah diingat.",
    "ELEMENT OF THE DAY": "UNSUR HARI INI", "Atomic number": "Nomor atom", "Atomic mass": "Massa atom",
    "Group": "Golongan", "Period": "Periode", "CHEMISTRY QUIZ": "KUIS KIMIA",
    "Which gas makes up most of the Earth's atmosphere?": "Gas apa yang paling banyak di atmosfer Bumi?",
    "Comment your answer below!": "Tulis jawabanmu di kolom komentar!", "LAB SAFETY TIP": "TIPS KESELAMATAN LAB",
    "Always wear": "Selalu pakai", "safety goggles": "kacamata pelindung",
    "Replace this text with a short explanation of your lab tip.": "Ganti teks ini dengan penjelasan singkat tipsmu.",
    "FORMULA OF THE DAY": "RUMUS HARI INI",
    "Water: two hydrogen atoms bonded to one oxygen atom": "Air: dua atom hidrogen terikat pada satu atom oksigen",
    "Write your amazing chemistry fact here. Keep it short and easy to read.":
        "Tulis fakta kimia menarikmu di sini. Buat singkat dan mudah dibaca.",
    "Swipe up to learn more": "Geser ke atas untuk selengkapnya", "QUIZ TIME": "WAKTUNYA KUIS",
    "CHEMISTRY": "KIMIA", "YOUR VIDEO": "JUDUL VIDEO", "TITLE HERE": "KAMU DI SINI",
    "Short subtitle or episode number": "Subjudul singkat atau nomor episode", "ACID": "ASAM", "BASE": "BASA",
    "Oxygen": "Oksigen", "Nitrogen": "Nitrogen", "Carbon dioxide": "Karbon dioksida", "Argon": "Argon",
    "YOUR CHANNEL NAME": "NAMA CHANNEL KAMU",
    "Chemistry made easy · new videos every week": "Belajar kimia jadi mudah · video baru setiap minggu",
    "THANKS FOR WATCHING!": "TERIMA KASIH SUDAH MENONTON!", "SUBSCRIBE": "SUBSCRIBE",
    "for more chemistry": "untuk video kimia lainnya", "CHAPTER 1": "BAB 1",
    "Your Chapter Title": "Judul Bab Kamu",
    "A short description of what this part covers": "Deskripsi singkat isi bagian ini",
})
