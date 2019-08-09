#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 19-7-3 上午10:19 
# @Author : Yuqiao
# @Site :  
# @File : train.py
# @Software: PyCharm
import requests
import datetime
import prettytable as pt
import check as ch
import station as sta

class TicketInquiry:


    # 123056列车请求路径
    sturl = 'https://kyfw.12306.cn/otn/leftTicket/query?'

    def __init__(self, train_date, from_station, to_station):
        self.train_date = train_date
        self.from_station = from_station
        self.to_station = to_station

    def get_ticket_url(self):
        try:
            if ch.check_date(self.train_date):
                url = self.sturl + 'leftTicketDTO.train_date=' + self.train_date \
                      + '&leftTicketDTO.from_station=' + self.from_station \
                      + '&leftTicketDTO.to_station=' + self.to_station \
                      + '&purpose_codes=ADULT'
                return url
        except ValueError:
            print('时间输入有误')

    def get_results(self):
        url = self.get_ticket_url()
        headers = {
            'User-Agent': r'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }
        req = requests.get(url, headers = headers)
        results = req.json()['data']['result']
        return results

    # def handle_results(self,results):
    #     for i in results:
    #         trains_info = str(i).split('|')
    #
    #     return trains_info

    def get_seat_count(self, count):
        if not str(count).strip():
            return '--'
        else:
            return count

    def arrival_time(self, start_time, trains_time):
        try:
            time1 = datetime.datetime.strptime(start_time, "%H:%M")
            time2 = datetime.datetime.strptime(trains_time, "%H:%M")
        except ValueError as e:
            return '时间异常'
        hour = 0
        if time1.minute + time2.minute >= 60:
            hour = 1

        if time1.hour + time2.hour + hour > 24:
            return "次日到达"
        else:
            return "今日到达"

    def print_ticket(self):
        results = self.get_results()
        tb = pt.PrettyTable()
        tb.field_names = ["车次", "车站", "时间", "历时", "商务座or特等座", "一等座", "二等座", "高级软卧", "软卧",
                          "动卧", "硬卧", "软座", "硬座", "无座"]
        for i in results:
            trains_info = str(i).split('|')
            from_station = trains_info[6]
            to_station = trains_info[7]
            from_station_name = sta.get_station_name(from_station)
            to_station_name = sta.get_station_name(to_station)
            start_time = trains_info[8]
            arrival_time = trains_info[9]
            trains_time = trains_info[10]
            tb.add_row([trains_info[3], from_station_name + "\n" + to_station_name, start_time + "\n" + arrival_time,
                        trains_time + "\n" + self.arrival_time(start_time, trains_time),
                        self.get_seat_count(trains_info[32]), self.get_seat_count(trains_info[31]),
                        self.get_seat_count(trains_info[30]), self.get_seat_count(trains_info[21]),
                        self.get_seat_count(trains_info[23]), self.get_seat_count(trains_info[33]),
                        self.get_seat_count(trains_info[28]), self.get_seat_count(trains_info[24]),
                        self.get_seat_count(trains_info[29]), self.get_seat_count(trains_info[26])])

        return tb


