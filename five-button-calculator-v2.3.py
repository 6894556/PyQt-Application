# five-v2.3 : five-v2.2의 새로운 버그 탐구 및 해결 (이제 보니 2버튼은 필요가 없다)
# 새로운 버그 : Error가 표시되면 처음으로 되돌아갈 방법이 없다.
# (Error가 lcd에 표시된 상태라는 가정에서)해결 방향(세가지) :
# - 임의의 operand를 클릭하면 해당하는 수가 LCD에 표시되고
#   기존에 입력된 self.operand1와 self.operand2, 그리고
#   self.operator에 저장된 모든 값을 초기화시키고 사용자가 클릭한
#   operand에 해당하는 수를 self.operand1에 assign한다.
# - Clear 버튼을 클릭하면 0이 저장되어 있는 self.operand2를 초기화한다.
#   =버튼을 누르기 전의 상태로 돌려보낸다?
# - All Clear 버튼을 누르면 모든 값을 초기화 하고 LCD에 0을 표시한다.
# - Error가 LCD에 표시된 상태에서 operator를 클릭하고 operand 클릭 후 =버튼 누르면
#   Error만 LCD에 표시한다.
# five-v2.3에서는 첫 번째 해결방향을 구현해보고자 한다.

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
        # Error가 5자리이므로 테스트를 위해서는 최소 6자리 이상이어야함
        self.lcd.setDigitCount(6)
        self.btn0 = QPushButton('0', self)
        self.btn1 = QPushButton('1', self)
        self.btn2 = QPushButton('/', self)
        self.btn3 = QPushButton('=', self)


        self.btn2.setCheckable(True)
        self.btn3.setCheckable(True)

        self.btn2.setAutoExclusive(True)
        self.btn3.setAutoExclusive(True)

        hbox = QHBoxLayout()
        hbox.addWidget(self.btn0)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        hbox.addWidget(self.btn3)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.btn0.clicked.connect(self.slot0)
        self.btn1.clicked.connect(self.slot1)
        self.btn2.clicked.connect(self.slot2)
        self.btn3.clicked.connect(self.slot3)

        self.setWindowTitle('five-v2.3')
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
        self.operand2 = self.lcd.value()
        if self.operator == '/':
            if self.operand2 == 0.0:
                rst = 'Error'
                ## 새로운 버그 수정 part1
                self.lcd.display(rst)
                # 0으로 초기화
                self.operand = str(0)
            else:
                rst = int(self.operand1) / int(self.operand2)
                ## 새로운 버그 수정 part2
                self.lcd.display(rst)
                self.operand = str(rst)
        # self.lcd.display(rst)
        # self.operand = str(rst)
        self.operand1 = 0.0
        self.operand2 = 0.0
        self.btn3.setAutoExclusive(False)
        self.btn3.setChecked(False)
        self.btn3.setAutoExclusive(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())