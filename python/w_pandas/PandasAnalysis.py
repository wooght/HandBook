# -- coding: utf-8 -
"""
@project    :HandBook
@file       :PandasAnalysis.py
@Author     :wooght
@Date       :2024/4/3 17:03
@Content    :分析操作
"""
import pandas as pd
import numpy as np
from wooght_tools.echo import echo
from wooght_tools.DateTimeMath import WDate

echo("创建数据")
turnover_1 = pd.read_excel('csv_file/202404021715.xls')
turnover_2 = pd.read_excel('csv_file/202404021717.xls')
echo('数据信息',turnover_1.size, turnover_1.index, turnover_1.shape)
echo('数据信息',turnover_2.size, turnover_2.index, turnover_2.shape)
print(turnover_1.columns)


def delete_columns(object):
    object.rename(columns={'订单号': 'code_nb', '商品名称': 'good_name', '商品数量': 'good_nums',
                           '商品金额': 'good_money', '结账时间': 'order_date', '订单金额': 'order_money'}, inplace=True)
    object.drop(['上传时间', '订单状态', '收银员', '自动抹零金额', '应收金额', '支付方式',
                 '找零金额', '减免', '优惠合计', '优惠名称', '优惠金额', '支付金额'], axis=1, inplace=True)
    # object.dropna(axis=0, inplace=True)

echo("数据清洗")
delete_columns(turnover_1)
delete_columns(turnover_2)
print(turnover_1)

echo("预处理")
all_data = pd.concat([turnover_1, turnover_2])
all_data.reset_index(inplace=True)
echo('组装后数据:', all_data, all_data.shape)
date_df = pd.DataFrame((x.__str__().split(' ') for x in all_data['order_date']), columns=['date', 'time'], index=all_data.index)
echo('日期序列:',date_df)
date_df.replace('nan', None, inplace=True)
all_data = pd.merge(all_data, date_df, how='left', on=all_data.index)
print(all_data.iloc[0, :])
print(all_data.count())
print(all_data[all_data['order_date'].isnull()].iloc[0, :])     # 输出第一行order_date为None的值
print(all_data['date'].unique())                                # 唯一项

echo("数据汇总")

date_code_nb = all_data['date'].value_counts().sort_index()     # 计数,并对索引进行排序
result_df = pd.DataFrame(date_code_nb.values, index=date_code_nb.index, columns=['orders'])
echo('日期-订单序列:', date_code_nb)
by_date_df = all_data.groupby('date')                           # 分组
print(by_date_df.describe().transpose())                        # 整体汇总

print('每日平均单价:', by_date_df['order_money'].mean())

print("每日销售额:", by_date_df['order_money'].sum())

print("每日销售商品数量:", by_date_df['good_nums'].sum())
print("未计算到的商品:", all_data[all_data['date'].isnull()]['good_nums'].sum())
result_df['order_mean'] = by_date_df['order_money'].mean().values

all_data['date'] = pd.to_datetime(all_data['date'])

all_data.ffill(inplace=True)            # 向前填充
day_goods = all_data.groupby('date').good_nums.sum().astype(int)
echo('每日销售数量(所有商品):', day_goods)
day_order_good_nums = pd.DataFrame(day_goods.values/by_date_df['good_nums'].count().values, index=day_goods.index)
echo("每日订单平均商品数量:",day_order_good_nums)
echo('平均订单商品数量:', all_data.groupby('code_nb').good_nums.sum().mean())

result_df['good_nums'] = day_goods
result_df['good_mean'] = day_order_good_nums
result_df['orders_mean_5'] = result_df['orders'].rolling(window=5, min_periods=1).mean()       # 滚动窗口求移动平均值
print(result_df)

result_df['date'] = result_df.index
ymd = pd.DataFrame((x.split('-') for x in result_df['date']), index=result_df.index, columns=['year', 'month', 'day'])
result_df = pd.merge(result_df, ymd, how='left', on=result_df.index)
result_df.drop('key_0', axis=1, inplace=True)
result_df['month'] = result_df['year'] + result_df['month']
result_df['orders_month_mean'] = 0
orders_month_mean = result_df.groupby('month').orders.mean()
print(orders_month_mean)

result_df['orders_month_mean'] = result_df['month'].apply(lambda x:orders_month_mean.loc[x])
print(result_df)

echo(str(WDate.run_time()))