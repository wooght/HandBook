# -- coding: utf-8 -
"""
@project    :HandBook
@file       :PicPlt.py
@Author     :wooght
@Date       :2024/6/6 16:18
@Content    :matplotlib 图片
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import ToolHandles
import mplcursors
from matplotlib.image import imread
from PIL import Image


x = np.linspace(0, 2*np.pi, 100)
print(x)
# y1 = np.sin(x)
# y2 = np.cos(x)
# fig, ax = plt.subplots()
# lin1 = ax.plot(x, y1, label='正弦曲线')
# lin2 = ax.plot(x, y2, label='余弦曲线')
#
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.legend()

path = 'pic/126.com_.png'
p_img = Image.open(path)
print(p_img.size)
# 加载图片
image = imread(path)

# 显示图片
plt.imshow(image)
plt.axis('on')

def on_click(sel):
    if sel.inaxes and sel.button == 1:
        x, y = sel.xdata, sel.ydata
        print(f'坐标为{x:.0f}和{y:.0f}')

# mplcursors.cursor(click=True).connect('add', on_hover)
plt.gcf().canvas.mpl_connect('button_press_event', on_click)

plt.show()