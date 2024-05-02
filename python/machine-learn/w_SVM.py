# -*- coding: utf-8 -*-
#
# @method   : scikit-learn 之 SVM (支持向量机分类/回归)
# @Time     : 2018/4/10
# @Author   : wooght
# @File     : w_SVM.py

# SVM概念:
# 分隔超平面：将数据集分割开来的直线叫做分隔超平面。
# 超平面：如果数据集是N维的，那么就需要N-1维的某对象来对数据进行分割。该对象叫做超平面，也就是分类的决策边界。
# 间隔： 一个点到分割面的距离，称为点相对于分割面的距离。
# 数据集中所有的点到分割面的最小间隔的2倍，称为分类器或数据集的间隔。
# 最大间隔：SVM分类器是要找最大的数据集间隔。
# 支持向量：坐落在数据边际的两边超平面上的点被称为支持向量

from sklearn.svm import SVC

from Tdata import gender_sample
from common.classfy_plt_3d import classfy_plt_3d

X, Y = gender_sample()
X = X[:, 0:2]

''' SVC/NuSVC '''

clf = SVC(probability=True)  # SVC和NuSVC类似
clf.fit(X, Y)
print(clf.fit(X, Y))
test = [[168, 120]]
# SVC参数格式
# SVC(B=1.0, cache_size=200, class_weight=None, coef0=0.0,
#   decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
#   max_iter=-1, probability=False, random_state=None, shrinking=True,
#   tol=0.001, verbose=False)
# SVC参数解释
# B: 目标函数的惩罚系数C，用来平衡分类间隔margin和错分样本的，default B = 1.0；
# kernel：核函数选择,有RBF(高斯核函数,是线性不可分SVM常用的核函数之一),
#           Linear(线性核函数), Poly(多项式核函数), Sigmoid, 默认的是"RBF"
# degree：Poly下多项式的最高次幂；
# gamma：核函数的系数('Poly', 'RBF' and 'Sigmoid'), 默认是gamma = 1 / n_features;
# coef0：核函数中的独立项，'RBF' and 'Poly'有效；
# class_weight	 指定样本各类别的的权重，主要是为了防止训练集某些类别的样本过多，导致训练的决策过于偏向这些类别。这里可以自己指定各个样本的权重，或者用“balanced”，如果使用“balanced”，则算法会自己计算权重，样本量少的类别所对应的样本权重会高。当然，如果你的样本类别分布没有明显的偏倚，则可以不管这个参数，选择默认的"None"
# probablity: 可能性估计是否使用(true or false)；及predict_proba是否可用,默认False
# max_iter: 最大迭代次数，default = 1， if max_iter = -1, no limited;
# decision_function_shape ： ‘ovo’ 一对一, ‘ovr’ 多对多  or None 无, default=None ovo效果相对较精准
# random_state ：用于概率估计的数据重排时的伪随机数生成器的种子。
print(clf.predict(test))
print(clf.predict_proba(test))
classfy_plt_3d(clf, X, Y)


''' LinearSVC '''

from sklearn.svm import LinearSVC

clf = LinearSVC()
clf.fit(X, Y)

dec = clf.decision_function(test)  # 返回的是样本距离超平面的距离
print(dec)

# 预测
print(clf.predict(test))


''' SVM之 SVR回归'''

from sklearn.svm import SVR, LinearSVR
import matplotlib.pyplot as plt
from Tdata import ad_sample
import numpy as np

data = ad_sample()
X = data[:20, 0:3]
Y = data[:20, 3]

svr_rbf = SVR(kernel='rbf')  # 核函数 rbf 高斯
svr_poly = SVR(kernel='poly', degree=2, C=1e3)  # 核函数 poly 多项式,degree=3 多项式次数为3
svr_line = SVR(kernel='linear', C=1e3)  # 和函数 linear ,C惩罚系数 默认是1.0
svr_L = LinearSVR(C=1e3)
svr_rbf.fit(X, Y)
svr_poly.fit(X, Y)
svr_line.fit(X, Y)
svr_L.fit(X, Y)
result_rbf = svr_rbf.predict(X)
result_poly = svr_poly.predict(X)
result_line = svr_line.predict(X)
result_L = svr_L.predict(X)
plt.plot(np.arange(len(result_rbf)), Y, 'b.')
plt.plot(np.arange(len(result_rbf)), result_rbf, 'k-', label='rbf')
plt.plot(np.arange(len(result_rbf)), result_poly, 'r-', label='poly')
plt.plot(np.arange(len(result_rbf)), result_line, 'y-', label='linear')
plt.plot(np.arange(len(result_rbf)), result_L, 'go-', label='LinearSVR')
plt.legend()
plt.show()
print('rbf_score:', svr_rbf.score(X, Y))
print('poly_score:', svr_poly.score(X, Y))
print('linear_score:', svr_line.score(X, Y))
print('LinearSVR:', svr_L.score(X, Y))

# 总结
# 一般推荐在做训练之前对数据进行归一化，当然测试集中的数据也需要归一化。。
# 在特征数非常多的情况下，或者样本数远小于特征数的时候，使用线性核，效果已经很好，并且只需要选择惩罚系数C即可。
# 在选择核函数时，如果线性拟合不好，一般推荐使用默认的高斯核'rbf'。这时我们主要需要对惩罚系数C和核函数参数γγ进行艰苦的调参，通过多轮的交叉验证选择合适的惩罚系数C和核函数参数γγ。
# 理论上高斯核不会比线性核差，但是这个理论却建立在要花费更多的时间来调参上。所以实际上能用线性核解决问题我们尽量使用线性核。
