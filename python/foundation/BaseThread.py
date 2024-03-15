# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseThread.py
@Author     :wooght
@Date       :2024/3/13 20:23
@Content    :
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
totle_distance = 200

def run(person, distance,speed):
    while distance < totle_distance:
        step = random.random() * speed
        distance += round(step,2)
        print(person, '跑了', round(distance,2), '米了')
        time.sleep(1)
T = Thread(target=run, args=('puwenfeng',0,10))
T.start()

run('wooght',0, 10)

T.join()