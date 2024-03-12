# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseClass.py
@Author     :wooght
@Date       :2024/3/11 10:45
"""
import random
class People(object):
    name = ''
    age = 0
    _sex = 1                 # 建议性的内部成员,但外部可以访问
    sex_contrast = {1: '男', 2: '女'}
    __money = 0              # 强制性的内部成员,外部不能直接访问

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        """打印对象,一般调试用,用于开发过程中明白当前实例是哪个"""
        return f"当前类{self.__class__}, 当前实例:{self.name}"

    def update_age(self, age):
        self.age = age if age > 0 else 0

    def get_money(self):
        return self.__money

    def set_money(self, moneys):
        self.__money = moneys

    def __getattr__(self, item):
        """访问不存在的属性时调用此方法"""
        return False


new_a = People('wooght', 28)
print(new_a)
print(new_a.__dict__)       # {'name': 'wooght'} __dict__对象属性字典,这里不是全部属性,而是实例化过程中使用到的属性
new_a.update_age(18)
print(new_a.__dict__)       # {'name': 'wooght', 'age': 18}
try:
    print(new_a.__money)    # False  __ 外部不能直接访问,当定义了__getattr__函数,就把__属性当成未定义的属性
except AttributeError:
    print('禁止访问财富')
new_a.set_money(100000)
print('财富为:',new_a.get_money())
print(new_a.sex_contrast[new_a._sex])       # 男 _外部可以访问
print(new_a.__dict__)       # {'name': 'wooght', 'age': 18, '_Ren__money': 100000}
print(new_a.height)         # False

class Company:
    company_name = ''
    off_duty_time = 18      # 下班时间
    hour_wages = 100        # 小时工资
    overtime_wages = 200    # 加班工资
    totle_wages = 0         # 总发工资

    def __init__(self, name):
        self.company_name = name

    def compute_wages(self, work_days):
        """计算工资"""
        for s_t, end_t in work_days:
            if end_t >self.off_duty_time:
                day_wages = (18-s_t) * self.hour_wages + (end_t - 18) * self.overtime_wages
            else:
                day_wages =  (end_t - s_t) * self.hour_wages
            self.totle_wages += day_wages
            yield day_wages


class Person(People, Company):
    """ 继承多个类 """
    def __init__(self, name, age, company_name):
        super().__init__(name, age)             # 超类及第一个继承
        # People.__init__(self, name, age)      # 和上面执行效果一样
        Company.__init__(self, company_name)    # 其他继承需要类名访问

    def update_age(self, age):
        """重写父类的方法"""
        self.stay = age - self.age
        self.age = age

    def do_business(self):
        try:
            People.__money *= random.uniform(2,3)           # __子类也无法访问,这里修改无效
        except:
            last_money = self.get_money() * random.uniform(2, 3)
            self.set_money(last_money)
            print('无法访问__属性')

    def get_sex(self):
        return self.sex_contrast[self._sex]

wooght = Person('wooght', 31, '航城科技')
print(wooght)       # 当前类<class '__main__.Person'>, 当前实例:wooght
print(f'职工{wooght.name}的年龄是{wooght.age},公司是{wooght.company_name}')
work_days = [(random.randint(8, 12), random.randint(17, 24)) for x in range(30)]
wages = wooght.compute_wages(work_days)         # 实例访问父类方法
print('第一天工资是:',wages.__next__())
list(wages)
print('总发工资是:',wooght.totle_wages)

second_month_work = [(random.randint(9, 12), random.randint(17, 24)) for x in range(30)]
second_wages = wooght.compute_wages(second_month_work)
list(second_wages)
wooght.set_money(wooght.totle_wages)
print('wooght的财富为:',wooght.get_money())

wooght.update_age(36)
print('已经在公司待了',wooght.stay, '年')
all_person_message = wooght.__dict__
print('员工信息如下:')
for key,value in all_person_message.items():
    print(key, value)

wooght.do_business()            # 无法访问__属性
print('做生意后财富:', wooght.get_money())

print(wooght.get_sex())         # 男
wooght._sex = 2
print(wooght._sex)              # 2
print(wooght.get_sex())         # 女

print(wooght.__dict__)          # 这里多了 _sex