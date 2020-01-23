from PyQt5 import QtWidgets
from PyQt5 import uic
import sys
import threading, time
import crawler


class Form(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.crawl = crawler.Crawl()
        self.ui = uic.loadUi("asd.ui", self)  # ui 파일 불러오기
        self.ui.show()
        self.working = False

    def entercode(self):
        self.working = True
        time.sleep(5)
        self.working = False
        self.sendshowresult()

    def sendshowresult(self):
        if self.working:  # thread lock 쓸 수 있을까??
            return
        if len(self.ui.lineEdit.text()) < 7:  # 코드 자릿수 확인
            print('올바른 코드 입력')
            return
        self.crawl.crawling(self.ui.lineEdit.text())  # 크롤링 함수 호출
        self.ui.code.setText(self.ui.lineEdit.text())  # 결과 label 업데이트
        self.ui.name.setText(self.crawl.nm)
        self.ui.max.setText(self.crawl.maxNumber)
        self.ui.now.setText(self.crawl.nowNumber)
        threading.Timer(3, self.sendshowresult).start()

    def closeEvent(self, QCloseEvent):
        self.working = True
        QCloseEvent.accept()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())
