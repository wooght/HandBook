# -*- coding: utf-8 -*-
#
# @method   : scikit-learn preprocessing (数据预处理)
# @Time     : 2018/4/4
# @Author   : wooght
# @File     : w_preprocessing.py
# 涉及词条: preprocessing [prep'roʊsesɪŋ] 预处理

import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing

dataSet = np.linspace(1, 2, 10)
print(dataSet)
# 将数据转换为标准正太分布
scaleData = preprocessing.scale(dataSet)
print(scaleData)
y = np.array(2 - abs(scaleData))
plt.plot(scaleData, y, 'b-')
plt.show()

# 将数据缩放在固定区间 默认0,1
zerosData = preprocessing.minmax_scale(dataSet, feature_range=(1, 2))  # feature_range 指定缩放区间 默认0,1
print(zerosData)

matrix = np.random.randint(-10, 10, size=(5, 5))
print(matrix)
print(preprocessing.maxabs_scale(matrix, axis=1))  # 缩放到[-1, 1]之间
print(preprocessing.binarize(matrix, threshold=0.0))  # 数据二值化 小于threshold的未0