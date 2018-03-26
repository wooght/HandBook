# -*- coding: utf-8 -*-
#
# @method   : pytesseract 图片识别
# @Time     : 2018/1/5
# @Author   : wooght
# @File     : wpytesseract.py

from pytesseract import *
from PIL import Image
from PIL import ImageEnhance


im = Image.open('image/5.png')
# 使用ImageEnhance可以增强图片的识别率
enhancer = ImageEnhance.Contrast(im)
image = im.convert('L')
text = image_to_string(im)

print('is:',text)