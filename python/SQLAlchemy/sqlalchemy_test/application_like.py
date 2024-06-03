# -- coding: utf-8 -
"""
@project    :HandBook
@file       :application_like.py
@Author     :wooght
@Date       :2024/6/3 14:45
@Content    :
"""
from table import Session, Boys, Girls, Sclass
import random
s = Session()

class_exists = {row.id:row.name for row in s.query(Sclass).all()}
boys_exists = {row.id:row.name for row in s.query(Boys).all()}
girls_exists = {row.id:row.name for row in s.query(Girls).all()}

def set_like(Tables, current_table, exists):
    """
    随机修改男生,女生的喜欢对象ID,班级ID
    Parameters
    ----------
    Tables          目标数据表
    current_table   当前操作的数据
    exists          可选对象
    """
    for id in current_table.keys():
        r = s.query(Tables).filter_by(id=id).update(
            {'like_id':random.choice(list(exists.keys())), 'class_id':random.choice(list(class_exists.keys()))})
        print('修改数据{}条'.format(r))

set_like(Boys, boys_exists, girls_exists)
set_like(Girls, girls_exists, boys_exists)
s.commit()
s.close()