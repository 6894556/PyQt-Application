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
        self.btn3 = QPushButton('-', self)
        self.btn4 = QPushButton('=', self)

        self.btn2.setCheckable(True)
        self.btn3.setCheckable(True)
        self.btn4.setCheckable(True)

        self.btn2.setAutoExclusive(True)
        self.btn3.setAutoExclusive(True)
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

        self.setWindowTitle('four-v1.8')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def slot1(self):
        self.operand += '1'
        self.lcd.display(self.operand)

    def slot2(self):
        self.operand1 = self.lcd.value()
        self.operand = ''
        self.operator = ''
        self.operator = self.btn2.text()

    def slot3(self):
        self.operand1 = self.lcd.value()
        self.operand = ''
        self.operator = ''
        self.operator = self.btn3.text()

    def slot4(self):
        self.operand2 = self.lcd.value()
        self.operand = ''
        if self.operator == '+':
            rst = int(self.operand1) + int(self.operand2)
        if self.operator == '-':
            rst = int(self.operand1) - int(self.operand2)
        self.lcd.display(rst)
        self.operator = ''
        self.operand1 = 0
        self.operand2 = 0

        ## 이하 =버튼이 눌리면 모든 연산자 버튼을
        ## 선택되지 않은 상태로 만들기 위한 코드
        self.btn4.setAutoExclusive(False)
        self.btn4.setChecked(False)
        self.btn4.setAutoExclusive(True)
''' 아래 코드가 필요 없는 이유를 이해하지 못함.
        self.btn3.setAutoExculsive(False)
        self.btn3.setChecked(False)
        self.btn3.setAutoExclusive(True)

        self.btn4.setAutoExclusive(True)
        self.btn4.setChecked(False)
        self.btn4.setAutoExclusive(True)

'''




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())