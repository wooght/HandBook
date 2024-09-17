# -- coding: utf-8 -
"""
@project    :HandBook
@file       :get_new_sign.py
@Author     :wooght
@Date       :2024/9/17 1:05
@Content    :
"""
import frida, sys
import pprint, json
import time

with open('http_txt/hashMap1.txt') as f:
    hashmap_txt = f.read()

def last_to_dict(s):
    s = 'deviceId' + s
    s_list = s.split(',')
    result_dict = {ss.split('=')[0].strip(): ss.split('=')[1] for ss in s_list}
    return result_dict

hashmap_txt = hashmap_txt.replace('\\', '')
forward_params, last_params = hashmap_txt.split('deviceId')
forward_params = forward_params.replace('}"', "}")
forward_params = forward_params.replace('"{', "{")
forward_params = forward_params[6:-2]
print(forward_params)
f_params_json = json.loads(forward_params)
pprint.pprint(f_params_json)

last_params_json = last_to_dict(last_params[:-1])
print(last_params_json)

now_time = time.time()
# 跟新f_params 数据
f_params_json['containerParams']['recommend_multi_channel']['clientReqTime'] = int(now_time*1000)

# 更新last_params 数据
last_params_json['t'] = int(now_time)
