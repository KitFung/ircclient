import sys
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from ui import NavigationBar, SocketEstablishScene, CommunicationScene
from irc import IRCClient


class ConnectionScene(QWidget):
    def __init__(self):
        super().__init__()

        self.irc = IRCClient()
        self.importStyle()
        self.initUI()

    def importStyle(self):
        with open('style/main.stylesheet', 'r') as f:
            self.setStyleSheet(f.read())

    def initUI(self):
        self.setWindowTitle('ircclient')
        self.setObjectName("MainWindow")
        self.resize(823, 454)

        naviBar = NavigationBar(self)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        naviBar.setSizePolicy(sizePolicy)

        self.horizon = QHBoxLayout(self)
        self.horizon.addWidget(naviBar)
        self.set_SocketEstablishScene()

        self.show()

    def remove_contentScene(self):
        if self.horizon.count() > 1:
            self.horizon.itemAt(1).widget().deleteLater()

    def set_SocketEstablishScene(self):
        self.remove_contentScene()
        contentArea = SocketEstablishScene(self, self.irc)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        contentArea.setSizePolicy(sizePolicy)
        self.horizon.addWidget(contentArea)

    def set_CommunicationScene(self):
        self.remove_contentScene()
        contentArea = CommunicationScene(self, self.irc)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(8)
        contentArea.setSizePolicy(sizePolicy)
        self.horizon.addWidget(contentArea)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    m = ConnectionScene()
    sys.exit(app.exec_())
