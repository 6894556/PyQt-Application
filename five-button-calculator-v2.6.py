# five-v2.6 : Clear All 버튼 구현
# 재설계:
#   - Clear All과 Clear Entry 버튼 분리
#   - Clear All
#       - lcd 패널에 0을 표시한다.
#       - self.operand1을 초기화
#       - self.operand2를 초기화
#       - self.operand를 초기화
#       - self.operator를 초기화
#   - Clear Entry
#       - Error가 발생한 경우
#
#       - Error가 발생하지 않은 경우
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
        self.initUI()

    def initUI(self):
        self.lcd = QLCDNumber(self)
        self.btn0 = QPushButton('0', self)
        self.btn1 = QPushButton('1', self)
        self.btn2 = QPushButton('/', self)
        self.btn3 = QPushButton('AC', self)
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

        self.setWindowTitle('five-v2.6')
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


    def slot3(self):
        self.operand = ''
        self.operand1 = 0.0
        self.operator = ''
        self.operand2 = 0.0
        self.lcd.display('0')

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

        self.btn4.setAutoExclusive(False)
        self.btn4.setChecked(False)
        self.btn4.setAutoExclusive(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())