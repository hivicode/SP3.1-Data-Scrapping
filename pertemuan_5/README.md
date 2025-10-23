# Pertemuan 5 - Advanced Web Scraping dengan Multiclass Selectors

Pertemuan ini mempelajari teknik lanjutan dalam web scraping menggunakan BeautifulSoup dengan fokus pada:
- Multiclass selectors untuk mencari elemen dengan multiple class
- Advanced HTML parsing dengan nested selectors
- Kombinasi Requests + BeautifulSoup untuk scraping real website
- Menyimpan hasil scraping ke file

## File Structure

```
pertemuan_5/
├── README.md (file ini)
├── 1_multiclass.py (contoh dasar multiclass selector)
├── 2_contoh_multiclass.py (implementasi multiclass pada website nyata)
├── 3_ambil_judul.py (scraping dengan nested selectors dan file output)
└── fungsi.py (utility functions untuk file operations)
```

## Requirements

- Python 3.6+
- beautifulsoup4
- requests
- os (built-in)

## Penjelasan File

### 1_multiclass.py
**Tujuan**: Demonstrasi dasar penggunaan multiclass selector

**Fitur**:
- Mencari semua tag dengan class `class1` dan `class2`
- Menggunakan `findAll(True, {"class":["class1", "class2"]})`
- Contoh HTML parsing sederhana

**Output**:
```
[<div class="class1"></div>, <div class="class2"></div>]
```

### 2_contoh_multiclass.py
**Tujuan**: Implementasi multiclass selector pada website nyata (Kompas Tekno)

**Fitur**:
- Scraping artikel dari https://tekno.kompas.com/gadget
- Menggunakan multiple selector strategies:
  - `find_all("h3", {"class":["article__title article__title--medium"]})`
  - `find_all(True,{"class":["article__box", "article__title"]})`
- Menampilkan URL dan title artikel
- Menggunakan utility functions dari `fungsi.py`

**Output**:
```
URL: https://tekno.kompas.com/read/2024/...
Title: Judul Artikel 1

URL: https://tekno.kompas.com/read/2024/...
Title: Judul Artikel 2
```

### 3_ambil_judul.py
**Tujuan**: Advanced scraping dengan nested selectors dan file output

**Fitur**:
- Scraping dengan nested HTML structure navigation
- Menggunakan chain of selectors untuk mencapai target elements
- Menyimpan hasil ke file `articles.txt` di folder `hasil`
- Kombinasi console output dan file output

**Struktur HTML yang di-scrape**:
```html
<div class="row mt3 col-offset-fluid clearfix">
  <div class="col-bs10-7">
    <div class="row article__wrap__grid--flex col-offset-fluid mt2">
      <div class="article__box">
        <h3>Title</h3>
      </div>
    </div>
  </div>
</div>
```

**Output**:
- Console: URL dan title artikel
- File: `hasil/articles.txt` berisi data yang sama

### fungsi.py
**Tujuan**: Utility functions untuk operasi file dan directory

**Functions**:
- `create_directory(directory)`: Membuat directory jika belum ada
- `write_to_file(path, data)`: Menulis data ke file dengan append mode

## Cara Menjalankan

1. **Install dependencies**:
   ```bash
   pip install beautifulsoup4 requests
   ```

2. **Jalankan file sesuai kebutuhan**:
   ```bash
   # Contoh dasar multiclass
   python 1_multiclass.py
   
   # Scraping website nyata
   python 2_contoh_multiclass.py
   
   # Advanced scraping dengan file output
   python 3_ambil_judul.py
   ```

3. **Hasil akan tersimpan di**:
   - Console output untuk semua file
   - File `hasil/articles.txt` untuk file `3_ambil_judul.py`

## Konsep Penting

### Multiclass Selectors
```python
# Mencari elemen dengan class tertentu
soup.find_all("div", {"class": "single-class"})

# Mencari elemen dengan multiple classes
soup.find_all("div", {"class": ["class1", "class2"]})

# Mencari semua tag dengan class tertentu
soup.find_all(True, {"class": ["class1", "class2"]})
```

### Nested Selectors
```python
# Navigasi struktur HTML bertingkat
articles = soup.find("div", {"class": "parent"})
articles2 = articles.find("div", {"class": "child"})
articles3 = articles2.find_all("div", {"class": "grandchild"})
```

### File Operations
```python
# Membuat directory
if not os.path.exists(directory):
    os.mkdir(directory)

# Menulis ke file dengan append
with open(path, 'a') as file:
    file.write(data + '\n')
```

## Catatan Penting

1. **Rate Limiting**: Website mungkin memiliki rate limiting, gunakan `time.sleep()` jika diperlukan
2. **User Agent**: Beberapa website memblokir request tanpa user agent
3. **Legal Considerations**: Pastikan scraping sesuai dengan terms of service website
4. **Error Handling**: Tambahkan try-catch untuk handling error network

## 🔗 Referensi

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://requests.readthedocs.io/)
- [Python os Module](https://docs.python.org/3/library/os.html)
