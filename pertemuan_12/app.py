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
    for item in items:
        link_tag = item.find("a")
        img_tag = link_tag.find("img") if link_tag else None
        title = img_tag.get("title") if img_tag else None
        img_src = img_tag.get("src") if img_tag else None

        date_tag = item.find("div", {"class": "media__date"})
        date_span = date_tag.find("span") if date_tag else None
        date_title = date_span.get("title") if date_span else None

        results.append(
            {
                "title": title,
                "img": img_src,
                "date": date_title,
            }
        )

    return results

@app.route("/")
def index():
    return render_template("index.html", items=None, page_title="Beranda")

@app.route("/detik-populer")
def detik_populer():
    items = fetch_detik_populer()
    return render_template("index.html", items=items, page_title="Detik Populer")

if __name__ == "__main__":
    app.run(debug=True)
