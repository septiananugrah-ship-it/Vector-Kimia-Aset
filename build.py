#!/usr/bin/env python3
"""Bangun aset microstock dari definisi ikon di src/.

Keluaran (folder dist/):
  svg/  - vektor sumber
  eps/  - EPS (PostScript level 2, kompatibel EPS 10)
  jpg/  - pratinjau JPG berlatar putih
  png/  - PNG transparan
  adobe_stock.csv, shutterstock.csv - judul & keyword per file
  <set>.zip - semua di atas, siap unggah

Pemakaian: python build.py [--size 4000] [--color 1E2A3A]
"""
import argparse
import csv
import io
import shutil
import sys
import zipfile
from pathlib import Path

import cairocffi
import cairosvg
from cairosvg.surface import Surface
from PIL import Image

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "src"))
import icons_lab  # noqa: E402
import icons_lab_flat  # noqa: E402

SETS = [icons_lab, icons_lab_flat]

GRID = 64
PAD = 3  # ruang kosong di sekeliling ikon, dalam satuan grid
STROKE = 2.5  # bawaan; set bisa menimpa lewat atribut STROKE
SHADOW_COLOR = "#E4E8EE"


class EPS2Surface(Surface):
    """EPS dibatasi ke PostScript level 2 supaya aman untuk syarat 'EPS 10'."""

    def _create_surface(self, width, height):
        surface = cairocffi.PSSurface(self.output, width, height)
        surface.restrict_to_level(cairocffi.PS_LEVEL_2)
        surface.set_eps(True)
        return surface, width, height


def style_attrs(color, stroke):
    return (f'fill="none" stroke="#{color}" stroke-width="{stroke}" '
            'stroke-linecap="round" stroke-linejoin="round"')


def bbox(body, stroke):
    """Kotak pembatas (x0, y0, x1, y1) ikon dalam satuan grid, termasuk garis tepi."""
    k, m = 10, 32  # piksel per satuan, margin
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{(GRID + 2 * m) * k}" '
           f'height="{(GRID + 2 * m) * k}" viewBox="{-m} {-m} {GRID + 2 * m} {GRID + 2 * m}">'
           f'<g {style_attrs("000000", stroke)}>{body}</g></svg>')
    img = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode())))
    x0, y0, x1, y1 = img.getchannel("A").getbbox()
    return x0 / k - m, y0 / k - m, x1 / k - m, y1 / k - m


def fitted(ic, mod):
    """Skalakan ikon agar mengisi grid 64x64 dengan ukuran visual seragam.

    Tebal garis dikompensasi supaya sama di semua ikon. Set dengan SHADOW
    mendapat bayangan elips di bawah benda.
    """
    stroke = getattr(mod, "STROKE", STROKE)
    shadow = getattr(mod, "SHADOW", False)
    x0, y0, x1, y1 = bbox(ic["body"], stroke)
    w, h = x1 - x0, y1 - y0
    area_h = GRID - (5 if shadow else 0)
    sc = min(GRID / w, area_h / h)
    tx = (GRID - w * sc) / 2 - x0 * sc
    ty = (area_h - h * sc) / 2 - y0 * sc if not shadow else area_h - h * sc - y0 * sc
    out = ""
    if shadow:
        out += (f'<ellipse cx="{GRID / 2}" cy="{area_h + 1.2:.2f}" rx="{min(w * sc * .48, 30):.2f}" '
                f'ry="2.6" fill="{SHADOW_COLOR}" stroke="none"/>')
    out += (f'<g transform="translate({tx:.3f} {ty:.3f}) scale({sc:.4f})" '
            f'stroke-width="{stroke / sc:.3f}">{ic["body"]}</g>')
    return out


def icon_svg(ic, mod, color, px=1000):
    v = GRID + 2 * PAD
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{px}" height="{px}" '
            f'viewBox="{-PAD} {-PAD} {v} {v}">\n'
            f'<g {style_attrs(color, getattr(mod, "STROKE", STROKE))}>{fitted(ic, mod)}</g>\n</svg>\n')


def sheet_svg(mod, color, cols=5, cell=80):
    icons = mod.ICONS
    rows = -(-len(icons) // cols)
    w, h = cols * cell, rows * cell
    off = (cell - GRID) / 2
    parts = []
    for i, ic in enumerate(icons):
        x, y = (i % cols) * cell + off, (i // cols) * cell + off
        parts.append(f'<g transform="translate({x} {y})">{fitted(ic, mod)}</g>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w * 10}" height="{h * 10}" '
            f'viewBox="0 0 {w} {h}">\n<g {style_attrs(color, getattr(mod, "STROKE", STROKE))}>\n'
            + "\n".join(parts) + "\n</g>\n</svg>\n")


def export(name, svg, out, long_side):
    data = svg.encode()
    (out / "svg" / f"{name}.svg").write_bytes(data)
    eps = io.BytesIO()
    EPS2Surface.convert(bytestring=data, write_to=eps)
    (out / "eps" / f"{name}.eps").write_bytes(eps.getvalue())

    png = cairosvg.svg2png(bytestring=data, scale=long_side / _width(svg))
    img = Image.open(io.BytesIO(png)).convert("RGBA")
    img.save(out / "png" / f"{name}.png", optimize=True)
    bg = Image.new("RGB", img.size, "white")
    bg.paste(img, mask=img.split()[3])
    bg.save(out / "jpg" / f"{name}.jpg", quality=95, dpi=(300, 300))


def _width(svg):
    return float(svg.split('width="', 1)[1].split('"', 1)[0])


def clean_keywords(words, limit=49):
    seen, out = set(), []
    for w in words:
        k = w.strip().lower()
        if k and k not in seen:
            seen.add(k)
            out.append(k)
    return out[:limit]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--size", type=int, default=4000, help="sisi panjang raster (px)")
    ap.add_argument("--color", default="1E2A3A", help="warna garis (hex tanpa #)")
    ap.add_argument("--out", default="dist")
    args = ap.parse_args()

    for mod in SETS:
        build_set(mod, args)


def build_set(mod, args):
    out = ROOT / args.out / mod.SET_ID
    shutil.rmtree(out, ignore_errors=True)
    for sub in ("svg", "eps", "jpg", "png"):
        (out / sub).mkdir(parents=True)

    rows = []  # (nama file, judul, keywords)
    sheet_name = f"{mod.SET_ID}-set"
    export(sheet_name, sheet_svg(mod, args.color), out, int(args.size * 1.25))
    rows.append((sheet_name, mod.SET_TITLE, clean_keywords(mod.SET_KEYWORDS)))

    for ic in mod.ICONS:
        name = f"{mod.SET_ID}-{ic['id']}"
        export(name, icon_svg(ic, mod, args.color), out, args.size)
        rows.append((name, ic["title"], clean_keywords(ic["keywords"] + mod.COMMON_KEYWORDS)))

    with open(out / "adobe_stock.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Filename", "Title", "Keywords", "Category", "Releases"])
        for name, title, kw in rows:
            w.writerow([f"{name}.eps", title, ", ".join(kw), 16, ""])  # 16 = Science

    with open(out / "shutterstock.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Filename", "Description", "Keywords", "Categories",
                    "Illustration", "Mature Content", "Editorial"])
        for name, title, kw in rows:
            w.writerow([f"{name}.eps", title, ",".join(kw[:50]), "Science,Objects",
                        "yes", "no", "no"])

    zpath = ROOT / args.out / f"{mod.SET_ID}.zip"
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(out.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(out.parent))
    print(f"{len(rows)} aset -> {zpath}")


if __name__ == "__main__":
    main()
