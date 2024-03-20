# -- coding: utf-8 -
"""
@project    :HandBook
@file       :NumpyMatrix.py
@Author     :wooght
@Date       :2024/3/19 16:10
@Content    :矩阵应用
"""
import numpy
from wooght_tools.echo import echo
from NumpyDet import determinant, get_cofactor

numpy.set_printoptions(suppress=True)       # set_printoptions() 设置打印选项 取消科学计数法
def mcl_nums(matrix, num):
    """
    矩阵数乘   乘法 multiplication
    数乘:矩阵的每个元素都要去乘以乘数
     """
    x, y = matrix.shape[0], matrix.shape[1]
    for i in range(x):
        for j in range(y):
            matrix[i][j] *= num
    return matrix

echo('矩阵数乘')
arr = numpy.arange(0,10).reshape(5,2)
echo(arr, mcl_nums(arr.copy(), 2))
# [[ 0  2]
#  [ 4  6]
#  [ 8 10]
#  [12 14]
#  [16 18]]
print(arr*2)        # 与上方相同


echo("矩阵乘法")
def mcl_matrix(m1, m2):
    """
    矩阵乘法    矩阵A*矩阵B
    矩阵A的列数L必须等于矩阵B的行数H
    |A11 A12|       |B11 B12|       |A11*B11+A12*B21  A11*B12+A12*B22|
    |A21 A22|   *   |B21 B22|   =   |A21*B11+A22*B21  A21*B12+A22*B22|
    |A31 A32|                       |A31*B11+A32*B21  A31*B12+A32*B22|
    新矩阵C的阶数为:(A的行M,B的列N)
    C矩阵ij位置的元素值为: ∑Ai0*B0j+Ai1*B1j...AiL*BLj    及A的i行元素与B的j列元素对应乘积之和
    """
    m1_shape = m1.shape
    m2_shape = m2.shape
    if m1_shape[1] != m2_shape[0]: return None
    result_arr = numpy.zeros((m1_shape[0], m2_shape[1]))
    for i in range(m1_shape[0]):
        for j in range(m2_shape[1]):
            for k in range(m2_shape[0]):
                result_arr[i][j] += m1[i][k] * m2[k][j]
    return result_arr
arr2 = numpy.arange(10).reshape(2, 5)
echo(arr, arr2)
print(mcl_matrix(arr, arr2))
# [[ 10.  12.  14.  16.  18.]
#  [ 30.  40.  50.  60.  70.]
#  [ 50.  68.  86. 104. 122.]
#  [ 70.  96. 122. 148. 174.]
#  [ 90. 124. 158. 192. 226.]]
print(mcl_matrix(arr2, arr))        # 矩阵乘法交换位置后结果会随之改变
# [[120. 140.]
#  [320. 390.]]
arr = numpy.array([[-1, -2], [-2, -4]])
print(mcl_matrix(arr, arr))
print(numpy.dot(arr,arr))


echo("矩阵转置")
def transposition(matrix):
    shape = matrix.shape
    result_m = numpy.zeros((shape[1], shape[0]))
    for i in range(shape[1]):
        result_m[i,:] = matrix[:,i]
    return result_m
arr = numpy.linspace(1, 10, 15).reshape(3, 5)
echo(arr, transposition(arr))
"""T(AB) = T(B)*T(A)"""
arr = numpy.arange(6).reshape(2,3)
arr_2 = numpy.random.randint(1,10,(3,2))
print(arr, '\r\n', arr_2)
Tab = transposition(mcl_matrix(arr,arr_2))
TbTa = mcl_matrix(transposition(arr_2), transposition(arr))
echo(Tab, TbTa)             # 两者相同

echo("伴随矩阵")
def adjoint_matrix(matrix):
    """返回矩阵的伴随矩阵 adjoint 伴随"""
    matrix_t = transposition(matrix)
    shape = matrix_t.shape
    if shape[0] != shape[1]: return None
    result_array = numpy.zeros((shape[0], shape[1]))
    for i in range(shape[0]):
        for j in range(shape[1]):
            result_array[i][j] = (-1)**(i+j)*determinant(get_cofactor(matrix_t,i,j))
    return result_array


arr = numpy.random.randint(10, 30, (3, 3))
arr_adjoint = adjoint_matrix(arr)
echo('原矩阵:',arr,'伴随矩阵:', arr_adjoint)
""" A*A伴==|A|En """
eye_3 = numpy.eye(3)
print(determinant(arr))
echo("A * A伴", mcl_matrix(arr, arr_adjoint), "|A|*E", determinant(arr) * eye_3)
# [[-449.    0.    0.]
#  [   0. -449.    0.]
#  [   0.    0. -449.]]
# [[-449.   -0.   -0.]
#  [  -0. -449.   -0.]
#  [  -0.   -0. -449.]]
echo("逆矩阵")
"""逆矩阵 A逆 = (1/|A|)*A伴"""
def inverse_matrix(matrix):
    """返回矩阵的逆矩阵"""
    return (1 / determinant(matrix)) * adjoint_matrix(matrix)
echo("A逆:", inverse_matrix(arr), "A*A逆=E:", mcl_matrix(arr, inverse_matrix(arr)))
print(numpy.linalg.inv(arr))        # numpy.linalg.inv()    numpy的逆矩阵函数

"""实例"""
"""
    A = [[2, 1, -1],
         [2, 1, 0],
         [1, -1, 1]]
    C = [[1, -1, 3],
         [0, 0, 1]]
    YA  = C   求Y    
    因: A * A逆 = E  估,等式两边同时乘以A逆
    Y = C*A逆
"""
arr_a = numpy.array([[2, 1, -1],
                     [2, 1, 0],
                     [1, -1, 1]])
arr_c = numpy.array([[1, -1, 3],
                     [0, 0, 1]])
echo(arr_a, arr_c, 'Y=', mcl_matrix(arr_c, (1/determinant(arr_a))*adjoint_matrix(arr_a)))

echo("矩阵求解线性方程组")
def Sole(matrix):
    """
    矩阵求解齐次线性方程组
    AX = B  推导出:  X = A逆 * B
    """
    shape = matrix.shape
    A = numpy.delete(matrix, shape[1]-1, 1)
    B = matrix[:,shape[1]-1]
    A_inverse = inverse_matrix(A)
    return numpy.dot(A_inverse, B)


arr = numpy.array(
    [[0, 1, 2, -1],
     [1, 1, 4, 0],
     [2, -1, 0, 2]]
)
echo('方程组矩阵为:', arr, "X的值分别为:", Sole(arr))
