# four-v3.2 : AC 버튼 슬롯 정의 & 연결
# four-v3.2의 문제점 : AC 버튼을 눌러도 operator의 선택이 취소가 되지 않음 (취소 되어야 함)
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLCDNumber, QPushButton,
                             QHBoxLayout, QVBoxLayout)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.operand = ''
        self.operand1 = 0
        self.operator = ''
        self.operand2 = 0
        self.initUI()

    def initUI(self):
        self.lcd = QLCDNumber(self)
        self.btn1 = QPushButton('1', self)
        self.btn2 = QPushButton('+', self)
        self.btn3 = QPushButton('AC', self)
        self.btn4 = QPushButton('=', self)

        self.btn2.setCheckable(True)
        self.btn4.setCheckable(True)

        self.btn2.setAutoExclusive(True)
        self.btn4.setAutoExclusive(True)

        hbox = QHBoxLayout()
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        hbox.addWidget(self.btn3)
        hbox.addWidget(self.btn4)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.btn1.clicked.connect(self.slot1)
        self.btn2.clicked.connect(self.slot2)
        self.btn3.clicked.connect(self.slot3)
        self.btn4.clicked.connect(self.slot4)

        self.setWindowTitle('four-v3.2')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def slot1(self):
        self.operand += '1'
        self.lcd.display(self.operand)

    def slot2(self):
        self.operand1 = self.lcd.value()
        self.operand = ''
        self.operator = self.btn2.text()

    # AC 버튼이 클릭될 경우
    # - lcd 패널에 표시된 숫자가 0으로 바뀜
    # - self.operand 초기화 (무슨값이 있었던 간에 0을 대입하면 될 줄 알았으나 안됨. 초기값이 0이 아니였음)
    # - self.operand1, self.operand2 초기화
    # - rst 초기화 - 필요한가? 필요없을 수도 있을 거 같다. (local 변수라 slot3에서 초기화 못함)
    def slot3(self):
        self.lcd.display(0)
        self.operand = ''
        self.operand1 = 0
        self.operator = ''
        self.operand2 = 0


    def slot4(self):
        self.operand2 = self.lcd.value()
        if self.operator == '+':
            rst = int(self.operand1) + int(self.operand2)
        self.lcd.display(rst)
        self.btn4.setAutoExclusive(False)
        self.btn4.setChecked(False)
        self.btn4.setAutoExclusive(True)

        self.operand = ''
        self.operand1 = 0
        self.operator = ''
        self.operand2 = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())