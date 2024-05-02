# -- coding: utf-8 -
"""
@project    :scrapy_test
@file       :ClassMethod.py
@Author     :wooght
@Date       :2024/5/2 16:51
@Content    :@classmethod 方法问题
"""


class A:
    name = 'A'
    age = 30

    def __init__(self, name, age):
        self.name, self.age = name, age

    @classmethod
    def add_age(cls):
        cls.age += 1
        return cls.age

    def cut_age(self):
        self.age -= 1
        return self.age

    @classmethod
    def new_one(cls, name, age):
        return cls(name, age)

person = A('wooght', 18)
print(person.age)       # 18
person.cut_age()
print(person.age)       # 17
print(A.add_age())      # 31
print(A.age)            # 31
"""
    classmethod 类方法,不实例化通过类名可以直接访问
    类似于工厂模式,及类本身的方法,而其他方法为实例化对象的方法
    修改工厂,不会对已经出厂的对象参数影响
"""

person_2 = A.new_one('pwf', 36)
print(person_2.age)     # 36
"""
    classmethod 可以实现多个构造函数
"""

class B(A):
    def cut_age(self):
        self.age -= 2

print(B.age)            # 31    及继承的时候,工厂(A)的值
B.add_age()
print(B.age)            # 32
print(A.age)            # 31    继承在工厂模式中,也算是实例化了一次
