# -- coding: utf-8 -
"""
@project    :HandBook
@file       :formula.py
@Author     :wooght
@Date       :2024/3/25 19:58
@Content    :数学公式实现
"""
import random

import numpy
from wooght_tools.echo import echo

def variance(nums_list):
    """
    返回数列的方差 单词:variance 方差
    公式  Var = ∑(x-x平均值)**2 / N
    Return Nums
    """
    average = sum(nums_list)/len(nums_list)        # 数列平均值
    sgm = 0
    for i in nums_list:
        sgm += (i - average)**2
    return sgm/len(nums_list)
arr = numpy.arange(1, 7)
variance_nums = variance(arr)
print("数列方差为:%.2f" % variance_nums)             # 2.92
echo("numpy验证:", arr, numpy.var(arr), numpy.std(arr))


def expect(nums_list):
    """
    数学期望    单词 expect 期望,期待,预期
    E(x) = ∑(Xi*P(xi))      及期望等于每个值*出现的概率的和
    Returns Nums
    """
    length = len(nums_list)
    odds = 1/length                                 # 每一个出现的概率  列表中概率固定
    expect_nums = 0
    for i in nums_list:
        expect_nums += i * odds
    return expect_nums
arr = numpy.arange(1, 10, 2)
print('列表的期望为:%.2f' % expect([1, 3, 5, 7, 9]))      # 4.00


def normalization(data, method=False):
    """
    归一化
        最值归一化           (data-min_data) /(max_data-min_data)
        均值标准差归一化      (data-mean_data)/std_data
    """
    if not method:
        min_val = data.min()
        max_val = data.max()
        return (data-min_val)/(max_val-min_val)
    else:
        return (data-data.mean())/data.std()
data = numpy.random.randint(1, 15, 15).reshape(3, 5)
echo("最值归一化:", normalization(data), "均值方差归一:", normalization(data, True))


# def covariance(x, y);
#     """
#         求两个数列的协方差
#         cov = E(x-E(x))(y-E(y))
#     """
#     ex = expect(x)
#     ey = expect(y)
#     x_ex = x-ex
#     y_ex = y-ey
#     result = expect(x_ex*y_ex)
#     return result
#
# x = numpy.random.uniform(1,10,100)
# y = numpy.random.uniform(1,10,100)
# print(covariance(x, y))
