# -*- coding: utf-8 -*-
__author__ = 'wooght'
from sqlalchemy import TEXT as Text, Integer, String, SmallInteger
from sqlalchemy import create_engine, Table, Column, MetaData
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://homestead:secret@192.168.10.10:3306/scrapy?charset=utf8",encoding="utf-8", echo=False)
metadata = MetaData()

#新闻表
news = Table('news',metadata,
    Column('id',Integer,primary_key=True),
    Column('url',Integer,nullable=False),       #网页地址ID号
    Column('only_id',String(32)),               #唯一标识,去重
    Column('title',String(128),nullable=True),  #新闻标题
    Column('body',Text),                        #新闻内容
    Column('put_time',String(64))               #发布时间
)
#话题表-分析文章
topic = Table('topic',metadata,
    Column('id',Integer,primary_key=True),
    Column('url',Integer,nullable=False),       #网页地址ID号
    Column('only_id',String(32)),               #唯一标识,去重
    Column('title',String(128),nullable=True),  #新闻标题
    Column('body',Text),                        #新闻内容
    Column('put_time',String(64))               #发布时间
)
#行情一行表
quotes_item = Table('quotes_item',metadata,
    Column('id',Integer,primary_key=True),
    Column('code_id',SmallInteger,index=True),      #股票代码
    Column('quotes',Text),                          #60天行情
)

metadata.create_all(engine)
conn = engine.connect()

DB_Session = sessionmaker(bind=engine)
session = DB_Session()

#
# #删除html标签
# def delete_html(str):
#     re_str = re.sub(r'<[^>]*>','',str.strip())
#     return re_str
#
# def alldelete(topic):
#     s = select([topic.c.id,topic.c.body])
#     r = conn.execute(s)
#     num = 0
#     for i in r.fetchall():
#         new_body = delete_html(i[1])
#         u = topic.update().where(topic.c.id==i[0]).values(body=new_body)
#         result = conn.execute(u)
#         if(result.rowcount==1):
#             num+=1
#         else:
#             print('Error!--->行数为:',result.rowcount)
#
#         print(num,'修改成功!')
# alldelete(news)

# s = select([news.c.url,news.c.only_id,news.c.title,news.c.body,news.c.put_time]).where(news.c.put_time>10000000000)
# r = conn.execute(s)
# items = r.fetchall()
# delete_x = []
# for item in items:
#     delete_x.append({'url':item[0],'only_id':item[1],'title':item[2],'body':item[3],'put_time':item[4]})
#
# i = topic.insert()
# r = conn.execute(i,delete_x)
# if(r):
#     print(r.rowcount)

# i = sns_sseinfo.insert()
# list = dict(time='2017-10-10',ask='aa',anwser='11',dm='11')
# print(i)
# r = conn.execute(i,list)

'''数据库设计'''
# 来源网站:
# ID
# URL
# TITLE
# 新闻类:

# ID
# URL           地址
# ONLY_id       唯一标识
# TITLE         标题
# BODY          内容
# CONTENT       内容,去HTML
# PUT_TIME      发布时间
# PUT_TIME_NUM  发布时间 时间暨
# SAVE_TIME     爬取时间
# FROM          来源
