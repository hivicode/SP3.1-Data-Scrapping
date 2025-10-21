# SP3.1 Data Scraping

Repository ini berisi materi pembelajaran Data Scraping dengan Python.

## 📚 Struktur Materi

### [Pertemuan 2 - File Operations](./pertemuan_2/)
Mempelajari operasi-operasi dasar file dan directory dalam Python:
- Membuat dan mengelola folder
- Operasi file (create, read, write, delete)
- Validasi file dan directory

### [Pertemuan 3 - BeautifulSoup HTML Parsing](./pertemuan_3/)
Mempelajari penggunaan BeautifulSoup untuk parsing HTML:
- Basic HTML parsing
- Navigasi struktur HTML
- Selektor dan filter elemen
- Manipulasi konten HTML

### [Pertemuan 4 - Web Scraping dengan Requests](./pertemuan_4/)
Mempelajari penggunaan library Requests untuk HTTP request dan web scraping:
- HTTP GET request
- Response properties (status code, headers, encoding)
- Menyimpan HTML ke file
- Kombinasi Requests + BeautifulSoup

### [Pertemuan 5 - Advanced Web Scraping dengan Multiclass Selectors](./pertemuan_5/)
Mempelajari teknik lanjutan dalam web scraping:
- Multiclass selectors untuk mencari elemen dengan multiple class
- Advanced HTML parsing dengan nested selectors
- Kombinasi Requests + BeautifulSoup untuk scraping real website
- Menyimpan hasil scraping ke file

### [Pertemuan 6 - AJAX dan Web Development](./pertemuan_6/)
Mempelajari pengembangan web dengan AJAX dan JavaScript:
- AJAX dengan vanilla JavaScript dan jQuery
- Cascading dropdown dengan data JSON
- Form validation dan user interaction
- **Kalkulator Biaya Kirim Paket** - Aplikasi studi kasus dengan:
  - Form input untuk nomor resi, berat barang, kota asal, dan tujuan
  - Dropdown bertingkat untuk pemilihan kota
  - Perhitungan otomatis biaya berdasarkan berat dan jarak
  - Tabel referensi harga berat dan jarak

## 🚀 Quick Start

1. Clone repository ini
2. Install dependencies:
   ```bash
   pip install beautifulsoup4 requests
   ```
3. Masuk ke folder pertemuan yang diinginkan
4. Jalankan file Python yang ada
5. Baca README.md di setiap folder untuk penjelasan detail

## 📁 Struktur Folder

```
SP3.1 Data Scrapping/
├── README.md (file ini)
├── pertemuan_2/
│   ├── pertemuan_2.py
│   └── README.md
├── pertemuan_3/
│   ├── pertemuan_3.py
│   └── README.md
├── pertemuan_4/
│   ├── pertemuan_4.py
│   ├── tes_1.py
│   ├── fungsi.py
│   └── README.md
├── pertemuan_5/
│   ├── 1_multiclass.py
│   ├── 2_contoh_multiclass.py
│   ├── 3_ambil_judul.py
│   ├── fungsi.py
│   └── README.md
└── pertemuan_6/
    ├── index.html (AJAX dengan vanilla JavaScript)
    ├── index1.html (AJAX dengan jQuery)
    ├── script.js (JavaScript untuk AJAX)
    ├── data.json (Data mahasiswa)
    ├── select.html (Cascading dropdown)
    ├── data-lokasi.js (JavaScript untuk dropdown)
    └── tugas/
        ├── shipping-calculator.html (Kalkulator biaya kirim)
        ├── shipping-calculator.js (Logika perhitungan)
        └── kota.xml (Data kota)
```

## 🔧 Requirements

- Python 3.6+
- beautifulsoup4
- requests
- os (built-in)

### Untuk Pertemuan 6 (Web Development):
- Web browser modern
- Local web server (optional, untuk AJAX)
- jQuery 3.6.0+ (untuk contoh AJAX dengan jQuery)

## 📖 Cara Menggunakan

Setiap folder pertemuan memiliki:
- File Python dengan contoh kode
- README.md dengan penjelasan detail setiap metode
- Contoh output untuk setiap fungsi

Baca README.md di setiap folder untuk penjelasan lengkap dan contoh output.
