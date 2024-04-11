# -- coding: utf-8 -
"""
@project    :HandBook
@file       :test.py
@Author     :wooght
@Date       :2024/4/11 16:49
@Content    :测试
"""
import pandas as pd
import numpy as np

classify = {
    '123': '默认分类',
    '124': '快消类'
}
bar_codes = np.array(list(classify.keys()))
print(bar_codes)

orders = pd.DataFrame({
    'date': np.arange('2020-10-01', '2020-10-10', dtype='datetime64[D]'),
    'bar_code': np.random.choice(bar_codes, 9),
    'moneys': np.random.uniform(10, 20, 9)
})
orders.loc[5, 'bar_code'] = 125
# orders.loc[5]['bar_code'] = 126   # 此方式为获取值
print(orders)

classify_df = pd.DataFrame(classify, index=[0])
classify_df_t = classify_df.transpose()
classify_df_t.rename(columns={0: 'name'}, inplace=True)
classify_df_t['bar_code'] = classify_df_t.index
print(classify_df_t)

"""merge合并,不一定必须两个长度相等,不等则会根据on值一一对应填充"""
all_data = pd.merge(orders, classify_df_t, on='bar_code', how='left')
print(all_data)

"""transform 是groupby后的广播功能,及将计算得到的值广播的每一行"""
all_data.dropna(axis=0, inplace=True)
all_data['类平均值'] = all_data.groupby('name')['moneys'].transform('mean')
print(all_data)
