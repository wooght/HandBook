# -*- coding: UTF-8 -*-

'''
    Python 正则表达式 by wooght 2017
'''

import io
import re
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

'''
    match 只匹配字符串开始
'''
print(re.match('wooght', 'wooght is i').span())     # 在起始位置匹配
reobj=re.match('i', 'wooght is i')
if(reobj):
    #匹配成功后,使用span
    print(re.match('i','wooght is i').span())       #span是获取匹配结果位置,没有匹配结果会报错
else:
    print('None')

'''
    group(n) 获取第n个匹配项
'''
wstr="i Am wooght ,who are you"
wstrmatch=re.match(r'(.*) am (.*?) .*',wstr,re.I)   #re.I 大小写不敏感
if(wstrmatch):
    print(wstrmatch.group())                        #group 匹配的字符串
    print(wstrmatch.group(1))                       #group(num) 匹配的第num个字符串
    print(wstrmatch.group(2))
    print('groups:',wstrmatch.groups())             #groups() 匹配到的所有子匹配


'''
    search 任意位置开始匹配
'''
print('search:',re.search('i','wooght is i').span()) #search 不在起始位置匹配


'''
    sub 替换内容
'''
phone='189-899-876-87'
result=re.sub(r'\-','',phone)
print('del -:',result)
print(phone)
result=re.sub(r'\D',' ',phone)
print(result)

#sub patten参数为函数 将匹配的数字做特定的运算
ii=0
def abc(mm):
    global ii
    ii+=1
    v = int(mm.group('vvv'))
    if(v%2==0):
        return str(v/2)
    return str(v * 2)

s = 'A23BB34CCC56'
print(re.sub('(?P<vvv>\d+)', abc, s))   #sub 第二个参数是函数的情况
print('totle preg is',ii)               #匹配成功一次,调用函数一次


'''
    sub替换 替换规则采用函数的方式
    sub \n  反向引用
'''
def bcd(mm):
    return mm.group(2)+' '+mm.group(1)
patten=re.compile(r'(\w+) (\w+)')
result=re.sub(patten,bcd,'one two three four')  #替换内容为函数  默认传递当前匹配项给函数
print(result)

print(re.sub(patten,r'\2 \1','11 22 33 44'))    #反向替换

str = "<a href='www.baidu.com'>哈哈</a>"
re_str = re.sub(r'<[^<]*>','',str)
print(re_str)
encode_str = str.encode('utf-8')                #str转bytes叫encode，bytes转str叫decode
print(encode_str)

class E(Exception):
    pass
try:
    raise E('Error')
except E as e:
    print(e.args)
try:
    str.decode('utf-8')
except Exception as e:
    print('Error:',e.args)
else:
    #错误保护,如果没有错误执行这里
    print(str.decode('utf-8'))

#split 分割成列表
patten=re.compile(r'\d+')                       #re.compile构造匹配模式
print(re.split(patten,'one1two2three3four'))    #以匹配到的项作为分割点进行分割,并将结果存放列表中

#findall 列表返回匹配项
print(re.findall(patten,'one1two2three3four'))  #将匹配到的项以列表格式返回

preg_str = 'http://jxjump.58.com/service?target=FCADVFdVGJSbUnkeXOrkIYXzkJxLX94M3jVfo7Awk_3UeqgeWIVioRsBqa8f' \
           '-5NvxKrSq4HgscFYojc_URCMrkcZk0qECF3p7KaAnu9_1sWKj6P7ZWagmQq5gfq_kLogGs8t9tDUeWqaMlx0bZ6bDLvHciI' \
           '-TC0mci09YWzkWnYWZHG1cGnr8miwYkZilceudLC0O8UTdkeJ5vIgMOnSlnh0mMCXkDpQWNdnYq3M' \
           '-E7eqOuJGjPE65qoR5b3Y4IdBwcD4&local=102&pubid=25378245&apptype=0&psid=182142276198563518994288059&entinfo' \
           '=32546267038793_0&cookie=||http%3A%2F%2Fcallback.58.com%2Ffirewall%2Fvalid%2F1857562532.do%3Fnamespace' \
           '%3Dershoufangphp%26url%3Dcd.58.com%252Fershoufang%252F32334355244099x.shtml|c5/nn1emJLYQkDf/M8QHAg' \
           '==&fzbref=0&key=&params=esfjxpclranxuanctrAB^desc&cookie=||http%3A%2F%2Fcallback.58.com%2Ffirewall' \
           '%2Fvalid%2F1857562532.do%3Fnamespace%3Dershoufangphp%26url%3Dcd.58.com%252Fershoufang%252F32334355244099x' \
           '.shtml|c5/nn1emJLYQkDf/M8QHAg==&fzbref=0&key=&from=1-list-5 '
x = re.search(r'entinfo=(\d{14})\_',preg_str)
print(x.group(1))