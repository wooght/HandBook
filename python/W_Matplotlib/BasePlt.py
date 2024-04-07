# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BasePlt.py
@Author     :wooght
@Date       :2024/4/4 18:11
@Content    :Matplotlib 基础
"""
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.patches import ConnectionPatch
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
fig.subplots_adjust(wspace=0)       # 多个子图之间无间距
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
    层叠柱状图
"""
personnel = pd.DataFrame({
    'age_interval': ['<22', '22-30', '30-35', '35-50'],
    'php_percent': [9, 36, 28, 27],
    'python_percent': [7, 42, 37, 14],
    'C_percent': [3, 26, 29, 42]
})
fig = plt.figure(figsize=(10, 8))
ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))
bottom = np.zeros(4)
for column_name in personnel.columns[1:]:
    bar1 = ax.bar(x=personnel['age_interval'], height=personnel[column_name],
                  bottom=bottom, label=column_name)
    ax.bar_label(bar1, label_type='center')
    bottom += personnel[column_name]
ax.legend(loc='best')
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
print(colors)
areas = (np.random.rand(100)*10)**2
ax.scatter(x,y,c=colors, s=areas, alpha=0.5)
plt.show()


import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from matplotlib.patches import ConnectionPatch

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']   # 设定中文字体
"""
    饼状图
"""
cd_gdp = pd.DataFrame({
    'areas': ['锦江区', '成华区', '金牛区', '青羊区', '武侯区'],
    'gdp': [1730, 1690, 1890, 1840, 1750]
})
print(cd_gdp)
fig = plt.figure(figsize=(10, 8))
ax = fig.add_axes((0.1, 0.1, 0.9, 0.9))
"""
    autopct 饼图显示格式  %d%%整数百分数,  %0.2f%% 两位小数百分数
    radius  饼图的半径
    explode 数组,和下一个扇形之间的距离
    startangle  起始角度,默认0度
    counterclock    默认true,逆时针, false为顺时针
"""
ax.pie(x=cd_gdp['gdp'], labels=cd_gdp['areas'], autopct='%1.2f%%', radius=0.8, explode=[0.1, 0, 0, 0, 0.1],
       colors=['r', 'b', 'g', 'y', 'm'])
plt.show()

"""
    嵌套图
"""
educational = pd.DataFrame({
    'xx': [8000, 12000, 14000, 8000, 9000],
    'zx': [12000, 14000, 18000, 11000, 11500],
    'dx': [30000, 29000, 27000, 30500, 29500],
    'yjs': [3000, 1200, 1300, 2900, 2100]
})
all_df = cd_gdp.merge(educational, how='inner', on=cd_gdp.index)
print(all_df)
"""创建画布"""
fig, (ax1, ax2) = plt.subplots(1, 2)
fig.subplots_adjust(wspace=0)
"""绘制左边圆饼图"""
left_ax = ax1.pie(x=all_df['gdp'], labels=all_df['areas'], autopct="%1.2f%%", radius=1.1,
                  explode=[0, 0, 0, 0, 0.1], colors=plt.cm.rainbow(np.linspace(0, 1, 5)),
                  wedgeprops=dict(width=0.6, edgecolor='w'), startangle=35)
"""绘制右边柱状图"""
all_df.set_index('areas', inplace=True)
all_df.drop('key_0', inplace=True, axis=1)
new_df = all_df.transpose()
new_df.drop('gdp', axis=0, inplace=True)
new_df['bottom'] = new_df['武侯区'].cumsum() - new_df['武侯区']           # 计算起始高度
print(new_df)
label1 = ax2.bar(x='educational', height=new_df['武侯区'], width=.4,
                 bottom=new_df['bottom'], label=new_df.index,
                 color=plt.cm.rainbow(np.linspace(0,1,4)))
ax2.bar_label(label1, label_type='center')
ax2.legend()
ax2.axis('off')                                                         # 关闭坐标
ax2.set_title('区域学历占比')
ax2.set_xlim(-1, 1)                                                     # 设置x坐标轴的范围
"""绘制连接线"""
"""
    patches 饼图的扇形列表
    theta1,theta2 表示扇形的开始角度和结束角度,
    center表示扇形中心位置坐标[x,y], 如果没有偏移量,则为零 ,如果扇形与其他扇形有距离,则中心的位置发生偏移
"""
theta1, theta2 = ax1.patches[-1].theta1, ax1.patches[-1].theta2
print(theta1, theta2)
center, r = ax1.patches[-1].center, ax1.patches[-1].r
x = r * np.cos(np.pi / 180 * theta2) + center[0]
y = r * np.sin(np.pi / 180 * theta2) + center[1]

con1 = ConnectionPatch(xyB=(-.2, new_df['武侯区'].sum()),    # 连接线终点位置
                       xyA=(x, y),                      # 连接线起点位置
                       coordsA=ax1.transData,           # 起点位置坐标系
                       coordsB=ax2.transData,           # 终点位置坐标系
                       axesA=ax1, axesB=ax2)            # 起始点位于的子图
con1.set_color('gray')                                     # 连接线颜色
ax2.add_artist(con1)                                    # 添加连接线
con1.set_linewidth(4)                                   # 连接线宽度

x = r * np.cos(np.pi / 180 * theta1) + center[0]
y = r * np.sin(np.pi / 180 * theta1) + center[1]
con2 = ConnectionPatch(xyA=(-.2, 0),
                       xyB=(x, y),
                       coordsA=ax2.transData,
                       coordsB=ax1.transData,
                       axesA=ax2, axesB=ax1)

con2.set_color('gray')
ax2.add_artist(con2)
con2.set_linewidth(4)
plt.show()
#
# fig, ax = plt.subplots()
#
# size = 0.3
# vals = np.array([[60., 32.], [37., 40.], [29., 10.]])
#
# cmap = plt.colormaps["tab20c"]
# outer_colors = cmap(np.arange(3) * 4)
# inner_colors = cmap([1, 2, 5, 6, 9, 10])
#
# ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
#        wedgeprops=dict(width=size, edgecolor='w'))
#
# ax.pie(vals.flatten(), radius=1-size, colors=inner_colors,
#        wedgeprops=dict(width=size, edgecolor='w'))
#
# ax.set(title='Pie plot with `ax.pie`')
# plt.show()