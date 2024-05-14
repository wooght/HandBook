# -- coding: utf-8 -
"""
@project    :HandBook
@file       :ThreadLock.py
@Author     :wooght
@Date       :2024/5/14 21:49
@Content    :线程锁
"""
import threading
from threading import Thread, Lock
import time

class Account:
    def __init__(self, card_id, balance):
        self.card_id = card_id
        self.balance = balance

def withdraw(account, money):
    if lock.locked():
        print('{}无法访问账号,等待重试'.format(threading.current_thread().name))
        time.sleep(1)
        lock.release()
        print('{}解锁取款成功'.format(threading.current_thread().name))
    lock.acquire()      # 获得锁
    if account.balance > money:
        time.sleep(3)
        # current 当前        current_thread 当前线程
        account.balance -= money
        print("{}取出{}钱,剩余{}".format(threading.current_thread().name, money, account.balance))

    elif account.balance < money:
        print("{}显示余额不足,余额为:{}".format(threading.current_thread().name, account.balance))
    if lock.locked():
        lock.release()      # 释放锁

acct = Account('8888', 900)
lock = Lock()
T1 = Thread(name='窗口A', target=withdraw, args=(acct, 600))
T1.start()
T2 = Thread(name='窗口B', target=withdraw, args=(acct, 300))
T2.start()
T1.join()
T2.join()
"""
    Lock锁:谁都可以解锁
    RLock锁,谁上锁,谁解锁, 解铃还须系铃人
"""

def open_door(t):
    name = threading.current_thread().name
    try:
        rlock.acquire()
        print('{}上锁成功'.format(name))
        time.sleep(t)
    except:
        print('已经上锁,{}无法上锁'.format(name))
        return False
    print('{}已经解锁'.format(name))
    rlock.release()

rlock = threading.RLock()
Thread(name='路人甲', target=open_door, args=(6,)).start()
Thread(name='路人乙', target=open_door, args=(2,)).start()
"""
    上锁,就像上厕所一样,前面的人没出来,后面的人就只有等
"""