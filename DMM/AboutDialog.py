from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QScroller

class AboutDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(AboutDialog, self).__init__()
        uic.loadUi('aboutdialog.ui', self)

        self.parent = parent

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WA_ShowWithoutActivating)
        self.setModal(True)

        QScroller.grabGesture(self.scrollArea, QScroller.LeftMouseButtonGesture)

        self.ABOUT_TXT = 'about.txt'

        fp = open(self.ABOUT_TXT)
        data = fp.read()

        self.lblText.setText(data)

        self.btnBack.clicked.connect(self.on_btnBack_clicked)

    def on_btnBack_clicked(self):
        self.reject()