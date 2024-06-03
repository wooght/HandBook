# -- coding: utf-8 -
"""
@project    :HandBook
@file       :application_query.py
@Author     :wooght
@Date       :2024/6/3 15:02
@Content    :综合数据查询-链表查询
"""
from table import Session, Sclass, Boys, Girls
s = Session()
print('男生对应班级')
r = s.query(Boys).all()
print('男生'.ljust(8), '班级'.ljust(8), '喜欢女孩')
"""一对多 正向查询"""
for item in r:
    print(item.name.ljust(8), item.sclass.name.ljust(8), item.girls.name)

sclass = {row.id:row.name for row in s.query(Sclass).all()}
print('女生信息')
print('姓名'.ljust(8), '班级'.ljust(8), '被多少人喜欢')
"""一对多 反向查询"""
r = s.query(Girls).all()
for item in r:
    print(item.name.ljust(8), sclass[item.class_id].ljust(8), len(item.boys))

"""join基于一对多(定义了relationship)链表查询"""
r = s.query(Boys, Girls).join(Boys.girls, isouter=True).all()
for item in r:
    print(item[0].name, '喜欢', item[1].name)