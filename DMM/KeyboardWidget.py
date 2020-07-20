import sys
import threading
import sip
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import Qt
from PyQt5.QtWidgets import *
import IRScanner


class KeyboardWidget(QWidget):
    updateText = pyqtSignal(str)
    def __init__(self, parent=None, title='Keyboard', GUI=None, mode=None, scanner = False):
        super(KeyboardWidget, self).__init__(parent)
        self.currentTextBox = None
        self.setGeometry(0, 0, 800, 480)
        self.setWindowTitle(title)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)
        self.signalMapper = QSignalMapper(self)
        self.signalMapper.mapped[int].connect(self.buttonClicked)

        self.GUI = GUI
        self.MODE = mode
        self.SHIFT = False
        self.initUI()
        if scanner is True:
            self.updateText.connect(self.text_box.setText)
            th = threading.Thread(target=self.initBarcodeScanner, args=())
            th.start()


    def initBarcodeScanner(self):
        try:
            print('startIRScanCom')
            self.updateText.emit("Please use scanner...")
            self.IR = IRScanner.IRScanner()
            irbarcode = self.IR.scanIRCODE()
            if irbarcode != 'ERROR':
                self.updateText.emit(irbarcode)
            else:
                self.updateText.emit('No Scan Code Found')

        except Exception as e:
            print('startIRScanCom Error:', e)

    def updateScanCode(self, code):
        self.text_box.setText(code)

    def initUI(self):
        layout = QGridLayout()

        # p = self.palette()
        # p.setColor(self.backgroundRole(),Qt.white)
        # self.setPalette(p)
        self.setAutoFillBackground(True)
        self.text_box = QTextEdit()
        self.text_box.setFont(QFont('Arial', 12))

        self.text_box.setFixedHeight(50)
        # self.text_box.setFixedWidth(300)
        layout.addWidget(self.text_box, 0, 0, 1, 13)

        names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                 '1', '2', '3', '4', '5', '5', '7', '8', '9', '0', '/', '*', '-',
                 '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', ':', '?', '+',
                 ',', '.', '<', '>', '\\', ';', '|', '{', '}', '`', '~', '_','"']

        positions = [(i + 1, j) for i in range(5) for j in range(13)]

        for position, name in zip(positions, names):

            if name == '':
                continue
            button = QPushButton(name)
            button.setFont(QFont('Arial', 12))
            button.setFixedHeight(50)
            button.setFixedWidth(50)
            button.setStyleSheet("background-color:#403E3E; color:white; border:none;")
            button.KEY_CHAR = ord(name)
            button.clicked.connect(self.signalMapper.map)
            self.signalMapper.setMapping(button, button.KEY_CHAR)
            layout.addWidget(button, *position)

        # Cancel button
        cancel_button = QPushButton('Cancel')
        cancel_button.setFixedHeight(75)
        cancel_button.setFont(QFont('Arial', 12))
        cancel_button.KEY_CHAR = Qt.Key_Cancel
        layout.addWidget(cancel_button, 6, 0, 1, 2)
        cancel_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(cancel_button, cancel_button.KEY_CHAR)
        cancel_button.setFixedWidth(100)
        cancel_button.setStyleSheet("background-color:red; color:white; border:none;")

        # Cancel button
        clear_button = QPushButton('Clear')
        clear_button.setFixedHeight(75)
        clear_button.setFont(QFont('Arial', 12))
        clear_button.KEY_CHAR = Qt.Key_Clear
        layout.addWidget(clear_button, 6, 2, 1, 2)
        clear_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(clear_button, clear_button.KEY_CHAR)
        clear_button.setFixedWidth(100)
        clear_button.setStyleSheet("background-color:#36362E; color:white; border:none;")

        # Space button
        space_button = QPushButton('Space')
        space_button.setFixedHeight(75)
        space_button.setFont(QFont('Arial', 12))
        space_button.KEY_CHAR = Qt.Key_Space
        layout.addWidget(space_button, 6, 4, 1, 3)
        space_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(space_button, space_button.KEY_CHAR)
        space_button.setFixedWidth(100)
        space_button.setStyleSheet("background-color:#36362E; color:white; border:none;")

        # Back button
        back_button = QPushButton('Back')
        back_button.setFixedHeight(75)
        back_button.setFont(QFont('Arial', 12))
        back_button.KEY_CHAR = Qt.Key_Backspace
        layout.addWidget(back_button, 6, 7, 1, 2)
        back_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(back_button, back_button.KEY_CHAR)
        back_button.setFixedWidth(100)
        back_button.setStyleSheet("background-color:#36362E; color:white; border:none;")

        # Enter button
        enter_button = QPushButton('Shift')
        enter_button.setFixedHeight(75)
        enter_button.setFont(QFont('Arial', 12))
        enter_button.KEY_CHAR = Qt.Key_Shift
        layout.addWidget(enter_button, 6, 9, 1, 2)
        enter_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(enter_button, enter_button.KEY_CHAR)
        enter_button.setFixedWidth(100)
        enter_button.setStyleSheet("background-color:#36362E; color:white; border:none;")

        # Done button
        done_button = QPushButton('Done')
        done_button.setFixedHeight(75)
        done_button.setFont(QFont('Arial', 12))
        done_button.KEY_CHAR = Qt.Key_Home
        layout.addWidget(done_button, 6, 11, 1, 2)
        done_button.clicked.connect(self.signalMapper.map)
        self.signalMapper.setMapping(done_button, done_button.KEY_CHAR)
        done_button.setFixedWidth(110)
        done_button.setStyleSheet("background-color:green; color:white; border:none;")

        self.setGeometry(0, 0, 800, 480)
        self.setLayout(layout)

    def buttonClicked(self, char_ord):

        txt = self.text_box.toPlainText()

        if char_ord == Qt.Key_Backspace:
            txt = txt[:-1]
        elif char_ord == Qt.Key_Shift:
            #txt += chr(10)
            if self.SHIFT is True:
                self.SHIFT = False
            else:
                self.SHIFT = True

        elif char_ord == Qt.Key_Home:
            self.GUI.DOCID = txt
            self.GUI.OPENKEYBORADACTIONSTAT = True
            self.GUI.showMainWindowAgain(self.MODE)
            self.close()
        elif char_ord == Qt.Key_Cancel:
            self.GUI.OPENKEYBORADACTIONSTAT = False
            self.GUI.showMainWindowAgain(self.MODE)
            self.close()
        elif char_ord == Qt.Key_Clear:
            txt = ""
        elif char_ord == Qt.Key_Space:
            txt += ' '
        else:
            if self.SHIFT is True:
                t = chr(char_ord)
                t = t.lower()
                txt += t
            else:
                txt += chr(char_ord)

        self.text_box.setText(txt)
