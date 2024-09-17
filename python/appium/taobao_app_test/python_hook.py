# -- coding: utf-8 -
"""
@project    :HandBook
@file       :python_hook.py
@Author     :wooght
@Date       :2024/9/11 20:42
@Content    :python hook android
"""
import frida, sys
import pprint, json
import time

def get_key_words(p):
    """
    返回参数列表, 多级按照:连接
    :param p:
    :return:
    """
    if isinstance(p, dict):
        key_words = []
        for key, value in p.items():
            if isinstance(value, dict):
                key_list = get_key_words(value)
                if isinstance(key_list, list):
                    for k in key_list:
                        key_words.append(key+':'+k)
            else:
                key_words.append(key)
        return key_words
    else:
        return None

def get_multi_dict(p, l):
    """
    获取多级(不定级)dict的值
    Parameters
    ----------
    p
    l

    Returns
    -------

    """
    if len(l)>1:
        c = p
        for k in l:
            c = c[k]
        return c
    else:
        return None

def get_params_diff(p1, p2):
    """
    参数对比,返回不同参数的key
    :param p1:
    :param p2:
    :return:
    """
    key_words = get_key_words(p1)
    key_words_p2 = get_key_words(p2)
    print('p1_key_words:', key_words, '\r\n p2_key_words:', key_words_p2)
    diff_key = {}
    for key in key_words:
        if key in key_words_p2:
            if ':' in key:
                p1_multi = get_multi_dict(p1, key.split(':'))
                p2_multi = get_multi_dict(p2, key.split(':'))
                if p1_multi != p2_multi:
                    diff_key[key] = f'p1:{key}:{p1_multi}, p2:{key}:{p2_multi}'
            else:
                if p1[key] != p2[key]:
                    diff_key[key] = f'p1:{key}:{p1[key]}, p2:{key}:{p2[key]}'
        else:
            if ':' in key:
                p1_multi = get_multi_dict(p1, key.split(':'))
                diff_key[key] = f'p1:{key}:{p1_multi}, p2:null'
            else:
                diff_key[key] = f'p1:{key}:{p1[key]}, p2:null'
    return diff_key

def get_mo140317a_params(mo140317a_params):
    mo140317a_params = mo140317a_params.replace('\\"', '"')
    forward_params, last_params = mo140317a_params.split('deviceId')
    forward_params = forward_params.replace('}"', "}")
    forward_params = forward_params.replace('"{', "{")
    forward_params = forward_params[6:-2]
    print(forward_params)
    f_params_json = json.loads(forward_params)
    pprint.pprint(f_params_json)

params_models = {}

def on_message(message, data):
    global params_models
    if message['type'] == 'send':
        print('send-->')
        payload_text = message['payload']
        print(payload_text)
        if 'pageNum' in str(payload_text):
            # print(payload_text[6:])
            mo140317a_params = payload_text.replace('\\"', '"')
            mo140317a_params = mo140317a_params.replace('\\', '')
            forward_params, last_params = mo140317a_params.split('deviceId')
            last_params = 'deviceId' + last_params
            forward_params = forward_params.replace('}"', "}")
            forward_params = forward_params.replace('"{', "{")
            forward_params = forward_params[6:-2]
            f_params_json = json.loads(forward_params)
            # 后半截无引号的做处理
            print(last_params[0:-1])
            last_params_list = last_params[0:-2].split(',')
            print(last_params_list)
            for k in last_params_list:
                if 'openappkey' in k:
                    key1, key2 ,val  = k.strip().split('=')
                    f_params_json[key1], f_params_json[key2] = val, val
                else:
                    key, val = k.strip().split('=')
                    f_params_json[key] = val
            # pprint.pprint(f_params_json)
            if len(params_models) < 1:
                params_models = f_params_json
            else:
                print('len:', len(params_models))
                pprint.pprint(get_params_diff(params_models, f_params_json))
                print('now_time', int(time.time()*1000))

    else:
        print('-=-=:', message)



# hook javascript
hook_js = """
function mapToString(hash_map) {
    var result = "";
 var keyset = hash_map.keySet();
 var it = keyset.iterator();
 while (it.hasNext()) {
     var keystr = it.next().toString();
     var valuestr = hash_map.get(keystr).toString();
     result += keystr +"="+valuestr+"&";
 }
 return result.substring(0, result.length - 1);
}
// 接受 python传递的参数  固定格式
recv('poke', function onMessage(pokeMessage) { send('pokeBack:'+pokeMessage.type); });
Java.perform(function () {
    var SwitchConfig = Java.use('mtopsdk.mtop.global.SwitchConfig');
    // 关闭spdy协议
    SwitchConfig.isGlobalSpdySwitchOpen.overload().implementation = function () {
        // var ret = this.isGlobalSpdySwitchOpen.apply(this, arguments);
        // console.log('start:' + ret)
        return false;
    };

    /**
     * 重点:
     * hashMap: url参数及headers部分参数:  exParams, appKey,api,坐标(lat,lng),ttid,extdata,utdid,deviceId,sid,uid
     * result:x-sgext, x-umt, x-mini-wua, x-sign 等headers字段
     */
    let ryw = Java.use("tb.ryw");
    ryw["a"].overload('java.util.HashMap', 'java.util.HashMap', 'java.lang.String', 'java.lang.String', 'boolean', 'java.lang.String').implementation = function (hashMap, hashMap2, str, str2, z, str3) {
        send(`${hashMap}`);  // 回调内容
        let result = this["a"](hashMap, hashMap2, str, str2, z, str3);
        // console.log(`ryw.mo140317a result=${result}`);
        return result;
    };
});
"""

# 启动hook操作
'''
    get_usb_device  (Device类), 得到一个USB设备
    Device.get_frontmost_application() 获取当前运行app信息
    Device.spawn(进程ID/包名)   重启进程,并返回进程ID
    Device.attach(进程ID/报名)  (Session实例)绑定目标进程,并建立会话
    Session.create_script()  创建JS脚本,注入JavaScript并得到(Script)实例
    Script.on('message', callback_function) 为Script实例添加一个消息回调
    Script.load()   加载(运行)JS脚本
'''
process = frida.get_usb_device(-1).attach('淘宝')     # get_usb_device() 得到一个连接中的USB设备, attach() 附加到目标进程
script = process.create_script(hook_js)
script.on('message', on_message)
script.load()
script.post({"type": "poke"})   # 传递参数
# script.unload() 卸载js 及停用插桩
sys.stdin.read()


"""
变动的内容:
{'containerParams:newface_home_main:bizParams:multiTab:tabId': 'p1:containerParams:newface_home_main:bizParams:multiTab:tabId:pindao_0008, '
                                                               'p2:containerParams:newface_home_main:bizParams:multiTab:tabId:pindao_0010',
 'containerParams:newface_home_main:clientReqTime': 'p1:containerParams:newface_home_main:clientReqTime:1726219354378, '
                                                    'p2:containerParams:newface_home_main:clientReqTime:1726219373779',
 'containerParams:newface_home_sub:bizParams:multiTab:tabId': 'p1:containerParams:newface_home_sub:bizParams:multiTab:tabId:pindao_0008, '
                                                              'p2:containerParams:newface_home_sub:bizParams:multiTab:tabId:pindao_0010',
 'containerParams:newface_home_sub:clientReqTime': 'p1:containerParams:newface_home_sub:clientReqTime:1726219354378, '
                                                   'p2:containerParams:newface_home_sub:clientReqTime:1726219373780',
 't': 'p1:t:1726219354, p2:t:1726219373'}
"""