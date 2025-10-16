#mencari semua tag dengan class class1 dan class2
from bs4 import BeautifulSoup
soup = BeautifulSoup('<html><body><div class="class1"></div> <div class="class2"></div><div class="class3"></div></body></html>')
soup.findAll(True, {"class":["class1", "class2"]})