
'''calculator's model'''
'''model will evaluate the math expression that uesers introduced in the gui'''
'''evaluateExpression is the calculator's model.'''
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QGridLayout, QVBoxLayout,
    QWidget, QLineEdit, QPushButton,
    )

ERRO_MSG = "ERROR"
WINDOW_SIZE = 235
DISPLAY_HEIGHT = 35
BUTTON_SIZE = 40

class PyCalcWindow(QMainWindow):
    # view of calculator
    def __init__(self):
        super().__init__()
        self.setWindowTitle('pycalc2')
        self.setFixedSize(WINDOW_SIZE, WINDOW_SIZE)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self._createDisplay()
        self._createButtons()

    def _createDisplay(self):
        self.display = QLineEdit()
        self.display.setFixedHeight(DISPLAY_HEIGHT)
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)

    def _createButtons(self):
        self.buttonMap = {}
        buttonsLayout = QGridLayout()
        keyBoard = [
            ['7', '8', '9', '/', 'c'],
            ['4', '5', '6', '*', '('],
            ['1', '2', '3', '-', ')'],
            ['0', '00', '.', '+', '=']
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = QPushButton(key)
                self.buttonMap[key].setFixedSize(BUTTON_SIZE, BUTTON_SIZE)
                buttonsLayout.addWidget(self.buttonMap[key], row, col)

        self.generalLayout.addLayout(buttonsLayout)

    def setDiaplayText(self, text):
        '''set the display's text'''
        self.display.setText(text)
        '''set the cursor's focus on the display'''
        self.display.setFocus()

    def displayText(self):
        '''get the display's text'''
        '''when user clicks the equal sign'''
        return self.display.text()

    def clearDisplay(self):
        '''clear the display'''
        '''when user clicks the cancel sign'''
        self.setDiaplayText("")

'''free to rework below function to make it more reliable and secure'''
def evaluateExpression(expression):
    '''Evaluate an expression (Model)'''
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERRO_MSG
    return result

def main():
    # pycalc2.py's main function
    pycalcApp = QApplication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    sys.exit(pycalcApp.exec())

if __name__ == '__main__':
    main()