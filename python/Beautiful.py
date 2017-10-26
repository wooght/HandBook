# -*- coding: UTF-8 -*-

from bs4 import BeautifulSoup
import urllib
import urllib.request as wurl
import re

#读取页面内容 保存到html中
url='http://homestead'
request=wurl.Request(url)
response=wurl.urlopen(request)
html=response.read().decode('utf-8')

#创建BeautifulSoup对象
soup=BeautifulSoup(html,"html.parser")
#print(soup)             #原样输出
#print(soup.prettify())  #节点格式化输出

#获取tag
print(soup.title)       #输出 <title>BlogWooght</title>
print(soup.head)        #如上,输出了head标签及里面素有内容
print(soup.head.title)  #对象化输出指定位置内容 输出<title>BlogWooght</title>

#获取tag名称
print(soup.title.name)  #输出标签名字 输出:title

#获取tag的属性
print(soup.div.attrs)           #打印第一个div标签的所有属性 {'class': ['top'], 'name': 'top'}
print(soup.div.get('class'))    #打印指定属性值 ['top']
print(soup.div['class'])        #同上

#修改属性
soup.div['class']='wooght'      #修改属性
print(soup.div['class'])        #输出 wooght  这里是字符串  不是列表

#删除属性
del soup.div['class']           #删除属性
print(soup.div)

#类型
s=soup.span.string              #得到标签里面的内容 如果其下无文字内容而是其他标签 则返回null
print(s)
print(type(s))                  #得到文本的类型:<class 'bs4.element.NavigableString'>


#contents 子节点列表
print(soup.div.contents)        #得到子节点列表 可以进行列表应用
for div in soup.div.contents:   #子节点包括 换行,注释等
    if(div!='\n'):
        print(div,type(div))
    else:
        print('null',type(div))
#输出结果如下
# null <class 'bs4.element.NavigableString'> 换行符类型通字符串类型 NavigableString
# <span class="index"><a href="/">Blog-wooght</a></span> <class 'bs4.element.Tag'>  标签类型 tag
# null <class 'bs4.element.NavigableString'>
# 判断是否是游客 <class 'bs4.element.Comment'> 注释类型 comment
# null <class 'bs4.element.NavigableString'>
# <span class="f_right"><a href="http://homestead/register">注册</a></span> <class 'bs4.element.Tag'>
# null <class 'bs4.element.NavigableString'>
# <span class="f_right"><a href="http://homestead/login">登陆</a></span> <class 'bs4.element.Tag'>
# null <class 'bs4.element.NavigableString'>
# 不是游客运行 <class 'bs4.element.Comment'>
# null <class 'bs4.element.NavigableString'>

print('0:',soup.div.contents[1])        #可以获取列表的某一个

#children 子节点,只能获取一个  但可以遍历
for child in soup.div.children:         #和contents一样 得到所有子标签 包括换行,注释
    print('child:',child)

#descendants  所有子孙节点
for child in soup.table.descendants:    #获取内容同上两者
    print('descendants:',child)

#stripped_strings 所有内容 需要遍历 string指一个,strings指所有,但包括空格,  stripped_strings不包括空格
for string in soup.div.stripped_strings:
    print('string:',string)

#parent 父节点
print(soup.div.parent.name)             #得到 body


#兄弟节点 next_sibling 下一个 previous_sibling 前一个
print(soup.div.next_sibling.name)       #输出空  因为换行也是一个节点

#next_siblings 全部兄弟节点
for nextname in soup.div.next_siblings:
    if(nextname.name!=None):
        print(nextname.name)

print('----------------------------------------------------------------------------')
#find_all() 方法 搜索文档树
#print(soup.find_all('div'))                        #查找出所有 tag 为div的 字符串会被忽略掉
t=soup.find_all(re.compile(r'^t'))                  #查找所有t开头的tag
for tt in t:
    print(tt.name)

print(soup.find_all(['a','img']))                   #查询列表下的tag

def has_class_no_name(tagg):
    return tagg.has_attr('class') and not tagg.has_attr('name')
tagg=soup.find_all(has_class_no_name)               #find_all 使用函数进行匹配
for tname in tagg:
    print(tname['class'])

print(soup.find_all(class_='fanye'))                   #查询class为fanye的tag  class为保留字,所以用class_
print(soup.find_all(href=re.compile(r'^\/page')))      #查询href 为匹配表达式的tag
tags=soup.find_all(text=[re.compile(r'发布'),'首页'])   #搜索文字 及某个标签下的string
for tt in tags:
    print(tt)

tags=soup.select(".article_list")                       #查找class 名为article_list的tag
for tt in tags:
    print(tt.name)

tags=soup.select("a")                                   #查询所有a标签
for tt in tags:
    print(tt['href'])
