# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseVar.py
@Author     :wooght
@Date       :2024/3/3 15:11
"""

"""
固定命名习惯
变量  下划线
函数  大驼峰
属性/方法   下划线
文件目录 原名/小写
"""


"""
    变量赋值的方式
    字符串格式化赋值见BaseString.py文件
"""
# 直接赋值
var_1 = 1
print(var_1)
# 多个赋值
var_1, var_2 = 1, 2
print(var_1, var_2)
# 元祖/列表赋值 元素个数和前面变量个数一一对应即可
tuple_test = (3, 4)
var_1, var_2 = tuple_test
print(var_1, var_2)
var_1, var_2 = [1, 2]
print(var_1, var_2)

"""
    数据类型
    字符串 详细见BaseString.py文件
    整数
    浮点数
"""
str_1 = "123"
num_1 = 1
num_2 = 1.8
bool_1 = False
print(type(str_1))      # <class 'str'>
print(type(num_1))      # <class 'int'>
print(type(num_2))      # <class 'float'>
print(type(bool_1))     # <class 'bool'>
if "float" == type(num_2).__name__:
    print(f"{num_2} 是浮点数")
"""类型转换"""
new_num_2 = str(num_2)
print(type(new_num_2))  # <class 'str'>
new_str_1 = int(str_1)
print(type(new_str_1))  # <class 'int'>
new_num_1 = int(num_2)  # 直接舍去小数点后面的
print(type(new_num_1))  # <class 'int'>
print(new_num_1)        # 1
new_num_1 = float(new_str_1)
print(new_num_1)        # 123.0
"""字符串转列表"""
list_str_1 = list(str_1)
print(list_str_1)       # ['1', '2', '3']
for_str_1 = [item for item in str_1]
print(for_str_1)        # ['1', '2', '3']

"""
    基础运算
"""
str_1 = "abc"
str_2 = "def"
str_3 = str_1 + str_2
print(str_3)        # abcdef
num_1 = 123
try:
    print(str_1 + num_1)
except TypeError:
    print("字符串不能参与数学运算")        # 运行
    print(str_1+str(num_1))             # abc123
print(num_1 * 2)                        # 246
num_2 = 2
"""**幂运算"""
print(num_2**5)                         # 32
"""/ 除法, // 返回除法整数部分, % 整除余数(数学用语:取模)"""
num_3 = 16
print(num_3/3)                          # 5.333333333333333
print(num_3//3)                         # 5
print(num_3%9)                          # 7
list_10 = range(1, 12)
list_two = []
for i in list_10:
    if i % 2 == 0:
        list_two.append(i)
print(list_two)                         # [2, 4, 6, 8, 10]
"""python 没有++,-- 只有+=,-=,还有*=,/=,**=,//="""
num_1 = 2
num_2 = 3
num_2 += num_1
print(num_2)                            # 5
num_3 = 5
num_3 *= num_1
print(num_3)                            # 10
"""三元运算"""
num_1 = 2
num_2 = 3
num_3 = 4 if num_1*num_2 == 6 else 5
print(num_3)                            # 4


"""
    动态变量名/字符串当成变量名
"""
from wooght_tools.echo import echo
echo('动态变量名')
w = 888
class h:
    width = 123
    height = 321
def abc():
    print('abc')
words = ['w', 'h']
print(locals()['w'])                # locals() 寻找变量
print(locals()[words[0]])
print(vars()[words[1]].width)       # 将对象的属性和属性值以以字典方式返回
print(eval('w'))                    # 将字符串转换成表达式运算
eval('abc()')


"""
    global 全局变量
"""
echo('global 全局变量')
var_1 = 12


def abc():
    global var_1
    var_1 += 1


def bcd():
    try:
        var_1 += 1
    except UnboundLocalError:
        pass


print(var_1)
abc()
print(var_1)    # 13
bcd()
print(var_1)    # 13

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '整除', x, '商为:', n // x)
            break
    else:
        print(n, '是质数')
