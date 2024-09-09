# -- coding: utf-8 -
"""
@project    :HandBook
@file       :test.py
@Author     :wooght
@Date       :2024/8/22 12:44
@Content    :
"""
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'

# service = AppiumService()
# service.start(
#     # Check the output of `appium server --help` for the complete list of
#     # server command line arguments
#     args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT)],
#     timeout_ms=20000,
# )

def get_driver():
    options = UiAutomator2Options()
    options.platform_version = '7.1.2'                      # 系统版本
    options.platform_name = 'Android'                       # 系统名称
    options.device_name = '127.0.0.1:62001'                 # 虚拟机地址
    options.app_package = 'com.taobao.taobao'               # package
    options.app_activity = 'com.taobao.tao.TBMainActivity'  # activity

    driver = webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}/wd/hub', options=options)
    return driver

if __name__ == '__main__':
    get_driver()