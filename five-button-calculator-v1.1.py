# five-v1.1 : 윈도우 구성 (operator 두개, operand 두개)
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLCDNumber, QPushButton,
                             QHBoxLayout, QVBoxLayout)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lcd = QLCDNumber(self)
        self.btn1 = QPushButton('1', self)
        self.btn2 = QPushButton('2,', self)
        self.btn3 = QPushButton('+', self)
        self.btn4 = QPushButton('-', self)
        self.btn5 = QPushButton('=', self)

        ##### 눌린 상태를 구분하는 것도 모양에 포함 #####
        self.btn3.setCheckable(True)
        self.btn4.setCheckable(True)
        self.btn5.setCheckable(True)

        self.btn3.setAutoExclusive(True)
        self.btn4.setAutoExclusive(True)
        self.btn5.setAutoExclusive(True)
        ##########################################

        hbox = QHBoxLayout()
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)
        hbox.addWidget(self.btn3)
        hbox.addWidget(self.btn4)
        hbox.addWidget(self.btn5)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.btn5.clicked.connect(self.slot5)


        self.setWindowTitle('five-1.1')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def slot5(self):
        self.btn5.setAutoExclusive(False)
        self.btn5.setChecked(False)
        self.btn5.setAutoExclusive(True)

if __name__ =='__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())