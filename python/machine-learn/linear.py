# -*- coding: utf-8 -*-
#
# @method   : scikit-learn 之linear_model  线性回归
# @Time     : 2018/3/29
# @Author   : wooght
# @File     : linear.py

import pandas as pd
# from sklearn.cross_validation import train_test_split  # 即将淘汰
from sklearn.model_selection import train_test_split
import numpy as np

data = pd.read_csv('./data/Folds5x2_pp.csv')
print(data.head())  # 输出前五条
print(data.shape)  # 查看数据维度

X = data[['AT', 'V', 'AP', 'RH']]
print(X.head())
y = data['PE']
print(y.head())

# 划分训练集和测试集 train为训练街,test为测试集
# X_train 为训练自变量,y_train 为自变量对应的因变量
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    random_state=1)  # random_state 随机数种子,每次都填写1,那么每次的随机数相同,及数组排序的顺序
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)


# 训练线性回归模型
def one_linear(x, y):
    from sklearn.linear_model import LinearRegression
    linreg = LinearRegression()
    linreg.fit(x, y)  # 拟合或者叫做 训练 得到:样本或者模型
    return linreg


linreg = one_linear(X_train, y_train)
print(linreg.intercept_)  # 截距
print(linreg.coef_)  # 回归系数
y_pred = linreg.predict(X_test)  # 通过模型样本预测
print(y_pred)
# 方程为 截距+回归系数*变量
# [-1.97376045 -0.23229086  0.0693515  -0.15806957]

# 模型评价
# 两种方式:MSE 均方误差，RMSE均方根误差
from sklearn import metrics

print('MSE', metrics.mean_squared_error(y_test, y_pred))  # 对模型进行评价,不同方法得到的不同系数,选择MSE最小的时候对应的方法或者系数最佳
print('RMSE', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# 少选择一个特征 看系数是否更佳
X = data[['AT', 'V', 'RH']]  # 原来为: ['AT', 'V', 'AP', 'RH']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
linreg = one_linear(X_train, y_train)
y_pred = linreg.predict(X_test)
print('New MSE:', metrics.mean_squared_error(y_test, y_pred))  # 如果小于之前的MSE  证明这里少一个特征得到的系数更佳,模型就更佳


# 行情数据关系测试
stock_data = pd.read_csv('./data/data.csv')
print(stock_data.head(100))
stock_train = stock_data[['shou_change', 'dd_change', 'zd_money']]
last_data = stock_train[stock_train['shou_change'] != 0.]
print(last_data.head(100))
X_t = last_data[['shou_change', 'dd_change']]
y_t = last_data['zd_money']
stock_linreg = one_linear(X_t, y_t)
print(stock_linreg.intercept_, stock_linreg.coef_)  # 0.0455617718101 [ 2.79945893  1.49123189]
