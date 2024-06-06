# -- coding: utf-8 -
"""
@project    :HandBook
@file       :image_base.py
@Author     :wooght
@Date       :2024/6/3 21:26
@Content    :
"""
import numpy
from PIL import Image
from PIL import ImageFilter

im = Image.open('../pic/17273.png')
print(im.format)        # 图片格式(jpg/png/gif...)
print(im.mode)          # 图片模式(L黑白,RGB真彩,RGBA真彩+透明通道,CMYK颜色隔离,F32位浮点型)
new_im = im.convert('L')    # convert() 转换图像色彩模式
print(new_im.size)      # 图像的尺寸
box_size = (996, 406, 1384, 644)  # 截取图片的尺寸 左上角为原点,(x1,y1,x2,y2)  x1,y1为左上角顶点位置,x2,y2为右下角顶点位置
crop_im = new_im.crop(box_size)
contour_im = crop_im.filter(ImageFilter.FIND_EDGES)    # filter 滤波器,ImageFilter滤波器模块 CONTOUR轮廓,FIND_EDGES边缘
contour_im.show()
# numpy 加载图片
img_arr = numpy.array(contour_im)
print(img_arr.shape)
print(img_arr)
axis = img_arr.shape[0]

# 每行求和
y_sum = img_arr[::, 7:80].sum(axis=1)
row = []
print(y_sum)
for i in range(1, img_arr.shape[0] - 1):
    if y_sum[i] > 6000:
        row.append(i)
        print(i, ':', y_sum[i])

# 每列求和
x_sum = img_arr[row[0]:row[0]+60,::].sum(axis=0)
print(x_sum)
column = []
for i in range(1, img_arr.shape[1] - 1):
    if x_sum[i] > 6000:
        column.append(i)
        print(i, ':', x_sum[i])
