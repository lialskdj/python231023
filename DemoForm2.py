#DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import *
#웹서버에 요청
import requests
#크롤링
from bs4 import BeautifulSoup

#디자인 파일 로딩(파일명 변경)
form_class = uic.loadUiType("DemoForm2.ui")[0]
#폼 클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    #초기화 메소드
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    #슬롯 메소드
    def firstClick(self):
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

        self.label.setText("당근 크롤링 완료~~")


    def secondClick(self):
        self.label.setText("두번째 버튼~~")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭~~")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show() 
    app.exec_()
