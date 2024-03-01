# -*- coding: utf-8 -*-
#
# @method   : scikit-learn LogisticRegression(逻辑回归)
# @Time     : 2018/4/2
# @Author   : wooght
# @File     : w_LogisticRegression.py
# 逻辑回归用于分类,二元分类常用, 特征没有线性要求,因变量是二元的

from Tdata import gender_sample
from sklearn.linear_model import LogisticRegression
import numpy as np
from common.classfy_plt_3d import classfy_plt_3d


# 性别分类数据 为了3D展示,只取了体重和身高作为特征 特征数据离散
x, y = gender_sample()
x_train, y_train = np.row_stack([x[:50, :2], x[150:, :2]]), y[50:150]
x_test, y_test = x[50:150, :2], y[50:150]

logisticR = LogisticRegression()
logisticR.fit(x_train, y_train)  # y_train 必须是类别数据
result = logisticR.predict(x_test)
print(result)
classfy_plt_3d(logisticR, x_train, y_train)
print(logisticR.score(x_train, y_train))




import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
pf = PolynomialFeatures(degree=3)


def classfy_plt(clf, X, target):
    #  找到二维坐标轴的最值
    x_max, x_min = X[:, 0].max() + 1, X[:, 0].min() - 1
    y_max, y_min = X[:, 1].max() + 1, X[:, 1].min() - 1
    #  根据最值绘制二维坐标网络
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                         np.arange(y_min, y_max, 0.1))  # meshgrid(x,y)生产两个二维矩阵,用于网络型数据
    Z = clf.predict(pf.transform(np.c_[xx.ravel(), yy.ravel()]))  # 提取二维坐标所有点供分类模型分类
    # reavel 降维  降为一维
    # np.c_[a, b] 列拼接,及np.column_stack()
    Z = Z.reshape(xx.shape)  # 维度转换,将分类结果转换到二维坐标上
    plt.contourf(xx, yy, Z, alpha=0.4)  # 绘制三维轮廓/等高线
    plt.scatter(X[:, 0], X[:, 1], c=target, alpha=0.8)  # 绘制散点图
    plt.show()


# class_weight 指定特征权重(注意这里是特征权重,而不是类别权重)
logisticR = LogisticRegression(class_weight={0:0.5, 1:0.5})
x_pf_train = pf.fit_transform(x_train)
logisticR.fit(x_pf_train, y_train)
x_test = pf.transform(x_test)
result = logisticR.predict(x_test)
print(logisticR.coef_, logisticR.intercept_)
classfy_plt(logisticR, x_train, y_train)
print(logisticR.score(x_pf_train, y_train))