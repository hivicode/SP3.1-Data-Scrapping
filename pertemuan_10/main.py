from selenium import webdriver
from bs4 import BeautifulSoup
import fungsi
import requests
import os

def main_scraper(url):
    # headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36'}
    driver = webdriver.Chrome()
    # driver.set_page_load_timeout(5000)
    full_url = f"{url}"
    driver.get(full_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    hasil = soup.find_all("div", {'class':'latest--news mt2 clearfix'})
    hasil_parsing = []

    for i in range(len(hasil)):
        cards = hasil[i].find_all("div", {'class':'article__list clearfix'})
    
        for card in cards:
            Card = card.find("div", {'class':'article__subtitle article__subtitle--inline'})
            Judul = card.find("a", {'class':'article__link'})
            
            if Card and Judul:
                card_text = "Card : " + Card.text.strip()
                judul_text = "Judul : " + Judul.text.strip()
                separator = "====================================="
                
                print(card_text)
                print(judul_text)
                print(separator)
             
                hasil_parsing.append(card_text)
                hasil_parsing.append(judul_text)
                hasil_parsing.append(separator)

    # Simpan hasil parsing ke file txt
    fungsi.create_directory('11_December/hasil')
    file_path = os.path.join('11_December/hasil', 'kompasparser.txt')
    
    # Hapus file lama jika ada, lalu tulis hasil baru
    if fungsi.does_file_exist(file_path):
        fungsi.remove_file(file_path)
    
    # Tulis semua hasil parsing ke file
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in hasil_parsing:
            file.write(line + '\n')
    #print(html)

main_scraper("https://tekno.kompas.com/gadget")