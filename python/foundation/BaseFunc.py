# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseFunc.py
@Author     :wooght
@Date       :2024/3/7 15:50
"""
import random

"""
    函数变量
    global 函数访问全局变量
"""
var_1 = 10
def get_global():
    """
        global 全局变量
    """
    global var_1
    var_1 += 1
    print('var_1通过global引进变为全局变量', var_1)
def get_var():
    print('未声明的变量,函数内部可以调用', var_1)
def update_var():
    try:
        var_1 += 1
        print(var_1)
    except UnboundLocalError:
        print('函数内部没有用global引入的变量,只可访问,不可修改')


get_global()
get_var()
update_var()


"""
    *args 不定长度变量
    **args[] 不定长度关键词变量
    * 在函数定义处,为打包,将无键参数打包为一个列表
    * 在函数调用处,为解报,将列表罗列为一个一个的元素
    ** 在函数定义处,为打包,将有键值对的参数打包为一个字典
    ** 在函数调用处,为解包,将字典以键值的方式罗列成一对一对的元素
"""
class A:
    def __init__(self):
        print('默认运行')
        self.keywords = 'A'

    def __repr__(self):
        return "类说明"

    def __str__(self):
        return "类str说明"

    def get_sum(self, *args):
        """     不定长度参数        """
        result_sum = 0
        for num in args:
            result_sum += num
        return result_sum

    def get_area(self, **kwargs):
        """ **kwargs 不定长关键词参数 """
        if 'sd' in kwargs.keys():
            return (kwargs['sd']+kwargs['xd'])*kwargs['g']/2
        elif 'd' in kwargs.keys():
            return kwargs['d']*kwargs['g']/2
        else:
            return kwargs['c'] * kwargs['g']

    def get_address(self, *floor, **builds):
        for key,value in builds.items():
            for unit in range(1,value+1):
                print(f'{key}栋{unit}单元有{floor[0]}层{floor[1]}户')

    def get_keywords(self, is_print=True):
        """参数的默认值 argument default"""
        print(self.keywords) if is_print else print('请下查看指令')

    def get_print_word(self, name, city, age):
        print("she name's", name, "come from ", city, age, "old")


new_a = A()
print(new_a)

"""不定长参数 * 的逆应用"""
print(new_a.get_sum(1, 2, 3))                      # 6
print(new_a.get_sum(1, 3, 5, 7))                   # 16
"""不定长关键词参数 ** 的逆应用"""
print(new_a.get_area(d=11, g=12))                        # 66.0
print(new_a.get_area(sd=10, xd=5, g=2))                  # 15.0
new_a.get_address(6, 5, one=2, two=4)
# one栋1单元有6层5户
# one栋2单元有6层5户
# two栋1单元有6层5户
# two栋2单元有6层5户
# two栋3单元有6层5户
# two栋4单元有6层5户
"""
    多个参数传递方式
    一:  对应位置一一传递
    二:  *列表对应位置一一传递
    三:  **字典传递
"""
zs_data = {'name': "张三", "city": "成都", "age": 32}
new_a.get_print_word(**zs_data)                         # she name's 张三 come from  成都 32 old
new_a.get_print_word("李四","上海", 32)   # she name's 李四 come from  上海 32 old
wmz_data = ('王麻子', '上海', 33)                         # she name's 王麻子 come from  上海 33 old
new_a.get_print_word(*wmz_data)
new_a.get_keywords(is_print=False)                       # 请下查看指令
new_a.get_keywords()                                     # A

"""
    lampda表达式  匿名函数
    lambda 参数:返回值
"""
func = lambda x: x ** 2
print('函数运行结果:', func(2))                               # 函数运行结果: 4
test_list = range(10)
# filter 过滤器,返回一个迭代器
print(list(filter(lambda x: x % 2 == 0, test_list)))        # [0, 2, 4, 6, 8]
arr = [x for x in range(10) if x % 2 == 0]
print(arr)                                                  # [0, 2, 4, 6, 8]
new_arr = arr[::-1]
print(new_arr)                                              # [8, 6, 4, 2, 0]
arr = [
    [1, 2, 3],
    [1, 2, 0],
    [3, 2, 1]
]
arr.sort(key=lambda x:x[2], reverse=False)                  # 以每一行的第二列进行排序
print(arr)                                                  # [[1, 2, 0], [3, 2, 1], [1, 2, 3]]

"""
    递归函数
    递归三定律:
        一:有结束条件
        二:算法能向结束条件靠近
        三:必须调用自身
    实例:列表求和
        进制转换
"""

def sum_list(nums):
    """
    递归求和
    """
    if len(nums) == 1:
        return nums[0]
    else:
        results = nums[0] + sum_list(nums[1:])
    return results


test_list = range(random.randint(1, 100))
print(sum_list(test_list))
contrast_str = '0123456789ABCDEF'       # 进制对照表
def hex_convert(nums, hex_num):
    """
    递归进制类型转换
    nums 要被转换的10进制数
    hex_num目的进制数,二,八,十六进制
    """
    return contrast_str[nums] if nums < hex_num else hex_convert(nums // hex_num, hex_num) + contrast_str[nums % hex_num]


print(hex_convert(88, 2))       # 1011000
