# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseNumpy.py
@Author     :wooght
@Date       :2024/3/15 18:26
@Content    :
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
    shape   tuple 返回维度元祖
    size    元素个数
    dtype   元素类型    int32
"""
print(arr.ndim, arr.shape, arr.size, arr.dtype)     # 2 (3, 5) 15 int32
echo("array()定义numpy数组对象")
arr = array([[1.1, 2.2], [3.3, 4.4]])
print(arr.ndim, arr.shape, arr.size, arr.dtype)     # 2 (2, 2) 4 float64
arr = array([[1,2],[3,4]], dtype=int16)      # 定义数据类型 dtype
print(arr)
print(arr.dtype)                                    # int16

echo("numpy的random和原生random用法相识")
print(random.randn(10))                             # 随机正态分布数组
# [ 0.55402747 -0.03356931 -0.49272335  0.00689967 -1.05794256  0.41512391
#   0.36155496 -0.47186917 -0.53020383 -0.80265128]
print(random.rand(10))                              # 随机0-1的数据数组
print(random.randint(1, 5))               # 给定范围的随机整数
print(random.random((2,3)))                         # random((维度))
# [[0.70050286 0.65787913 0.02066382]
#  [0.46570063 0.43273537 0.41394429]]

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

echo("arr.T 转轴")
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
print(arr)
print(arr.ndim)
arr_2 = arr.T
print(arr_2)
print(arr_2.ndim)

echo("numpy 的广播功能,矩阵运算")
"""
    广播功能;对位进行运算,
    低纬与高纬的每一行进行运算
"""
arr = array([[1, 2], [3, 4]])
print(arr + array([9, 10]))
# [[10 12]
#  [12 14]]

arr = arange(4)             # [0 1 2 3]
arr_2 = arange(4,8)         # [4 5 6 7]
print(arr + arr_2)          # [ 4  6  8 10]

arr = arange(1,4)           # [1 2 3]
print(arr**2)               # [1 4 9]
print(10*sin(arr))          # [8.41470985 9.09297427 1.41120008]

echo("矩阵相乘")
arr = arange(4).reshape(2, 2)
arr_2 = arange(4, 8).reshape(2, 2)
print(arr, arr_2)
# [[0 1]
#  [2 3]]
# [[4 5]
#  [6 7]]
print(arr * arr_2)          # 对位相乘
# [[ 0  5]
#  [12 21]]
print(arr.T * arr_2)        # 转换后,按照新的位置进行对位相乘
# [[ 0 10]
#  [ 6 21]]
arr = arange(6).reshape(2,3)
arr_2 = arange(6,12).reshape(2,3)
print(arr * arr_2)

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

def get_nums(x, y):
    return x**8+y
arr = fromfunction(get_nums, (3,3), dtype=int)
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