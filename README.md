# Vector-Kimia-Aset

Aset vektor microstock bertema kimia yang dibuat sepenuhnya lewat kode
(SVG digambar dari `src/`), lalu diekspor ke format yang diminta situs microstock.

## Set yang tersedia

Setiap baris di bawah menjadi satu ZIP siap unggah (226 aset total).

| Set | Isi |
|-----|-----|
| `lab-line-icons` | 20 ikon alat lab gaya garis + lembar set |
| `lab-flat-icons` | 20 ikon alat lab semi-flat berwarna (dua tone, kilau kaca, bayangan) + lembar set |
| `lab-flat-glyph-icons` | versi glyph (solid gelap) dari set di atas |
| `lab-flat-patterns` | 3 pola seamless dari ikon alat lab |
| `lab2-flat-icons` | 20 alat & perlengkapan lab jilid 2 (botol reagen, kondensor, sentrifus, jas lab, APD, dll.) |
| `lab2-flat-glyph-icons` | versi glyph jilid 2 |
| `lab2-flat-patterns` | 2 pola seamless jilid 2 |
| `molecule-icons` | 20 model molekul bola-dan-batang (H2O, CO2, CH4, benzena, NaCl, H2SO4, dll.) |
| `molecule-glyph-icons` | versi glyph model molekul |
| `molecule-patterns` | 3 pola seamless molekul |
| `bohr-atom-icons` | model atom Bohr unsur 1–20 |
| `bohr-atom-glyph-icons` | versi glyph model atom |
| `bohr-atom-patterns` | 2 pola seamless atom |
| `periodic-table-posters` | poster tabel periodik 118 unsur, tema terang & gelap |
| `hexagon-patterns` | 4 pola seamless sarang lebah / cincin benzena |

## Keluaran per file

- `eps/`: EPS PostScript level 2 (aman untuk syarat "EPS 10" Shutterstock / Adobe Stock)
- `jpg/`: pratinjau JPG berlatar putih (ikon 4000×4000 px, lembar set 5000×4000 px)
- `png/`: PNG transparan, ukuran sama (tidak dibuat untuk pola dan poster karena berlatar)
- `svg/`: vektor sumber
- `adobe_stock.csv` dan `shutterstock.csv`: judul dan keyword (bahasa Inggris) per file, sesuai format CSV unggahan masing-masing situs

## Cara pakai

**Lewat GitHub:** tab *Actions* → **Buat aset** → *Run workflow*. Setelah selesai, unduh
artefak `aset-microstock` (berisi ZIP siap unggah). Workflow juga jalan otomatis
setiap ada perubahan di `src/` atau `build.py` pada branch `main`.

**Lokal:**

```bash
pip install -r requirements.txt
python build.py              # opsi: --size 4000 --only molecule-icons hexagon-patterns
```

## Mengunggah

- **Shutterstock:** unggah file `.eps`, lalu impor `shutterstock.csv` di halaman metadata.
- **Adobe Stock:** unggah `.eps` bersama `.jpg` dengan nama yang sama (bisa dalam satu ZIP per aset), lalu impor `adobe_stock.csv` lewat *Upload CSV*.

## Catatan konten AI

Kode dan desain di repo ini dibuat dengan bantuan AI. Adobe Stock mewajibkan aset seperti ini
ditandai **"Created using generative AI tools"** saat diunggah. Kolom itu tidak ada di CSV, jadi
centang sendiri di portal. Situs lain punya aturan sendiri; cek aturan terbaru tiap situs sebelum mengunggah.

## Struktur

- `src/icons_*.py`, `src/molecules.py`, `src/atoms.py`: set ikon. Tiap ikon punya `id`, `title`,
  `keywords`, dan `body` (elemen SVG di grid 64×64). `build.py` menskalakan ikon agar mengisi bingkai,
  menyeragamkan tebal garis, lalu membuat varian glyph (`GLYPH = True`) dan pola seamless (`PATTERNS`).
- `src/periodic.py`, `src/hex_patterns.py`: aset utuh lewat fungsi `assets()`.
- `src/textpath.py`: teks diubah menjadi outline (wajib di microstock) memakai font Inter di `fonts/`
  (lisensi SIL OFL, lihat `fonts/LICENSE-Inter.txt`).
- Daftar modul yang dibangun ada di `MODULES` pada `build.py`.
