# -*- coding: utf-8 -*-
#
# @method   : scikit-learn 之 DecisionTreeClassifier (决策树)
# @Time     : 2018/3/30
# @Author   : wooght
# @File     : decisionTree.py
# 决策树分类,树回归测试预测

from sklearn import tree
import numpy as np
import matplotlib.pyplot as plt
from Tdata import sin_data
from sklearn import datasets
from common.classfy_plt_3d import classfy_plt_3d

# 决策树分类
# 基本操作/流程
# 拟合/训练:fit(样本,样本类标签)---->预测:predict(测试样本)/predict_proba(测试样本)
X = [[1, 2], [2, 3], [1, 3], [2, 4], [3, 1], [3, 2], [4, 2], [4, 1], [1, 1], [2, 2], [3, 3], [4, 4]]
y = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]

# DecisionTreeClassifier 参数说明:
# criterion: Gini(默认),entropy,entropy采用信息增益来选择特征
# max_depth:树的最大深度,默认None,及一直扩展到叶子单一或min_samples_split个样本点
# min_samples_split:一个内部节点最小样本数
tree_model = tree.DecisionTreeClassifier(criterion='entropy')
tree_model = tree_model.fit(X, y)
result_proba = tree_model.predict_proba([[3, 2]], check_input=True)
print('分类概率:', result_proba.tolist())
print('分类结果:', tree_model.predict([[3, 2]]))


# 3D 图表展示分类效果
iris = datasets.load_iris() # 使用自带的iris数据
X = iris.data[:, [0, 2]]
y = iris.target
clf = tree.DecisionTreeClassifier(max_depth=4)  # 训练模型，限制树的最大深度4
clf.fit(X, y)  #拟合模型
classfy_plt_3d(clf, X, y)



# 决策树回归
# fit(变量,结果)
train, test = sin_data()
x_train, y_train = train[:, :2], train[:, 2]  # 数据前两列是x1,x2 第三列是y,这里的y有随机噪声
x_test, y_test = test[:, :2], test[:, 2]  # 同上,不过这里的y没有噪声
# train数据格式:
# [[  0.         -10.           2.69876376]
#  [  0.1002004   -9.95991984   2.36347624]
#  ...,
#  [ 50.          10.           7.29325787]]


# 方法调度函数
def try_different_method(clf):
    clf.fit(x_train, y_train)
    score = clf.score(x_test, y_test)  # 评估预测值和真实值的差异
    result = clf.predict(x_test)
    plt.figure()
    plt.plot(np.arange(len(result)), y_test, 'ro-', label='true', color='blue')
    plt.plot(np.arange(len(result)), result, 'ro-', label='predict', color='black')
    plt.title('score: %f' % score)
    plt.legend()
    plt.show()
    return clf

#
# 树回归
tree_reg = tree.DecisionTreeRegressor()
clf = try_different_method(tree_reg)
# print(clf.coef_)
# print(clf.intercept_)

# 线性回归
from sklearn import linear_model

linear_reg = linear_model.LinearRegression()
clf =try_different_method(linear_reg)
print(clf.coef_)
print(clf.intercept_)
#
#
# # SVM回归
# from sklearn import svm
# svr = svm.SVR()
# try_different_method(svr)
#
# # KNN 回归
# from sklearn import neighbors
# knn = neighbors.KNeighborsRegressor()
# try_different_method(knn)
#
#
# # 随机森林 回归
# from sklearn import ensemble
# rf = ensemble.RandomForestRegressor(n_estimators=20)  # 使用20个决策树
# try_different_method(rf)