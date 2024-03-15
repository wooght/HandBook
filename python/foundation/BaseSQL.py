# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseSQL.py
@Author     :wooght
@Date       :2024/3/14 19:09
@Content    : sqlalchemy 操作数据库 sql方式,ORM方式
"""
import sys
sys.path.append('..')
from wooght_tools.SecretCode import Wst
from wooght_tools.echo import echo
# 导入数据类型模块
from sqlalchemy import Integer, String, Float
# 导入sql基本模块
from sqlalchemy import create_engine, Table, Column, MetaData
# 导入ORM模块
from sqlalchemy.orm import declarative_base, sessionmaker
import random

host = '127.0.0.1'
port = '3306'
database = 'wooght_test'
user = 'root'
password = Wst.decryption('}a,>aN4|Y,9xODC0HUwq%.*T7<]+7}B>{P$>x')
db_uri = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8'
engine = create_engine(db_uri,echo=False)               # 创建数据库引擎
connect = engine.connect()                              # 引擎与数据库握手连接

"""
    执行SQL语句,通过传统方式操作数据库
    优点:快,稳定
    缺点:易收到SQL攻击
"""
metadata = MetaData()                                   # 定义表容器
"""定义表结构"""
user = Table("user", metadata,
             Column('id', Integer(), primary_key=True),
             Column("name", String(32)),
             Column('age', Integer(),),
             Column('sex',Integer()))
"""插入数据"""
to_insert = user.insert().values(
    name=''.join({i: random.choice(Wst.contrast_str) for i in range(1, random.randint(4, 10))}.values()),
    age=random.randint(10, 50), sex=1)
result = connect.execute(to_insert)     # execute 执行任务
print(result.inserted_primary_key)      # 获取主键key值
print(result.rowcount)                  # 获取插入行数
echo("插入多条数据")
user_insert = user.insert()
nums_list = [
    {'name':''.join(random.sample(Wst.contrast_str, random.randint(5,10))),'age':random.randint(10, 50)},
    {'name':''.join(random.sample(Wst.contrast_str, random.randint(5,10))),'age':random.randint(10, 50)}
]
insert_result = connect.execute(user_insert, nums_list)
print("新增:",insert_result.rowcount)
"""查询数据"""
user_select = user.select().filter(user.c.age>0,user.c.id>0).order_by('age').limit(10)
result = connect.execute(user_select)
print('总行数:',result.rowcount)
for item in result.fetchall():
    print(str(item.id).rjust(3), str(item.name).rjust(15), item.age)
user_wooght = result.fetchall()
print(len(user_wooght))             # fetchall() 是迭代器
"""查询单个数据"""
user_one_s = user.select().where(user.c.name=='wooght').order_by(user.c.id.desc())
user_one_r = connect.execute(user_one_s)
user_one_item = user_one_r.first()
print(user_one_item.name)
"""修改数据"""
user_update = user.update().where(user.c.id==67).values(name='puwenfeng')
result = connect.execute(user_update)
"""删除数据"""
user_delete = user.delete().where(user.c.age==32)
result = connect.execute(user_delete)
print('共删除:',result.rowcount)
# connect.rollback()        # 回滚数据,本运行的操作全部撤销
connect.commit()            # 最终提交
connect.close()

"""
    ORM操作数据库
    优点:可以快速创建数据表,支持业务对象
    缺点:速度比直接执行SQL慢
"""
echo('ORM操作')
Base = declarative_base()           # 元数据容器,表基类
"""定义表结构"""
class Bank(Base):
    __tablename__ = "Bank"
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer)
    moneys = Column(Float)

orm_engine = create_engine(db_uri)
Base.metadata.create_all(orm_engine)        # 无则创建表
Session = sessionmaker(bind=orm_engine)     # 绑定数据库映射
session = Session()                         # 建立会话
"""插入数据"""
new_nums = Bank(user_id=user_one_item.id, moneys=100)
session.add(new_nums)
# session.commit()            # 提交
"""查询数据"""
select_bank = session.query(Bank)
print('银行数据如下:')
print([row.moneys for row in select_bank])
"""条件查询"""
filter_select = session.query(Bank).filter(Bank.user_id==5).order_by(Bank.moneys)
print(filter_select.first().moneys)
print(filter_select[0].moneys)
print([row.moneys for row in filter_select])
"""修改数据"""
one_bank = session.query(Bank).filter(Bank.user_id==5).first()
one_bank.moneys = 200
"""删除数据"""
session.delete(one_bank)
session.commit()

"""
    反射,可以利用已经存在的数据表填充SQLALchemy对象
"""
