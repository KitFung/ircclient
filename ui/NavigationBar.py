import sys
import random
from PyQt5.QtWidgets import (
    QWidget, QApplication,
    QPushButton, QVBoxLayout,
    QSizePolicy
)
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class NavigationBar(QWidget):

    itemName = ['A', 'B', 'C', 'D', 'E']

    def __init__(self, parent):
        super().__init__(parent)

        self.initUI()

    def initUI(self):
        self.setObjectName("naviBar")

        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)

        self.vboxList = QVBoxLayout(self)
        self.vboxList.setContentsMargins(0, 0, 0, 0)
        self.vboxList.setSpacing(6)
        self.initBtnList(self.vboxList)

    def initBtnList(self, vBox):
        for name in self.itemName:
            btn = QPushButton(name, self)
            vBox.addWidget(btn)
