# -*- coding: utf-8 -*-
#
# @method   : numpy 应用
# @Time     : 2018/1/16
# @Author   : wooght
# @File     : numpy_b.py

from numpy import *

from echo import *

f('形状操作')
arr = floor(10*random.random((3, 4)))  # floor 向下取整
print(arr)
print(arr.shape)
arr2 = arr.ravel()  # ravel() 转换为一维数组
print(arr2, arr2.shape)
print(arr.transpose())  # transpose() 轴转换
arr.resize((2, 6))  # resize() 对原数组进行格式转换
print(arr)

f('数组组合')
arr = ceil(10*random.random((2, 3)))  # ceil 向上取整
print(arr)
arr2 = floor(10*random.random((2, 3)))
print(arr2)
print(vstack((arr, arr2)))  # vstack() 水平轴连接数组 纵向
print(hstack((arr, arr2)))  # hstack() 纵向轴连接数组 横向
print(column_stack((arr, arr2)))  # 水平组合
print(row_stack((arr, arr2)))  # 纵向组合

f('split分割数组')
arr = ceil(100*random.random((4, 6)))
print(arr)
arr2 = hsplit(arr, 3)  # hsplit() 水平轴分割
print(arr2)
print(arr2[1][1, :])
print(vsplit(arr, 2))  # vsplit() 纵向轴分割

f('视图view')
arr = arange(15).reshape(3,5)
print(arr)
arr2 = arr.view()  # 潜复制 可改变值,不改变结构
print(arr2)
print(arr2 is arr)  # false
arr2[0, 0] = 100
print(arr)

arr3 = arr  # 复制 完全操作
print(arr3 is arr)  # true
arr3[0, 0] = -1
print(arr)

arr4 = arr.copy()  # 深复制 完全复制,复制后,两者没关系
print(arr4 is arr)  # false
arr4[0, 0] = -100
print(arr)

f('通用函数ufunc')
arr = random.random((3, 3))
print(arr, arr.ndim)
print(arr.sum(), arr.min(), arr.max(), arr.mean())
print(arr.sum(axis=0), arr.sum(axis=1))
# sum,min,max,mean 数组基本函数 默认对整个数组
# 通过指定axis,指定对某个轴进行运算
# 通用函数都是对元素进行操作
arr = arange(3)
arr2 = linspace(3, 6, 3)
print(arr, arr2)
print(exp(arr))  # exp e为底的指数函数
print(sqrt(arr))  # sqrt 平方根
print(add(arr, arr2))  # add 求和

arr = array([[1, 1, 1],
             [1, 1, 0],
             [1, 0, 0]])
print('average:\n',average(arr, 1))
