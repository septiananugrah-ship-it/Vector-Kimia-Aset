# Vector-Kimia-Aset

Aset vektor microstock bertema kimia yang dibuat sepenuhnya lewat kode
(SVG digambar dari `src/`), lalu diekspor ke format yang diminta situs microstock.

## Set yang tersedia

| Set | Isi |
|-----|-----|
| `lab-line-icons` | 20 ikon alat lab gaya garis + 1 lembar set berisi semuanya |
| `lab-flat-icons` | 20 ikon alat lab gaya semi-flat berwarna (dua tone, kilau kaca, bayangan) + 1 lembar set |

## Keluaran per file

- `eps/`: EPS PostScript level 2 (aman untuk syarat "EPS 10" Shutterstock / Adobe Stock)
- `jpg/`: pratinjau JPG berlatar putih (ikon 4000×4000 px, lembar set 5000×4000 px)
- `png/`: PNG transparan, ukuran sama
- `svg/`: vektor sumber
- `adobe_stock.csv` dan `shutterstock.csv`: judul dan keyword (bahasa Inggris) per file, sesuai format CSV unggahan masing-masing situs

## Cara pakai

**Lewat GitHub:** tab *Actions* → **Buat aset** → *Run workflow*. Setelah selesai, unduh
artefak `aset-microstock` (berisi ZIP siap unggah). Workflow juga jalan otomatis
setiap ada perubahan di `src/` atau `build.py` pada branch `main`.

**Lokal:**

```bash
pip install -r requirements.txt
python build.py              # opsi: --size 4000 --color 1E2A3A
```

## Mengunggah

- **Shutterstock:** unggah file `.eps`, lalu impor `shutterstock.csv` di halaman metadata.
- **Adobe Stock:** unggah `.eps` bersama `.jpg` dengan nama yang sama (bisa dalam satu ZIP per aset), lalu impor `adobe_stock.csv` lewat *Upload CSV*.

## Catatan konten AI

Kode dan desain di repo ini dibuat dengan bantuan AI. Adobe Stock mewajibkan aset seperti ini
ditandai **"Created using generative AI tools"** saat diunggah. Kolom itu tidak ada di CSV, jadi
centang sendiri di portal. Situs lain punya aturan sendiri; cek aturan terbaru tiap situs sebelum mengunggah.

## Menambah ikon

Tambahkan entri ke `ICONS` di `src/icons_lab.py` (atau `src/icons_lab_flat.py`): `id`, `title`, `keywords`, dan `body`
(elemen SVG di grid 64×64, tanpa atribut gaya). Gaya garis diterapkan seragam oleh `build.py`.
