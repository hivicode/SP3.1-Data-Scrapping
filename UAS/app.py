from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def fetch_detik_populer():
    url = "https://www.detik.com/jatim/berita/indeks"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    populer_area = soup.find(attrs={"class": "grid-row list-content"})
    if not populer_area:
        return []

    items = populer_area.find_all(attrs={"class": "list-content__item"})
    results = []
    for idx, item in enumerate(items, start=1):
        media_image = item.find("div", {"class": "media__image"})
        img_tag = media_image.find("img") if media_image else None
        img_src = img_tag.get("src") if img_tag else None

        media_text = item.find("div", {"class": "media__text"})
        title_block = media_text.find("h3", {"class": "media__title"}) if media_text else None
        title_link = title_block.find("a") if title_block else None
        title = title_link.get_text(strip=True) if title_link else None

        date_block = item.find("div", {"class": "media__date"})
        date_span = date_block.find("span") if date_block else None
        date_title = date_span.get("title") if date_span else None
        countdown = date_span.get_text(strip=True) if date_span else None

        is_red = ((idx % 2 == 1) and idx not in {1, 9, 15}) or idx == 2 #ini buat nentuin warna index berapa aja yang harusnya merah pak

        results.append(
            {
                "number": idx,
                "title": title,
                "img": img_src,
                "countdown": countdown,
                "date": date_title,
                "is_red": is_red,
            }
        )

    return results

@app.route("/")
def index():
    return render_template("index.html", items=None, page_title="Beranda")

@app.route("/jatim/berita/indeks")
def detik_populer():
    items = fetch_detik_populer()
    return render_template("index.html", items=items, page_title="detikJatim")

if __name__ == "__main__":
    app.run(debug=True)
