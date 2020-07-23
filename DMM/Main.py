from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFontDatabase, QFont

from MainWidget import MainWidget
from ToolsWidget import ToolsWidget
import ClockHelper
import WeightButtonHelper


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi()
        self.mainWidget = MainWidget(self)
        self.toolsWidget = ToolsWidget(self)

        self.mainStacked.addWidget(self.mainWidget.mainWidget)
        self.mainStacked.addWidget(self.toolsWidget.toolsWidget)
       
        self.setMainWidget()
        #self.setToolsWidget()

        self.initStatVariables()
        self.setWeightFont()
        self.initHelperClass()

    def initStatVariables(self):
        self.WEIGHTTHRESHOLD = 100

        self.SERIALMODE = 'RS232'
        self.TRUCKID = ''
        self.CURRENTWEIGHT = '0'
        self.WEIGHTMODE = 'LBS'
        self.HX711STAT = True
        self.RS232STAT = True
        self.DOCID = ''
        self.OPENKEYBORADACTIONSTAT = False
        self.TIMESTAT = True

        self.DEBUG = True

    def setWeightFont(self):
        QFontDatabase.addApplicationFont("./res/font/DJB Get Digital.ttf")
        your_ttf_font = QFont("DJB Get Digital", 65)
        # your_ttf_font.setBold(True)
        self.mainWidget.lblWeight.setFont(your_ttf_font)
        # DMMMainUI.closeEvent(self.closeEvent1)

    def initHelperClass(self):
        ClockHelper.ClockHelper(self).startClock()
        self.WBHelper = WeightButtonHelper.WeightButtonHelper(self)
        if self.SERIALMODE == 'HX711':
            self.WBHelper.readHX711()
        else:
            self.WBHelper.readRS232()

    def setMainWidget(self):
        self.mainStacked.setCurrentIndex(0)

    def setToolsWidget(self):
        self.mainStacked.setCurrentIndex(1)

    def updateTimeText(self, timestamp):
        self.mainWidget.updateTimeText(timestamp)

    def updateWeightText(self, weight):
        self.mainWidget.updateWeightText(weight)

    def updateBarCodeImage(self, img):
        self.mainWidget.updateBarCodeImage(img)

    def updateQrCodeImage(self, img):
        self.mainWidget.updateQrCodeImage(img)

    def closeEvent(self, event):
        result = QtWidgets.QMessageBox.question(self,
                      "Confirm Exit...",
                      "Are you sure you want to exit ?",
                      QtWidgets.QMessageBox.Yes| QtWidgets.QMessageBox.No)
        event.ignore()

        if result == QtWidgets.QMessageBox.Yes:
            event.accept()

            print('Exiting Program Loop')
            self.HX711STAT = False
            self.RS232STAT = False
            self.TIMESTAT = False
            
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(1024, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(1024, 700))
        self.setMaximumSize(QtCore.QSize(1024, 700))
        self.setStyleSheet("QMainWindow#MainWindow {background-color: black;}")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainStacked = QtWidgets.QStackedWidget(self.centralwidget)
        self.mainStacked.setObjectName("mainStacked")

        self.verticalLayout.addWidget(self.mainStacked)
        self.setCentralWidget(self.centralwidget)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint)
        #self.showMaximized()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "DMM"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
