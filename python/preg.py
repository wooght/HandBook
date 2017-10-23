# -*- coding: UTF-8 -*-

'''
    Python 正则表达式 by wooght 2017
'''
import re

#match 只匹配字符串开始
print(re.match('wooght', 'wooght is i').span())  # 在起始位置匹配
reobj=re.match('i', 'wooght is i')
if(reobj):
    #匹配成功后,使用span
    print(re.match('i','wooght is i').span()) #span是获取匹配结果,没有匹配结果会报错
else:
    print('None')

wstr="i Am wooght ,who are you"
wstrmatch=re.match(r'(.*) am (.*?) .*',wstr,re.I)#re.I 大小写不敏感
if(wstrmatch):
    print(wstrmatch.group())#group 匹配的字符串
    print(wstrmatch.group(1))#group(num) 匹配的第num个字符串
    print(wstrmatch.group(2))
    print(wstrmatch.groups())#groups() 匹配到的所有子匹配

#任何位置匹配
print(re.search('i','wooght is i').span()) #search 不在起始位置匹配


#sub 替换
phone='189-899-876-87'
result=re.sub(r'\-','',phone)
print('del -:',result)
print(phone)
result=re.sub(r'\D',' ',phone)
print(result)

# 将匹配的数字做特定的运算
ii=0
def abc(mm):
    global ii
    ii+=1
    v = int(mm.group('vvv'))
    if(v%2==0):
        return str(v/2)
    return str(v * 2)

s = 'A23BB34CCC56'
print(re.sub('(?P<vvv>\d+)', abc, s))#sub 第二个参数是函数的情况
print('totle preg is',ii)
