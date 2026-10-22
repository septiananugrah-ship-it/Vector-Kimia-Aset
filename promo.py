#!/usr/bin/env python3
"""Gambar promosi bundle (untuk listing Etsy/Lynk.id/Shopee) dari hasil build di dist/.

Jalankan setelah build.py. Membuat kolase JPG di dist/9-promosi/ beserta ZIP-nya.
Ini gambar pemasaran, bukan aset microstock.
"""
import io
import sys
import zipfile
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFilter

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "src"))
from textpath import text  # noqa: E402

W, H = 3000, 2000
BG = "#16213A"


def banner(title, sub, accent="#FFC845"):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
           f'<rect width="{W}" height="{H}" fill="{BG}"/>'
           f'<rect x="0" y="{H - 330}" width="{W}" height="330" fill="#0F1830"/>'
           + text(title, W / 2, H - 175, 120, "#FFFFFF")
           + text(sub, W / 2, H - 80, 54, accent, "SemiBold") + "</svg>")
    return Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode()))).convert("RGB")


def shadowed(img, size, angle=0):
    k = min(size[0] / img.width, size[1] / img.height)
    img = img.resize((max(1, int(img.width * k)), max(1, int(img.height * k))), Image.LANCZOS)
    pad = 40
    sh = Image.new("RGBA", (img.width + 2 * pad, img.height + 2 * pad), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rectangle([pad + 10, pad + 16, pad + img.width + 10, pad + img.height + 16],
                                 fill=(0, 0, 0, 150))
    sh = sh.filter(ImageFilter.GaussianBlur(16))
    sh.paste(img, (pad, pad))
    return sh.rotate(angle, expand=True, resample=Image.BICUBIC)


def collage(files, title, sub, cols, angles=(-3, 2, -1, 3, -2, 1)):
    base = banner(title, sub)
    rows = -(-len(files) // cols)
    cell = ((W - 120) // cols, (H - 330 - 80) // rows)
    x0 = (W - cols * cell[0]) // 2
    for i, f in enumerate(files):
        img = Image.open(f).convert("RGB")
        tile = shadowed(img, (cell[0] - 40, cell[1] - 40), angles[i % len(angles)])
        cx = x0 + (i % cols) * cell[0] + cell[0] // 2
        cy = 50 + (i // cols) * cell[1] + cell[1] // 2
        base.paste(tile, (cx - tile.width // 2, cy - tile.height // 2), tile)
    return base


def pick(dist, pattern, n):
    return sorted(dist.glob(pattern))[:n]


def main():
    dist = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "dist"
    out = dist / "9-promosi"
    out.mkdir(parents=True, exist_ok=True)
    cp = "3-poster-edukasi/chemistry-posters/jpg/"
    jobs = [
        ("bundle-posters-dark", [dist / f"{cp}chemistry-posters-{k}-dark.jpg" for k in
                                 ("ph-scale", "lab-equipment", "states-of-matter", "molecules", "atomic-models",
                                  "reaction-types")]
         + [dist / "3-poster-edukasi/periodic-table-posters/jpg/periodic-table-posters-dark.jpg"],
         "CHEMISTRY POSTERS BUNDLE", "95 posters · dark, light & chalkboard · English & Indonesian", 4),
        ("bundle-posters-indonesia", pick(dist, "3-poster-edukasi/chemistry-posters-indonesian/jpg/*-dark.jpg", 8),
         "PAKET POSTER KIMIA", "95 poster edukasi · versi Bahasa Indonesia · siap cetak", 4),
        ("bundle-icons", [dist / p for p in (
            "1-alat-lab/lab-flat-icons/jpg/lab-flat-icons-set.jpg",
            "1-alat-lab/lab2-flat-icons/jpg/lab2-flat-icons-set.jpg",
            "2-molekul-atom/molecule-icons/jpg/molecule-icons-set.jpg",
            "2-molekul-atom/concept-flat-icons/jpg/concept-flat-icons-set.jpg",
            "2-molekul-atom/bohr-atom-icons/jpg/bohr-atom-icons-set.jpg",
            "8-stiker-kawaii/kawaii-lab-stickers/jpg/kawaii-lab-stickers-set.jpg",
            "2-molekul-atom/element-tile-icons/jpg/element-tile-icons-set.jpg",
            "1-alat-lab/lab-doodle-icons/jpg/lab-doodle-icons-set.jpg")],
         "CHEMISTRY ICONS MEGA PACK", "Flat, glyph, outline, doodle & kawaii · EPS, SVG, PNG", 4),
        ("bundle-printables", [dist / "7-lembar-kerja-mewarnai" / p for p in (
            "chemistry-coloring-pages/jpg/chemistry-coloring-pages-lab-tools-1.jpg",
            "chemistry-printables/jpg/chemistry-printables-flashcards-lab-1.jpg",
            "chemistry-printables/jpg/chemistry-printables-certificate-navy-gold.jpg",
            "chemistry-printables/jpg/chemistry-printables-worksheet-label-lab-equipment-1.jpg",
            "chemistry-coloring-pages/jpg/chemistry-coloring-pages-science.jpg",
            "chemistry-printables/jpg/chemistry-printables-lab-report-template.jpg",
            "chemistry-printables/jpg/chemistry-printables-element-bingo-1.jpg",
            "chemistry-printables/jpg/chemistry-printables-chemical-bottle-labels.jpg")],
         "CHEMISTRY PRINTABLES", "Coloring pages, worksheets, flashcards, certificates & more", 4),
        ("bundle-kawaii", [dist / "8-stiker-kawaii" / f"{k}/jpg/{k}-set.jpg" for k in
                           ("kawaii-lab-stickers", "kawaii-lab-stickers-2", "kawaii-science-stickers",
                            "kawaii-molecule-stickers")],
         "KAWAII CHEMISTRY STICKERS", "77 cute die-cut stickers · lab, science & molecules", 2),
        ("bundle-posters-midnight", pick(dist, "3-poster-edukasi/chemistry-posters-midnight/jpg/*.jpg", 8),
         "MIDNIGHT POSTER COLLECTION", "Every chemistry poster in a deep purple dark theme", 4),
        ("bundle-element-tiles", [dist / "2-molekul-atom" / f"{k}/jpg/{k}-set.jpg" for k in
                                  ("element-tile-icons-2", "element-tile-icons-3", "element-tile-icons-4",
                                   "element-tile-dark-icons-1", "element-tile-dark-icons-2",
                                   "element-tile-dark-icons-3")],
         "ALL 118 ELEMENT TILES", "Colorful and dark versions · every element of the periodic table", 3),
        ("bundle-environment", [dist / f"{cp}chemistry-posters-{k}-dark.jpg" for k in
                                ("acid-rain", "greenhouse-effect", "ozone-layer-depletion", "water-treatment-process",
                                 "rusting-of-iron", "plastics-recycling-codes")],
         "ENVIRONMENTAL CHEMISTRY", "Acid rain, greenhouse effect, ozone, water treatment & more", 3),
    ]
    made = []
    for name, files, title, sub, cols in jobs:
        files = [f for f in files if Path(f).exists()]
        if not files:
            continue
        img = collage(files, title, sub, cols)
        path = out / f"{name}.jpg"
        img.save(path, quality=92)
        made.append(path)
        print("promo ->", path.relative_to(dist))
    if made:
        with zipfile.ZipFile(out.parent / "9-promosi.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for p in made:
                z.write(p, p.relative_to(dist))


if __name__ == "__main__":
    main()
