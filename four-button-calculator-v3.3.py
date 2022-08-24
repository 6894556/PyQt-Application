# four-v3.3 : AC 버튼 제작 (v3.2의 문제점 해결)
# four button including all clear button
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
        self.btn3 = QPushButton('AC', self)
        self.btn4 = QPushButton('=', self)

        # AC 버튼의 눌린 상태 구분이 필요한가?
        # AC 버튼의 선택 상태 구분은 필요하지 않다.
        # 왜냐하면 AC 버튼을 눌렀을 경우
        # LCD에 표시되던 값이 무슨 값이었던 간에
        # 0으로 바뀌게끔 설정했고,
        # 선택된 operator가 무엇이었던 간에
        # 선택이 해제되게끔 설정했기 때문에
        # AC 버튼의 선택 상태를 setCheckable(True)로
        # 구분해줄 필요가 없다.
        self.btn2.setCheckable(True)
        self.btn4.setCheckable(True)

        self.btn2.setAutoExclusive(True)
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

        self.setWindowTitle('')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def slot1(self):
        self.operand += '1'
        self.lcd.display(self.operand)

    def slot2(self):
        self.operand1 = self.lcd.value()
        self.operand = ''
        self.operator = self.btn2.text()

    # AC 버튼이 클릭됬을 경우
    # - 선택된 operator 버튼이 선택 해제 & operator 초기화
    # - 모든 operand 값 초기화
    ## AC 버튼을 누르면 선택된 operator 버튼의 선택을 해제시키기 위해서는
    ## AC 버튼도 상태 구분을 setCheckable(True)로 설정해줘야 하는가?
    def slot3(self):
        self.operand = ''
        self.lcd.display(0)
        self.operand1 = 0
        self.operand2 = 0
        self.operator = ''
        ## 일단, AC 버튼이 눌리면 모든 operator 버튼에 setChecked(False) 옶션을 지정해보자.
        ## 이러한 솔루션이 완전하지 않다는 정도만 알겠다. 그 이상의 해결법은 잘 모르겠다.

        ### btn4에 교수님께서 적용하신 방법론을 이해하지 못한 상태로 적용함
        ### 적용 결과 원하는 대로 작동함을 확인함.
        ### 교수님 방법론을 이해해보자.
        ### - setAutoExclusive란 무엇인가?
        ### : 버튼의 배타성 여부, 즉 한 버튼을 선택할 시 다른 버튼을
        ###   선택 취소할지 여부입니다.
        ###   In an exclusive button group, only one button can be checked at any time;
        ###   checking another button automatically unchecks the previously checked one.
        ### - setCheckable이란 무엇인가?
        ### : 버튼이 체크 가능한 형태로 할지 여부입니다.
        ### - setChecked란 무엇인가?
        ### : 버튼의 체크 상태여부를 지정할 수 있습니다.
        ### - isChecked란 무엇인가?
        ### - 왜 slot4에서 btn4에만 setAutoExclusive(False), setChecked(False), setAutoExclusive(True)를 하셨는가?
        self.btn2.setAutoExclusive(False)
        self.btn2.setChecked(False)
        self.btn2.setAutoExclusive(True)

    def slot4(self):
        self.operand2 = self.lcd.value()
        if self.operator == '+':
            rst = int(self.operand1) + int(self.operand2)
        self.lcd.display(rst)

        # initialize
        self.operand1 = 0
        self.operand2 = 0
        self.operand = ''

        # slot4 내부에서 btn4를 exclusive button group으로부터
        # 빼버리는 코드 elf.btn4.setAutoExclusive(False)를 넣으신 이유?
        self.btn4.setAutoExclusive(False)
        # btn4가 클릳되면 setCheckable(True)라
        # 선택 상태로 전환될 것 같지만
        # setChecked(False)가 slot4에 있기 때문에
        # btn4가 선택된 상태를 볼 수 없다고 생각한다.
        self.btn4.setChecked(False)
        self.btn4.setAutoExclusive(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

