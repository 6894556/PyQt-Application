# Model=View-Controller(MVC) desing pattern
# - model : handles the input values and the calculations
# - view : the calculator window on screen
# - controller : will receive the target math expression from the gui,
# ask the model to perform calculations, and update the gui with the result.
'''calculator's view'''
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow,
    QGridLayout, QVBoxLayout,
    QWidget, QLineEdit, QPushButton,
    )

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

def main():
    # pycalc2.py's main function
    pycalcApp = QApplication([])
    pycalcWindow = PyCalcWindow()
    pycalcWindow.show()
    sys.exit(pycalcApp.exec())

if __name__ == '__main__':
    main()