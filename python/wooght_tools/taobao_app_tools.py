# -- coding: utf-8 -
"""
@project    :HandBook
@file       :taobao_app_tools.py
@Author     :wooght
@Date       :2024/9/5 16:07
@Content    :
"""

import sys
import io

# 设置标准输出的编码为希望的编码，例如GBK
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
import json
import pprint

# api_content = '''"{\r\n    \"skeleton\": [\r\n        {\r\n            \"index\": \"0\",\r\n            \"subSkeleton\": [\r\n                {\r\n                    \"targetId\": \"821\",\r\n                    \"conversationInstance\": \"logistics\",\r\n                    \"targetType\": \"-1\",\r\n                    \"text\": \"物流\",\r\n                    \"bizType\": \"20421\",\r\n                    \"instance\": \"logistics\",\r\n                    \"entityType\": \"PU\",\r\n                    \"index\": \"0\"\r\n                }\r\n            ],\r\n            \"style\": \"noTab\",\r\n            \"unreadNumType\": \"number\",\r\n            \"text\": \"物流 \"\r\n        },\r\n        {\r\n            \"index\": \"1\",\r\n            \"subSkeleton\": [\r\n                {\r\n                    \"targetId\": \"1704176173204\",\r\n                    \"conversationInstance\": \"aftersale\",\r\n                    \"targetType\": \"-1\",\r\n                    \"text\": \"售后\",\r\n                    \"bizType\": \"20434\",\r\n                    \"instance\": \"aftersale\",\r\n                    \"entityType\": \"PU\",\r\n                    \"index\": \"0\"\r\n                }\r\n            ],\r\n            \"style\": \"noTab\",\r\n            \"unreadNumType\": \"number\",\r\n            \"text\": \"售后 \"\r\n        },\r\n        {\r\n            \"index\": \"2\",\r\n            \"subSkeleton\": [\r\n                {\r\n                    \"targetId\": \"1002\",\r\n                    \"conversationInstance\": \"service\",\r\n                    \"targetType\": \"-1\",\r\n                    \"text\": \"提醒\",\r\n                    \"bizType\": \"20422\",\r\n                    \"instance\": \"service\",\r\n                    \"entityType\": \"PU\",\r\n                    \"index\": \"0\"\r\n                }\r\n            ],\r\n            \"style\": \"noTab\",\r\n            \"unreadNumType\": \"number\",\r\n            \"text\": \"提醒 \"\r\n        },\r\n        {\r\n            \"index\": \"3\",\r\n            \"subSkeleton\": [\r\n                {\r\n                    \"targetId\": \"1623064098839\",\r\n                    \"conversationInstance\": \"game\",\r\n                    \"targetType\": \"-1\",\r\n                    \"text\": \"互动\",\r\n                    \"bizType\": \"20427\",\r\n                    \"instance\": \"game\",\r\n                    \"entityType\": \"PU\",\r\n                    \"index\": \"0\"\r\n                }\r\n            ],\r\n            \"style\": \"noTab\",\r\n            \"unreadNumType\": \"number\",\r\n            \"text\": \"互动\"\r\n        },\r\n        {\r\n            \"index\": \"4\",\r\n            \"subSkeleton\": [\r\n                {\r\n                    \"targetId\": \"1692782748477\",\r\n                    \"conversationInstance\": \"like\",\r\n                    \"targetType\": \"-1\",\r\n                    \"text\": \"点赞收藏\",\r\n                    \"bizType\": \"20430\",\r\n                    \"instance\": \"like\",\r\n                    \"entityType\": \"PU\",\r\n                    \"index\": \"0\"\r\n                },\r\n                {\r\n                    \"targetId\": \"1692782591856\",\r\n                    \"conversationInstance\": \"follow\",\r\n                    \"targetType\": \"-1\",\r\n                    \"text\": \"新增关注\",\r\n                    \"bizType\": \"20431\",\r\n                    \"instance\": \"follow\",\r\n                    \"entityType\": \"PU\",\r\n                    \"index\": \"1\"\r\n                },\r\n                {\r\n                    \"targetId\": \"1692782837115\",\r\n                    \"conversationInstance\": \"comment\",\r\n                    \"targetType\": \"-1\",\r\n                    \"text\": \"评论和@\",\r\n                    \"bizType\": \"20432\",\r\n                    \"instance\": \"comment\",\r\n                    \"entityType\": \"PU\",\r\n                    \"index\": \"2\"\r\n                }\r\n            ],\r\n            \"style\": \"hasTab\",\r\n            \"unreadNumType\": \"number\",\r\n            \"text\": \"赞评\"\r\n        },\r\n        {\r\n            \"index\": \"5\",\r\n            \"subSkeleton\": [\r\n                {\r\n                    \"targetId\": \"1556181449297\",\r\n                    \"conversationInstance\": \"promotion\",\r\n                    \"targetType\": \"-1\",\r\n                    \"text\": \"优惠 \",\r\n                    \"bizType\": \"20424\",\r\n                    \"instance\": \"promotion\",\r\n                    \"entityType\": \"PU\",\r\n                    \"index\": \"0\"\r\n                }\r\n            ],\r\n            \"style\": \"noTab\",\r\n            \"unreadNumType\": \"redDot\",\r\n            \"text\": \"优惠\"\r\n        },\r\n        {\r\n            \"index\": \"6\",\r\n            \"subSkeleton\": [\r\n                {\r\n                    \"targetId\": \"1554969329808\",\r\n                    \"conversationInstance\": \"team\",\r\n                    \"targetType\": \"-1\",\r\n                    \"text\": \"其他\",\r\n                    \"bizType\": \"20425\",\r\n                    \"instance\": \"team\",\r\n                    \"entityType\": \"PU\",\r\n                    \"index\": \"0\"\r\n                }\r\n            ],\r\n            \"style\": \"noTab\",\r\n            \"unreadNumType\": \"number\",\r\n            \"text\": \"其他 \"\r\n        }\r\n    ],\r\n    \"mergeConvInfo\": {\r\n        \"convList\": [\r\n            {\r\n                \"targetId\": \"821\",\r\n                \"targetType\": \"-1\",\r\n                \"bizType\": \"20421\",\r\n                \"loadMsgCount\": 3\r\n            },\r\n            {\r\n                \"targetId\": \"1002\",\r\n                \"targetType\": \"-1\",\r\n                \"bizType\": \"20422\",\r\n                \"loadMsgCount\": 3\r\n            },\r\n            {\r\n                \"targetId\": \"1623064098839\",\r\n                \"targetType\": \"-1\",\r\n                \"bizType\": \"20427\",\r\n                \"loadMsgCount\": 1\r\n            },\r\n            {\r\n                \"targetId\": \"1692782748477\",\r\n                \"targetType\": \"-1\",\r\n                \"bizType\": \"20430\",\r\n                \"loadMsgCount\": 1\r\n            },\r\n            {\r\n                \"targetId\": \"1692782591856\",\r\n                \"targetType\": \"-1\",\r\n                \"bizType\": \"20431\",\r\n                \"loadMsgCount\": 1\r\n            },\r\n            {\r\n                \"targetId\": \"1692782837115\",\r\n                \"targetType\": \"-1\",\r\n                \"bizType\": \"20432\",\r\n                \"loadMsgCount\": 1\r\n            },\r\n            {\r\n                \"targetId\": \"1556181449297\",\r\n                \"targetType\": \"-1\",\r\n                \"bizType\": \"20424\",\r\n                \"loadMsgCount\": 3\r\n            },\r\n            {\r\n                \"targetId\": \"1554969329808\",\r\n                \"targetType\": \"-1\",\r\n                \"bizType\": \"20425\",\r\n                \"loadMsgCount\": 1\r\n            },\r\n            {\r\n                \"targetId\": \"1704176173204\",\r\n                \"targetType\": \"-1\",\r\n                \"bizType\": \"20434\",\r\n                \"loadMsgCount\": 1\r\n            }\r\n        ]\r\n    }\r\n}"'''
# new_str = api_content.replace('\r\n', '')
# new_str = new_str.replace('\"', '"')
# new_str = new_str.replace(' ', '')
# print(new_str)
# new_str = new_str.replace('"{', "{")
# new_str = new_str.replace('}"', '}')
# print(len(new_str), new_str)
# json_data = json.loads(new_str)
# pprint.pprint(json_data)

"""
    api:https://guide-acs.m.taobao.com/gw/mtop.relationrecommend.wirelessrecommend.recommend/
"""


"""
    api:mtop.taobao.wireless.home.category
    content:列表
"""

"""
    api:https://trade-acs.m.taobao.com/gw/mtop.taobao.detail.batchgetdetail/
    content: 详情
"""
# 文本转二进制串
with open('taobao_app_response.txt', 'rb') as t:
    response_text = t.read()
response_bytes = [int(b) for b in response_text]
response_128 = [b if b < 128 else b-256 for b in response_bytes]
print('response_bytes:')
print(response_bytes[0:100])
print('response_128:')
print(response_128[0:100])
print(bytes([101,118,101,110,116,58,32,116,114,97,105,108,101,114,10,100,97,116,97,58,32,123,34,120,45,114,101,116,99,111,100,101,34,58,34,83,85,67,67,69,83]).decode('utf-8'))

# app 转换后的二进制串
print('*'*50, 'from char file:')
with open('taobao_app_list_response.txt',) as f:
    response_bytes = f.read()
response_list = response_bytes.split(',')
response_list_256 = [int(i) % 256 for i in response_list]
print(response_list_256[0:100])
print(int('dd', 16))
response_text = bytes(response_list_256).decode('utf-8')
print('response b2 covent utf-8:', response_text)
print(len(response_128), len(response_list_256))
# 两种二进制差
cha = []
i=0
while i < 100:
    cha.append(response_list_256[i] - int(response_128[i]))
    i+=1
print('cha', cha)
# print(bytes(cha[0:4]).decode('utf-8'))


bytedata = '''123,34,97,112,105,34,58,34,109,116,111,112,46,116,97,111,98,97,111,46,100,101,116,97,105,108,46,100,97,116,97,46,103,101,116,34,44,34,100,97,116,97,34,58,123,34,97,112,105,83,116,97,99,107,34,58,91,123,34,110,97,109,101,34,58,34,101,115,105,34,44,34,118,97,108,117,101,34,58,34,123,92,34,99,111,110,116,97,105,110,101,114,92,34,58,123,92,34,100,97,116,97'''
bytes_utf = [123,34,97,112,105,34,58,34,109,116,111,112,46,116,97,111,98,97,111,46,108,98,115,46,112,111,115,115,101,114,118,105,99,101,34,44,34,100,97,116,97,34,58,123,125,44,34,114,101,116,34,58,91,34,83,85,67,67,69,83,83,58,58,-24,-80,-125,-25,-108,-88,-26,-120,-112,-27,-118,-97,34,93,44,34,118,34,58,34,49,46,48,34,125]
bytes_utf8 = [i % 256 for i in bytes_utf]       # -127-128 转256  Java 转 python
print(bytes_utf)
print(bytes_utf8)
a = bytes(bytes_utf8).decode('utf-8')
print(str(a))

# 将字符串转二进制流
str = '{name:哈哈}'
str_b = str.encode()
print(str_b)
str_b_l = [i for i in str_b]
print(str_b_l)