# four-v1.7 :
# - 버튼 그룹 제거하고 각 버튼에 setAutoExculsive 사용해서
# - 세개 버튼 중 하나만 선택되도록 v1.6 수정
#
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QLCDNumber, QPushButton,
                             QHBoxLayout, QVBoxLayout, QButtonGroup)

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
        ############################# choijy  >>>>>>>>>>
        self.btn3.setCheckable(True)
        self.btn2.setCheckable(True)
        self.btn4.setCheckable(True)
        self.btn2.setAutoExclusive(True)
        self.btn3.setAutoExclusive(True)
        self.btn4.setAutoExclusive(True)
       ############################# choijy  <<<<<<<<<<<<

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

        self.setWindowTitle('four-v1.7')
        self.setGeometry(300, 300, 300, 200)
        self.show()




    def slot1(self):
        self.operand += '1'
        self.lcd.display(self.operand)


    def slot2(self):
        '''
         ############################# choijy  >>>>>>>>>>
         ## btn3의 상태에 관계 없이 구분을 없애기
         self.btn3.setCheckable(False)
         self.btn2.setCheckable(True)
         ## toggle()을 제거할 경우 btn2가 눌린 상태가 지속되지 않습니다.
         self.btn2.toggle()
         ############################# choijy  >>>>>>>>>>  '''
        self.operand1 = self.lcd.value()
        self.operand = ''
        self.operator = ''
        self.operator = self.btn2.text()

    def slot3(self):
        ## btn2의 상태에 관계 없이 구분을 없애기
        #self.btn2.setCheckable(False)
        #self.btn3.setCheckable(True)
        ## toggle()을 제거할 경우 btn3이 눌린 상태가 지속되지 않습니다.
        #self.btn3.toggle()
        self.operand1 = self.lcd.value()
        self.operand = ''

        self.operator = '' # 초기화
        self.operator = self.btn3.text()

    def slot4(self):
        ## 클릭된 버튼이 연산자 버튼 둘 중 어느 것인지 알 수 없으므로
        ## 모든 operator 버튼의 상태가 구분이 안되게 바꿔봤습니다.

        self.operand2 = self.lcd.value()
        if self.operator =='+':
            rst = int(self.operand1) + int(self.operand2)
        if self.operator == '-':
            rst = int(self.operand1) - int(self.operand2)
        self.lcd.display(rst)
        rst = 0
        self.operand1 = 0
        self.operand2 = 0
        self.btn4.setAutoExclusive(False)
        self.btn4.setChecked(False)
        self.btn4.setAutoExclusive(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())