# -- coding: utf-8 -
"""
@project    :scrapy_test
@file       :SuperClass.py
@Author     :wooght
@Date       :2024/5/2 15:13
@Content    :继承 super问题
"""

class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age


class Company:
    def __init__(self, c_name):
        self.c_name = c_name


class OnePerson(Person, Company):
    def __init__(self, name, age, c_name):
        super().__init__(name, age)         # super 默认运行第一个继承
        Company.__init__(self, c_name)      # 其他继承类需点名继承,并且传递self

one = OnePerson('wooght', 30, '航城科技')
print(one.name)