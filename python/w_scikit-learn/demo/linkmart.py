# -- coding: utf-8 -
"""
@project    :HandBook
@file       :linkmart.py
@Author     :wooght
@Date       :2024/4/17 16:33
@Content    :linkmart 数据回归分析
"""
from wooght_tools.DateTimeMath import WDate
import w_pandas.Demo.db as db
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
from wooght_tools.echo import echo
from matplotlib import pyplot as plt

"""获取天气数据"""
weather_xls = pd.read_excel('exls/weather.xlsx')
weather_xls['date'] = weather_xls['日期'].apply(lambda x: x.split(' ')[0])
weather_xls['date'] = pd.to_datetime(weather_xls['date'])
print(weather_xls['date'].dtypes)
weather_xls['air_score'] = weather_xls['空气质量指数'].apply(lambda x: x.split(' ')[0])
weather_xls['max_t'] = weather_xls['最高温'].apply(lambda x: int(x.strip('°')))
weather_xls['min_t'] = weather_xls['最低温'].apply(lambda x: int(x.strip('°')))
# weather_xls.set_index('date', inplace=True, drop=True)      # drop是否删除原来的列
print(weather_xls.to_string())
print(weather_xls.iloc[0].name)     # 对应的index的值

"""获取营业数据"""
turnover_select = db.bs_data.select().filter(
    db.bs_data.c.date >= weather_xls.iloc[0].date,
    db.bs_data.c.store_id == 1
)
turnover_pd = pd.read_sql(turnover_select, db.connect)
turnover_pd['date'] = pd.to_datetime(turnover_pd['date'])
turnover_pd.sort_values('date', inplace=True)
# turnover_pd.set_index('date', inplace=True, drop=True)
print(turnover_pd)


all_data = pd.merge(weather_xls, turnover_pd, on='date')
all_data.sort_values('max_t', inplace=True)
# all_data = all_data[all_data['air_score'] != '-']
all_data.replace({'air_score': '-'}, 0, inplace=True)       # 将-替换为0
all_data['air_score'] = all_data['air_score'].astype(int)
all_data.replace({'air_score': 0}, all_data[all_data['air_score']>0]['air_score'].mean(), inplace=True)
all_data.sort_values('min_t', inplace=True)
print(all_data.head().to_string())

echo('最高温度相关度:', all_data['turnover'].corr(all_data['max_t']))
echo('最低温度相关度:', all_data['turnover'].corr(all_data['min_t']))
echo('空气质量相关度', all_data['turnover'].corr(all_data['air_score']))


"""最低温度回归模型"""
reg = linear_model.LinearRegression()
reg.fit(all_data['min_t'].to_numpy().reshape(-1, 1), all_data['turnover'].to_numpy().reshape(-1, 1))    # reshape(-1,1) 转置
echo('系数', reg.coef_, '常数', reg.intercept_)
x_test = np.linspace(1, 30, 30)
y_predict = reg.predict(x_test.reshape(-1, 1))

fig, ax = plt.subplots()
ax.scatter(all_data['min_t'].to_numpy(), all_data['turnover'].to_numpy())
ax.plot(x_test, y_predict)
plt.show()

"""取样,判断R2"""

echo('运行时间:' + str(WDate.run_time()))
