from PyQt5 import QtCore, QtGui, QtWidgets, uic

from Config import _App

class EmailSetupDialog(QtWidgets.QDialog):
    def __init__(self, parent):
        super(EmailSetupDialog, self).__init__()
        uic.loadUi('emaildialog.ui', self)

        self.parent = parent

        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WA_ShowWithoutActivating)
        self.setModal(True)

        self.smtp_server = _App._Settings.SMTP_SERVER
        self.smtp_port = _App._Settings.SMTP_PORT
        self.smtp_email = _App._Settings.SMTP_EMAIL
        self.smtp_pwd = _App._Settings.SMTP_PWD
        self.smtp_ccemail = _App._Settings.SMTP_CCEMAIL

        self.editServer.setText(self.smtp_server)
        self.editPort.setText(str(self.smtp_port))
        self.editEmail.setText(self.smtp_email)
        self.editPassword.setText(self.smtp_pwd)
        self.editCcemail.setText(self.smtp_ccemail)

        try:
            self.btnBack.clicked.disconnect()
            self.btnSave.clicked.disconnect()
            self.editServer.cursorPositionChanged.disconnect()
            self.editPort.cursorPositionChanged.disconnect()
        except:
            pass

        self.btnBack.clicked.connect(self.on_btnBack_clicked)
        self.btnSave.clicked.connect(self.on_btnSave_clicked)
        self.editServer.cursorPositionChanged.connect(self.on_editServer_changed)
        self.editPort.cursorPositionChanged.connect(self.on_editPort_changed)

    def on_editServer_changed(self):
        r = self.parent.MainWindow.showKeyboard(self.smtp_server, "Enter SMTP Server")

        if r:
            self.smtp_server = _App.KEYBOARD_TEXT[0]
            self.editServer.setText(self.smtp_server)
    
    def on_editPort_changed(self):
        r = self.parent.MainWindow.showKeyboard(str(self.smtp_port), "Enter SMTP Port")

        if r:
            self.smtp_port = int(_App.KEYBOARD_TEXT[0])
            self.editPort.setText(str(self.smtp_port))

    def on_btnBack_clicked(self):
        self.reject()

    def on_btnSave_clicked(self):
        _App._Settings.SMTP_SERVER = self.smtp_server
        _App._Settings.SMTP_PORT = self.smtp_port
        _App._Settings.SMTP_EMAIL = self.smtp_email
        _App._Settings.SMTP_PWD = self.smtp_pwd
        _App._Settings.SMTP_CCEMAIL = self.smtp_ccemail
        _App._Settings.saveSMTPConfig()

        self.accept()