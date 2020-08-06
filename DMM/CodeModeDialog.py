from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

class CodeModeDialog(QtWidgets.QDialog):
    def __init__(self, MainWindow):
        super(CodeModeDialog, self).__init__()
        uic.loadUi('codemodedialog.ui', self)

        self.MainWindow = MainWindow
