# -*- coding: UTF-8 -*-
# python 函数库
# by wooght
# date 2017-11
import io
import os
import re
import sys
from math import log, exp

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')  # 改变标准输出的默认编码

# strip 去掉字符串首尾特定字符
str = ' dslfjdsl '
print(str.strip())  # 去掉空额
str = '00jdsfldj00'
print(str.strip('0'))  # 指定去掉什么内容

# filter 过滤掉不符合条件的元素
a = range(1, 10)
new_list = filter(lambda x: x > 5, a)
for i in new_list:
    print(i)


def is_not_empty(s):
    return s and len(s.strip()) > 0


new_list = filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
for i in new_list:
    print(i)

# map 接受可迭代的序列,返回规定规则的集合
new_list = map(lambda x: x[1], [('a', 1), ('b', 2)])
for i in new_list:
    print(i, '-map')
new_list = map(lambda x, y: x * y, [4, 5, 6], [1, 2, 3])
for i in new_list:
    print(i, '--map')
new_tuple = map(tuple, 'abcde')
new_list = list(new_tuple)
print(new_list)  # map应用,将字符串转换成元祖,并以列表返回

# zip 列表组合 相同位置的组合成元祖
new_list = zip([1, 2, 3], [4, 5, 6])
print(list(new_list))

# marshal 对象序列化和反序列化
# d = marshal.load(open(fname, 'rb'))
# marshal.dump(d, open(fname, 'wb'))
# d = marshal.loads(f.read())

# exp方法返回x的指数,ex
print(exp(-10))
# log 方法返回x的对数log(e,x)
print(log(0.4))

# 正则表达式 split截取字符串
re_zh = re.compile('[,!?]')
sent = "大家好,我是wooght,很高兴认识大家!你们高兴吗?"
new_str = re_zh.split(sent)
del new_str[-1]
print(new_str)

# __file__ ,os.path应用
dir = __file__.split('\\');
print(__package__);
print(dir);
del dir[-2:]
path = '/'.join(dir)
print(path)
print(os.path.dirname(__file__))
data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tag.marshal')
print(data_path, '-')

a = {'one': 1, 'two': 2}
for i in a.items():
    print(i)

a = [('你', 1), ('好', 2), ('他', 3)]
b = []
c = []
for k, v in a:
    b.append(k)
    c.append(v)
print(b, c)
