import requests
from bs4 import BeautifulSoup

html_doc = requests.get("https://www.detik.com/jatim/berita/indeks")

soup = BeautifulSoup(html_doc.text, 'html.parser')

populer_area = soup.find(attrs={'class': 'grid-row list-content'})

items = populer_area.findAll(attrs={'class': 'list-content__item'})
# titles = populer_area.findAll(attrs={'class': 'media__title'})
# text = populer_area.findAll(attrs={'class': 'media__text'})

for item in items:
    print(item.find('a').find('img')['src'])
    print(item.find('a').find('img')['title'])
    print(item.find('div', {'class': 'media__date'}).find('span')['title'])
    print("-" * 50)