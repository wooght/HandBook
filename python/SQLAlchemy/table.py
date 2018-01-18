# -*- coding: utf-8 -*-
__author__ = 'wooght'
from sqlalchemy import create_engine, Table, Column ,MetaData, select
from sqlalchemy import VARCHAR as Varchar,TEXT as Text, Integer, String, ForeignKey
# 连接数据库
#mysql+pymysql  表示数据库为mysql,通过pymysql为基础链接操作数据库
engine = create_engine("mysql+pymysql://homestead:secret@192.168.10.10:3306/scrapy?charset=utf8",encoding="utf-8", echo=False)
# 获取元数据
metadata = MetaData()

#上证E互动 sns_sseinfo
sns_sseinfo = Table('sns_sseinfo',metadata,
    Column('id',Integer,primary_key=True),
    Column('time',String(56)),              #时间
    # Column('ask',Varchar(256)),             #问题
    Column('ask',Text(256)),             #问题
    Column('anwser',Text()),                #回答
    Column('dm',String(16))                 #股票代码
)
#测试数据表
sns_id = Table('sna_id',metadata,
    Column('id',Integer,primary_key=True),
    Column('info_id',Integer,nullable=False),
    Column('name',String(64),nullable=True)
)
# Column类型有：
#     TIMESTAMP
#     TIME
#     DATETIME
#     DATE
#     CHAR
#     BOOLEAN

#创建数据表 如果存在则pass
metadata.create_all(engine)
#链接数据库
conn = engine.connect()

# i = sns_sseinfo.insert()
# list = dict(time='2017-10-10',ask='aa',anwser='11',dm='11')
# print(i)
# r = conn.execute(i,list)
