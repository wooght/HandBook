# -*- coding: UTF-8 -*-
'''
    python 基础 by wooght 2017
'''

import time
import math
import random
import calendar

#日历
print(calendar.month(2017,10))

#时间
now_time=time.time()#time.time()当前微妙
time.sleep(1)#暂停允许 sleep
new_time=time.time()
print(new_time-now_time)
print('now:'+str(new_time))#类型转换str(),int()等等
print(time.localtime())#输出:time.struct_time(tm_year=2017, tm_mon=10, tm_mday=23, tm_hour=17, tm_min=9, tm_sec=9, tm_wday=0, tm_yday=296, tm_isdst=0)
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))#格式化时间 2017-10-23 17:10:54

'''输出'''
a='x';b='y'
print(a)
print(b,a) #同时输出多个,不换行

'''字符串'''
a=1
b=1.1
c="aabbcc"
print(a,b,c)
print(c[0:2])#输出字符串中的某一部分 不包括后边界

'''列表list,索引数组'''
arr=[1,'22',3];
print(arr*2)#输出两次
print(arr[1])
arr[0]=111;#重新赋值
print(arr)
arr[2]=[1,1000,3]#二维
print(arr)

'''元祖tuple'''
tuple=(1,'222',3);
print(tuple)
print(tuple[1])
#tuple[1]='333' 元祖不能重新赋值

'''字典dict,及关联数组'''
dict={'name':'wooght','age':18}
print(dict)
print(dict['name'])
dict['name']="puwenfeng"#重新赋值
print(dict['name'])
dict['height']=198
print(dict['height'])#添加新元素
dict['before']={'age':17,'name':'puwei'}
print(dict['before']['name'])#二维元祖
print(dict)
print('len:',len(dict['name']))#字符串长度
print('len:',len(dict))#字典长度
if('name' in dict):
    #判断key是否存在数组中
    print('name in dict')
else:
    print('name not in dict')

'''运算符'''
a="5+8*2"
print(eval(a))#eval 执行字符串表达式

#函数
def echo(var):
    print(var)
echo('aaa')
a=2;b=3
echo(a**b)#幂运算
a=3;b=23
echo(b//a)#整除的整数部分
echo(b%a)#返回余数
a=2;b=3
if(a==b):
    echo('ok')
else:
    echo('!=')

aa=[1,2,3,'a']
bb='a'
if(bb in aa):
    #//in 判断
    echo("bb in  aa")
else:
    echo ("not in")

a=111.111
print('%10.1f'%a)#格式化输出
#str=input('qing shu ru \n') 等待输入内容
print(random.randint(1,100))#随机数
arr=['abc','bcd','cde','def']#随机获取数组元素
print(random.choice(arr))


'''循环'''
#while循环
bnum=1
while bnum<10:
    bnum+=1
    echo(bnum)
#9*9乘法表
i=1
while i<10:
    j=1
    while j<=i:
        print("%dX%d=%d"%(j,i,i*j),end=",")
        j+=1
    print()
    i+=1

#for 循环
arr=[4,1,6,8,3,9,2,0,5,7]
for i in arr:
    print(i,end=',')
else:
    print('for end')

for i in range(1,100):
    #range(a,b) 迭代a到b的数字
    if(i%3==0):
        echo(i)
    else:
        pass #pass 代码占位符  不做任何处理

global_a=5
def suma(v):
    global global_a#global 获取外部变量作为全局变量
    global_a+=v
suma(5)
print(global_a)
