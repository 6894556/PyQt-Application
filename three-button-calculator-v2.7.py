# v2.7 : 슬롯 연결
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
        self.btn3 = QPushButton('=', self)

        hbox = QHBoxLayout()
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        hbox.addWidget(self.btn3)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.btn1.clicked.connect(self.slot1)
        self.btn2.clicked.connect(self.slot2)
        self.btn3.clicked.connect(self.slot3)

        self.setWindowTitle('one-lcd')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def slot1(self):
        self.operand += '1'
        self.lcd.display(self.operand)

    def slot2(self):
        self.btn2.setCheckable(True)
        self.btn2.toggle()
        self.operand1 = self.lcd.value()
        self.operand = ''

    def slot3(self):
        self.btn2.toggle()
        self.operand2 = self.lcd.value()
        self.operator = self.btn2.text()
        if self.operator == '+':
            rst = int(self.operand1) + int(self.operand2)
            self.lcd.display(rst)
        rst = 0
        # rst가 lcd에 표시된 상태에서 operator를 클릭하고
        # 숫자를 입력하고 equal sign 버튼을 클릭하면
        # rst + 입력한 숫자가 계산되는 이유가 궁금합니다.
        # (이를 방지하기 위한 차원에서 위 rst = 0를 추가했습니다)
        # (하지만 결과적으로는 더 자연스러운 실행이 가능한듯 합니다.)
        self.operand1 = 0
        self.operand2 = 0



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())