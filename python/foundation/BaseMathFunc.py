# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseMathFunc.py
@Author     :wooght
@Date       :2024/3/4 18:30
"""

import math
import random

"""
    数学基本函数
    math基本函数
"""

"""eval(string) 执行字符串表达式"""
str_math = "2 * 8"
print(eval(str_math))  # 16
a_num = 2
b_num = 8
str_math = "a_num * b_num"
print(eval(str_math))  # 16

"""abs()绝对值"""
num = -2
print(abs(num))  # 2

"""
    round(num,小数位数) 对num四舍五入,小数位数默认为0
    math.ceil(num)  对num向上取整
    math.floor(num) 对num向下取整
"""
num = 3.44445
print(round(num))  # 3
print(round(num + 0.3))  # 4
print(round(num, 3))  # 3.444
print(math.ceil(num))  # 4
print(math.floor(num))  # 3
"""
    sum() 求和函数,参数可以是元祖,列表
    min()最小,max()最大
"""
list_1 = [1, 2, 3]
print(sum(list_1))  # 6
print(math.fsum(list_1))  # 6.0
print(min(list_1))  # 1
print(max(list_1))  # 3

"""divmod(被除数, 除数)   返回(商,余数)的元祖"""
num_1 = 9
num_2 = 4
print(divmod(num_1, num_2))  # (2, 1)

"""
    pow(x,y) 返回x的y次方
    math.fmod(x, y) x于y的模 及x整除于y的余数
"""
num_1, num_2 = 2, 4
print(pow(num_1, num_2))  # 16
print(math.pow(num_1, num_2))  # 16.0
print(math.fmod(9, 5))  # 4.0
print(math.modf(3.338))

"""
    range(start, stop, step)
    生成可迭代的整数列表 从start开始,默认是0, 到stop结束,不包括stop,按step递增,step默认是1
"""
for i in range(1, 12):
    print(i, end=" ")  # 1 2 3 4 5 6 7 8 9 10 11
for i in range(-100, 10, 10):
    print(i, end=" ")  # -100 -90 -80 -70 -60 -50 -40 -30 -20 -10 0
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
    iter 迭代器,不用遍历,可以用next依次取出元素的对象叫迭代器
    next(iter, 0) 让迭代器迭代一次,获取下一个项目, 如果是字典,就返回key
    当迭代到最后一项继续迭代时,或处罚异常,0表示触发异常后返回0而不是报错
    迭代器只能往前不能后退,迭代完后无法再次迭代
    for循环是将数据全部放在内存中,而迭代器只将指针放内存中,内容是用的时候才用
"""
date_list = [27, 28, 1, 2]
it = iter(date_list)  # 创建迭代器
next(it)  # 在for循环开始之前要提前迭代一次
for i in date_list:
    # 这里next(it) 就是for循环的下一次
    if next(it, 0) == 1:
        print("这个月有%d天" % i)        # 这个月有28天
        break
print(list(it))  # [2]
test_list = iter(range(10))
for item in test_list:
    print(item, end=" ")        # 0 1 2 3 4 5
    if item == 5:
        break
print("是否可以继续遍历")
for item in test_list:
    print(item, end=" ")        # 6 7 8 9

"""
    map(function, *iterable) 迭代执行函数的迭代器
    把可迭代对象iterable的每一个元素在function的运行结果组成一个列表
    function有几个参数,就有几个iterable
    Return [result,result,...]的迭代器
"""


def square(x):
    return x ** 3


def add_xy(x, y):
    return x + y


result_list = map(square, [1, 2, 3, 4])
# 迭代器可以直接用next获取下一项,或者for遍历,或者list转换为列表
print(next(result_list))  # 1
print(list(result_list))  # [8, 27, 64]
result_list = map(add_xy, [1, 2, 3], [4, 5, 6])
print(list(result_list))  # [5, 7, 9]
result_list = list(map(lambda x, y: x + y, [1, 3, 5, 7], [2, 4, 6, 8]))
print(result_list)  # [3, 7, 11, 15]

"""
    zip(*iterable)
    将多个可迭代对象的元素打包成一个元祖列表的迭代器
    Return [tuple,tuple,..]的迭代器
"""
fruits = ['苹果', '橘子', '桃子']
prices = [5, 3, 4]
goods_zip = zip(fruits, prices)
print(goods_zip.__next__())     # ('苹果', 5)
print(list(goods_zip))  # [('橘子', 3), ('桃子', 4)]
"""zip应用:矩阵点乘"""
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = [[1, 1, 1], [2, 2, 3], [3, 3, 3]]
print([x*y for a, b in zip(m, n) for x, y in zip(a, b)])        # [1, 2, 3, 8, 10, 18, 21, 24, 27]


"""
    generator 生成器
    迭代运行的函数,yield依次取出函数的返回值
    yield 类似于普通函数的return,返回结果
    普通函数Return后就不能在执行,而生成器可以用next可以继续调用,继续从上次yield的位置继续运行,直到下一次yield
    生成器相对于需要遍历长列表的函数更节约内存,因为他不会将返回结果全部给内存,而是需要的时候在提取
"""
test_list = [item for item in range(10)]
test_tuple = (item for item in range(10))
print(test_list, test_tuple)        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] <generator object <genexpr> at 0x000002158ECD5D80>
print(test_tuple.__next__())        # 0
print(next(test_tuple))             # 1
for i in test_tuple:
    print(i, end=" ")               # 2 3 4 5 6 7 8 9
test_tuple = (item for item in range(10))
print(list(test_tuple))

def fib(n):
    """
    生成器 有yield的函数就变成一个generator(生成器)
    斐波拉契数列 1、1、2、3、5、8、13、21、34...
    """
    i, a, b = 0, 0, 1
    while i < n:
        # 返回本次结果
        yield b
        # 计算下一次
        b, a = a+b, b       # 先计算等式右边的,等右边的计算完了,在分别赋值给左边的变量
        i += 1


fib_list = fib(10)
print(fib_list)     # <generator object fib at 0x000001CA84105EE0>
print(next(fib_list), end=" ")      # 1
print([item for item in fib_list])  # [1, 2, 3, 5, 8, 13, 21, 34, 55]

"""list.reverse() 列表原地翻转"""
list_1 = [1, 2, 3]
list_1.reverse()
print(list_1)  # [3, 2, 1]

"""all(list) 全真判断,及判断列表中是否有0,空,None,False等非真的元素,如果都为真,则返回True"""
print(all([1, 2, '3', True]))  # True
print(all([1, 0, 3]))  # False
print(all([1, '', 3]))  # False
