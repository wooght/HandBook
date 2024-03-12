# -*- coding: UTF-8 -*-

import http.cookiejar
import urllib
import urllib.request as wurl

from bs4 import BeautifulSoup

url='http://homestead/admin/login'

token=''
'''#读取token'''
def read_token(html):
    # #建立请求实例
    # token_request=wurl.Request(url)
    # #获得响应
    # token_resopnse=wurl.urlopen(token_request)
    # #得到内容
    # token_html=token_resopnse.read()

    global token
    token_soup=BeautifulSoup(html,"html.parser")            #创建BS实例
    print(token_soup.find_all('input',type='hidden'))       #查询inpu type为hidden
    token_input=token_soup.select('input[name="_token"]')   #搜索input name=_token
    token = token_input[0]['value']
    print(token)

'''#读取cookie'''
def get_cookie():
    global url
    cookie=http.cookiejar.CookieJar()           #声明一个cookiejar 来保存cookie
    handler = wurl.HTTPCookieProcessor(cookie)  #创建cookie处理器,并绑定到cookiejar
    opener = wurl.build_opener(handler)         #通过cookie处理器来构建opener
    response = opener.open(url)                 #opener的open来获得cookie,执行爬取
    read_token(response.read().decode('utf-8'))
    for item in cookie:
        print(item.name,':',item.value)
    return cookie

# cookie请求过程:
# 1声明保存cookie变量
# 2创建cookie处理器,并绑定到变量上
# 3通过处理器来构建opener
# 4通opener执行open来访问页面,及爬取和获取cookie


'''数据处理'''
def data_exit(html):
    soup = BeautifulSoup(html,"html.parser")
    #div_box=soup.find_all(class_=re.compile(r'^progress-bar .*'))
    div_box=soup.find_all(class_='progress-group')
    for smail_div in div_box:
        print(smail_div.contents[1].string,smail_div.div.div['style'][7:9])


handler = wurl.HTTPCookieProcessor(get_cookie())                #调用函数,获取cookie
opener = wurl.build_opener(handler)                             #构建opener

'''post请求包,header包'''
posts={'email':'wooght@126.com','password':'111111','_token':token}
user_agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
headers={'User-Agent':user_agent,'Referer':url}

data=urllib.parse.urlencode(posts).encode(encoding='utf-8')     #请求数据编码
request=wurl.Request(url,data,headers)                          #通过数据,header创建请求
try:
    response=opener.open(request)                               #打开,执行爬取
    print('now status:',response.getcode())                     #response.getcode() 获取当前爬去链接状态
    data_exit(response.read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(e)
