# -*- coding: utf-8 -*-
"""
Created on Wed May 29 00:00:33 2019

@author: 张勇成 18231171
"""

#本自定义库用于建立CodeTest类和对于测试数据的处理。

#调库。time库用于计算运行时间。subprocess用于建立CodeTest类
#以实现子进程以及相关操作。time_profiler用于内存监测。
import time
import subprocess
import memory_profiler

#测试数据处理函数。根据格式分割并去除左边可能会残留的换行符。

#注意：此处的操作严格保留初始格式。


#该函数将会返回一个二元列表，分别储存标准输入和预计输出（注意先后顺序）。
#即处理测试数据，将输入输出分离到一个二维列表的两个子列表。
def data_modify(data):
    result = [[], []]
    temp = data.split('-----')
    for eachone in temp:
        temp_0 = eachone.split('#####')
        result[0].append(temp_0[0].lstrip('\n'))
        result[1].append(temp_0[1].lstrip('\n'))
    return result

#建立CodeTest类，以便于处理测试代码和对应结果。


#注意：尽管程序支持多组数据，但此处仅支持处理单独一组，多组处理
#需要通过外部实现，详见main.py。
class CodeTest:
    #初始化基本属性。输入数据，预计输出数据，是否严格限制空格与换行的bool值，时间限制，内存限制。
    def __init__(self, input_data, check_data, space, time_limit, ram_limit):
        self.input_data = input_data
        self.check_data = check_data
        self.space = space
        #将单位转化成s。
        self.time_limit = time_limit / 1000
        self.ram_limit = ram_limit

    def code_run(self):
        #防止因Exception的直接跳出。
        try:
            #尽管不提倡clock，但出于提高对于单一进程的时间测算精度。
            start_time = time.clock()
            #调用subprocess库的Popen类，标准输入、输出、错误都用PIPE导出。在shell环境下运行且支持换行符。
            temp = subprocess.Popen('temp.py',
                                    stdin=subprocess.PIPE,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    shell=True,
                                    universal_newlines=True)
            #调用memory_profiler库的memory_usage以计算最大内存使用。将pid赋值给proc, max_usage为True以返回最大内存占用。
            memory_use_max = memory_profiler.memory_usage(proc=temp.pid,
                                                          max_usage=True)
            #用communicate传入标准输入，设定最长时间。
            res = temp.communicate(self.input_data, self.time_limit)
            #尽管communicate会自动清理进程，但考虑到python不靠谱的进程管理，小心不为过。
            temp.kill()
            end_time = time.clock()
            #计算运行时长。
            all_time = end_time - start_time
        #该报错将涵盖超时以及其他可能的Exception。
        except Exception as err:
            end_time = time.clock()
            #判断是否为超时错误。
            if 'timed out' in str(err):
                #返回TLE，尽管此处的TLE在后续中无用，但若改为None则会在某个call语句中报错。
                res = [None, 'TLE']
                #上行注释所述的判断的对象即为all_time。
                all_time = 'Out'
            else:
                #同理。Traceback用于上行所述的判断，位于main.py。
                res = [None, 'Traceback']
                #由于end_time赋值并不位于测试代码结束时，且若报错运行时长将毫无意义。
                #但为了测试结果不过于奇怪，同时添加判断代码以合理化输出。
                all_time = end_time - start_time
                if all_time > self.time_limit:
                    all_time = self.time_limit
        #返回res,运行时长，最大运行内存。
        return [res, all_time, memory_use_max]
    #通过上行返回的列表判断运行结果。返回结果字符串。
    def output_judge(self, target):
        if 'Traceback' in target[0][1] or 'SyntaxError' in target[0][1]:
            return 'CE'
        elif target[1] == 'Out':
            return 'TLE'
        elif target[2] > self.ram_limit:
            return 'MLE'
        #下述代码依据space的bool值判断是否需要严格限制空格即换行。
        elif self.space == True:
            if target[0][0] == self.check_data:
                return 'AC'
            else:
                return 'WA'
        #通过直接去除空格及空行实现。
        elif self.space == False:
            temp_output = target[0][0].split()
            temp_check = self.check_data.split()
            if temp_output == temp_check:
                return 'AC'
            else:
                return 'WA'