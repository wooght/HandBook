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

# 打开文件
with open('http_txt/hashMap1.txt') as f:
    hashmap_txt = f.read()

with open('js/up_sign_params.js') as f:
    hook_js = f.read()

def last_to_dict(s):
    s = 'deviceId' + s
    s_list = s.split(',')
    result_dict = {ss.split('=')[0].strip(): ss.split('=')[1] for ss in s_list}
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


# 斜杠模型  slash:斜杠
slash_models = {'7': '\\'*7+'"', '3': '\\'*3+'"', '1': '\\'+'"', '0': '"'}


def multi_dict_string(d, current_depth, depth_dict):
    """
    多级字典转字符串 带斜杠判断
    Parameters
    ----------
    d               多级字典
    current_depth   初始深度
    depth_dict      深度字典

    Returns
    -------

    """
    return_str = ''
    if isinstance(d, dict):
        start_bracket = '{'              # 前括号 bracket: 括号
        end_bracket = '},'                # 结束符号
        for key, val in d.items():
            if isinstance(val, dict):
                child_keys = list(val.keys())
                if len(child_keys) == 0:
                    key_depth = current_depth
                else:
                    child_first = child_keys[0]
                    if child_first in depth_dict.keys():
                        key_depth = depth_dict[child_first]
                        if key_depth != current_depth:
                            # 深度改变
                            start_bracket = slash_models[current_depth] + '{'
                            end_bracket = '}' + slash_models[current_depth] + ','
                        else:
                            # {} 里外 \\\ 数相同,则{不需要双引号
                            start_bracket = '{'
                            end_bracket = '},'
                    else:
                        key_depth = current_depth
                        start_bracket = '{'
                        end_bracket = '},'
                # 递归调用
                slash = slash_models[current_depth]
                return_str += slash+key+slash+':'+start_bracket+multi_dict_string(val, key_depth, depth_dict) + end_bracket
            else:
                # 在深度字典中 则需要判断斜杠的个数
                if key in depth_dict.keys():
                    slash = slash_models[depth_dict[key]]
                    current_str = slash + key + slash
                    v = ''
                    if not isinstance(val, str):
                        # 布尔值和数字 不需要双引号
                        if isinstance(val, bool):
                            print(key,val)
                            v = 'true' if val else 'false'                      # 转小写
                        elif isinstance(val, int) or isinstance(val, float):    # python False 为-1  True 为1
                            v = str(val)
                    else:
                        v = slash + str(val) + slash
                    return_str += current_str + ':' + v + ','
                else:
                    return_str += '"'+key+'":"'+str(val)+'",'
        return return_str[:-1]
    else:
        return None

'''
    frida 片段
'''
params_models = {}
def on_message(message, data):
    if message['type'] == 'send':
        print(message['payload'])
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

hashmap_json = extract_category_params(hashmap_txt)
pprint.pprint(hashmap_json)
depth_dict = get_keys_depth(hashmap_txt)
print(depth_dict)
send_txt = multi_dict_string(hashmap_json, '0', depth_dict)
print('{'+send_txt+'}')


process = frida.get_usb_device(-1).attach('淘宝')     # get_usb_device() 得到一个连接中的USB设备, attach() 附加到目标进程
script = process.create_script(hook_js)
script.on('message', on_message)
script.load()
script.post({'type': 'poke', 'data': '{'+send_txt+'}', 'now_time':str(int(time.time()))})   # 传递参数
# script.unload() 卸载js 及停用插桩
sys.stdin.read()