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
"""列表切片 [start,end,step]"""
print(test_list[:2])  # [1, 2]
print(test_list[-2:])  # [4, 5]
print(test_list[1:3])  # [2, 3]
sl = slice(1,4,2)
print(test_list[sl])    # [2, 4]
print(test_list[1:4:2]) # [2, 4]
print(test_list[::-1])  # [5, 4, 3, 2, 1]   倒序
"""切片赋值"""
test_list[1:3] = ['a', 'b']
print(test_list)  # [1, 'a', 'b', 4, 5]
"""list.reverse() 翻转列表"""
list_1 = [1, 2, 3]
list_1.reverse()            # [::-1] 相同
print(list_1)               # [3, 2, 1]
"""list(var) 将var转变为列表对象"""
str_1 = "你好吗"
print(list(str_1))          # ['你', '好', '吗']
"""列表合并 list.extend(list),在原来的列表上追加"""
list_1 = [1, 2, 3, 4]
list_2 = [2, 3, 4]
print(list_1+list_2)        # [1, 2, 3, 4, 2, 3, 4]
list_1.extend(list_2)       # extend 直接追加,会改变原来的列表而不是创建新的列表
print(list_1)               # [1, 2, 3, 4, 2, 3, 4]
"""list.append() 向列表追加元素,末尾追加"""
test_list.append(5)
print(test_list)                        # [1, 'a', 'b', 4, 5, 5]
test_list.append([1, 2])
print(test_list)                        # [1, 'a', 'b', 4, 5, 5, [1, 2]]
"""list.insert(index,var) 在列表下标index后面插入var元素"""
test_list.insert(1, 'hello')
print(test_list)                        # [1, 'hello', 'a', 'b', 4, 5, 5, [1, 2]]
"""list.remove(x) 删除列表中元素值为x的项目,如果没有则报ValueError错"""
test_list.remove('a')
print(test_list)                        # [1, 'hello', 'b', 4, 5, 5, [1, 2]]
"""list.pop(key) 删除列表中的元素,无key则删除最后一项"""
test_list = [1, 2, 3, 4]
print(test_list.pop())      # 4
print(test_list)            # [1, 2, 3]
"""all(list) 全真判断,及判断列表中是否有0,空,None,False等非真的元素,如果都为真,则返回True"""
print(all([1, 2, '3', True]))  # True
print(all([1, 0, 3]))  # False
print(all([1, '', 3]))  # False
print('' in [1, '', 3])  # True
"""any(list) 有一个是True,就返回True"""
print(any(['', 2, None]))       # True



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
# 访问及切片操作和列表一样
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
"""dict.pop(key)   删除列表/字典中的元素"""
return_val = test_dict.pop('zhangs')
print(test_dict)                        # {'wooght': {'name': 'pwf', 'level': 10}}
print(return_val)                       # {'name': 'zhangs', 'level': 18} pop返回值为删除元素的内容,但不包括key
"""del dict[key]   删除列表/字典中的元素"""
del test_dict['wooght']
print(test_dict)                        # {}
"""pop 和 del 在列表中的方法和字典中的一样"""
test_list = [1, 2, 3]
del test_list[2]
print(test_list)                        # [1, 2]
test_list.pop(0)
print(test_list)                        # [2]
"""dict.clear() 清空列表/字典"""
test_list.clear()
print(test_list)                        # []
"""dict.update(dict) 融合字典"""
dict_one = {"one": 1, "two": 2, "three": 3}
dict_two = {"four": 3, "five": 5}
dict_one.update(dict_two)
print(dict_one)                         # # {'one': 1, 'two': 2, 'three': 3, 'four': 3, 'five': 5}
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



"""
    set 集合
    {}表示集合,和字典不一样的是只有key,没有value
    集合无序(故不能通过下标访问),无重复
"""
test_set = {1, 2, 3, 1}
print(test_set)         # {1, 2, 3} 自动去除了重复项
"""集合去重"""
vip_1 = ['zs', 'ls', 'wmz']
vip_2 = ['zs', 'fg', 'yf']
vip_list = vip_1+vip_2
vip_set = set(vip_list)     # set(元祖/列表/字典) 直接转换为集合
print(vip_set)              # {'zs', 'wmz', 'fg', 'yf', 'ls'}
"""add()添加元素"""
test_set = set()
test_set.add('张三')
print(test_set)                     # {'张三'}
"""update()添加多个元素"""
test_set.update(['李四', '王麻子'])
print(test_set)                     # {'张三', '李四', '王麻子'}
"""remove()删除元素"""
test_set.remove('李四')
print(test_set)                     # {'王麻子', '张三'}
"""pop() 随机删除元素"""
test_set.pop()
print(test_set)
"""discard()删除元素,如果元素不存在不报错"""
test_set.discard('李四')
print(test_set)
""" & 集合的交集, | 并集, - 差集, ^ 对称差集"""
num_set_1 = {1, 3, 5, 7}
num_set_2 = {1, 4, 5, 7}
print(num_set_1 & num_set_2)            # {1, 5, 7}
print(num_set_2 | num_set_1)            # {1, 3, 4, 5, 7}
print(num_set_1 - num_set_2)            # {3}
print(num_set_2 - num_set_1)            # {4}   - 差集,只在前者中,不在后者中
print(num_set_1 ^ num_set_2)            # {3, 4}    ^ 只出现在集合1或者集合2中,不能同时出现  并集-交集=对称差集



"""
    推导式
    列表,字典,集合可用推导式简洁创建
"""
""" 常规创建列表 """
test_list = []
for num in range(10):
    test_list.append(num)
print(test_list)                # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
""" 列表推导式创建 """
test_list = [item for item in range(10)]
print(test_list)                # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print([item for item in range(10) if item % 2 == 0])  # 输出偶数 [0, 2, 4, 6, 8]
# 分别求出1,2,3的2,3次方   for嵌套推导式
print([(a, a**b) for a in range(1, 4) for b in range(2, 4)])        # [(1, 1), (1, 1), (2, 4), (2, 8), (3, 9), (3, 27)]
cfb = [[f"{a}*{b}=" + str(a * b).rjust(2) for a in range(1, 10) if b >= a] for b in range(1, 10)]
for item in cfb:
    print(item)
# ['1*1= 1']
# ['1*2= 2', '2*2= 4']
# ['1*3= 3', '2*3= 6', '3*3= 9']
# ['1*4= 4', '2*4= 8', '3*4=12', '4*4=16']
# ['1*5= 5', '2*5=10', '3*5=15', '4*5=20', '5*5=25']
# ['1*6= 6', '2*6=12', '3*6=18', '4*6=24', '5*6=30', '6*6=36']
# ['1*7= 7', '2*7=14', '3*7=21', '4*7=28', '5*7=35', '6*7=42', '7*7=49']
# ['1*8= 8', '2*8=16', '3*8=24', '4*8=32', '5*8=40', '6*8=48', '7*8=56', '8*8=64']
# ['1*9= 9', '2*9=18', '3*9=27', '4*9=36', '5*9=45', '6*9=54', '7*9=63', '8*9=72', '9*9=81']
""" 字典推导式创建字典 """
person_list = [("张三", 33), ("李四", 30), ("王麻子", 28)]
print({key: value for key, value in person_list})       # {'张三': 33, '李四': 30, '王麻子': 28}
print({key: value for key in ['张三', '李四', '王麻子'] for value in range(30, 33)})       # {'张三': 32, '李四': 32, '王麻子': 32} 因为key是唯一的,所以都是32岁
""" 元祖推导式会变成一个生成器 """
test_tuple = (item for item in range(10))
print(test_tuple)               # <generator object <genexpr> at 0x0000021525235480>
print(test_tuple.__next__())    # 0
