# -*- coding: UTF-8 -*-
#
# numpy python数组扩展用法
# by wooght 2017-11
# array的应用
#
import numpy as np
a = [1,2,3,4]
b = np.array(a)
print(b)

#array 讲元祖也转为列表
print(np.array((1,2,3,4)))

print(np.array([[1,2],[3,4]]))

#可以指定数据类型 int32,64...
print(np.array([1,2,3,4],dtype=np.int32))

#arange 连续个数  arange.reshape()对连续数 构造矩阵
print(type(np.arange(15)),np.arange(15))
ndarr = np.arange(100,115).reshape(3,5)
print(ndarr)
# [[100 101 102 103 104]
#  [105 106 107 108 109]
#  [110 111 112 113 114]]

#linspace 1到5之间产生5个数
randomnum = np.linspace(1,5,5)
print(randomnum)
for i in randomnum:
    print(i)

print(np.zeros((3,4)))              #0的矩阵 3行4列
print(np.ones((3,4)))               #1的剧中 3行4列
print(np.eye(3))

three_array = np.zeros((3,4,5))     #三维数组构建
print(three_array)
# [[[ 0.  0.  0.  0.  0.]
#   [ 0.  0.  0.  0.  0.]
#   [ 0.  0.  0.  0.  0.]
#   [ 0.  0.  0.  0.  0.]]
#
#  [[ 0.  0.  0.  0.  0.]
#   [ 0.  0.  0.  0.  0.]
#   [ 0.  0.  0.  0.  0.]
#   [ 0.  0.  0.  0.  0.]]
#
#  [[ 0.  0.  0.  0.  0.]
#   [ 0.  0.  0.  0.  0.]
#   [ 0.  0.  0.  0.  0.]
#   [ 0.  0.  0.  0.  0.]]]


print(three_array.ndim)     #获取维度
print(three_array.size)     #获取元素个数
print(three_array.dtype)    #元素类型

new_arr = np.array([[1,2,3],[4,5,6]])
print(new_arr[1][2])                        #通过索引查询
print(new_arr[1,:])                         #切片
# [[4 5 6]]
new_arr[1,:] = [8,9,10]                     #赋值
print(new_arr)

num1 = np.ones((2,2))
num2 = np.eye(2)
print(num1,num2)
print(num1*num2)

print(num2*2/(num1**2))
print(num1.sum())                           #全部求和
print(num2.sum(axis=0))                     #每一列求和
print(num1.max())
print(num2.min())

print(np.sin(num1))
print(np.cos(num1))
