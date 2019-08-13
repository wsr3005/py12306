# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 14:58
# @Author  : wsr
# @Site    : 
# @File    : Query.py
# @Software: PyCharm
import collections

import requests
import datetime
import prettytable as pt
from colorama import Fore

from framework.conf.CityCode import code2city, city2code
from framework.conf.Constant import PASSENGER_TYPE_ADULT
from framework.conf.Url import queryUrls

#  车次：3
from framework.utils.log.Log import Log
from framework.utils.net.NetUtils import EasyHttp
from train.query.TicketAttr import TicketAttr

INDEX_TRAIN_INFO = 3
#  start_station_code:起始站：4
INDEX_TRAIN_START_STATION_CODE = 4
#  end_station_code终点站：5
INDEX_TRAIN_END_STATION_CODE = 5
#  from_station_code:出发站：6
INDEX_TRAIN_FROM_STATION_CODE = 6
#  to_station_code:到达站：7
INDEX_TRAIN_TO_STATION_CODE = 7
#  start_time:出发时间：8
INDEX_TRAIN_LEAVE_TIME = 8
#  arrive_time:达到时间：9
INDEX_TRAIN_ARRIVE_TIME = 9
#  历时：10
INDEX_TRAIN_TOTAL_CONSUME = 10
#  商务特等座：32
INDEX_TRAIN_BUSINESS_SEAT = 32
#  一等座：31
INDEX_TRAIN_FIRST_CLASS_SEAT = 31
#  二等座：30
INDEX_TRAIN_SECOND_CLASS_SEAT = 30
#  高级软卧：21
INDEX_TRAIN_ADVANCED_SOFT_SLEEP = 21
#  软卧：23
INDEX_TRAIN_SOFT_SLEEP = 23
#  动卧：33
INDEX_TRAIN_MOVE_SLEEP = 33
#  硬卧：28
INDEX_TRAIN_HARD_SLEEP = 28
#  软座：24
INDEX_TRAIN_SOFT_SEAT = 24
#  硬座：29
INDEX_TRAIN_HARD_SEAT = 29
#  无座：26
INDEX_train_info_SEAT = 28
#  其他：22
INDEX_TRAIN_OTHER = 22
#  备注：1
INDEX_TRAIN_MARK = 1

INDEX_SECRET_STR = 0

INDEX_START_DATE = 13  # 车票出发日期


class Query:
    @staticmethod
    def query(flag, base_url, train_date, from_station, to_station, passengerType=PASSENGER_TYPE_ADULT):
        params = collections.OrderedDict()
        params['leftTicketDTO.train_date'] = train_date
        params['leftTicketDTO.from_station'] = city2code(from_station)
        params['leftTicketDTO.to_station'] = city2code(to_station)
        params['purpose_codes'] = "ADULT"
        
        if flag > 1:
            jsonRet = EasyHttp.send(queryUrls['query'], params=params)
        else:
            for suffix in ['', 'O', 'X', 'Z', 'A', 'T', 'V']:
                queryUrls['query']['url'] = base_url + suffix
                jsonRet = EasyHttp.send(queryUrls['query'], params=params)
                if jsonRet:
                    break
        try:
            if jsonRet:
                return Query._decode(jsonRet['data']['result'], passengerType)
        except Exception as e:
            Log.error(e)
        
        return []
    
    @staticmethod
    def _decode(query_results, passenger_type):
        for query_result in query_results:
            info = query_result.split('|')
            ticket = TicketAttr()
            ticket.passenger_type = passenger_type
            ticket.train_info = info[INDEX_TRAIN_INFO]
            ticket.start_station_code = info[INDEX_TRAIN_START_STATION_CODE]
            ticket.end_station_code = info[INDEX_TRAIN_END_STATION_CODE]
            ticket.from_station_code = info[INDEX_TRAIN_FROM_STATION_CODE]
            ticket.to_station_code = info[INDEX_TRAIN_TO_STATION_CODE]
            ticket.leave_time = info[INDEX_TRAIN_LEAVE_TIME]
            ticket.arrive_time = info[INDEX_TRAIN_ARRIVE_TIME]
            ticket.total_consume = info[INDEX_TRAIN_TOTAL_CONSUME]
            ticket.business_seat = info[INDEX_TRAIN_BUSINESS_SEAT]
            ticket.first_class_seat = info[INDEX_TRAIN_FIRST_CLASS_SEAT]
            ticket.second_class_seat = info[INDEX_TRAIN_SECOND_CLASS_SEAT]
            ticket.advanced_soft_sleeper = info[INDEX_TRAIN_ADVANCED_SOFT_SLEEP]
            ticket.soft_sleeper = info[INDEX_TRAIN_SOFT_SLEEP]
            ticket.move_sleeper = info[INDEX_TRAIN_MOVE_SLEEP]
            ticket.hard_sleeper = info[INDEX_TRAIN_HARD_SLEEP]
            ticket.soft_seat = info[INDEX_TRAIN_SOFT_SEAT]
            ticket.hard_seat = info[INDEX_TRAIN_HARD_SEAT]
            ticket.no_seat = info[INDEX_train_info_SEAT]
            ticket.other = info[INDEX_TRAIN_OTHER]
            ticket.note = info[INDEX_TRAIN_MARK]
            ticket.start_station = code2city(ticket.start_station_code)
            ticket.end_station = code2city(ticket.end_station_code)
            ticket.from_station = code2city(ticket.from_station_code)
            ticket.to_station = code2city(ticket.to_station_code)
            ticket.secret_str = info[INDEX_SECRET_STR]
            ticket.start_date = info[INDEX_START_DATE]
            yield ticket
            
    @staticmethod
    def output(train_data, from_station, to_station, passenger_type):
        tb = pt.PrettyTable()
        tb.field_names = ["车次", "车站", "时间", "历时", "商务座or特等座", "一等座", "二等座", "高级软卧", "软卧",
                          "动卧", "硬卧", "软座", "硬座", "无座", "其他", "备注"]
        base_query_url = queryUrls['query']['url']
        for ticket in Query.query(1, base_query_url, train_data, from_station, to_station):
            if not ticket:
                continue
            tb.add_row([ticket.train_info,
                       '\n'.join([Fore.GREEN + ticket.from_station + Fore.RESET,
                                  Fore.RED + ticket.to_station + Fore.RESET]),
                       '\n'.join([Fore.GREEN + ticket.leave_time + Fore.RESET,
                                 Fore.RED + ticket.arrive_time + Fore.RESET]),
                       ticket.total_consume,
                       ticket.business_seat or '--',
                       ticket.first_class_seat or '--',
                       ticket.second_class_seat or '--',
                       ticket.advanced_soft_sleeper or '--',
                       ticket.soft_sleeper or '--',
                       ticket.move_sleeper or '--',
                       ticket.hard_sleeper or '--',
                       ticket.soft_seat or '--',
                       ticket.hard_seat or '--',
                       ticket.no_seat or '--',
                       ticket.other or '--',
                       ticket.note or '--'])
        print(tb)
            
if __name__ == "__main__":
    Query.output('2019-08-15', '沙坪坝', '兰州', 'ADULT')