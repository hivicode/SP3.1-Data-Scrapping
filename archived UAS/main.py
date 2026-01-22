import requests
from bs4 import BeautifulSoup

html_doc = requests.get("https://www.detik.com/jatim/berita/indeks")
soup = BeautifulSoup(html_doc.text, 'html.parser')
populer_area = soup.find(attrs={'class': 'grid-row list-content'})
items = populer_area.find_all(attrs={'class': 'list-content__item'})

for item in items:
    # media__image
    image = item.find('div', {'class': 'media__image'})
    image_src = image.find('img')['src']

    #media__title
    media_text = item.find('div', {'class': 'media__text'})
    title_block = media_text.find('h3', {'class': 'media__title'})
    title_link = title_block.find('a')
    title_link_href = title_link['href']
    title = title_link.get_text(strip=True)

    # media__date
    date_block = item.find('div', {'class': 'media__date'})
    date_span = date_block.find('span')
    date = date_span['title']
    countdown = date_span.get_text(strip=True)

    print(image_src)
    print(title)
    print(f"title_link_href: {title_link_href}")
    print(countdown)
    print(date)
    print("-" * 50)
