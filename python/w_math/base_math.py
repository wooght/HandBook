# -*- coding: utf-8 -*-
#
# @method   : 基础数学函数库
# @Time     : 2018/4/4
# @Author   : wooght
# @File     : base_math.py
import math
print(dir(math))


def echo(name, num):
    print('%-10s:%s'%(name, num))


def f(str):
    print('\n', "*" * 20, str, "*" * 20, '\n')


f('math常量')
print(math.pi, math.e)  # π,e

f('math数学函数')
num = 4
echo('log', math.log(num, 2))  # 以2为底的对数  默认是e为底
echo('log2', math.log2(num))  # 以2位底的对数
echo('sqrt', math.sqrt(num))  # 平方根  与num**0.5 效果一样
echo('exp', math.exp(num))  # 指数 e**x
echo('modf', math.modf(math.pi))  # 返回小数部分,整数部分组成的元祖
echo('ceil', math.ceil(1.2))  # 向上
echo('floor', math.floor(1.2))  # 向下

f('python 原生数学函数')
echo('round', round(math.pi, 2))  # python.round(x, n) 返回四舍五入的值,如果指定n,则保留n位小数
echo('abs', abs(-num))  # 绝对值

f('常用数学公式')
# 期望  E(X) = x1*p(x1)+x2*p(x2)....xn*p(xn)  每个值*每个值概率的和
# 方差  s^2=[(x1-x)^2+(x2-x)^2+......(xn-x)^2]/(n) （x为平均数）
# 标准差 = 方差的算术平方根

