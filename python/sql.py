#!/usr/bin/python3
# encoding: utf-8

import pymysql as my
import random

mysqlconfig = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'wooght565758',
    'db': 'linkmart',
    'charset': 'utf8'
}
mysql_connect = my.connect(**mysqlconfig)
# cursor 光标
cursor = mysql_connect.cursor()

# 查询
sql = 'select * from order_form'
data = '0'
cursor.execute(sql)
for row in cursor.fetchmany(3):
    print(row[0], row[1])
# fetchall 获取所有行数据
# fetchone 获取第一行数据
# fetchmany(num) 获取前num行数据


one_name = ('蒲', '王', '李', '张', '杨', '易', '陈', '蒋', '梁')
one_lastname = ('文锋', '玉刚', '大东', '洁', '浩', '刚', '天天', '子龙', '果', '兰')

# 插入
sql = "insert into one (name)values('%s')"
data = (random.choice(one_name) + random.choice(one_lastname))
cursor.execute(sql % data)
mysql_connect.commit()
print('成功插入数据', cursor.rowcount, '条数据,ID为:', cursor.lastrowid)
