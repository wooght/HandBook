# -- coding: utf-8 -
"""
@project    :HandBook
@file       :NumpyApplication.py
@Author     :wooght
@Date       :2024/3/25 22:55
@Content    :Numpy 应用实例
"""


import numpy as np
import numpy.random

from wooght_tools.echo import echo

np.random.seed(1)

"""在数组中找到给定标量最接近的值"""
arr = np.random.uniform(1, 100, (5, 5))
contrast_num = np.random.uniform(100)                   # 生成单个随机浮点数
index = (np.abs(arr - contrast_num)).argmin()           # argmin()/max()    返回一维索引
index_2d = (index // 5, index % 5)
echo(arr, contrast_num, index_2d, arr[index_2d])

"""数组中满足条件的元素赋值,不满足的原样显示"""
new_arr = np.where(arr > 10, 100, arr)
print(new_arr)

"""创建结构化数组"""
arr = np.zeros(10, [('position', [('x', float), ('y', float)]), ('rgb', [('r', float), ('g', float), ('b', float)])])
print(arr[0])
arr[0] = ((11, 22), (211, 128, 99))
print(arr[0]['position'])
print(arr.dtype)