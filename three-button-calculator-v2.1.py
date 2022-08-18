# v2.1 : v1.x 수정
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLCDNumber, QPushButton,
                             QHBoxLayout, QVBoxLayout)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.operand = ''
        self.operand1 = 0
        self.operand2 = 0
        # self.operator = which type?
        # self.turn = 0
        self.initUI()

    def initUI(self):
        self.lcd = QLCDNumber(self)

        btn1 = QPushButton('1', self)
        btn2 = QPushButton('+', self)
        btn3 = QPushButton('=', self)

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lcd)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        btn1.clicked.connect(self.slot1)
        btn2.clicked.connect(self.slot2)
        btn3.clicked.connect(self.slot3)

        self.setWindowTitle('')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    # slot1 : 1 sign을 클릭 했을 경우
    def slot1(self):
        # 1버튼을 n번 클릭했을 경우에 대비하여
        # str 타입 self.ran에 btn1이 클릭 될 때마다
        # (slot1이 호출되므로) '1'을 append하는 방식.
        self.operand += '1'

        # lcd 패널 한개로 첫번째 operand와
        # 두번째 operand, 그리고 result 값을 화면에 표시할 것임을 고려하여
        # 아래와 같이 처리함.
        self.lcd.display(self.operand)


    # slot2 : addition sign을 클릭 했을 경우
    def slot2(self):
        # 어떤 연산자가 클릭 되는 시그널이 한번이라도 발생했을 경우 (=사인 버튼 누르기 전까지만 유효해야함.)
        # 모든 연산자 버튼을 비활성화시키는 것을 목표로 삼아
        # 여기서는 +버튼이 클릭 됬을 경우 +버튼을 비활성화하는 기능을 구현.

        # 어떤 operator가 클릭 되면
        # equal sign 버튼을 누르기 전까지 입력 되는 모든 숫자들은
        # 두 번째 operand로 처리함을 목표로 함.
        self.btn2.setCheckable(False)

        # lcd 패널에 표시된 값을 operand1에 저장
        self.operand1 = self.lcd.value()

        # 첫 번째 operand에 저장된 값이 두 번째 operand로
        # 넘어가면 안되므로 self.ran 값을 초기화함.
        self.operand = ''



    # slot3 : equal sign을 클릭 했을 경우
    # -- 1) 비활성화 상태인 모든 버튼들이 활성화 상태로 전환되어야 함.
    # -- 2) 연산의 결과값이 계산되어 result 변수에 저장되어야 함.
    # -- 3) 연산의 결과값이 lcd 패널에 표시 되어야 함.
    def slot3(self):
        # equal sign이 눌렸을 때 lcd 패널에 표시된 값이
        # 두 번째 operand이므로
        operand2 = self.lcd.value()

        # 버튼의 텍스트가 operator이므로
        operator = self.btn2.text()

        if operator == '+':
            rst = int(self.operand1) + int(operand2)
            # lcd 패널에 결과값을 표시
            self.lcd.display(rst)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())