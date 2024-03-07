# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseIter.py
@Author     :wooght
@Date       :2024/3/6 16:46
"""
import random

"""
    iter 迭代器,不用遍历,可以用next依次取出元素的容器叫迭代器
    next(iter, 0) 让迭代器迭代一次,获取下一个项目, 如果是字典,就返回key
    当迭代到最后一项继续迭代时,或处罚异常,0表示触发异常后返回0而不是报错
    迭代器只能往前不能后退,迭代完后无法再次迭代,迭代一次就释放一次内存
    for循环是将数据全部放在内存中,在遍历过程中可以访问已经遍历过的数据,未释放内存
    for循环遍历可迭代对象(元祖,列表,字典,集合等),会额外创建一个迭代器,而遍历迭代器时,不会额外创建
"""
test_list = iter(range(10))     # 创建迭代器
print(test_list.__next__())     # 0 访问迭代器的下一项
print(next(test_list))          # 1 访问迭代器的下一项
for item in test_list:
    print(item, end=" ")        # 2 3 4 5
    if item == 5:
        break
print("是否可以继续遍历")
for item in test_list:
    print(item, end=" ")        # 6 7 8 9   从上一次指针继续迭代,意为按需运行,节约内存
try:
    next(test_list)
except StopIteration:
    print("触发异常")           # 触发异常,迭代器迭代结束后不能再迭代
print(next(test_list, 0))      # 0 next()函数解决异常的方法,第二个参数给定异常返回值


"""
    enumerate(iterable, start=0) 枚举
    将一个可遍历的数据对象组合为一个带索引序列的迭代器
"""
citys = ['北京', '上海', '广州', '深圳', '成都', '重庆']
for city in citys:
    print(city, end=" ")            # 北京 上海 广州 深圳 成都 重庆
enumerate_citys = enumerate(citys)
enumerate_citys.__next__()          # (0, '北京')
for city in enumerate_citys:
    print(city, end="")              # (1, '上海')(2, '广州')(3, '深圳')(4, '成都')(5, '重庆')


def square(x):
    return x ** 3


def add_xy(x, y):
    return x + y


"""
    map(function, *iterable) 迭代执行函数的迭代器
    把可迭代对象iterable的每一个元素在function的运行结果组成一个列表
    function有几个参数,就有几个iterable
    Return [result,result,...]的迭代器
"""
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
    filter() 过滤器 lamda
    filter(function, iterable) function 筛选函数,iterable可迭代对象
    自动把iterable中的元素传递给function,然后更加function返回的bool值判断是否保留
    返回迭代器
"""
random_int = [random.randint(1, 100) for a in range(100)]


def fiter_func(num)::q
    return random_int.count(num) > 1


list_100 = [a for a in range(100)]
repeat_list = filter(fiter_func, list_100)
print('重复的随机数:', list(repeat_list))
null_list = filter(lambda num: random_int.count(num) < 1, list_100)
print('未出现的数字有:', list(null_list))



"""
    generator 生成器,一个做迭代运算的迭代函数
    普通迭代函数,一经调用,就全部迭代,并把结果存放内存中(一般会额外产生一个中间变量)
    而生成器调用一次就只运行一次,只返回一个结果,并且释放上一次返回结果的内存
    yield 类似于普通函数的return,返回结果
    普通函数Return后就不能在执行,而生成器可以用next可以继续调用,继续从上次yield的位置继续运行,直到下一次yield
    生成器相对于需要遍历长列表的函数更节约内存,因为他不会将返回结果全部给内存,而是需要的时候在提取
"""
test_list = [item for item in range(10)]
test_tuple = (item for item in range(10))       # 元祖的推导式会生成一个生成器
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


def base_cfb():
    """传统99乘法表,会额外给定一个中间变量存放返回结果"""
    result_list = {}
    for x in range(1, 10):
        result_list[x] = []
        for y in range(1, 10):
            if y <= x:
                result_list[x].append(f"{y}*{x}=" + ("%02d" % (x * y)))
    return result_list


cfb = base_cfb()
for key, value in cfb.items():
    print(key, value)


def gen_cfb():
    """ 用生成器的99乘法表 没有中间变量"""
    for x in range(1, 10):
        yield [f"{y}*{x}=" + (str(x * y).rjust(2)) for y in range(1, 10) if y <= x]    # 生成器里面不能嵌套生成器,所以这里不能是()


cfb = list(gen_cfb())
for value in cfb:
    print(value)


"""
    itertools.islice(iterable, start, stop, step) 迭代器切片
    iterable 可迭代对象/迭代器,start 开始位置,stop结束位置,末尾是None,step步长
"""
from itertools import islice
test_list = iter(range(10))
lice_list = islice(test_list, 5, None)
for value in lice_list:
    print(value, end=" ")       # 5 6 7 8 9
