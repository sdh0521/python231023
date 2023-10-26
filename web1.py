# web1.py

from bs4 import BeautifulSoup

page=open("c:\\work\\test01.html", "rt", encoding="utf-8").read()

soup=BeautifulSoup(page, "html.parser")

# 전체 보기
# print(soup.prettify())

# <p>태그 전체를 검색
# print(soup.find_all("p"))

# 첫번째 <p>태그만 검색
# print(soup.find("p"))

# <p class="outer-text"> 형태만 검색
# print(soup.find_all("p", class_="outer-text"))
# attrs를 사용(위 대신 이렇게 사용)
# print(soup.find_all("p", attrs={"class":"outer-text"}))

# 특정 태그만 지정할 경우 id속성
# print(soup.find_all(id="first"))

# 태그 내부의 컨텐츠를 가져오기
for tag in soup.find_all("p"):
    title=tag.text.strip()
    title=title.replace("\n", "").replace("\t","")
    print(title)