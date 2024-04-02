# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseNumpy.py
@Author     :wooght
@Date       :2024/3/15 18:26
@Content    :Numpy 基础
"""
import datetime

import numpy
from numpy import *
from wooght_tools.echo import echo

"""
    numpy 基础操作
    numpy.info()    查看函数说明
    size 数组元素个数
    itemsize 每个元素所占空间大小,以字节为单位
"""
echo("numpy基础操作")
info(add)
arr = numpy.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
echo(arr.size, arr.itemsize, nbytes)


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
print(arr.dtype)                                        # int16
"""
    numpy 数据类型
    数据类型    内置码     意义
    int8        i1     字节(-128 to 127)
    int16       i2      整数 16字节
    int32       i4      整数 32字节
    int64       i8      整数 64字节
    float16     f2      浮点数 16字节
    float32     f4      浮点数 32字节
    float64     f8      浮点数 63字节
    bool_       b       布尔类型
    Unicode     U       Unicode编码
    String      S       字符串
"""

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


"""
    对角矩阵
    单位矩阵numpy.eye(num) 这里是3阶单位矩阵(行列数相同,主对角线全为1的对角矩阵)
"""
echo('对角矩阵')
print(eye(3))
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
"""
    numpy.diag(v,k)     单词:diagonal 斜线的,对角线的
    v是一维时候: 生成对角矩阵,k默认0,小于0为对角线下方,大于0是上分
    v是二维时候: 返回这个二维数组的对角线的元素
"""
arr = diag(arange(4)+1, k=-1)
echo("diag:", arr)
arr = eye(5)
echo(arr, diag(arr))
echo("瓷砖矩阵")
"""
    numpy.tile(Arr,reps)    瓷砖平铺数组  单词 tile 瓷砖,瓦片
    Arr 要平铺的数组
    reps  平铺的方式 
    tile(arr,3)     水平平铺三次
    tile(arr,(3,3))  水平纵向各平铺三次
    tile(arr,(3,1))    纵向平铺三次
"""
arr = eye(2)
echo(arr, tile(arr, 3), tile(arr, (3, 3)), tile(arr,(3,1)))

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
delete_x = transpose(arr_2)
print(delete_x)
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
delete_x = arr[arr > 5]            # 取出大于5的元素,返回一个一维数组
print(delete_x)                  # [ 6  7  8  9 10 11 12 13 14]
print(where(arr > -1))          # 获取大于-1的所有元素的索引 (x索引列表,y索引列表)
# (array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2], dtype=int64), array([0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4], dtype=int64))

echo("索引,切片,赋值")
"""
    切片
    arr[横坐标,纵坐标]
    arr[start:end:step,::]
"""
arr = arange(5) ** 2
print(arr, arr[3], arr[:2])     # [ 0  1  4  9 16] 9 [0 1]
arr[3:] = 100                   # 集体赋值
print(arr)                      # [  0   1   4 100 100]
print(arr[::-1])                # [100 100   4   1   0]
arr.sort()
print(arr)                      # [  0   1   4 100 100]
arr = arange(10).reshape(5,2)
echo(arr, arr[2], arr[2:4])

z = zeros((8, 8), dtype=int)
z[1::2, ::2] = 1
z[::2, 1::2] = 1
echo("输出类似棋盘的矩阵:", z)
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
"""
    delete(ndarray,obj,axis)删除行或列,并返回新的矩阵
    ndarray 要操作的数组,obj要删除的位置,axis 维度 
"""
delete_x = delete(arr, 0, 0)
# [[2 0]
#  [4 0]
#  [6 0]
#  [8 0]]
delete_y = delete(arr, 0, 1)
print(delete_y)
# [[0]
#  [0]
#  [0]
#  [0]
#  [0]]
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

"""
    数组copy
    = 和原生的list一样,浅复制只是引用,他们拥有同一个地址,一个改动,另一个也改动
    view 创建一个视图,不共享内存, 但统一改动一个,另一个也改动了
    copy 创建完整的副本
"""
echo("数组copy")
arr1 = array([[1, 2, 3], [4, 5, 6]])
arr2 = arr1
arr1[0] = [100, 100, 100]
print(arr2)
# [[100 100 100]
#  [  4   5   6]]
print(arr1)
print(id(arr1), id(arr2))  # 相同内存
arr3 = arr1.view()
arr3[0] = [1, 2, 3]
print(arr1)
print(id(arr1), id(arr3))
arr4 = arr1.copy()
arr1[0] = [100, 100, 100]
print(arr4)
# [[1 2 3]
#  [4 5 6]]

"""
    numpy与日期
    数据类型:datetime64[Y/M/D/h/m/s]
"""
echo("numpy日期")
d = numpy.datetime64('2020-09-01')  # datetime64[D]
print(d.dtype)
print(numpy.datetime64('2020-09-01 10:00:01').dtype)    # datetime64[s]
"""强制指定单位"""
print(numpy.datetime64('2020-08', 'D'))     # 2020-08-01
days = numpy.arange('2020-01', '2020-02', dtype='datetime64[D]')
print(days)
days = numpy.arange("2020-01", "2020-02", dtype='datetime64[D]')
print(days)
month = numpy.arange('2020-01', '2020-12', dtype='datetime64[M]')
print(month)        # ['2020-01' '2020-02' '2020-03' '2020-04' '2020-05' '2020-06' '2020-07' '2020-08' '2020-09' '2020-10' '2020-11']
for m in month:
    print(m.__str__())
"""timedelta64 时间差"""
cha_days = numpy.datetime64('2019-09-20') - numpy.datetime64('2019-09-15')
echo(cha_days.dtype, cha_days)      # timedelta64[D] 5 days
cha_minth = numpy.datetime64('2020-08-09 20:00') - numpy.datetime64('2020-08-08', 'm')
print(cha_minth.dtype, cha_minth)       # timedelta64[m] 2640 minutes
tomorrow = numpy.datetime64('today', 'D') + numpy.timedelta64(1, 'D')
print("明天是:", tomorrow)
one_weeks = numpy.timedelta64(1, 'W')
one_day = numpy.timedelta64(1, 'D')
print(one_weeks/one_day)                # 7.0
"""工作日"""
the_day = numpy.datetime64('2020-08-08', 'D').astype(datetime.date)
print(numpy.is_busday(the_day))    # False
print(the_day.weekday())            # 5
days = numpy.arange('2020-09-09', '2020-10-10', dtype='datetime64[D]')
print(days)
new_day_list = numpy.where(numpy.is_busday(days),'上班','周末')
days_type = numpy.dtype([('datetime','datetime64[D]'),('is_busday','U2')])
arr = list(zip(days,new_day_list))
echo('格式化输出:',numpy.array(arr, dtype=days_type))



"""
    numpy 结构化数组
"""
echo("结构化数组")
position_type = numpy.dtype([('x', 'f4'), ('y', 'f4')])
print(position_type)
print(numpy.eye(3, dtype=position_type))

turnover_list = numpy.array([('2018-08-08', 11788, 3245), ("2018-10-10", 12568, 3654)],
                            dtype=[('date', 'datetime64[D]'), ('turnover', float), ('maoli', float)])
print(turnover_list)

turnover_type = numpy.dtype([('datetime', 'datetime64[D]'), ('turnover', numpy.float16), ('maoli', float)])
turnover_list = numpy.ones(31, dtype=turnover_type)
"""ndenumerate numpy的枚举功能"""
for i,day in numpy.ndenumerate(numpy.arange('2020-01-01', '2020-02-01', dtype='datetime64[D]')):
    turnover_list[i[0]]['datetime'] = day
print(turnover_list)
turnover_rec = numpy.rec.array(turnover_list)       # numpy.rec.array() 将结构化数组转化为对象
print(turnover_rec.datetime)
zero_arr = numpy.zeros((3,3), dtype=turnover_type)
for index, value in numpy.ndenumerate(zero_arr):
    print(index, value)
print(zero_arr.shape)
print(zero_arr[0, 2])
for index in numpy.ndindex(zero_arr.shape):
    print(index, zero_arr[index])
