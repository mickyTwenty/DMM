from PyQt5 import QtCore, QtGui, QtWidgets, uic

class EmailSetupDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(EmailSetupDialog, self).__init__()
        uic.loadUi('emaildialog.ui', self)

        self.parent = parent

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WA_ShowWithoutActivating)
        self.setModal(True)