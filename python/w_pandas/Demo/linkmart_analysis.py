# -- coding: utf-8 -
"""
@project    :HandBook
@file       :linkmart_analysis.py
@Author     :wooght
@Date       :2024/4/7 19:57
@Content    :分析实例
"""
import db
import pandas as pd
from wooght_tools.DateTimeMath import WDate
from wooght_tools.echo import echo
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']   # 设定中文字体


# import warnings
# warnings.simplefilter(action='error', category='PerformanceWarning')

"""获取商品"""
goods_select = db.goods_list.select()
goods = db.connect.execute(goods_select)
print(goods.rowcount)                                       # 获取结果条数
goods_df = pd.DataFrame(goods)
hy_goods = goods_df[goods_df['store_id'] == 1].copy()       # 条件筛选结果是应用,copy后才能赋新值
echo('华宇商品均价:',hy_goods['price'].mean(),'库存成本:', (hy_goods['stock_nums'] * hy_goods['cost']).sum())
hy_goods.drop_duplicates(subset=['bar_code'], keep='last', inplace=True)
hy_goods.set_index('bar_code', inplace=True)
print(hy_goods)
print(hy_goods.loc['6941254707854'])

"""获取订单"""
order_select = db.order_form.select().filter(db.order_form.c.form_date >= '2023-12-01',db.order_form.c.store_id == 1)
orders = pd.read_sql(order_select, db.connect)
echo('用时:'+str(WDate.run_time()))

orders.sort_values(by='form_date', inplace=True)

"""订单分类广播"""
hy_goods_code = hy_goods.index.values
orders['classify'] = orders['goods_code'].apply(lambda x: hy_goods.loc[x]['classify'])
orders['cost'] = orders['goods_code'].apply(lambda x: hy_goods.loc[x]['cost'])
orders['cost_percent'] = 1 - (orders['cost'] / (orders['goods_money'] / orders['goods_num'])).round(2)

"""判断语句耗时较多,这里1万条约多10秒"""
# orders['classify'] = orders['goods_code'].apply(lambda x:hy_goods.loc[x]['classify'] if x in hy_goods_code else None)
"""原生加新赋值耗时较多,这里1万条约多2秒"""
# orders_classify = []
# for index, row in orders.iterrows():
#     orders_classify.append(hy_goods.loc[row.goods_code]['classify'] if row.goods_code in hy_goods_code else None)
# orders['classify'] = orders_classify

"""按分类分组"""
by_classify = orders.groupby('classify')
classify_orders = by_classify.agg({'goods_num':'sum', 'goods_money':'sum', 'cost_percent':'mean'})     # agg 给定字典,调用多个聚合函数
classify_orders.sort_values('goods_num', inplace=True)
echo('分类总销量:', classify_orders)
echo('中烟实际毛利率:', classify_orders.loc['中烟']['cost_percent'].round(4), '川烟实际毛利率',classify_orders.loc['川烟']['cost_percent'])

"""透视表获取分类每天销量"""
echo('用时:'+str(WDate.run_time()))
pivot_table = orders.pivot_table(values='goods_num', index=['form_date'], columns=['classify'], aggfunc='sum')
echo('透视表获取分类每天销量:',pivot_table)

"""分组每个类别每天销量"""
turnover_temp = {}
for classify in classify_orders.index.values:
    """
        对所有orders中找到某一特定的类,然后进行日期分组,就得到基于日期的某类销量
        如果某一类某一天没有销量,那么就会缺少那个日期,所以这里直接用DataFrame就会出现行数不一样的情况,就无法确定DataFrame的行数
    """
    turnover_temp[classify] = orders[orders['classify'] == classify].groupby('form_date')['goods_num'].sum()
classify_turnover = pd.DataFrame(turnover_temp)
echo('传统方法获取分类每天销量:',classify_turnover)
"""pandas 会自动将date,time,datetime的字符串数据转换为datetime数据,所以不能用时间字符串去匹配"""
classify_turnover.drop(labels=pd.to_datetime(['2024-04-06', '2024-04-07']), axis=0, inplace=True)
classify_turnover.fillna(0, inplace=True)
print(classify_turnover)

"""获取营业额数据"""
turnover_select = db.bs_data.select().filter(db.bs_data.c.date >= '2023-12-01', db.bs_data.c.store_id ==1)
turnover_df = pd.read_sql(turnover_select, db.connect)
turnover_df.set_index('date', inplace=True)
turnover_df['profit_rate'] = turnover_df['gross_profit'] / turnover_df['turnover']      # 毛利率
all_data = pd.merge(turnover_df, classify_turnover, on=classify_turnover.index, how='left')
all_data.set_index('key_0', inplace=True)
echo('GMV及分类数据:', all_data)

"""计算烟占比 单词:proportion 占比"""
all_data['gross_nums'] = orders.groupby('form_date')['goods_num'].sum()                 # 每天总销量
all_data['smoke_ppt'] = (all_data['中烟'] + all_data['川烟']) / all_data['gross_nums']   # 香烟占比
"""绘制占比图"""
fig, ax = plt.subplots()
ax.plot(all_data.index, all_data['smoke_ppt'])
plt.show()

"""相关度计算"""
classify_corr = pd.DataFrame()
for classify in classify_turnover.columns.values:
    try:
        classify_corr[classify] = [all_data['turnover'].cov(all_data[classify].round(2)),
                                   all_data['turnover'].corr(all_data[classify].round(2)),
                                   all_data['profit_rate'].corr(all_data[classify]).round(2)]
    except pd.errors.PerformanceWarning:
        print(classify)
classify_corr['name'] = ['classify_cov', 'classify_corr', 'profit_rate']
classify_corr.set_index('name', inplace=True)
print(classify_corr)

"""转轴,方便排序"""
classify_corr_t = classify_corr.transpose()
classify_corr_t = pd.merge(classify_corr_t, classify_orders['goods_num'], on=classify_corr_t.index, how='inner')
classify_corr_t.sort_values('classify_corr', inplace=True)
classify_corr_t.set_index('key_0', inplace=True)    # merge会把on对应的column变成key_0
echo('相关性最终报表:', classify_corr_t)

"""相关性绘图"""
fig, (ax, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(10, 10))
fig.subplots_adjust(wspace=0)
ax.barh(y=classify_corr_t.index.values, width=classify_corr_t['classify_corr'])
ax.set_title('营业额-类别销量相关度')
plt.yticks(rotation=0, fontsize=8)
ax2.barh(y=classify_corr_t.index.values, width=classify_corr_t['goods_num'])
ax2.set_xlim(0, 200)
ax2.axis('off')
ax2.set_title('分类销量')
ax3.barh(y=classify_corr_t.index.values, width=classify_corr_t['profit_rate'])
ax3.set_title('类别销量-毛利率相关度')
plt.show()


"""获取二年营业额"""
two_years = np.datetime64('today', format('D')) - 730
turnover_select = db.bs_data.select().filter(db.bs_data.c.date > two_years, db.bs_data.c.store_id == 1)
turnover_df = pd.read_sql(turnover_select, db.connect)
turnover_df.sort_values('date', inplace=True)

turnover_df['mean_30'] = turnover_df['turnover'].rolling(window=30, min_periods=1).mean()       # 30日平均值
turnover_df['month'] = turnover_df['date'].apply(lambda x:str(x.year)+str('%02d' % x.month))    # 组装年月,月不足2位0补位
turnover_month_mean = turnover_df.groupby('month')['turnover'].mean()                           # 月平均值
turnover_df['month_mean'] = turnover_df['month'].apply(lambda x:turnover_month_mean.loc[x])     # 广播月平均值
print(turnover_df)
print(turnover_month_mean)
"""会走势图"""
fig, ax= plt.subplots(figsize=(10,6))
ax.bar(x=turnover_df['date'], height=turnover_df['turnover'])
ax.plot(turnover_df['date'], turnover_df['mean_30'], color='r')
ax.plot(turnover_df['date'], turnover_df['month_mean'], color='c')
plt.show()

"""
    天气分析
"""
weather_xls = pd.read_excel('exls/weather.xlsx')
print(weather_xls)

print(WDate.run_time())