# -*- coding: utf-8 -*-
#
# @method   : scikit-learn 之linear_model  线性回归
# @Time     : 2018/3/29
# @Author   : wooght
# @File     : linear.py
# 涉及词条 regressor 回归

import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from Tdata import ad_sample

data = pd.read_csv('./data/Folds5x2_pp.csv')
print(data.head())  # 输出前五条 tail() 指末尾数据 默认5条
print(data.shape)  # 查看数据维度

X = data[['AT', 'V', 'AP', 'RH']]
y = data['PE']

# 划分训练集和测试集 train为训练街,test为测试集
# X_train 为训练自变量,y_train 为自变量对应的因变量
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
# random_state 随机数种子,每次都填写1,那么每次的随机数相同,及数组排序的顺序


# 训练线性回归模型
def one_linear(x, y):
    from sklearn.linear_model import LinearRegression
    linreg = LinearRegression()
    linreg.fit(x, y)  # 样本拟合或者叫做 训练 得到:模型  x:自变量,y:结果(因变量)
    return linreg


# 图表工具
def plt_def(result, y_train, title):
    plt.title('score:'+str(title))
    plt.plot(np.arange(len(result)), y_train, color='black')
    plt.plot(np.arange(len(result)), result, color='blue')
    plt.show()


linreg = one_linear(X_train, y_train)
print('截距:', linreg.intercept_)  # 截距
print('回归系数:', linreg.coef_)  # 回归系数
y_pred = linreg.predict(X_test)  # 通过模型样本预测
print('预测结果:', y_pred)
# 方程为 截距+回归系数*变量
# [-1.97376045 -0.23229086  0.0693515  -0.15806957]
plt_def(y_pred[-100:], y_test[-100:], linreg.score(X_test, y_test))


# 模型评价
# 两种方式:MSE 均方误差，RMSE均方根误差
from sklearn import metrics

# 对模型进行评价,不同方法得到的不同系数,选择MSE最小的时候对应的方法或者系数最佳
print('MSE', metrics.mean_squared_error(y_test, y_pred))
print('RMSE', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))

# 少选择一个特征 看系数是否更佳
X = data[['AT', 'V', 'RH']]  # 原来为: ['AT', 'V', 'AP', 'RH']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
linreg = one_linear(X_train, y_train)
y_pred = linreg.predict(X_test)
# 如果小于之前的MSE  证明这里少一个特征得到的系数更佳,模型就更佳
print('New MSE:', metrics.mean_squared_error(y_test, y_pred))


#  广告投放效果回归测试
data = ad_sample()
x, y = data[:, :3], data[:, 3]
x_train, y_train = x[:100], y[:100]  # 样本
x_test, y_test = x[100:], y[100:]  # 测试样本

ad_linreg = one_linear(x_train, y_train)
result = ad_linreg.predict(x_test)
plt_def(result, y_test, ad_linreg.score(x_test,y_test))


# 行情数据关系测试
stock_data = pd.read_csv('./data/data.csv')
stock_train = stock_data[['shou_change', 'dd_change', 'zd_money']]
last_data = stock_train[stock_train['shou_change'] != 0.]
X_t = last_data[['shou_change', 'dd_change']]
y_t = last_data['zd_money']
stock_linreg = one_linear(X_t, y_t)
print(stock_linreg.intercept_, stock_linreg.coef_)  # 0.0455617718101 [ 2.79945893  1.49123189]

# 图表查看
test_data = X_t.head(100)
result = stock_linreg.predict(test_data)
plt.plot(np.arange(len(result)), list(last_data.head(100)['zd_money']), lw=3, color="blue")  # 实际值
plt.plot(np.arange(len(result)), result, linewidth=3, color="black")  # 预测值(较好的回归,是预测值有较好的收敛)
plt.show()
