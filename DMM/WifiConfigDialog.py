from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

from Config import _App

class WifiConfigDialog(QtWidgets.QDialog):
    def __init__(self):
        super(WifiConfigDialog, self).__init__()
        uic.loadUi('wificonfigdialog.ui', self)

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WA_ShowWithoutActivating)
        self.setModal(True)
