from datetime import datetime

from PIL.ImageQt import ImageQt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QFontDatabase, QFont
from PyQt5.QtWidgets import QMessageBox

import WeightButtonHelper
from  KeyboardWidget import KeyboardWidget
from TimerMessageBox import TimerMessageBox


class Ui_DMMMainUI(object):
    def setupUi(self, DMMMainUI):
        DMMMainUI.setObjectName("DMMMainUI")
        DMMMainUI.resize(800, 480)
        DMMMainUI.setMinimumSize(QtCore.QSize(800, 480))
        DMMMainUI.setMaximumSize(QtCore.QSize(800, 480))
        DMMMainUI.setStyleSheet("background-color:rgb(152,152,152)")
        self.MainFrame = QtWidgets.QFrame(DMMMainUI)
        self.MainFrame.setGeometry(QtCore.QRect(0, 0, 680, 380))
        self.MainFrame.setMinimumSize(QtCore.QSize(680, 380))
        self.MainFrame.setMaximumSize(QtCore.QSize(680, 380))
        self.MainFrame.setAutoFillBackground(False)
        self.MainFrame.setStyleSheet("background-color:rgb(64,62,62);\n"
"border-style:solid;\n"
"border-width:4;\n"
"border-color:rgb(183, 149, 11 );\n"
"")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.label_TimeNow = QtWidgets.QLabel(self.MainFrame)
        self.label_TimeNow.setGeometry(QtCore.QRect(10, 10, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_TimeNow.setFont(font)
        self.label_TimeNow.setStyleSheet("border:none;\n"
"color:rgb(167,167,102);")
        self.label_TimeNow.setObjectName("label_TimeNow")
        self.label_Weight = QtWidgets.QLabel(self.MainFrame)
        self.label_Weight.setGeometry(QtCore.QRect(10, 50, 440, 151))
        self.label_Weight.setMaximumSize(QtCore.QSize(440, 151))
        font = QtGui.QFont()
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.label_Weight.setFont(font)
        self.label_Weight.setStyleSheet("border:none;\n"
"color: rgb(255,228,30);")
        self.label_Weight.setObjectName("label_Weight")
        self.label_QRCode = QtWidgets.QLabel(self.MainFrame)
        self.label_QRCode.setGeometry(QtCore.QRect(15, 210, 160, 160))
        self.label_QRCode.setAutoFillBackground(True)
        self.label_QRCode.setStyleSheet("border:none;")
        self.label_QRCode.setText("")
        self.label_QRCode.setScaledContents(True)
        self.label_QRCode.setObjectName("label_QRCode")
        self.widget_FloatFrame4 = QtWidgets.QWidget(self.MainFrame)
        self.widget_FloatFrame4.setGeometry(QtCore.QRect(455, 290, 215, 80))
        self.widget_FloatFrame4.setStyleSheet("border-style:dotted;\n"
"border-width:3;")
        self.widget_FloatFrame4.setObjectName("widget_FloatFrame4")
        self.label_OpID = QtWidgets.QLabel(self.widget_FloatFrame4)
        self.label_OpID.setGeometry(QtCore.QRect(6, 42, 201, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_OpID.setFont(font)
        self.label_OpID.setStyleSheet("border:none;\n"
"color:#FFE41E;\n"
"background-color:#17202A;")
        self.label_OpID.setObjectName("label_OpID")
        self.label_7 = QtWidgets.QLabel(self.widget_FloatFrame4)
        self.label_7.setGeometry(QtCore.QRect(6, 8, 201, 36))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("border:none;\n"
"background-color:#B1B1B1;\n"
"color:black;")
        self.label_7.setObjectName("label_7")
        self.widget_FloatFrame3 = QtWidgets.QWidget(self.MainFrame)
        self.widget_FloatFrame3.setGeometry(QtCore.QRect(455, 207, 215, 80))
        self.widget_FloatFrame3.setStyleSheet("border-style:dotted;\n"
"border-width:3;")
        self.widget_FloatFrame3.setObjectName("widget_FloatFrame3")
        self.label_DocID = QtWidgets.QLabel(self.widget_FloatFrame3)
        self.label_DocID.setGeometry(QtCore.QRect(6, 42, 201, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_DocID.setFont(font)
        self.label_DocID.setStyleSheet("border:none;\n"
"color:#FFE41E;\n"
"background-color:#17202A;")
        self.label_DocID.setObjectName("label_DocID")
        self.label_5 = QtWidgets.QLabel(self.widget_FloatFrame3)
        self.label_5.setGeometry(QtCore.QRect(6, 8, 201, 36))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setStyleSheet("border:none;\n"
"background-color:#B1B1B1;\n"
"color:black;")
        self.label_5.setObjectName("label_5")
        self.label_BarCode = QtWidgets.QLabel(self.MainFrame)
        self.label_BarCode.setGeometry(QtCore.QRect(195, 210, 240, 160))
        self.label_BarCode.setAutoFillBackground(True)
        self.label_BarCode.setStyleSheet("border:none;")
        self.label_BarCode.setText("")
        self.label_BarCode.setScaledContents(True)
        self.label_BarCode.setObjectName("label_BarCode")
        self.label_TruckID = QtWidgets.QLabel(self.MainFrame)
        self.label_TruckID.setGeometry(QtCore.QRect(460, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_TruckID.setFont(font)
        self.label_TruckID.setStyleSheet("border:none;\n"
"color:rgb(236, 112, 99 );")
        self.label_TruckID.setObjectName("label_TruckID")
        self.label_TruckIDIcon = QtWidgets.QLabel(self.MainFrame)
        self.label_TruckIDIcon.setGeometry(QtCore.QRect(420, 10, 34, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_TruckIDIcon.setFont(font)
        self.label_TruckIDIcon.setStyleSheet("border:none;\n"
"color:rgb(205,97,85);")
        self.label_TruckIDIcon.setText("")
        self.label_TruckIDIcon.setPixmap(QtGui.QPixmap("res/gui/truck-enabled.png"))
        self.label_TruckIDIcon.setObjectName("label_TruckIDIcon")
        self.label_WifiIcon = QtWidgets.QLabel(self.MainFrame)
        self.label_WifiIcon.setGeometry(QtCore.QRect(635, 15, 34, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_WifiIcon.setFont(font)
        self.label_WifiIcon.setStyleSheet("border:none;\n"
"color:rgb(205,97,85);")
        self.label_WifiIcon.setText("")
        self.label_WifiIcon.setPixmap(QtGui.QPixmap("res/gui/wifi-enabled.png"))
        self.label_WifiIcon.setObjectName("label_WifiIcon")
        self.widget_FloatFrame1 = QtWidgets.QWidget(self.MainFrame)
        self.widget_FloatFrame1.setGeometry(QtCore.QRect(455, 40, 215, 80))
        self.widget_FloatFrame1.setStyleSheet("border-style:dotted;\n"
"border-width:3;")
        self.widget_FloatFrame1.setObjectName("widget_FloatFrame1")
        self.label_DocID_2 = QtWidgets.QLabel(self.widget_FloatFrame1)
        self.label_DocID_2.setGeometry(QtCore.QRect(6, 42, 201, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_DocID_2.setFont(font)
        self.label_DocID_2.setStyleSheet("border:none;\n"
"color:#FFE41E;\n"
"background-color:#17202A;")
        self.label_DocID_2.setObjectName("label_DocID_2")
        self.label_6 = QtWidgets.QLabel(self.widget_FloatFrame1)
        self.label_6.setGeometry(QtCore.QRect(6, 8, 201, 36))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setStyleSheet("border:none;\n"
"background-color:#B1B1B1;\n"
"color:black;")
        self.label_6.setObjectName("label_6")
        self.widget_FloatFrame2 = QtWidgets.QWidget(self.MainFrame)
        self.widget_FloatFrame2.setGeometry(QtCore.QRect(455, 124, 215, 80))
        self.widget_FloatFrame2.setStyleSheet("border-style:dotted;\n"
"border-width:3;")
        self.widget_FloatFrame2.setObjectName("widget_FloatFrame2")
        self.label_DocID_6 = QtWidgets.QLabel(self.widget_FloatFrame2)
        self.label_DocID_6.setGeometry(QtCore.QRect(6, 42, 201, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_DocID_6.setFont(font)
        self.label_DocID_6.setStyleSheet("border:none;\n"
"color:#FFE41E;\n"
"background-color:#17202A;")
        self.label_DocID_6.setObjectName("label_DocID_6")
        self.label_11 = QtWidgets.QLabel(self.widget_FloatFrame2)
        self.label_11.setGeometry(QtCore.QRect(6, 8, 201, 36))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_11.setStyleSheet("border:none;\n"
"background-color:#B1B1B1;\n"
"color:black;")
        self.label_11.setObjectName("label_11")
        self.pushButton_ScreenUnlock = QtWidgets.QPushButton(DMMMainUI)
        self.pushButton_ScreenUnlock.setGeometry(QtCore.QRect(690, 5, 100, 70))
        self.pushButton_ScreenUnlock.setMinimumSize(QtCore.QSize(100, 70))
        self.pushButton_ScreenUnlock.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton_ScreenUnlock.setStyleSheet("")
        self.pushButton_ScreenUnlock.setObjectName("pushButton_ScreenUnlock")
        self.pushButton_ToolsSettings = QtWidgets.QPushButton(DMMMainUI)
        self.pushButton_ToolsSettings.setGeometry(QtCore.QRect(690, 80, 100, 70))
        self.pushButton_ToolsSettings.setMinimumSize(QtCore.QSize(100, 70))
        self.pushButton_ToolsSettings.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton_ToolsSettings.setStyleSheet("")
        self.pushButton_ToolsSettings.setObjectName("pushButton_ToolsSettings")
        self.pushButton_Mode = QtWidgets.QPushButton(DMMMainUI)
        self.pushButton_Mode.setGeometry(QtCore.QRect(690, 155, 100, 70))
        self.pushButton_Mode.setMinimumSize(QtCore.QSize(100, 70))
        self.pushButton_Mode.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton_Mode.setObjectName("pushButton_Mode")
        self.pushButton_DocID = QtWidgets.QPushButton(DMMMainUI)
        self.pushButton_DocID.setGeometry(QtCore.QRect(690, 230, 100, 70))
        self.pushButton_DocID.setMinimumSize(QtCore.QSize(100, 70))
        self.pushButton_DocID.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton_DocID.setObjectName("pushButton_DocID")
        self.pushButton_OpID = QtWidgets.QPushButton(DMMMainUI)
        self.pushButton_OpID.setGeometry(QtCore.QRect(690, 305, 100, 70))
        self.pushButton_OpID.setMinimumSize(QtCore.QSize(100, 70))
        self.pushButton_OpID.setMaximumSize(QtCore.QSize(100, 70))
        self.pushButton_OpID.setObjectName("pushButton_OpID")
        self.pushButton_Weight = QtWidgets.QPushButton(DMMMainUI)
        self.pushButton_Weight.setGeometry(QtCore.QRect(20, 390, 100, 80))
        self.pushButton_Weight.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_Weight.setMaximumSize(QtCore.QSize(100, 80))
        self.pushButton_Weight.setStyleSheet("")
        self.pushButton_Weight.setObjectName("pushButton_Weight")
        self.pushButton_Zero = QtWidgets.QPushButton(DMMMainUI)
        self.pushButton_Zero.setGeometry(QtCore.QRect(200, 390, 100, 80))
        self.pushButton_Zero.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_Zero.setMaximumSize(QtCore.QSize(100, 80))
        self.pushButton_Zero.setObjectName("pushButton_Zero")
        self.pushButton_Tare = QtWidgets.QPushButton(DMMMainUI)
        self.pushButton_Tare.setGeometry(QtCore.QRect(380, 390, 100, 80))
        self.pushButton_Tare.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_Tare.setMaximumSize(QtCore.QSize(100, 80))
        self.pushButton_Tare.setObjectName("pushButton_Tare")
        self.pushButton_Print = QtWidgets.QPushButton(DMMMainUI)
        self.pushButton_Print.setGeometry(QtCore.QRect(560, 390, 100, 80))
        self.pushButton_Print.setMinimumSize(QtCore.QSize(100, 80))
        self.pushButton_Print.setMaximumSize(QtCore.QSize(100, 80))
        self.pushButton_Print.setObjectName("pushButton_Print")
        self.label = QtWidgets.QLabel(DMMMainUI)
        self.label.setGeometry(QtCore.QRect(719, 390, 70, 80))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("res/gui/logo.png"))
        self.label.setObjectName("label")

        self.retranslateUi(DMMMainUI)
        QtCore.QMetaObject.connectSlotsByName(DMMMainUI)

    def retranslateUi(self, DMMMainUI):
        _translate = QtCore.QCoreApplication.translate
        DMMMainUI.setWindowTitle(_translate("DMMMainUI", "DMMMainUI"))
        self.label_TimeNow.setText(_translate("DMMMainUI", "13:00H Friday, December 20, 2019"))
        self.label_Weight.setText(_translate("DMMMainUI", "10000"))
        self.label_OpID.setText(_translate("DMMMainUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">TK-4215</span></p></body></html>"))
        self.label_7.setText(_translate("DMMMainUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">OPERATOR ID</span></p></body></html>"))
        self.label_DocID.setText(_translate("DMMMainUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">WH99632709987/43A</span></p></body></html>"))
        self.label_5.setText(_translate("DMMMainUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">DOCUMENT ID</span></p></body></html>"))
        self.label_TruckID.setText(_translate("DMMMainUI", "WP-WW1234"))
        self.label_DocID_2.setText(_translate("DMMMainUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">WH99632709987/43A</span></p></body></html>"))
        self.label_6.setText(_translate("DMMMainUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">DOCUMENT ID</span></p></body></html>"))
        self.label_DocID_6.setText(_translate("DMMMainUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">WH99632709987/43A</span></p></body></html>"))
        self.label_11.setText(_translate("DMMMainUI", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">DOCUMENT ID</span></p></body></html>"))
        self.pushButton_ScreenUnlock.setText(_translate("DMMMainUI", "SCREEN UNLOCK"))
        self.pushButton_ToolsSettings.setText(_translate("DMMMainUI", "PushButton"))
        self.pushButton_Mode.setText(_translate("DMMMainUI", "PushButton"))
        self.pushButton_DocID.setText(_translate("DMMMainUI", "PushButton"))
        self.pushButton_OpID.setText(_translate("DMMMainUI", "PushButton"))
        self.pushButton_Weight.setText(_translate("DMMMainUI", "PushButton"))
        self.pushButton_Zero.setText(_translate("DMMMainUI", "PushButton"))
        self.pushButton_Tare.setText(_translate("DMMMainUI", "PushButton"))
        self.pushButton_Print.setText(_translate("DMMMainUI", "PushButton"))


##------------------------------------------------------------------------------------------------------------------------------------------------------------
        self.initStatVariables()
        self.formatWindow(DMMMainUI)
        self.connectButtonsAction()
        self.initHelperClass()

## ************************************************************************************************************************************************************
    def formatWindow(self, DMMMainUI):
        DMMMainUI.setGeometry(0, 0, 800, 480)
        font_db = QFontDatabase()
        font_id = font_db.addApplicationFont("./res/font/DJB Get Digital.ttf")
        your_ttf_font = QFont("DJB Get Digital", 120)
        #your_ttf_font.setBold(True)
        self.label_Weight.setFont(your_ttf_font)
        #DMMMainUI.closeEvent(self.closeEvent1)

    def closeEvent(self):
        print('Exiting Program Loop')
        self.HX711STAT = False
        self.RS232STAT = False

    def insertWeightData(self):
        try:
            weight = (float)(self.CURRENTWEIGHT)
            if weight > (float)(self.WEIGHTTHRESHOLD):
                now = datetime.now()
                date_time = now.strftime("%m/%d/%Y %H:%M:%S")
                stat = self.WBHelper.insertData([self.TRUCKID, weight, self.WEIGHTMODE, self.DOCID, 'SINGLE', date_time])
                if stat is True:
                    messagebox = TimerMessageBox(2, 'Database', 'Data Stored Successfully', DMMMainUI)
                    messagebox.exec_()

        except Exception as e:
            print('Inserting Database Error:', e)

    def connectButtonsAction(self):
        self.pushButton_Weight.clicked.connect(self.actionWeightModeChange)
        self.pushButton_DocID.clicked.connect(self.actionDocIDScan)


    def initHelperClass(self):
        self.WBHelper = WeightButtonHelper.WeightButtonHelper(self)
        if self.SERIALMODE == 'HX711':
            self.WBHelper.readHX711()
        else:
            self.WBHelper.readRS232()

    def updateWeightText(self, weight):
        self.label_Weight.setText(weight)
        self.label_Weight.adjustSize()

    def updateBarCodeImage(self, img):
        im = img.convert("RGB")
        data = im.tobytes("raw", "RGB")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qim)
        #pixmap = QPixmap('./res/img/barcode_resized.jpg')
        self.label_BarCode.setPixmap(pixmap)

    def updateQrCodeImage(self, img):
        im = img.convert("RGB")
        data = im.tobytes("raw", "RGB")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(qim)
        #pixmap = QPixmap('./res/img/qrcode_resized.jpg')
        self.label_QRCode.setPixmap(pixmap)

    def showMainWindow(self, mode):
        DMMMainUI.show()
        if mode is 'DOC':
            self.widget_FloatFrame3.show()
            self.label_DocID.setText(self.DOCID)
            self.label_DocID.adjustSize()
            self.insertWeightData()


    def actionWeightModeChange(self):
        if self.WEIGHTMODE == 'KG':
            self.WEIGHTMODE = 'LBS'
        else:
            self.WEIGHTMODE = 'KG'

    def actionDocIDScan(self):
        DMMMainUI.hide()
        self.w = KeyboardWidget(title='ENTER or SCAN --> Documentation ID', GUI=self, mode='DOC')
        self.w.show()

    def initStatVariables(self):
        self.WEIGHTTHRESHOLD = 100

        self.SERIALMODE = 'RS232'
        self.TRUCKID = ''
        self.CURRENTWEIGHT = '0'
        self.WEIGHTMODE = 'KG'
        self.HX711STAT = True
        self.RS232STAT = True
        self.DOCID = ''
        self.OPENKEYBORADACTIONSTAT = False

        self.DEBUG = True


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DMMMainUI = QtWidgets.QWidget()
    DMMMainUI.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
    DMMMainUI.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
    DMMMainUI.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)
    ui = Ui_DMMMainUI()
    ui.setupUi(DMMMainUI)
    DMMMainUI.show()
    app.aboutToQuit.connect(ui.closeEvent)
    sys.exit(app.exec_())

