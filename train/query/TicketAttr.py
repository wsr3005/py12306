# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 14:41
# @Author  : wsr
# @Site    : 
# @File    : TicketAttr.py
# @Software: PyCharm
class TicketAttr(object):
    @property
    def train_info(self):
        return self._train_info
    @train_info.setter
    def train_info(self, train_info):
        self._train_info = train_info

    @property
    def from_station(self):
        return self._from_station
    @from_station.setter
    def from_station(self, from_station):
        self._from_station = from_station
       
    @property
    def to_station(self):
        return self._to_station
    @to_station.setter
    def to_station(self, to_station):
        self._to_station = to_station
        
    @property
    def start_station(self):
        return self._start_station
    @start_station.setter
    def start_station(self, start_station):
        self._start_station = start_station
        
    @property
    def end_station(self):
        return self._end_station
    @end_station.setter
    def end_station(self, end_station):
        self._end_station = end_station

    #  start_station_code:起始站：4
    @property
    def start_station_code(self):
        return self._start_station_code
    @start_station_code.setter
    def start_station_code(self, start_station_code):
        self._start_station_code = start_station_code

    #  end_station_code终点站：5
    @property
    def end_station_code(self):
        return self._end_station_code
    @end_station_code.setter
    def end_station_code(self, end_station_code):
        self._end_station_code = end_station_code

    #  from_station_code:出发站：6
    @property
    def from_station_code(self):
        return self._from_station_code
    @from_station_code.setter
    def from_station_code(self, from_station_code):
        self._from_station_code = from_station_code

    #  to_station_code:到达站：7
    @property
    def to_station_code(self):
        return self._to_station_code
    @to_station_code.setter
    def to_station_code(self, to_station_code):
        self._to_station_code = to_station_code

    #  start_time:出发时间：8
    @property
    def leave_time(self):
        return self._leave_time
    @leave_time.setter
    def leave_time(self, leave_time):
        self._leave_time = leave_time

    #  arrive_time:达到时间：9
    @property
    def arrive_time(self):
        return self._arrive_time
    @arrive_time.setter
    def arrive_time(self, arrive_time):
        self._arrive_time = arrive_time

    #  历时：10
    @property
    def total_consume(self):
        return self._total_consume
    @total_consume.setter
    def total_consume(self, total_consume):
        self._total_consume = total_consume

    #  商务特等座：32
    @property
    def business_seat(self):
        return self._business_seat
    @business_seat.setter
    def business_seat(self, business_seat):
        self._business_seat = business_seat

    #  一等座：31
    @property
    def first_class_seat(self):
        return self._first_class_seat
    @first_class_seat.setter
    def first_class_seat(self, first_class_seat):
        self._first_class_seat = first_class_seat

    #  二等座：30
    @property
    def second_class_seat(self):
        return self._second_class_seat
    @second_class_seat.setter
    def second_class_seat(self, second_class_seat):
        self._second_class_seat = second_class_seat

    #  高级软卧：21
    @property
    def advanced_soft_sleeper(self):
        return self._advanced_soft_sleeper
    @advanced_soft_sleeper.setter
    def advanced_soft_sleeper(self, advanced_soft_sleeper):
        self._advanced_soft_sleeper = advanced_soft_sleeper

    #  软卧：23
    @property
    def soft_sleeper(self):
        return self._soft_sleeper
    @soft_sleeper.setter
    def soft_sleeper(self, soft_sleeper):
        self._soft_sleeper = soft_sleeper

    #  动卧：33
    @property
    def move_sleeper(self):
        return self._move_sleeper
    @move_sleeper.setter
    def move_sleeper(self, move_sleeper):
        self._move_sleeper = move_sleeper

    #  硬卧：28
    @property
    def hard_sleeper(self):
        return self._hard_sleeper
    @hard_sleeper.setter
    def hard_sleeper(self, hard_sleeper):
        self._hard_sleeper = hard_sleeper

    #  软座：24
    @property
    def soft_seat(self):
        return self._soft_seat
    @soft_seat.setter
    def soft_seat(self, soft_seat):
        self._soft_seat = soft_seat

    #  硬座：29
    @property
    def hard_seat(self):
        return self._hard_seat
    @hard_seat.setter
    def hard_seat(self, hard_seat):
        self._hard_seat = hard_seat

    #  无座：26
    @property
    def no_seat(self):
        return self._no_seat
    @no_seat.setter
    def no_seat(self, no_seat):
        self._no_seat = no_seat

    #  其他：22
    @property
    def other(self):
        return self._other
    @other.setter
    def other(self, other):
        self._other = other

    #  备注：1
    @property
    def note(self):
        return self._note
    @note.setter
    def note(self, note):
        self._note = note
        
        
    @property
    def passenger_type(self):
        return self._passenger_type
    @passenger_type.setter
    def passenger_type(self, passenger_type):
        self._passenger_type = passenger_type
        
        
    @property
    def secret_str(self):
        return self._secret_str
    @secret_str.setter
    def secret_str(self, secret_str):
        self._secret_str = secret_str
        
        
    @property
    def start_date(self):
        return self._start_date
    @start_date.setter
    def start_date(self, start_date):
        self._start_date = start_date