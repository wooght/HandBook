# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseOS.py
@Author     :wooght
@Date       :2024/3/15 14:23
@Content    :
"""
# python 系统相关模块
import sys
# 操作系统相关模块
import os

print('模块搜索路径',sys.path)                     # python的path目录
print('系统',sys.platform)                        # win32 当前运行系统环境名称
print('python版本',sys.version)                   # python 版本
print('python路径',sys.executable)                # python解释器的路径

print(os.environ)                                # 操作系统的环境变量
print(os.name)                                   # 操作系统名称,windows是NT,Linux是posix
print(os.path.abspath(__file__))                 # 获取path规范的绝对路径
print(os.path.dirname(__file__))                 # 返回路径的目录
print(os.path.split(__file__))                   # 返回绝对路径,文件名的元祖
print(os.path.getsize(__file__))                 # 返回文件的字符数量


""" 将当前文件目录加入到模块搜索路径中 """
now_dir = os.path.dirname(__file__)
print(now_dir)
sys.path.append(now_dir)
if "E:\\wooght-server\\HandBook\\python\\foundation" in sys.path:
    print('添加成功')

print(os.path.abspath("../../"))                   # 当前目录的上一级目录
print(os.path.dirname("../../"))