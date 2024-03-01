# -*- coding: utf-8 -*-
#
# @method   : scikit-learn KNN(最近邻)
# @Time     : 2018/4/2
# @Author   : wooght
# @File     : w_KNN.py
# 涉及词条: neighbors: 领居
# KNN分类,KNN回归

from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from common.classfy_plt_3d import classfy_plt_3d
from sklearn.model_selection import train_test_split
from Tdata import ad_sample
import numpy as np

# iris 原始数据
iris = load_iris()
X = iris.data[:, 1:3]
Y = iris.target
x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=1)
plt.scatter(x_train[:, 0], x_train[:, 1], marker='o', c=y_train)
plt.show()

# KNeighorsClassifier K最近邻分类
clf = KNeighborsClassifier(n_neighbors=10, algorithm='kd_tree', weights='distance')
# n_neighbors K值的选择,默认5
# weights K个近邻样本的权重 默认的"uniform"，所有最近邻样本权重都一样,"distance",则权重和距离成反比例
# algorithm 一共有三种算法brute，kd_tree，ball_tree  可以填写auto,自动选择最佳
clf.fit(x_train, y_train)
classfy_plt_3d(clf, x_test, y_test)
print(clf.predict_proba(x_test))
print(clf.score(x_train, y_train))

# KNeighorsRegressor K最近邻回归
rgs = KNeighborsRegressor(n_neighbors=5, algorithm='auto', weights='distance')
rgs.fit(x_train, y_train)
print(rgs.predict(x_test))


# 图表工具
def plt_def(result, y_train, title):
    plt.title('score:'+str(title))
    plt.plot(np.arange(len(result)), y_train, color='black')
    plt.plot(np.arange(len(result)), result, color='blue')
    plt.legend()
    plt.show()

# 最近邻回归效果图表展示
data = ad_sample()  # 广告收益数据
x, y = data[:, :3], data[:, 3]
x_train, y_train = x[:100], y[:100]  # 样本
x_test, y_test = x[100:], y[100:]  # 测试样本

rgs = KNeighborsRegressor(n_neighbors=10)
rgs.fit(x, y)
result = rgs.predict(x_test)
plt_def(result, y_test, rgs.score(x_test, y_test))


# 交叉验证用于调节参数
from sklearn.model_selection import cross_val_score
k_range = np.arange(1, 40)
k_scores = []
for k in k_range:
    # 获取K等于某个值时,测试准确率
    knn = KNeighborsClassifier(n_neighbors=k)  # 调节K值
    # cross_val_score 交叉验证 原因:因为model.score(x_test, y_test)会根据test数据不同而不同
    # cv=N,将数据集平均分割成N个等份
    # 使用1份数据作为测试数据，其余作为训练数据
    scores = cross_val_score(knn, X, Y, cv=10, scoring='accuracy')
    k_scores.append(scores.mean())

print(k_scores)
plt.plot(k_range, k_scores)
plt.show()
