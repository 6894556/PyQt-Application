# v1.2 : 슬롯 정의
import sys
from PyQt5.QtWidgets import(QApplication, QWidget,
                            QLCDNumber, QPushButton,
                            QHBoxLayout, QVBoxLayout)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.operand = ''
        self.operand1 = 0
        # 연산자를 클래스 변수로 두기
        self.operator = ''
        self.operand2 = 0
        self.initUI()

    def initUI(self):
        self.lcd = QLCDNumber(self)
        self.btn1 = QPushButton('1', self)
        self.btn2 = QPushButton('+', self)
        self.btn3 = QPushButton('-', self)
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

        self.setWindowTitle('v1.1')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def slot1(self):
        self.operand += '1'
        self.lcd.display(self.operand)

    def slot2(self):
        # btn3가 선택된 상태면 그 상태를 전환해주는 코드????
        self.btn2.setCheckable(True)
        self.btn2.toggle()
        self.operand1 = self.lcd.value()
        self.operand = ''
        # 연산자로 정의한 객체 변수에 버튼의 값을 저장하기
        self.operator = ''  # 초기화 - 이전에 어떤 값이 들어가 있을지 모르므로
        self.operator = self.btn2.text()

    def slot3(self):
        # btn2가 선택된 상태면 그 상태를 전환해주는 코드????
        self.btn3.setCheckable(True)
        self.btn3.toggle()
        self.operand1 = self.lcd.value()
        self.operand = ''
        # 연산자로 정의한 객체 변수에 버튼의 값을 저장하기
        self.operator = '' # 초기화
        self.operator = self.btn3.text()

    def slot4(self):
        # (둘 중 어느 것인지 모르는)클릭된 버튼의 상태를 전환해주는 코드가 필요한가?
        # 모든 operator 버튼의 상태가 구분이 안되게 바꿔보자.
        self.btn2.setCheckable(False)
        self.btn3.setCheckable(False)
        self.operand2 = self.lcd.value()
        # 최종적으로 선택한 연산자를 담고 있는 클래스 변수의 값을 보고
        # 어떤 연산을 수행할지 판단하도록 하기
        if self.operator =='+':
            rst = int(self.operand1) + int(self.operand2)

        elif self.operator == '-':
            rst = int(self.operand1) - int(self.operand2)

        # else:
        # '+'도 '-'도 아니면 어떤 처리가 필요한가?
        # '+'도 '-'도 아닐 수가 없지 않은가?
        self.lcd.display(rst)
        rst = 0
        self.operand1 = 0
        self.operand2 = 0
        # self.operator = '' 초기화 위치 후보


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())