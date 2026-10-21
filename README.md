# Vector-Kimia-Aset

Aset vektor microstock bertema kimia yang dibuat sepenuhnya lewat kode
(SVG digambar dari `src/`), lalu diekspor ke format yang diminta situs microstock.

## Set yang tersedia

Total 288 aset dalam 18 ZIP, dipetakan ke 5 kategori. Daftar lengkap semua file ada di `dist/katalog.csv`.

### 1-alat-lab
| Set | Isi |
|-----|-----|
| `lab-line-icons` | 20 ikon alat lab gaya garis + lembar set |
| `lab-flat-icons` | 20 ikon alat lab semi-flat berwarna + lembar set |
| `lab-flat-glyph-icons` | versi glyph (solid gelap) |
| `lab2-flat-icons` | 20 alat & perlengkapan lab jilid 2 (botol reagen, kondensor, sentrifus, jas lab, APD, dll.) |
| `lab2-flat-glyph-icons` | versi glyph jilid 2 |

### 2-molekul-atom
| Set | Isi |
|-----|-----|
| `molecule-icons` | 20 model molekul bola-dan-batang (H2O, CO2, CH4, benzena, NaCl, H2SO4, dll.) |
| `molecule-glyph-icons` | versi glyph model molekul |
| `bohr-atom-icons` | model atom Bohr unsur 1–20 |
| `bohr-atom-glyph-icons` | versi glyph model atom |

### 3-poster-edukasi
| Set | Isi |
|-----|-----|
| `periodic-table-posters` | tabel periodik 118 unsur: lengkap (terang & gelap), hanya lambang, dan lembar kerja kosong; bahasa Inggris & Indonesia |
| `chemistry-posters` | 16 poster × 2 tema (gelap & terang): bagan 40 alat lab berlabel, molekul + rumus, atom Bohr, skala pH, wujud zat, jenis reaksi, gugus fungsi organik, deret alkana, struktur atom, jenis ikatan kimia, tata tertib keselamatan lab, tren periodik, konfigurasi elektron, indikator asam-basa, teknik pemisahan campuran, hukum gas |
| `chemistry-posters-indonesian` | 16 poster yang sama dalam Bahasa Indonesia |

### 4-pola-seamless
| Set | Isi |
|-----|-----|
| `lab-flat-patterns`, `lab2-flat-patterns` | pola alat lab (5) |
| `molecule-patterns`, `bohr-atom-patterns` | pola molekul & atom (5) |
| `hexagon-patterns` | pola sarang lebah / cincin benzena (4) |

### 5-latar-presentasi
| Set | Isi |
|-----|-----|
| `chemistry-backgrounds` | 11 latar presentasi/banner 16:9 dengan ruang kosong untuk teks (heksagon + molekul, orbit atom, alat lab, rumus kimia, ubin unsur) |

## Keluaran per file

- `eps/`: EPS PostScript level 2 (aman untuk syarat "EPS 10" Shutterstock / Adobe Stock)
- `jpg/`: pratinjau JPG berlatar putih (ikon 4000×4000 px, lembar set 5000×4000 px)
- `png/`: PNG transparan, ukuran sama (tidak dibuat untuk pola dan poster karena berlatar)
- `svg/`: vektor sumber
- `adobe_stock.csv` dan `shutterstock.csv`: judul dan keyword (bahasa Inggris) per file, sesuai format CSV unggahan masing-masing situs

## Cara pakai

**Lewat GitHub:** tab *Actions* → **Buat aset** → *Run workflow*. Setelah selesai, unduh
artefak per kategori (`1-alat-lab`, `2-molekul-atom`, `3-poster-edukasi`, `4-pola-seamless`,
`5-latar-presentasi`) dan `katalog`. Workflow juga jalan otomatis
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
- `src/periodic.py`, `src/posters.py`, `src/posters2.py`, `src/posters3.py`, `src/hex_patterns.py`, `src/backgrounds.py`: aset utuh
  lewat fungsi `assets()`. Teks poster diterjemahkan lewat kamus di `src/poster_i18n.py`.
- `src/render.py`: pembantu render ikon bersama; `category()` di `build.py` memetakan set ke folder kategori.
- `src/textpath.py`: teks diubah menjadi outline (wajib di microstock) memakai font Inter di `fonts/`
  (lisensi SIL OFL, lihat `fonts/LICENSE-Inter.txt`).
- Daftar modul yang dibangun ada di `MODULES` pada `build.py`.
