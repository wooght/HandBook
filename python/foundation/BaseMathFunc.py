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
    range(start, stop, step)    返回整数序列
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
    print(str_list_1[i], end=" ")                           # 2 4 6 8 10
print([str_list_1[i] for i in range(1, len(str_list_1), 2)])                                # ['2', '4', '6', '8', '10']
print([str_list_1[i] for i in range(1, len(str_list_1)) if int(str_list_1[i]) % 2 ==0])     # ['2', '4', '6', '8', '10']


""" 
    random 随机数
    random.random() 生成一个随机浮点数(精度16),在0到1之间
    random.uniform(a,b) 生成一个随机浮点数,基于a,b之间
    random.randint(a,b) 生成一个随机整数,基于a,b之间
    random.choice(list) 从一个序列中随机获取一个元素
    random.sample(list,k)  从序列中随机获取k个元素,这k个元素是无序的
"""
print(random.random())      # 0.5174316816074847
print(random.uniform(1, 10))        # 5.029117095203566
print(random.randint(1, 100))       # 60
test_list = [1, 3, 5, 7, 9]
print(random.choice(test_list))     # 7
print(random.sample(test_list, 2))      # [9 ,7]


def random_100_100():
    for i in range(100):
        yield [random.randint(1, 100) for a in range(100)]


random_1 = random_100_100()
print(next(random_1))
print(list(random_1))


"""
    排序 list.sort(),sorted()
    sort()时列表对象的一个方法,会直接改变对象的顺序
    sorted()可以作用于元祖,字典,不改变原对象,而是产生一个新对象
    有key,reverse两个参数,key是排序已经得函数,reverse指是否倒序,默认是False及升序
"""
test_list = [2,1,3,5,9,0]
test_list.sort()
print(test_list)        # [0, 1, 2, 3, 5, 9]
test_list = [2,1,3,5,9,0]
print(sorted(test_list))        # [0, 1, 2, 3, 5, 9]
print(test_list)                # [2, 1, 3, 5, 9, 0]

test_list = [
    [1, 2, 3],
    [0, 2, 4],
    [2, 4, 8]
]
test_list.sort(key=lambda x: x[2], reverse=True)    # 按元素列表的第2个元素大小进行排序, 倒序
print(test_list)        # [[2, 4, 8], [0, 2, 4], [1, 2, 3]]


def get_len(str):
    return len(str)


"""调用外部函数作为排序依据"""
test_list = ['217342918734', '394', '56761', '14645157']
new_list = sorted(test_list, key=get_len)       # 调用函数,函数返回排序依据,注意这里的函数没有()
print(new_list)     # ['394', '56761', '14645157', '217342918734']
"""将字典的某个字段作为排序依据"""
test_dict = [
    {'name': 'wooght', 'edu': '本科', "age": 1986},
    {'name': 'pwf', "edu": '小学', "age": 1988},
    {'name': 'zhangsan', "edu": '博士', "age": 1990}
]
new_dict = sorted(test_dict, key=lambda x: x["age"])    # 列表里面的字典的某个字段进行排序
print(new_dict)
