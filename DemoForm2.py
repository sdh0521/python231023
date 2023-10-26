# DemoForm2.py

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests # 웹서버 요청
from bs4 import BeautifulSoup  # 크롤링

form_class=uic.loadUiType("DemoForm2.ui")[0]

class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
    # 슬럿 메서드
    def firstClick(self):
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

        self.label.setText("당근 크롤링 완료")
    def secondClick(self):
        self.label.setText("두번째 버튼")
    def thirdClick(self):
        self.label.setText("세번째 버튼")

if __name__ == "__main__":
    app=QApplication(sys.argv)
    DemoForm = DemoForm()
    DemoForm.show()
    app.exec_()