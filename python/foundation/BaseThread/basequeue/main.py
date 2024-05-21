# -- coding: utf-8 -
"""
@project    :HandBook
@file       :main.py
@Author     :wooght
@Date       :2024/5/17 17:10
@Content    :进程之间通信
"""
import multiprocessing
import time
import random
import signal
"""
    signal.signal()
        两个参数 收到的信号值     采取的行动
        signal.SIGCHLD  终止信号
        signal.SIG_IGN  忽略子进程,释放内存
    此方法针对僵尸进程:子进程终止了,但主进程不知道,就没有释放内存
"""
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
def run_process(queue):
    for i in range(10):
        wait_time = random.randint(1,5)
        if i == 5:
            queue.put('已经运行到第{}次了'.format(i))
        if wait_time > 3:
            queue.put('第{}次等待{}秒'.format(i,wait_time))
        time.sleep(wait_time)
    queue.put('kill')

if __name__ == '__main__':
    queue = multiprocessing.Queue()
    p = multiprocessing.Process(target=run_process, args=(queue,))
    p.start()

    while True:
        if not p.is_alive():break
        result = queue.get(True)        # 接受通信,并释放通信
        if result == 'kill':
            print('子进程{}关闭{}'.format(p.pid, p.exitcode))
            break
        print(result)
    p.join()
    print(p.exitcode)