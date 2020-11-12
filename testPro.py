import sys
from Pro import Ui_MainWindow
import serial
import serial.tools.list_ports
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import function_file
# from function_file import data_send_function


''' 
参考博客
https://www.cnblogs.com/ubuntu1987/archive/2004/01/13/12191633.html
https://www.pythonf.cn/read/108311
https://blog.csdn.net/liuxf196921/article/details/88165399
https://www.jianshu.com/p/d4c0169a28db
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
        self.POWER_ON = '55 AA 07 08 80 00 00 00 00 00 00 00 00 F0'
        self.POWER_OFF = '55 AA 07 08 00 00 00 00 00 00 00 00 00 F0'
        self.LOCK = '55 AA 07 08 10 00 00 00 00 00 00 00 00 F0'
        self.READ_DATA = '55 AA 07 08 00 FF 00 00 00 00 00 00 00 F0'
        # self.SERVO_OFF = '55 AA 07 08 01 01 00 00 00 00 00 00 00 00 F0'  伺服关闭


    def init(self):

        # 打开串口按钮
        self.btn_open.clicked.connect(self.port_open)
        # 关闭串口按钮
        self.btn_close.clicked.connect(self.port_close)
        # 发送数据按钮
        # self.btn_send.clicked.connect(self.data_send)

        # self.radioButton1.setChecked(True)
        self.radioButton1.toggled.connect(self.button_active)
        self.radioButton2.toggled.connect(self.button_active)
        self.radioButton_w.toggled.connect(self.button_active)
        self.radioButton3.toggled.connect(self.button_active_else)
        self.radioButton4.toggled.connect(self.button_active_else)
        self.radioButton5.toggled.connect(self.button_active_else)
        self.radioButton6.toggled.connect(self.button_active_else)
        self.btn_open.clicked.connect(self.data_receive)
        # 定时器接收数据
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.data_receive)

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

        # 打开串口接收定时器，周期为2ms
        self.timer.start(2)

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

    # 显示收发数据
    def dispContent(self, argvStr):
        pass

    # 发送数据
    def data_send(self):
        if self.ser.isOpen():
            if self.active_button == '速度运行模式':
                input_speed_initial1 = round(float(self.data_edit1.text()) * 100)
                input_speed_initial2 = round(float(self.data_edit2.text()) * 100)
                hex_command1, input_speed_form = function_file.data_send_function(input_speed_initial1, input_speed_initial2,
                                                                    '55 AA 07 08 03 00 ')
                self.ser.write(hex_command1)
                self.show_send.append(input_speed_form)

            elif self.active_button == '位置运行模式':
                input_speed_initial1 = round(float(self.data_edit1.text()) * 65536 / 360)
                input_speed_initial2 = round(float(self.data_edit2.text()) * 65536 / 360)
                hex_command1, input_speed_form = function_file.data_send_function(input_speed_initial1, input_speed_initial2,
                                                                    '55 AA 07 08 0C 00 ')
                self.ser.write(hex_command1)
                self.show_send.append(input_speed_form)

            elif self.active_button == '稳定运行模式':
                input_speed_initial1 = round(float(self.data_edit1.text()) * 100)
                input_speed_initial2 = round(float(self.data_edit2.text()) * 100)
                hex_command1, input_speed_form = function_file.data_send_function(input_speed_initial1, input_speed_initial2,
                                                                    '55 AA 07 08 60 00 ')
                self.ser.write(hex_command1)
                self.show_send.append(input_speed_form)

    #接收数据
    def data_receive(self):
        try:
            count = self.ser.inWaiting()
        except:
            self.port_close()
            return None
        if count != 0:
            dealStr = ''
            # 读串口数据
            recv = self.ser.read(count)
            # 在这里将接收到数据进行区分：hex 或 字符串
            # hex 格式：\xYY\xYY\xYY，如果接收到的字符是这种格式，则说明是hex字符，我们需要将
            # \x去除掉，取出YY，然后组成字符串返回
            # 如果接收到的是字符串，则使用decode进行解码
            print("接收到的数据 %s \n类型为: %s\n" % (recv, type(recv)))
            print(dealStr[12:16])
            print(type(dealStr[12:16]))

            try:
                dealStr = recv.decode()
            except (TypeError, UnicodeDecodeError):
                for i in range(len(recv)):
                    dealStr += hex(recv[i])[2:]
                    dealStr += ' '
            print("处理后的数据 %s \n类型为: %s\n" % (dealStr, type(dealStr)))


            dealStr_new = dealStr.replace(' ', '')  #去除首尾空格
            print(dealStr_new)
            print(type(dealStr_new))
            recv1 = str(dealStr_new[8:10])  # 当前运行模式
            print(recv1)
            if recv1 == '03':
                self.lineEdit_1.setText('速度运行模式')
            elif recv1 == '0C':
                self.lineEdit_1.setText('位置运行模式')
            elif recv1 == '10':
                self.lineEdit_1.setText('锁定')
            elif recv1 == '60':
                self.lineEdit_1.setText('稳定运行模式')
            elif recv1 == '80':
                self.lineEdit_1.setText('功放上电')
            elif recv1 == '00':
                self.lineEdit_1.setText('功放断电')
            else:
                pass
            recv2 = str(dealStr_new[10:12])  # 转台到位状态
            print(recv2)
            if recv2 == '01':
                self.lineEdit_2.setText('俯仰到位')
            elif recv2 == '10':
                self.lineEdit_2.setText('方位到位')
            else:
                pass

            recv3 = '0x' + str(dealStr_new[12:20])   #方位角速度
            recv3_er_new = function_file.data_receive_process(recv3, 32)
            self.lineEdit_3.setText(str(round(recv3_er_new, 2)))

            recv4 = '0x' + str(dealStr_new[20:28])   #俯仰角速度
            recv4_er_new = function_file.data_receive_process(recv4, 32)
            self.lineEdit_4.setText(str(round(recv4_er_new, 2)))

            recv5 = '0x' + str(dealStr_new[28:34])   #方位角度
            recv5_er_new = function_file.data_receive_process(recv5, 24)
            self.lineEdit_5.setText(str(round(recv5_er_new, 2)))

            recv6 = '0x' + str(dealStr_new[34:40])  # 俯仰角度
            recv6_er_new = function_file.data_receive_process(recv6, 24)
            self.lineEdit_6.setText(str(round(recv6_er_new, 2)))




    ''' 功放、锁定、伺服选定时直接发送的数据 '''
    def str_data_send(self):
        if self.active_button == '功放上电':
            hex_command = bytes.fromhex(self.POWER_ON)
            self.ser.write(hex_command)
            self.show_send.append(self.POWER_ON)
        elif self.active_button == '功放断电':
            hex_command = bytes.fromhex(self.POWER_OFF)
            self.ser.write(hex_command)
            self.show_send.append(self.POWER_OFF)
        elif self.active_button == '锁定':
            hex_command = bytes.fromhex(self.LOCK)
            self.ser.write(hex_command)
            self.show_send.append(self.LOCK)
        elif self.active_button == '取数指令':
            hex_command = bytes.fromhex(self.READ_DATA)
            self.ser.write(hex_command)
            self.show_send.append(self.READ_DATA)



    # 位置模式和速度模式按钮动作
    def button_active(self):
        radiobutton = self.sender()
        if radiobutton.text() == '速度运行模式' or radiobutton.text() == '稳定运行模式' or radiobutton.text() == '位置运行模式':
            self.active_button = radiobutton.text()
            self.data_edit1.setEnabled(True)
            self.data_edit2.setEnabled(True)
            if radiobutton.isChecked() == True:
                print('<' + radiobutton.text() + '>被选中')
                # 发送数据按钮
                print('<' + radiobutton.text() + '>下的数据:')
                self.btn_send.disconnect()
                self.btn_send.clicked.connect(self.data_send)
            else:
                pass

    # 功放、伺服关闭、断电按钮动作
    def button_active_else(self):
        radiobutton = self.sender()
        if radiobutton.text() == '功放上电' or radiobutton.text() == '功放断电' or radiobutton.text() == '锁定' or radiobutton.text() == '取数指令':
            self.active_button = radiobutton.text()
            self.data_edit1.setEnabled(False)
            self.data_edit2.setEnabled(False)

            if radiobutton.isChecked() == True:
                print('<' + radiobutton.text() + '>被选中')
                # 发送数据按钮
                print('<' + radiobutton.text() + '>下的数据:')
                self.btn_send.disconnect()
                self.btn_send.clicked.connect(self.str_data_send)
            else:
                pass



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


# print(-int(recv3_er[1:],2))
# recv3_er_new = reverse(recv3_er[1:])
# recv3_er_add = add_1(recv3_er_new)
#
# self.lineEdit_3.setText(str(round(-int(recv3_er_add[1:],2)/14800, 2)))
# bin(int('0x11', 16)) 十六进制数转二进制数 输出字符串类型
# print(-int(recv3_er_add[1:],2))
# print('1111111111111111111111')
