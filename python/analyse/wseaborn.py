# -*- coding: UTF-8 -*-
#
# Seaborn科学绘图工具 依赖如下:
# matplotlib
# numpy,scipy
# by wooght 2017-11
#

# Numpy 重点是矩阵模块 N维数组容器
# pandas 重点是统计分析 表格容器 基于numpy
# Scipy 重点是抽象模型 计算函数库 基于numpy

import matplotlib as mpl
import matplotlib.pyplot as plt     #matplotlib.pyplot 绘图主键
import seaborn as sns
import numpy as np
import pandas as pd
import json

import time
import Db as T

mpl.rcParams['font.sans-serif'] = ['SimHei']    #指定默认字体 解决中文问题

# sns.set_style('whitegrid')      #设置主体 darkgrid , whitegrid , dark , white ,和 ticks
# plt.plot(np.arange(10))
# plt.show()

# sns.set(style="darkgrid",palette="muted",color_codes=True)
# plt.plot(np.arange(100))
# plt.show()


# x = np.random.normal(size=100)  #随机抽样,正太分布图
# print(x)
# plt.plot(x)
# plt.show()
#
# ts = pd.Series(np.random.randn(100), index=pd.date_range('9/9/2017', periods=100))
# ts = ts.cumsum()
# plt.plot(ts)
# plt.show()
#
# arr = np.ones((2,2))
# arr2 = np.eye(2)
# new_arr = (arr*2)*arr2**2
# plt.plot(new_arr)
# plt.show()
#
# dates = pd.date_range('20171101',periods=6)
# df = pd.DataFrame(np.random.randn(6,5),index=dates,columns=('a','b','c','d','e'))
# print(df)
# plt.plot(df)
# plt.show()

#查询新闻事件大于2011-09-01的所有数据
#提到360的加一
start_time = int(time.time())-24*3600*24
print(start_time,'---->')
query = T.session.query(T.news.c.url,T.news.c.put_time)
s = query.filter(T.news.c.title.like('%360%')).filter(T.news.c.put_time>start_time).all()
print(s)

#创建数据贴
dates = pd.date_range('20171103',periods=24)
df = pd.DataFrame(np.zeros((24,3)),index=dates,columns=('sina','yicai','qq'))
for item in s:
    numindex = time.strftime("%Y-%m-%d",time.localtime(int(item[1])))
    if('yicai' in item[0]):
        column='yicai'
    elif('sina' in item[0]):
        column='sina'
    else:
        column='qq'
    df.loc[numindex,column]+=1
print(df)                           #这里得到的是宽表格(透视表) 类十余课程表

#根据数据贴创建数据列表
df2 = df.copy()
df2['time'] = df.index               #DataFrame类型追加一列
df_list = []
for hang in df.index:
    for column in df.columns:
        df_list.append({'time':str(hang)[0:10],'from_name':column,'num':df.loc[hang,column]})
print(df_list)
list_df = pd.DataFrame(df_list)     #这里得到的是长表格
print(list_df)

#matplotlib原生 plot 折线图
def matplotlib_ys(df):
    plt.xlabel('Time')
    plt.ylabel('Num')
    plt.title('360上市报道',fontsize=16,color='red')
    plt.grid(True)                  #是否显示网格
    for i in df.columns:
        plt.plot(df.loc[:,[i]],label=i)
    plt.legend()                    #图例
    plt.show()
matplotlib_ys(df)

# fig,axes = plt.subplots(1,2)
# sns.kdeplot(df,ax=axes[0],shade=True)
# plt.show()

#统计都是按照列来统计

#boxplot 箱线图
def boxplot_ys(df):
    tips = sns.load_dataset("tips")
    # 绘制箱线图
    ax = sns.boxplot(x="day",y="total_bill",data=tips)
    plt.show()
# boxplot_ys(df)

#barplot 直方图,不分组则为平均值
def barplot_ys(d):
    sns.set(style="darkgrid",palette="muted",color_codes=True)
    plt.title('360 news average/day ')
    sns.barplot(data=d,ci=0)   #ci指上方的置信度线
    plt.plot(df)               #不显示   ??????
    plt.show()
# barplot_ys(df)
#barplot 分组
def barplot_ys2(d):
    sns.barplot(x='time',y='num',data=d,hue='from_name',ci=0)   #ci指上方的置信度线
    plt.plot(df)
    plt.show()
# barplot_ys2(list_df)

#countplot 统计计数 直方图
def countplot_ys(d):
    ax = sns.countplot(y='num',hue='from_name',data=list_df)
    plt.show()

#factorplot 因子变量-数值变量
def factorplot_ys():
    sns.set(style="ticks")
    exercise = sns.load_dataset("exercise")
    g = sns.factorplot(x="time", y="pulse", hue="kind",
                        data=exercise, kind="violin")
    print(exercise)
    plt.show()

#模拟数据
data = {
        'month':np.arange(12),                          #日期月
        'from_name':np.random.randint(1,2,size=12),     #来源
        'news':np.random.randint(20,50,size=12),        #新闻数
        'comments':np.random.randint(50,155,size=12)    #评论数
}
df_mn = pd.DataFrame(data)
print(df_mn)
#lmport 线性回归
def lmport_ys():
    tips = sns.load_dataset("tips")
    # g = sns.lmplot(x="news", y="comments",hue='from_name', data=df_mn,markers=["o", "x"])#markers分组用不同的符号表示
    # s = sns.lmplot(x="news", y="comments",col='from_name', data=df_mn) # col 分子图绘画
    s = sns.lmplot(x="news", y="comments",fit_reg=False,hue='from_name', data=df_mn)# fit_reg 是否花回归线
    plt.show()
lmport_ys()

#distplot 数值分布图 接受数组
def distplot_ys():
    sns.set(style="darkgrid",palette="muted",color_codes=True)
    ax = sns.distplot(list_df.loc[:,['num']],rug=True,hist=True) #直方图hist=True，核密度曲线rug=True
    plt.show()

# distplot_ys()

#jointplot 双变量关系图
sns.jointplot(x='news',y='comments',data=df_mn,kind="kde") #kind='reg' 绘制散点图和线性回归拟合直线,kind='kde'绘制核密度图
plt.show()

#线图
df_mn.pivot(index='month',columns='from_name',values='news').plot(title='报道量')  #columns 分组的意思
plt.show()

r = T.select([T.quotes_item.c.quotes]).where(T.quotes_item.c.code_id==2)
s = T.conn.execute(r)
for item in s.fetchall():
    obj = json.loads(item[0])

quotes = pd.DataFrame(obj)
quotes.index = quotes['datatime']   #将所有改为某列的值
print(quotes.info())
quotes = quotes.convert_objects(convert_numeric=True)   #小数有可能是obj类型 要运算就必须类型转换
print(quotes.info())
def quotes_ys(df):
    plt.xlabel('datatime')
    plt.ylabel('shou')
    plt.title('行情走势',fontsize=16,color='red')
    plt.grid(True)                  #是否显示网格
    plt.plot(df.loc[:,['shou','gao','di']])
    plt.legend()                    #图例
    plt.show()
quotes_ys(quotes.sort_index(axis=1,ascending=True))
newquotes = quotes.sort_values(by="datatime",ascending=True)
# quotes.shou = quotes.shou.astype(int)
# quotes.gao = quotes.gao.astype('int8')
sns.jointplot(x='shou',y='gao',data=quotes,kind="reg") #kind='reg' 绘制散点图和线性回归拟合直线,kind='kde'绘制核密度图
plt.show()
#涨跌幅 分布图
ax = sns.distplot(quotes.loc[:,['zd_range']],rug=True,hist=True)
try:
    plt.savefig("F:\homestead\caijing_lvl\public\seaborn_pic\sns.png")
    print('save SUCCESS')
except Exception as e:
    print('save dailed .....',e)
plt.show()

gammas = sns.load_dataset("gammas")
ax = sns.tsplot(time="timepoint", value="BOLD signal",unit="subject", condition="ROI",data=gammas, err_style="ci_bars")
plt.show()
print(gammas)
