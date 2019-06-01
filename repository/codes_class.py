# -*- coding: utf-8 -*-
"""
Created on Wed May 29 00:00:33 2019

@author: 张勇成 18231171
"""

import time
import subprocess
import memory_profiler

def data_modify(data):
    result = [[], []]
    temp = data.split('-----')
    for eachone in temp:
        temp_0 = eachone.split('#####')
        result[0].append(temp_0[0].lstrip('\n'))
        result[1].append(temp_0[1].lstrip('\n'))
    return result
class CodeTest:
    def __init__(self, input_data, check_data, space, time_limit, ram_limit):
        self.input_data = input_data
        self.check_data = check_data
        self.space = space
        self.time_limit = time_limit / 1000
        self.ram_limit = ram_limit
    def code_run(self):
        try:
            start_time = time.clock()
            temp = subprocess.Popen('temp.py', stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = True, universal_newlines = True)
            memory_use_max = memory_profiler.memory_usage(proc = temp.pid, max_usage = True)
            res = temp.communicate(self.input_data, self.time_limit)
            temp.kill()
            end_time = time.clock()
            all_time = end_time - start_time
            
        except Exception as err:
            end_time = time.clock()
            print(str(err))
            if 'timed out' in str(err):
                res = [None, 'TLE']
                all_time = 'Out'
            else:
                res = [None, 'Traceback']
                all_time = end_time - start_time
        return [res, all_time, memory_use_max]
    def output_judge(self, target):
        if 'Traceback' in target[0][1] or 'SyntaxError' in target[0][1]:
            return 'CE'
        elif target[1] == 'Out':
            return 'TLE'
        elif target[2] > self.ram_limit:
            return 'MLE'
        elif self.space == True:
            if target[0][0] == self.check_data:
                return 'AC'
            else:
                return 'WA'
        elif self.space == False:
            temp_output = target[0][0].split()
            temp_check = self.check_data.split()
            if temp_output == temp_check:
                return 'AC'
            else:
                return 'WA'

        
    
        
