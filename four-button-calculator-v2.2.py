# four-v2.2 : 슬롯 연결 (operand가 두개)
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
        self.btn2 = QPushButton('2', self)
        self.btn3 = QPushButton('+', self)
        self.btn4 = QPushButton('=', self)

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

        self.setWindowTitle('four-v2.1')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    # 버튼1이 클릭됬을 경우
    def slot1(self):
        self.operand += '1'
        self.lcd.display(self.operand)
    def slot2(self):
        self.operand += '2'
        self.lcd.display(self.operand)
    def slot3(self):
        self.operand1 = self.lcd.value()
        # print(self.operand1)
        self.operand = ''
        self.operator = ''
        self.operator = self.btn3.text()

    def slot4(self):
        self.operand2 = self.lcd.value()
        if self.operator == '+':
            rst = int(self.operand1) + int(self.operand2)
        self.lcd.display(rst)
        rst = 0
        self.operand1 = 0
        self.operand2 = 0




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())