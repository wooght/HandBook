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

APPIUM_PORT = 4723          # appium 端口
APPIUM_HOST = '127.0.0.1'   # appium 地址

# service = AppiumService()
# service.start(
#     # Check the output of `appium server --help` for the complete list of
#     # server command line arguments
#     args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT)],
#     timeout_ms=20000,
# )

def get_driver():
    options = UiAutomator2Options()
    # options.platform_version = '12'                         # 系统版本
    # options.platform_name = 'Android'                       # 系统名称
    # options.device_name = '127.0.0.1:16384'                 # 虚拟机地址
    # options.app_package = 'com.taobao.taobao'               # package
    # options.app_activity = 'com.taobao.tao.TBMainActivity'  # activity
    options.load_capabilities({
        "platformName": "Android",                              # 系统名称
        "appium:platformVersion": "12",                         # 系统版本
        "appium:deviceName": "127.0.0.1:16384",                 # 虚拟机地址
        # "appium:appPackage": "com.ss.android.article.news",     # package
        # "appium:appActivity": "com.ss.android.article.news.activity.MainActivity",  # activity
        "appium:ensureWebviewsHavePages": True,
        "appium:nativeWebScreenshot": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "noReset": True,                                        # 不清理数据
        "autoGrantPermissions": True                            # 自动授权
    })


    driver = webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}/wd/hub', options=options)
    return driver

if __name__ == '__main__':
    import time
    driver = get_driver()
    loop_nums = 0

    """
        淘宝操作
    """
    top_bar_nums = 0
    # 商品列表://android.widget.FrameLayout[@resource-id="com.taobao.taobao:id/rv_main_container_wrapper"]/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[2]
    multi_tab = driver.find_element(AppiumBy.ID, 'com.taobao.taobao:id/multi_tab_container')
    # 头部导航
    print(multi_tab)
    action_bar = multi_tab.find_elements(AppiumBy.CLASS_NAME, 'android.support.v7.app.ActionBar$b')
    top_bar_list = []
    for item in action_bar:
        print(item)
        try:
            current_bar = item.find_element(AppiumBy.CLASS_NAME, 'android.widget.TextView')
            print(current_bar.text)
            top_bar_list.append(current_bar)
        except Exception as e:
            print(e)

    def scroll_loop():
        global loop_nums
        global top_bar_nums
        # 列表下拉
        frame_layout = driver.find_elements(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="com.taobao.taobao:id/rv_main_container_wrapper"]/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/android.support.v4.view.ViewPager/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout')
        for item in frame_layout:
            print(item)
        max_frame = len(frame_layout) - 1
        driver.scroll(frame_layout[max_frame], frame_layout[0])
        if loop_nums < 10:
            if loop_nums % 2 == 0:
                time.sleep(5)
                top_bar_list[top_bar_nums].click()
                top_bar_nums += 1
            loop_nums += 1
            time.sleep(5)
            print(loop_nums)
            scroll_loop()

    scroll_loop()



    #
    # for bar in top_bar_list:
    #     time.sleep(5)
    #     bar.click()

    """
        今日头条操作
    """
    # def scroll_loop():
    #     global loop_nums
    #     ghk = driver.find_elements(AppiumBy.ID, 'com.ss.android.article.news:id/akb')
    #     nav = driver.find_element(AppiumBy.XPATH, '//android.widget.HorizontalScrollView[@resource-id="com.ss.android.article.news:id/az9"]/android.widget.LinearLayout')
    #     akb = driver.find_elements(AppiumBy.ID, 'com.ss.android.article.news:id/akb')
    #     print(nav.find_elements(AppiumBy.CLASS_NAME, 'android.widget.Button'))
    #     for item in ghk:
    #         print(item)
    #     if loop_nums < 4:
    #         max_item = len(ghk) - 1
    #         driver.scroll(ghk[max_item], ghk[0])
    #     else:
    #         max_item = len(akb) - 1
    #         driver.scroll(akb[max_item], akb[0])
    #     time.sleep(5)
    #
    #     loop_nums += 1
    #     if loop_nums % 3 == 0:
    #         nav.find_elements(AppiumBy.CLASS_NAME, 'android.widget.Button')[4].click()
    #     if loop_nums < 15:
    #         scroll_loop()
    #
    # scroll_loop()