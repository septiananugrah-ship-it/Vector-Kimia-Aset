"""Ikon gaya lencana/aplikasi tema gelap: ikon semi-flat di dalam kotak bulat navy.
Cocok untuk ikon aplikasi, sorotan Instagram (highlight cover), dan tombol situs bertema gelap.
"""
import icons_concepts
import icons_lab2
import icons_lab_flat
import molecules
from render import GRID, fitted, style_attrs

NAVY, RING = "#1B2742", "#2E4066"
KEYWORDS = ["app icon", "badge", "button", "dark", "navy", "dark mode", "rounded square", "highlight cover",
            "instagram highlight", "ui", "web", "chemistry", "science", "laboratory", "education", "icon", "vector",
            "flat", "colorful", "symbol"]

SETS = [
    ("lab-badge-icons-dark", (icons_lab_flat, icons_lab2), "laboratory equipment"),
    ("concept-badge-icons-dark", (icons_concepts, molecules), "science and molecule"),
]


def badge(body, stroke, ink="E9EEF5"):
    """Kotak bulat navy berbingkai tipis; ikon digambar dengan garis terang agar kontras."""
    k = 66 / GRID
    return (f'<rect x="3" y="3" width="94" height="94" rx="24" fill="{NAVY}"/>'
            f'<rect x="7" y="7" width="86" height="86" rx="20" fill="none" stroke="{RING}" stroke-width="2"/>'
            f'<g transform="translate(17 17) scale({k:.4f})"><g {style_attrs(stroke, ink)}>{fitted(body, stroke)}</g></g>')


def _doc(w, h, inner):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w * 40}" height="{h * 40}" viewBox="0 0 {w} {h}">\n'
            f'{inner}\n</svg>\n')


def assets():
    out = []
    for set_id, mods, what in SETS:
        items = [(ic, m.STROKE) for m in mods for ic in m.ICONS]
        assets_ = []
        for ic, stroke in items:
            name = ic.get("name", ic["id"].replace("-", " ")).split(" ball and stick")[0]
            assets_.append(dict(name=f"{set_id}-{ic['id']}", svg=_doc(100, 100, badge(ic["body"], stroke)), size=4000,
                                title=f"{name.capitalize()} {what} app icon in dark navy rounded square badge, "
                                      "vector symbol",
                                keywords=[w for w in ic["keywords"] if w != "isolated"][:8] + KEYWORDS))
        cols = 8
        rows = -(-len(items) // cols)
        sheet = "".join(f'<g transform="translate({(i % cols) * 110 + 5} {(i // cols) * 110 + 5})">'
                        f'{badge(ic["body"], st)}</g>' for i, (ic, st) in enumerate(items))
        assets_.insert(0, dict(name=f"{set_id}-set", svg=_doc(cols * 110, rows * 110, sheet), size=6000,
                               title=f"{what.capitalize()} app icons set, {len(items)} dark navy rounded square "
                                     "badges, vector collection",
                               keywords=["set", "collection", "icon set"] + KEYWORDS))
        out.append((set_id, assets_))
    return out
