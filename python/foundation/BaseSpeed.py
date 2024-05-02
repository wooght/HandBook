# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseSpeed.py
@Author     :wooght
@Date       :2024/3/7 17:35
"""
from time import time

import pymysql as my

from python.wooght_tools.SecretCode import Wst

mysqlconfig = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': Wst.decryption("}a,>aN4|Y,9xODC0HUwq%.*T7<]+7}B>{A$>x"),
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
forms_iterable = cursor.fetchmany(1000)
linkmart_forms = []
for row in forms_iterable:
    linkmart_forms.append(row)
iter_forms = iter(linkmart_forms)

s_time = time()
for item in linkmart_forms:
    if item[0] > 800888:
        print(item[0], end=" ")
spend_time = time() - s_time
print("")
print(spend_time)

s_time = time()
for item in iter_forms:
    if item[0] > 800888:
        print(item[0], end=" ")
print("")
spend_time = time()-s_time
print(spend_time)

def get_gen():
    for item in linkmart_forms:
        yield item

s_time = time()
forms_list = get_gen()
for item in forms_list:
    if item[0] > 800888:
        print(item[0], end=" ")
print("")
spend_time = time()- s_time
print(spend_time)