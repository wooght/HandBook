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

APPIUM_PORT = 16384
APPIUM_HOST = '127.0.0.1'




@pytest.fixture(scope='session')
def appium_service():
    service = AppiumService()
    service.start(
        # Check the output of `appium server --help` for the complete list of
        # server command line arguments
        args=['--address', APPIUM_HOST, '-p', str(APPIUM_PORT)],
        timeout_ms=20000,
    )
    yield service
    service.stop()

def create_android_driver(custom_opts=None):
    options = UiAutomator2Options()
    options.platform_version = '7'
    options.platform_name = 'Android'
    options.app_package = 'com.taobao.taobao'
    options.app_activity = 'com.taobao.tao.TBMainActivity'
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    return webdriver.Remote(f'http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)

@pytest.fixture
def android_driver_factory():
    return create_android_driver


@pytest.fixture
def android_driver():
    # prefer this fixture if there is no need to customize driver options in tests
    driver = create_android_driver()
    yield driver
    driver.quit()

def test_android_click(appium_service, android_driver_factory):
    with android_driver_factory() as driver:
        el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='item')
        el.click()



