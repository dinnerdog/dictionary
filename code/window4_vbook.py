# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window4_vbook.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChildWindow_4(object):
    def setupUi(self, VBook):
        VBook.setObjectName("VBook")
        VBook.resize(723, 527)
        self.label_2 = QtWidgets.QLabel(VBook)
        self.label_2.setGeometry(QtCore.QRect(490, 110, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(VBook)
        self.label_3.setGeometry(QtCore.QRect(600, 110, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(VBook)
        self.pushButton.setGeometry(QtCore.QRect(510, 240, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(VBook)
        self.pushButton_2.setGeometry(QtCore.QRect(510, 380, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(VBook)
        self.widget.setGeometry(QtCore.QRect(20, 24, 441, 481))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)

        self.retranslateUi(VBook)
        QtCore.QMetaObject.connectSlotsByName(VBook)

    def retranslateUi(self, VBook):
        _translate = QtCore.QCoreApplication.translate
        VBook.setWindowTitle(_translate("VBook", "VBook"))
        self.label_2.setText(_translate("VBook", "收藏词汇总数:"))
        self.label_3.setText(_translate("VBook", "0"))
        self.pushButton.setText(_translate("VBook", "删除选中项"))
        self.pushButton_2.setText(_translate("VBook", "清空单词本"))
        self.label.setText(_translate("VBook", "单词本"))

