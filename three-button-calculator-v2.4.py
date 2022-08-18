# v2.4. : 슬롯 연결
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLCDNumber, QPushButton,
                             QHBoxLayout, QVBoxLayout)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        # class variables (클래스 변수)
        self.operand = ''
        self.operand1 = 0
        self.operand2 = 0
        self.operator = ''
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

        self.setWindowTitle('')
        self.setGeometry(300, 300, 500, 200)
        self.show()

    # slot1 : 1 sign을 클릭 했을 경우
    # -- 1) n번 클릭 했을 경우에 대비 (operator 클릭 전까지 누적)
    # -- 2) operand 값을 lcd에 출력
    def slot1(self):
        self.operand += '1'
        self.lcd.display(self.operand)

    # slot2 : addition sign을 클릭 했을 경우
    # -- 1) 어떤 operator가 클릭 됬을 경우 모든 operator 버튼을 비활성화 (equal sign 클릭 전까지)
    # -- 2) lcd에 표시된 값(self.operand에 누적된 값)을 첫 번째 operand 값으로 assign
    # -- 3) lcd에 표시된 값을 초기화
    def slot2(self):
        # True 설정 시, 누른 상태와 그렇지 않은 상태를 구분
        self.btn2.setCheckable(True)
        # 상태를 바꾸는 메서드
        self.btn2.toggle()
        # self.btn2.setEnabled(False) - 임시보류
        self.operand1 = self.lcd.value()
        self.operand = ''
        # print(self.operand1)

    # slot3 : equal sign을 클릭 했을 경우
    # -- 1) lcd에 표시된 값을 두 번째 operand 값으로 assign
    # -- 1) 비활성화 상태인 모든 버튼을 활성화 상태로 전환 (n번 계산 가능하게 하기 위함)
    # -- 2) 결과값 계산
    # -- 3) 결과값을 lcd에 표시
    def slot3(self):
        self.btn2.toggle()
        operand2 = self.lcd.value()
        self.operator = self.btn2.text()

        if self.operator == '+':
            rst = int(self.operand1) + int(operand2)
            self.lcd.display(rst)
        rst = 0
        # equal sign을 한번 이상 눌렀을 경우 값이 계속 증가하는 이슈를 방지하기 위함
        self.operand1 = 0
        self.operand2 = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

# 누른 상태와 누르지 않은 상태를 구분한다 vs operator를 한번 누르면 모든 operator를 disable시킨다.
# width 300 일 때 maximum 자릿수 : 5
# width 500 일 때 maximum 자릿수 : 5
# lcd 한개는 최대 다섯자리까지 표시할 수 있다.