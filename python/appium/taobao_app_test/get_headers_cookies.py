# -- coding: utf-8 -
"""
@project    :HandBook
@file       :get_headers_cookies.py
@Author     :wooght
@Date       :2024/10/11 12:40
@Content    :获取淘宝app headers cookie
"""
import time

import frida


with open('js/get_headers_cookie.js', 'r', encoding='utf-8') as f:
    headers_c_js = f.read()
is_run = False
run_params = {'cookies':'', 'headers':''}

def on_message(message, data):
    global is_run, run_params
    if message['type'] == 'send':
        print(message)
        result_type = message['payload']['type']
        run_params[result_type] = message['payload'][result_type]
        if len(run_params['cookies']) > 0 and len(run_params['headers']) > 0:
            is_run = True
process = frida.get_usb_device(-1).attach('淘宝')     # 得到最近一个USB连接,attach 绑定目标进程
script = process.create_script(headers_c_js)         # 创建hook js文件
script.on('message', on_message)
script.load()                                        # 执行js
while not is_run:
    time.sleep(1)

cookies = run_params['cookies']
headers = run_params['headers']

cookies_arr = cookies.split(';')
headers_arr = headers.split(',')

cookies_dict = {}
headers_dict = {}
for c in cookies_arr:
    c_arr = c.split('=')
    cookies_dict[c_arr[0].strip()] = c_arr[1].strip()

for h in headers_arr:
    h_arr = h.split('=')
    headers_dict[h_arr[0].strip()] = h_arr[1].strip()

import pprint

pprint.pprint(cookies_dict)
pprint.pprint(headers_dict)