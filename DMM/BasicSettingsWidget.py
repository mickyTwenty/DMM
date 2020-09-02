from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QPainter
import CodeModeDialog
import WifiConfigDialog
import sys

from Config import _App

class BasicSettingsWidget(QtWidgets.QWidget):
    def __init__(self, MainWindow):
        super(BasicSettingsWidget, self).__init__()
        uic.loadUi('basicsettingwidget.ui', self)

        self.MainWindow = MainWindow

        self.btnBack.clicked.connect(self.MainWindow.setMainWidget)
        self.btnHome.clicked.connect(self.MainWindow.setMainWidget)

        self.btnWeightcode.clicked.connect(self.slotCodeClicked)
        self.btnWifi.clicked.connect(self.slotWifiClicked)
        

        self.icon_0 = QtGui.QIcon(QtGui.QPixmap("res/gui/settings_code_none.png"))
        self.icon_1 = QtGui.QIcon(QtGui.QPixmap("res/gui/settings_code_bar.png"))
        self.icon_2 = QtGui.QIcon(QtGui.QPixmap("res/gui/settings_code_qr.png"))

        if _App._Settings.WEIGHTCODE == 'BARCODE':
            self.btnWeightcode.setIcon(self.icon_1)
        elif _App._Settings.WEIGHTCODE == 'QRCODE':
            self.btnWeightcode.setIcon(self.icon_2)
        else:
            self.btnWeightcode.setIcon(self.icon_0)


    def slotCodeClicked(self):
        diag = CodeModeDialog.CodeModeDialog()
        r = diag.exec_()
        if r:
            if _App._Settings.WEIGHTCODE == 'BARCODE':
                self.btnWeightcode.setIcon(self.icon_1)
            elif _App._Settings.WEIGHTCODE == 'QRCODE':
                self.btnWeightcode.setIcon(self.icon_2)
            else:
                self.btnWeightcode.setIcon(self.icon_0)

    def slotWifiClicked(self):
        diag = WifiConfigDialog.WifiConfigDialog(self)
        r = diag.exec_()

    def paintEvent(self, event):        
        qp = QPainter()
        qp.begin(self)
        qp.end()
