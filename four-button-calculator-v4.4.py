# four-v4.4 : v4.3의 버그1, 2, 3 잡기
# 버그1 : first operand를 입력하고 operator를 선택한 후에 Back버튼을 눌렀을 때,
#         LCD에서 값이 다 사라진다.
#         (일의 자리 숫자 하나만 지우고 싶다.)
# 버그2 : operand 두개 입력하고 operator 한개 선택한 후에
#        = 버튼을 누른 계산 결과에서 Back버튼을 누르면 LCD에 보였던 값이 전부 사라진다.
#        (전부 지워지면 안되고 일의 자리 숫자만 지워져야 한다.)
# 버그3 : Back 버튼이 지운 일의 자리 숫자가 유일한 숫자일 경우,
#        LCD에 아무 것도 표시되지 않는다.
#        (아무 것도 표시되지 않을 게 아니라 0이 LCD에 표시되게 고치고 싶다.)

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

        self.setWindowTitle('four-v4.4')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def slot1(self):
        self.operand += '1'
        self.lcd.display(self.operand)

    def slot2(self):
        self.operand1 = self.lcd.value()
        self.operand = ''
        self.operator = self.btn2.text()

    def slot3(self):
        self.operand = self.operand[:-1]
        ## 버그1, 버그3 해결을 위한 lambda 함수 추가
        ## getvalue : 마지막 element가 제거된 문자열 self.operand의 길이가
        ##            0보다 작거나 같으면 "0"을 반환하고,
        ##            0보다 크면 마지막 element가 제거된 self.operand를 반환한다.
        getvalue = lambda a: "0" if (len(self.operand) <= 0) else self.operand
        self.lcd.display(getvalue(self.operand))

    def slot4(self):
        self.operand2 = self.lcd.value()
        if self.operator == '+':
            rst = int(self.operand1) + int(self.operand2)
        self.lcd.display(rst)
        ## 버그2 해결을 위해 '' 대신
        ## str(rst)로 self.operand를 초기화 시킨다.
        self.operand = str(rst)
        self.operand1 = 0
        self.operand2 = 0
        self.operator = ''

        # =버튼을 누르면 선택된 operator 버튼을 선택 해제 시키는 코드
        # 선택된 operator 버튼만 선택 해제 시키는 게 아니라 =버튼도 선택 해제 시킨다.
        self.btn4.setAutoExclusive(False)
        self.btn4.setChecked(False)
        self.btn4.setAutoExclusive(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())