# -*- coding: utf-8 -*-
#
# @method   : redis 基础
# @Time     : 2018/3/26
# @Author   : wooght
# @File     : index.py

import random
import redis

"""连接"""
# host 服务器地址,port端口, db数据库序号,socket_connect_timeout连接超时时间
pool = redis.ConnectionPool(host='192.168.101.103', port=6379, db=0, socket_connect_timeout=2)
r = redis.Redis(connection_pool=pool)  # 连接,指定连接池

"""String操作"""
allname = ['wooght', 'pwf']
r.set('wooght', random.choice(allname), ex=10)  # 默认不存在则创建,存在则修改
print('set ok')
# set(name, value, ex=None, px=None, nx=False, xx=False)
#      ex，过期时间（秒）
#      px，过期时间（毫秒）
#      nx，如果设置为True，则只有name不存在时，当前set操作才执行,同setnx(name, value)
#      xx，如果设置为True，则只有name存在时，当前set操作才执行'''
r.set('hc', 'honc', ex=10)
name = r.get('wooght').decode('utf8')
print(name)
print(r.mget('wooght', 'hc'))  # 批量获取
print(r.strlen('wooght'))  # 返回字节长度
print(r.incr('N'))  # 自增  decr 自减
r.incr('N')
print(r.get('N'))
print(r.append('wooght', '-ABC'))  # 追加内容,返回长度
print(r.get('wooght'))

"""Hash 操作"""
r.hset('arr', 'one', '111')  # hset(名称,键,值)
r.hset('arr', 'two', '222')
print(r.hget('arr', 'one'))  # 获取对应键
print(r.hgetall('arr'))  # 全部获取
keys = ['a', 'b']
print(r.hmget('arr2', keys))  # 批量获取键值
print(r.hlen('arr2'))  # 获取长度
print(r.hkeys('arr2'))  # 获取所有key
print(r.hvals('arr2'))  # 获取所有value
print(r.hexists('arr2', 'd'))  # 检查是否存在
print(r.hdel('arr2', 'b'))  # 删除指定key键值对

"""List 操作"""
r.lpush('list_one', *[11, 22, 33])
r.lpush('list_one', *[1, 2, 3])  # 在最左侧添加元素
r.rpush('list_one', *[4, 5, 6])  # 在最右侧添加元素
print(r.lindex('list_one', 3))  # 根据索引查找
print(r.lrange('list_one', 0, -1))  # 切片是查找

"""无序集合"""
print('集合添加成功{}个'.format(r.sadd('test_ips', *['123', '321', '555'])))  # 设置集合
print(r.smembers('test_ips'))  # 获取集合
r.sadd('test_ips', *[111, 456, 7788])
print([val for val in r.srandmember('test_ips', 3)])  # 随机选择
print('是否存在:{}'.format('存在' if r.sismember('test_ips', '123') else '不存在'))  # 判断是否存在
print('是否存储成功:{}'.format('成功' if r.sadd('test_ips', '123') else '已经存在,不成功'))
print('集合元素个数{}'.format(r.scard('test_ips')))

"""删除键"""
all_keys = r.keys('8*')
print(len(all_keys))
for key in all_keys:
    r.delete(key)
