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
from textpath import formula, text, width

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


def element_of_day(p, W, H):
    out = [hexes(80, H - 60, 70, 3, p["line"], 2, 4)]
    m = W * .08
    out.append(pill("ELEMENT OF THE DAY", m, H * .08, W * .026, p["accent"], "#FFFFFF"))
    ts = W * .42
    tx, ty = (W - ts) / 2, H * .2
    out.append(f'<rect x="{tx}" y="{ty}" width="{ts}" height="{ts}" rx="{ts * .08}" fill="#8ACBEF" '
               f'stroke="#1E2A3A" stroke-width="{W * .006}"/>'
               + text("8", tx + ts * .1, ty + ts * .18, ts * .12, "#1E2A3A", "SemiBold", "start")
               + text("O", tx + ts / 2, ty + ts * .66, ts * .46, "#1E2A3A", "Bold")
               + text("Oxygen", tx + ts / 2, ty + ts * .82, ts * .1, "#1E2A3A", "SemiBold")
               + text("15.999", tx + ts / 2, ty + ts * .93, ts * .07, "#1E2A3A", "Regular"))
    facts = [("Atomic number", "8"), ("Atomic mass", "15.999"), ("Group", "16"), ("Period", "2")]
    fy = ty + ts + H * .07
    cw = (W - 2 * m - 3 * 16) / 4
    for i, (k, v) in enumerate(facts):
        x = m + i * (cw + 16)
        out.append(f'<rect x="{x:.1f}" y="{fy:.1f}" width="{cw:.1f}" height="{H * .12:.1f}" rx="18" fill="{p["card"]}"/>'
                   + text(v, x + cw / 2, fy + H * .065, W * .045, p["accent2"], "Bold")
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
]

KEYWORDS = ["social media", "template", "instagram", "post", "story", "youtube thumbnail", "chemistry", "science",
            "education", "school", "teacher", "content", "editable", "layout", "banner", "quiz", "fact", "did you know",
            "laboratory", "atom", "molecule", "element", "dark", "modern", "design", "vector", "illustration",
            "marketing", "channel", "learning", "student", "lesson", "infographic", "card", "promo"]


def assets():
    out = []
    for key, fn, (W, H), title in DESIGNS:
        for pname, p in PALETTES.items():
            inner = "".join(fn(p, W, H))
            svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W * 2}" height="{H * 2}" viewBox="0 0 {W} {H}">\n'
                   f'<rect x="-1" y="-1" width="{W + 2}" height="{H + 2}" fill="{p["bg"]}"/>'
                   f'<clipPath id="sm"><rect width="{W}" height="{H}"/></clipPath><g clip-path="url(#sm)">{inner}</g>'
                   '\n</svg>\n')
            out.append(dict(name=f"{SET_ID}-{key}-{pname}", svg=svg, size=4000, png=False,
                            title=f"{title}, {p['mood']} background, editable vector layout", keywords=KEYWORDS))
    return [(SET_ID, out)]
