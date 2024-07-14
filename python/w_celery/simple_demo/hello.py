# -- coding: utf-8 -
"""
@project    :HandBook
@file       :hello.py
@Author     :wooght
@Date       :2024/5/11 17:26
@Content    :
"""

import time
from celery import Celery

backend = 'redis://192.168.101.103:6379/0'      # 存储任务结果及状态,将worker的执行结果返回给调用方
broker = 'redis://192.168.101.103:6379/1'       # 存储消息队列,负责接受任务请求,并转发值worker

hello_celery = Celery('hello', broker=broker, backend=backend)

@hello_celery.task      # 单词 task 任务
def say(x, y):
    time.sleep(5)
    return x + y


@hello_celery.task
def send_email():
    time.sleep(5)
    print('in send_email')
    return 'ok'


if __name__ == '__main__':
    say('Hello','World')
    # print(say('Hello', 'World'))
    # send_email()
