# four-v4.3 : v4.2의 Back 버튼 동작 버그 수정
# bug1 : first operand를 입력하고 operator를 선택한 후에 B버튼을 눌렀을 때 lcd에서 값이 다 사라진다.
# bug2 : operand 두개 입력하고 operator 한개 선택한 후에 =버튼을 누른 계산 결과에서 백버튼을 누를 경우 lcd에 보이는 값이 전부 지워진다.
# (전부 지워지면 안되고 일의 자리 숫자만 지워져야 한다.)
# bug3 : B버튼이 지운 일의 자리 숫자가 유일한 숫자일 경우 LCD에 아무것도 표시되지 않는다.
# (아무것도 표시되지 않을 게 아니라 0이 표시되게 고치고 싶다.)
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
        self.btn2.clicked.connect(self.slot2)
        self.btn3.clicked.connect(self.slot3)
        self.btn4.clicked.connect(self.slot4)


        self.setWindowTitle('four-v4.3')
        self.setGeometry(300, 300, 300 ,200)
        self.show()

    def slot1(self):
        self.operand += '1'
        self.lcd.display(self.operand)

    def slot2(self):
        self.operand1 = self.lcd.value()
        self.operator = self.btn2.text()
        self.operand = ''
        # print(self.operand1)
        # print(self.operator)

    def slot3(self):
        # lcd.value로 현재값을 불러온다.
        # 불러온 현재값을 str로 전환한다. (불러온 값이 int라는 가정)
        # str = str[:-1]로 마지막 element를 제거한다.
        # 마지막 element를 제거한 str을 lcd.display(str)한다.
        # self.operand = self.lcd.value()
        self.operand = self.operand[:-1]
        self.lcd.display(self.operand)

    def slot4(self):
        self.operand2 = self.lcd.value()
        if self.operator == '+':
            rst = int(self.operand1) + int(self.operand2)
        self.lcd.display(rst)
        # initialization
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