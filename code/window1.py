# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication


class Ui_HomePage(object):
    def setupUi(self, HomePage):
        HomePage.setObjectName("HomePage")
        HomePage.resize(367, 516)
        HomePage.setStyleSheet("background-color: rgb(37, 45, 68);")
        self.label = QtWidgets.QLabel(HomePage)
        self.label.setGeometry(QtCore.QRect(90, 20, 191, 81))
        self.label.setStyleSheet("image: url(:/img/icon.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(HomePage)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 120, 271, 381))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButtonRecite = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRecite.sizePolicy().hasHeightForWidth())
        self.pushButtonRecite.setSizePolicy(sizePolicy)
        self.pushButtonRecite.setStyleSheet("background-color: #4a90e8;\n"
"font-size:22px;\n"
"font-family:\"Microsoft YaHei\";\n"
"color:#ebf6ff")
        self.pushButtonRecite.setObjectName("pushButtonRecite")
        self.verticalLayout_3.addWidget(self.pushButtonRecite)
        self.pushButtonSearch = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonSearch.setStyleSheet("background-color: #4a90e8;\n"
"font-size:22px;\n"
"font-family:\"Microsoft YaHei\";\n"
"color:#ebf6ff")
        self.pushButtonSearch.setObjectName("pushButtonSearch")
        self.verticalLayout_3.addWidget(self.pushButtonSearch)
        self.pushButtonWBook = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonWBook.setStyleSheet("background-color: #4a90e8;\n"
"font-size:22px;\n"
"font-family:\"Microsoft YaHei\";\n"
"color:#ebf6ff")
        self.pushButtonWBook.setObjectName("pushButtonWBook")
        self.verticalLayout_3.addWidget(self.pushButtonWBook)
        self.pushButtonQuit = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonQuit.setStyleSheet("background-color: #4a90e8;\n"
"font-size:22px;\n"
"font-family:\"Microsoft YaHei\";\n"
"color:#ebf6ff")
        self.pushButtonQuit.setObjectName("pushButtonQuit")
        self.verticalLayout_3.addWidget(self.pushButtonQuit)

        self.retranslateUi(HomePage)
        QtCore.QMetaObject.connectSlotsByName(HomePage)

    def retranslateUi(self, HomePage):
        _translate = QtCore.QCoreApplication.translate
        HomePage.setWindowTitle(_translate("HomePage", "简译"))
        self.pushButtonRecite.setText(_translate("HomePage", "背单词"))
        self.pushButtonSearch.setText(_translate("HomePage", "查单词"))
        self.pushButtonWBook.setText(_translate("HomePage", "单词本"))
        self.pushButtonQuit.setText(_translate("HomePage", "退出"))

import my_resources_rc

