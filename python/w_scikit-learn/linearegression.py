# -- coding: utf-8 -
"""
@project    :HandBook
@file       :linearregression.py
@Author     :wooght
@Date       :2024/4/13 19:30
@Content    :scikit-learn 线性回归
"""

from wooght_tools.echo import echo
from wooght_tools.DateTimeMath import WDate

import pandas as pd
import numpy as np
from sklearn import linear_model, datasets
from sklearn.metrics import mean_squared_error, r2_score
from matplotlib import pyplot as plt

"""
    单词: Linear Regression   线性回归
"""

y = np.linspace(10, 100, 10) + np.random.uniform(-10, 20, 10)
x = np.linspace(1, 10, 10) + np.random.uniform(-1, 1, 10)
b = np.random.uniform(1,3,10)
"""
    创建线性回归模型
        positive    是否非负最小二乘法进行拟合 默认 False
        在实际生活中,有非负关系,则采用非负最小二乘法更精准
"""
reg = linear_model.LinearRegression(positive=True)
"""
    fit(x,y)训练数据
        x为矩阵,有几列就代表有几个系数
        y为向量
    coef_   系数      单词:Coefficients 系数
    intercept_   常数
"""
reg.fit(x.reshape((10,1)), y)
print(reg.coef_, reg.intercept_)
"""
    predict(x_test) 根据模型预测
"""
x_test = np.linspace(2,11, 10)
y_test = np.linspace(20, 110, 10) + np.random.uniform(-12, 25, 10)
y_predict = reg.predict(x_test.reshape((10,1)))

echo('均方差:',mean_squared_error(y_test, y_predict), 'R2决定系数:', r2_score(y_test, y_predict))

fig, ax = plt.subplots()
ax.scatter(x, y)                        # 显示训练数据
ax.scatter(x_test, y_test, color='g')   # 显示测试数据
ax.plot(x_test, y_predict)              # 显示拟合方程
plt.show()

echo('耗时:'+str(WDate.run_time()))