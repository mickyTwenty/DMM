# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolwidget.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ToolWidget(object):
    def setupUi(self, ToolWidget):
        ToolWidget.setObjectName("ToolWidget")
        ToolWidget.resize(1024, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ToolWidget.sizePolicy().hasHeightForWidth())
        ToolWidget.setSizePolicy(sizePolicy)
        ToolWidget.setMinimumSize(QtCore.QSize(1024, 600))
        ToolWidget.setMaximumSize(QtCore.QSize(1024, 600))
        ToolWidget.setStyleSheet("QWidget#ToolWidget {\n"
"    background-color: black;\n"
"}\n"
"\n"
"QToolButton {\n"
"    background-color: transparent;\n"
"};")
        self.verticalLayout = QtWidgets.QVBoxLayout(ToolWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(40, 24, 40, -1)
        self.gridLayout.setSpacing(50)
        self.gridLayout.setObjectName("gridLayout")
        self.btnCopy = QtWidgets.QToolButton(ToolWidget)
        self.btnCopy.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("res/gui/tools_copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCopy.setIcon(icon)
        self.btnCopy.setIconSize(QtCore.QSize(200, 148))
        self.btnCopy.setObjectName("btnCopy")
        self.gridLayout.addWidget(self.btnCopy, 0, 1, 1, 1)
        self.btnEmail = QtWidgets.QToolButton(ToolWidget)
        self.btnEmail.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("res/gui/tools_email.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnEmail.setIcon(icon1)
        self.btnEmail.setIconSize(QtCore.QSize(200, 148))
        self.btnEmail.setObjectName("btnEmail")
        self.gridLayout.addWidget(self.btnEmail, 0, 0, 1, 1)
        self.toolButton = QtWidgets.QToolButton(ToolWidget)
        self.toolButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.toolButton.setStyleSheet("background-color: transparent")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("res/gui/tools_calculator.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon2)
        self.toolButton.setIconSize(QtCore.QSize(200, 148))
        self.toolButton.setObjectName("toolButton")
        self.gridLayout.addWidget(self.toolButton, 1, 0, 1, 1)
        self.btnDiagnostics = QtWidgets.QToolButton(ToolWidget)
        self.btnDiagnostics.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDiagnostics.setIcon(icon1)
        self.btnDiagnostics.setIconSize(QtCore.QSize(200, 148))
        self.btnDiagnostics.setObjectName("btnDiagnostics")
        self.gridLayout.addWidget(self.btnDiagnostics, 0, 2, 1, 1)
        self.btnInfo = QtWidgets.QToolButton(ToolWidget)
        self.btnInfo.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnInfo.setIcon(icon)
        self.btnInfo.setIconSize(QtCore.QSize(200, 148))
        self.btnInfo.setObjectName("btnInfo")
        self.gridLayout.addWidget(self.btnInfo, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 76, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(12, -1, 12, 7)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnBack = QtWidgets.QToolButton(ToolWidget)
        self.btnBack.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("res/gui/button_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBack.setIcon(icon3)
        self.btnBack.setIconSize(QtCore.QSize(103, 103))
        self.btnBack.setObjectName("btnBack")
        self.horizontalLayout.addWidget(self.btnBack)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(ToolWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("res/gui/img_tools.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnHome = QtWidgets.QToolButton(ToolWidget)
        self.btnHome.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("res/gui/button_home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnHome.setIcon(icon4)
        self.btnHome.setIconSize(QtCore.QSize(103, 103))
        self.btnHome.setObjectName("btnHome")
        self.horizontalLayout.addWidget(self.btnHome)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ToolWidget)
        QtCore.QMetaObject.connectSlotsByName(ToolWidget)

    def retranslateUi(self, ToolWidget):
        _translate = QtCore.QCoreApplication.translate
        ToolWidget.setWindowTitle(_translate("ToolWidget", "Form"))
        self.btnCopy.setText(_translate("ToolWidget", "..."))
        self.btnEmail.setText(_translate("ToolWidget", "..."))
        self.toolButton.setText(_translate("ToolWidget", "..."))
        self.btnDiagnostics.setText(_translate("ToolWidget", "..."))
        self.btnInfo.setText(_translate("ToolWidget", "..."))
        self.btnBack.setText(_translate("ToolWidget", "..."))
        self.btnHome.setText(_translate("ToolWidget", "..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ToolWidget = QtWidgets.QWidget()
    ui = Ui_ToolWidget()
    ui.setupUi(ToolWidget)
    ToolWidget.show()
    sys.exit(app.exec_())
