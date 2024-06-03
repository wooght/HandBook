# -- coding: utf-8 -
"""
@project    :HandBook
@file       :alchemy_sql.py
@Author     :wooght
@Date       :2024/3/14 19:09
@Content    : sqlalchemy 操作数据库 sql方式,ORM方式
"""
import sys
sys.path.append('..')
from wooght_tools.SecretCode import Wst
from wooght_tools.echo import echo
# 导入数据类型模块
from sqlalchemy import Integer, String, Float, select, func
# 导入sql基本模块
from sqlalchemy import create_engine, Table, Column, MetaData
# 导入ORM模块
from sqlalchemy.orm import declarative_base, sessionmaker
import random

host = '127.0.0.1'
port = '3306'
database = 'wooght_test'
user = 'root'
password = Wst.decryption('.u/fe<qzO|~TrC;13E=z2vpQI#]X_?>[_.F!,T`!B')
db_uri = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8'
engine = create_engine(db_uri,echo=False)               # 创建数据库引擎
connect = engine.connect()                              # 引擎与数据库握手连接

"""
    执行SQL语句,通过传统方式操作数据库
    优点:快,稳定
    缺点:易受到SQL攻击
"""
metadata = MetaData()                                   # 定义表容器
"""定义表结构"""
user = Table("user", metadata,
             Column('id', Integer(), primary_key=True),
             Column("name", String(32)),
             Column('age', Integer(),),
             Column('sex',Integer()))

"""
    插入数据
    (1) connect.execute(insert_obj)
        insert_obj = table.insert().values(name='wooght', age=32)
    (2) connect.execute(insert_obj, values)
        insert_obj = name.insert()
        values = [{'name':'wooght', age:32},{'name':'pwf', age:33},...]
"""
to_insert = user.insert().values(
    name=''.join({i: random.choice(Wst.contrast_str) for i in range(1, random.randint(4, 10))}.values()),
    age=random.randint(10, 50), sex=2)
result = connect.execute(to_insert)     # execute 执行任务
print(result.inserted_primary_key)      # (primary_key,)获取主键key值的元祖,因为主键可能是多个列
print(result.rowcount)                  # int 获取插入行数

echo("插入多条数据")
user_insert = user.insert()
nums_list = [
    {'name':''.join(random.sample(Wst.contrast_str, random.randint(5,10))),'age':random.randint(10, 50)},
    {'name':''.join(random.sample(Wst.contrast_str, random.randint(5,10))),'age':random.randint(10, 50)}
]
insert_result = connect.execute(user_insert, nums_list)     # 插入多条数据execute(插入对象,数据字典)
print("新增:",insert_result.rowcount)

"""
    查询数据
    result = table.select()
             table.select().filter()/where()
             select(Column(fieldname),..).select_from(table)
    result.rowcount 查询行数
    result.fetchall() 查询的全部内容, 迭代器,返回字典
"""
user_select = user.select().filter(user.c.age > 0, user.c.id > 0).order_by('id').limit(10)
result = connect.execute(user_select)
print('总行数:', result.rowcount)
for item in result.fetchall():
    print(str(item.id).rjust(3), str(item.name).rjust(15), item.age)
user_wooght = result.fetchall()
print('fetchall遍历后,还有{}条'.format(len(user_wooght)))

user_where = user.select().where(user.c.age > 0).order_by(user.c.id.desc()).limit(10)   # desc的用法
where_result = connect.execute(user_where)
print('where查询排序共{}条'.format(where_result.rowcount))
for item in where_result.fetchmany(5):
    print(str(item.id).rjust(4), str(item.name).rjust(8))

"""指定字段查询"""
echo('指定字段查询')
user_column_s = select(func.count(Column('age')), Column('sex')).select_from(user).group_by(user.c.sex)
result = connect.execute(user_column_s)
for item in result.fetchall():
    print(item)

"""查询单个数据"""
echo("查询单个数据")
user_one_s = user.select().where(user.c.name == 'wooght').order_by(user.c.id.desc())
user_one_r = connect.execute(user_one_s)
user_one_item = user_one_r.first()
print(user_one_item.name)

"""模糊查询"""
echo('模糊查询')
user_like_s = user.select().where(user.c.name.like('%oo%'))
user_like_r = connect.execute(user_like_s)
current_user = user_like_r.first()
print(current_user.name)

"""修改数据"""
user_update = user.update().where(user.c.id == 67).values(name='puwenfeng')
result = connect.execute(user_update)
print('修改{}条数据'.format(result.rowcount))

"""删除数据"""
user_delete = user.delete().where(user.c.age==32)
result = connect.execute(user_delete)
print('共删除:', result.rowcount, '条数据')
# connect.rollback()        # 回滚数据,本运行的操作全部撤销
connect.commit()            # 最终提交
connect.close()

"""
    ORM操作数据库->见alchemy_orm
    优点:可以快速创建数据表,支持业务对象
    缺点:速度比直接执行SQL慢
"""
"""
    反射,可以利用已经存在的数据表填充SQLALchemy对象
"""
