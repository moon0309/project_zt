import  sys
# 发送数据


def data_send_sudu(str1, str2):
    global hex_command1
    global input_speed_form

    input_speed_initial1 = round(float(str1) * 100)
    input_speed_initial2 = round(float(str2) * 100)

    if input_speed_initial1 >= 0 and input_speed_initial2 >= 0:
        input_speed_1 = hex(input_speed_initial1)[2:].zfill(4)
        input_speed_2 = hex(input_speed_initial2)[2:].zfill(4)
        input_speed_form = '55 AA 07 08 03 00 ' + input_speed_1[0:2] + ' ' + str(input_speed_1)[2:] + ' ' + input_speed_2[0:2] + ' ' + str(input_speed_2)[2:] + ' 00 00 00 F0'
        hex_command1 = bytes.fromhex(input_speed_form)


    elif input_speed_initial1 < 0 and input_speed_initial2 < 0:
        input_speed_abs1 = hex(32768 - abs(input_speed_initial1) + 32768)
        input_speed_abs2 = hex(32768 - abs(input_speed_initial2) + 32768)
        input_speed_form = '55 AA 07 08 03 00 ' + input_speed_abs1[-4:-2] + ' ' + str(input_speed_abs1)[-2:] + ' ' + input_speed_abs2[-4:-2] + ' ' + str(input_speed_abs2)[-2:] + ' 00 00 00 F0'
        hex_command1 = bytes.fromhex(input_speed_form)

    elif input_speed_initial1 >= 0 and input_speed_initial2 < 0:
        input_speed_1 = hex(input_speed_initial1)[2:].zfill(4)
        input_speed_abs2 = hex(32768 - abs(input_speed_initial2) + 32768)
        input_speed_form = '55 AA 07 08 03 00 ' + input_speed_1[0:2] + ' ' + str(input_speed_1)[2:] + ' ' + input_speed_abs2[-4:-2] + ' ' + str(input_speed_abs2)[-2:] + ' 00 00 00 F0'
        hex_command1 = bytes.fromhex(input_speed_form)


    elif input_speed_initial1 < 0 and input_speed_initial2 >= 0:
        input_speed_abs1 = hex(32768 - abs(input_speed_initial1) + 32768)
        input_speed_2 = hex(input_speed_initial2)[2:].zfill(4)
        input_speed_form = '55 AA 07 08 03 00 ' + input_speed_abs1[-4:-2] + ' ' + str(input_speed_abs1)[-2:] + ' ' + input_speed_2[0:2] + ' ' + str(input_speed_2)[2:] + ' 00 00 00 F0'
        hex_command1 = bytes.fromhex(input_speed_form)

    else:
        pass

    return hex_command1, input_speed_form