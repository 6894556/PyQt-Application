# five-v2.2 : five-v2.1의 버그1, 2, 3 탐구 및 해결
# 버그1 : "0 -> 1"의 순서로 버튼을 택했을 때,
#         LCD에 1이 아니라 01이 표시되는 버그 (처음 선택한 버튼이 0일 경우)
# 버그2 : “1 -> 1 -> 1 -> 1 -> 1 -> 2 ”의 순서로 버튼을 택했을 때,
#        111112(일다섯개)가 아니라 11112(일네개)가 LCD에 표시되는 버그 (최대 다섯자리 표시)
# 버그3 : 0을 second operand로 택하고
#        eqaul sign 버튼을 눌렀을 경우 LCD에 어떤 문구를 표시할지에 대한 고찰.
#        e.g. NaN이라는 문구를 표시하고자 하니 A만 LCD에 표시되는 버그가 발생함.
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
        # setDigitCount 위치 후보 1 : 탈락
        # (self.operand가 처음에 ''로 초기화 되기 때문에 len이 0이다.)
        # self.lcd.setDigitCount(len(self.operand))
        # 0, 1, 2 버튼이 연결된 슬롯에 모두 넣는 방안은 어떨까?
        self.btn0 = QPushButton('0', self)
        self.btn1 = QPushButton('1', self)
        self.btn2 = QPushButton('2', self)
        self.btn3 = QPushButton('/', self)
        self.btn4 = QPushButton('=', self)

        self.btn3.setCheckable(True)
        self.btn4.setCheckable(True)

        self.btn3.setAutoExclusive(True)
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

        self.setWindowTitle('five-v2.2')
        self.setGeometry(300, 300, 300, 200)
        self.show()
    # 0버튼만 10번 눌렀을 때 LCD에 표시되는 0의 크기가 작아진다. (버그인가?)
    def slot0(self):
        self.operand += '0'
        # 버그2 해결 part1 : setDigitCount(len(self.operand))
        self.lcd.setDigitCount(len(self.operand))
        # 버그1 해결 part1 : str(int(self.operand))
        self.lcd.display(str(int(self.operand)))

    def slot1(self):
        self.operand += '1'
        # 버그2 해결 part2 : setDigitCount(len(self.operand))
        self.lcd.setDigitCount(len(self.operand))
        # 버그1 해결 part2 : str(int(self.operand))
        self.lcd.display(str(int(self.operand)))

    def slot2(self):
        self.operand += '2'
        # 버그2 해결 part3 : setDigitCount(len(self.operand))
        self.lcd.setDigitCount(len(self.operand))
        # 버그1 해결 part3 : str(int(self.operand))
        self.lcd.display(str(int(self.operand)))

    def slot3(self):
        self.operand1 = self.lcd.value()
        self.operand = ''
        self.operator = self.btn3.text()

    ## 새로운 버그 : Error가 표시되면 처음으로 되돌아갈 방법이 없다.
    def slot4(self):
        self.operand2 = self.lcd.value()
        # print(type(self.operand2))
        if self.operator == '/':
            # self.lcd.value는 float 타입을 반환하므로 0.0
            if self.operand2 == 0.0:
                ## 버그3 : seven-segment로 Error표시가 가능하다. 하지만 작동하지 않는다. 왜?
                rst = "Error"
                ## rst = "E r r o r"
                ##   : 문자와 문자 사이에 스페이스를 넣어주면 어떨지 테스트 해보기 위함. (but failed)
                ## 버그3 해결 : LCD의 digitCount가 1인 상태이므로 digitCount가 5인 Error를 표시하지 못한 것.
                self.lcd.setDigitCount(len(rst))
            else:
                rst = int(self.operand1) / int(self.operand2)
        self.lcd.display(rst)
        # Back 버튼 제어를 위한 수정된 self.operand 초기화
        self.operand = str(rst)
        self.operand1 = 0
        self.operand2 = 0
        self.operator = ''


        self.btn4.setAutoExclusive(False)
        self.btn4.setChecked(False)
        self.btn4.setAutoExclusive(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())