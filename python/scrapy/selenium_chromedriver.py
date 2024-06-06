# -- coding: utf-8 -
"""
@project    :HandBook
@file       :selenium_chromedriver.py
@Author     :wooght
@Date       :2024/4/24 18:16
@Content    :chromedriver demo
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import json
import pandas as pd

chrome_options = Options()
chrome_options.add_argument("--headless")   # 设置无头

browser = webdriver.Chrome(options=chrome_options)
browser.get('http://www.linkbld.com')
assert "领克" in browser.title
browser.find_element('name', 'user').send_keys('wooght')
browser.find_element('name', 'password').send_keys('wooght565758')
browser.find_element(By.XPATH, '/html/body/div/div[2]/form/div[3]/div[2]/button').click()
time.sleep(2)
browser.get('http://www.linkbld.com/day_sales_trend')

response = browser.page_source.lstrip('<html><body><head></head><body>(')
response = response.rstrip(")</body></html>")
print(response)
month_data = json.loads(response)
for key in month_data:
    print(key)
    for value in month_data[key]:
        print(value)