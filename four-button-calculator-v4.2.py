# four-v4.2 : B (back) 버튼 슬롯 정의 & 연결
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
        self.btn3 = QPushButton('B', self)
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
        self.btn3.clicked.connect(self.slot3)
        self.btn2.clicked.connect(self.slot2)
        self.btn4.clicked.connect(self.slot4)

        self.setWindowTitle('four-v4.1')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def slot1(self):
        self.operand += '1'
        self.lcd.display(self.operand)

    def slot2(self):
        self.operand1 = self.lcd.value()
        self.operand = ''
        self.operator = ''
        self.operator = self.btn2.text()

    # B 버튼이 클릭된 경우
    # - lcd에서 마지막으로 더해진 숫자 하나를 제거하는게 보여야함
    # - self.operand 에서 마지막으로 더해진 숫자 하나가 제거되야함
    def slot3(self):
        # bug report 1 : first operand를 입력하고 operator를 선택한 후에 B버튼을 눌렀을 때 lcd에서 값이 다 사라진다.
        # bug report 2 : operand 두개 입력하고 operator 한개 선택한 후에 =버튼을 누른 계산 결과에서 백버튼을 누를 경우 lcd에 보이는 값이 전부 지워진다.
        # (전부 지워지면 안되고 일의 자리 숫자만 지워져야 한다.)
        self.operand = self.operand[:-1]
        self.lcd.display(self.operand)
        # self.lcd.display(back)
        # print(self.operand)
        # self.lcd.

    def slot4(self):
        self.operand2 = self.lcd.value()

        rst = int(self.operand1) + int(self.operand2)
        self.lcd.display(rst)
        rst = 0
        self.operand = ''
        self.operand1 = 0
        self.operator = ''
        self.operand2 = 0

        self.btn4.setAutoExclusive(False)
        self.btn4.setChecked(False)
        self.btn4.setAutoExclusive(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())