## Pertemuan 6

Mengambil daftar artikel dari halaman Kompas Tekno (kategori Gadget), lalu menyimpan URL dan judul artikel ke berkas `hasil/articlestitles.txt`.

### Tujuan
- Mengirim HTTP request ke halaman listing.
- Melakukan parsing HTML untuk menemukan elemen berisi judul dan tautan artikel.
- Menyimpan hasil (URL dan Judul) ke berkas teks untuk dipakai di pertemuan selanjutnya.

### Skrip Utama
- `3_ambil_judul.py`: Mengambil halaman listing dan menambahkan baris URL dan Judul ke berkas output.
- `fungsi.py`: Utilitas sederhana untuk pembuatan direktori dan operasi file.

### Dependensi
- Python 3.8+ (direkomendasikan 3.12+)
- `requests`
- `beautifulsoup4`

Instalasi dependensi:
```bash
pip install requests beautifulsoup4
```

### Alur Singkat
1. Buat direktori `hasil` jika belum ada.
2. Ambil HTML halaman listing menggunakan `requests`.
3. Parse HTML dengan `BeautifulSoup` untuk menemukan elemen judul artikel.
4. Tulis setiap pasangan URL dan Judul ke `hasil/articlestitles.txt` (append).

### Cara Menjalankan
```bash
python3 3_ambil_judul.py
```

### Keluaran
- `hasil/articlestitles.txt` berisi daftar baris dengan format: URL dan Judul artikel.

### Catatan
- Struktur HTML situs dapat berubah; sesuaikan selector bila elemen target tidak ditemukan.
- Jalankan skrip secara wajar agar tidak membebani server.
