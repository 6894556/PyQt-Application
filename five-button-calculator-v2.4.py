# five-v2.4 : five-v2.3 개선 (Clear Entry 버튼 기능 구현 - 카운터 사용)

# Error가 LCD에 표시된 상태라고 가정하자.
# Clear Entry 버튼을 한번 눌렀을 경우 :
#   Error 대신 self.operand1을 LCD에 출력한다.
#   self.operand2를 초기화한다.
#   self.operator에 담긴 연산자 버튼을 setChecked(True)한다.
# Clear Entry 버튼을 두번 눌렀을 경우 :
#   self.operator에 담긴 연산자 버튼을 setChecked(False)한다.
#   self.operator를 초기화한다.
# Clear Entry 버튼을 세번 눌렀을 경우 :
#   Clear Entry 버튼의 텍스트를 setText('AC')로 바꾼다.
#   LCD에 0을 표시한다.
#   self.operand1을 초기화한다.

import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLCDNumber, QPushButton,
                             QHBoxLayout, QVBoxLayout)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.operand = ''
        self.operand1 = 0.0
        self.operator = ''
        self.operand2 = 0.0
        ## CE 버튼 클릭 횟수 카운팅을 위한 전역변수
        self.count = 0
        self.initUI()

    def initUI(self):
        self.lcd = QLCDNumber(self)
        self.btn0 = QPushButton('0', self)
        self.btn1 = QPushButton('1', self)
        self.btn2 = QPushButton('/', self)
        self.btn3 = QPushButton('CE', self) # CE : Clear Entry
        self.btn4 = QPushButton('=', self)

        self.btn2.setCheckable(True)
        self.btn4.setCheckable(True)

        self.btn2.setAutoExclusive(True)
        self.btn4.setAutoExclusive(True)

        hbox = QHBoxLayout()
        hbox.addWidget(self.btn0)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        hbox.addWidget(self.btn3)
        hbox.addWidget(self.btn4)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.btn0.clicked.connect(self.slot0)
        self.btn1.clicked.connect(self.slot1)
        self.btn2.clicked.connect(self.slot2)
        self.btn3.clicked.connect(self.slot3)
        self.btn4.clicked.connect(self.slot4)

        self.setWindowTitle('five-v2.4')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def slot0(self):
        self.operand += '0'
        self.lcd.display(str(int(self.operand)))

    def slot1(self):
        self.operand += '1'
        self.lcd.display(str(int(self.operand)))

    def slot2(self):
        self.operand1 = self.lcd.value()
        self.operator = self.btn2.text()
        self.operand = ''

    ## CE 버튼 구현
    def slot3(self):
        self.count += 1
        self.count %= 3

        if self.count == 1:
            self.lcd.display(self.operand1)
            self.operand = ''

            self.btn2.setAutoExclusive(False)
            self.btn2.setChecked(True)
            self.btn2.setAutoExclusive(True)
        elif self.count == 2:
            self.btn2.setAutoExclusive(False)
            self.btn2.setChecked(False)
            self.btn2.setAutoExclusive(True)
            self.operator = ''
        elif self.count == 0:
            # self.btn3.setText('AC')
            self.lcd.diaplay(str(int(0)))
            print(self.count)
            self.operand1 = 0


    def slot4(self):
        self.operand2 = self.lcd.value()
        if self.operator == '/':
            if self.operand2 == 0.0:
                rslt = 'Error'
                self.lcd.display(rslt)
                self.operand = str(0)
            else:
                rslt = int(self.operand1) / int(self.operand2)
                self.lcd.display(rslt)
                self.operand = str(rslt)
        ## CE 기능 구현을 위해서 커멘트 처리
        ## self.operand1 = 0.0
        ## self.operand2 = 0.0
        self.btn4.setAutoExclusive(False)
        self.btn4.setChecked(False)
        self.btn4.setAutoExclusive(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())