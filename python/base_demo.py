# -*- coding: utf-8 -*-
#
# @method   : python基础习题
# @Time     : 2018/5/15
# @Author   : wooght
# @File     : base_demo.py

s = ['1', '2', '3']
str = list(s)
s.append('4')
print(s, str)

all_zuhe = []


# 输出列表的所有组合的方法
# 列表复制，=是创建了一个应用，修改都会同时修改 list()和切片方法可以实现真正的复制
def zuhe(s):
    for key in s:
        if key not in all_zuhe:
            all_zuhe.append(key)
            zuhe_tmp = list(all_zuhe)
            for zh in zuhe_tmp:
                if zh != key:
                    all_zuhe.append(zh + key)


zuhe('abcd')
print(all_zuhe)

# 原生排序
str = [1, 2, 3, 4]
str.reverse()  # 倒序排列
print(str)
print(sorted(str, reverse=True))  # 排序，reverse=True 倒序

# 冒泡排序
dataset = [3, 6, 7, 1, 4, 0, 9, 8, 2, 5]
length = len(dataset)
for i in range(length):
    for j in range(i + 1, length):
        # range(start,stop)可以指定开始和结算，如值传递一个，则0开始
        if dataset[j] > dataset[i]:
            tmp = dataset[j]
            dataset[j] = dataset[i]
            dataset[i] = tmp

print(dataset)

# 快速排序法
# 列表合并 直接用 + 即可
dataset = [3, 5, 1, 7, 9, 0, 2, 4, 6, 8]


def quick_sort(arr):
    if len(arr) == 0:
        return []
    left_arr = []
    right_arr = []
    center_arr = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < center_arr:
            left_arr.append(arr[i])
        else:
            right_arr.append(arr[i])
    return quick_sort(left_arr) + [center_arr] + quick_sort(right_arr)


print(quick_sort(dataset))

# 上传文件类型字典
file_type = {
    'turnover': '营业数据',
    'order': '订单数据',
    'goods': '商品数据'
}
print(file_type)
file_t = file_type
print(file_t)
for i, n in file_t.items():
    print(i, ':', n)

import calendar

cal = calendar.month(2019, 12)
for i in cal:
    print('2019-12', i)

import pandas as pd
import time

w = pd.date_range(start='2019-11-17', end='2019-12-15')
a = list(w.date)
s = {}
for i in a:
    s[i.strftime('%Y-%m-%d')] = 1

print(s)

print(time.strftime('%Y-%m-%d', time.localtime(time.time() - 3600 * 24 * 60)))


def one_day_date(one=0):
    date_code = '%Y-%m-%d'
    day = 3600 * 24
    if not one:
        return time.strftime(date_code, time.localtime()), time.time()/day
    else:
        one_day_time = time.time() - one*day
        return time.strftime(date_code, time.localtime(one_day_time)), one_day_time/day

import math
cha_time = one_day_date()[1] - one_day_date(180)[1]
print(math.ceil(cha_time), '天')

a_dict = {
    '2019-12-12' : 1,
    '2019-12-11' : 1,
    '2018-12-12' : 1
}
item = a_dict.items()
print(item)
min_item = min(item)[0]
print(min_item)

print(one_day_date()[0])
print(pd.to_datetime(one_day_date()[0]))


# 字典应用
print('---------------------------------字典应用')
b_dict = {'a': [1, 2, 3], 'b': [3, 4, 6], 'c': '123321'}
print('单个变量，指获取字典中的可以')
for i in b_dict:
    print(i)
print('keys()')
for i in b_dict.keys():
    print(i)
print('values()')
for i in b_dict.values():
    print(i)
print('items()')
for i, n in b_dict.items():
    print(i, n)

str = 'c'
if str not in b_dict.keys():
    print('a not in b_dict.keys')
else:
    print('a in b_dict.keys')
    print(b_dict[str])

date_str = '2019-12-23'
pd_date = pd.to_datetime(date_str)
print(pd_date.weekday())

arr = ['haha','hehe','heihei']
str = 'ha'

if str not in arr:
    print('not')
else:
    print('yes')