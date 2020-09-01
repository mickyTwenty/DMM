from PyQt5 import QtCore, QtGui, QtWidgets, uic
import os
import time
from subprocess import check_output
import subprocess
import threading
from wireless import Wireless

from Config import _App

wireless = Wireless()

class WifiConfigDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(WifiConfigDialog, self).__init__()
        uic.loadUi('wificonfigdialog.ui', self)

        self.parent = parent

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WA_ShowWithoutActivating)
        self.setModal(True)

        try:
            self.btnConnect.clicked.disconnect()
        except:
            pass

        self.btnConnect.clicked.connect(self.on_btnConnect_clicked)

        t = threading.Thread(target=self.initListWidget)
        t.daemon = True
        t.start()
        
    def initListWidget(self):
        self.listWidget.setEnabled(False)
        self.btnConnect.setEnabled(False)

        self.listWidget.clear()
        self.listWidget.addItems(self.getWIFIList())

        self.listWidget.setEnabled(True)
        self.btnConnect.setEnabled(True)

    def on_btnConnect_clicked(self):
        if ( self.listWidget.currentItem() is None ):
            return
        
        ssid = self.listWidget.currentItem().text()
        
        r = self.parent.MainWindow.showKeyboard(None, "Input wifi access password: " + ssid, QtWidgets.QLineEdit.Password)

        if r:
            pwd = _App.KEYBOARD_TEXT[0]
            try:
                print('connecting to wifi', ssid, '---', pwd)

                if len(ssid) > 0 and len(pwd) > 0:
                    wireless.connect(ssid = ssid, password = pwd)
                elif len(ssid) > 0 and len(pwd) == 0:
                    wireless.connect(ssid = ssid, password = '')
                else:
                    print('NOT CONNECTING')
                
            except Exception as ex:
                print('WIFI CON ERROR:', ex)

    def getWIFIList(self):
        try:
            scanoutput = check_output(["iwlist", "wlan0", "scan"])

            ssid = []

            for line in scanoutput.split():
                line = line.decode("utf-8")
                # print(line)
                # if line[:5]  == "ESSID":
                #  ssid = line.split('"')[1]
                if line.startswith("ESSID"):
                    eid = line.split('\"')[1]
                    if eid not in ssid:
                        ssid.append(eid)
            if len(ssid) < 1:
                os.system('sudo ifconfig wlan0 down')
                os.system('sudo ifconfig wlan0 up')
                time.sleep(1)
                scanoutput = check_output(["iwlist", "wlan0", "scan"])

                ssid = []

                for line in scanoutput.split():
                    line = line.decode("utf-8")
                    # print(line)
                    # if line[:5] == "ESSID":
                    #  ssid = line.split('"')[1]
                    if line.startswith("ESSID"):
                        eid = line.split('\"')[1]
                        if eid not in ssid:
                            ssid.append(eid)
            return ssid
        except:
            return []
    