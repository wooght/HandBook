# -- coding: utf-8 -
"""
@project    :HandBook
@file       :FuncNumpy.py
@Author     :wooght
@Date       :2024/3/16 13:04
@Content    :Numpy 数组操作运算
"""
import random

import numpy.linalg

from wooght_tools.echo import echo
from numpy import *

numpy.set_printoptions(suppress=True)       # set_printoptions() 设置打印选项 取消科学计数法
echo('array 合并')
"""
    hstack((arr..))             # x轴合并  行合并 水平      合并的元素有相同的行
    vatack((arr..))             # y轴合并  列合并 垂直      合并的元素有相同的列
"""
arr = arange(9).reshape(3,3)
arr_2 = arange(9, 15).reshape(3, 2)
print(arr)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
print(arr_2)
# [[ 9 10]
#  [11 12]
#  # [13 14]]
arr_3 = hstack((arr, arr_2))
print(arr_3)
# [[ 0  1  2  9 10]
#  [ 3  4  5 11 12]
#  [ 6  7  8 13 14]]

arr = random.random((3, 3))
# [[0.55727641 0.24649873 0.9106814 ]
#  [0.19821806 0.66159848 0.13725621]
#  [0.18209827 0.41629981 0.07467693]]
arr_2 = ones((2, 3))
# [[1. 1. 1.]
#  [1. 1. 1.]]
arr_3 = vstack((arr, arr_2))
print(arr_3)
# [[0.01763516 0.78524637 0.44146776]
#  [0.95876891 0.52638454 0.6987244 ]
#  [0.82681885 0.55327809 0.76765581]
#  [1.         1.         1.        ]
#  [1.         1.         1.        ]]
"""
    concatenate((arr..), axis=) # 合并数组 axis指定合并的方向
    0为垂直方向,1为水平方向
"""
arr_4 = concatenate((arr, arr_2), axis=0)
print(arr_4)
# [[0.35136048 0.42227244 0.65578136]
#  [0.00320955 0.26568225 0.54466677]
#  [0.62791553 0.58443731 0.99565765]
#  [1.         1.         1.        ]
#  [1.         1.         1.        ]]
try:
    arr_4 = concatenate((arr, arr_2), axis=1)
except ValueError:
    print('行数不同')                   # 运行    合并的数组在轴方向上必须一致

"""rashape() 重塑形状"""
arr = arange(4).reshape((2,2))
# [[0 1]
#  [2 3]]
print(arr.reshape((4,1)))
# [[0]
#  [1]
#  [2]
#  [3]]

echo("numpy 矩阵运算")
"""
    广播功能;对位进行运算,
    低纬与高纬的每一行进行运算
"""
arr = array([[1, 2], [3, 4]])
print(arr + array([9, 10]))
# [[10 12]
#  [12 14]]
print(arr - 2)
# [[-1  0]
#  [ 1  2]]

arr = arange(4)             # [0 1 2 3]
arr_2 = arange(4,8)         # [4 5 6 7]
print(arr + arr_2)          # [ 4  6  8 10]

arr = arange(1,4)           # [1 2 3]
print(arr**2)               # [1 4 9]       每个位置进行2次幂运算
print(square(arr))          # [1 4 9]       矩阵平方
"""
    sin(arr)    对numpy数组每个元素进行正弦运算
    cos(arr)    余弦运算
    tan(arr)    正切运算
    sqrt(arr)   开根号运算
"""
print(10*sin(arr))          # [8.41470985 9.09297427 1.41120008]

echo("矩阵点乘")
""" 点乘  又称:哈达玛积 要求相称的两个矩阵大小形状完全相同   """
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
arr = arange(6).reshape(2, 3)
arr_2 = arange(6, 12).reshape(2, 3)
print(arr * arr_2)
# [[ 0  7 16]
#  [27 40 55]]
echo("普通乘法")
"""
    dot(arr1,arr2)
    普通乘法,要求第一个矩阵的列数要等于另一个矩阵的行数
"""
arr = arange(6).reshape(2,3)
# [[0 1 2]
#  [3 4 5]]
arr_2 = arange(6,12).reshape(3,2)
# [[ 6  7]
#  [ 8  9]
#  [10 11]]
"""
    运算方式:
    [0*6+1*8+2*10, 0*7+1*9+2*11
     3*6+4*8+5*10, 3*7+4*9+5*11]
"""
assert arr.shape[1] == arr_2.shape[0]       # assert 当套件成立才继续执行
print(dot(arr, arr_2))
# [[ 28  31]
#  [100 112]]
print(dot(arr_2, arr))                      # 矩阵乘法不能交换位置,交换位置后结果也变了
# [[21 34 47]
#  [27 44 61]
#  [33 54 75]]

echo('矩阵常规数学运算')
"""
    axis=0  指垂直方向,及列
    axis=1  指水平方向,及行
"""
arr = arange(0, 9).reshape(3,3)
arr[1, 2] = 11
# [[ 0  1  2]
#  [ 3  4 11]
#  [ 6  7  8]]
print(arr.max())                    # 11
print(arr.max(axis=0))              # [6 7 11]   每列最大
print(arr.max(axis=1))              # [2 11 8]   最行最大
print(arr.argmax(axis=0))           # [2 2 1]    每一列最大的索引
print(arr.min())                    # 0          最小值
print(arr.mean())                   # 4.66..     平均值
print(arr.mean(axis=0))             # [3. 4. 7.]    每一列的平均值
print(arr.sum())                    # 42            求和
print(arr.var())                    # 11.555.       方差
print(arr.var(axis=0))              # [ 6.  6. 14.] 每一列的方差
print(arr.std(axis=0))              # [2.44948974 2.44948974 3.74165739]    标准差 及方差的算数平方根
print(arr.cumsum())                 # [ 0  1  3  6 10 21 27 34 42]          之前数的累加 及n=∑(n-1)

print(median(arr))                  # 4.0           中位数
print(median(arr,axis=0))           # [3. 4. 8.]    每一列的中位数

echo("numpy的random和原生random用法相识")
print(random.randn(10))                             # 随机正态分布数组 平均值为0, 方差为1
# [ 0.55402747 -0.03356931 -0.49272335  0.00689967 -1.05794256  0.41512391
#   0.36155496 -0.47186917 -0.53020383 -0.80265128]
print(random.rand(10).reshape(2, 5))                # 随机0-1的数据数组, 具有均匀分布
# [[0.37132652 0.5589355  0.12176712 0.92824329 0.88278714]
#  [0.36963314 0.13043997 0.03338992 0.59251962 0.29262469]]
print(random.randint(1, 5, (3, 3)))                  # 给定范围的随机整数
# [[3 3 2]
#  [1 3 2]
#  [2 1 4]]
print(random.random((2, 3)))                         # 0到1的随机数 random((维度))
# [[0.70050286 0.65787913 0.02066382]
#  [0.46570063 0.43273537 0.41394429]]
random.seed(1)                                      # 随机一次数据,然后以后每次运行的时候,都和第一次是相同的随机数
print(random.rand(2, 2))
# [[4.17022005e-01 7.20324493e-01]
#  [1.14374817e-04 3.02332573e-01]]
arr = random.randint(1, 10, 20)
print(arr)                          # [1 1 2 8 7 3 5 6 3 5 3 5 8 8 2 8 1 7 8 7]
print(random.choice(arr, 4))   # [1 1 7 3]  choice 只能是一维
random.shuffle(arr)                 # 随机排序  ,当时二维时,只对行进行随机排序
print(arr)                          # [5 8 2 8 1 7 1 7 7 5 1 3 5 8 6 2 3 3 8 8]
arr = random.randint(1, 10, (5, 3))
# [[1 4 3]
#  [1 5 3]
#  [8 8 9]
#  [7 4 8]
#  [8 5 6]]
random.shuffle(arr)
print(arr)
# [[8 5 6]
#  [1 4 3]
#  [8 8 9]
#  [7 4 8]
#  [1 5 3]]
print(random.normal(0, 1, (2, 3)))  # 正态分布, normal(平均值,方差,size)

echo("numpy对矩阵的应用")
vec_arr = array([
    [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]
])
matrix_arr = vec_arr[0:3, :]
echo(vec_arr, matrix_arr, '行列式的值:', linalg.det(matrix_arr))
echo("方阵的秩:", linalg.matrix_rank(matrix_arr))
b_arr = vec_arr[3, :]
matrix_arr[2][2] = 10
echo('齐次方程组系数:', matrix_arr, '常数:', b_arr, "方程组的解:", linalg.solve(matrix_arr, b_arr))
echo("矩阵的逆矩阵", linalg.inv(matrix_arr))
matrix_inv = linalg.inv(matrix_arr)
echo("A和A逆相乘等于E", dot(matrix_arr, matrix_inv))
