# -- coding: utf-8 -
"""
@project    :HandBook
@file       :pandas_numpy_date.py
@Author     :wooght
@Date       :2024/4/20 20:54
@Content    :pandas,numpy 时间
"""
import pandas as pd
import numpy as np


days = np.arange('2019-01', '2021-09', dtype='datetime64[D]')
nums = np.random.uniform(1,100, days.shape[0])
df = pd.DataFrame({
    'date': days,
    'nums': nums
})
print(df)
df['year'] = df['date'].apply(lambda x:x.year)
df['year_month'] = df['date'].apply(lambda x:"%d-%02d" % (x.year, x.month))
print(df['date'].dtype)
df['date'].apply(lambda x:print(x.date()))
by_month = df.groupby('year_month').agg({'nums':'mean'})
print(by_month)

the_day = np.datetime64('2020-01-01', format('M'))
print(the_day.dtype)