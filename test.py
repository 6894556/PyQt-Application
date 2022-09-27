#  Clear Entry 버튼 구현 (카운터를 사용하지 않는 방식 탐구)

# 아이디어 :
# self.operand 가 초기값이 아닐 때
# self.oeprand1이 초기값이 아닐 때
# self.operand2가 초기값이 아닐 때
# self.btn2.isclicked()가 False를 리턴할 때


if self.count == 1:
    self.lcd.display(self.operand1)
    self.operand = ''

    self.btn2.setAutoExclusive(False)
    self.btn2.setChecked(True)
    self.btn2.setAutoExclusive(True)
elif self.count == 2:
    self.btn2.setAutoExclusive(False)
    self.btn2.setChecked(False)
    self.btn2.setAutoExclusive(True)
    self.operator = ''
elif self.count == 0:
    # self.btn3.setText('AC')0-\]-\
    7
    self.lcd.display(str(int(0)))
    print(self.count)
    self.operand1 = 0

## =버튼이 클릭 되기 전에 에서 CE버튼이 클릭 되면
if self.operand2 != 0.0:
    self.lcd.display(self.operand1)
elif self.operator != '':
elif self.operand1 != 0.0:
