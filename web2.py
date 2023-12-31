#web2.py

#웹서버에 요청
import requests
#크롤링
from bs4 import BeautifulSoup

f = open("C:\\work\\dangn.txt", "wt", encoding="utf-8")

url = "https://www.daangn.com/fleamarket/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

posts = soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    title = post.find("h2",attrs={"class","card-title"})
    price = post.find("div", attrs={"class":"card-price"})
    addr = post.find("div", attrs={"class":"card-region-name"})

    #메서드체인(함수체인)
    title = title.text.strip().replace("\n","")
    price = price.text.strip().replace("\n","")
    addr = addr.text.strip().replace("\n","")

    print(f"{title}, {price}, {addr}")
    f.write(f"{title}, {price}, {addr}\n") 

f.close()

# <div class="card-desc">
#       <h2 class="card-title">다이슨청소기</h2>
#       <div class="card-price ">
#         50,000원
#       </div>
#       <div class="card-region-name">
#         대구 수성구 범어2동
#       </div>