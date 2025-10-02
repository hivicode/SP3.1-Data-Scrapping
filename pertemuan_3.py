# #1
# from bs4 import BeautifulSoup
# import os

# html = "<div>Hello World</div><p>Hello World</p>"

# soup = BeautifulSoup(html, "html.parser")

# print(soup)


# #2
# from bs4 import BeautifulSoup
# import os

# html = "<div>Hello World</div><p>Hello World</p>"

# soup = BeautifulSoup(html, "html.parser")

# print(soup.p.text)


# #3
# from bs4 import BeautifulSoup   
# import os

# html = """<div>Hello World</div>
# <p>Hello World</p>
# <p>Morning</p>
# <div> ini paragraf kedua </div>  
# """

# soup = BeautifulSoup(html, "html.parser")

# print(soup)

# #print
# print(soup.div)
# print(soup.findAll("div"))
# print(soup.findAll("div")[1])

# #4
# from bs4 import BeautifulSoup   
# import os

# html = """<div>Hello World</div>
# <p>Hello World</p>
# <p>Morning</p>
# <div class="bold"> ini paragraf kedua </div>  
# """

# soup = BeautifulSoup(html, "html.parser")

# print(soup.findAll("div",{"class":"bold"}))
# # print(soup.findAll("p",{'id':'para'}))

# #5
# from bs4 import BeautifulSoup       
# import os


# html = """
#         <div id="d1" class="wide">
#             <p id="p1"> ini kalimat pertama </p>
#             <img src=""/>
#             <a id="a1"></a>
#         </div>
#         <div id="d2" class="small">
#             <p id="p2"> ini kalimat kedua </p>
#             <img src=""/>
#             <a id="a2"></a>
#         </div>
#         """

# soup = BeautifulSoup(html, "html.parser")

# print(soup.findAll("div",{"id":"d2"})[0].p)

# #6 test
# from bs4 import BeautifulSoup       
# import os


# html4 = """
#         <div id="d1" class="wide">
#             <p id="p1"> this is a p</p>
#             <img src=""/>
#             <a id="a1"></a>
#         </div>
#         <div id="d1" class="small">
#             <p id="p1"> this is a p </p>
#             <div><p>KO</p></div>
#             <img src=""/>
#             <a id="a1"></a>
#         </div>
#         """

# soup = BeautifulSoup(html4, "html.parser")

# print(soup.findAll("div",{"id":"d1"})[1].div.p.text)
# print(soup.findAll("div",{"id":"d1", "class":"small"})[0].div.p.text)
# print(soup.findAll("div",{"class":"small"})[0].div.p.text)

from bs4 import BeautifulSoup       
import os


html4 = """
        <div>div1</div>
        <div>div2</div>
        <div>div3</div>
        <div>div4</div>
        <div>div5</div>
        <div>div6</div>
        <div>div7</div>
        <div>div8</div>
        <div>div9</div>
        <div>div10</div>
        """

# soup = BeautifulSoup(html4, "html.parser")

# print(soup.findAll("div")[1].text, 
# soup.findAll("div")[3].text, 
# soup.findAll("div")[5].text, 
# soup.findAll("div")[7].text, 
# soup.findAll("div")[9].text)

# div = soup.findAll("div")
# print(div[1].text, div[3].text, div[5].text, div[7].text, div[9].text)

# divs = soup.findAll("div")[1::2]
# for div in divs:
#    print(div.text)


# divs = soup.findAll("div")
# list = [1, 3, 5, 7, 9]
# for i in list:
#     print(divs[i].text)

divs = soup.findAll("div")
for i, div in enumerate(divs):
    if (i+1) % 2 == 0:
        print(div.text)