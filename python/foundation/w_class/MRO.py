# -- coding: utf-8 -
"""
@project    :scrapy_test
@file       :MRO.py
@Author     :wooght
@Date       :2024/5/2 14:34
@Content    :python 继承MRO问题
"""


class A:
    def __init__(self, num):
        self.num = num

    def add(self, n):
        print('class:{},num:{}@A.add'.format(self, self.num))
        self.num += n

class B(A):
    def add(self, n):
        print('class:{},num:{}@B.add'.format(self, self.num))
        super().add(n)
        self.num += 2

test_b = B(5)
test_b.add(2)
print(test_b.num)
# out
# class:<__main__.B object at 0x000001A6732B4920>,num:5@B.add
# class:<__main__.B object at 0x000001A6732B4920>,num:5@A.add
# 9
# 实例化后,self指实例化的入口处的class

class C(A):
    def add(self, n):
        print('class:{},num:{}@B.add'.format(self, self.num))
        super().add(n)
        self.num += 3

class D(B, C):
    def add(self, n):
        print('class:{},num:{}@D.add'.format(self, self.num))
        super().add(n)
        self.num += 4

test_d = D(5)
test_d.add(2)
print(test_d.num)
# out
# class:<__main__.D object at 0x00000159B5592B10>,num:5@D.add
# class:<__main__.D object at 0x00000159B5592B10>,num:5@B.add
# class:<__main__.D object at 0x00000159B5592B10>,num:5@B.add
# class:<__main__.D object at 0x00000159B5592B10>,num:5@A.add
# 16
# D->B->A->C->A  变成了 D->B->C->A ->表示super应用,如果中途super断了,就不再继续执行
#                                   比如这里如果B没有super,那么后面的C和A就不会执行
#                                   super的本职功能是运行第一个继承的类,在MRO中,如果中途没有super,则断开MRO
# super顺序: 从左到右,深度优先,重复项保留最后一个
print(D.mro())
# (<class '__main__.One'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)

