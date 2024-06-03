# -- coding: utf-8 -
"""
@project    :HandBook
@file       :alchemy_orm.py
@Author     :wooght
@Date       :2024/6/2 23:27
@Content    :ORM操作
"""
from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
# from sqlalchemy.ext.declarative import declarative_base     # 2.0已经不再使用
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, SmallInteger, Index, UniqueConstraint
from sqlalchemy.sql import text
import sys
sys.path.append('..')
from wooght_tools.SecretCode import Wst
import random
"""
    sqlalchemy 本身无法操作数据库,需要借助第三方插件如pymysql等
"""

Base = declarative_base()

class Users(Base):
    __tablename__ = 'orm_users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(32), index=True, nullable=False)       # nullable 是否为空,True表示可以为空
    sex = Column(SmallInteger, default=0)                       # 默认0代表男
    __table_args__ = (
        # UniqueConstraint('id', 'name', name='uix_id_name'),     # 联合唯一
        # Index('id_name', 'name')    # 声明索引
    )

host = '127.0.0.1'
port = '3306'
database = 'wooght_test'
user = 'root'
password = Wst.decryption('.u/fe<qzO|~TrC;13E=z2vpQI#]X_?>[_.F!,T`!B')

engine = create_engine(
    f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8',
    echo=False,         # 打印SQL语句,生成环境关闭
    max_overflow=0,     # 超过连接池大小外最多创建的连接
    pool_size=5,        # 连接池大小
    pool_timeout=10,    # 连接超时时间
    pool_recycle=-1     # 多久后对连接池中的线程进行一次连接回收(重置)
)
Base.metadata.create_all(engine)        # 根据类创建数据库表
# 表结构定义结束/导入结束后 执行connection来执行数据库操作
Session = sessionmaker(bind=engine)  # 根据连接engine绑定会话
session = Session()  # 开启一个会话
user1 = Users(name='wooght')
session.add(user1)
user2 = Users(name='pwf', sex=1)
session.add(user2)
many_users = [Users(name='abc'), Users(name='bcd')]
print(session.add_all(many_users))  # session.add 不返回任何内容?
print('最近一次add新增:', len(session.new))   # session.new 最近一次新增的内容
for item in session.new:
    print(item.name, item.id)       # session.new 无法返回mysql处理后的数据
session.commit()
session.close()     # 关闭会话

"""
    CURD
"""
# 开启新的会话
s = scoped_session(Session)     # 每个线程共用同一个session,目的:线程安全

"""查询"""
r = s.query(Users).filter(Users.id > 1).all()       # filter()传表达式
print('查询{}条数据'.format(len(r)))
for item in r:
    print(item.id, item.name)

r1 = s.query(Users).filter_by(id=5).all()           # filter_by() 传参数
print("查询到{}条数据".format(len(r1)))

r11 = s.query(Users).filter(Users.id.between(10,20), Users.name.like('%oo%')).all()
print('between查询到{}条数据'.format(len(r11)))       # like() 模糊查询
r112 = s.query(Users).filter(Users.name.like('w%')).all()
print('以W开头的用户有{}个'.format(len(r112)))          # 通配符 %

r12 = s.query(Users).filter(Users.id.in_([10, 20, 30])).first()
print('in_查询到的第一条数据是', r12.name, r12.id)      # in_([])   in 注意_和参数是列表
r121 = s.query(Users).filter(Users.id.notin_([10, 20, 30])).first()
print("notin_查询到的第一条数据id是", r121.id)

from sqlalchemy import and_, or_
r13 = s.query(Users).filter(and_(Users.id < 100, Users.name == 'wooght'), Users.sex <= 0).all()
print('and_共查询到{}条数据'.format(len(r13)))

r14 = s.query(Users.name.label('xm'), Users.id).filter(Users.id.__eq__(100)).first()
all_fields = r14._fields    # label()自定义字段名   , _fields   查询行(row)的字段
print('返回字段:', ','.join(all_fields))
for field in all_fields:
    print(getattr(r14, field))      # 动态访问类属性


# :id, :name 占位符,用params 传参数    text()执行sql语句
r2 = s.query(Users).filter(text("id<:id and name=:name")).params(id=11, name='wooght').order_by(Users.id.desc())
for item in r2.all():                               # order_by() 参数为字段  desc() 倒序
    print(item.id, item.name)
# text()执行自定义sql语句
r22 = s.query(Users).from_statement(text("select * from orm_users where id > :id")).params(id=20).all()
print('查询到{}条数据'.format(len(r22)))

"""delete"""
r3 = s.query(Users).filter_by(id=6).delete()        # delete() 返回bool值
print('删除{}!'.format('成功' if r3 else '失败'))

"""update"""
name_model = 'abcdefghijklmnopqrstuvwxyz'
r4 = s.query(Users).filter(and_(Users.id > 40, Users.name == 'wooght')).update(
    {'name': ''.join(random.choices(name_model, k=5))})
print('修改{}条数据'.format(r4))         # update 返回修改条数
r5 = s.query(Users).filter_by(id=100).update({'sex': Users.sex + 1, 'name': 'Test'})
print('执行修改{}条数据'.format(r5))      # update() 参数为字典
r55 = s.query(Users).filter_by(id=100).first()
print(r55.name)
s.commit()

"""group"""
r6 = s.query(Users)[1:6]        # limit()的用法, 用于分页
for item in r6:
    print(item.name.rjust(8), item.id)

# order_by 多级应用 先名字倒序,再ID升序
r7 = s.query(Users).filter(Users.id < 10).order_by(Users.name.desc(), Users.id.asc()).all()
for item in r7:
    print(item.name.rjust(8), item.id)

from sqlalchemy import func
r8 = s.query(func.count(Users.name).label('count'), func.max(Users.id).label('maxid')).filter(Users.id < 100).group_by(Users.name).first()
print(r8.count, r8.maxid)       # sqlalchemy的func 常用的sql函数 count max min sum

# having 结合group_by使用,是分组后的筛选
r81 = s.query(func.count(Users.name).label('count'), Users.name).group_by(Users.name).having(func.count(Users.name) > 1).order_by(func.count(Users.name)).all()
for item in r81:
    print(item.count, item.name)

"""一对多见sqlalchemy_test"""
