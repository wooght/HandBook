# -*- coding: utf-8 -*-
#
# @method   : sklearn-naive_bayes_classifier(朴素贝叶斯分类)
# @Time     : 2018/3/27
# @Author   : wooght
# @File     : NBC.py

import pandas as pd
import numpy as np
from sklearn import metrics


# 多项式分布的朴素贝叶斯  --多元离散值
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


# 伯努利分布的朴素贝叶斯 --二元离散值 特征取值0,1
def b_nb(x, y):
    from sklearn.naive_bayes import BernoulliNB
    model = BernoulliNB()
    model.fit(x, y)
    return model


x1 = np.array([[1, 1, 3, 4, 5], [5, 4, 3, 2, 1]])  # 样本
y1 = np.array([0, 1])  # 样本标签
t1 = np.random.randint(6, size=(1, 5))  # 测试数据
yb = m_nb(x1, y1)
print(yb.coef_, yb.intercept_)
print('分类结果:', yb.predict(t1))  # 预测,返回结果标签
print('概率分布:', yb.predict_proba(t1))  # 预测,返回对应概率
print('概率对数:', yb.predict_log_proba(t1))  # 预测,返回概率对数
print('x1', x1)
print('t1', t1)
print('y1', y1)
print(metrics.accuracy_score(t1[0], x1[0]))  # 匹配度
print(metrics.accuracy_score(t1[0], x1[1]))

# 支持pandas数据格式
x1 = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
x2 = pd.Series(np.random.randint(5, size=(1, 5))[0], index=['a', 'b', 'c', 'd', 'e'])
yb = m_nb([x1, x2], np.array([0, 1]))
print('pd数据处理:', yb.predict([pd.Series(np.random.randint(5, size=(1, 5))[0], index=['a', 'b', 'c', 'd', 'e'])]))

# 文本分类实例
pos_words = pd.Series({'a': 100, 'b': 130, 'c': 32, 'd': 9, 'e': 7})
neg_words = pd.Series({'a': 9, 'b': 7, 'c': 32, 'd': 100, 'e': 130})
attitude_model = m_nb([pos_words, neg_words], np.array([0, 1]))
test_words = pd.Series({'a': 4, 'b': 0, 'c': 0, 'd': 3, 'e': 0})
result_predict = attitude_model.predict([test_words])
result_proba = attitude_model.predict_proba([test_words])
print(result_proba)
print('分析结果,pos:', '%.5f' % result_proba[0][0], ' neg:', '%.5f' % result_proba[0][1], result_predict)


X = np.array([
    [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3],
    [4, 5, 5, 4, 4, 4, 5, 5, 6, 6, 6, 5, 5, 6, 6]
])
X = X.T  # 转换
y = np.array([-1, -1, 1, 1, -1, -1, -1, 1, 1, -1, 1, 1, 1, 1, -1])
print(np.column_stack((X, y)))
from sklearn.naive_bayes import MultinomialNB

nb = MultinomialNB(alpha=1, fit_prior=True)
nb.fit(X, y)
print(nb.predict(np.array([[3, 5]])))
print(nb.predict_proba(np.array([[3, 5], [2, 5]])))
