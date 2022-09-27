# five-v2.5 : five-v2.4  로직 에러 수정
# 오류가 발생한 경우 CE 버튼을 AC버튼으로 변경

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
        self.count = 0
        self.initUI()

    def initUI(self):
        self.lcd = QLCDNumber(self)
        self.btn0 = QPushButton('0', self)
        self.btn1 = QPushButton('1', self)
        self.btn2 = QPushButton('/', self)
        self.btn3 = QPushButton('CE', self)
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

        self.setWindowTitle('five-v2.5')
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

    ## Clear 버튼 구현 (All Clear, Clear Entry)
    def slot3(self):
        self.count += 1
        self.count %= 3

        ## Error가 발생한 경우
        if self.btn3.text() == 'AC':
            self.lcd.display(0)
            self.operand = ''
            self.operand1 = 0
            self.operator = ''
            self.operand2 = 0
        ## Error가 발생하지 않은 경우
# if self.btn3.text() == 'CE':

    def slot4(self):
        self.operand2 = self.lcd.value()
        if self.operator == '/':
            if self.operand2 == 0.0:
                rslt = 'Error'
                self.lcd.display(rslt)
                self.operand = str(0)
                ## Error 발생 시 Clear Entry 버튼을 All Clear 버튼으로 변경
                ## Error가 발생하면 Clear Entry 버튼 사용 불가.
                self.btn3.setText('AC')
            else:
                rslt = int(self.operand1) / int(self.operand2)
                self.lcd.display(rslt)
                self.operand = str(rslt)
                ## Error가 발생하지 않을 시 Clear Entry 버튼 사용 가능.
                self.btn3.setText('CE')

        self.btn4.setAutoExclusive(False)
        self.btn4.setChecked(False)
        self.btn4.setAutoExclusive(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())