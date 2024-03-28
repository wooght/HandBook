# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BasePandas.py
@Author     :wooght
@Date       :2024/3/28 14:26
@Content    :pandas 基础
"""
import numpy
import numpy as np
import pandas as pd
from wooght_tools.echo import echo
from wooght_tools.DateTimeMath import WDate

"""
    series 一维数组     单词:series 系列
    pandas.Series(data,index)
"""
echo('series')
countries = ['中国', '英国', '俄罗斯', '法国', '美国']
history = [5000, 3000, 3000, 3000, 300]
pd_data = pd.Series(history, countries)
echo(pd_data,pd_data['中国'])

history_dict = {'中国': 5000, '美国': 300}
pd_data = pd.Series(history_dict)
print(pd_data)
pd_data = pd.Series(history_dict, ['中国', '美国', '英国'])
print(pd_data)      # 英国对应NaN,表示缺失

countries_type = np.dtype([('name', 'U10'),('history', 'U10')])
np_data = np.array([('中国',5000),('美国',300)], dtype=countries_type)
try:
    pd_data = pd.Series(np_data)
    echo(np_data, pd_data)  # ValueError: Cannot construct a Series from an ndarray with compound dtype.  Use DataFrame instead.
except ValueError:
    echo("ValueError:",'不能从结构化numpy中series创建')

pd_data['日本'] = 1
pd_data2 = pd.Series(history, countries)
echo(pd_data * 2, pd_data + pd_data2)  # 加法是相应index进行加减,如果相应位置没有及为NaN


"""
    Dataframe   二维数组        单词: frame 框架
"""
echo("Dataframe")
original_data = {
    'name': pd.Series(['China', 'US', "En"], [1, 2, 3]),
    'history': pd.Series([5000, 300, 3000], [1, 2, 3]),
    'race': pd.Series(['黄', '白', '白'], [1, 2, 3])
}
df = pd.DataFrame(original_data)
print(df)
#     name  history race
# 1  China     5000    黄
# 2     US      300    白
# 3     En     3000    白
print(df.columns)               # 获取列坐标
print(df.index)                 # 获取索引
print(df.loc[1])                # 或者行数据 按给定的索引
print(df.iloc[0])               # 获取行数据 按默认的索引 从0开始
print(df['name'])               # 获取列数据
print(df[['name', 'history']])  # 获取多列数据
print(df['name'].loc[1])        # China
print(df['history'].iloc[0])    # 5000
original_data = {
    'name': ['China', 'US', "En"],
    'history': [5000, 300, 3000],
    'race': ['黄', '白', '白']
}
df = pd.DataFrame(original_data, index=['中', '美', '英'])
print(df)
print(df.loc['中']['name'])              # 指定某行某列
print(df.loc['中', 'name'])
print(df.iloc[0, 1])                     # 指定某行某列
print(df.loc[['中', '英']])               # 获取指定的多行
print(df.loc[['中', '英'], ['name']])     # 获取指定多行的多列
print(df[df['history'] > 1000])          # 条件筛选

"""增加数据"""
df['area'] = pd.Series([960, 930, 70], index=['中', '美', '英'])
print(df)
echo('多条件筛选', df[(df['history'] > 1000) & (df['area'] > 100)])

"""
    删除数据
    drop(位置,方向,正式删除)
"""
df.drop('area', axis=1, inplace=True)
print(df)
df.drop('英', axis=0, inplace=True)
print(df)
df.reset_index(inplace=True)                # 删除索引, 删除后会自动生成0开始的索引
print(df)
df['id'] = pd.Series(['id1','id2'],index=[0,1])
print(df)
df.set_index('id', inplace=True)        # 设置新的索引
print(df)

"""
    多级索引    MultiINdex  单词 Multi 多个 
"""
outside = ['0 grade', '0 grade', '0 grade', '1 grade', '1 grade', '1 grade']
inside = [11, 12, 13, 11, 12, 13]
grade_index = list(zip(outside, inside))
multi_index = pd.MultiIndex.from_tuples(grade_index)
print(multi_index)
df = pd.DataFrame(np.random.randint(1, 100, size=(6, 2)), index=multi_index, columns=['A', 'B'])
echo('访问多级索引', df, df.loc['0 grade'], df.loc['0 grade', 11], df.loc[['0 grade'], ['A']])
df.index.names = ['Levels', 'score']
#                 A   B
# Levels  score
# 0 grade 11     14  28
#         12     60  41
#         13     63  93
# 1 grade 11     92  67
#         12     34  82
#         13     66   4
print(df.xs(13, level='score'))     # 获取某个等级的所有元素

"""缺失值"""
df = pd.DataFrame({'name':['China', 'USA', 'Rus'], 'area':[906,930,None]})
print(df)
df.dropna(axis=0, inplace=True)     # 删除有缺失值的行
print(df)
df = pd.DataFrame({'name':['China', 'USA', 'Rus'], 'area':[960,930,None]})
df.fillna(0, inplace=True)      # 替换缺失值
print(df)

"""分组统计"""
area_list = ['area_A', 'area_B', 'area_C']
echo("groupby 分组统计")
def get_area(num):
    return {
        'area_name': numpy.random.choice(area_list, num),
        'turnover': numpy.random.randint(12000, 12005, num),
        'maolilv': numpy.random.uniform(0.25, 0.29, num)
    }
df = pd.DataFrame(get_area(30))
print(df)
print(df.groupby('area_name').mean())
print(df.groupby('area_name').describe())                       # 数据描述  单词:describe 描述
describe_T = df.groupby('area_name').describe().transpose()     # 转置数据
print(describe_T)
echo(describe_T['area_A'], describe_T['area_A'].loc['turnover','mean'])


echo('concat 堆叠')
data_a = pd.DataFrame(get_area(5))
data_b = pd.DataFrame(get_area(3))
print(pd.concat([data_a, data_b]))                  # concat([data1,data2...], axis) 堆叠数据
print(pd.concat([data_a, data_b], axis=1))

echo('merge 归并/合并')
date_list = np.arange('2020-09-09', '2020-09-13', dtype='datetime64[D]')
data_a = pd.DataFrame({
    'datetime': date_list,
    'turnover': np.random.randint(10000, 10005, 4),
})
data_b = pd.DataFrame({
    'datetime': date_list,
    'maolilv': np.random.uniform(0.25, 0.28, 4)
})
"""
    merge 合并,归并     单词:merge  合并
    merge(left,right, how="inner/outer/left/right", on="key")
    left,right 值要归并的数据
    how:inner,outer 指内连接(交集),外连接(并集).left/right 指取左边全部,右边全部,没有则NaN填充
    on:归并的键所在列
"""
print(pd.merge(data_a, data_b, how="inner", on='datetime'))

"""查找不重复的值"""
echo("重复值")
area_A = pd.DataFrame(get_area(30))
print(area_A)
print(area_A['turnover'].unique())                  # [12001 12000 12002 12004 12003]
print(area_A['turnover'].nunique())                 # 不重复值的个数
print(area_A['turnover'].value_counts())            # 所有值和重复次数组成的DataFrame
print(area_A['turnover'].value_counts().values)     # 重复次数组成的列表
print(area_A['turnover'].value_counts().loc[12004]) # 获取某个重复值的次数

"""apply 自定义函数"""
def square(num):
    return num*1.2

print(area_A['turnover'].apply(square))             # 对数据进行自定义函数运算
print(area_A['turnover'].apply(lambda x: x*1.2))
print(area_A['maolilv'].apply(lambda x: '%.2f' % x))


data_a = pd.DataFrame({
    'datetime': date_list,
    'turnover': np.random.randint(10000, 10010, 4),
})
data_b = pd.DataFrame({
    'datetime': date_list,
    'maolilv': np.random.uniform(0.25, 0.28, 4)
})
echo(data_a,"排序:", data_a.sort_values('turnover', ascending=False))     # 按列排序,ascending 是否正序
all_data = pd.merge(data_a, data_b, how='inner', on='datetime')


print(WDate.run_time())