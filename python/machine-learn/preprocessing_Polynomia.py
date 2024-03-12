# -*- coding: utf-8 -*-
#
# @method   : scikit-learn 数据预处理之polynomia 多项式
# @Time     : 2018/4/5
# @Author   : wooght
# @File     : preprocessing_Polynomia.py
# 多项式意义: 当线性回归打分不高,但各样本见系数也是偏线性时,可以用多项式回归
# 涉及词条: polynomia [ˌpɒlɪ'noʊmɪrl] 多项式

import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 房价数据集 面积越大,对应房价单价越低
X = [[40], [70], [90], [110], [150], [200]]
y = [[120], [200], [240], [270], [305], [330]]
X_test = [[70], [200]]
y_test = [[200], [330]]
plt.axis([30, 210, 110, 340])
plt.plot(X, y, 'r.')

'''普通线性回归'''

lr = LinearRegression()
lr.fit(X, y)
X2 = [[30], [80], [100], [130], [250]]
y2 = lr.predict(X2)
plt.plot(X2, y2, 'b+-')
print(lr.score(X_test, y_test))  # 匹配分 0.924
print(lr.coef_)


'''
    多项式预处理
    多项式回归
'''

# 多项式回归 因为是曲线,所以需要预测的样本数要更多
# 训练和测试样本都必须是多形式样本
X2 = np.linspace(30, 210, 100)  # 未预测的样本

# 实例多项式模型
pf = PolynomialFeatures(degree=2)  # 二次多项式实例 degree指几次多项式 默认2

# 各样本做多项式转换
X_polynomial = pf.fit_transform(X)  # 对样本做多项式转换
X2_polynomial = pf.transform(X2.reshape(X2.shape[0], 1))  # 对预测样本做多项式转换
Xtest_polynomial = pf.transform(X_test)  # 打分数据做多项式转换

# 回归及预测
lr_quadratic = LinearRegression()
lr_quadratic.fit(X_polynomial, y)  # 训练多项式数据
y2 = lr_quadratic.predict(X2_polynomial)  # 预测
print(lr_quadratic.score(Xtest_polynomial, y_test))  # 匹配分 0.996
print(lr_quadratic.coef_)

plt.plot(X2, y2, 'g-')
plt.show()