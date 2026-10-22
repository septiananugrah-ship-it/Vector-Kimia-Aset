#!/usr/bin/env python3
"""Paket jualan siap unggah ke Lynk.id / Karyakarsa / Gumroad (versi Bahasa Indonesia).

Membuat dist/10-paket-jualan/:
  1-mega-paket-poster-kimia/   PDF A4 97 poster (tema terang untuk cetak + tema navy untuk layar)
  2-paket-printable-kimia/     PDF A4 lembar mewarnai + lembar kerja, kartu, sertifikat, dll.
  3-gratis-5-poster/           PDF sampel gratis untuk menarik pengikut
  sampul/                      gambar sampul produk 1080x1080 + pratinjau halaman
Teks deskripsi produk dan rencana Instagram ada di PANDUAN-LYNK-IG.md.
"""
import io
import sys
from pathlib import Path

import cairosvg
from PIL import Image, ImageDraw, ImageFilter
from pypdf import PdfWriter

ROOT = Path(__file__).parent
sys.path.insert(0, str(ROOT / "src"))
import coloring  # noqa: E402
import poster_kit  # noqa: E402
import posters  # noqa: E402
import printables  # noqa: E402
from poster_kit import THEMES, doc  # noqa: E402
from textpath import text, width  # noqa: E402

A4 = (595.28, 841.89)  # pt
NAVY, GOLD = "#16213A", "#FFC845"
SAMPLE = ["ph-scale", "states-of-matter", "lab-equipment", "bohr-atoms", "reaction-types"]


def _inner(svg):
    """Ambil viewBox dan isi dari dokumen SVG buatan modul."""
    head, body = svg.split(">", 1)
    vb = head.split('viewBox="')[1].split('"')[0]
    return [float(v) for v in vb.split()][2:], body.rsplit("</svg>", 1)[0]


def a4_page(svg, bg="#FFFFFF", margin=24):
    """Satu halaman PDF A4 (tegak/mendatar mengikuti bentuk gambar), gambar di tengah, tetap vektor."""
    (w, h), body = _inner(svg)
    pw, ph = A4 if h >= w else A4[::-1]
    k = min((pw - 2 * margin) / w, (ph - 2 * margin) / h)
    x, y = (pw - w * k) / 2, (ph - h * k) / 2
    page = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{pw}pt" height="{ph}pt" viewBox="0 0 {pw} {ph}">'
            f'<rect width="{pw}" height="{ph}" fill="{bg}"/>'
            f'<svg x="{x:.2f}" y="{y:.2f}" width="{w * k:.2f}" height="{h * k:.2f}" viewBox="0 0 {w} {h}">{body}</svg>'
            '</svg>')
    return cairosvg.svg2pdf(bytestring=page.encode())


def cover_page(title, sub, lines):
    pw, ph = A4
    s = [f'<rect width="{pw}" height="{ph}" fill="{NAVY}"/>',
         f'<rect x="40" y="40" width="{pw - 80}" height="{ph - 80}" rx="18" fill="none" stroke="{GOLD}" stroke-width="2"/>']
    y = 300
    for t in title:
        size = min(40, 40 * (pw - 120) / max(width(t, 40), 1))
        s.append(text(t, pw / 2, y, size, "#FFFFFF"))
        y += size * 1.25
    s.append(text(sub, pw / 2, y + 20, 17, GOLD, "SemiBold"))
    for i, ln in enumerate(lines):
        s.append(text(ln, pw / 2, 600 + i * 26, 13.5, "#AEB9C9", "SemiBold"))
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{pw}pt" height="{ph}pt" viewBox="0 0 {pw} {ph}">'
           + "".join(s) + "</svg>")
    return cairosvg.svg2pdf(bytestring=svg.encode())


def write_pdf(path, pages):
    out = PdfWriter()
    for p in pages:
        out.append(io.BytesIO(p))
    out.compress_identical_objects()
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        out.write(f)
    print(f"{path.relative_to(ROOT)}  {len(pages)} hal  {path.stat().st_size / 1e6:.1f} MB")


def thumb(svg, px=900):
    (w, h), _ = _inner(svg)
    png = cairosvg.svg2png(bytestring=svg.encode(), output_width=px if w >= h else int(px * w / h))
    return Image.open(io.BytesIO(png)).convert("RGB")


def shadowed(img, box):
    k = min(box / img.width, box / img.height)
    img = img.resize((int(img.width * k), int(img.height * k)), Image.LANCZOS)
    pad = 24
    sh = Image.new("RGBA", (img.width + 2 * pad, img.height + 2 * pad), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([pad + 6, pad + 10, pad + img.width + 6, pad + img.height + 10], 8,
                                         fill=(0, 0, 0, 160))
    sh = sh.filter(ImageFilter.GaussianBlur(10))
    sh.paste(img, (pad, pad))
    return sh


def cover_image(path, thumbs, title, sub, badge):
    """Sampul produk persegi 1080x1080: kolase pratinjau + judul + label harga/jumlah."""
    S = 1080
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{S}" height="{S}" viewBox="0 0 {S} {S}">'
           f'<rect width="{S}" height="{S}" fill="{NAVY}"/><rect y="760" width="{S}" height="320" fill="#0F1830"/>'
           + text(title, S / 2, 868, min(66, 66 * 980 / width(title, 66)), "#FFFFFF")
           + text(sub, S / 2, 930, min(30, 30 * 980 / width(sub, 30, "SemiBold")), GOLD, "SemiBold")
           + f'<rect x="{S / 2 - 170}" y="970" width="340" height="62" rx="31" fill="{GOLD}"/>'
           + text(badge, S / 2, 1012, 28, NAVY) + "</svg>")
    base = Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode()))).convert("RGB")
    n = len(thumbs)
    cols = 3 if n >= 3 else n
    cell = S // cols
    rows = -(-n // cols)
    for i, im in enumerate(thumbs):
        tile = shadowed(im, cell - 50 if rows == 1 else (740 // rows) - 20)
        cx = (i % cols) * cell + cell // 2
        cy = 30 + (i // cols) * (730 // rows) + (730 // rows) // 2
        base.paste(tile, (cx - tile.width // 2, cy - tile.height // 2), tile)
    path.parent.mkdir(parents=True, exist_ok=True)
    base.save(path, quality=92)
    print(path.relative_to(ROOT))


def main():
    out = ROOT / "dist" / "10-paket-jualan"
    poster_kit.set_lang("id")
    light, dark = THEMES["light"], THEMES["dark"]
    light_svgs, dark_svgs = {}, {}
    for key, fn, *_ in posters.POSTERS:
        W, H, inner = fn(light)
        light_svgs[key] = doc(W, H, light, inner)
        W, H, inner = fn(dark)
        dark_svgs[key] = doc(W, H, dark, inner)
    n = len(light_svgs)

    # 1. Mega paket poster
    p1 = out / "1-mega-paket-poster-kimia"
    info = ["Ukuran A4, vektor tajam, bisa dicetak sampai A2", f"{n} topik kimia SMA dalam Bahasa Indonesia",
            "Untuk penggunaan pribadi dan kelas. Dilarang dijual ulang."]
    write_pdf(p1 / "Poster-Kimia-Tema-Terang-(untuk-cetak).pdf",
              [cover_page(["MEGA PAKET", "POSTER KIMIA"], f"{n} poster · tema terang (hemat tinta)", info)]
              + [a4_page(s, light["bg"]) for s in light_svgs.values()])
    write_pdf(p1 / "Poster-Kimia-Tema-Gelap-(untuk-layar-dan-proyektor).pdf",
              [cover_page(["MEGA PAKET", "POSTER KIMIA"], f"{n} poster · tema navy gelap", info)]
              + [a4_page(s, dark["bg"]) for s in dark_svgs.values()])

    # 2. Paket printable
    pages = [a["svg"] for _, a_ in coloring.assets() for a in a_ if a["name"].endswith("-indonesian")]
    pages += [a["svg"] for _, a_ in printables.assets() for a in a_ if a["name"].endswith("-indonesian")]
    poster_kit.set_lang("id")
    write_pdf(out / "2-paket-printable-kimia" / "Printable-Kimia-Bahasa-Indonesia.pdf",
              [cover_page(["PAKET PRINTABLE", "KIMIA"], f"{len(pages)} halaman siap cetak A4",
                          ["Lembar mewarnai, lembar kerja, kartu, sertifikat, dan lainnya",
                           "Cocok untuk guru, les privat, dan orang tua",
                           "Untuk penggunaan pribadi dan kelas. Dilarang dijual ulang."])]
              + [a4_page(s, margin=0) for s in pages])

    # 3. Sampel gratis
    write_pdf(out / "3-gratis-5-poster" / "GRATIS-5-Poster-Kimia.pdf",
              [cover_page(["5 POSTER KIMIA", "GRATIS"], "Contoh dari Mega Paket Poster Kimia",
                          [f"Versi lengkap berisi {n} poster: cek link di bio Instagram",
                           "Boleh dicetak dan dibagikan, tidak untuk dijual"])]
              + [a4_page(light_svgs[k], light["bg"]) for k in SAMPLE])

    # Sampul dan pratinjau
    sp = out / "sampul"
    keys = list(dark_svgs)
    pick = [keys[i] for i in range(0, n, max(1, n // 6))][:6]
    cover_image(sp / "sampul-1-mega-paket-poster.jpg", [thumb(dark_svgs[k]) for k in pick],
                "MEGA PAKET POSTER KIMIA", f"{n} poster · Bahasa Indonesia · PDF siap cetak", f"{n} POSTER")
    cover_image(sp / "sampul-2-printable.jpg", [thumb(s) for s in pages[::max(1, len(pages) // 6)][:6]],
                "PAKET PRINTABLE KIMIA", "Mewarnai, lembar kerja, kartu & sertifikat", f"{len(pages)} HALAMAN")
    cover_image(sp / "sampul-3-gratis.jpg", [thumb(light_svgs[k]) for k in SAMPLE[:3]],
                "5 POSTER KIMIA GRATIS", "Download lewat link di bio", "GRATIS")
    for i, k in enumerate(pick[:4], 1):
        thumb(dark_svgs[k], 1600).save(sp / f"pratinjau-poster-{i}.jpg", quality=90)
    poster_kit.set_lang("en")


if __name__ == "__main__":
    main()
