# -- coding: utf-8 -
"""
@project    :HandBook
@file       :DateTimeMath.py
@Author     :wooght
@Date       :2024/3/13 17:13
@Content    : 日期计算模块
"""
import time
import random


class DateTimeMath:
    time_stamp = time.time()  # 当前时间戳
    time_struct = time.localtime()  # 当前时间结构
    datetime_model = "%Y-%m-%d %H:%M:%S"  # 完整时间格式
    date_model = "%Y-%m-%d"  # 日期格式
    time_model = "%H:%M:%S"  # 时间格式
    time_tpl = time.strftime(datetime_model, time_struct)  # 当前输出时间

    def __init__(self):
        self.now_date = time.strftime(self.date_model, self.time_struct)
        self.now_time = time.strftime(self.time_model, self.time_struct)

    def __str__(self):
        """ 实例化后默认得到当前日期时间 """
        return str(self.time_tpl)

    def pass_day(self, start_date, end_date=''):
        """ 返回两个日期相差天数 """
        start_struct = self.str_to_struct(start_date)
        start_stamp = self.mktime(start_struct)
        if not end_date:
            cha_stamp = self.time_stamp - start_stamp
        else:
            end_struct = self.str_to_struct(end_date)
            end_stamp = self.mktime(end_struct)
            cha_stamp = end_stamp - start_stamp
        return int(cha_stamp / (24 * 3600))

    def is_leap(self, year=0):
        """是否闰年"""
        year = self.time_struct.tm_year if not year else year
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    def month_days(self, year=0, month=0):
        """ 返回当月天数 """
        if not year:
            year = self.time_struct.tm_year
            month = self.time_struct.tm_mon
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 28 if not self.is_leap(year) else 29

    def date_list(self, start_date, end_state=0):
        """
            返回日期序列
            RETURN: ["%Y-%m-%d"....]
        """
        if not end_state: end_state = self.now_date
        start_stamp = self.str_to_stamp(start_date)
        pass_days = self.pass_day(start_date, end_state)
        for day in range(pass_days + 1):
            yield time.strftime(self.date_model, time.localtime(start_stamp + day * 3600 * 24))

    def get_day(self, target_date):
        """
            返回给定日期的年月日周
            RETURN:{Y:num,m:num,d:num,wk:num}
        """
        if not target_date: target_date = self.now_date
        return self.str_to_struct(target_date)

    def str_to_struct(self, str_date):
        """
        返回时间结构
        :param str_date: 输入时间格式 2020-10-10 10:10:10
        :return: 时间结构
        """
        t_model = self.datetime_model if len(str_date) > 10 else self.date_model
        time_struct = time.strptime(str_date, t_model)
        return time_struct

    def str_to_stamp(self, str_date):
        return self.mktime(self.str_to_struct(str_date))

    def mktime(self, struct):
        return time.mktime(struct)

    def stamp_to_str(self, stamp):
        return time.strftime(self.datetime_model, time.localtime(stamp))

    def run_time(self):
        return time.time() - self.time_stamp

    def wait_random(self, num):
        random_num = random.randint(1, num)
        time.sleep(random_num)
        return random_num

    def real_time(self):
        """
        返回实时时间
        :return: %H:%M:%S
        """
        return time.strftime(self.time_model, time.localtime())

    def before_day(self, days=30):
        """
        得到给定days前的日期和时间戳
        Parameters
        ----------
        days 默认30天
        Returns [date,stamp]
        -------
        """
        before_stamp = self.time_stamp - 24 * 3600 * days
        before_datetime = self.stamp_to_str(before_stamp)
        date = before_datetime.split(' ')[0]
        date_stamp = self.str_to_stamp(before_datetime)
        return [date, int(date_stamp)]



WDate = DateTimeMath()
if __name__ == "__main__":
    print(WDate)
    print("今天是", WDate.time_struct.tm_mday, "号")
    print("现在时间是:", WDate.now_time)
    print("当前时间戳是:", WDate.time_stamp)

    print(WDate.str_to_struct("2024-12-28 00:00:00"))
    print(WDate.pass_day('2018-10-07 0:0:0', "2024-03-14 0:0:0"), "天")
    print(WDate.str_to_stamp('2018-10-07 0:0:0'))
    print('给定时间戳得到日期:', WDate.stamp_to_str(1538841600))
    print('2020是闰年吗:', WDate.is_leap(2024))
    print("2018年2月有多少天:", WDate.month_days(2018, 2))
    date_list = WDate.date_list('2022-10-28')
    print(list(date_list))
    date_list = WDate.date_list('2024-3-10')
    print("下一天是:", date_list.__next__())
    print('2022-10-7是星期几:', WDate.get_day('2022-10-10').tm_wday)
    print("共运行时间:", WDate.run_time())
    print(WDate.before_day())
