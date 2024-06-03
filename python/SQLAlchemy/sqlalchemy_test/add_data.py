# -- coding: utf-8 -
"""
@project    :HandBook
@file       :add_data.py
@Author     :wooght
@Date       :2024/6/3 13:54
@Content    :
"""
from table import Session, Boys, Girls, Sclass
import random
s = Session()

x = ['张', '王', '李', '蒲', '赵', '钱', '孙', '蒋', '任', '陈']
girl_m = ['芳', '丽', '红', '雅', '小花', '春艳', '萍', '芳芳', '晶晶', '莎莎', '秀清', '秀丽', '田田']
boy_m = ['刚', '伟', '强', '大宝', '二狗', '俊', '雪峰', '子俊', '佳', '波', '龙']
class_list = [{'name': '高三四班', 'floor': 6}, {'name': '高三八班', 'floor': 7}]
exists_class = [row.name for row in s.query(Sclass.name).all()]
for c in class_list:
    if c['name'] not in exists_class:                       # sqlalchemy orm 无直接判断唯一项重复不能添加的功能
        s.add(Sclass(name=c['name'], floor=c['floor']))

print('新增{}个班级'.format(len(s.new)))                      # session.new 获取最近一次add 提交成功的条数

exists_boys = [row.name for row in s.query(Boys.name).all()]
boy = '{}{}'.format(random.choice(x), random.choice(boy_m))
if boy not in exists_boys:
    s.add(Boys(name=boy, height=random.randint(160, 190)))

print('新增{}名男生'.format(len(s.new)))

exists_girl = [row.name for row in s.query(Girls).all()]
girl = '{}{}'.format(random.choice(x), random.choice(girl_m))
if girl not in exists_girl:
    s.add(Girls(name=girl, height=random.randint(150, 180)))

print('新增{}名女生'.format(len(s.new)))
s.commit()
s.close()