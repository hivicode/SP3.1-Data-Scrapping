import requests
import fungsi
from bs4 import BeautifulSoup

# def main_scrapper(url, directory, filename):
#     fungsi.create_directory(directory)
#     source_code = requests.get(url)
#     source_text = source_code.text
#     with open(directory + "/" + filename, "w") as file:
#         file.write(source_text)

# main_scrapper("https://www.detik.com/", "hasil", "hasil.html")

def main_scrapper(url, directory):
    fungsi.create_directory(directory)
    source_code = requests.get(url)
    source_text = source_code.text
    soup = BeautifulSoup(source_text, "html.parser")
    print(soup.findAll("div",{"id":"newsfeed_recommendation_wp"}))

if __name__ == "__main__":
    main_scrapper("https://www.detik.com/", "hasil")


