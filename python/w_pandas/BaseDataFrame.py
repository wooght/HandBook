# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseDataFrame.py
@Author     :wooght
@Date       :2024/3/28 14:26
@Content    :DataFrame 基础
"""
import numpy
import numpy as np
import pandas as pd
from wooght_tools.echo import echo
from wooght_tools.DateTimeMath import WDate


"""
    Dataframe   数据表        单词: frame 框架
    pd.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)
"""
echo("Dataframe创建数据表")
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

echo("基础信息")

print(df.shape)                 # 获取维度元祖
print(df.columns)               # 获取列坐标object
print(df.columns.values)        # 获取列坐标列表
print(df.index)                 # 获取索引
print(df['name'].isnull)        # 是否空值

echo("数据提取->列操作")
print(df.history)                       # 获取一列数据
history_data = df['history']            # 获取一别数据
echo(history_data, history_data[1])
history_data += 1
history_data *= 2                       # 整列值数学运算
print(history_data)
print(history_data > 100)               # 得到新的DataFrame,是判断语句的结果
print(history_data.eq(100))             # ?==
print(history_data.astype(int).mod(5))  # 取模    %
print(history_data.floordiv(5))         # 整除    //
print(df['name'].str.split(''))         # 整列字符串操作
print(df[['name', 'history']])          # 获取多列数据

echo("数据提取->行操作")
print(df.loc[1])                        # 获取行数据 按给定的索引
echo('多行:', df.iloc[0:2])         # 获取行数据 按默认的索引 从0开始
print(df['name'].loc[1])                # China
print(df['history'].iloc[0])            # 5000
original_data = {
    'name': ['China', 'U S ', "En"],
    'history': [5000, 300, 3000],
    'race': ['黄', '白', '白']
}
df = pd.DataFrame(original_data, index=['中', '美', '英'])
print(df)
print(df.loc['中']['name'])              # 指定某行某列
print(df.loc['中', 'name'])              # 两者效果相同 [行,列]
print(df.iloc[0, 1])                     # 指定某行某列
print(df.loc[['中', '英']])               # 获取指定的多行
print(df.loc[['中', '英'], ['name']])     # 获取指定多行的多列
print(df[df['history'] > 1000])          # 条件筛选
print(df[df['name'].isin(['China', 'En'])])
print(df.filter(items=['name']))

"""
    数据清洗
        去空,去重
"""
echo("数据清洗")

area_list = ['area_A', 'area_B', 'area_C']
def get_area(num):
    return {
        'area_name': numpy.random.choice(area_list, num),
        'turnover': numpy.random.randint(12000, 12005, num),
        'maolilv': numpy.random.uniform(0.25, 0.29, num)
    }
original_data = {'name': ['China', 'USA ', 'Rus'], 'area': [960, 930, None]}
df = pd.DataFrame(original_data, index=['中', '美', '俄'])
df['name'] = df['name'].map(str.strip)                                       # 去掉空格 map函数,类似原生map
echo('去空格后:',df)
df.dropna(axis=0, inplace=True)                                              # 删除有缺失值的行
echo('删除后:', df)

df = pd.DataFrame(original_data, index=['中', '美', '俄'])
df.fillna(960, inplace=True)                                          # 替换缺失值
echo('替换后', df)
df['history'] = pd.Series([5000, 300, 3000], index=['中', '美', '俄'])    # 增加列
df.rename(columns={'area': 'area_size'}, inplace=True)                        # 改列名
echo('多条件筛选', df[(df['history'] > 1000) & (df['area_size'] > 100)])    # 多条件筛选
df.drop_duplicates(['area_size'], keep='first', inplace=True)          # 删除重复值
echo("删除重复值:", df)

df = pd.DataFrame(original_data, index=['中', '美', '俄'])
df.drop('area', axis=1, inplace=True)                                   # drop(位置,方向,正式删除)
print(df)
df.drop('俄', axis=0, inplace=True)                                      # 删除行
print(df)
df.reset_index(inplace=True)                                                  # 删除索引, 删除后会自动生成0开始的索引
print(df)
df['id'] = pd.Series(['id1', 'id2'], index=[0, 1])
print(df)
df.set_index('id', inplace=True)                                        # 设置新的索引
echo('新索引:', df)

"""
    数据预处理
        索引,组装(合并,堆叠),计算,排序
"""
echo("数据预处理")

"""    多级索引    MultiINdex  单词 Multi 多个 """
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

echo('concat 堆叠')
data_a = pd.DataFrame(get_area(5))
data_b = pd.DataFrame(get_area(3))
print(pd.concat([data_a, data_b]))                  # concat([data1,data2...], axis) 堆叠数据
print(pd.concat([data_a, data_b], axis=1))
all_data = data_a._append(data_b)
echo('append追加:', all_data)                     # _append() 追加

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
all_data = pd.merge(data_a, data_b, how='inner', on='datetime')
echo('merge合并:', all_data)
all_data.set_index('datetime')
print(all_data.loc[:'2020-09-11'])              # 时间为索引

data_a = pd.DataFrame({
    'datetime': date_list,
    'turnover': np.random.randint(10000, 10010, 4),
})
data_b = pd.DataFrame({
    'datetime': date_list,
    'maolilv': np.random.uniform(0.25, 0.28, 4)
})
echo(data_a, "排序:", data_a.sort_values('turnover', ascending=False))     # 按列排序,ascending 是否正序
all_data = pd.merge(data_a, data_b, how='inner', on='datetime')

"""查找不重复的值"""
echo("重复值")
area_A = pd.DataFrame(get_area(30))
print(area_A.head())
print(area_A['turnover'].unique())                  # [12001 12000 12002 12004 12003]
print(area_A['turnover'].nunique())                 # 不重复值的个数
print(area_A['turnover'].value_counts())            # 所有值和重复次数组成的DataFrame
print(area_A['turnover'].value_counts().values)     # 重复次数组成的列表
print(area_A['turnover'].value_counts().loc[12004]) # 获取某个重复值的次数


"""分列"""
data_a = pd.DataFrame({
    'datetime': np.arange('2020-09', '2022-09', dtype='datetime64[M]'),
    'turnover': np.random.randint(1000, 1200, 24),
    'maolilv': np.random.uniform(0.25, 0.28, 24)
})
data_b = pd.DataFrame((x.__str__().split("-") for x in data_a['datetime']), index=data_a['datetime'], columns=['year', 'month', 'day'])
data_c = pd.DataFrame(data_b['year'].str[2:])
echo('分列', data_b, data_c)


"""
    数据筛选
    &   |   !=
"""
echo('数据筛选')
echo(data_a.head(), data_a.loc[(data_a['turnover'] > 1100) & (data_a['maolilv'] > 0.26), ['datetime','turnover']])
echo('筛选并计数', data_a.loc[(data_a['turnover'] < 1100), ['datetime', 'maolilv']].maolilv.count())
echo('query筛选,并求平均值', data_a.query('datetime > "2021-09"').turnover.mean())

"""
    数据汇总
"""
echo("数据汇总")
def get_turnover(area_name):
    df_turnover = pd.DataFrame({
        'area_name': [area_name] * 20,
        'datetime': np.arange('2018-10-10', '2018-10-30', dtype='datetime64[D]'),
        'turnover': np.random.randint(12000, 16000, 20),
        'maolilv': np.random.uniform(0.25, 0.29, 20)
    })
    df_turnover.set_index('datetime', inplace=True)
    df_maolilv = pd.DataFrame((df_turnover['turnover'] * df_turnover['maolilv']), columns=['maolie'])
    df = pd.merge(df_turnover, df_maolilv, how='inner', on="datetime")
    return df
hy_df = get_turnover('huayu')
ddl_df = get_turnover('ddl')
df = hy_df._append(ddl_df)
echo('分组计数:',df.groupby('area_name').turnover.count())
echo('平均值:',df.groupby('area_name').mean())
echo("求和:",df.groupby('datetime').sum())
echo("中位数:", df.groupby('area_name').median())
print(df.groupby('area_name').describe())                       # 数据描述  单词:describe 描述
describe_T = df.groupby('area_name').describe().transpose()     # 转置数据
print(describe_T.round(2))
echo(describe_T['huayu'], describe_T['huayu'].loc['turnover', 'mean'])


"""
    数据统计/分析
"""
echo("数据分析")
echo('数据采样',df.sample(n=8).round(2))
print('毛利额与毛利率的协方差:', df['maolie'].cov(df['maolilv']).round(2))
print("营业额与毛利额的相关性:", df['turnover'].corr(df['maolie']).round(2))
echo("遍历pandas")
for index,values in df.iterrows():
    print('星期',index.weekday()+1,':', values['turnover'])

print('运行耗时:',WDate.run_time())