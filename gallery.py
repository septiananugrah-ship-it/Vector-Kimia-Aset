#!/usr/bin/env python3
"""Galeri pratinjau HTML dari hasil build (dist/) untuk GitHub Pages.

Membuat dist/galeri/index.html + thumbnail JPG kecil per aset, dikelompokkan per
kategori dan set. Jalankan setelah build.py (dan promo.py bila ada).
"""
import csv
import html
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).parent
THUMB = 480

CAT_NAMES = {
    "1-alat-lab": "Alat laboratorium", "2-molekul-atom": "Molekul, atom & konsep",
    "3-poster-edukasi": "Poster edukasi", "4-pola-seamless": "Pola seamless",
    "5-latar-presentasi": "Latar presentasi & wallpaper", "6-template-sosmed": "Template media sosial & YouTube",
    "7-lembar-kerja-mewarnai": "Lembar kerja, mewarnai & printable", "8-stiker-kawaii": "Stiker kawaii",
    "9-promosi": "Gambar promosi bundle",
}

PAGE = """<!doctype html><html lang="id"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Galeri Vector Kimia</title>
<style>
:root{{--bg:#16213A;--card:#1F2C48;--ink:#fff;--sub:#AEB9C9;--acc:#3FB6C4}}
*{{box-sizing:border-box}}body{{margin:0;font-family:system-ui,-apple-system,Segoe UI,sans-serif;background:var(--bg);color:var(--ink)}}
header{{padding:24px 16px;text-align:center}}h1{{margin:0 0 6px;font-size:28px}}header p{{margin:0;color:var(--sub)}}
nav{{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;padding:0 16px 16px}}
nav a{{color:var(--ink);background:var(--card);padding:6px 12px;border-radius:999px;text-decoration:none;font-size:14px}}
section{{padding:8px 16px 24px;max-width:1400px;margin:0 auto}}h2{{color:var(--acc);margin:24px 0 8px}}
h3{{margin:16px 0 8px;font-size:15px;color:var(--sub);font-weight:600}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px}}
figure{{margin:0;background:var(--card);border-radius:10px;overflow:hidden}}
figure img{{width:100%;height:150px;object-fit:contain;background:#fff;display:block}}
figcaption{{font-size:11px;color:var(--sub);padding:6px 8px;line-height:1.3;max-height:3.9em;overflow:hidden}}
</style></head><body>
<header><h1>Galeri Vector Kimia</h1><p>{total} aset · klik gambar untuk ukuran lebih besar</p></header>
<nav>{nav}</nav>{body}</body></html>"""


def main():
    dist = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist"
    out = dist / "galeri"
    (out / "img").mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(open(dist / "katalog.csv", encoding="utf-8")))
    by_cat = {}
    for r in rows:
        by_cat.setdefault(r["Kategori"], {}).setdefault(r["Set"], []).append(r)
    promo = sorted((dist / "9-promosi").glob("*.jpg")) if (dist / "9-promosi").exists() else []
    nav, body, total = [], [], 0
    for cat in sorted(by_cat) + (["9-promosi"] if promo else []):
        nav.append(f'<a href="#{cat}">{html.escape(CAT_NAMES.get(cat, cat))}</a>')
        parts = [f'<section id="{cat}"><h2>{html.escape(CAT_NAMES.get(cat, cat))}</h2>']
        sets = by_cat.get(cat, {"promosi": [{"File": p.name, "Judul": p.stem, "_path": p} for p in promo]})
        for set_id, items in sets.items():
            parts.append(f"<h3>{html.escape(set_id)} · {len(items)}</h3><div class=grid>")
            for r in items:
                name = Path(r["File"]).stem
                src = r.get("_path") or dist / cat / set_id / "jpg" / f"{name}.jpg"
                if not Path(src).exists():
                    continue
                im = Image.open(src).convert("RGB")
                im.thumbnail((THUMB, THUMB))
                im.save(out / "img" / f"{name}.jpg", quality=80)
                big = out / "img" / f"{name}-big.jpg"
                if cat in ("3-poster-edukasi", "9-promosi", "7-lembar-kerja-mewarnai"):
                    im2 = Image.open(src).convert("RGB")
                    im2.thumbnail((1600, 1600))
                    im2.save(big, quality=82)
                    href = f"img/{name}-big.jpg"
                else:
                    href = f"img/{name}.jpg"
                parts.append(f'<figure><a href="{href}"><img loading="lazy" src="img/{name}.jpg" '
                             f'alt="{html.escape(r["Judul"])}"></a><figcaption>{html.escape(r["Judul"])}'
                             "</figcaption></figure>")
                total += 1
            parts.append("</div>")
        parts.append("</section>")
        body.append("".join(parts))
    (out / "index.html").write_text(PAGE.format(total=total, nav="".join(nav), body="".join(body)), encoding="utf-8")
    print(f"galeri: {total} gambar -> {out / 'index.html'}")


if __name__ == "__main__":
    main()
