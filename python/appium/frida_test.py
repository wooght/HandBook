# -- coding: utf-8 -
"""
@project    :HandBook
@file       :frida_test.py
@Author     :wooght
@Date       :2024/9/4 16:09
@Content    :
"""
"""
    应用frida之前,需启动虚拟机,然后启动虚拟机中的frida-server
    一:启动虚拟机
    二:链接虚拟机 adb connect 127.0.0.1:16384
    三:启动虚拟机中的frida-server
        adb shell 进入虚拟机shell模式
        su 获取管理员权限
        cd /data/local/tmp 进入frida-server目录
        ./ frida-server 运行服务
"""
import frida

# 得到一个连接中的设备 device(装备,设备)  -1 只最近一次
# Device(id="127.0.0.1:16384", name="2206122SC", type='usb')
process = frida.get_usb_device(-1)
print(process.id, process.name, process.type)

all_app = process.enumerate_applications
print(all_app)
# 获取当前运行应用
# Application(identifier="com.ss.android.article.news", name="今日头条", pid=2546, parameters={})
front_app = process.get_frontmost_application()
print(front_app)

# 打开app
taobao_pid = process.spawn('com.taobao.taobao')     # 返回进程pid
print(taobao_pid)

"""
    获取远程设备
"""
# Device(id="socket", name="Local Socket", type='remote')
rdev = frida.get_remote_device()
print(rdev)
# Application(identifier="com.ss.android.article.news", name="今日头条", pid=2478, parameters={})
front_app = rdev.get_frontmost_application()
print(front_app)

# 启动hook操作
'''
    python 启动 frida 进行hook操作流程:
    A: 运行frida,启动js
        frida -U -l xx.js  淘宝  此方法为绑定已经打开的淘宝
        frida -U -l xx.js  com.taobao.taobao 此方法为打开淘宝,并绑定
    B:应用
        一:frida.get_usb_device  (Device类), 得到一个USB设备
        二:Device.attach(进程ID/报名)  (Session实例)绑定目标进程,并建立会话
            也可以用Device.spawn(进程ID/包名)   重启进程,并返回进程ID 缺陷:重启app的次数会明显增多
        三:Session.create_script()  创建JS脚本,注入JavaScript并得到(Script)实例
        四:Script.on('message', callback_function) 为Script实例添加一个消息回调
        五:Script.load()   加载(运行)JS脚本
        六:创建python创建回调函数
            callback_function(message, data):
                message['type'] 为回调类型,js端send过来,这里type就是send
                data 就是回到传递的数据
        七:执行hook js中的函数,并得到返回结果
            python:script.exports.function_name(params...)
            js:
                rpc.exports = {
                    // 名字同python访问的名字不同,大写
                    // script_function 为js中具体要执行的函数
                    FunctionName:script_function,
                    ...
                }
'''