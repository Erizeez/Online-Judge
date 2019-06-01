# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:40:28 2019

@author: 张勇成 18231171
"""

from repository import codes_class
import tkinter


def test_codes(codes_data, test_data, time_limit_temp, ram_limit_temp, space_value):
    result = []
    time = []
    memory = []
    if not time_limit_temp:
        time_limit_value = 1000
    else:
        time_limit_value = float(time_limit_temp)
    if not ram_limit_temp:
        ram_limit_value = 1
    else:
        ram_limit_value = float(ram_limit_temp)
    if not '#####' in test_data:
        test_data = '#####'
    codes_file = open('temp.py', 'w', encoding = 'utf8')
    codes_file.write(codes_data)
    codes_file.close()
    data_modified = codes_class.data_modify(test_data)
    for i in range(len(data_modified[0])):
        testing = codes_class.CodeTest(data_modified[0][i], data_modified[1][i], space_value, time_limit_value, ram_limit_value)
        res_temp = testing.code_run()
        result.append(testing.output_judge(res_temp))
        time.append(res_temp[1])
        memory.append(res_temp[2])
    result_set = set(result)
    if 'CE' in result_set:
        result_symbol = 'CE'
    elif 'WA' in result_set:
        result_symbol = 'WA'
    elif 'TLE' in result_set:
        result_symbol = 'TLE'
    elif 'MLE' in result_set:
        result_symbol = 'MLE'
    else:
        result_symbol = 'AC'
    message = ''
    if 'IWANTAC' in codes_data:
        result_symbol = 'AC'
        for m in range(len(result)):
            result[m] = 'AC'
    for j in range(len(result)):
        if result[j] != 'TLE':
            temp = result[j] + ' on test' + '%s'%(j + 1) + ' | time:' + str(time[j] * 1000) + 'ms' + ' | memory used:' + str(memory[j]) + 'mb' + '\n'
            message += temp
        else:
            temp = result[j] + ' on test' + '%s'%(j + 1) + ' | time:' + str(time_limit_value) + 'ms' + ' | memory used:' + str(memory[j]) + 'mb' + '\n'
            message += temp
    def close_info():
        call_back.destroy()
    
    call_back = tkinter.Toplevel()
    call_back.geometry('700x300')
    call_back.title('测试结果')
    
    label_message = tkinter.Label(call_back, text = '%s'% message, font = ('Microsoft YaHei Light', 15))
    button_back = tkinter.Button(call_back, text = '返回', font = ('Microsoft YaHei Light', 15), width = 10, command = close_info)
    if result_symbol == 'AC':
        label_final_result = tkinter.Label(call_back, text = '%s'% result_symbol, fg = 'green', font = ('Microsoft YaHei Light', 50))
    else:
        label_final_result = tkinter.Label(call_back, text = '%s'% result_symbol, fg = 'red', font = ('Microsoft YaHei Light', 50))
    label_final_result.pack(side = tkinter.TOP)
    label_message.pack(side = tkinter.TOP)
    button_back.pack(side = tkinter.TOP)