# -*- coding: utf-8 -*-
#
# @method   : numpy 基础
# @Time     : 2018/1/16
# @Author   : wooght
# @File     : numpy_a.py

from numpy import *

from python.w_math.echo import f

f('定义ndarray')
arr = arange(15)  # 定义一个列表 1D
print(arr, type(arr).__name__)
# reshape指定维度
arr = arange(15).reshape(3, 5)  # 定义3行,5列的二维数组2D
print(arr)
print(arr.ndim, arr.shape, arr.size, arr.dtype)
# ndim 数组轴(axis)的个数,几维数组
# shape 数组的维度(3,5)
# size 数组的元素个数
# dtype 数组的类型 int32
print(type(arr).__name__)  # ndarray

arr = array([1, 2, 3, 4])
print(arr, arr.dtype)
arr = array([[1, 2, 3], [4, 5, 6]], dtype=int16)
print(arr, arr.dtype, type(arr).__name__, arr.ndim)

arr = zeros((2, 3))
print(arr, arr.shape, arr.dtype)  # 默认是float64类型
arr = ones((2, 3, 4))  # 定义三维数组3D
print(arr, arr.ndim, arr.shape, arr.dtype)
# 得到3维数组 二维数组打印成矩阵,三维数组打印成矩阵列表
# [[[ 1.  1.  1.  1.]
#   [ 1.  1.  1.  1.]
#   [ 1.  1.  1.  1.]]
#
#  [[ 1.  1.  1.  1.]
#   [ 1.  1.  1.  1.]
#   [ 1.  1.  1.  1.]]]


f('数组的运算')
arr = arange(4)
arr2 = array([10, 20, 30, 40])
arr3 = arr2 - arr
print(arr3)  # [10 19 28 37]
print(arr ** 2)  # [0 1 4 9]
print(10 * sin(arr2))  # [-5.44021111  9.12945251 -9.88031624  7.4511316 ]

f('矩阵乘法')
# 乘法按元素进行
arr = arange(4).reshape(2, 2)
arr2 = array([[4, 5], [6, 7]])
print(arr * arr2)
print('转轴:', arr.T * arr2)
# 矩阵乘法 outer
print(outer(arr, arr2))


f('ones快速创建矩阵,linspace等差')
arr = ones((2, 3), dtype=int)
arr2 = random.random((2, 3))  # numpy.random 非python自带的random
print(arr, arr2)
arr2 += arr  # += 赋值 不会产生新的数组
print(arr2)

l1 = ones(3, dtype=int)
l2 = linspace(0, pi, 3)  # linspace 等差数列
print(l1, l2)
l3 = l1 + l2  # 类型为最接近的那个数组的类型
print(l3, l3.dtype)
a = exp(l3 * 1j)  # [ 0.54030231+0.84147098j -0.84147098+0.54030231j -0.54030231-0.84147098j]
print(a)
print(2 * 3j)

# 数组比较运算
arr = random.random((3, 3))
print(arr < 0.5)
arr = eye(2, 2)
print(arr == 1)


f('索引,切片,迭代')
arr = arange(8) ** 2
print(arr, arr[2], arr[1:3])  # : 不包括后边界
arr[:2] = -666
print(arr)
arr[:5:2] = 777  # 前4个元素,每隔2个元素赋值 [ 777 -666  777    9  777   25   36   49]
print(arr)
for i in arr:
    print(i ** 3., end='\t')
    # 末尾加 . 意味类型转换为float


def g(x, y):
    return 100 * x + y


# fromfunction 数据来源函数
arr = fromfunction(g, (3, 3), dtype=int)
print(arr)
# arr[轴1,轴2]
print(arr[1, 2])  # 输出1行,2列的值
print(arr[0:3, 1])  # 输出0:3行,1列的值
print(arr[:, 2])  # 第2列的所有值
print(arr[2, :])  # 第二行的所有值
print(arr[-1, 1:3])
# 多维数组遍历第一个轴
for i in arr:
    print(i, end=type(i).__name__+'\n')
# 多维数组遍历所有元素
for i in arr.flat:
    print(i)