# -*- coding: utf-8 -*-
#
# @method   : redis 基础
# @Time     : 2018/3/26
# @Author   : wooght
# @File     : index.py

import redis, random

print('11111')
# 连接方式
pool = redis.ConnectionPool(host='localhost', port=6379, db=0, socket_connect_timeout=2)  # 连接池
r = redis.Redis(connection_pool=pool)  #连接,指定连接池
allname = ['puwenfeng', 'wooght', 'PWF']
print(allname)

# String操作
r.set('wooght', random.choice(allname),ex=10)  # 默认不存在则创建,存在则修改
print('set ok')
# set(name, value, ex=None, px=None, nx=False, xx=False)
#      ex，过期时间（秒）
#      px，过期时间（毫秒）
#      nx，如果设置为True，则只有name不存在时，当前set操作才执行,同setnx(name, value)
#      xx，如果设置为True，则只有name存在时，当前set操作才执行'''
r.set('hc', 'honc', ex=10)
name = r.get('wooght').decode('utf8')
print(name)
print(r.mget('wooght','hc'))  # 批量获取
print(r.strlen('wooght'))  # 返回字节长度
print(r.incr('N'))  # 自增  decr 自减
r.incr('N')
print(r.get('N'))
print(r.append('wooght', '-ABC'))  # 追加内容,返回长度
print(r.get('wooght'))

# Hash 操作
r.hset('arr', 'one', '111')  # hset(名称,键,值)
r.hset('arr', 'two', '222')
print(r.hget('arr', 'one'))  # 获取对应键
print(r.hgetall('arr'))  # 全部获取

arr = {'a':1, 'b':2, 'c':3}
r.hmset('arr2', arr)  # 批量设置
print(r.hget('arr2', 'b'))

keys = {'a', 'b'}
print(r.hmget('arr2', keys))  # 批量获取键值

print(r.hlen('arr2'))  # 获取长度
print(r.hkeys('arr2'))  # 获取所有key
print(r.hvals('arr2'))  # 获取所有value
print(r.hexists('arr2', 'd'))  # 检查是否存在
print(r.hdel('arr2', 'b'))  # 删除指定key键值对

# List 操作
r.lpush('list_one', {'a':11, 'b':22})
r.lpush('list_one', [1, 2, 3])  # 在最左侧添加元素
r.rpush('list_one', [4, 5, 6])  # 在最右侧添加元素
print(r.lindex('list_one', 3))  # 根据索引查找
print(r.lrange('list_one', 0, -1))  # 切片是查找