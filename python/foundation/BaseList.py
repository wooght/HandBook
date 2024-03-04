# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseList.py
@Author     :wooght
@Date       :2024/3/3 14:49
"""

"""
    list 列表
    test_list = [] 列表里面可以是任意元素,整数,浮点数,字符串,字典,元祖,列表,对象等都可以
    索引是在边界上的
    0    1   2   3   4   
    _____ ___ ___ ___ ___
    ["0", "1","2","3","4"]
    ----- --- --- --- ---
    -5  -4  -3  -2  -1
    所以切片的时候,都不包括后边界
"""
test_list = [1, 2, 'three']
print(test_list[2])  # three
test_list[1] = [3, 2, 1]
print(test_list[1][1])  # 2
test_list = [1, 2, 3, 4, 5]
"""列表切片"""
print(test_list[:2])  # [1, 2]
print(test_list[-2:])  # [4, 5]
print(test_list[1:3])  # [2, 3]
"""切片赋值"""
test_list[1:3] = ['a', 'b']
print(test_list)  # [1, 'a', 'b', 4, 5]
"""list.reverse() 翻转列表"""
list_1 = [1, 2, 3]
list_1.reverse()
print(list_1)               # [3, 2, 1]
"""字符串快速转变为列表"""
str_1 = "你好吗"
str_list = [item for item in str_1]
print(str_list)             # ['你', '好', '吗']
print(list(str_1))          # ['你', '好', '吗']

"""
    tuple 元祖
    test_tuple = () 特性和list几乎一样,唯一不同是tuple不能修改内容
"""
test_tuple = (1, 2, [3, 4], 'hello')
print(test_tuple)
try:
    test_tuple[1] = 'a'
except TypeError:
    print('元祖不能被修改')
# 其他操作和列表一样
print(test_tuple[1])        # 2
print(test_tuple[:2])       # (1, 2)
test_tuple[2][1] = 'b'
print(test_tuple)           # (1, 2, [3, 'b'], 'hello')
"""字符串转元祖"""
str_1 = "abc"
print(tuple(str_1))         # ('a', 'b', 'c')

"""
    列表,元祖同时给多个变量赋值
"""
num_a, num_b = ('a', 'b')
print(num_a, num_b)         # a b
num_1, num_2 = [1, 2]
print(num_1, num_2)         # 1 2
test_tuple = (1, 2, 3)
new_message = "我有{}个苹果,{}个桃子,{}个西瓜".format(*test_tuple)
print(new_message)          # 我有1个苹果,2个桃子,3个西瓜



"""
    dictionary  字典
    test_dict = {}  存放 键值对 数据
    键必须是数字或字符串,并且唯一
    值可以是任意元素
"""
test_dic = {
    'name': 'wooght',
    "age": 36
}
print(test_dic['name'])     # wooght
test_dict = {
    'wooght': {"name": "wooght", "level": 10},
    'zhangs': {"name": "zhangs", "level": 18}
}
print(test_dict['zhangs']['level'])     # 18
test_dict['wooght']['name'] = 'pwf'
print(test_dict['wooght']['name'])      # pwf

"""
    dict.pop(key)   删除列表/字典中的元素
    pop返回值为删除元素的内容,但不包括key
    del dict[key]   删除列表/字典中的元素
    dict.clear()    清空列表/字典
    list.append()   向列表末尾追加元素
"""
return_val = test_dict.pop('zhangs')
print(test_dict)                        # {'wooght': {'name': 'pwf', 'level': 10}}
print(return_val)                       # {'name': 'zhangs', 'level': 18}
del test_dict['wooght']
print(test_dict)                        # {}
"""pop 和 del 在列表中的方法和字典中的一样"""
test_list = [1, 2, 3]
del test_list[2]
print(test_list)                        # [1, 2]
test_list.pop(0)
print(test_list)                        # [2]
test_list.clear()
print(test_list)                        # []
"""list.append() 向列表追加元素,末尾追加"""
test_list.append(5)
print(test_list)                        # [5]
test_list.append([1, 2])
print(test_list)                        # [5, [1, 2]]


"""
    字典 键,值的操作
    dict.keys(),dict.values(),dict.items()
"""
test_dic = {"one": 1, "two": 2}
keys = test_dic.keys()
print(keys)                 # dict_keys(['one', 'two']) keys()为一个对象
print(type(keys))           # <class 'dict_keys'>
print(len(test_dic))        # 2
for key in test_dic.keys():
    print(key)                          # one  /n  two
if "one" in test_dic:
    print("one is in dict")             # 运行
if "one" in test_dic.keys():
    print("the key one in dict")        # 运行
if 1 in test_dic.values():
    print("the value 1 in dict")        # 运行
for key, value in test_dic.items():
    print(key, ":", value)              # one: 1 /n two: 2
test_dic.clear()
print(test_dic)                         # {}