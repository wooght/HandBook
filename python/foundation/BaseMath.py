# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseMath.py
@Author     :wooght
@Date       :2024/3/11 17:07
"""

"""
    找到数列中的质数
    质数:不能被其他整数整除的数
"""
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '整除', x, '商为:', n // x)
            break
    else:
        print(n, '是质数')


contrast_str = '0123456789ABCDEF'       # 进制对照表
def hex_convert(nums, hex_num):
    """
    递归进制类型转换
    nums 要被转换的10进制数
    hex_num目的进制数,二,八,十六进制
    """
    return contrast_str[nums] if nums < hex_num else hex_convert(nums // hex_num, hex_num) + contrast_str[nums % hex_num]


print(hex_convert(88, 2))       # 1011000


def fib(n):
    """
    斐波拉契数列 1、1、2、3、5、8、13、21、34...
    """
    i, a, b = 0, 0, 1
    while i < n:
        # 返回本次结果
        yield b
        # 计算下一次
        b, a = a+b, b       # 先计算等式右边的,等右边的计算完了,在分别赋值给左边的变量
        i += 1

print(list(fib(10)))


def maopao(nums_list):
    """
        改良冒泡排序
    """
    list_length = len(nums_list)
    for i in range(list_length):
        max = nums_list[i]
        for j in range(i, list_length):
            if nums_list[j] > max:
                nums_list[i] = nums_list[j]
                nums_list[j] = max
                max = nums_list[i]
    return nums_list
test_list = [3, 6, 1, 7, 2, 9, 8, 4, 5]
print(maopao(test_list))
print(test_list[::-1])


def w_maopo(nums_list):
    """
        冒泡排序法
    """
    nums_length = len(nums_list)
    for i in range(nums_length - 1):
        for j in range(nums_length - i - 1):
            if nums_list[j] > nums_list[j + 1]:
                nums_list[j], nums_list[j + 1] = nums_list[j + 1], nums_list[j]
    return None


test_nums = [55, 88, 99, 1, 33, 77]
w_maopo(test_nums)
print(test_nums)

new_list = []
def dg_maopao(nums_list):
    length = len(nums_list)
    if length <= 1:
        new_list.append(nums_list[0])
    else:
        for i in range(length-1):
            if nums_list[i] > nums_list[i+1]:
                nums_list[i], nums_list[i+1] = nums_list[i+1], nums_list[i]
        new_list.append(nums_list[length-1])
        dg_maopao(nums_list[:length-1])

test_nums = [9,3,8,1,5,4,7]
dg_maopao(test_nums)
print(new_list)

"""
    快速排序法
"""


def variance(nums_list):
    """
    返回数列的方差
    公式  Var = ∑(x-x平均值)**2 / N
    Return Nums
    """
    average = sum(nums_list)/len(nums_list)        # 数列平均值
    sgm = 0
    for i in nums_list:
        sgm += (i - average)**2
    return sgm/len(nums_list)
variance_nums = variance([1,2,3,4,5,6])
print("数列方差为:%.2f" % variance_nums)             # 2.92

def expect(nums_list):
    """
    数学期望
    E(x) = ∑(Xi*P(xi))      及期望等于每个值*出现的概率的和
    Returns Nums
    """
    length = len(nums_list)
    odds = 1/length                                 # 每一个出现的概率  列表中概率固定
    expect_nums = 0
    for i in nums_list:
        expect_nums += i * odds
    return expect_nums
print('列表的期望为:%.2f' % expect([1,3,5,7,9]))      # 4.00

