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


def maopao(list_nums):
    list_length = len(list_nums)
    for i in range(list_length):
        max = list_nums[i]
        for j in range(i, list_length):
            if list_nums[j] > max:
                list_nums[i] = list_nums[j]
                list_nums[j] = max
                max = list_nums[i]
    return list_nums
print(maopao([3, 6, 1, 7, 2, 9, 8, 4, 5]))
