# -*- coding: utf-8 -*-
#
# @method   : scikit-learn LogisticRegression(逻辑回归)
# @Time     : 2018/4/2
# @Author   : wooght
# @File     : w_LogisticRegression.py
# 逻辑回归用于分类,二元分类常用, 特征没有线性要求

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

# class_weight 指定特征权重
logisticR = LogisticRegression(class_weight={0:0.3, 1:0.7})
logisticR.fit(x_train, y_train)
result = logisticR.predict(x_test)
print(logisticR.coef_, logisticR.intercept_)
classfy_plt_3d(logisticR, x_train, y_train)
print(logisticR.score(x_train, y_train))