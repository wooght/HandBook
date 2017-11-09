# -*- coding: UTF-8 -*-
#
# pandas
# by wooght 2017-11
#
import pandas as pd
import numpy as np
import matplotlib

import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

def fg(args=''):
    print('--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-',args)

fg('Series')
#Series 默认创建整数索引
s = pd.Series([1,3,5,np.nan,6,8])
print(s)

#指定索引
s=pd.Series([1,2,3,4],index=['a','b','c','d'])
print(s)

dict = {'b':2,'a':1,'c':3}
s = pd.Series(dict) #给定字典的时候,默认会排序
print(s)
print('b' in s)
print(s.isnull())
print(s.index)
print(s['b'])

fg('date_range')
#连续日期   range连续的意思  numpy中arange 连续数字
dates = pd.date_range('20171111',periods=6)   #如不指定日期,默认当前
print(dates)
for d in dates:
    print(d)

fg('数据贴')
#创建数据贴 生成日期索引和标记列
df = pd.DataFrame(np.random.randn(6,5),index=dates,columns=list(('one','two','three','four','five')))
print(df)
print(df.dtypes)    #输出每一行的类型

#使用 可转换序列的字典对象 创建数据贴
df2 = pd.DataFrame({
'A':'one',
'B':np.random.randn(3)  #故这里的数据贴是三行
})
print(df2)

fg('获取头,底')
#查看头部和底部行 默认为5行
print(df.head())
print(df.tail(3))

fg('获取行,列,序列')
print(df.index)         #index序列
print(df.columns)       #columns 列头 dtype=object
print(df.one)           #得到一列的值
print(df.values)        #值 二维

fg('describe快速统计摘要')
print(df.describe())

#数据转置 不改变对应关系
fg('转置')
print(df.T)

fg('排序')
#按轴排序 axis=0指横轴,1指纵轴
print(df.sort_index(axis=0, ascending=False))
#按值排序
print(df.sort_values(by='two',ascending=True))      #ascending True 为升,Flase为降

fg('标签取值')
print(df.loc[dates[0]]) #index 第0行 行切片
print(df.loc[:,['one']])    #取某一列 列切片
print(df.loc[dates[0]:dates[2],['two','five']])
print(df.loc['20171113':,['five']])
print(df.loc[dates[0],'one'])   #精确取某个值
fg('位置取值')
print(df.iloc[3])
print(df.iloc[[1,2],[0,2]])
print(df.iloc[:,[0]])
print(df.iloc[1,2])
fg('布尔索引')
print(df[df.three>0])
print(df[df>0])
df2 = df.copy()
df2['six'] = ['a','b','c','d','e','f']
print(df2[df2['six'].isin(['a','c'])])

ts = pd.Series(np.random.randn(100), index=pd.date_range('1/1/2000', periods=100))
print(ts)
ts = ts.cumsum()
ts.plot()
