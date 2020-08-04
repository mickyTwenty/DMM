# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWidget(object):
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
        mainWidget.setStyleSheet("QWidget#mainWidget { background-color: black; }")
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
        self.scaleWidget.setMinimumSize(QtCore.QSize(0, 207))
        self.scaleWidget.setMaximumSize(QtCore.QSize(16777215, 207))
        self.scaleWidget.setStyleSheet("QWidget #scaleWidget {\n"
"border: 3px solid rgb(32, 125, 198);\n"
"}")
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
        self.label_3.setStyleSheet("background: rgb(6, 57, 71);\n"
"color: rgb(241, 187, 2);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lblBarcode = QtWidgets.QLabel(self.scaleWidget)
        self.lblBarcode.setAlignment(QtCore.Qt.AlignCenter)
        self.lblBarcode.setObjectName("lblBarcode")
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
        self.lblWeight.setMinimumSize(QtCore.QSize(260, 80))
        self.lblWeight.setMaximumSize(QtCore.QSize(260, 80))
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
        self.lblUnit.setMinimumSize(QtCore.QSize(260, 50))
        self.lblUnit.setMaximumSize(QtCore.QSize(260, 50))
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
        self.liftWidget.setMinimumSize(QtCore.QSize(0, 310))
        self.liftWidget.setMaximumSize(QtCore.QSize(16777215, 310))
        self.liftWidget.setStyleSheet("QWidget #liftWidget {\n"
"border: 3px solid rgb(32, 125, 198);\n"
"}")
        self.liftWidget.setObjectName("liftWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.liftWidget)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
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
        self.label_4.setStyleSheet("background: rgb(157, 122, 1);\n"
"color: rgb(241, 187, 2);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
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
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
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
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
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
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
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
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.label_2 = QtWidgets.QLabel(mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(50, 36))
        self.label_2.setMaximumSize(QtCore.QSize(50, 36))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("res/gui/wifi.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
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
        self.logWidget.setStyleSheet("QWidget #logWidget {\n"
"border: 3px solid rgb(32, 125, 198);\n"
"}")
        self.logWidget.setObjectName("logWidget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.logWidget)
        self.verticalLayout_7.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
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
        self.label_5.setStyleSheet("background: rgb(86, 86, 86);\n"
"color: rgb(162, 162, 162);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_7.addWidget(self.label_5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem6)
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
        self.messageWidget.setStyleSheet("QWidget #messageWidget {\n"
"border: 3px solid rgb(32, 125, 198);\n"
"}")
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
        self.label_6.setStyleSheet("background: rgb(7, 159, 212);\n"
"color: white;")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem7)
        self.verticalLayout_8.addWidget(self.messageWidget)
        self.actionWidget = QtWidgets.QWidget(mainWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.actionWidget.sizePolicy().hasHeightForWidth())
        self.actionWidget.setSizePolicy(sizePolicy)
        self.actionWidget.setMinimumSize(QtCore.QSize(0, 214))
        self.actionWidget.setMaximumSize(QtCore.QSize(16777215, 214))
        self.actionWidget.setStyleSheet("QWidget #actionWidget {\n"
"border: 3px solid rgb(32, 125, 198);\n"
"}")
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
        self.label_7.setStyleSheet("background: rgb(7, 159, 212);\n"
"color: white;")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_10.addWidget(self.label_7)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem8)
        self.verticalLayout_8.addWidget(self.actionWidget)
        self.gridLayout.addLayout(self.verticalLayout_8, 2, 1, 1, 1)

        self.retranslateUi(mainWidget)
        QtCore.QMetaObject.connectSlotsByName(mainWidget)

    def retranslateUi(self, mainWidget):
        _translate = QtCore.QCoreApplication.translate
        mainWidget.setWindowTitle(_translate("mainWidget", "MainWidget"))
        self.label_3.setText(_translate("mainWidget", "SCALE"))
        self.lblWeight.setText(_translate("mainWidget", "1000"))
        self.lblUnit.setText(_translate("mainWidget", "LBS"))
        self.label_4.setText(_translate("mainWidget", "ACTIVE LIFT"))
        self.lblDateTime.setText(_translate("mainWidget", "13:00 Monday, May 04,  2020"))
        self.label_5.setText(_translate("mainWidget", "LOG"))
        self.label_6.setText(_translate("mainWidget", "MESSAGE CENTER"))
        self.label_7.setText(_translate("mainWidget", "AVAILABLE ACTIONS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWidget = QtWidgets.QWidget()
    ui = Ui_mainWidget()
    ui.setupUi(mainWidget)
    mainWidget.show()
    sys.exit(app.exec_())
