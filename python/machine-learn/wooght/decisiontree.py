# -*- coding: utf-8 -*-
#
# @method   : 决策树算法
# @Time     : 2018/4/10
# @Author   : wooght
# @File     : decisiontree.py

import numpy as np
from math import log

'''
    决策树算法流程:
    1:样本
    2:香农熵
    3:信息增益
        a:特征选择-->2,3
        b:特征方向/类型分类
        c:递归a,b生产树
    4:样本预测  
'''


class TreeClassfly:
    tree = {}

    def fit(self, X):
        self.tree = self.createTree(X)
        return self.tree

    def predict(self, X):
        return self.classfly(X, self.tree)

    def classfly(self, X, tree):
        for i in tree:
            for item in tree[i].items():
                if X[i] == item[0]:
                    if type(item[1]).__name__ == 'dict':
                        del X[i]
                        return self.classfly(X, item[1])
                    else:
                        return item[1]



    def createTree(self, X):
        if X.shape[0] == 1:
            print(X.dtype)
            return X[0]
        if len(set(X[:, -1])) == 1:
            return X[0, -1]
        # 特征选择
        besti = self.bestfeature(X)
        # 特征分类
        newsdata = self.splitData(X, besti)
        tree = {}
        for i in newsdata.items():
            if besti not in tree:
                tree[besti] = {}
            tree[besti][i[0]] = self.createTree(i[1])
        return tree


    def shares_shang(self, data):
        if data.shape[0] == 1:
            return 0
        data = data[:, -1]
        shang = 0
        feature = {}
        feature_pvc = 0
        for i in data:
            if i not in feature:
                feature[i] = 0
            feature[i] += 1
            feature_pvc += 1
        for i in feature.items():
            pvc = i[1]/feature_pvc
            shang += -pvc* log(pvc, 2)
        return shang

    def bestfeature(self, data):
        cols = data.shape[1]
        rows = data.shape[0]
        min_shang = 0
        besti = 0
        for i in range(cols-1):
            newdata = self.splitData(data, i)
            shang = 0
            for feature in newdata.items():
                s = self.shares_shang(feature[1])
                shang += feature[1].shape[0]/rows * s
            if min_shang == 0 :
                min_shang = shang
            if min_shang > shang:
                besti = i
                min_shang = shang
        return besti

    def splitData(self, data, i):
        rows = data.shape[0]
        newdata = {}
        for row in range(rows):
            num = data[row][i]
            data_tmp = data[row][0:i]
            data_tmp2 = data[row][i+1:]
            if data_tmp.shape[0] > 0 and data_tmp2.shape[0] > 0:
                data_tmp = np.column_stack([data_tmp, data[row][i+1:]])
            else:
                data_tmp = data_tmp2 if data_tmp.shape[0] ==0 else data_tmp
            if num not in newdata:
                newdata[num] = data_tmp
            else:
                newdata[num] = np.row_stack([newdata[num], data_tmp])
        return newdata





dataSet = np.array([[1, 1, 1], [1, 0, 0], [0, 1, 0], [1, 1, 1], [0, 0, 0]])
clf = TreeClassfly()
print(clf.fit(dataSet))
print(clf.predict([0, 1]))