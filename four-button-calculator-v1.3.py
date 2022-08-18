# v1.3 : 슬롯 연결
import sys
from PyQt5.QtWidgets import(QApplication, QWidget,
                            QLCDNumber, QPushButton,
                            QHBoxLayout, QVBoxLayout)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.operand = ''
        self.operand1 = 0
        ## 연산자를 클래스 변수로 두기
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

        self.btn1.clicked.connect(self.slot1)
        self.btn2.clicked.connect(self.slot2)
        self.btn3.clicked.connect(self.slot3)
        self.btn4.clicked.connect(self.slot4)

        self.setWindowTitle('v1.1')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def slot1(self):
        self.operand += '1'
        self.lcd.display(self.operand)

    def slot2(self):
        # btn3가 선택된 상태면 그 상태를 전환해주는 방법을 잘 모르겠습니다.
        self.btn2.setCheckable(True)
        self.btn2.toggle()
        self.operand1 = self.lcd.value()
        self.operand = ''
        ## 연산자로 정의한 객체 변수에 버튼의 값을 저장했습니다.
        # 이전에 어떤 값이 들어가 있을지 모르겠어서 초기화 했으나
        # 필요 유무를 잘 모르겠습니다.
        self.operator = ''
        self.operator = self.btn2.text()

    def slot3(self):
        # btn2가 선택된 상태면 그 상태를 전환해주는 방법을 잘 모르겠습니다.
        self.btn3.setCheckable(True)
        self.btn3.toggle()
        self.operand1 = self.lcd.value()
        self.operand = ''
        ## 연산자로 정의한 객체 변수에 버튼의 값을 저장했습니다.
        self.operator = '' # 초기화
        self.operator = self.btn3.text()

    def slot4(self):
        # 클릭된 버튼이 연산자 버튼 둘 중 어느 것인지 알 수 없으므로
        # 모든 operator 버튼의 상태가 구분이 안되게 바꿔봤습니다.
        self.btn2.setCheckable(False)
        self.btn3.setCheckable(False)
        self.operand2 = self.lcd.value()
        ## 최종적으로 선택한 연산자를 담고 있는 클래스 변수의 값을 보고
        ## 어떤 연산을 수행할지 판단하도록 작성했습니다.
        if self.operator =='+':
            rst = int(self.operand1) + int(self.operand2)
        if self.operator == '-':
            rst = int(self.operand1) - int(self.operand2)
        self.lcd.display(rst)
        rst = 0
        self.operand1 = 0
        self.operand2 = 0
        # self.operator = ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())