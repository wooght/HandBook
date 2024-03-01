# -*- coding: utf-8 -*-
#
# @method   : regression equation 回归方程 求解方程y=a+bx 中的a,b
# @Time     : 2018/4/14
# @Author   : wooght
# @File     : regression_equation.py

# 一元线性回归方程 y=a+bx 最小二乘法求解公式:
# b = [sum(xi*yi)-nx^y^]/[sum(xi**2)-nx^**2]  ^指平均数
# a = y^ - bx^

# 数学概念:
# 标准差就是均方差,标准差是方差的开根号
# 方差:sum([xi-x^]**2)/N  x^指平均值或者期望  期望是 sum(xi*p(xi))
# 均方误差: sqrt({sum(xi-X)**2/N}) X指真实值

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(211)


# 线性回归拟合--求解a,b
def linearregression(x, y):
    matrix = np.column_stack([x, y])
    x_mean = np.mean(matrix[:, 0])
    y_mean = np.mean(matrix[:, 1])
    xy = 0
    xexp = 0
    for i in matrix:
        xy += i[0] * i[1]
        xexp += i[0] ** 2
    xyMean = matrix.shape[0] * x_mean * y_mean
    xMeanExp = matrix.shape[0] * (x_mean ** 2)
    b = (xy - xyMean) / (xexp - xMeanExp)
    a = y_mean - b * x_mean
    return a, b


# 数据样本
x = np.linspace(1, 10, 100)
y = x * (np.random.rand(100) + 2) + np.random.randint(2, 4, size=(100))  # random.rand() 0,1之间的随机浮点数
plt.plot(x, y, 'k.')

a, b = linearregression(x, y)  # 求a,b
y_predict = a + b * x  # 测试a,b
plt.plot(x, y_predict, 'b-')  # 绘制回归线
plt.show()
