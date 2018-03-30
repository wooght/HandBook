# -*- coding: utf-8 -*-
#
# @method   : 分类图表3D展示
# @Time     : 2018/3/31
# @Author   : wooght
# @File     : classfy_plt_3d.py

import matplotlib.pyplot as plt
import numpy as np


def classfy_plt_3d(clf, X, target):
    #  找到二维坐标轴的最值
    x_max, x_min = X[:, 0].max() + 1, X[:, 0].min() - 1
    y_max, y_min = X[:, 1].max() + 1, X[:, 1].min() - 1
    #  根据最值绘制二维坐标网络
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))  # meshgrid(x,y)生产两个二维矩阵,用于网络型数据
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])  # 提取二维坐标所有点供分类模型分类
    # reavel 降维  降为一维
    # np.c_[a, b] 列拼接,及np.column_stack()
    Z = Z.reshape(xx.shape)  # 维度转换,将分类结果转换到二维坐标上
    plt.contourf(xx, yy, Z, alpha=0.4)  # 绘制三维轮廓/等高线
    plt.scatter(X[:, 0], X[:, 1], c=target, alpha=0.8)  # 绘制散点图
    plt.show()