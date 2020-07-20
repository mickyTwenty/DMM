from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox


class TimerMessageBox(QMessageBox):
    def __init__(self, timeout=3, title='Information', message='Action Performed', parent=None):
        super(TimerMessageBox, self).__init__(parent)
        self.resize(300, 300)
        self.setStyleSheet("border:none;\n"
                           "color:#FFE41E;\n"
                           "background-color:#17202A;")
        self.setWindowTitle(title)
        self.time_to_wait = timeout
        self.setText(message)
        self.setStandardButtons(QMessageBox.NoButton)
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.changeContent)
        self.timer.start()

    def changeContent(self):
        self.time_to_wait -= 1
        if self.time_to_wait <= 0:
            self.close()

    def closeEvent(self, event):
        self.timer.stop()
        event.accept()
