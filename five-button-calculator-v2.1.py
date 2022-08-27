# five-2.1 : / (division) 버튼 원도우 구성
# 분자와 분모가 같으면 정수 범위를 벗어나지 않으므로
# 정수 범위를 벗어난 결과를 테스트하기 위해
# 0이 아닌 서로 다른 정수 두개가 필요하다.
# 분모가 0인 경우도 여기서 다루고자 한다.
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

        self.setWindowTitle('five-v2.1')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def slot0(self):
        self.operand += '0'
        self.lcd.display(self.operand)

    def slot1(self):
        self.operand += '1'
        self.lcd.display(self.operand)

    def slot2(self):
        self.operand += '2'
        self.lcd.display(self.operand)
    # opeator를 클릭해도 lcd 상에서 operand1에 append가 된다.
    # : self.btn3.clicked.connect(self.slot3)이 누락되었다.
    # 누락된 코드를 추가하니 문제가 해결되었다.
    def slot3(self):
        self.operand1 = self.lcd.value()
        self.operand = ''
        self.operator = self.btn3.text()


    def slot4(self):
        self.operand2 = self.lcd.value()
        if self.operator == '/':
            # int 0으로 해야할지, str 0으로 해야할지 헷갈립니다.
            if self.operand2 == 0:
                rst = 'NaN'
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