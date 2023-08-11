# DemoForm2.py 
# DemoForm.ui(화면단) + DemoForm.py(로직단)
import sys
import typing 
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget 
#웹서버에 실행 요청
import requests
#웹크롤링
from bs4 import BeautifulSoup

#디자인 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

#폼 클래스 정의(부모 클래스명 QMainWindow)
class DemoForm(QMainWindow, form_class):
    #초기화 메서드
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    #슬롯메서드정의
    def firstClick(self):
        self.label.setText("첫번째 버튼")
    def secondClick(self):
        self.label.setText("두번째 버튼")
    def thirdClick(self):
        self.label.setText("세번째 버튼 클릭")
        
    url = "https://www.daangn.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    #파일 저장
    f = open("daangn.txt", "wt", encoding="utf-8")
    posts = soup.find_all("div", attrs={"class":"card-desc"})
    for post in posts:
        titleElem = post.find("h2", attrs={"class":"card-title"})
        title = titleElem.text.replace("\n", "") 
        priceElem = post.find("div", attrs={"class":"card-price"})
        price = priceElem.text.replace("\n", "")  
        addrElem = post.find("div", attrs={"class":"card-region-name"})
        addr = addrElem.text.replace("\n", "")  
        print("{0}, {1}, {2}".format(title, price, addr))
        #python 3.8이상에서 사용 
        f.write(f"{title}, {price}, {addr}\n")
    f.close()    

#진입점 체크(이 모듈을 직접 실행한 경우)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_() 

