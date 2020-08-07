from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys

from functools import partial

DEFAULT_LABEL_STRING = "Enter your name"

class KeyboardWidget(QtWidgets.QDialog):
    def __init__(self, MainWindow):
        super(KeyboardWidget, self).__init__()
        uic.loadUi('keyboardwidget.ui', self)

        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WA_ShowWithoutActivating)

        self.MainWindow = MainWindow
        self.key_buttons = []

        self.key_list_by_lines_lower = [ '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '\\',
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'",
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', ' ', '.com' ]
        
        self.key_list_by_lines_caps = [ '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '\\',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'",
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', ' ', '.COM' ]

        self.key_list_by_lines_shift = [ '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '|',
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"',
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?', ' ', '.COM' ]

        self.initKeyboard()
        self.initConnections()

    def initKeyboard(self, Src = None, LabelText = DEFAULT_LABEL_STRING, EchoMode = QtWidgets.QLineEdit.Normal):
        self.Capslock = False
        self.Shift = False
        self.key_capslock.setChecked(False)
        self.key_shift.setChecked(False)

        self.Label.setText(LabelText)
        self.lineEdit.setEchoMode(EchoMode)
        self.source = Src

        if Src is None:
            self.lineEdit.setText("")
        else:
            self.lineEdit.setText(Src.getText())

    def initConnections(self):
        self.key_buttons.append(self.key_accent)
        self.key_buttons.append(self.key_1)
        self.key_buttons.append(self.key_2)
        self.key_buttons.append(self.key_3)
        self.key_buttons.append(self.key_4)
        self.key_buttons.append(self.key_5)
        self.key_buttons.append(self.key_6)
        self.key_buttons.append(self.key_7)
        self.key_buttons.append(self.key_8)
        self.key_buttons.append(self.key_9)
        self.key_buttons.append(self.key_0)
        self.key_buttons.append(self.key_minus)
        self.key_buttons.append(self.key_equal)
        self.key_buttons.append(self.key_q)
        self.key_buttons.append(self.key_w)
        self.key_buttons.append(self.key_e)
        self.key_buttons.append(self.key_r)
        self.key_buttons.append(self.key_t)
        self.key_buttons.append(self.key_y)
        self.key_buttons.append(self.key_u)
        self.key_buttons.append(self.key_i)
        self.key_buttons.append(self.key_o)
        self.key_buttons.append(self.key_p)
        self.key_buttons.append(self.key_backslash)
        self.key_buttons.append(self.key_a)
        self.key_buttons.append(self.key_s)
        self.key_buttons.append(self.key_d)
        self.key_buttons.append(self.key_f)
        self.key_buttons.append(self.key_g)
        self.key_buttons.append(self.key_h)
        self.key_buttons.append(self.key_j)
        self.key_buttons.append(self.key_k)
        self.key_buttons.append(self.key_l)
        self.key_buttons.append(self.key_semicolon)
        self.key_buttons.append(self.key_apos)
        self.key_buttons.append(self.key_z)
        self.key_buttons.append(self.key_x)
        self.key_buttons.append(self.key_c)
        self.key_buttons.append(self.key_v)
        self.key_buttons.append(self.key_b)
        self.key_buttons.append(self.key_n)
        self.key_buttons.append(self.key_m)
        self.key_buttons.append(self.key_comma)
        self.key_buttons.append(self.key_fullstop)
        self.key_buttons.append(self.key_slash)
        self.key_buttons.append(self.key_space)
        self.key_buttons.append(self.key_dotcom)

        for x in range(47):
            self.key_buttons[x].clicked.connect(partial(self.key_pressed, x))

        self.key_reject.clicked.connect(self.reject)

    def key_pressed(self, index):
        print(index)
        key_to_add = self.key_list_by_lines_lower[index]
        eventPress = QtGui.QKeyEvent(QtCore.QEvent.KeyPress, QtCore.Qt.Key_1, QtCore.Qt.NoModifier, key_to_add)
        QtCore.QCoreApplication.postEvent(self.lineEdit, eventPress)
        eventRelease = QtGui.QKeyEvent(QtCore.QEvent.KeyRelease, QtCore.Qt.Key_1, QtCore.Qt.NoModifier, key_to_add)
        QtCore.QCoreApplication.postEvent(self.lineEdit, eventRelease)
        self.key_left.animateClick(100)