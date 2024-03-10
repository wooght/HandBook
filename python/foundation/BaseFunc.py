# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseFunc.py
@Author     :wooght
@Date       :2024/3/7 15:50
"""



var_1 = 10
def get_global():
    """
        global 全局变量
    """
    global var_1
    var_1 += 1
    print('var_1通过global引进变为全局变量', var_1)
def get_var():
    print('未声明的变量,函数内部可以调用', var_1)
def update_var():
    try:
        var_1 += 1
        print(var_1)
    except UnboundLocalError:
        print('函数内部没有用global引入的变量,只可访问,不可修改')

get_global()
get_var()
update_var()


class A(object):
    def __init__(self):
        print('默认运行')

    def __repr__(self):
        return "类说明"

    def __str__(self):
        return "类str说明"


new_a = A()
print(new_a)
