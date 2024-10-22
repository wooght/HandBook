# -- coding: utf-8 -
"""
@project    :HandBook
@file       :get_new_sign.py
@Author     :wooght
@Date       :2024/9/17 1:05
@Content    :
"""
import frida, sys
import pprint, json, re
import time
from tools.json_tools import multi_dict_string

"""
    打开文件
"""
# hashMap
with open('http_txt/hashMap1.txt') as f:
    hashmap_txt = f.read()
# headers
with open('http_txt/headers.txt') as f:
    headers_txt = f.read()
# cookies
with open('http_txt/cookies.txt') as f:
    cookies_txt = f.read()

with open('js/up_sign_params.js') as f:
    hook_js = f.read()

def get_headers_dict(headers_text):
    """
    从字符串中提取headers
    Parameters
    ----------
    headers_text

    Returns
    -------
    返回headers 字典
    """
    headers_list = headers_text.split('\n')
    headers_dict = {header.split(': ')[0]:header.split(': ')[1] for header in headers_list}
    return headers_dict

def get_cookies_dict(txt):
    """
    从字符串中提取cookies
    Parameters
    ----------
    txt

    Returns
    -------

    """
    txt_list = txt.split(';')
    result_dict = {}
    for l in txt_list:
        split_list = l.split('=')
        if len(split_list) > 1:
            k, v = split_list[0], split_list[1]
        else:
            k, v = split_list[0], None
        result_dict[k.strip()] = v.strip()
    return result_dict

def get_keys_depth(s):
    """
    depth: 深度
    通过/的个数,获取字典深度关系
    Parameters
    ----------
    s

    Returns
    -------
    返回深度关系 {key:depth, key2:depth, ...}
    """
    # ss = '''{\\\"performanceAbTestInfo\\\":\\\"{\\\\\\\"bucketId\\\\\\\":\\\\\\\"20002\\\\\\\",\\\\\\\"bucketType\\\\\\\":\\\\\\\"test\\\\\\\",\\\\\\\"testId\\\\\\\":\\\\\\\"tb_start_exp\\\\\\\"}\\\"}\",\"deviceInfo\":\"{\\\"deviceModel\\\":\\\"phone\\\"}\",\"lastClickItemId\":\"\",\"networkStatus\":\"poor\",\"ucpFatigueData\":\"{\\\"c\\\":0,\\\"r\\\":\\\"0|21423|500000002|9448|40168|47852|20240911|8#\\\"}\"}"}'''
    random_nums = {'7':r'\\\\\\\\\\\\\\"(\w+)\\\\\\\\\\\\\\"\:', '3':r'\\\\\\"(\w+)\\\\\\"\:', '1':r'\\"(\w+)\\"\:'}   # 顶级无/  ,一级一个/ 二级 ///  三级///////
    depth_dict = {}
    for n, r in random_nums.items():
        re_result = re.findall(r, s)
        if len(re_result) > 0:
            for k in re_result:
                depth_dict[k] = n
    return depth_dict


def extract_category_params(hashmap_txt):
    """
    extract:提取    category:分类
    获取已经保存的params,并对其进行值改变,返回字典
    Parameters
    ----------
    hashmap_txt

    Returns
    -------

    """
    hashmap_txt = hashmap_txt.replace('\\', '')
    # 分成前后两部分
    data_params = hashmap_txt.replace('}"', "}")
    data_params = data_params.replace('"{', "{")
    # 转换为json
    data_json = json.loads(data_params)
    # pprint.pprint(data_json)
    now_time = time.time()
    data_json['containerParams']['recommend_multi_channel']['clientReqTime'] = int(now_time * 1000)

    # other_json = last_to_dict(other_params)
    # # print(other_json)
    # other_json['t'] = int(now_time)
    #
    # result_dict = {'data':data_json}
    # result_dict = {**result_dict, **other_json}
    # pprint.pprint(result_dict)
    return data_json


'''
    frida 片段
'''
params_models = {}
def on_message(message, data):
    if message['type'] == 'send':
        print('send success:', message['payload']['data'])
    else:
        print(message)
    # global params_models
    # if message['type'] == 'send':           # 获取message的类型,如果是send,就是传递数据
    #     payload_text = message['payload']   # 获取send数据主体
    #     if 'pageNum' in str(payload_text):
    #         hashmap_txt = payload_text.replace('\\', '')
    #         # 分成前后两部分
    #         data_params, other_params = hashmap_txt.split('deviceId')
    #         data_params = data_params.replace('}"', "}")
    #         data_params = data_params.replace('"{', "{")
    #         # 去除开头{data= 和末尾}字符
    #         data_params = data_params[6:-2]
    #         # 转换为json
    #         data_json = json.loads(data_params)
    #         pprint.pprint(data_json)
    #
    #         other_json = last_to_dict(other_params)
    #         print(other_json)
    #
    #         now_time = time.time()
    #         data_params['containerParams']['recommend_multi_channel']['clientReqTime'] = int(now_time)
    #         other_params['t'] = int(now_time*1000)
    # else:
    #     print('-=-=:', message)

"""
    hashMap操作
"""
hashmap_json = extract_category_params(hashmap_txt)
pprint.pprint(hashmap_json)
depth_dict = get_keys_depth(hashmap_txt)
print(depth_dict)
send_txt = multi_dict_string(hashmap_json, '0', depth_dict)
print('{'+send_txt+'}')

"""
    headers 操作
"""
headers_dict = get_headers_dict(headers_txt)
pprint.pprint(headers_dict)

"""
    cookies 操作
"""
cookies_dict = get_cookies_dict(cookies_txt)
pprint.pprint(cookies_dict)


process = frida.get_usb_device(-1).attach('淘宝')     # get_usb_device() 得到一个连接中的USB设备, attach() 附加到目标进程
script = process.create_script(hook_js)
script.on('message', on_message)
script.load()
time.sleep(10)
script.post({'type': 'sign', 'data': '{'+send_txt+'}', 'now_time':str(int(time.time()))})   # 传递参数
while True:

    print('send new:')
    script.post({'type': 'sign', 'data': '{'+send_txt+'}', 'now_time':str(int(time.time()))})   # 传递参数
    time.sleep(10)


# script.unload() 卸载js 及停用插桩
# sys.stdin.read()


"""
{'Accept-Encoding': 'zstd, gzip',
 'Connection': 'Keep-Alive',
 'Content-Encoding': 'gzip',
 'Content-Length': '1049',
 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
 'Host': 'guide-acs.m.taobao.com',
 'a-orange-dq': 'appKey=21646297&appVersion=10.39.10&clientAppIndexVersion=1120240918153202768',
 'c-launch-info': '2,0,1726645476982,1726644517613,2',
 'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
 'f-refer': 'mtop',
 'user-agent': 'MTOPSDK%2F3.1.1.7+%28Android%3B12%3BXiaomi%3B2206122SC%29+DeviceType%28Phone%29',
 'x-app-conf-v': '0',
 'x-app-edition': 'ST',
 'x-app-ver': '10.39.10',
 'x-appkey': '21646297',
 'x-biz-info': 'containerId=recommend_multi_channel_pindao_0001;requestType=',
 'x-biz-type': 'dosa',
 'x-bx-version': '6.6.240704',
 'x-c-traceid': '04hdzQV2N',
 'x-devid': 'AqG65eu5Gpa1TRU6pBy5oeIvE-NbacZRFaSYUrt0qtBF',
 'x-extdata': 'openappkey%3DDEFAULT_AUTH',
 'x-falco-id': '04hdzQV2N',
 'x-features': '27',
 'x-location': '115.109334%2C39.633542',
 'x-mini-wua': 'aJgQWBET33hS7vGTV6js1%2BjaJdi4GZdsrRgK2Bynva72tWiZMSp5EVs6DwwJOWMto9t0sixZvbdktn4MFdPNhvPuf4OgC50W3WpvRxiUguLjbXSm6xLDlCVALlmOIL%2Bx9yrV13ZqFNfT4YrIm%2BqOpU9hJG06KdkhFRWdDjLxUGFY0MjVNQF3ZNOBb7MxjzQuDnQM%3D',
 'x-nettype': 'WIFI',
 'x-nq': 'WIFI',
 'x-page-name': 'com.taobao.tao.TBMainActivity',
 'x-page-url': 'http%3A%2F%2Fm.taobao.com%2Findex.htm',
 'x-pv': '6.3',
 'x-regid': 'reg0pnFeVn0umJbetWmmuBkv0BEL1rHS',
 'x-region-channel': 'CN',
 'x-sgext': 'JBPfsM1uOUFl1h1UthPQ3LDugO%2BD65PqhuqD%2FIXuk%2FyB6ILphuuE6oHmk%2B%2BG6NbrgO2AvNLn0uqF69T8he%2BT6JPvgPyA74Dok%2ByT7pPuk%2B6T7ZPsk%2ByT75Pth%2FyD%2FID8gPyA%2FID8gPyA%2FID8k7qT75Pvk%2BjW6IfvgfyA74DvgPyA%2FIXmhPyA%2FJPuk%2B6T7JPvk6XzseH8gPyQ%2F4K9kP%2BQ75Pv757XrImdx570nvLn8ZfHno2AhICC%2BYfplu6W75bthPmB6ZbuhvmA%2BYb5hvmG%2BYD5geqE7IXqlqrarO%2Fq7%2B%2BW75bphrrR54S90fmA%2BYD5gPmA%2BYHpluvv6e%2Fulu2W6pbmlryWu5bugYCHgIHqne2J8oPygPKA8oDygPKB8oPsh%2FKC6IDygu2FgImAgfKB8u%2B%2B7%2B2W7oD5gIDSgIfnne6d7Ynyg%2FKB7%2B%2B87%2B6d7oDyg%2FKA8oTu0%2BadvtTyg77W8oCA1IDlif6N5u7%2BjeXu9eLvue%2Fsne%2Bd7YfmhfKB6IDyge%2BE5u%2FugID%2BlvW307LCt9iS8fCEnvGXn577ndqFgJv3psee8Z7xnvGe8Z76qt6%2B2O6AjfLr2prhvOKwwrTSs9Oy8uv2ntWbx5T0qPGe8Z79nvGU6er5iOme7%2B6BgID5gPGJ54Hvg%2BaW7oL5g%2FmB7Zbrg%2FmB6pbvlu6I%2BYXulu2B%2BYHt7%2B6CgILygeqd5onq7%2B6DgPGM257IqPHw8ZXlnvGe8abxndue0Y7xhvGc9Z7v7oaAgICB6O%2Fune6d653tgPKD5oXygfKA8oXsneqG8oPt7w%3D%3D',
 'x-sid': '25601ccd9fad1321ce4f2a5cebbd86dd',
 'x-sign': 'azYBCM006xAALP4PXfeaElQ7Mtx9PP4M9%2FAC6pmSMSWrhh4Zk0hNzGX5riXePgEXutnhT6YXy8v1ttpIXUbKAKewqJwODP4M%2Fqz%2BDP',
 'x-social-attr': '3',
 'x-t': '1726645476',
 'x-ttid': '703304%40taobao_android_10.39.10',
 'x-uid': '4060247732',
 'x-umt': 'WK4BVtRLPAm%2FVQKSAy%2FxtE1R9DWBs1xw',
 'x-utdid': 'Zs7Pnkn0r40DAKSy%2FCBlF7cX'}
"""
