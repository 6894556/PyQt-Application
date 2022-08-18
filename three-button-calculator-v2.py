# v2 : 슬롯 정의
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLCDNumber, QLabel, QPushButton,
                             QHBoxLayout, QVBoxLayout)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.initUI()

    def initUI(self):
        self.lcd1 = QLCDNumber(self)
        self.lbl2 = QLabel(self)
        self.lcd3 = QLCDNumber(self)
        self.lcd4 = QLCDNumber(self)

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.lcd1)
        hbox1.addWidget(self.lbl2)
        hbox1.addWidget(self.lcd3)
        hbox1.addWidget(self.lcd4)

        btn1 = QPushButton('1', self)
        btn2 = QPushButton('+', self)
        btn3 = QPushButton('=', self)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(btn1)
        hbox2.addWidget(btn2)
        hbox2.addWidget(btn3)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        self.setLayout(vbox)

        self.setWindowTitle('')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def slot1(self):
        self.turn += 1
        if self.turn > 1:
            self.lcd3.display(1)
        else:
            self.lcd1.display(1)

    def slot2(self):
        self.lbl2.setText('+')

    def slot3(self):
        self.turn = 0
        operand1 = self.lcd1.value()
        operator = self.lbl2.text()
        operand2 = self.lcd3.value()

        if operator == '+':
            r = int(operand1) + int(operand2)
            self.lcd4.display(r)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())