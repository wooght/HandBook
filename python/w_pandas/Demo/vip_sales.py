# -- coding: utf-8 -
"""
@project    :HandBook
@file       :vip_sales.py
@Author     :wooght
@Date       :2024/4/11 15:01
@Content    :门店VIP消费分析案例
"""

import pandas as pd
import numpy as np
from wooght_tools.echo import echo
from wooght_tools.DateTimeMath import WDate
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']

vip_sale_table = pd.read_excel('exls/会员消费报表.xlsx')
store_table = pd.read_excel('exls/门店信息表.xlsx')
vip_table = pd.read_excel('exls/会员信息查询.xlsx')
print(vip_sale_table)
print(store_table.to_string())                                          # 输出全部数据
print(vip_table)
echo('读取数据耗时:', WDate.run_time())
print(vip_sale_table.columns.values)
store_vip_sale = pd.merge(vip_sale_table, store_table, on='店铺代码')
print(store_vip_sale.columns.values)
echo('merge耗时:', WDate.run_time())

"""透视--商圈级别-会员消费趋势对比"""
# level:程度,等级   trend:趋势
level_trend = store_vip_sale.pivot_table(values='消费金额', index=['订单日期'], columns=['商圈等级描述'], aggfunc='sum')
level_trend.cumsum().plot(kind='line')                             # cumsum() 默认返回每一列的累加DataFrame,不改变原来结构
plt.show()

"""透视--商圈级别-性别消费对比"""
# whole: 整个,完整,整体
whole_vip_sale = pd.merge(store_vip_sale, vip_table, left_on='卡号', right_on='会员卡号')
gender_trend = whole_vip_sale.pivot_table(values='消费金额', index=['商圈等级描述'], columns=['性别'], aggfunc='sum')
gender_trend['total'] = gender_trend.sum(axis=1)
print(gender_trend)
gender_trend['man_percent'] = gender_trend['男'].div(gender_trend['total'])
gender_trend['woman_percent'] = gender_trend['女'].div(gender_trend['total'])
gender_trend[['man_percent', 'woman_percent']].plot(kind='bar', title='商圈-性别消费对比', legend=True, grid=True)
plt.show()

"""透视--每月新增会员统计"""
vip_table['month'] = vip_table['注册时间'].apply(lambda x:x.strftime('%Y-%m'))
vip_pivot = vip_table.pivot_table(values='会员卡号', index=['month'], columns=['会员等级'], aggfunc='count')
print(vip_pivot)
fig, ax = plt.subplots(figsize=(10,8), dpi=100)
ax2 = ax.twinx()                                                    # 构建双Y轴坐标系,及双胞胎坐标系
vip_pivot[['白银会员', '黄金会员']].plot(ax=ax, legend=True, ylabel='白银黄金', grid=True)
vip_pivot[['钻石会员', '铂金会员']].plot(ax=ax2, kind='bar', ylabel='钻石铂金')
ax2.legend(loc='upper left')
plt.show()
vip_pivot['total'] = vip_pivot.sum(axis=1)                           # sum(axis=1) 求列上的和,及每一行上求每一列的和
print(vip_pivot)
vip_pivot['黄金占比'] = vip_pivot['黄金会员'].div(vip_pivot['total'])   # df.div(df1) 返回df/df1的值,及求占比
vip_pivot['黄金占比'].plot()
plt.show()

"""会员来源与店铺等级关系"""
vip_table.rename(columns={'所属店铺编码':'店铺代码'}, inplace=True)
print(vip_table)
vip_store_table = pd.merge(vip_table, store_table, on='店铺代码')
vip_store_pivot = vip_store_table.pivot_table(values='会员卡号', index=['商圈类别描述'], columns=['会员来源'], aggfunc='count')
print(vip_store_pivot)
vip_store_pivot.plot(kind='bar', grid=True, legend=True)
plt.show()