# -*- coding: utf-8 -*-
#
# @method   : 机器学习流程，思路总结
# @Time     : 2018/5/15
# @Author   : wooght
# @File     : machine_learning_base.py

'''
数据预处理，多项式
preprocessing.PolynomialFeatures
定义多项石模型：pf=PolynomialFeatures(degree=2),指2次多项式
pf.fit_transform(X)  对样本做转换
pf.transform(X_test) 对其他测试样本，预测样本做多项式转换
'''