# -- coding: utf-8 -
"""
@project    :HandBook
@file       :analysis.py
@Author     :wooght
@Date       :2024/4/7 19:57
@Content    :分析实例
"""
import db
import pandas as pd
from wooght_tools.DateTimeMath import WDate
from wooght_tools.echo import echo
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']   # 设定中文字体


# import warnings
# warnings.simplefilter(action='error', category='PerformanceWarning')

"""获取商品"""
goods_select = db.goods_list.select()
goods = db.connect.execute(goods_select)
print(goods.rowcount)                   # 获取结果条数
goods_df = pd.DataFrame(goods)
hy_goods = goods_df[goods_df['store_id'] == 1].copy()
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

"""订单分类"""
hy_goods_code = hy_goods.index.values
orders['classify'] = orders['goods_code'].apply(lambda x: hy_goods.loc[x]['classify'])

"""判断语句耗时较多,这里1万条约多10秒"""
# orders['classify'] = orders['goods_code'].apply(lambda x:hy_goods.loc[x]['classify'] if x in hy_goods_code else None)
"""原生加新赋值耗时较多,这里1万条约多2秒"""
# orders_classify = []
# for index, row in orders.iterrows():
#     orders_classify.append(hy_goods.loc[row.goods_code]['classify'] if row.goods_code in hy_goods_code else None)
# orders['classify'] = orders_classify

echo('用时:'+str(WDate.run_time()))
by_classify = orders.groupby('classify')
classify_orders = by_classify.agg({'goods_num':'sum', 'goods_money':'sum'})
classify_orders.sort_values('goods_num', inplace=True)
print(classify_orders)

"""每个类别每天销量"""
turnover_temp = {}
for classify in classify_orders.index.values:
    turnover_temp[classify] = orders[orders['classify'] == classify].groupby('form_date')['goods_num'].sum()
classify_turnover = pd.DataFrame(turnover_temp)
print(classify_turnover)
"""pandas 会自动将date,time,datetime的字符串数据转换为datetime数据,所以不能用时间字符串去匹配"""
classify_turnover.drop(labels=pd.to_datetime(['2024-04-06', '2024-04-07']), axis=0, inplace=True)
classify_turnover.fillna(0, inplace=True)
print(classify_turnover)


"""获取营业额数据"""
turnover_select = db.bs_data.select().filter(db.bs_data.c.date >= '2023-12-01', db.bs_data.c.store_id ==1)
turnover_df = pd.read_sql(turnover_select, db.connect)
turnover_df.set_index('date', inplace=True)
turnover_df['profit_rate'] = turnover_df['gross_profit'] / turnover_df['turnover']
all_data = pd.merge(turnover_df, classify_turnover, on=turnover_df.index, how='left')
print(turnover_df)

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
classify_corr_t.set_index('key_0', inplace=True)
print(classify_corr_t)

"""相关性绘图"""
fig, (ax, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(10,10))
fig.subplots_adjust(wspace=0)
ax.barh(y=classify_corr_t.index.values, width=classify_corr_t['classify_corr'])
ax.set_title('营业额-类别销量相关度')
plt.yticks(rotation=0, fontsize=8)
ax2.barh(y=classify_corr_t.index.values, width=classify_corr_t['goods_num'])
ax2.set_xlim(0,200)
ax2.axis('off')
ax2.set_title('分类销量')
ax3.barh(y=classify_corr_t.index.values, width=classify_corr_t['profit_rate'])
ax3.set_title('类别销量-毛利率相关度')
plt.show()

print(WDate.run_time())