from bs4 import BeautifulSoup
import os

# 1. Basic HTML Parsing
html = "<div>Hello World</div><p>Hello World</p>"
soup = BeautifulSoup(html, "html.parser")
print("1. Basic HTML Parsing:")
print(soup)
print()

# 2. Mengambil Text dari Tag
soup = BeautifulSoup(html, "html.parser")
print("2. Mengambil Text dari Tag p:")
print(soup.p.text)
print()

# 3. Parse HTML Multi-line
html3 = """<div>Hello World</div>
<p>Hello World</p>
<p>Morning</p>
<div> ini paragraf kedua </div>"""

soup = BeautifulSoup(html3, "html.parser")
print("3. Parse HTML Multi-line:")
print(soup)
print()

# 4. Mencari Tag dengan Class
html4 = """<div>Hello World</div>
<p>Hello World</p>
<p>Morning</p>
<div class="bold"> ini paragraf kedua </div>"""

soup = BeautifulSoup(html4, "html.parser")
print("4. Mencari Tag dengan Class 'bold':")
print(soup.findAll("div",{"class":"bold"}))
print()

# 5. Mencari Tag dengan ID
html5 = """
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

soup = BeautifulSoup(html5, "html.parser")
print("5. Mencari Tag dengan ID 'd2':")
print(soup.findAll("div",{"id":"d2"})[0].p)
print()

# 6. Navigasi HTML Nested Structure
html6 = """
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

soup = BeautifulSoup(html6, "html.parser")
print("6. Navigasi HTML Nested Structure:")
print(soup.findAll("div",{"id":"d1"})[1].div.p.text)
print(soup.findAll("div",{"id":"d1", "class":"small"})[0].div.p.text)
print(soup.findAll("div",{"class":"small"})[0].div.p.text)
print()

# 7. Iterasi dan Filter Elemen
html7 = """
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

soup = BeautifulSoup(html7, "html.parser")
print("7. Mengambil elemen dengan index genap (div2, div4, div6, div8, div10):")
divs = soup.findAll("div")
for i, div in enumerate(divs):
    if (i+1) % 2 == 0:
        print(div.text)
print()

# 8. Alternatif: Menggunakan slicing
print("8. Alternatif dengan slicing [1::2]:")
divs = soup.findAll("div")[1::2]
for div in divs:
    print(div.text)
print()

# 9. Alternatif: Menggunakan list index
print("9. Alternatif dengan list index:")
divs = soup.findAll("div")
indices = [1, 3, 5, 7, 9]
for i in indices:
    print(divs[i].text)