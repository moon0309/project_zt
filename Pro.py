# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pro.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 761)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cmb_port_name = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_port_name.setObjectName("cmb_port_name")
        self.cmb_port_name.addItem("")
        self.cmb_port_name.addItem("")
        self.horizontalLayout.addWidget(self.cmb_port_name)
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setObjectName("btn_open")
        self.horizontalLayout.addWidget(self.btn_open)
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout.addWidget(self.btn_close)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton1.setObjectName("radioButton1")
        self.gridLayout.addWidget(self.radioButton1, 0, 0, 1, 1)
        self.radioButton2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton2.setObjectName("radioButton2")
        self.gridLayout.addWidget(self.radioButton2, 0, 1, 1, 1)
        self.radioButton6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton6.setObjectName("radioButton6")
        self.gridLayout.addWidget(self.radioButton6, 0, 5, 1, 1)
        self.radioButton4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton4.setObjectName("radioButton4")
        self.gridLayout.addWidget(self.radioButton4, 0, 3, 1, 1)
        self.radioButton3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton3.setObjectName("radioButton3")
        self.gridLayout.addWidget(self.radioButton3, 0, 2, 1, 1)
        self.radioButton5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton5.setObjectName("radioButton5")
        self.gridLayout.addWidget(self.radioButton5, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.data_edit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.data_edit1.setObjectName("data_edit1")
        self.horizontalLayout_2.addWidget(self.data_edit1)
        self.data_edit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.data_edit2.setObjectName("data_edit2")
        self.horizontalLayout_2.addWidget(self.data_edit2)
        self.btn_send = QtWidgets.QPushButton(self.centralwidget)
        self.btn_send.setObjectName("btn_send")
        self.horizontalLayout_2.addWidget(self.btn_send)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cmb_port_name.setItemText(0, _translate("MainWindow", "COM1"))
        self.cmb_port_name.setItemText(1, _translate("MainWindow", "COM2"))
        self.btn_open.setText(_translate("MainWindow", "打开"))
        self.btn_close.setText(_translate("MainWindow", "关闭"))
        self.radioButton1.setText(_translate("MainWindow", "速度运行模式"))
        self.radioButton2.setText(_translate("MainWindow", "位置运行模式"))
        self.radioButton6.setText(_translate("MainWindow", "伺服关闭"))
        self.radioButton4.setText(_translate("MainWindow", "功放断电"))
        self.radioButton3.setText(_translate("MainWindow", "功放上电"))
        self.radioButton5.setText(_translate("MainWindow", "锁定"))
        self.btn_send.setText(_translate("MainWindow", "发送"))

