from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

class CodeModeDialog(QtWidgets.QDialog):
    def __init__(self):
        super(CodeModeDialog, self).__init__()
        uic.loadUi('codemodedialog.ui', self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WA_ShowWithoutActivating)
        self.setModal(True)
