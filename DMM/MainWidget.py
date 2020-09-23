# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtWidgets import QMessageBox
import sqlite3
from sqlite3 import Error
import subprocess

from Config import _App
from Config import APP_STATE

class MainWidget(object):
    def __init__(self, MainWindow):
        self.mainWidget = QtWidgets.QWidget()
        self.setupUi(self.mainWidget)

        self.MainWindow = MainWindow

        self.CURRENT_WEIGHT = 0
        self.CURRENT_LID = ''
        self.CURRENT_SID = ''

        self.setFont()

        self.icon_login = QtGui.QPixmap("res/gui/button_login.png")
        self.icon_logout = QtGui.QPixmap("res/gui/button_logout.png")

        self.btnTools.clicked.connect(self.MainWindow.setToolsWidget)
        self.btnSetup.clicked.connect(self.MainWindow.setBasicSettingWidget)     
        self.btnLogin.clicked.connect(self.on_btnLogin_clicked)
        self.btnSetRWT.clicked.connect(self.on_btnRwt_clicked)

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
                self.setAppState()
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

    def setNewLift(self, weight, weightmode):
        self.CURRENT_WEIGHT = weight
        self.updateWeightText(str(weight), weightmode)
        self.generateLID()

        _App.APPSTATE = APP_STATE.STATE_SCAN_BARCODE
        self.setAppState()
    
    def generateLID(self):
        datetime = _App.getDateTimeStamp("%Y%m%d%H%M%S")
        self.CURRENT_LID = "{}-{}".format(_App._Settings.TRUCK_ID, datetime)
        self.setLiftIDText(self.CURRENT_LID)
        #self.setActiveLiftText(self.CURRENT_LID)

    def setupUi(self, mainWidget):
        mainWidget.setObjectName("mainWidget")
        mainWidget.resize(1024, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWidget.sizePolicy().hasHeightForWidth())
        mainWidget.setSizePolicy(sizePolicy)
        mainWidget.setMinimumSize(QtCore.QSize(1024, 600))
        mainWidget.setMaximumSize(QtCore.QSize(1024, 600))
        mainWidget.setStyleSheet("QWidget#mainWidget { background-color: black; }\n"
"QToolButton { background: transparent; }")
        self.gridLayout = QtWidgets.QGridLayout(mainWidget)
        self.gridLayout.setContentsMargins(5, 8, 8, 6)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.scaleWidget = QtWidgets.QWidget(mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scaleWidget.sizePolicy().hasHeightForWidth())
        self.scaleWidget.setSizePolicy(sizePolicy)
        self.scaleWidget.setMinimumSize(QtCore.QSize(521, 207))
        self.scaleWidget.setMaximumSize(QtCore.QSize(521, 207))
        self.scaleWidget.setStyleSheet("QWidget #scaleWidget {border: 3px solid rgb(32, 125, 198);}")
        self.scaleWidget.setObjectName("scaleWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scaleWidget)
        self.verticalLayout_3.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.scaleWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 34))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 34))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background: rgb(6, 57, 71);color: rgb(241, 187, 2);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblBarcode = QtWidgets.QLabel(self.scaleWidget)
        self.lblBarcode.setMinimumSize(QtCore.QSize(225, 165))
        self.lblBarcode.setMaximumSize(QtCore.QSize(225, 165))
        self.lblBarcode.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBarcode.setObjectName("lblBarcode")
        #self.lblBarcode.setStyleSheet("background-color:red")
        self.horizontalLayout_3.addWidget(self.lblBarcode)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.lblWeight = QtWidgets.QLabel(self.scaleWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblWeight.sizePolicy().hasHeightForWidth())
        self.lblWeight.setSizePolicy(sizePolicy)
        self.lblWeight.setMinimumSize(QtCore.QSize(280, 80))
        self.lblWeight.setMaximumSize(QtCore.QSize(280, 80))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.lblWeight.setFont(font)
        self.lblWeight.setStyleSheet("color: rgb(0, 255, 240);")
        self.lblWeight.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblWeight.setObjectName("lblWeight")
        self.verticalLayout_5.addWidget(self.lblWeight)
        self.lblUnit = QtWidgets.QLabel(self.scaleWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblUnit.sizePolicy().hasHeightForWidth())
        self.lblUnit.setSizePolicy(sizePolicy)
        self.lblUnit.setMinimumSize(QtCore.QSize(280, 50))
        self.lblUnit.setMaximumSize(QtCore.QSize(280, 50))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.lblUnit.setFont(font)
        self.lblUnit.setStyleSheet("color: rgb(255, 228, 30);")
        self.lblUnit.setAlignment(QtCore.Qt.AlignCenter)
        self.lblUnit.setObjectName("lblUnit")
        self.verticalLayout_5.addWidget(self.lblUnit)
        self.horizontalLayout_3.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addWidget(self.scaleWidget)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.liftWidget = QtWidgets.QWidget(mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.liftWidget.sizePolicy().hasHeightForWidth())
        self.liftWidget.setSizePolicy(sizePolicy)
        self.liftWidget.setMinimumSize(QtCore.QSize(521, 310))
        self.liftWidget.setMaximumSize(QtCore.QSize(521, 310))
        self.liftWidget.setStyleSheet("QWidget #liftWidget {border: 3px solid rgb(32, 125, 198);}")
        self.liftWidget.setObjectName("liftWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.liftWidget)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")


        #self.editTest = QtWidgets.QLineEdit(self.liftWidget)
        #self.verticalLayout_4.addWidget(self.editTest)

        self.label_4 = QtWidgets.QLabel(self.liftWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 34))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 34))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background: rgb(157, 122, 1);color: rgb(241, 187, 2);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.lblActiveLift = QtWidgets.QLabel(self.liftWidget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.lblActiveLift.setFont(font)
        self.lblActiveLift.setStyleSheet("color: rgb(0, 255, 240);")
        self.lblActiveLift.setAlignment(QtCore.Qt.AlignCenter)
        self.lblActiveLift.setObjectName("lblActiveLift")
        self.verticalLayout_4.addWidget(self.lblActiveLift)
        self.lblLiftID = QtWidgets.QLabel(self.liftWidget)
        self.lblLiftID.setMinimumSize(QtCore.QSize(0, 50))
        self.lblLiftID.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.lblLiftID.setFont(font)
        self.lblLiftID.setStyleSheet("color: rgb(0, 255, 240);")
        self.lblLiftID.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLiftID.setObjectName("lblLiftID")
        self.verticalLayout_4.addWidget(self.lblLiftID)
        self.listBarcodes = QtWidgets.QListWidget(self.liftWidget)
        self.listBarcodes.setObjectName("listBarcodes")
        self.verticalLayout_4.addWidget(self.listBarcodes)
        self.verticalLayout_2.addWidget(self.liftWidget)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(3, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblDateTime = QtWidgets.QLabel(mainWidget)
        self.lblDateTime.setMinimumSize(QtCore.QSize(0, 37))
        self.lblDateTime.setMaximumSize(QtCore.QSize(16777215, 37))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lblDateTime.setFont(font)
        self.lblDateTime.setStyleSheet("color: rgb(104, 144, 153);")
        self.lblDateTime.setObjectName("lblDateTime")
        self.horizontalLayout.addWidget(self.lblDateTime)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 7, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnTools = QtWidgets.QToolButton(mainWidget)
        self.btnTools.setMinimumSize(QtCore.QSize(55, 50))
        self.btnTools.setMaximumSize(QtCore.QSize(55, 50))
        self.btnTools.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnTools.setStyleSheet("background: transparent;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/gui/button_tools.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnTools.setIcon(icon)
        self.btnTools.setIconSize(QtCore.QSize(55, 50))
        self.btnTools.setObjectName("btnTools")
        self.horizontalLayout_2.addWidget(self.btnTools)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btnSetup = QtWidgets.QToolButton(mainWidget)
        self.btnSetup.setMinimumSize(QtCore.QSize(45, 45))
        self.btnSetup.setMaximumSize(QtCore.QSize(45, 45))
        self.btnSetup.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSetup.setStyleSheet("background-color: transparent;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/gui/button_setup.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSetup.setIcon(icon1)
        self.btnSetup.setIconSize(QtCore.QSize(45, 45))
        self.btnSetup.setObjectName("btnSetup")
        self.horizontalLayout_2.addWidget(self.btnSetup)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(160, 38))
        self.label.setMaximumSize(QtCore.QSize(160, 38))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("res/gui/logo.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.lblWifi = QtWidgets.QLabel(mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblWifi.sizePolicy().hasHeightForWidth())
        self.lblWifi.setSizePolicy(sizePolicy)
        self.lblWifi.setMinimumSize(QtCore.QSize(50, 36))
        self.lblWifi.setMaximumSize(QtCore.QSize(50, 36))
        self.lblWifi.setText("")
        self.lblWifi.setPixmap(QtGui.QPixmap("res/gui/wifi.png"))
        self.lblWifi.setObjectName("lblWifi")
        self.horizontalLayout_2.addWidget(self.lblWifi)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.logWidget = QtWidgets.QWidget(mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logWidget.sizePolicy().hasHeightForWidth())
        self.logWidget.setSizePolicy(sizePolicy)
        self.logWidget.setMinimumSize(QtCore.QSize(0, 207))
        self.logWidget.setMaximumSize(QtCore.QSize(16777215, 207))
        self.logWidget.setStyleSheet("QWidget #logWidget {border: 3px solid rgb(32, 125, 198);}")
        self.logWidget.setObjectName("logWidget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.logWidget)
        self.verticalLayout_11.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.logWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(0, 34))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 34))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background: rgb(86, 86, 86);color: rgb(162, 162, 162);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_11.addWidget(self.label_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(6, 6, 0, 6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.listLog = QtWidgets.QListWidget(self.logWidget)
        self.listLog.setObjectName("listLog")
        self.horizontalLayout_5.addWidget(self.listLog)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.btnLogup = QtWidgets.QToolButton(self.logWidget)
        self.btnLogup.setMinimumSize(QtCore.QSize(63, 64))
        self.btnLogup.setMaximumSize(QtCore.QSize(63, 64))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/gui/arrow_up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogup.setIcon(icon2)
        self.btnLogup.setIconSize(QtCore.QSize(63, 64))
        self.btnLogup.setObjectName("btnLogup")
        self.verticalLayout_7.addWidget(self.btnLogup)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem5)
        self.btnLogdown = QtWidgets.QToolButton(self.logWidget)
        self.btnLogdown.setMinimumSize(QtCore.QSize(63, 64))
        self.btnLogdown.setMaximumSize(QtCore.QSize(63, 64))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("res/gui/arrow_down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogdown.setIcon(icon3)
        self.btnLogdown.setIconSize(QtCore.QSize(63, 64))
        self.btnLogdown.setObjectName("btnLogdown")
        self.verticalLayout_7.addWidget(self.btnLogdown)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.addWidget(self.logWidget)
        self.gridLayout.addLayout(self.verticalLayout_6, 1, 1, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.messageWidget = QtWidgets.QWidget(mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageWidget.sizePolicy().hasHeightForWidth())
        self.messageWidget.setSizePolicy(sizePolicy)
        self.messageWidget.setMinimumSize(QtCore.QSize(0, 90))
        self.messageWidget.setMaximumSize(QtCore.QSize(16777215, 90))
        self.messageWidget.setStyleSheet("QWidget #messageWidget {border: 3px solid rgb(32, 125, 198);}")
        self.messageWidget.setObjectName("messageWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.messageWidget)
        self.verticalLayout_9.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.messageWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(0, 34))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 34))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background: rgb(7, 159, 212);color: white;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.lblMessage = QtWidgets.QLabel(self.messageWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lblMessage.setFont(font)
        self.lblMessage.setStyleSheet("color: rgb(255, 228, 30);")
        self.lblMessage.setAlignment(QtCore.Qt.AlignCenter)
        self.lblMessage.setObjectName("lblMessage")
        self.verticalLayout_9.addWidget(self.lblMessage)
        self.verticalLayout_8.addWidget(self.messageWidget)
        self.actionWidget = QtWidgets.QWidget(mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionWidget.sizePolicy().hasHeightForWidth())
        self.actionWidget.setSizePolicy(sizePolicy)
        self.actionWidget.setMinimumSize(QtCore.QSize(0, 214))
        self.actionWidget.setMaximumSize(QtCore.QSize(16777215, 214))
        self.actionWidget.setStyleSheet("QWidget #actionWidget {border: 3px solid rgb(32, 125, 198);}")
        self.actionWidget.setObjectName("actionWidget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.actionWidget)
        self.verticalLayout_10.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_7 = QtWidgets.QLabel(self.actionWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setMinimumSize(QtCore.QSize(0, 34))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 34))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background: rgb(7, 159, 212);color: white;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        self.widget = QtWidgets.QWidget(self.actionWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 174))
        self.widget.setStyleSheet("background:transparent;")
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(145, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.btnLogin = QtWidgets.QToolButton(self.widget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("res/gui/button_login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnLogin.setIcon(icon4)
        self.btnLogin.setIconSize(QtCore.QSize(159, 118))
        self.btnLogin.setObjectName("btnLogin")
        self.horizontalLayout_4.addWidget(self.btnLogin)
        self.btnSetRWT = QtWidgets.QToolButton(self.widget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("res/gui/settings_wthreshold_record.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSetRWT.setIcon(icon5)
        self.btnSetRWT.setIconSize(QtCore.QSize(159, 118))
        self.btnSetRWT.setObjectName("btnSetRWT")
        self.horizontalLayout_4.addWidget(self.btnSetRWT)
        spacerItem7 = QtWidgets.QSpacerItem(144, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_10.addWidget(self.widget)
        self.verticalLayout_8.addWidget(self.actionWidget)
        self.gridLayout.addLayout(self.verticalLayout_8, 2, 1, 1, 1)

        self.retranslateUi(mainWidget)
        QtCore.QMetaObject.connectSlotsByName(mainWidget)

    def retranslateUi(self, mainWidget):
        _translate = QtCore.QCoreApplication.translate
        mainWidget.setWindowTitle(_translate("mainWidget", "MainWidget"))
        self.label_3.setText(_translate("mainWidget", "SCALE"))
        self.lblWeight.setText(_translate("mainWidget", "00000.0"))
        self.lblUnit.setText(_translate("mainWidget", "LBS"))
        self.label_4.setText(_translate("mainWidget", "ACTIVE LIFT"))
        self.lblActiveLift.setText(_translate("mainWidget", "PLEASE LOGIN"))
        self.lblLiftID.setText(_translate("mainWidget", "Lift ID"))
        self.lblDateTime.setText(_translate("mainWidget", "13:00 Monday, May 04,  2020"))
        self.label_5.setText(_translate("mainWidget", "LOG"))
        self.label_6.setText(_translate("mainWidget", "MESSAGE CENTER"))
        self.lblMessage.setText(_translate("mainWidget", "Please Login"))
        self.label_7.setText(_translate("mainWidget", "AVAILABLE ACTIONS"))

