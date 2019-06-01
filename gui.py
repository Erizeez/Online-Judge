# -*- coding: utf-8 -*-
"""
Created on Wed May 29 15:22:47 2019

@author: 张勇成 18231171
"""

import tkinter
from repository import main

space_value = False

def codes_submit():
    codes_data = text_codes.get('1.0', 'end')
    test_data = text_test.get('1.0', 'end')
    time_limit_temp = entry_time.get()
    ram_limit_temp = entry_ram.get()
    main.test_codes(codes_data, test_data, time_limit_temp, ram_limit_temp, space_value)
def clear_all():
    text_codes.delete('1.0', 'end')
def window_destroy():
    root.destroy()
def space_yes():
    global space_value
    space_value = True
def space_no():
    global space_value
    space_value = False

root = tkinter.Tk()
root.geometry('1024x768+0+0')
root.title('OJ在线评测系统')

label_title = tkinter.Label(root, text = 'OJ在线评测系统', font = ('Microsoft YaHei Light', 25))
text_codes = tkinter.Text(root, width = 45, height = 22, borderwidth = 10, font = ('Microsoft YaHei Light', 15), undo = True)
label_codes = tkinter.Label(root, text = '代码框', font = ('Microsoft YaHei Light', 15))
text_test = tkinter.Text(root, width = 41, height = 10, borderwidth = 10, font = ('Microsoft YaHei Light', 15), undo = True)
label_test = tkinter.Label(root, text = '测试框', font = ('Microsoft YaHei Light', 15))
label_time = tkinter.Label(root, text = '时间限制(ms):', font = ('Microsoft YaHei Light', 15))
label_ram = tkinter.Label(root, text = '内存限制(mb):', font = ('Microsoft YaHei Light', 15))
label_space = tkinter.Label(root, text = '是否严格限制空格与换行', font = ('Microsoft YaHei Light', 15))
entry_time = tkinter.Entry(root, font = ('Microsoft YaHei Light', 15), width = 8)
entry_ram = tkinter.Entry(root, font = ('Microsoft YaHei Light', 15), width = 8)
button_clear = tkinter.Button(root, text = '清除所有', font = ('Microsoft YaHei Light', 15), width = 10, command = clear_all)
button_submit = tkinter.Button(root, text = '提交', font = ('Microsoft YaHei Light', 15), width = 10, command = codes_submit)
button_exit = tkinter.Button(root, text = '退出', font = ('Microsoft YaHei Light', 15), width = 10, command = window_destroy)
button_space_yes = tkinter.Button(root, text = '是', font = ('Microsoft YaHei Light', 15), width = 10, command = space_yes)
button_space_no = tkinter.Button(root, text = '否', font = ('Microsoft YaHei Light', 15), width = 10, command = space_no)

label_title.pack(side = tkinter.TOP)
text_codes.place(x = 10, y = 100)
label_codes.place(x = 230, y = 60)
text_test.place(x = 536, y = 100)
label_test.place(x = 740, y = 60)
label_time.place(x = 550, y = 450)
label_ram.place(x = 550, y = 500)
label_space.place(x = 550, y = 550)
entry_time.place(x = 700, y = 450)
entry_ram.place(x = 700, y = 500)
button_clear.place(x = 100, y = 720)
button_submit.place(x = 320, y = 720)
button_exit.place(x = 850, y = 720)
button_space_yes.place(x = 620, y = 600)
button_space_no.place(x = 810, y = 600)

tkinter.mainloop()