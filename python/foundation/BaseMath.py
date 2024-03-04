# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseMath.py
@Author     :wooght
@Date       :2024/3/4 18:30
"""

import math

"""
    数学基本函数
    math基本函数
"""

"""eval(string) 执行字符串表达式"""
str_math = "2 * 8"
print(eval(str_math))       # 16
a_num = 2
b_num = 8
str_math = "a_num * b_num"
print(eval(str_math))       # 16

"""abs()绝对值"""
num = -2
print(abs(num))             # 2

"""round(num) 对num四舍五入"""
num = 3.4
print(round(num))           # 3
print(round(num+0.3))       # 4

"""
    sum() 求和函数,参数可以是元祖,列表
    min()最小,max()最大
"""
list_1 = [1, 2, 3]
print(sum(list_1))      # 6
print(min(list_1))      # 1
print(max(list_1))      # 3


"""divmod(被除数, 除数)   返回(商,余数)的元祖"""
num_1 = 9
num_2 = 4
print(divmod(num_1, num_2))     # (2, 1)

"""pow(x,y) 返回x的y次方"""
print(pow(2, 4))                # 16
print(math.pow(2, 4))   # 16.0

"""
    range(start, stop, step)
    生成可迭代的整数列表 从start开始,默认是0, 到stop结束,不包括stop,按step递增,step默认是1
"""
for i in range(1, 12):
    print(i, end=" ")       # 1 2 3 4 5 6 7 8 9 10 11
for i in range(-100, 10, 10):
    print(i, end=" ")       # -100 -90 -80 -70 -60 -50 -40 -30 -20 -10 0
print("")
str_1 = "1,2,3,4,5,6,7,8,9,10"
str_list_1 = str_1.split(",")
# 输出偶数
for i in range(1, len(str_list_1), 2):
    print(str_list_1[i], end=" ")


"""
    zip,map,filter,reversed,enumerate
"""

"""
    next(iter, 0) 让迭代器迭代一次,获取下一个项目, 如果是字典,就返回key
    iter 迭代器对象,0指最后一项后返回0,而不是返回错误
    运行机制和for遍历一样,只是迭代完后,不会回到第一项
"""
date_list = [27, 28, 1, 2]
it = iter(date_list)    # 创建迭代器
next(it)                # 要提前迭代一次,要不然他和for循环一样的迭代顺序
for i in date_list:
    if next(it, 0) == 1:
        print("这个月有%d天" % i)
        print(f"这个月有{i}天")
print(list(it))         # []


"""
    map(function, iterable,....) 迭代执行函数
    把可迭代对象iterable的每一个元素在function的运行结果组成一个列表
    function有几个参数,iterable就有几个
"""


def square(x):
    return x**3


def add_xy(x, y):
    return x+y


result_list = map(square, [1, 2, 3, 4])
print(list(result_list))        # [1, 8, 27, 64]
result_list = map(add_xy, [1, 2, 3], [4, 5, 6])
print(list(result_list))        # [5, 7, 9]
result_list = list(map(lambda x, y: x+y, [1, 3, 5, 7], [2, 4, 6, 8]))
print(result_list)              # [3, 7, 11, 15]

"""list.reverse() 列表原地翻转"""
list_1 = [1, 2, 3]
list_1.reverse()
print(list_1)           # [3, 2, 1]

"""all(list) 判断列表中是否有0,空,None,False等非真的元素,如果都为真,则返回True"""
print(all([1, 2, '3', True]))       # True
print(all([1, 0, 3]))               # False
print(all([1, '', 3]))              # False
