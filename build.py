#!/usr/bin/env python3
"""Bangun aset microstock dari definisi di src/.

Jenis set:
  - set ikon (modul dengan ICONS): ikon tunggal + lembar set, opsional varian
    glyph (solid gelap) dan pola seamless dari ikon-ikonnya
  - set poster (modul dengan fungsi assets()): ilustrasi utuh, mis. tabel periodik

Keluaran per set di dist/<set>/: svg/ eps/ jpg/ png/ + adobe_stock.csv +
shutterstock.csv, lalu dist/<set>.zip siap unggah.

Pemakaian: python build.py [--size 4000] [--only lab-flat-icons ...]
"""
import argparse
import csv
import importlib
import io
import os
import random
import re
import shutil
import sys
import zipfile
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import cairocffi
import cairosvg
from cairosvg.surface import Surface
from PIL import Image

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "src"))

MODULES = ["icons_lab", "icons_lab_flat", "icons_lab2", "molecules", "molecules2", "atoms", "atoms2", "icons_concepts", "ghs_icons", "element_tiles",
           "kawaii", "kawaii2", "kawaii3", "periodic", "posters", "hex_patterns", "backgrounds", "social", "social_compounds", "coloring", "printables"]


def category(set_id):
    """Folder kategori untuk sebuah set (pemetaan aset)."""
    if set_id.endswith("patterns"):
        return "4-pola-seamless"
    if set_id.endswith("backgrounds"):
        return "5-latar-presentasi"
    if set_id.startswith("kawaii"):
        return "8-stiker-kawaii"
    if set_id.startswith("social"):
        return "6-template-sosmed"
    if "coloring" in set_id or "printables" in set_id:
        return "7-lembar-kerja-mewarnai"
    if set_id.startswith(("periodic", "chemistry-posters")):
        return "3-poster-edukasi"
    if set_id.startswith(("molecule", "bohr", "concept", "element")):
        return "2-molekul-atom"
    return "1-alat-lab"

from render import GRID, INK, STROKE, chalkify, doodlify, fitted, outlinify, style_attrs  # noqa: E402

PAD = 3  # ruang kosong di sekeliling ikon, dalam satuan grid
GLYPH_INK = "#1E2A3A"
from icons_lab_flat import G as _G, M as _M, W as _W, dark as _dark  # noqa: E402

# Warna yang menjadi putih di varian glyph (kaca, logam, putih); sisanya tinta gelap.
GLYPH_LIGHT = {c.upper() for c in (_W, _G, _M, _dark(_G, .07), _dark(_G, .14), _dark(_M, .14), _dark(_W, .14),
                                   "#FFE7A3", "#FFD978")}


class EPS2Surface(Surface):
    """EPS dibatasi ke PostScript level 2 supaya aman untuk syarat 'EPS 10'."""

    def _create_surface(self, width, height):
        surface = cairocffi.PSSurface(self.output, width, height)
        surface.restrict_to_level(cairocffi.PS_LEVEL_2)
        surface.set_eps(True)
        return surface, width, height


def svg_doc(w, h, inner, px_w=None, bg=None):
    px_w = px_w or w * 10
    bgrect = f'<rect x="0" y="0" width="{w}" height="{h}" fill="{bg}"/>' if bg else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{px_w}" height="{px_w * h / w:.0f}" '
            f'viewBox="0 0 {w} {h}">\n{bgrect}{inner}\n</svg>\n')


# ---------------------------------------------------------------- ikon

def glyphify(body, extra_light=()):
    """Varian glyph: semua warna menjadi tinta gelap, warna terang menjadi putih."""
    light = GLYPH_LIGHT | {c.upper() for x in extra_light for c in (x, _dark(x, .14))}

    def sub(m):
        attr, col = m.group(1), m.group(2).upper()
        if attr == "stroke" and col == "#FFFFFF":
            return m.group(0)
        return f'{attr}="{"#FFFFFF" if col in light else GLYPH_INK}"'
    return re.sub(r'(fill|stroke)="(#[0-9A-Fa-f]{6})"', sub, body)


def icon_doc(body, stroke, shadow):
    v = GRID + 2 * PAD
    inner = (f'<g transform="translate({PAD} {PAD})"><g {style_attrs(stroke)}>'
             f'{fitted(body, stroke, shadow)}</g></g>')
    return svg_doc(v, v, inner, px_w=1000)


def sheet_doc(bodies, stroke, shadow, cols=5, cell=80):
    rows = -(-len(bodies) // cols)
    w, h = cols * cell, rows * cell
    off = (cell - GRID) / 2
    parts = []
    for i, b in enumerate(bodies):
        x, y = (i % cols) * cell + off, (i // cols) * cell + off
        parts.append(f'<g transform="translate({x} {y})">{fitted(b, stroke, shadow)}</g>')
    return svg_doc(w, h, f'<g {style_attrs(stroke)}>' + "".join(parts) + "</g>")


def pattern_doc(bodies, stroke, bg, seed, accent, n=4, cell=90, size=0.62, ink=INK):
    """Pola seamless: ikon disebar dengan baris berselang (half-drop), diputar
    acak, plus titik/plus dekoratif. Elemen yang melewati tepi diulang di sisi
    seberang sehingga ubin menyambung tanpa sambungan."""
    rnd = random.Random(seed)
    W = H = n * cell
    items = []
    order = bodies[:]
    rnd.shuffle(order)
    k = 0
    for cx in range(n):
        for cy in range(n):
            x = cx * cell + cell / 2
            y = cy * cell + cell / 2 + (cell / 2 if cx % 2 else 0)
            s = size * cell / GRID * rnd.uniform(.9, 1.05)
            a = rnd.uniform(-22, 22)
            b = order[k % len(order)]
            k += 1
            items.append(f'<g transform="translate({x:.2f} {y:.2f}) rotate({a:.1f}) scale({s:.4f}) '
                         f'translate({-GRID / 2} {-GRID / 2})">{fitted(b, stroke / s * .9)}</g>')
            # dekorasi kecil di sela ikon
            dx, dy = x + cell / 2, y + rnd.uniform(-.15, .15) * cell
            if rnd.random() < .5:
                items.append(f'<circle cx="{dx:.2f}" cy="{dy:.2f}" r="{rnd.uniform(1.6, 2.6):.2f}" '
                             f'fill="{accent}" stroke="none"/>')
            else:
                r = rnd.uniform(2.5, 3.5)
                items.append(f'<path d="M{dx - r:.2f} {dy:.2f}h{2 * r:.2f}M{dx:.2f} {dy - r:.2f}v{2 * r:.2f}" '
                             f'stroke="{accent}" stroke-width="1.6"/>')
    tiled = []
    for it in items:
        for ox in (-W, 0, W):
            for oy in (-H, 0, H):
                tiled.append(f'<g transform="translate({ox} {oy})">{it}</g>' if (ox or oy) else it)
    inner = (f'<clipPath id="tile"><rect width="{W}" height="{H}"/></clipPath>'
             f'<g clip-path="url(#tile)"><g {style_attrs(stroke, ink)}>' + "".join(tiled) + "</g></g>")
    return svg_doc(W, H, inner, bg=bg)


def icon_set_assets(mod):
    """Hasilkan [(set_id, [aset...])] untuk satu modul ikon."""
    stroke = getattr(mod, "STROKE", STROKE)
    shadow = getattr(mod, "SHADOW", False)
    out = []

    def variant(set_id, bodies, title_fn, set_title, set_kw, common_kw, shadow, extra_kw=()):
        assets = [dict(name=f"{set_id}-set", svg=sheet_doc(bodies, stroke, shadow), size=5000,
                       title=set_title, keywords=list(extra_kw) + set_kw)]
        for ic, b in zip(mod.ICONS, bodies):
            assets.append(dict(name=f"{set_id}-{ic['id']}", svg=icon_doc(b, stroke, shadow), size=4000,
                               title=title_fn(ic), keywords=list(extra_kw) + ic["keywords"] + common_kw))
        return assets

    bodies = [ic["body"] for ic in mod.ICONS]
    out.append((mod.SET_ID, variant(mod.SET_ID, bodies, lambda ic: ic["title"], mod.SET_TITLE,
                                    mod.SET_KEYWORDS, mod.COMMON_KEYWORDS, shadow)))

    if getattr(mod, "GLYPH", False):
        gid = mod.SET_ID.replace("-icons", "") + "-glyph-icons"
        gb = [glyphify(ic["body"], ic.get("glyph_light", ())) for ic in mod.ICONS]
        theme = mod.THEME
        out.append((gid, variant(
            gid, gb,
            lambda ic: f"{ic.get('name') or ic['id'].replace('-', ' ').capitalize()} solid glyph icon, {theme} vector",
            f"{theme.capitalize()} solid glyph icons set, 20 black vector pictograms",
            mod.SET_KEYWORDS, mod.COMMON_KEYWORDS, False,
            extra_kw=("glyph", "solid", "black", "silhouette", "pictogram", "monochrome"))))

    if getattr(mod, "GLYPH", False):
        oid = mod.SET_ID.replace("-flat-icons", "").replace("-icons", "") + "-outline-icons"
        ob = [outlinify(ic["body"]) for ic in mod.ICONS]
        theme = mod.THEME
        out.append((oid, variant(
            oid, ob,
            lambda ic: f"{ic.get('name') or ic['id'].replace('-', ' ').capitalize()} outline line icon, "
                       f"{theme} vector for coloring",
            f"{theme.capitalize()} outline line icons set, 20 black and white vector icons",
            mod.SET_KEYWORDS, mod.COMMON_KEYWORDS, False,
            extra_kw=("outline", "line icon", "line art", "black and white", "coloring", "linear"))))

    if getattr(mod, "DOODLE", False):
        did = mod.SET_ID.replace("-flat-icons", "").replace("-icons", "") + "-doodle-icons"
        db = [doodlify(ic["body"]) for ic in mod.ICONS]
        theme = mod.THEME
        out.append((did, variant(
            did, db,
            lambda ic: f"{ic.get('name') or ic['id'].replace('-', ' ').capitalize()} hand drawn doodle icon, "
                       f"{theme} sketch vector",
            f"{theme.capitalize()} hand drawn doodle icons set, 20 black and white sketch vectors",
            mod.SET_KEYWORDS, mod.COMMON_KEYWORDS, False,
            extra_kw=("doodle", "hand drawn", "sketch", "line art", "black and white", "drawing"))))
        out.append((did.replace("-icons", "-patterns"), [dict(
            name=did.replace("-icons", "-pattern") + "-01",
            svg=pattern_doc(db, stroke, "#FFFFFF", seed=99, accent="#1E2A3A"), size=4000, png=False,
            title=f"{theme.capitalize()} hand drawn doodle seamless pattern, black and white vector background",
            keywords=["seamless pattern", "doodle", "hand drawn", "sketch", "black and white", "background",
                      "pattern", "line art", "coloring", "texture", "wallpaper"] + mod.SET_KEYWORDS)]))

    if getattr(mod, "GLYPH", False):
        # pola garis: kapur di papan hijau dan garis putih di atas navy
        lid = mod.SET_ID.replace("-flat-icons", "").replace("-icons", "") + "-line-patterns"
        assets = []
        for k, (bg, chalk, mood, kw) in enumerate((
                ("#2F4A3A", "#F2F1EA", "chalkboard style on green board", ["chalkboard", "chalk", "blackboard"]),
                ("#16213A", "#E9F1F7", "white line icons on dark navy", ["line icons", "dark", "navy"]))):
            cb = [chalkify(ic["body"], bg, chalk) for ic in mod.ICONS]
            assets.append(dict(
                name=f"{lid}-{k + 1:02d}", png=False, size=4000,
                svg=pattern_doc(cb, stroke, bg, seed=40 + k, accent=chalk, ink=chalk[1:]),
                title=f"{mod.THEME.capitalize()} seamless pattern, {mood}, vector background",
                keywords=["seamless pattern", "pattern", "background", "seamless", "line art", "school",
                          "wallpaper", "texture", "repeat"] + kw + mod.SET_KEYWORDS))
        out.append((lid, assets))

    if getattr(mod, "PATTERNS", None):
        pid = mod.SET_ID.replace("-icons", "") + "-patterns"
        assets = []
        for i, (bg, accent, mood) in enumerate(mod.PATTERNS):
            assets.append(dict(
                name=f"{pid}-{i + 1:02d}", svg=pattern_doc(bodies, stroke, bg, seed=i * 7 + 1, accent=accent),
                size=4000, png=False,
                title=f"{mod.THEME.capitalize()} seamless pattern, {mood} vector background",
                keywords=["seamless pattern", "pattern", "background", "seamless", "repeat", "wallpaper",
                          "texture", "wrapping paper", "fabric", "textile", "print", "backdrop", "tile"]
                         + mod.SET_KEYWORDS))
        out.append((pid, assets))
    return out


# ---------------------------------------------------------------- ekspor

def _width(svg):
    return float(svg.split('width="', 1)[1].split('"', 1)[0])


def export(a, out):
    name, svg = a["name"], a["svg"]
    data = svg.encode()
    (out / "svg" / f"{name}.svg").write_bytes(data)
    eps = io.BytesIO()
    EPS2Surface.convert(bytestring=data, write_to=eps)
    (out / "eps" / f"{name}.eps").write_bytes(eps.getvalue())

    png = cairosvg.svg2png(bytestring=data, scale=a["size"] / _width(svg))
    img = Image.open(io.BytesIO(png)).convert("RGBA")
    if a.get("png", True):
        img.save(out / "png" / f"{name}.png", optimize=True)
    bg = Image.new("RGB", img.size, "white")
    bg.paste(img, mask=img.split()[3])
    bg.save(out / "jpg" / f"{name}.jpg", quality=95, dpi=(300, 300))


def clean_keywords(words, limit=49):
    seen, out = set(), []
    for w in words:
        k = w.strip().lower()
        if k and k not in seen:
            seen.add(k)
            out.append(k)
    return out[:limit]


def write_set(set_id, assets, dist, scale):
    out = dist / set_id
    shutil.rmtree(out, ignore_errors=True)
    for sub in ("svg", "eps", "jpg", "png"):
        (out / sub).mkdir(parents=True)
    for a in assets:
        a["size"] = int(a["size"] * scale)
    if POOL:  # ekspor paralel: EPS + PNG + JPG tiap aset di proses terpisah
        list(POOL.map(export, assets, [out] * len(assets)))
    else:
        for a in assets:
            export(a, out)

    with open(out / "adobe_stock.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Filename", "Title", "Keywords", "Category", "Releases"])
        for a in assets:
            w.writerow([f"{a['name']}.eps", a["title"], ", ".join(clean_keywords(a["keywords"])), 16, ""])

    with open(out / "shutterstock.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Filename", "Description", "Keywords", "Categories",
                    "Illustration", "Mature Content", "Editorial"])
        for a in assets:
            w.writerow([f"{a['name']}.eps", a["title"], ",".join(clean_keywords(a["keywords"], 50)),
                        "Science,Education", "yes", "no", "no"])

    zpath = dist / f"{set_id}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(out.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(dist))
    print(f"{len(assets):3d} aset -> {dist.name}/{zpath.name}")


POOL = None


def main():
    global POOL
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", type=int, default=4000, help="sisi panjang raster ikon tunggal (px)")
    ap.add_argument("--out", default="dist")
    ap.add_argument("--only", nargs="*", help="hanya bangun set dengan id ini")
    ap.add_argument("--jobs", type=int, default=os.cpu_count() or 1, help="jumlah proses ekspor paralel")
    args = ap.parse_args()
    if args.jobs > 1:
        POOL = ProcessPoolExecutor(max_workers=args.jobs)
    dist = ROOT / args.out
    dist.mkdir(exist_ok=True)
    scale = args.size / 4000

    catalog = []
    for modname in MODULES:
        mod = importlib.import_module(modname)
        sets = mod.assets() if hasattr(mod, "assets") else icon_set_assets(mod)
        for set_id, assets in sets:
            if args.only and set_id not in args.only:
                continue
            cat = category(set_id)
            (dist / cat).mkdir(exist_ok=True)
            write_set(set_id, assets, dist / cat, scale)
            catalog += [(cat, set_id, f"{a['name']}.eps", a["title"]) for a in assets]

    with open(dist / "katalog.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Kategori", "Set", "File", "Judul"])
        w.writerows(catalog)
    print(f"Total {len(catalog)} aset, katalog: {args.out}/katalog.csv")
    if POOL:
        POOL.shutdown()


if __name__ == "__main__":
    main()
