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
#_from = input("请输入始发站：")
from_station = sta.set_station_name(input("请输入始发站："))
# 目的地
#_to = input("请输入到达站：")
to_station = sta.set_station_name(input("请输入到达站："))

# 出发时间
train_date = input("请输入出发日期(XX-XX—XX)：")
search = ti.TicketInquiry(train_date, from_station, to_station)
print(search.print_ticket())