# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BasePlt.py
@Author     :wooght
@Date       :2024/4/4 18:11
@Content    :Matplotlib 基础
"""
from matplotlib import pyplot as plt
import numpy as np
import math
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']   # 设定中文字体
"""
    figure(figsize,dpi,facecolor,edgecolor,linewidth)
        figsize 画布size, 单位英寸
        dpi 分辨率
        facecolor   背景颜色
        edgecolor   边框颜色
        linewidth   边框宽度
"""
fig = plt.figure(figsize=(10, 8))

"""
    Axes(left,bottom;width*height)  轴类图像区域,left,bottom为在画布中的位置,width,height为画布大小的比例
    add_axes((left,bottom,width,height))    添加图像区域
"""
ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))     # 添加轴坐标
x = np.arange(0, math.pi * 4, 0.01)
y = np.sin(x)

"""
    绘制线条    单词:plot 绘制(线条)
    plot(x,y,color,alpha,linestyle(ls),linewidth(lw),marker,markersize(ms))
"""
y2 = np.cos(x)
ax.plot(x, y)
ax.plot(x, y2, color='blue', linestyle='--', lw=1)
ax.set_title('三角函数曲线')            # 图标信息设置
ax.set_xlabel('angle-角')
ax.set_ylabel('sin/cos')
"""
    legend(lables,loc)  添加图例说明  单词:legend 说明
            loc:位置(best,upper right,upper light,lower left,lower right right,center left...)
"""
ax.legend(labels=['sinx', 'cosx'], loc='best')
plt.show()                            # 显示

"""
    subplot(rows,cols,index)    创建子图
    如果3个参数都小于10,那么subplot(3,3,3)和subplot(333)等价
"""
# fig2 = plt.figure(figsize=(8, 10))
ax1 = plt.subplot(2, 1, 1)
ax1.plot(range(10))
ax2 = plt.subplot(212, facecolor='y')
ax2.plot(range(10), color='g')
plt.show()

"""
    subplots(rows,cols) 创建多个子图
"""
fig, axlist = plt.subplots(2, 2)
print(fig)
x = np.arange(1, 10)
axlist[0][0].grid(True)             # axes.grid() 设置网格
axlist[0][0].plot(x, x * x)
axlist[0][1].plot(x, np.exp(x))
axlist[1][0].plot(x, np.sqrt(x))
axlist[1][1].plot(x, np.log(x), 'o:r')  # 'o:r' 为fmt定义样式的方式 三个位置分别为:market,line,color
plt.show()
"""
    fmt参数定义基本格式
    market: .点标记    ,像素     o圆形标记   ^上三角标记  S正方形    P五角星    D砖石 d小钻石
    line:   solid   -   实线
            dashed  --  虚线
            dashdot -.  点线
            dotted  :   点虚线
    color:  b blue      g green     r red       c cyan(青色)  m magenta(品红)   y yellow    k black     w white
"""

"""
    设置轴标签
"""
fig = plt.figure(figsize=(10, 8))
ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))
x = np.arange(1, 10)
ax.plot(x, x ** 2)
ax.set_xlabel(xlabel='x', rotation=0, fontdict={'fontsize': 16, 'fontweight': 'bold', 'color': 'red'})
ax.set_ylabel(ylabel='y', rotation=45, labelpad=20)
ax.set_title(label='图标标题', fontdict={'fontsize':16, 'color':'blue'},loc='center', pad=10)
plt.show()

"""
    柱状图
"""
x = np.array(['China', 'USA', 'EN', 'Ru'])
y = np.array([5000, 300, 3000, 2500])
fig = plt.figure(figsize=(10, 8))
ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))
ax.bar(x, height=y)
ax.set_title('各国历史')
ax.set_xlabel(xlabel='国家')
ax.set_ylabel(ylabel='年份')
plt.show()

"""
    两组label柱状图
"""
y2 = np.array([960, 930, 70, 1700])
fig = plt.figure(figsize=(10,9))
ax = fig.add_axes((0.1,0.1,0.8,0.8))

xlabel = np.arange(len(x))
width = 0.4

lab1 = ax.bar(x=xlabel-width/2, height=y, width=width, label='历史')
ax.bar_label(lab1)
lab2 = ax.bar(x=xlabel+width/2, height=y2, width=width, label='国土')
ax.bar_label(lab2)

ax.set_xticks(xlabel)   # 设置X坐标值
ax.set_xticklabels(x)   # 设置X坐标标签

ax.legend(loc='best', fontsize=16)
plt.show()

"""
    横向条形图
"""
fig = plt.figure(figsize=(10,8))
ax = fig.add_axes((0.1,0.1,0.8,0.8))
ax.barh(x, height=0.5, width=y, color=['r', 'b', 'g', 'y'])
plt.show()

"""
    散点图/气泡图
"""
fig = plt.figure(figsize=(10,8))
ax = fig.add_axes((0.1,0.1,0.8,0.8))
nums = 100
x = np.random.rand(100)
y = np.random.rand(100)
colors = np.random.rand(100)
areas = (np.random.rand(100)*10)**2
ax.scatter(x,y,c=colors, s=areas, alpha=0.5)
plt.show()