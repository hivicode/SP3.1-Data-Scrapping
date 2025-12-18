## Pertemuan 7

Melanjutkan proses scraping dengan mengunjungi setiap URL artikel dari daftar pada `hasil/articlestitles.txt`, lalu mengambil isi lengkap artikel dan menyimpannya ke `hasil/detail.doc`.

### Tujuan
- Membaca daftar URL dan judul artikel yang sudah dikumpulkan sebelumnya.
- Mengunjungi setiap halaman artikel dan mengekstrak isi utama artikel.
- Menambahkan hasil ekstraksi ke berkas keluaran untuk analisis lebih lanjut.

### Skrip Utama
- `get_details.py`: 
  - Menjalankan scraping listing (jika diperlukan), menulis URL/Judul ke `hasil/articlestitles.txt`.
  - Mengunjungi setiap URL artikel dan mengekstrak isi artikel.
  - Menyimpan konten artikel ke `hasil/detail.doc`.
- `fungsi.py`: Utilitas untuk pembuatan direktori dan operasi file.

### Dependensi
- Python 3.8+ (direkomendasikan 3.12+)
- `requests`
- `beautifulsoup4`

Instalasi dependensi:
```bash
pip install requests beautifulsoup4
```

### Alur Singkat
1. Pastikan `hasil/articlestitles.txt` tersedia (hasil dari Pertemuan 6).
2. Untuk setiap URL pada berkas tersebut, kirim request dan ambil HTML artikel.
3. Parse HTML untuk menemukan elemen isi artikel (judul, paragraf utama, dsb.).
4. Tulis hasil ekstraksi ke `hasil/detail.doc` (append) beserta pemisah yang jelas antar artikel.

### Cara Menjalankan
```bash
python3 get_details.py
```

### Keluaran
- `hasil/articlestitles.txt` (daftar URL dan judul artikel).
- `hasil/detail.doc` (kumpulan isi artikel).

### Catatan
- Selector elemen isi artikel dapat berubah mengikuti struktur situs; sesuaikan bila diperlukan.
- Gunakan penundaan antar permintaan bila scraping dalam jumlah besar.
