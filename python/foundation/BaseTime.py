# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseTime.py
@Author     :wooght
@Date       :2024/3/13 14:55
@Content    :时间,定时应用
"""

import time
print(time.time())      # time stamp 获取当前时间戳 1970年1月1日0时0分0秒为0开始累加

"""
    结构化时间 struct_time
    localtime(time_stamp) 获取结构化时间 默认当前本地时间    将时间戳转化为元祖化的时间对象
    gmtime(time_stamp)    默认世界时间
    mktime()              逆函数,将结构化时间转换为时间戳
    tm_year     当前年份
    tm_mon      当前月份
    tm_mday     当前几号
    tm_hour     当前几时
    tm_min      当前几分
    tm_sec      当前几秒
    tm_wday     当前周几    实际-1
    tm_yday     当前一年的第几天
    
"""
now_struct = time.localtime()       # 当前时间结构
print(now_struct.tm_year)     # 2024
print(now_struct.tm_mon)      # 3
print(now_struct.tm_zone)     # 中国标准时间
print(now_struct.tm_min + 4)  # 时间可以进行计算
print(time.mktime(now_struct))
print(time.gmtime())        # time.struct_time(tm_year=2024, tm_mon=3, tm_mday=13, tm_hour=7, tm_min=3, tm_sec=24, tm_wday=2, tm_yday=73, tm_isdst=0)
print(time.gmtime().tm_zone)        # UTC

"""
    格式化时间
    time.strftime(tpl,struct_time) 将时间对象转换为字符串  tpl:时间格式    struct_time: 结构化时间对象
    time.strptime(str,tpl)  strftime的逆函数, 将时间字符串转换为格式化时间对象
    流程:时间戳->结构化时间->格式化时间
    时间格式控制符:
    %Y,%m,%d,%H,%M,%S,%I,%p    分别是:年,月,日,时,分,秒,时(12小时制),上下午(AM,MP)
"""

tec = time.localtime(time.time())
print(time.strftime("%Y-%m-%d %H:%M:%S", tec))      # 2024-03-13 15:09:31
print(time.strptime('2023-10-01 22:22:22', "%Y-%m-%d %H:%M:%S"))    # time.struct_time(tm_year=2023, tm_mon=10, tm_mday=1, tm_hour=22, tm_min=22, tm_sec=22, tm_wday=6, tm_yday=274, tm_isdst=-1)

"""
    计时
    time.perf_counter()     获取CPU纳秒时钟
"""
start_time = time.perf_counter()
print('开始时间:',start_time)
test_list = [(x, y) for x in range(10) for y in range(10)]
print(test_list)
time.sleep(1.1)
end_time = time.perf_counter()

print('结束时间:',end_time)
print("共用时间", end_time- start_time)

"""
    应用:计算时间差
"""
start_datetime = '2020-02-2'
end_datetime = '2023-12-31'

start_struct = time.strptime(start_datetime, '%Y-%m-%d')
end_struct = time.strptime(end_datetime, '%Y-%m-%d')
start_stamp = time.mktime(start_struct)
end_stamp = time.mktime(end_struct)
print(int((end_stamp-start_stamp)/(3600*24)), '天')      # 1428 天