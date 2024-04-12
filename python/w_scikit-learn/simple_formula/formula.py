# -- coding: utf-8 -
"""
@project    :HandBook
@file       :formula.py
@Author     :wooght
@Date       :2024/4/12 20:42
@Content    :基本公式
"""

def ad(data):
    """
    平均差
    ∑(x-x平均值)
    """
    average = sum(data)/len(data)
    sgm = 0
    for d in data:
        sgm += (d-average)
    return sgm
