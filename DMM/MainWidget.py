# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import Qt, QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QMessageBox
import sqlite3
from sqlite3 import Error
import subprocess

from Config import _App
from Config import APP_STATE


class SignalTrigger(QObject):

    # Define a new signal called 'trigger' that has no arguments.
    chanage_app_state = pyqtSignal()

    def connect_and_emit_trigger(self):
        # Connect the trigger signal to a slot.
        self.chanage_app_state.connect(self.handle_trigger)

        # Emit the signal.
        self.chanage_app_state.emit(APP_STATE.STATE_SCAN_BARCODE)

    def handle_trigger(self):
        # Show that the slot has been called.

        print("trigger signal received")

class MainWidget(QtWidgets.QWidget):
    def __init__(self, MainWindow):
        super(MainWidget, self).__init__()
        uic.loadUi('mainwidget.ui', self)
        #self.mainWidget = QtWidgets.QWidget()
        #self.setupUi(self.mainWidget)

        self.MainWindow = MainWindow

        self.CURRENT_WEIGHT = 0
        self.CURRENT_UOM = ''
        self.CURRENT_LID = ''
        self.CURRENT_SID = ''

        self.setFont()

        self.icon_login = QtGui.QPixmap("res/gui/button_login.png")
        self.icon_logout = QtGui.QPixmap("res/gui/button_logout.png")

        try:
            self.btnLogin.clicked.disconnect()
        except:
            pass

        self.btnTools.clicked.connect(self.MainWindow.setToolsWidget)
        self.btnSetup.clicked.connect(self.MainWindow.setBasicSettingWidget)     
        self.btnLogin.clicked.connect(self.on_btnLogin_clicked)
        self.btnSetRWT.clicked.connect(self.on_btnRwt_clicked)

        self.signals = SignalTrigger()
        self.signals.chanage_app_state.connect(self.setAppState)

    #@QtCore.pyqtSlot(APP_STATE)
    def changeAppState(self):
        self.signals.chanage_app_state.emit()

    @QtCore.pyqtSlot()
    def setAppState(self):
        if _App.APPSTATE == APP_STATE.STATE_NEED_TRUCKID:
            self.setMessageText("PLEASE SET TRUCK ID")
            self.setActiveLiftText("SET TRUCK ID")
            self.updateWeightText("TRUCKID", "")
            self.updateNoneCodeImage()
            self.btnLogin.setVisible(False)
            self.btnSetRWT.setVisible(True)
        
        if _App.APPSTATE == APP_STATE.STATE_NEED_LOGIN:
            self.setMessageText("PLEASE LOGIN")
            self.setActiveLiftText("PLEASE LOGIN")
            self.updateWeightText("LOGIN", "")
            self.updateNoneCodeImage()
            self.btnLogin.setVisible(True)
            self.btnSetRWT.setVisible(False)

        if _App.APPSTATE == APP_STATE.STATE_BEGIN_LIFT:
            self.setMessageText("PLEASE BEGIN LIFT")
            self.setActiveLiftText("NO LOAD")
            self.updateWeightText("NO LOAD", "")
            self.updateNoneCodeImage()
            self.btnLogin.setVisible(True)
            self.btnSetRWT.setVisible(False)
        
        if _App.APPSTATE == APP_STATE.STATE_SCAN_BARCODE:
            self.setMessageText("PLEASE SCAN BARCODE OF ITEMS")
            #self.setActiveLiftText("")
            self.setLiftIDText(self.CURRENT_LID)
            self.btnLogin.setVisible(True)
            self.btnSetRWT.setVisible(False)

    def setFont(self):
        QFontDatabase.addApplicationFont("./res/font/DJB Get Digital.ttf")
        your_ttf_font = QFont("DJB Get Digital", 65)
        # your_ttf_font.setBold(True)
        self.lblWeight.setFont(your_ttf_font)
        self.lblActiveLift.setFont(your_ttf_font)
        # DMMMainUI.closeEvent(self.closeEvent1)

    def on_btnLogin_clicked(self):
        if _App.LoginState == True:
            _App.LoginID = ''
            _App.LoginState = False
            self.btnLogin.setIcon(QtGui.QIcon(self.icon_login))
        else:
            r = self.MainWindow.showKeyboard(_App.LoginID, "Input your Login ID")
            if r and _App.KEYBOARD_TEXT[0] != '':
                _App.LoginID = _App.KEYBOARD_TEXT[0]
                _App.LoginState = True
                self.btnLogin.setIcon(QtGui.QIcon(self.icon_logout))

                _App.APPSTATE = APP_STATE.STATE_BEGIN_LIFT
                self.changeAppState()
                #self.setAppState()
                #self.updateWeightText("", "")

    def on_btnRwt_clicked(self):
        r = self.MainWindow.showKeyboard('', "Enter Truck ID")
        if r:
            if _App.KEYBOARD_TEXT[0] == '':
                _App._Settings.TRUCK_ID = ''
            else:
                new_id = "WP-" + _App.KEYBOARD_TEXT[0]

                if new_id == _App._Settings.TRUCK_ID:
                    return

                try:
                    #subprocess.run(['sudo', _App.APP_PATH + '/change_hostname.sh', new_id])
                    #subprocess.run(['./change_hostname.sh',  new_id])
                    subprocess.call(['sh', './change_hostname.sh', new_id])
                    #subprocess.call(['hostname', truckid])
                    
                    _App._Settings.TRUCK_ID = new_id

                    reply = QMessageBox.question(None, "Reboot System", "Sytem Reboot Required?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                    if reply == QMessageBox.Yes:
                        _App._Settings.save()
                        os.system('sudo shutdown -r now')
                except:
                    print('Hostname Edit Failed')
    
    def setMessageText(self, message):
        self.lblMessage.setText(message)

    def setActiveLiftText(self, message):
        self.lblActiveLift.setVisible(True)
        self.lblLiftID.setVisible(False)
        self.listBarcodes.setVisible(False)

        self.lblActiveLift.setText(message)
    
    def setLiftIDText(self, message):
        self.lblLiftID.setVisible(True)
        self.listBarcodes.setVisible(True)
        self.lblActiveLift.setVisible(False)

        self.lblLiftID.setText(message)

    def updateTimeText(self, timestamp):
        self.lblDateTime.setText(timestamp)

    def updateWeightText(self, weight, unit):
        self.lblWeight.setText(weight)
        self.lblUnit.setText(unit)

    def updateBarCodeImage(self, img):
        im = img.convert("RGB")
        data = im.tobytes("raw", "RGB")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qim)
        # pixmap = QPixmap('./res/img/barcode_resized.jpg')
        self.lblBarcode.setPixmap(pixmap)

    def updateQrCodeImage(self, img):
        im = img.convert("RGB")
        data = im.tobytes("raw", "RGB")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qim)
        # pixmap = QPixmap('./res/img/qrcode_resized.jpg')
        self.lblBarcode.setPixmap(pixmap)
    
    def updateNoneCodeImage(self):
        self.lblBarcode.clear()

    def setWifiLoading(self):
        movie = QtGui.QMovie("res/gui/loader.gif")
        self.lblWifi.setMovie(movie)
        movie.start()
    
    def setWifiIcon(self):
        if _App.WIFI_CONNECTION is True:
            self.lblWifi.setPixmap(QtGui.QPixmap("res/gui/wifi.png"))
        elif _App.WIFI_CONNECTION is False:
            self.lblWifi.setPixmap(QtGui.QPixmap("res/gui/wifi-disabled.png"))

    def insertDB(self, data):
        if _App.LoginState == False or _App._Settings.TRUCK_ID == '':
            return

        stat = False
        try:
            conn = sqlite3.connect('./res/db/weightrpi.db')
            sql = 'INSERT INTO tbl_weight_info(truckid, weight, measurement, barcode, scantype, recorded) VALUES (?,?,?,?,?,?)'
            cur = conn.cursor()
            cur.execute(sql, data)
            conn.commit()
            stat = True
        except Error as e:
            print(e)
            stat = False
        finally:
            conn.close()

        print('Data Stored')
        return stat

    def insertNewFBItem(self, LID, FB_ID):
        is_new = False

        try:
            conn = sqlite3.connect('./res/db/weightrpi.db')
            cur = conn.cursor()

            cur.execute("SELECT COUNT(*) FROM tbl_weight_info WHERE lift_id=:LID AND fb_item_barcode=:BARCODE", {"LID": LID, "BARCODE": FB_ID})
            exist_one = cur.fetchone()

            if exist_one[0] == 0:
                is_new = True
                SCAN_ID = "{}-{}".format(_App._Settings.TRUCK_ID, FB_ID)
                data = [_App._Settings.TRUCK_ID, LID, SCAN_ID, FB_ID, self.CURRENT_WEIGHT, self.CURRENT_UOM, _App.getDateTimeStamp("%m/%d/%Y %H:%M:%S")]
                cur.execute("INSERT INTO tbl_weight_info(truck_id, lift_id, scan_id, fb_item_barcode, fb_weight, uom, datetime) VALUES (?,?,?,?,?,?,?)", data)
                conn.commit()

        except Error as e:
            print(e)
            return is_new
        finally:
            conn.close
            return is_new


    def setNewLift(self, weight, weightmode):
        self.CURRENT_WEIGHT = weight
        self.CURRENT_UOM = weightmode
        self.updateWeightText(str(weight), weightmode)
        self.generateLID()

        _App.APPSTATE = APP_STATE.STATE_SCAN_BARCODE
        self.changeAppState()
        #self.setAppState()
    
    def generateLID(self):
        datetime = _App.getDateTimeStamp("%Y%m%d%H%M%S")
        self.CURRENT_LID = "{}-{}".format(_App._Settings.TRUCK_ID, datetime)
        #self.setLiftIDText(self.CURRENT_LID)
        self.listBarcodes.clear()
        #self.setActiveLiftText(self.CURRENT_LID)

    def addFBItem(self, barcode):
        new_fbitem = barcode

        if self.insertNewFBItem(self.CURRENT_LID, new_fbitem):
            self.listBarcodes.addItem("{}\t(New Scan)".format(new_fbitem))
        else:
            self.listBarcodes.addItem("{}\t(Already Scan)".format(new_fbitem))
        self.listBarcodes.scrollToBottom()
        
            
