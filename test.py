# v4 :
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QPushButton,
                             QVBoxLayout)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.turn = 0
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton('+', self)
        btn2.setEnabled(False)
        btn3 = QPushButton('=', self)


        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        self.setLayout(vbox)

        btn1.clicked.connect(self.slot1)
        btn2.clicked.connect(self.slot2)


        self.setWindowTitle('')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def slot1(self):
       self.btn1.setCheckable(True)


    def slot2(self):
        self.btn1.toggle()

    def slot3(self):
        self.btn3.setCheckable(False)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())