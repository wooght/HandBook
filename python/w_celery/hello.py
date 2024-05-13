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

backend = 'redis://192.168.101.103:6379/0'
broker = 'redis://192.168.101.103:6379/1'

hello_celery = Celery('hello', broker=broker, backend=backend)

@hello_celery.task
def say(x, y):
    time.sleep(5)
    return x + y


# @celery.task
# def send_email():
#     time.sleep(5)
#     print('in send_email')
#     return 'ok'


if __name__ == '__main__':
    say('Hello','World')
    # print(say('Hello', 'World'))
    # send_email()
