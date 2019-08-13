# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 10:52
# @Author  : wsr
# @Site    : 
# @File    : Log.py
# @Software: PyCharm
from colorama import Fore


class Log(object):
    def _print(msg, color):
        if type(msg) == str:
            print(color+msg+Fore.RESET)
        else:
            print(color)
            print(msg)
            print(Fore.RESET)
            
    def login(msg):
        Log._print(msg, Fore.BLUE)
        
    def verify(msg):
        Log._print(msg, Fore.GREEN)
        
    def worn(msg):
        Log._print(msg, Fore.YELLOW)
        
    def error(msg):
        Log._print(msg, Fore.RED)
        
        
if __name__ == "__main__":
    pass