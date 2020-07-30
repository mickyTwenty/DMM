from PyQt5 import QtWidgets, uic
import sys

class KeyboardWidget(QtWidgets.QWidget):
    def __init__(self, MainWindow):
        super(KeyboardWidget, self).__init__()
        uic.loadUi('keyboardwidget.ui', self)

        self.MainWindow = MainWindow

        self.key_reject.clicked.connect(MainWindow.hideKeyboard)