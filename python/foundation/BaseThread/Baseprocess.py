# -- coding: utf-8 -
"""
@project    :HandBook
@file       :Baseprocess.py
@Author     :wooght
@Date       :2024/5/16 23:23
@Content    :多进程
"""
import multiprocessing
from multiprocessing import Process
import os

def run_proc(name):
    print("运行process是{}, ID是{}".format(multiprocessing.current_process().name, os.getpid()))

if __name__ == '__main__':
    run_proc('主机')
    new_proc = Process(name='子进程', target=run_proc, args=('子进程',))
    new_proc.start()
    new_proc.join()     # 等待子进程的结果,子进程执行完了再执行主进程
    print('所有进程执行完毕,关闭系统')
    """
    结果:
    运行process是MainProcess, ID是24136
    运行process是子进程, ID是4672
    所有进程执行完毕,关闭系统
    """

"""
    multiprocessing.Process 
    参数:
        group   分组
        target  调用对象,就是此进程调用的函数名
        name    进程的签名
        args    调用对象的位置参数
        kwargs  调用对象的字典参数
    方法:
        close()     关闭进程
        is_alive()  进程是否在运行
        join()      等待join之前的内容执行完毕后再执行后面的内容
        start()     进程准备就绪,等待CPU调用
        run()       start()默认调用run()方法
                    如果实例化时,没有传入target参数,则调用run()方法
                    
    属性:
        pid     进程ID
        name    进程签名
"""