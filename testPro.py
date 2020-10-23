import sys
from Pro import  Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QTimer
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

''' 
参考博客
https://www.cnblogs.com/ubuntu1987/archive/2004/01/13/12191633.html
https://www.pythonf.cn/read/108311
'''


class Pyqt5Serial(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Pyqt5Serial, self).__init__()
        self.setupUi(self)
        self.init()
        self.setWindowTitle("转台上位机")
        self.ser = serial.Serial()
        # self.port_check()

    def init(self):

        # 打开串口按钮
        self.btn_open.clicked.connect(self.port_open)

        # 关闭串口按钮
        self.btn_close.clicked.connect(self.port_close)

        # 发送数据按钮
        self.btn_send.clicked.connect(self.data_send)


        self.radioButton1.setChecked(True)
        self.radioButton1.toggled.connect(self.buttonState)
        self.radioButton2.toggled.connect(self.buttonState)

        # self.timer_send = QTimer()

    # 打开串口
    def port_open(self):
        self.ser.port = self.cmb_port_name.currentText()
        self.ser.baudrate = 460800
        self.ser.bytesize = 8
        self.ser.stopbits = 1

        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, "Port Error", "此串口不能被打开！")
            return None

        if self.ser.isOpen():
            self.btn_open.setEnabled(False)
            self.btn_close.setEnabled(True)

    # 关闭串口
    def port_close(self):
        try:
            self.ser.close()
        except:
            pass
        self.btn_open.setEnabled(True)
        self.btn_close.setEnabled(False)

    # 发送数据
    def data_send(self):
        if self.ser.isOpen():
            print("OK")
            input_1 = bytes(self.data_edit1.text(), encoding='utf-8')
            input_2 = bytes(self.data_edit2.text(), encoding='utf-8')
            input_s = input_1 + input_2
            print(input_s)
            if input_s != "":
                # 非空字符串
                data = QtCore.QByteArray(input_s)
                self.ser.write(data)
        else:
            pass

    def buttonState(self):
        radioButton = self.sender()
        if  radioButton.text() =='速度运行模式':
            if radioButton.isChecked() == True:
                print('<' + radioButton.text() + '>被选中')
            else:
                print('<' + radioButton.text() + '>取消选中')
        if radioButton.text() == '位置运行模式':
            if radioButton.isChecked() == True:
                print('<' + radioButton.text() + '>被选中')
            else:
                print('<' + radioButton.text() + '>取消选中')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myshow = Pyqt5Serial()
    myshow.show()
    sys.exit(app.exec_())






# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     mainWindow = QMainWindow()
#     ui = Pro.Ui_MainWindow()
#     ui.setupUi(mainWindow)
#     mainWindow.show()
#     sys.exit(app.exec_())
