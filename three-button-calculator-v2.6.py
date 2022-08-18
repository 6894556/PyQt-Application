# v2.6 : 슬롯 정의
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
            rst = int(self.operan1) + int(self.operand2)
            self.lcd.display(rst)
        rst = 0
        self.operand1 = 0
        self.operand2 = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())