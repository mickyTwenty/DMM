from PyQt5 import QtCore, QtGui, QtWidgets, uic
import os
import time
from subprocess import check_output
import subprocess

from Config import _App

class WifiConfigDialog(QtWidgets.QDialog):
    def __init__(self):
        super(WifiConfigDialog, self).__init__()
        uic.loadUi('wificonfigdialog.ui', self)

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WA_ShowWithoutActivating)
        self.setModal(True)

        #self.getWIFIList()
        self.listWidget.addItems(self.getWIFIList())

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
                    # if line[:5]  == "ESSID":
                    #  ssid = line.split('"')[1]
                    if line.startswith("ESSID"):
                        eid = line.split('\"')[1]
                        if eid not in ssid:
                            ssid.append(eid)
            return ssid
        except:
            return []
    