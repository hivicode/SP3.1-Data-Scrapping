# Pertemuan 3 - BeautifulSoup HTML Parsing

Pertemuan ini membahas penggunaan BeautifulSoup untuk parsing dan manipulasi HTML content.

## 🏷️ Metode yang Dipelajari

### 1. Basic HTML Parsing
**Fungsi**: Parse HTML sederhana dan tampilkan struktur lengkap
```python
from bs4 import BeautifulSoup

html = "<div>Hello World</div><p>Hello World</p>"
soup = BeautifulSoup(html, "html.parser")
print(soup)
```

**Contoh Output**:
```html
<div>Hello World</div><p>Hello World</p>
```

### 2. Mengambil Text dari Tag Tertentu
**Fungsi**: Mengambil teks dari tag `<p>` pertama
```python
soup = BeautifulSoup(html, "html.parser")
print(soup.p.text)
```

**Contoh Output**:
```
Hello World
```

### 3. Parse HTML Multi-line
**Fungsi**: Parse HTML dengan multiple tags dan baris
```python
html = """<div>Hello World</div>
<p>Hello World</p>
<p>Morning</p>
<div> ini paragraf kedua </div>"""

soup = BeautifulSoup(html, "html.parser")
print(soup)
```

**Contoh Output**:
```html
<div>Hello World</div>
<p>Hello World</p>
<p>Morning</p>
<div> ini paragraf kedua </div>
```

### 4. Mencari Tag dengan Class
**Fungsi**: Mencari semua div dengan class "bold"
```python
html = """<div>Hello World</div>
<p>Hello World</p>
<p>Morning</p>
<div class="bold"> ini paragraf kedua </div>"""

soup = BeautifulSoup(html, "html.parser")
print(soup.findAll("div",{"class":"bold"}))
```

**Contoh Output**:
```html
[<div class="bold"> ini paragraf kedua </div>]
```

### 5. Mencari Tag dengan ID dan Class
**Fungsi**: Mencari div dengan ID "d2" dan mengambil tag `<p>` di dalamnya
```python
html = """
<div id="d1" class="wide">
    <p id="p1"> ini kalimat pertama </p>
    <img src=""/>
    <a id="a1"></a>
</div>
<div id="d2" class="small">
    <p id="p2"> ini kalimat kedua </p>
    <img src=""/>
    <a id="a2"></a>
</div>"""

soup = BeautifulSoup(html, "html.parser")
print(soup.findAll("div",{"id":"d2"})[0].p)
```

**Contoh Output**:
```html
<p id="p2"> ini kalimat kedua </p>
```

### 6. Navigasi HTML Nested Structure
**Fungsi**: Mengakses elemen dalam struktur HTML bertingkat
```python
html = """
<div id="d1" class="wide">
    <p id="p1"> this is a p</p>
    <img src=""/>
    <a id="a1"></a>
</div>
<div id="d1" class="small">
    <p id="p1"> this is a p </p>
    <div><p>KO</p></div>
    <img src=""/>
    <a id="a1"></a>
</div>"""

soup = BeautifulSoup(html, "html.parser")
print(soup.findAll("div",{"id":"d1"})[1].div.p.text)
```

**Contoh Output**:
```
KO
```

### 7. Mengambil Elemen dengan Multiple Selector
**Fungsi**: Mencari div dengan ID dan class spesifik
```python
print(soup.findAll("div",{"id":"d1", "class":"small"})[0].div.p.text)
print(soup.findAll("div",{"class":"small"})[0].div.p.text)
```

**Contoh Output**:
```
KO
KO
```

### 8. Iterasi dan Filter Elemen
**Fungsi**: Mengambil elemen dengan index genap (div2, div4, div6, div8, div10)
```python
html = """
<div>div1</div>
<div>div2</div>
<div>div3</div>
<div>div4</div>
<div>div5</div>
<div>div6</div>
<div>div7</div>
<div>div8</div>
<div>div9</div>
<div>div10</div>"""

soup = BeautifulSoup(html, "html.parser")
divs = soup.findAll("div")
for i, div in enumerate(divs):
    if (i+1) % 2 == 0:
        print(div.text)
```

**Contoh Output**:
```
div2
div4
div6
div8
div10
```

### 9. Alternatif Methods untuk Mengambil Elemen Genap
**Fungsi**: Menggunakan slicing untuk mengambil elemen dengan index genap
```python
# Method 1: Manual index selection
divs = soup.findAll("div")
list = [1, 3, 5, 7, 9]
for i in list:
    print(divs[i].text)

# Method 2: Slicing
divs = soup.findAll("div")[1::2]
for div in divs:
    print(div.text)
```

**Contoh Output**:
```
div2
div4
div6
div8
div10
```

## 📦 Dependencies

Pastikan untuk menginstall BeautifulSoup4:
```bash
pip install beautifulsoup4
```

## 📝 Cara Menjalankan

1. Install BeautifulSoup4: `pip install beautifulsoup4`
2. Uncomment bagian kode yang ingin dijalankan di `pertemuan_3.py`
3. Jalankan file dengan: `python pertemuan_3.py`
4. Perhatikan output HTML parsing di console

## 🔍 Tips

- Gunakan `soup.prettify()` untuk format HTML yang lebih rapi
- `findAll()` mengembalikan list, gunakan index `[0]` untuk elemen pertama
- Kombinasi selector seperti `{"id":"d1", "class":"small"}` untuk pencarian lebih spesifik
- `.text` untuk mengambil teks tanpa tag HTML
