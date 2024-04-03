# -- coding: utf-8 -
"""
@project    :HandBook
@file       :FuncPandas.py
@Author     :wooght
@Date       :2024/4/2 20:34
@Content    : pandas 函数应用
"""
import pandas as pd
import numpy as np
from wooght_tools.echo import echo
from wooght_tools.DateTimeMath import WDate
import matplotlib
"""
    创建->清洗->预处理->提取->筛选->汇总->统计
"""
def get_turnover(area_name, start_date, end_date):
    cha_date = np.datetime64(end_date) - np.datetime64(start_date)
    df_turnover = pd.DataFrame({
        'area_name': [area_name] * cha_date.astype('i2'),
        'datetime': np.arange(start_date, end_date, dtype='datetime64[D]'),
        'turnover': np.random.randint(12000, 16000, cha_date.astype('i2')),
        'maolilv': np.random.uniform(0.25, 0.29, cha_date.astype('i2'))
    })
    df_turnover['date'] = df_turnover['datetime']
    df_turnover.set_index('datetime', inplace=True)
    df_maolilv = pd.DataFrame((df_turnover['turnover'] * df_turnover['maolilv']), columns=['maolie'])
    df = pd.merge(df_turnover, df_maolilv, how='inner', on="datetime")
    return df

"""
    日期
"""
hy_df = get_turnover('huayu', '2020-10-01', '2021-02-02')
print(hy_df.head())
for key, values in hy_df.iterrows():
    if key.is_month_end: print(key.date(), key.time(), key.month, key.day, key.weekday())
print("闰年" if hy_df.loc['2020-10-10'].date.is_leap_year else "平年")
print("本月最大的日期:", hy_df.loc['2020-10-10']['date'].daysinmonth)
print("本年第",  hy_df.loc['2020-10-10']['date'].dayofyear, '天')


hy_dict = hy_df.head().to_dict()
for values in hy_dict.values():
    print(values)
#
# hy_df['turnover'].hist()
turnover_list = hy_df['turnover'].to_list()
maolilv_list = hy_df['maolilv'].round(2).to_list()
echo(turnover_list, maolilv_list)
print(WDate.run_time())