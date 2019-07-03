#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 19-7-3 上午11:49 
# @Author : Yuqiao
# @Site :  
# @File : check.py 
# @Software: PyCharm
import datetime
import re


def check_date(date):
    # 判断日期格式
    date_text = re.search(r"(\d{4}-\d{2}-\d{2})", date)
    # 判断时间格式是否正确
    try:
        if date_text == None:
            return False

        date_text = date_text.group(0)

        if date_text != datetime.datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
            return False
        else:
            return True

    except ValueError:
        return False
