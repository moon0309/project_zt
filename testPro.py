import sys
from Pro import Ui_MainWindow
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
        self.active_button = ''
        self.POWER_ON = '55 AA 07 08 40 01 00 00 00 00 00 00 00 00 F0'
        self.POWER_OFF = '55 AA 07 08 80 01 00 00 00 00 00 00 00 00 F0'
        self.LOCK = '55 AA 07 08 10 01 00 00 00 00 00 00 00 00 F0'
        self.SERVO_OFF = '55 AA 07 08 01 01 00 00 00 00 00 00 00 00 F0'

    def init(self):

        # 打开串口按钮
        self.btn_open.clicked.connect(self.port_open)
        # 关闭串口按钮
        self.btn_close.clicked.connect(self.port_close)
        # 发送数据按钮
        # self.btn_send.clicked.connect(self.data_send)

        # self.radioButton1.setChecked(True)
        self.radioButton1.toggled.connect(self.button_state)
        self.radioButton2.toggled.connect(self.button_state)
        self.radioButton3.toggled.connect(self.no_edit)
        self.radioButton4.toggled.connect(self.no_edit)
        self.radioButton5.toggled.connect(self.no_edit)
        self.radioButton6.toggled.connect(self.no_edit)

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
    def data_send(self, operate_type1):
        if self.ser.isOpen():
            input_1 = bytes(self.data_edit1.text(), encoding='utf-8')
            print(type(input_1))
            input_2 = bytes(self.data_edit2.text(), encoding='utf-8')
            input_s = input_1 + input_2
            print(input_s)
            if input_s != "":          # 非空字符串
                data = QtCore.QByteArray(input_s)
                self.ser.write(data)
        else:
            pass

    ''' 功放、锁定、伺服选定时直接发送的数据 '''

    def str_data_send(self):

        if self.active_button == '功放上电':
            hex_command = bytes.fromhex(self.POWER_ON)
            self.ser.write(hex_command)
        elif self.active_button == '功放断电':
            hex_command = bytes.fromhex(self.POWER_OFF)
            self.ser.write(hex_command)
        elif self.active_button == '锁定':
            hex_command = bytes.fromhex(self.LOCK)
            self.ser.write(hex_command)
        elif self.active_button == '伺服关闭':
            hex_command = bytes.fromhex(self.SERVO_OFF)
            self.ser.write(hex_command)


    # 位置模式和速度模式按钮动作
    def button_state(self):
        radiobutton = self.sender()
        if radiobutton.text() == '速度运行模式' or radiobutton.text() == '位置运行模式':
            self.active_button = radiobutton.text()
            self.data_edit1.setFocusPolicy(QtCore.Qt.StrongFocus)
            self.data_edit2.setFocusPolicy(QtCore.Qt.StrongFocus)
            if radiobutton.isChecked() == True:
                print('<' + radiobutton.text() + '>被选中')
                # 发送数据按钮
                print('<' + radiobutton.text() + '>下的数据:')
                self.btn_send.disconnect()
                self.btn_send.clicked.connect(self.data_send)
            else:
                pass
                # print('<' + radiobutton.text() + '>取消选中')

    def no_edit(self):
        radiobutton = self.sender()
        if radiobutton.text() == '功放上电' or radiobutton.text() == '功放断电' or radiobutton.text() == '锁定' or radiobutton.text() == '伺服关闭':
            self.active_button = radiobutton.text()
            self.data_edit1.setFocusPolicy(QtCore.Qt.StrongFocus)
            self.data_edit2.setFocusPolicy(QtCore.Qt.StrongFocus)
            if radiobutton.isChecked() == True:
                print('<' + radiobutton.text() + '>被选中')
                # 发送数据按钮
                print('<' + radiobutton.text() + '>下的数据:')
                self.btn_send.disconnect()
                self.btn_send.clicked.connect(self.str_data_send)
            else:
                pass
        # self.data_edit1.setFocusPolicy(QtCore.Qt.NoFocus)
        # self.data_edit2.setFocusPolicy(QtCore.Qt.NoFocus)
        # print('不可用')
        # self.btn_send.disconnect()
        # self.btn_send.clicked.connect(self.str_data_send)


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


# def button_state(self):
#     radiobutton = self.sender()
#     if  radiobutton.text() =='速度运行模式':
#         if radiobutton.isChecked() == True:
#             print('<' + radiobutton.text() + '>被选中')
#             # 发送数据按钮
#             print('等待发送速度运行模式下的数据:' )
#             self.btn_send.clicked.connect(self.data_send)
#         else:
#             print('<' + radiobutton.text() + '>取消选中')
#     if radiobutton.text() == '位置运行模式':
#         if radiobutton.isChecked() == True:
#             print('<' + radiobutton.text() + '>被选中')
#             print('等待发送位置运行模式下的数据:')
#             self.btn_send.clicked.connect(self.data_send)
#         else:
#             print('<' + radiobutton.text() + '>取消选中')
