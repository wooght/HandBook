# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseRe.py
@Author     :wooght
@Date       :2024/5/14 16:40
@Content    : 正则表达式
"""

import re

'''
基本字符
    .   可以代替除换行符(\n)以外的任何一个字符
    *   前面的子表达式,字符可以出现0到无限次
    ?   前面的子表达式,字符可以出现0到1次  
    \   特殊字符变成普通字符
    \d  一个数字
    \D  数字以外的所有字符
    ()  子表达式及一个分组,可以提出来
    \w  单词字符 [a-zA-Z0-9_] 包含下划线,但是不包含-
    \s  空白字符,空格,换行符
    \S  非空白字符
    +   前面的子表达式,字符可以出现1次到无限次
    {m} 匹配前一个字符串m次
    {m,n}   匹配前一个字符串m到n次
    ^   匹配模式在字符串开头
    $   匹配模式在字符串末尾
    [^] 否定  [^a-z] 否定小写字母
    
    *? +? ?? {}? 表示非贪婪模式
    
    正则表达式前要加 r
    r'表达式'
'''

"""
    match(pattern, string, flag=0)
    只从字符串的最开始与pattern匹配,匹配成功返回匹配对象(只有一个结果), 否则返回None
"""
s1 = 'abcdef-g123456'
s2 = '.abcw79237'
pattern = re.compile(r"\w+")        # compile 可以不用,只是速度会慢一点
result1 = re.match(pattern, s1)
print(result1.group())              # abcdef 只有一个结果,group(1)会报错
result2 = re.match(pattern, s2)
print(type(result2).__name__)       # NoneType 从第一个位置开始匹配,第一个位置不匹配,则返回None
result11 = re.match(r"\w+", s1)
print(result11.group())             # abcdef
print(result11.span())              # (0, 6) 开始,结束的位置

"""
    search(pattern, string, flag=0)
    方式和match一样,但不一定从第一个位置开始匹配,而是从任意位置开始匹配,只匹配一次,不匹配则返回None
"""
result22 = re.search(r"\w+", s2)
print(result22.group())        # abcw79237

"""
    findall(pattern, string)
    匹配所有,返回一个列表
"""
s3 = 'abc-123-a123'
result3 = re.findall(r'\w+', s3)
print(result3)                  # ['abc', '123', 'a123']
print(result3.count('abc'))     # 1 list.count(s) s在列表中出现的次数

"""
    group()     返回一个匹配项
    groups()    返回包含所有匹配的元祖
"""
s4 = 'wooght@126.com'
result4 = re.search(r'(\w+)@(\w+)\.(\w+)', s4)
print(result4.groups())         # ('wooght', '126', 'com')
result44 = re.search(r'(\w)+@(\w)+\.(\w+)', s4)
print(result44.groups())        # ('t', '6', 'com')
# (\w)+ 表示括号里面的字符可以出现1到无数次,但是必须是一样的字符
# (\w) 表示括号里面只有一个字符

"""
    re 模块的属性    flag
    re.I    匹配不分大小写
    re.S    表示.可以匹配全部字符,包括换行符
"""
s5 = '''one
two
three
'''
result5 = re.match(r'.*', s5, re.S)
print(result5.group())
# one
# two
# three
result55 = re.match(r'.*', s5)
print(result55.group())             # one

html = '''
<html>
    <head>
        <title>网页</title>
    </head>
    <body>
        <div class='one'>
            <p>这里是一个段落</p>
            <img src="abc/abc.jpg" />
        </div>
    </body>
</html>
'''
rhtml1 = re.search(r'<img src=\"(.*)\"', html)
print(rhtml1.group(0))      # <img src="abc/abc.jpg"
print(rhtml1.group(1))      # abc/abc.jpg
# group(0) 表示匹配表达式本身 1表示()

"""
    sub(pattern, repl, string, count=0, flag=0)
    替换  repl 可以是字符串,也可以是有返回值的函数
"""
rhtml2 = re.sub(r'<.*?>', '', html)     # 替换掉网页代码
rhtml2 = re.sub(r'\s', '', rhtml2)      # 替换掉空格和换行符
print(rhtml2)       # 网页这里是一个段落

ii = 0
def abc(mm):
    global ii
    ii += 1
    v = int(mm.group())
    if (v % 2 == 0):
        return str(v / 2)
    return str(v * 2)
s6 = 'A23BB34CCC56'
print(re.sub(r'(\d+)', abc, s6))  # sub 第二个参数是函数的情况
print('共匹配{}次'.format(ii))

result6 = re.sub(r'(\d+)[^\d]+(\d+)', r'\2 \1', s6)
print(result6)              # A34 23CCC56       反向替换

"""
    在网页中的应用
    查找地址
    查找IP
    查找特定值
"""
ip89result = '''
<a href="https://proxy.ip3366.net/" target="_blank" data-type="img"><img src="img/hfad.png"></a><br><script type="text/javascript" src="js/jquery.min.js"></script>
<div id="adarea"onclick=location.href='https://proxy.ip3366.net/' style="cursor: pointer;display: none;position: fixed;right:15px;bottom:15px;width: 285px;height: 250px;background: url(/img/fkad.png) no-repeat;">
<div id="adclose" style="cursor: pointer; position: absolute;  top: 0px;  left: 0px;  display: block;  width: 20px;  height: 20px;font-family: cursive;background: url(img/close.png) no-repeat;" title="点击关闭"> </div>
</div>
<script type="text/javascript">
$(function(){
$('#adarea').slideDown(500);
$('#adclose').click(function(){
$('#adarea').slideUp(500);
});
});
</script>
223.85.12.114:2222<br>182.131.17.19:80<br>112.53.184.170:9091<br>171.221.210.114:80<br>更好用的代理ip请访问：https://proxy.ip3366.net/
'''

href = re.findall(r'(https://[^/]*/)', ip89result)                  # 获取所有网址
print(href)     # ['https://proxy.ip3366.net/', 'https://proxy.ip3366.net/', 'https://proxy.ip3366.net/']
ips = re.findall(r'(\d{3}(\.\d{2,3}){3}:\d{2,5})', ip89result)      # 获取所有IP地址
print(ips)
# [('223.85.12.114:2222', '.114'), ('182.131.17.19:80', '.19'), ('112.53.184.170:9091', '.170'), ('171.221.210.114:80', '.114')]
slide = re.findall(r'slide\w+\((\d+)\)', ip89result)
print(slide)            # ['500', '500']
