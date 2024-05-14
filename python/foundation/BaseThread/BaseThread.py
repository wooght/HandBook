# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseThread.py
@Author     :wooght
@Date       :2024/3/13 20:23
@Content    :线程基础
"""
import os
from threading import Thread
import time
import random

"""
    Thread 线程
    Thread(target=function,arge=位置参数,kwargs=字典参数)
    .start() 开始线程
    .join() 回收线程
"""
# 主进程和线程比较200米跑步
total_distance = 100
def run(person, distance,speed):
    while distance < total_distance:
        step = random.random() * speed
        distance += round(step,4)
        print(person, '跑了', round(distance,2), '米了')
        time.sleep(1)
    print('{}线程结束'.format(person))


T = Thread(target=run, args=('puwenfeng', 2, 12))       # 开启线程
T.start()                                               # start 线程运行

run('wooght',1, 10)
T.join()    # 结束线程
print('主线程结束')