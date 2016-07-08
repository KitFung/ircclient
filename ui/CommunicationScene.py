import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class CommunicationScene(QWidget):

    def __init__(self, parent, ircObj):
        super().__init__(parent)
        self.ircObj = ircObj
        self.initUI()
        self.initSignalSlot()
        self.ircObj.start_communication()

    def initUI(self):
        self.vboxList = QVBoxLayout(self)
        self.vboxList.setObjectName("CommunicationScene")
        self.vboxList.setContentsMargins(10, 25, 25, 25)
        self.vboxList.setSpacing(6)

        self.messageList = QListWidget(self)
        self.messageField = QLineEdit(self)
        self.messageField.returnPressed.connect(self.send_message)

        self.top_spacer = QWidget(self)
        self.top_spacer.setSizePolicy(
            QSizePolicy.Expanding,
            QSizePolicy.Expanding)

        self.vboxList.addWidget(self.messageList)
        self.vboxList.addWidget(self.top_spacer)
        self.vboxList.addWidget(self.messageField)

        self.show()

    def initSignalSlot(self):
        self.ircObj.new_message_signal.connect(self.receive_data)

    def send_message(self):
        message = self.messageField.text()
        self.ircObj.send_raw_cmd(message)
        self.messageField.clear()

    def receive_data(self, msg):
        self.messageList.addItem(QListWidgetItem(msg))
