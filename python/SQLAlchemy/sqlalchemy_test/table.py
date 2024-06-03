# -- coding: utf-8 -
"""
@project    :HandBook
@file       :table.py
@Author     :wooght
@Date       :2024/6/3 13:18
@Content    :sqlalchemy 测试_模型
"""
from sqlalchemy import create_engine, String, Integer, MetaData, Column, VARCHAR, FLOAT, DATETIME, Date, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship
import datetime
import sys
sys.path.append('../../')
from wooght_tools.SecretCode import Wst

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
BaseTable = declarative_base()

class Sclass(BaseTable):
    __tablename__ = 'sclass'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(VARCHAR(32))
    floor = Column(Integer, default=1)

    def __repr__(self):
        return '[Class:%s,ID:%s]' % (self.name, self.id)
class Boys(BaseTable):
    __tablename__ = 'boys'
    id = Column(Integer, primary_key=True, autoincrement=True)
    age = Column(Integer, default=18)
    height = Column(FLOAT, default=170.0)
    name = Column(VARCHAR(32), nullable=False)
    birthday = Column(Date, default=datetime.date.today)
    like_id = Column(Integer, ForeignKey('girls.id', ondelete='SET NULL'))
    class_id = Column(Integer, ForeignKey('sclass.id', ondelete='SET NULL'))         # ForeignKey 定义外键 ()中填写数据库实际的名称及field
    # 外键映射
    sclass = relationship('Sclass', backref='boys')     # 和数据库每关系,目的为了链表查询
    girls = relationship('Girls', backref='boys')       # 应用的时候可以直接访问girls的字段
    """
    外键约束:
    RESTRICT：若子表中有父表对应的关联数据，删除父表对应数据，会阻止删除。默认项
    NO ACTION：在MySQL中，同RESTRICT。
    CASCADE：级联删除。
    SET NULL：父表对应数据被删除，子表对应数据项会设置为NULL。
    """

class Girls(BaseTable):
    __tablename__ = 'girls'
    id = Column(Integer, primary_key=True, autoincrement=True)
    age = Column(Integer, default=18)
    height = Column(FLOAT, default=160.0)
    name = Column(VARCHAR(32), nullable=False)
    birthday = Column(Date, default=datetime.date.today)
    like_id = Column(Integer, default=0)
    class_id = Column(Integer, ForeignKey('sclass.id', ondelete='SET NULL'))

Session = sessionmaker(bind=engine)

if __name__ == '__main__':
    BaseTable.metadata.create_all(engine)