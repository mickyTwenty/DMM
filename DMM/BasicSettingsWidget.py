from PyQt5 import QtCore, QtGui, QtWidgets, uic
import CodeModeDialog
import sys

class BasicSettingsWidget(QtWidgets.QWidget):
    def __init__(self, MainWindow):
        super(BasicSettingsWidget, self).__init__()
        uic.loadUi('basicsettingwidget.ui', self)

        self.MainWindow = MainWindow

        self.btnBack.clicked.connect(self.MainWindow.setMainWidget)
        self.btnHome.clicked.connect(self.MainWindow.setMainWidget)

        self.btnWeightcode.clicked.connect(self.slotCodeClicked)


    def slotCodeClicked(self):
        diag = CodeModeDialog.CodeModeDialog()
        diag.exec_()