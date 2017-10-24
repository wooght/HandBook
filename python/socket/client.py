'''
    socket 测试 客户端
    author wooght
    date 2017-10-21

    @module socket
'''

import sys
from socket import *

#发送的文本
message='Hello network world'
if len(sys.argv)>1:
    serverHost=sys.argv[1]
    if len(sys.argv)>2:
        serverHost=sys.argv[2:]

#建立tcp/ip套接字对象
sockobj=socket(AF_INET,SOCK_STREAM)
is_connect=True
try:
    sockobj.connect(('localhost',8001))
except ConnectionRefusedError:
    is_connect=False
    print('无法连接')
if is_connect:
    try:
        sockobj.send(str(5).encode())
    except:
        print('连接成功,但发送失败')
while True:
    if not is_connect:
        break
    #line=input('输入内容:')
    #发送数据
    #sockobj.send(line.encode())
    try:
        #接受数据
        data=sockobj.recv(1024)
        print(int(data))
        sockobj.send(str(int(data)).encode())
    except:
        print('与服务端失去连接')
        is_connect=False
sockobj.close()
