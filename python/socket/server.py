#!/usr/bin/python3
# encoding: utf-8
'''
    socket 测试 服务端
    author wooght
    date    2017-10-25

    @module socket,threading
'''
from socket import *
import time
import threading
from threading import Timer

#设置TCP socket对象
#socket(family,type)
#family AF_UNIX 同一台机器通信 AF_INET IPV4通信
#type SOCK_STREAM 流套接字 SOCK_DGRAM 报文套接字
sockobj=socket(AF_INET,SOCK_STREAM)
#bind(地址,端口)
#地址 ''表示localhost
sockobj.bind(('',8001))
#监听,设置监听数量上限
sockobj.listen(10)

thread=[]#线程池
connect=[]#连接池
next=1#连接记数

'''
    @连接响应模块
    @init 等待客户端连接
    @clientrun 和客户端交互
'''
class socketclass():
    def __init__(self):
        #accept 等待客户消息 得到两个元素 前面是socket对象 后者是地址
        self.connection,self.address=sockobj.accept()

    def clientrun(self):
        print('与客户端:',self.address,'建立连接')
        while True:
            #读取客户端套接字的下一行
            try:
                data=self.connection.recv(1024).decode()
            #except ConnectionResetError: Python 3.5提示ConnectionResetError is not defined
            except:
                print('客户:',self.address,'退出')
                break
            if not data:break
            if data=='1':
                print('输入的是1')
            #向客户端发送数据
            data1=int(data)+1
            time.sleep(0.5)
            try:
                self.connection.send(str(data1).encode())
            except:
                print('客户端',self.address,'连接中断')
                break
        self.connection.close()

#开启线程操作
class ThreadClass(threading.Thread):
    def run(self):
        connect[-1].clientrun()

#建立第一个连接
connect.append(socketclass())

#等待上一个连接成功后,执行下一个连接
while connect[-1]:
    #注册一个线程
    thread.append(ThreadClass())
    #开始线程
    thread[-1].start()
    print(next)
    next+=1
    #实例下一个连接响应对象
    connect.append(socketclass())
