# -- coding: utf-8 -
"""
@project    :HandBook
@file       :db.py
@Author     :wooght
@Date       :2024/4/7 19:10
@Content    :访问数据库
"""
from wooght_tools.SecretCode import Wst
from sqlalchemy import Integer, String, Float, Date, Time
from sqlalchemy import create_engine, Table, Column, MetaData

host = '127.0.0.1'
port = '3306'
database = 'linkmart'
user = 'root'
password = Wst.decryption('}a,>aN4|Y,9xODC0HUwq%.*T7<]+7}B>{A$>x')
db_uri = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8'
engine = create_engine(db_uri,echo=False)               # 创建数据库引擎
connect = engine.connect()                              # 引擎与数据库握手连接

"""
    定义表结构
"""

metadata = MetaData()
order_form = Table('order_form', metadata,
                   Column('id', Integer(), primary_key=True, autoincrement=True),
                   Column('form_code', String(32)),
                   Column('goods_name', String(32)),
                   Column('goods_code', String(32)),
                   Column('goods_num', Integer()),
                   Column('goods_money', Float()),
                   Column('form_date', Date()),
                   Column('form_time', Time()),
                   Column('form_money', Float()),
                   Column('form_money_true', Float()),
                   Column('store_id', Integer()))

goods_list = Table('goods_list', metadata,
                   Column('id', Integer(), primary_key=True, autoincrement=True),
                   Column('name', String(32)),
                   Column('bar_code', String()),
                   Column('qgp', Integer()),
                   Column('store_id', Integer()),
                   Column('classify', String()),
                   Column('stock_nums', Integer()),
                   Column('cost', Float()),
                   Column('price', Float()),
                   Column('company', String()),
                   Column('place', String()))

bs_data = Table('bs_data', metadata,
                Column('id',Integer(), primary_key=True, autoincrement=True),
                Column('date', Date()),
                Column('cost', Float()),
                Column('turnover', Float()),
                Column('gross_profit', Float()),
                Column('store_id', Integer()))
