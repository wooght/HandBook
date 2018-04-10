# -*- coding: utf-8 -*-
#
# @method   : scikit-learn 之 RandomForest(随机森林分类,回归)
# @Time     : 2018/4/10
# @Author   : wooght
# @File     : w_RandomForest.py
# 涉及词条: ensemble  [ɑ:nˈsɑ:mbl] 集成

from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.model_selection import train_test_split
import numpy as np
from common.classfy_plt_3d import classfy_plt_3d

data = datasets.load_iris()
X = data.data[:, 0:2]
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

''' RF 分类 '''

clf = RandomForestClassifier()
clf.fit(X_train, y_train)
print(clf.predict(X_test))
print(clf.predict_proba(np.array([[5, 3]])))
print(clf.score(X_test, y_test))

# 参数调节
# n_estimators = 10 默认10,弱学习期最大迭代次数
# bootstrap = True 是否放回抽样 默认True
# oob_score = False 是否采用袋外样本评估 袋外样本指未有抽到的样本
# criterion = 'gini' CART树对特征的评判标准 有基尼系数(gini)和信息增益(entropy)
# 还有其他决策树的参数
clf = RandomForestClassifier(n_estimators=10, bootstrap=True, max_depth=8)
clf.fit(X_train, y_train)
print(clf.score(X_test, y_test))
classfy_plt_3d(clf, X_test, y_test)


''' 最佳参数搜索 '''
# from sklearn.grid_search import GridSearchCV
from sklearn.model_selection import GridSearchCV
param_test = {'n_estimators': range(5, 50, 5), 'max_depth': range(5, 30, 5)}
gsearch = GridSearchCV(estimator=RandomForestClassifier(bootstrap=True), param_grid=param_test, cv=5)
gsearch.fit(X_train, y_train)
print(gsearch.best_params_, gsearch.best_score_)


''' RF 回归 '''

import Tdata
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

data_train, data_test = Tdata.sin_data()
X_train = data_train[:, :2]
y_train = data_train[:, 2]
X_test = data_test[:, :2]
y_test = data_test[:, 2]

# 参数和分类基本一样
rgs = RandomForestRegressor()
rgs.fit(X_train, y_train)
print(rgs.score(X_test, y_test))

plt.plot(X_test[:, 0], y_test, 'b-')
plt.plot(X_test[:, 0], rgs.predict(X_test), 'k-')
plt.title('score:'+str(rgs.score(X_test, y_test)))
plt.show()

