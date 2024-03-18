# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseNumpy.py
@Author     :wooght
@Date       :2024/3/15 18:26
@Content    :Numpy 基础
"""
from numpy import *
from wooght_tools.echo import echo

"""
    numpy数组中的元素必须是同数据类型
    array()定义ndarray数组
"""
echo('arange(),linspace()创建等差数列对象')
arr = arange(0,15,2)                        # 类似 range()    整数
print(arr)                                  # [ 0  2  4  6  8 10 12 14]
print(type(arr).__name__)                   # ndarray
arr = linspace(0, 3, 5)     # linspace() 包括前后边界, 输出的为浮点数
print(arr)                                  # [0.   0.75 1.5  2.25 3.  ]
"""reshape指定维度"""
arr = arange(15).reshape(3,5)               # 三行五列  这里是二维,及2D numpy数组
print(arr)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]]
"""
    ndim    int 数组轴(axis)的个数,及维度
    shape   tuple 返回维度元祖(x,y)
    size    元素个数
    dtype   元素类型    int32
"""
print(arr.ndim, arr.shape, arr.size, arr.dtype)         # 2 (3, 5) 15 int32
echo("array()定义numpy数组对象")
arr = array([[1.1, 2.2], [3.3, 4.4]])
print(arr.ndim, arr.shape[0], arr.size, arr.dtype)       # 2 2 4 float64
arr = array([[1,2],[3,4]], dtype=int16)           # 定义数据类型 dtype
print(arr)
print(arr.dtype)                                    # int16

echo("快速定义矩阵")
print(zeros(5))                     # [0. 0. 0. 0. 0.]
print(zeros((2,3)))
# [[0. 0. 0.]
#  [0. 0. 0.]]
print(ones((2,3,4)))
# [[[1. 1. 1. 1.]
#   [1. 1. 1. 1.]
#   [1. 1. 1. 1.]]
#
#  [[1. 1. 1. 1.]
#   [1. 1. 1. 1.]
#   [1. 1. 1. 1.]]]
print(eye(3))                       # 单位矩阵
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

echo("arr.T 转轴 transpose 转置")
"""
    转轴不会改变轴的数量,而是改变轴的方向
    如有如下数据:
    姓名  苹果  香蕉  西瓜
    张三  1    2     3
    李四  4    5     6 
    转轴后如下:
    姓名  张三  李四
    苹果  1    4
    香蕉  2    5
    西瓜  3    6
"""
arr = array([[1, 2, 3], [4, 5, 6]])
# [[1 2 3]
#  [4 5 6]]
print(arr.ndim)                 # 2
arr_2 = arr.T
# [[1 4]
#  [2 5]
#  [3 6]]
print(arr_2.ndim)               # 2
new_arr = transpose(arr_2)
print(new_arr)
# [[1 2 3]
#  [4 5 6]]


echo("比较运算")
arr = random.random((2,2))
print(arr)
arr_bool = arr < 0.3
print(arr_bool)
# [[False  True]
#  [False False]]
arr_2 = random.random((2,2))
print(arr>arr_2)
# [[ True  True]
#  [False False]]
arr = arange(15).reshape(3,5)
print(arr)
new_arr = arr[arr>5]            # 取出大于5的元素,返回一个一维数组
print(new_arr)                  # [ 6  7  8  9 10 11 12 13 14]

echo("索引,切片,赋值")
"""切片与原生相同"""
arr = arange(5) ** 2
print(arr, arr[3], arr[:2])     # [ 0  1  4  9 16] 9 [0 1]
arr[3:] = 100                   # 集体赋值
print(arr)                      # [  0   1   4 100 100]
print(arr[::-1])                # [100 100   4   1   0]
arr.sort()
print(arr)                      # [  0   1   4 100 100]

arr = arange(10).reshape(5,2)
print(arr, arr[2], arr[2:4])
# [[0 1]
#  [2 3]
#  [4 5]
#  [6 7]
#  [8 9]]

#  [4 5]

#  [[4 5]
#  [6 7]]
arr[0] = 1
print(arr[0])           # [1 1]
arr[1] = [2, 2]
print(arr[1])           # [2 2]
print(arr[3][0])        # 6
arr[:, 1] = 0           # 所有行的第一列赋值为 0      清零操作
print(arr)
# [[1 0]
#  [2 0]
#  [4 0]
#  [6 0]
#  [8 0]]
def get_nums(x, y):
    """x为Numpy中的行,y为列"""
    return x**8+y
arr = fromfunction(get_nums, (3,3), dtype=int)      # 使用函数对numpy数组元素的行和列的索引做处理，得到当前元素的值，索引从0开始
print(arr)
# [[  0   1   2]
#  [  1   2   3]
#  [256 257 258]]
# arr[轴1,轴2]/ arr[x轴,y轴]/arr[行,列]
print(arr[1, 2])        # 3 输出第1行,第二列的值  x轴=2,y轴=2
print(arr[0:2, 1])      # [1 2] 输出第0行第一列的值,第1行第一列的值 x=0,1  y=1
print(arr[1:3, 0:2])
# [[  1   2]
#  [256 257]]
print(arr[:, 2])        # [  2   3 258]
for i in arr:
    print(i, type(i).__name__)
"""flat 遍历取出所有元素"""
for i in arr.flat:
    print(i*1.)         # 末尾*1.意为转换为Float

arr = fromfunction(function=(lambda x, y: x * y), shape=(3, 3), dtype=int)
print(arr)
# [[0 0 0]
#  [0 1 2]
#  [0 2 4]]