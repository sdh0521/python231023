# web2.py

import requests # 웹서버 요청
from bs4 import BeautifulSoup  # 크롤링

url="https://www.daangn.com/fleamarket/"
response=requests.get(url)
soup=BeautifulSoup(response.text, "html.parser")

f=open("c:\\work\\dangn.txt", "wt", encoding="utf-8")
# <div class 속성 딕셔너리>
posts=soup.find_all("div", attrs={"class":"card-desc"})
for post in posts:
    title=post.find("h2", attrs={"class":"card-title"})
    price=post.find("div", attrs={"class":"card-price"})
    addr=post.find("div", attrs={"class":"card-region-name"})
    
    title=title.text.strip().replace("\n", "")
    price=price.text.strip().replace("\n", "")
    addr=addr.text.strip().replace("\n", "")
    
    print("물건: {0} / 가격: {1} / 주소: {2}".format(title, price, addr))
    # f를 붙이고 변수명 넘기기
    f.write(f"물건: {title} / 가격: {price} / 주소: {addr}\n")

f.close()

# <div class="card-desc">
#       <h2 class="card-title">다이슨청소기</h2>
#       <div class="card-price ">
#         50,000원
#       </div>
#       <div class="card-region-name">
#         대구 수성구 범어2동
#       </div>
#       <div class="card-counts">
#           <span>
#             관심 28
#           </span>
#         ∙
#         <span>
#             채팅 26
#           </span>
#       </div>
#     </div>