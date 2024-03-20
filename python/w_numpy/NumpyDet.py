# -- coding: utf-8 -
"""
@project    :HandBook
@file       :NumpyDet.py
@Author     :wooght
@Date       :2024/3/18 21:15
@Content    :行列式应用
"""

from wooght_tools.echo import echo
import numpy
def get_cofactor(matrix, i, j):
    """  获取余子式 """
    """
        行列式a如下:
        [[1,2,3],
         [4,5,6],
         [7,8,9]]
         a11,a12的余子式分别是:
         [[5,6],    [[4,6],
          [8,9]]     [7,9]]
    """
    dx_matrix = numpy.delete(matrix, i, 0)
    cofactor = numpy.delete(dx_matrix, j, 1)
    return cofactor

def determinant(matrix):
    """
    计算行列式的值 n阶方阵/n阶矩阵
    公式: n阶行列式 n**2个元素 值为D,D等于第一行的元素分别乘以它的代数余子式再求和
        D = ∑Aij*(-1)**(i+j)*Mij    i=1 ,j=(1..n)   Mij余子式
    """
    shapes = matrix.shape
    if shapes[0] != shapes[1] or matrix.ndim !=2 : return None
    if shapes[0] == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        sgm = 0
        for j in numpy.arange(0, shapes[0]):
            cofactor = get_cofactor(matrix, 0, j)
            sgm += matrix[0][j] * (-1) ** (2+j) * determinant(cofactor)
        return sgm
numpy.random.seed(1)
arr = numpy.random.randint(-10, 10, (4,4))
print(arr)
print('余子式:')
print(get_cofactor(arr,0, 0))
sgm = determinant((arr))
print(sgm)
print(numpy.linalg.det(arr))        # 矩阵行列式的值
echo("行列式的法则")
""" 行列式调换两行,符号相反 """
arr_2 = arr.copy()
arr_2[0], arr_2[1] = arr[1], arr[0]
print('符号变化:', determinant(arr_2))
""" 行列式两行相同,值为0 同倍数也为0"""
arr_2[0] = arr[0]
print("值为0:", determinant(arr_2))            # 0
"""行列式某一行扩大K倍,值也扩大K倍"""
arr[0] = arr[0] * 5
print(arr)
print("扩大K倍",determinant(arr))
"""行列式某一行加上另一行的K倍,值不变"""
arr[1] = arr[1] + arr[2] * 2
print(arr)
print("加上另外一行的K倍,值不变", determinant(arr))

echo("对角行列式")
arr_d = numpy.eye(4)
arr_d[1, 1], arr_d[2, 2] = 5, 6
# [[1. 0. 0. 0.]
#  [0. 5. 0. 0.]
#  [0. 0. 6. 0.]
#  [0. 0. 0. 1.]]
"""
    对角行列式  A11,A22..Ann(称为主对角线)不为零,其余元素皆为0
    值等于对角线上的元素的积
"""
print(determinant(arr_d))
""" 
    三角行列式
    值任然等于对角行列式 
"""
for i in range(0,arr_d.shape[0]):
    for j in range(i+1, arr_d.shape[0]):
        arr_d[i,j] = numpy.random.randint(10)
# [[1. 4. 5. 2.]
#  [0. 5. 4. 2.]
#  [0. 0. 6. 4.]
#  [0. 0. 0. 1.]]
print(determinant(arr_d))

echo("解线性方程组")
""" 
    解线性方程组 System of linear equations
    X11*A11+X12*A12... = B1
    X21*A21+X22*A22... = B2
    ...
    Xn1*An1+Xn2*An2... = Bn
            |B1  A12  ...|
            |B2  A22  ...|
            |...         |
    X1 = ____________________
            |A11 A12  ...|
            |A21 A22  ...|
            |...         |
"""
def Sole(matrix):
    """
    求多元齐次次线性方程的解
    克莱姆法则   适用于变量数与方程组相等的线性方程
    公式:
        x1 = D1/D,  x2 = D2/D ...
        D为变量系数组成的行列式
        D1 为在D的基础上将变量所对应的列替换为=后边的列
    """
    ndim = matrix.shape[0]
    d = matrix[:, :ndim]
    d_value = determinant(d)
    b = matrix[:, ndim]
    return_list = []
    if d_value == 0: return None
    for i in range(matrix.shape[0]):
        di = d.copy()
        di[:, i] = b
        return_list.append(determinant(di) / d_value)
    return return_list
"""
    1x + 2y = 3
    2x + 3y = 5
    转换为行列式
    [
    [1,2,3],
    [2,3,5]]
"""
sole2 = numpy.array([[1, 2, 3], [2, 3, 5]])
print(Sole(sole2))      # [1.0, 1.0]  x,y的值分别是1,1
sole3 = numpy.array([[2, 5, 9], [4, 9, 44]])
print(Sole(sole3))      # [69.5, -26.0]
sole4 = numpy.array([[2, 4, 6, 19], [3, -1, 3, 12], [1, 6, -7, 77]])
print(Sole(sole4))      # [10.345744680851064, 6.0638297872340425, -4.324468085106383]
