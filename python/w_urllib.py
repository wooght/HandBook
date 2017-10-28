# -*- coding: UTF-8 -*-

import urllib
import urllib.request as wurl
import http.cookiejar
#import request
#import urllib3

# num=0
# with wurl.urlopen('http://homestead') as link:
#     num+=1
#     print(link.read())
#     print('num is :',num)

url='http://homestead'
response=wurl.urlopen(url)  #打开地址
print(response.read())      #读取内容


#使用到request,目的在于对请求添加请求参数
request=wurl.Request(url)                       #建立一个请求,Request 这里需要大写首字母
response=wurl.urlopen(request)                  #打开请求
print(response.read().decode('utf-8'))          #读取请求返回的内容


posts={'email':'wooght@126.com','password':'111111'}
#header 内容 具体内容参见 pythonurllib.php
user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
headers={'User-Agent':user_agent,'Referer':"http://homestead/login"}        #referer 指定来源
data=urllib.parse.urlencode(posts).encode(encoding='utf-8')                 #传输内容编码 encode用法 Python3
url='http://homestead/pythonurllib.php?from=http://homestead'               #指明了来源地址
request=wurl.Request(url,data,headers)
response=wurl.urlopen(request)
print(response.read().decode('utf-8'))

#读取登录页面cookie
url='http://homestead/login'
cookie = http.cookiejar.CookieJar()  # 声明一个CookieJar对象实例来保存cookie
handler = wurl.HTTPCookieProcessor(cookie)  # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
opener = wurl.build_opener(handler)  # 通过handler来构建opener
request = wurl.Request(url)
response = opener.open(request)  # 此处的open方法同urllib2的urlopen方法，也可以传入request
for item in cookie:
    print(item.name,':',item.value)
# request=wurl.Request(url)
# try:
#     response=wurl.urlopen(request)
#     resulthtml=response.read()
#     print(resulthtml.decode('utf-8'))                                       #编码需要输出的内容 默认不是与前置设定不同
# except urllib.error.HTTPError as e:
#     print('ERROR',e)
# except urllib.error.URLError as e:                                          #http异常
#     print(e)
