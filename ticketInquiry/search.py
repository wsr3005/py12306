#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 19-7-3 上午10:08
# @Author : Yuqiao
# @Site :
# @File : search.py
# @Software: PyCharm
import ticketInquiry as ti
import station as sta
# 出发地
from_station = sta.set_station_name('北京')

# 目的地
to_station = sta.set_station_name('武汉')

# 出发时间
train_date = '2019-07-03'
search = ti.TicketInquiry(train_date,from_station,to_station)
print(search.print_ticket())