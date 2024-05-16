# -- coding: utf-8 -
"""
@project    :HandBook
@file       :thread_cpu.py
@Author     :wooght
@Date       :2024/5/16 20:37
@Content    :测试线程对CPU的利用
"""

from threading import Thread

def loop():
    while True:
        pass

if __name__ == '__main__':
    """
        CPU 涨了8%,评价14%
        意义: 实际为并发,宏观为同时执行,微观为高速切换,交替进行,实际只利用到单核CPU
            因为python解释器是上锁执行,然后解锁执行下一个线程.微观看,同时只执行了一个线程,一个CPU
            高并发一般讲的是多线程
    """
    for i in range(20):
        t = Thread(target=loop)
        t.start()

# from multiprocessing import Process
# if __name__ == '__main__':
#     """
#         CPU 直接干到100%
#         意义:同时运行多个独立的进程,每个进程拥有自己独立的内存和执行上下文,相互独立
#             一个CPU代表一个进程,可以同时利用多个CPU
#             并行一般指多进程
#     """
#     for i in range(20):
#         t = Process(target=loop)
#         t.start()

