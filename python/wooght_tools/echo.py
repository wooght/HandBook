# -- coding: utf-8 -
"""
@project    :HandBook
@file       :echo.py
@Author     :wooght
@Date       :2024/3/15 18:10
@Content    : 简易输出模块区分
"""


def echo(*ss):
    if len(ss) == 1:
        print("=" * 80, '\r\n', ss[0].center(80, " "), '\r\n', "=" * 79, end='\r\n')
    else:
        print("_" * 50)
        for str in ss: print(str)
        print("-" * 30)
