# -*- coding: UTF-8 -*-
#
# Seaborn科学绘图工具之bar图
# matplotlib
# numpy
# by wooght 2017-11
#
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
plt.rc('font', family='SimHei', size=13)

num = np.array([13325, 9403, 9227, 8651])
ratio = np.array([0.75, 0.76, 0.72, 0.75])
men = num * ratio
women = num * (1-ratio)
x = ['聊天','支付','团购\n优惠券','在线视频']

width = 0.5
idx = np.arange(len(x))
plt.bar(idx, women, width, bottom=men, color='yellow', label='女性用户')  #这一块可是设置bottom,top，如果是水平放置的，可以设置right或者left。
plt.bar(idx, men, width, color='red', label='男性用户')                   #width 之bar的宽度比例

plt.xlabel('应用类别')
plt.ylabel('男女分布')
plt.xticks(idx, x, rotation=40)     #设置X坐标,idx指坐标的位置,rotation指旋转角度
plt.legend()    #显示图例
plt.show()


#seaborn 之barplot
f, ax=plt.subplots(figsize=(12,20))
sub_area = np.array(['cd','cq','sh','bj','sz','gz','wh'])
price_doc = np.array(['95','97','103','109','104','102','99'],dtype=int)
#orient='h'表示是水平展示的，alpha表示颜色的深浅程度
sns.barplot(y=sub_area, x=price_doc,orient='x', alpha=0.7, color='red')

#设置y轴、X轴的坐标名字与字体大小
plt.ylabel('price_doc', fontsize=16)
plt.xlabel('sub_area', fontsize=16)

#设置X轴的各列下标字体是水平的
plt.xticks(rotation='horizontal')

#设置Y轴下标的字体大小
plt.yticks(fontsize=15)
plt.show()
