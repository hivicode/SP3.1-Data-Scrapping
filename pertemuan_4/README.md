# Pertemuan 4 - Web Scraping dengan Requests

Pertemuan ini membahas penggunaan library Requests untuk melakukan HTTP request dan scraping website.

## Metode yang Dipelajari

### 1. Import Library Requests
**Fungsi**: Mengimport library untuk melakukan HTTP request
```python
import requests
```

### 2. GET Request ke Website
**Fungsi**: Melakukan HTTP GET request ke URL
```python
result = requests.get("https://www.detik.com/")
print(result)
```

**Contoh Output**:
```
<Response [200]>
```

### 3. Response Encoding
**Fungsi**: Mendapatkan encoding dari response
```python
print(result.encoding)
```

**Contoh Output**:
```
utf-8
```

### 4. Response URL
**Fungsi**: Mendapatkan URL final setelah redirect (jika ada)
```python
print(result.url)
```

**Contoh Output**:
```
https://www.detik.com/
```

### 5. Response Elapsed Time
**Fungsi**: Mendapatkan waktu yang dibutuhkan untuk request
```python
print(result.elapsed)
```

**Contoh Output**:
```
0:00:00.523456
```

### 6. Response Status Code
**Fungsi**: Mendapatkan HTTP status code
```python
print(result.status_code)
```

**Contoh Output**:
```
200
```

**Status Code yang Umum**:
- `200`: OK (berhasil)
- `404`: Not Found (halaman tidak ditemukan)
- `500`: Internal Server Error
- `403`: Forbidden (akses ditolak)

### 7. Response Headers
**Fungsi**: Mendapatkan header spesifik dari response
```python
print(result.headers['Content-Type'])
```

**Contoh Output**:
```
text/html; charset=utf-8
```

### 8. Response History
**Fungsi**: Mendapatkan history redirect (jika ada)
```python
print(result.history)
```

**Contoh Output**:
```
[]
```

### 9. Response Text (HTML Content)
**Fungsi**: Mendapatkan konten HTML dari website
```python
print(result.text)
```

**Contoh Output**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>detikcom - Informasi Berita Terkini Hari Ini</title>
    ...
</head>
<body>
    ...
</body>
</html>
```

## File Pendukung

### fungsi.py
**Fungsi**: Module helper untuk membuat directory
```python
import os

def create_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)
```

**Contoh Penggunaan**:
```python
import fungsi
fungsi.create_directory("hasil")
```

### tes_1.py
**Fungsi**: Implementasi web scraper lengkap dengan BeautifulSoup

#### Method 1: Menyimpan HTML ke File
```python
def main_scrapper(url, directory, filename):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    with open(directory + "/" + filename, "w") as file:
        file.write(source_text)

main_scrapper("https://www.detik.com/", "hasil", "hasil.html")
```

**Contoh Output**:
```
File 'hasil/hasil.html' akan dibuat berisi konten HTML dari website
```

#### Method 2: Parsing HTML dengan BeautifulSoup
```python
def main_scrapper(url, directory):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    print(soup.findAll("div",{"id":"newsfeed_recommendation_wp"}))

main_scrapper("https://www.detik.com/", "hasil")
```

**Contoh Output**:
```html
[<div id="newsfeed_recommendation_wp">
    ... konten div dengan id tersebut ...
</div>]
```

## Dependencies

Install library yang diperlukan:
```bash
pip install requests beautifulsoup4
```

## Cara Menjalankan

### Menjalankan pertemuan_4.py
```bash
python pertemuan_4.py
```
Output akan menampilkan berbagai informasi tentang HTTP response.

### Menjalankan tes_1.py
```bash
python tes_1.py
```
Output akan melakukan scraping dan parsing HTML dari website.

## Konsep Penting

### HTTP Request Flow
1. **Request**: Kirim GET request ke URL
2. **Response**: Terima response dari server
3. **Parse**: Parse HTML dengan BeautifulSoup
4. **Extract**: Ekstrak data yang diinginkan

### Best Practices
- Selalu cek `status_code` sebelum parse HTML
- Gunakan `try-except` untuk handle error
- Respect website's `robots.txt`
- Jangan overload server dengan terlalu banyak request

## Tips

- Gunakan `result.text` untuk mendapatkan HTML content
- Kombinasikan dengan BeautifulSoup untuk parsing HTML
- Simpan hasil scraping ke file untuk analisis lebih lanjut
- Gunakan `result.status_code` untuk validasi request berhasil

## Struktur File yang Dibuat

```
hasil/
└── hasil.html (konten HTML dari website yang di-scrape)
```
