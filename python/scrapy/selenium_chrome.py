# coding=utf-8
# @Explain  : chromedriver 详解
# @Author   : wooght
# @File     : honc_live selenium_chrome
# @Time     : 18-5-28 下午8:17

import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()  # 启动设置项
# chrome_options.add_argument('--headless')  # 设置无头
# 设置user-agent  这里设置成iphone浏览器
# chrome_options.add_argument('user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"')
chrome_options.add_argument('lang=zh_CN.UTF-8')  # 设置语音和编码
driver = webdriver.Chrome(chrome_options)  # 实例webdirver,病添加设置项目
driver.maximize_window()  # 窗口最大化
driver.get('https://www.baidu.com')  # 添加获取网站
driver.find_element_by_id('kw').send_keys('wooght')  # 窗口输入
driver.find_element_by_id('su').click()  # 按钮点击
time.sleep(2)
driver.execute_script("var a=document.documentElement.scrollTop=3000;")  # 滚动条滚动
print(driver.page_source)