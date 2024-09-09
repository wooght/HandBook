# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseException.py
@Author     :wooght
@Date       :2024/8/29 22:27
@Content    :
"""
import sys, inspect

try:
    num = 1
    str = '11'
    print(num + str)
except Exception as e:
    print(e.__class__.__name__, ':', sys._getframe().f_lineno - 2)  # 获取当前行号
    print(e.__str__(), ':', inspect.currentframe().f_lineno)
