# -- coding: utf-8 -
"""
@project    :HandBook
@file       :frida_test.py
@Author     :wooght
@Date       :2024/9/4 16:09
@Content    :
"""
import frida
rdev = frida.get_remote_device()
front_app = rdev.get_frontmost_application()
print(front_app)