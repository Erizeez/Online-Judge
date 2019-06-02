# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:40:28 2019

@author: 张勇成 18231171
"""

#本自定义库为代码核心。
#注意：此处的调用看似错误，实则由于python的根目录调用机制，程序执行
#位于根目录，故所有自定义库调用基于运行代码，不基于相对于自定义库的
#相对地址。
from repository import codes_class
import tkinter

#主体运行函数。

#接收参数：代码，测试数据（包括输入输出），时间限制，内存限制，控制空格及换行限制的bool值。
def test_codes(codes_data, test_data, time_limit_temp, ram_limit_temp, space_value):
    #建立空列表。储存各测试点测试结果、花费时间和占用最大内存。
    result = []
    time = []
    memory = []
    
    #处理时间限制。默认为1000ms。
    
    #注意：若Entry不输入任何值，bool值为False。
    if not time_limit_temp:
        time_limit_value = 1000
    #浮点化时间限制。
    else:
        time_limit_value = float(time_limit_temp)
    #解释同上。内存限制默认为1mb。
    if not ram_limit_temp:
        ram_limit_value = 1
    else:
        ram_limit_value = float(ram_limit_temp)
    
    #防止测试框无任何数据导致程序无法分离输入输出而报错。
    #这意味着无输入输出。
    if not '#####' in test_data:
        test_data = '#####'
    
    #将测试代码储存到缓存文件。
    codes_file = open('temp.py', 'w', encoding = 'utf8')
    codes_file.write(codes_data)
    codes_file.close()
    
    #处理测试数据。分离各个测试点和对应输入输出。
    data_modified = codes_class.data_modify(test_data)
    
    #测试在各数据点情况下的代码运行情况。
    for i in range(len(data_modified[0])):
        #创建CodeTest实例。
        testing = codes_class.CodeTest(data_modified[0][i], data_modified[1][i], space_value, time_limit_value, ram_limit_value)
        #使用code_run方法以获得运行的反馈数据。
        res_temp = testing.code_run()
        
        #往三个空列表中添加各类测试反馈。
            #利用output_judge方法获得运行结果。
        result.append(testing.output_judge(res_temp))
        time.append(res_temp[1])
        memory.append(res_temp[2])
    
    #实现多测试点下的概括判定。
    #用set获得列表的元素种类。
    #优先级说明：CE > WA > TLE > MLE > AC。
    #即在所有测试结果中，程序将返回优先级最高的结果。
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
    
    #作弊码。只要测试代码中有该字符串，则只会输出AC。
    if 'IWANTAC' in codes_data:
        result_symbol = 'AC'
        for m in range(len(result)):
            result[m] = 'AC'
    
    #实现多测试点数据的格式化合并，以利于后续图形化界面上的显示。
    message = ''
    for j in range(len(result)):
        if result[j] != 'TLE':
            temp = result[j] + ' on test' + '%s'%(j + 1) + ' | time:' + str(time[j] * 1000) + 'ms' + ' | memory used:' + str(memory[j]) + 'mb' + '\n'
            message += temp
        else:
            temp = result[j] + ' on test' + '%s'%(j + 1) + ' | time:' + str(time_limit_value) + 'ms' + ' | memory used:' + str(memory[j]) + 'mb' + '\n'
            message += temp
            
    #定义反馈窗口的销毁函数。
    def close_info():
        call_back.destroy()
    
    #创建反馈窗口。
    call_back = tkinter.Toplevel()
    call_back.geometry('700x300')
    call_back.title('测试结果')
    #布置反馈信息和返回按钮。
    label_message = tkinter.Label(call_back, text = '%s'% message, font = ('Microsoft YaHei Light', 15))
    button_back = tkinter.Button(call_back, text = '返回', font = ('Microsoft YaHei Light', 15), width = 10, command = close_info)
    #实现概括判定为AC时的绿色字体显示。
    #和其他情况下红色字体显示。
    if result_symbol == 'AC':
        label_final_result = tkinter.Label(call_back, text = '%s'% result_symbol, fg = 'green', font = ('Microsoft YaHei Light', 50))
    else:
        label_final_result = tkinter.Label(call_back, text = '%s'% result_symbol, fg = 'red', font = ('Microsoft YaHei Light', 50))
    #打包各个组件，此处用pack是因为组件数目少。且此处可能有改变
    #窗口大小的需求，能保证窗口大小改变时也能保持相对位置。
    label_final_result.pack(side = tkinter.TOP)
    label_message.pack(side = tkinter.TOP)
    button_back.pack(side = tkinter.TOP)