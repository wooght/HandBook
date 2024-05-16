# -- coding: utf-8 -
"""
@project    :HandBook
@file       :thread_speed.py
@Author     :wooght
@Date       :2024/5/16 21:06
@Content    :多线程速度测试
"""

import threading as th
import multiprocessing as mp
import time
from functools import wraps
def timer(func):
    @wraps(func)        # 将原函数的元信息拷贝到装饰函数中,要不然函数元信息会变成装饰器的元函数信息
    def inner_func():
        t = time.time()
        rts = func()
        print(f'用时{time.time() - t : .5f} 秒')
        return rts
    return inner_func


def euler_func(n: int) -> int:
    res = n
    i = 2
    while i <= n // i:
        if n % i == 0:
            res = res // i * (i - 1)
            while (n % i == 0): n = n // i
        i += 1
    if n > 1:
        res = res // n * (n - 1)
    return res

nums = 500000   # 50000 这里执行两个数据做比较
task1 = list(range(2, nums, 3))  # 2, 5, ...
task2 = list(range(3, nums, 3))  # 3, 6, ...
task3 = list(range(4, nums, 3))  # 4, 7, ...

def job(task: list):
    for t in task:
        euler_func(t)

@timer
def normal():  # 顺序串行执行
    job(task1)
    job(task2)
    job(task3)

@timer
def mutlthread():  # 多线程调用
    th1 = th.Thread(target=job, args=(task1,))
    th2 = th.Thread(target=job, args=(task2,))
    th3 = th.Thread(target=job, args=(task3,))
    # start() ，告诉线程/进程：你可以开始干活了,程序主逻辑还得继续往下运行
    th1.start()
    th2.start()
    th3.start()
    # 到 join() 这里，咱们是指让线程/进程阻塞住咱的主逻辑，比如p1.join()是指：p1不干完活，我主逻辑不往下进行（属于是「阻塞」）
    th1.join()
    th2.join()
    th3.join()


@timer
def multcore():  # 多进程调用
    p1 = mp.Process(target=job, args=(task1,))
    p2 = mp.Process(target=job, args=(task2,))
    p3 = mp.Process(target=job, args=(task3,))
    # start() ，告诉线程/进程：你可以开始干活了,程序主逻辑还得继续往下运行
    p1.start()
    p2.start()
    p3.start()
    # 到 join() 这里，咱们是指让线程/进程阻塞住咱的主逻辑，比如p1.join()是指：p1不干完活，我主逻辑不往下进行（属于是「阻塞」）
    p1.join()
    p2.join()
    p3.join()

# if __name__ == '__main__':
#     print('串行:'); normal()          # 顺序执行
#     print('并发:'); mutlthread()      # 多线程执行,中间会增加切换时间
#     print('并行:'); multcore()        # 开启进程的资源更多,所以时间更多
"""
    结果:
        nums = 50000 时:
            串行: 0.111
            并行: 0.112
            并发: 0.189
        nums = 150000 是:
            串行: 0.534
            并发: 0.539
            并行: 0.381

    理解:
        顺序执行    python默认执行过程,将上下文传递给解释器,由上往下依次解释
        并发执行    多个线程交替进行,速度和顺序执行一样,但会增加切换线程的时间,但切换时间极短,整体和默认执行时间相当
                  应用意义:作为服务端,如果并发量较大,那么后进者会等待前进者执行完才执行,需要等待过长时间.
                          如果用多线程并发模式,将交替进行,前进者执行一段,后进者也执行一段,然后几乎同时返回结果.
        并行执行    启动多个进程,上面两者都是一个进程.故启动进程时间花销较大.但计算量较大时,可以同时计算,速度更快
                  应用意义:服务器允许的情况下,可以实现真正的同时进行,如启动多个爬虫
"""

"""
    观察并发和并行的区别
"""
import random
def timer_args(func):
    @wraps(func)        # 将原函数的元信息拷贝到装饰函数中,要不然函数元信息会变成装饰器的元函数信息
    def inner_func(*args, **kwargs):
        t = time.time()
        rts = func(*args, **kwargs)
        print(f'用时{time.time() - t : .5f} 秒')
        return rts
    return inner_func
@timer_args
def run(name, speed):
    total_distance = 100
    while total_distance > 0:
        total_distance -= speed
        sleep_time = random.randint(1,8)
        print(f'{time.time()}:{name}进行中...,休息{sleep_time}秒')
        time.sleep(sleep_time)


def t_run():
    st_time = time.time()
    t_run1 = th.Thread(name='one', target=run, args=('one', 10))
    t_run2 = th.Thread(name='two', target=run, args=('two', 10))

    t_run1.start()
    t_run2.start()
    t_run1.join()
    t_run2.join()
    print(f'总花销:{time.time() - st_time : .5f}秒')
def mh_run():
    st_time = time.time()
    p_run1 = mp.Process(target=run, args=('one', 10))
    p_run2 = mp.Process(target=run, args=('two', 10))
    p_run1.start()
    p_run2.start()
    p_run1.join()
    p_run2.join()
    print(f'总花销:{time.time() - st_time : .5f}秒')

if __name__ == '__main__':
    mh_run()

"""
    结果:
        time.sleep()    都是暂停自己的线程,不会暂停同一进程的其他线程
"""