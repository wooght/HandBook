# -- coding: utf-8 -
"""
@project    :HandBook
@file       :abc.py
@Author     :wooght
@Date       :2024/5/14 20:20
@Content    :路径测试
"""

import sys, os

def now_pwd():
    print('abc abspath {}'.format(os.path.abspath(__file__)))
    print("abc pathdir {}".format(os.path.dirname(__file__)))
now_pwd()