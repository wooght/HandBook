# -*- coding: utf-8 -*-
#
# @method   : python list,tuple,dict
# @Time     : 2017/11/17
# @Author   : wooght
# @File     : base_array.py
# 词条:reverse [rɪˈvɜ:s] 颠倒

import random
from math import *
from echo import f

f('基础方法')
n = random.randrange(1, 5)
print(n)
n = random.random()
print(n)
print(floor(10 * n))
print(ceil(10 * n))
print(round(10 * n))
n = random.randint(1, 9)
print(n)

f('元祖tuple')
arr = (1, 4, 2, 7)
print(sorted(arr, reverse=True))  # reverse 颠倒
print(arr[1])  # tuple不能重新赋值

f('list 列表')
arr = [5, 3, 8, 9, 1, 4, 2]
print(arr)
print(sorted(arr))
arr[1] = 100
print(arr)
print(arr[:2])
print(arr[:4:2])  # 每隔2个元素取值
arr2 = arr
arr2[:4:2] = [88, 99]
print(arr)
print('choice:', random.choice(arr))  # 随机取值
print('100 index:', arr.index(100))  # 值的索引
arr.append(77)  # 追加新元素
print(arr)
print(len(arr))
arr.insert(1, 1010)  # 插入新元素
print(arr)
arr.pop(-1)
print(arr)

sl = slice(1, 5, 2)
print(arr[sl])  # 等同于 arr[1:5:2]

arr = [
    [1, 2, 3],
    [4, 7, 6]
]
print(arr)
print(arr[1][-1])
print(sorted(arr[1]))
for i in arr:
    print(i)
print(4 in arr[1])


f('dict 字典')
arr = {9, 3, 8, 1}
print(arr)
print(sorted(arr, reverse=True))  # sorted 排序返回list
arr = {
    'a3': 3,
    'a2': 2,
    'a1': 1,
    'a4': -5
}
# 字典元素的迭代
for key, i in arr.items():
    print(key, i)
print(arr)
print(arr['a4'])
print(sorted(arr))  # 对索引进行排序
print(sorted(arr.items()))  # items 键值对 键排序
print(sorted(arr.keys()))  # 对索引进行排序
print(sorted(arr.items(), key=lambda d: d[1], reverse=False))  # items 键值对 值排序
print(list(arr.values()))  # values 组成的列表
for i in arr.values():
    print(i)

for i in arr.keys():
    print(i)

for i in arr:
    print(i)

for i in arr.items():
    print(i)

print(-5 in arr)
print(-5 in arr.values())
print('a2' in arr)
print(arr.get('a4'))
del arr['a1']
print(arr)
arr.pop('a2')  # 删除指定的key对应的元素
print(arr)
arr['a2'] = 101
print(arr)

f('enumerate')
arr = [1, 2, 3, 4]
for i in arr:
    print(i)

# enumerate 将列表元素分解成 下标,值
for i, n in enumerate(arr):
    print('索引/下标:', i, ',对应值:', n)


f('zip')
a = [1, 2, 3]
b = [2, 3, 4]
arr = zip(a, b)  # 将对应的元素打包成元祖,并将这些元祖组成列表
for i, j in arr:
    print(i, j)


f('list set')
arr = [1, 2, 3, 1, 2]
print(set(arr))  # set 提取列表不重复元素组成dict(字典)


f('dict |(字典合并)')
arr1 = {1, 2, 3}
arr2 = {3, 4}
print(arr1 | arr2)  # 将字典合并,要求字典格式相同

f(' * 创建多元素列表')
arr = [0] * 10
print(arr)  # arr为10个元素的列表
arr = [[0, 0]] * 10
print(arr)
