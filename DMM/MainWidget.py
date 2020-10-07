# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import Qt, QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import pyqtSignal, QObject, QMutex, QSize, QRect
from PyQt5.QtGui import QFontDatabase, QFont, QColor, QFontMetrics, QPainter, QTextDocument, QPixmap, QImage
from PyQt5.QtWidgets import QMessageBox, QListWidgetItem
import subprocess

from Config import _App
from Config import APP_STATE
from DBHelper import _DB

LOG_PAGE_SIZE = 5


class SignalTrigger(QObject):

    # Define a new signal called 'trigger' that has no arguments.
    chanage_app_state = pyqtSignal()
    new_item_scanned = pyqtSignal(str)
    new_lift_set = pyqtSignal(str, str, object, object)
    new_transaction_set = pyqtSignal(str, object)
    code_mode_changed = pyqtSignal()

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

        self.CURRENT_WEIGHT = ''
        self.CURRENT_UOM = ''
        self.CURRENT_BARIMG = None
        self.CURRENT_QRIMG = None

        self.CURRENT_LID = ''
        self.CURRENT_FBID = ''

        self.message_queue = []
        self.message_mutex = QMutex()

        self.LOG_SCROLL_ITEM = 0

        self.setFont()

        #self.icon_login = QtGui.QPixmap("res/gui/button_login.png")
        #self.icon_logout = QtGui.QPixmap("res/gui/button_logout.png")

        try:
            self.btnLogin.clicked.disconnect()
            self.btnLogup.clicked.disconnect()
            self.btnLogdown.clicked.disconnect()
        except:
            pass

        self.btnTools.clicked.connect(self.MainWindow.setToolsWidget)
        self.btnSetup.clicked.connect(self.MainWindow.setBasicSettingWidget)     
        self.btnLogin.clicked.connect(self.on_btnLogin_clicked)
        self.btnSetRWT.clicked.connect(self.on_btnRwt_clicked)

        self.btnLogup.clicked.connect(self.on_btnLogup_clicked)
        self.btnLogdown.clicked.connect(self.on_btnLogdown_clicked)

        self.signals = SignalTrigger()
        self.signals.chanage_app_state.connect(self.setAppState)
        self.signals.new_item_scanned.connect(self.addFBItem)
        self.signals.new_lift_set.connect(self.setNewLift)
        self.signals.new_transaction_set.connect(self.setNewTransaction)
        self.signals.code_mode_changed.connect(self.updateWeightImage)

    def changeAppState(self):
        self.signals.chanage_app_state.emit()

    def newItemScanned(self, barcode):
        self.signals.new_item_scanned.emit(barcode)

    def newLiftSet(self, weight, uom, barimg, qrimg):
        self.signals.new_lift_set.emit(weight, uom, barimg, qrimg)

    def newTransactionSet(self, LID, data):
        self.signals.new_transaction_set.emit(LID, data)

    def changeCodeMode(self):
        self.signals.code_mode_changed.emit()

    @QtCore.pyqtSlot()
    def setAppState(self):
        if _App.APPSTATE == APP_STATE.STATE_NEED_TRUCKID:
            self.setMessageText("PLEASE SET TRUCK ID")
            self.setActiveLiftText("SET TRUCK ID")
            self.updateWeightText("TRUCKID", "")
            #self.updateNoneCodeImage()
            self.btnLogin.setVisible(False)
            self.btnSetRWT.setVisible(True)
        
        if _App.APPSTATE == APP_STATE.STATE_NEED_LOGIN:
            self.setMessageText("PLEASE LOGIN")
            self.setActiveLiftText("PLEASE LOGIN")
            self.updateWeightText("LOGIN", "")
            #self.updateNoneCodeImage()
            self.btnLogin.setVisible(True)
            self.btnSetRWT.setVisible(False)

        if _App.APPSTATE == APP_STATE.STATE_BEGIN_LIFT:
            self.setMessageText("PLEASE BEGIN LIFT")
            self.setActiveLiftText("NO LOAD")
            self.updateWeightText("NO LOAD", "")
            #self.updateNoneCodeImage()
            self.btnLogin.setVisible(True)
            self.btnSetRWT.setVisible(False)
        
        if _App.APPSTATE == APP_STATE.STATE_SCAN_BARCODE:
            if self.CURRENT_FBID == '':
                self.setMessageText("Please SCAN FIRST item")
            else:
                self.setMessageText("Please SCAN next item(s)")
            #self.setActiveLiftText("")
            self.setLiftIDText(self.CURRENT_FBID)
            self.btnLogin.setVisible(True)
            self.btnSetRWT.setVisible(False)
        
        '''
        if len(self.message_queue) == 0 and _App.CLIENT_HOST_ALIVE is True:
            pending_lift = _DB.getPendingLift()
            if pending_lift is not None:
                #print("Processing Pending Lifts...")
                print("Call API for Pending Lift")
                self.message_mutex.lock()
                data = _DB.getFBItems(pending_lift)
                self.message_queue.append(pending_lift)
                self.message_queue.append(data)
                self.message_mutex.unlock()
                self.showMessage("info", "Processing Pending Lifts", 3)
        '''

    def setFont(self):
        QFontDatabase.addApplicationFont("./res/font/DJB Get Digital.ttf")
        your_ttf_font = QFont("DJB Get Digital", 65)
        # your_ttf_font.setBold(True)
        self.lblWeight.setFont(your_ttf_font)
        self.lblActiveLift.setFont(your_ttf_font)
        # DMMMainUI.closeEvent(self.closeEvent1)

    def on_btnLogin_clicked(self):
        if _App.LoginState == True:
            if self.isMessageEmpty() is True:
                _App.LoginID = ''
                _App.LoginState = False
                #self.btnLogin.setIcon(QtGui.QIcon(self.icon_login))
                self.btnLogin.setStyleSheet("background-image: url('res/gui/button_login.png')")
            else:
                self.showMessage("Info", "PENDING LIFTS, PLEASE WAIT...", 3)

        else:
            r = self.MainWindow.showKeyboard(_App.LoginID, "Input your Login ID")
            if r and _App.KEYBOARD_TEXT[0] != '':
                _App.LoginID = _App.KEYBOARD_TEXT[0]
                #_App._Settings.SAVED_USER = _App.LoginID
                _App.LoginState = True
                #self.btnLogin.setIcon(QtGui.QIcon(self.icon_logout))
                self.btnLogin.setStyleSheet("background-image: url('res/gui/button_logout.png')")

                _App.APPSTATE = APP_STATE.STATE_BEGIN_LIFT
                #self.changeAppState()
                self.setAppState()

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
        if _App.MESSAGE_ON is True:
            if _App.MESSAGE_TYPE == "Alert":
                self.lblMessage.setStyleSheet("color: rgb(255, 30, 30); font-size: 15px")
            else:
                self.lblMessage.setStyleSheet("color: rgb(255, 30, 30); font-size: 24px")
            self.lblMessage.setText(_App.MESSAGE_TEXT)
        else:
            self.lblMessage.setStyleSheet("color: rgb(255, 228, 30); font-size: 24px")
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
        self.updateWeightImage()

    @QtCore.pyqtSlot()
    def updateWeightImage(self):
        if self.CURRENT_WEIGHT == "" or self.CURRENT_UOM == "" or _App._Settings.WEIGHTCODE is None:
            self.lblBarcode.clear()
        elif _App._Settings.WEIGHTCODE == 'BARCODE':
            self.lblBarcode.setPixmap(self.CURRENT_BARIMG)
        elif _App._Settings.WEIGHTCODE == 'QRCODE':
            self.lblBarcode.setPixmap(self.CURRENT_QRIMG)
        '''
        if _App._Settings.WEIGHTCODE == 'BARCODE':
            self.GUI.updateBarCodeImage(barimg)
        elif _App._Settings.WEIGHTCODE == 'QRCODE':
            self.GUI.updateQrCodeImage(qrimg)
        else:
            self.GUI.updateNoneCodeImage()
        '''

    def updateBarCodeImage(self, img):
        self.lblBarcode.setPixmap(img)

    def updateQrCodeImage(self, img):
        self.lblBarcode.setPixmap(img)

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

    @QtCore.pyqtSlot(str, str, object, object)
    def setNewLift(self, weight, weightmode, barimg=None, qrimg=None):
        if self.CURRENT_LID != "" and self.CURRENT_FBID != "":
            print("Call API")
            self.message_mutex.lock()
            data = _DB.getFBItems(self.CURRENT_LID)
            self.message_queue.append(self.CURRENT_LID)
            self.message_queue.append(data)
            self.message_mutex.unlock()
        
        if weight == 0:
            self.CURRENT_WEIGHT = ""
            self.CURRENT_UOM = ""
            self.CURRENT_BARIMG = None
            self.CURRENT_QRIMG = None

            self.CURRENT_LID = ""
            self.CURRENT_FBID = ""

            _App.APPSTATE = APP_STATE.STATE_BEGIN_LIFT
            #self.changeAppState()
            self.setAppState()
            
        else:
            self.CURRENT_WEIGHT = weight
            self.CURRENT_UOM = weightmode
            self.CURRENT_BARIMG = barimg
            self.CURRENT_QRIMG = qrimg
            self.updateWeightText(weight, weightmode)
            
            self.CURRENT_LID = self.generateLID()

            self.CURRENT_FBID = ''

            _DB.insertNewLift([_App._Settings.TRUCK_ID, self.CURRENT_LID, self.CURRENT_FBID, self.CURRENT_WEIGHT, self.CURRENT_UOM, _App.LoginID, self.generateTID(), _App.getDateTimeStamp("%m/%d/%Y %H:%M:%S")])

            _App.APPSTATE = APP_STATE.STATE_SCAN_BARCODE
            #self.changeAppState()
            self.setAppState()

        self.listBarcodes.clear()
    
    def generateLID(self):
        datetime = _App.getDateTimeStamp("%Y%m%d%H%M%S")
        return "{}-{}".format(_App._Settings.TRUCK_ID, datetime)
        #self.setLiftIDText(self.CURRENT_LID)
        #self.setActiveLiftText(self.CURRENT_LID)

    def generateTID(self):
        datetime = _App.getDateTimeStamp("%Y%m%d%H%M%S")
        return "TRANS-{}-{}".format(_App._Settings.TRUCK_ID, datetime)

    @QtCore.pyqtSlot(str)
    def addFBItem(self, barcode):
        new_fbitem = barcode
        
        new_fbid = new_fbitem.split("-")[0]

        if self.CURRENT_FBID == "":
            self.CURRENT_FBID = new_fbid
            self.setLiftIDText(new_fbid)
            _DB.setFBId(self.CURRENT_LID, self.CURRENT_FBID)

        if self.CURRENT_FBID != new_fbid:
            self.showMessage("Alert", "MULTIPLE FRIEGHT BILLS NOT ALLOWED. PLEASE RE-LIFT", 5)
            self.setNewLift(0, "")
        
        SCAN_ID = "{}-{}".format(_App._Settings.TRUCK_ID, new_fbitem)

        #if self.insertNewFBItem(self.CURRENT_LID, new_fbitem):
        if _DB.insertNewFBItem([self.CURRENT_LID, SCAN_ID, new_fbitem, _App.getDateTimeStamp("%m/%d/%Y %H:%M:%S")]):
            self.listBarcodes.addItem(new_fbitem)
            #self.setMessageText("PLEASE SCAN BARCODE OF ITEMS")
        else:
            #self.listBarcodes.addItem("{}\t(Already Scanned)".format(new_fbitem))
            #self.setMessageText("Already Scanned Item")
            self.showMessage("Warning", "Already Scanned Item", 2)
            print("Already Scanned")
        self.listBarcodes.scrollToBottom()

    @QtCore.pyqtSlot(str, object)
    def setNewTransaction(self, LID, data):
        #if data != False:
        lift = _DB.setLiftTransaction(LID, data)
        self.addLogItem(lift)
        '''
        if data is False:
            #self.listLog.addItem(data["FreightBill"] + "\tFailed")
            print("Connection problem")
            
        else:
            if data["IsSuccess"] is True:
                #self.listLog.addItem(data["FreightBill"] + "\tOK")
                self.addLogItem(data)
            else:
                #self.listLog.addItem(data["FreightBill"] + "\tScenario: {}".format(data["WeightApplication"]))
                self.addLogItem(data)

        self.listLog.scrollToBottom()
        '''

    def addLogItem(self, item):
        i = QListWidgetItem()
        if item[1] == 1 or item[1] == 2:
            i.setText("FB # {}\t{}".format(item[0], "OK"))
            i.setBackground(QColor("#00b050"))
        elif item[1] == 0:
            i.setText("FB # {}\t{}".format(item[0], "RETRY"))
            i.setBackground(QColor("#c00000"))
        elif item[1] == 3:
            i.setText("FB # {}\t{}".format(item[0], "WAITING"))
            i.setBackground(QColor("#ffa500"))
        elif item[1] == 404:
            i.setText("FB # {}\t{}".format(item[0], "FAILED"))
            i.setBackground(QColor("#c00000"))

        if item[1] == 4:
            return
            
        self.listLog.addItem(i)
        if self.LOG_SCROLL_ITEM == self.listLog.count() - 1:
            self.LOG_SCROLL_ITEM += 1
        self.logScroll()

        if self.listLog.count() > 100:
            if self.LOG_SCROLL_ITEM == self.listLog.count():
                self.LOG_SCROLL_ITEM -= 1
            self.listLog.takeItem(0)

        #if self.LOG_SCROLL_ITEM == 

    def logScroll(self):
        item = self.listLog.item(self.LOG_SCROLL_ITEM - 1)
        self.listLog.scrollToItem(item, QtWidgets.QAbstractItemView.PositionAtBottom)
            
    def on_btnLogup_clicked(self):
        if self.LOG_SCROLL_ITEM > LOG_PAGE_SIZE:
            self.LOG_SCROLL_ITEM -= 1
        self.logScroll()

    def on_btnLogdown_clicked(self):
        if self.LOG_SCROLL_ITEM < self.listLog.count():
            self.LOG_SCROLL_ITEM += 1
        self.logScroll()

    def paintEvent(self, event):
        self.drawLogoutButton()
    
    def drawLogoutButton(self):
        html = ""
        if _App.LoginState == True:
            html = "<div>&nbsp;</div><div style='text-align: left;color: #b51a00;font-size: 22px;margin-top: 0px;margin-left: 5px;font-weight: 600;'>{}</div>".format(_App.LoginID)

        self.drawContents(self.btnLogin, html)

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

    def showMessage(self, msg_type, msg_text, duration):
        _App.MESSAGE_ON = True
        _App.MESSAGE_TYPE = msg_type
        _App.MESSAGE_TEXT = msg_text
        _App.MESSAGE_DURATION = duration

    def isMessageEmpty(self):
        ret = True
        self.message_mutex.lock()
        if len(self.message_queue) > 0:
            ret = False
        self.message_mutex.unlock()
        return ret