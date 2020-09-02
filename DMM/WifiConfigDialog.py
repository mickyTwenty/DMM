from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import os
import time
from subprocess import check_output
import subprocess
import threading
from wireless import Wireless

from Config import _App


class WifiConfigDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(WifiConfigDialog, self).__init__()
        uic.loadUi('wificonfigdialog.ui', self)

        self.parent = parent

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WA_ShowWithoutActivating)
        self.setModal(True)

        self.ssid = ''
        self.pwd = ''
        self.wireless = Wireless()

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
        self.btnAdd.setEnabled(False)
        self.btnConnect.setText("Loading...")

        self.listWidget.clear()
        self.listWidget.addItems(self.getWIFIList())

        self.listWidget.setEnabled(True)
        self.btnConnect.setEnabled(True)
        self.btnAdd.setEnabled(True)
        self.btnConnect.setText("Connect")

    def on_btnConnect_clicked(self):
        if ( self.listWidget.currentItem() is None ):
            return
        
        self.ssid = self.listWidget.currentItem().text()
        
        r = self.parent.MainWindow.showKeyboard(None, "Input wifi access password: " + self.ssid, QtWidgets.QLineEdit.Password)

        if r:
            self.pwd = _App.KEYBOARD_TEXT[0]

            t = threading.Thread(target=self.wifi_connect)
            t.daemon = True
            t.start()
            

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
    
    def wifi_connect(self):
        self.btnConnect.setEnabled(False)
        self.listWidget.setEnabled(False)
        self.btnAdd.setEnabled(False)
        self.btnConnect.setText("Connecting...")
        try:
            print('connecting to wifi', self.ssid, '---', self.pwd)

            if len(self.ssid) > 0 and len(self.pwd) > 0:
                self.wireless.connect(ssid = self.ssid, password = self.pwd)
            elif len(self.ssid) > 0 and len(self.pwd) == 0:
                self.wireless.connect(ssid = self.ssid, password = '')
            else:
                print('NOT CONNECTING')
            
            _App.WIFI_SSID = self.ssid
            _App.WIFI_PWD = self.pwd

            QMessageBox.information(None, "Wifi", "Wifi connected: " + self.ssid)

            self.btnConnect.setEnabled(True)
            self.listWidget.setEnabled(True)
            self.btnAdd.setEnabled(True)
            self.btnConnect.setText("Connect")

            return self.accept()
            
        except Exception as ex:
            print('WIFI CON ERROR:', ex)
            
            QMessageBox.warning(None, "Wifi", "Wifi connect faild: " + self.ssid)

            self.btnConnect.setEnabled(True)
            self.listWidget.setEnabled(True)
            self.btnAdd.setEnabled(True)
            self.btnConnect.setText("Connect")
    