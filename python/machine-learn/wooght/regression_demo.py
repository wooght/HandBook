# -*- coding: utf-8 -*-
#
# @method   : 一元线性回归
# @Time     : 2018/5/1
# @Author   : wooght
# @File     : regression_demo.py

# 数学公式
# y = ax+b  a? b?
# w= [sum(xi*yi)-nx^y^]/[sum(xi**2)-nx^**2]
# b = y^-wx^

import matplotlib.pyplot as plt
import numpy as np


class regression:
    w = 0.
    b = 0.


    # 数据训练--数学建模
    def fit(self, x, y):
        dataset = np.column_stack([x, y])
        xy=0
        xexp= 0
        for row in dataset:
            xy += row[0] *row[1]
            xexp+=row[0]**2
        n = dataset.shape[0]  # (100, 2)
        self.w = (xy-n*x.mean()*y.mean())/(xexp-n*x.mean()**2)
        self.b = y.mean() - self.w*x.mean()


    # 模型预测
    def predict(self, x):
        y = self.w*x+self.b
        return y



if __name__ == '__main__':
    # 模拟数据
    x = np.linspace(1, 10, 100)
    y = (3 + np.random.random(100)) * x + (5 + np.random.randint(2, 5, size=100))# 3x + 5
    plt.plot(x, y, 'b.')
    # plt.show()
    rgs = regression()
    rgs.fit(x,y)
    print(rgs.w,rgs.b)
    new_y = rgs.predict(x)
    plt.plot(x,new_y,'k-')
    plt.show()