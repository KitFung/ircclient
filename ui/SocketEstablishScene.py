import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore


class SocketEstablishScene(QWidget):

    connection_signal = QtCore.pyqtSignal()

    def __init__(self, parent, ircObj):
        super().__init__(parent)
        self.delegate = parent
        self.ircObj = ircObj
        self.initUI()
        self.initSignalSlot()

    def initUI(self):
        self.vboxList = QVBoxLayout(self)
        self.vboxList.setObjectName("SocketScene")
        self.vboxList.setContentsMargins(10, 25, 25, 25)
        self.vboxList.setSpacing(6)

        self.addressField = QLineEdit(self)
        self.portField = QLineEdit(self)
        self.addressField.returnPressed.connect(self.connect_irc)
        self.portField.returnPressed.connect(self.connect_irc)

        self.top_spacer = QWidget(self)
        self.top_spacer.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding)
        self.bot_spacer = QWidget(self)
        self.bot_spacer.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding)

        self.vboxList.addWidget(self.top_spacer)
        self.vboxList.addWidget(self.addressField)
        self.vboxList.addWidget(self.portField)
        self.vboxList.addWidget(self.bot_spacer)

        self.show()

    def initSignalSlot(self):
        self.connection_signal.connect(self.success_connect)

    def connect_irc(self):
        # ircaddr = self.addressField.text()
        # ircport = self.portField.text()
        # self.ircObj.set_address()
        self.ircObj.connect(self.connection_signal)

    def success_connect(self):
        self.delegate.set_CommunicationScene()
