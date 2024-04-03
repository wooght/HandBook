# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseSeries.py
@Author     :wooght
@Date       :2024/4/3 16:07
@Content    :pandas Series 操作
"""
import pandas as pd
import numpy as np
from wooght_tools.echo import echo


"""
    series 一维数组     单词:series 系列
    pandas.Series(data,index)
"""
echo('series')
countries = ['中国', '英国', '俄罗斯', '法国', '美国']
history = [5000, 3000, 3000, 3000, 300]
pd_data = pd.Series(history, countries)
echo(pd_data, '取值:', pd_data['中国'])

"""根据字典创建series"""
history_dict = {'中国': 5000, '美国': 300}
pd_data = pd.Series(history_dict)
print(pd_data.to_frame())
pd_data = pd.Series(history_dict, ['中国', '美国', '英国'])
print(pd_data)      # 英国对应NaN,表示缺失

countries_type = np.dtype([('name', 'U10'), ('history', 'U10')])
np_data = np.array([('中国', 5000), ('美国', 300)], dtype=countries_type)
try:
    pd_data = pd.Series(np_data)
    echo(np_data, pd_data)  # ValueError: Cannot construct a Series from an ndarray with compound dtype.  Use DataFrame instead.
except ValueError:
    echo("ValueError:", '不能从结构化numpy中series创建')

"""series 基本运算"""
pd_data['日本'] = 1
pd_data2 = pd.Series(history, countries)
echo(pd_data * 2, pd_data + pd_data2)  # 加法是相应index进行加减,如果相应位置没有及为NaN

echo("series 基本函数")
"""
    value_conts() 每个值出现的次数 size 元素个数
    pd.fillna(n)    将NaNo替换成n
    describe()  摘要统计,包括方差,平均值,中位数,个数等统计
"""
echo(pd_data.value_counts(), pd_data.size, pd_data.shape)
echo('基础数学函数:', pd_data.min(), pd_data.max(), pd_data.sum(), pd_data.median(), pd_data.std())
echo(pd_data.isnull(), pd_data.fillna(1), pd_data.describe())
