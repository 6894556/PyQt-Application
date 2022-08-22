# five-v1.2까지 완성한 상태이다.
# LCD 패널 한개로 계산기를 구현하고자 했다.
# 하지만 LCD 패널 한개로는 사칙연산이 가능한 계산기를 구현할 수 없다.
# QLCDNumer : https://doc.qt.io/qt-6/qlcdnumber.html
# 위 문서를 확인해본 결과 float도 표현이 가능할 수 있겠다고 생각했다.
# 따라서 QLCDBumer instance의 모든 설정값이 기본값이라는 가정 하에
# LCD 패널 한개로 사칙연산이 가능한 계산기를 구현할 수 없다는 결론을 얻었다.

# division is not closed on the set of integers.
# LCD 패널 한개로 를 할 수 없다.

# 입력 받을 피연산자 개수 : 두개
# 입력 받을 연산자 개수 : 한개
# 가능한 연산 : 덧셈, 곱셈, 뺄셈
# 나눗셈을 제외시킨 이유 : 연산의 결과값을 정수범위로 제한하기 위함
# 추가할 버튼 : AC버튼, 괄호버튼, 백버튼

# 추가한 버튼을 테스트할 때 필요한 버튼들
# - AC버튼 : 1버튼, +버튼, =버튼
# - 괄호버튼 : 1버튼, +버튼, =버튼
# - 백버튼 : 1버튼, +버튼, =버튼


# https://stackoverflow.com/questions/701802/how-do-i-execute-a-string-containing-python-code-in-python

# 무언가 입력된 상태면 ac가 아닌 c, 입력값이 초기값과 같은 상태면 ac