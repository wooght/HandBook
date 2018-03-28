# -*- coding: utf-8 -*-
#
# @method   : sklearn-naive_bayes_classifier(朴素贝叶斯分类)
# @Time     : 2018/3/27
# @Author   : wooght
# @File     : NBC.py

import pandas as pd
import numpy as np
from sklearn import metrics

df = pd.read_csv('./data/data.csv')
print(df)
new_df = df.loc[:, ['shou_change', 'dd_change']]
arr = new_df.values
print(arr)


# 多项式分布的朴素贝叶斯  --多远离散值
def m_nb(x, y):
    from sklearn.naive_bayes import MultinomialNB
    model = MultinomialNB(alpha=0.9)  # alpha默认为1 根据拟合效果可适当调整
    model.fit(x, y)  # 数据拟合
    return model


# 高斯分布的朴素贝叶斯  --大部分是连续值
def g_nb(x, y):
    from sklearn.naive_bayes import GaussianNB
    model = GaussianNB()
    model.fit(x, y)
    return model


# 伯努利分布的朴素贝叶斯 --二元离散值或者很稀疏的多元离散值
def b_nb(x, y):
    from sklearn.naive_bayes import BernoulliNB
    model = BernoulliNB()
    model.fit(x, y)
    return model


x1 = np.array([[3, 4, 0, 1, 4], [2, 0, 1, 3, 2], [1, 3, 5, 2, 4]])  # 样本
y1 = np.array([0, 1, 2])  # 样本标签
t1 = np.random.randint(5, size=(1, 5))  # 测试数据
yb = m_nb(x1, y1)
print('分类结果:', yb.predict(t1))  # 预测,返回结果标签
print('概率分布:', yb.predict_proba(t1))  # 预测,返回对应概率
print('概率对数:', yb.predict_log_proba(t1))  # 预测,返回概率对数
print('t1', t1)
print('y1', y1)
print(metrics.accuracy_score(t1[0], x1[0]))
print(metrics.accuracy_score(t1[0], x1[1]))

# 支持pandas数据格式
x1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
x2 = pd.Series(np.random.randint(5, size=(1, 5))[0], index=['a', 'b', 'c', 'd', 'e'])
yb = m_nb([x1, x2], np.array([0, 1]))
print('pd数据处理:', yb.predict([pd.Series(np.random.randint(5, size=(1, 5))[0], index=['a', 'b', 'c', 'd', 'e'])]))
