# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolwidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ToolsWidget(object):
    def setupUi(self, ToolsWidget):
        ToolsWidget.setObjectName("ToolsWidget")
        ToolsWidget.resize(1024, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ToolsWidget.sizePolicy().hasHeightForWidth())
        ToolsWidget.setSizePolicy(sizePolicy)
        ToolsWidget.setMinimumSize(QtCore.QSize(1024, 600))
        ToolsWidget.setMaximumSize(QtCore.QSize(1024, 600))
        ToolsWidget.setStyleSheet("QWidget#ToolWidget {\n"
"    background-color: black;\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"};")
        self.verticalLayout = QtWidgets.QVBoxLayout(ToolsWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(40, 24, 40, -1)
        self.gridLayout.setSpacing(50)
        self.gridLayout.setObjectName("gridLayout")
        self.btnCopy = QtWidgets.QToolButton(ToolsWidget)
        self.btnCopy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/gui/tools_copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCopy.setIcon(icon)
        self.btnCopy.setIconSize(QtCore.QSize(200, 148))
        self.btnCopy.setObjectName("btnCopy")
        self.gridLayout.addWidget(self.btnCopy, 0, 1, 1, 1)
        self.btnEmail = QtWidgets.QToolButton(ToolsWidget)
        self.btnEmail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/gui/tools_email.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEmail.setIcon(icon1)
        self.btnEmail.setIconSize(QtCore.QSize(200, 148))
        self.btnEmail.setObjectName("btnEmail")
        self.gridLayout.addWidget(self.btnEmail, 0, 0, 1, 1)
        self.btnCalc = QtWidgets.QToolButton(ToolsWidget)
        self.btnCalc.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnCalc.setStyleSheet("background-color: transparent")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/gui/tools_calculator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCalc.setIcon(icon2)
        self.btnCalc.setIconSize(QtCore.QSize(200, 148))
        self.btnCalc.setObjectName("btnCalc")
        self.gridLayout.addWidget(self.btnCalc, 1, 0, 1, 1)
        self.btnDiagnostics = QtWidgets.QToolButton(ToolsWidget)
        self.btnDiagnostics.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("res/gui/tools_diagnostics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnDiagnostics.setIcon(icon3)
        self.btnDiagnostics.setIconSize(QtCore.QSize(200, 148))
        self.btnDiagnostics.setObjectName("btnDiagnostics")
        self.gridLayout.addWidget(self.btnDiagnostics, 0, 2, 1, 1)
        self.btnInfo = QtWidgets.QToolButton(ToolsWidget)
        self.btnInfo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("res/gui/tools_info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnInfo.setIcon(icon4)
        self.btnInfo.setIconSize(QtCore.QSize(200, 148))
        self.btnInfo.setObjectName("btnInfo")
        self.gridLayout.addWidget(self.btnInfo, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 76, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(12, -1, 12, 7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtWidgets.QToolButton(ToolsWidget)
        self.btnBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("res/gui/button_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon5)
        self.btnBack.setIconSize(QtCore.QSize(103, 103))
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(ToolsWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("res/gui/img_tools.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnHome = QtWidgets.QToolButton(ToolsWidget)
        self.btnHome.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("res/gui/button_home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHome.setIcon(icon6)
        self.btnHome.setIconSize(QtCore.QSize(103, 103))
        self.btnHome.setObjectName("btnHome")
        self.horizontalLayout.addWidget(self.btnHome)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ToolsWidget)
        QtCore.QMetaObject.connectSlotsByName(ToolsWidget)

    def retranslateUi(self, ToolsWidget):
        _translate = QtCore.QCoreApplication.translate
        ToolsWidget.setWindowTitle(_translate("ToolsWidget", "ToolsWidget"))
        self.btnCopy.setText(_translate("ToolsWidget", "..."))
        self.btnEmail.setText(_translate("ToolsWidget", "..."))
        self.btnCalc.setText(_translate("ToolsWidget", "..."))
        self.btnDiagnostics.setText(_translate("ToolsWidget", "..."))
        self.btnInfo.setText(_translate("ToolsWidget", "..."))
        self.btnBack.setText(_translate("ToolsWidget", "..."))
        self.btnHome.setText(_translate("ToolsWidget", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ToolsWidget = QtWidgets.QWidget()
    ui = Ui_ToolsWidget()
    ui.setupUi(ToolsWidget)
    ToolsWidget.show()
    sys.exit(app.exec_())
