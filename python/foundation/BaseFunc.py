# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseFunc.py
@Author     :wooght
@Date       :2024/3/7 15:50
"""


class A(object):
    def __init__(self):
        print('默认运行')

    def __repr__(self):
        return "类说明"

    def __str__(self):
        return "类str说明"


new_a = A()
print(new_a)
