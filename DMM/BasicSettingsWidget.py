from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtGui import QPainter, QTextDocument, QPixmap
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QSizeF, QSize, QRectF, QRect
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
        diag.exec_()
        

    def paintEvent(self, event):
        self.drawButtons()

    def drawButtons(self):
        self.drawWifiButton()
        

    def drawWifiButton(self):
        html = ""
        if _App.WIFI_CONNECTION is False:
            html = "<div style='text-align: center;color: #d5d58c;font-size: 36px'>WiFi</div><div style='text-align: center;color: #b51a00;font-size: 16px;margin-top: 20px;'>NOT CONNECTED</div>"
        else:
            html = "<div style='text-align: center;color: #d5d58c;font-size: 36px'>WiFi</div><div style='text-align: center;color: #00c421;font-size: 16px;margin-top: 20px;'>{}}</div>".format(_App.WIFI_SSID)


        self.drawContents(self.btnTemp, html)

    def drawContents(self, button, html):
        text = QTextDocument()
        text.setHtml(html)
        text.setTextWidth(150)

        pixmap = QPixmap(150, 100)
        pixmap.fill( QtCore.Qt.transparent )
        painter = QPainter(pixmap)
        text.drawContents(painter)

        button.setIcon(QtGui.QIcon(pixmap))
        button.setIconSize(QSize(160, 120))
        painter.end()
