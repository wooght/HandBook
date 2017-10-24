#coding: utf-8
import socket
import sys
encoding = 'utf-8'  
BUFSIZE = 65536
s = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_IP)
#绑定
s.bind(("192.168.8.132", 1147))
#设置socket选项
s.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,0)
s.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
i=0
while i<10:
    i=i+1
    pkt = s.recvfrom(BUFSIZE)
    pkt1=pkt[0]
    result_pkt=pkt[1]
    if(result_pkt[0]=='204.8.241.232'):
        print(pkt,end='-------\n')
        #u=chr(3255)
        #print(u.encode('utf-8'))
        #print(bytes.decode(pkt1,encoding))
        '''
encode函数和decode函数应用
        u=chr(1972)+'abc'
        print(u)
        print(u.encode('utf-8'))
        ss=b'\xde\xb4abc'
        print(ss.decode('utf-8'))
        '''
