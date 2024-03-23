# -- coding: utf-8 -
"""
@project    :HandBook
@file       :NumpyVector.py
@Author     :wooght
@Date       :2024/3/22 17:18
@Content    : 向量整理
"""
import numpy
from wooght_tools.echo import echo

"""n维向量的线性运算"""
echo("列表的加法:")
nums_list = [1, 2, 3]
nums2_list = [3, 2, 1]
echo(nums_list, nums2_list, "列表加法:", nums_list + nums2_list)
echo("列表数乘:", nums_list * 5)
echo("向量的和")
vec = numpy.array([1, 2, 3])
vec2 = numpy.array([3, 2, 1])
echo(vec, vec2, "和:", vec + vec2, "差:", vec - vec2)
echo('向量数乘:', vec, 'vec*5', vec * 5, "5*vec", 5 * vec)

echo("线性相关")
vec_arr = numpy.array([
    [1,2,3],[4,5,6],[7,8,9]
])
if numpy.linalg.det(vec_arr) == 0 :echo(vec_arr,"D值为0,及线性相关")
"""向量组线性不相关,每个向量上加一个分量后,也线性不相关"""
vec_arr = numpy.array([
    [0,1,1,2],[1,1,0,3],[0,0,2,4]
])
A_matrix = vec_arr[:,0:3]
message = "D值为0,线性相关" if numpy.linalg.det(A_matrix) == 0 else "D值不为零,线性不相关"
echo(vec_arr,A_matrix,message)


echo("线性表出/线性组合")
"""
    n维向量B = k1a1+k2a2..kmam (k1,k2,..km) 不全为零,则B是a1,a2..an这个向量组的线性组合
"""
vec_1 = numpy.array([
    [1, 2, 3], [4, 5, 6], [7, 8, 10], [11, 12, 13]
])
A_matrix = vec_1[0:3, :]
B_matrix = vec_1[3]
echo("向量组",A_matrix, "向量",B_matrix, "线性表示唯一值:",numpy.linalg.solve(A_matrix, B_matrix))


result_list = []
def indexcomb(temp_list):
    """
        说明: 求列表的所有组合
        返回值: None,调用全局变量
    """
    for i in range(len(temp_list)):
        temp = temp_list.copy()
        temp.pop(i)
        if temp not in result_list: result_list.append(temp)
        if len(temp) > 2: indexcomb(temp)


echo("极大无关组")
vec_arr = numpy.array([
    [1, 0, 0], [0, 1, 0], [0, 0, 1], [2, 0, 0], [0, 2, 0]
])
indexcomb([i for i in range(vec_arr.shape[0])])
print(result_list)
zhi = 0
for arr in result_list:
    if len(arr) >= 3:
        matrix = numpy.zeros((3, 3))
        for i in arr:
            matrix = numpy.vstack((matrix, vec_arr[i]))
        if len(arr) == 3:
            if numpy.linalg.det(matrix[3:, :]) != 0: print('不相关', matrix[3:, :])
            zhi = 3
        if len(arr) == 4:
            new_matrix = matrix[3:, :]
            A_matrix = new_matrix[0:3, :]
            B_matrix = new_matrix[3, :]
            try:
                numpy.linalg.solve(A_matrix, B_matrix)
            except:
                print(matrix[3:, :])
print("极大无关组向量个数,就是向量组的秩:", zhi)
print("矩阵的秩:",numpy.linalg.matrix_rank(vec_arr))