# -*- coding: UTF-8 -*-
'''
    Python 面向对象  by wooght 2017
'''
from module import wooght #导入module下的wooght模块

wooght.e('haha','\n')#应用模块下的方法
a=wooght.c()#模块下的类
print('\n the class is in :',a.__module__,'\n')#__module__所在模块

class w:
    #构造函数
    def __init__(self):
        print(self)#self 自己,实例(self 可以自定义)
        print(self.__class__)#__class__指本类

    def e(haha):
        print(haha)
        print(haha.__class__)
a=w()
a.e()

#父类
class car:
    name=''
    size=''
    __secret='123456'
    def __init__(self,name,size):
        self.name=name
        self.size=size
    def thecar(self):
        print('the ka is:',self.name,self.size)
        self.__secretfunc()
    def __secretfunc(self):
        print(self.__secret)

a=car('volvo','s90')
a.thecar()
a.name='das auto'
a.size='passter'
a.thecar()
#a.__secretfunc()  __ 双下划线是private 属性

class factory:
    fac_name='dasauto factory'
    _facnum='1153'
    def thefactory(self):
        print('the factory is ',self.fac_name)
    #_单下划线 是protected属性
    def _factorynum(self):
        print(self._facnum)

b=a.__dict__#对象的所有属性 键值对
print(b)
print(b['name'])

#子类  继承父类car 可同时继承多个类
class ren(car,factory):
    people=''
    def theren(self,people):
        self.people=people
        factory.fac_name='volvo factory'#访问父类属性和方法
        self.thefactory()#可以通过self访问父类的方法和属性
    def thecar(self):
        #重写父类方法
        print('the car is:',self.name,self.size,' people is',self.people)
        factory._factorynum(self)

b=ren('ford','moudiudiu')
b.theren('puwenfeng')
b.thecar()
print(b.__dict__)
b.thefactory()#访问父类方法


class M():
    table=''
    sql=''
    def __init__(self,table):
        self.table=table

    def where(self,arr):
        self.sql+=' where'
        for key,value in arr.items():
            self.sql+=' '+key+'='+value
        return self
user=M('users')
user.where({'name':'wooght','age':'18'})
print(user.sql)

#__dict__ 通过字典创建类属性 key是属性名,value是属性值
class todict(object):
    totle = 2
    def __init__(self):
        self.d = {}
        self.set_totle(5)
    def set_totle(self,key):
        self.totle = key
tdict = todict()
tdict.__dict__={'a':1,'b':2}
print(tdict.a)
tdict.set_totle(5)
print(tdict.totle)
