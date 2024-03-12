# -- coding: utf-8 -
"""
@project    :HandBook
@file       :BaseString.py
@Author     :wooght
@Date       :2024/3/3 11:37
"""

"""
    字符串切片
    [start:end:步长]  步长为-时,表示从后往前
"""
test_str = 'abcdef'
print(test_str[2:])     # cdef
print(test_str[:-1])    # abcde
print(test_str[1:3])    # bc
print(test_str[:-2:2])  # ac
print(test_str[::-1])   # fedcba    字符串快速倒序的方法


"""
    string.find(str,__start,__end)
    查找子字符串第一次出现的位置
    找到则返回位置,未找到返回-1
    rfind()和find一样，只是从右边开始找
    return num
"""
bst = "basestring_base"
cst = "se"
# 全局查找
print(bst.find(cst))  # 2
# 指定位置查找
print(bst.find(cst, 1, 2))  # -1
print(bst.rfind(cst))  # 13

"""
    string.index(str,__start,__end)
    查找目标字符串第一次出现的位置
    找到则返回位置，未找到则抛出ValueError异常
    index()可用于字典
    return num/ValueError
"""
print(bst.index(cst))  # 2
try:
    bst.index(cst, 5, 8)
except ValueError:
    print('ValueError 异常')  # 运行

"""
    sub in str 判断sub是否在str中 返回布尔值
    return True/False
"""
print(cst in bst)  # True
base_dict = [1, 2, 3]
son_dict = 2
print(son_dict in base_dict)  # True
if [2] not in base_dict:
    print('[2] 不在[1,2,3]中')

"""
    string.count(str,__start,__end)
    返回子字符串在目标字符串中出现的次数
    无则返回0
    return num
"""
cst = "abc_abc_abc"
fst = "abc"
dst = "bb"
print(cst.count(fst))  # 3
print(cst.count(bst))  # 0

"""
    string.strip(str) 
    去掉字符串中首尾特定的内容
    参数为空时表示去掉空格
    string.rstrip(str) 删除尾部指定内容
    string.lstrip(str) 删除首部指定内容
    return new string
"""
str = " Base String"
print(str)  # 输出 Base String
print(str.strip())  # 输出Base String
print(str.strip('g'))  # 输出 Base Strin
print(str.rstrip('g'))  # # 输出 Base Strin

"""
    string.replace(old_str,new_str,num)
    将string字符串中的old_str替换为new_str,共替换num次,不指定num为全部替换
    会产生一个新的string,不改变原来的string
    return new string
"""
str = "abc_abc_abc"
m_str = "abc"
new_str = "bcd"
print(str.replace(m_str, new_str))  # bcd_bcd_bcd
print(str.replace(m_str, new_str, 2))  # bcd_bcd_abc

"""
    string.split(str,num)
    按照分隔符str分割字符串,num表示分割次数
    无num则全分割
    return list
"""
str = "you and me,you and me"
c_str = "and"
print(str.split(c_str))  # ['you ', ' me,you ', ' me']
print(str.split(c_str, 1))  # ['you ', ' me,you and me']

"""
    seq.join(string)
    用seq作为连接符连接string字符串中的所有字符,注意这里不是单词,而是字符
    return new string
"""
str = "你好吗"
seq = "-"
print(seq.join(str))  # 你-好-吗
# len(string)   返回字符串的长度
print(len(str))  # 3
print("-" * 10)  # ----------


"""
    string.format()
    格式化字符串
    {}和format(变量) 一一对应赋值
    {}和format(*列表) 列表一一对应赋值,注意* 
    
    {name}和format(name=name) 指定赋值,可以多次引用
    f'string{var}string' 字符串前面加f,字符串{}中可以直接使用变量
"""
num1, num2 = 10, 20
message = "我们有{}个人,现在有{}个苹果,没人可以吃{}个".format(num1, num2, num2 / num1)
print(message)  # 我们有10个人,现在有20个苹果,没人可以吃2.0个
fruit = ["苹果", "香蕉", "桃子"]
message = "{},{}和{}都是水果".format(*fruit)     # * 意思是将列表中的元素展开作为单独的参数传递给函数,及不定长函数参数的应用
print(message)  # 苹果,香蕉和桃子都是水果
my_name, my_age = "张三", 18
string_module = "我叫{my_name},今年{my_age}岁了,她今年也{my_age}岁了"
print(string_module.format(my_name=my_name, my_age=my_age))     # # 我叫张三,今年18岁了,她今年也18岁了
message = f"我叫{my_name},今年{my_age}岁了,她今年也{my_age}岁了"
print(message)  # 我叫张三,今年18岁了,她今年也18岁了

"""
    string % (variable) 格式化字符串
    %s 字符串
    %d 整数   %0nd 表示补齐n位数
    %f 浮点数  %.nf 表示保留n位小数
"""
num1, num2, num3 = 10, 20, 25
message = "我们有%s个人,现在有%d个苹果,没人可以吃%02d个" % (num1, num2, num2 / num1)
print(message)  # 我们有10个人,现在有20个苹果,没人可以吃02个
message = "我们有%s个人,现在有%d个苹果,没人可以吃%.4f个" % (num2, num3, num3 / num2)
print(message)  # 我们有20个人,现在有25个苹果,没人可以吃1.2500个
message = "现在是%(week)s下午%(hour)d点" % {"week": "星期天", "hour": 5}
print(message)  # 现在是星期天下午5点


"""
    终端输出美化
    str()返回用户易读的表达形式
    repr()返回解释器易读的表达形式
    str.rjust(num,fillchar) 右对齐字符串,num是对齐后的总宽度,fillchar时填充的字符,默认是空格
    format中,:表示格式符,:num表示站位num,不足空格填充,默认居左
"""
test_list = [[repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4)] for x in range(3,8)]
for item in test_list:
    print(item)
# [' 3', '  9', '  27']
# [' 4', ' 16', '  64']
# [' 5', ' 25', ' 125']
# [' 6', ' 36', ' 216']
# [' 7', ' 49', ' 343']
test_list = ['{:1d},{:2d},{:3d}'.format(x, x*x, x*x*x)for x in range(3,8)]
for item in test_list:
    print(item)
# 3, 9, 27
# 4,16, 64
# 5,25,125
# 6,36,216
# 7,49,343
"""
    字符串编码
    str.encode(encoding=, errors=) encoding默认是 bytes,及字节码
"""
str_1 = "中文字"
print(str_1.encode())       # b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97'
str_2 = str_1.encode('utf-8')
print(str_2)                # b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97'
print(str_2.decode())       # 中文字
print("-" * 100)

"""
    字符串函数应用
    len(str) 返回str长度
"""
str = "*重大新闻-德国总理承认国防部录音事件-称非常严重-将调查*"
print("长度:", len(str), "内容:" + str)
if str.find("总理"):
    print('确认是总理')
    if "德国" in str:
        print("确认为德国总理")
        seq = "*"
        if str.find(seq) == 0 and str.rfind(seq) > 0:
            new_str = str.strip(seq)
            print(new_str)
            print(new_str.replace("-", ","))
            if (new_str.count("-")) > 0:
                list_words = new_str.split("-")
                print(list_words)
                print("输出所有字句:", "[" + "][".join(list_words), "]")
                just_words = new_str.replace('-', '')
                all_words_string = ",".join(just_words)
                print("输出所有汉字:", all_words_string)
                print("输出所有汉字:", all_words_string.split(','))

target_string = "掌握这些方法,轻松解决python的入门问题,如:WEB框架-爬虫框架-数据分析*"
print("长度:", len(target_string), "内容:", target_string)
if target_string.find("*") == len(target_string) - 1:
    strip_string = target_string.strip("*")
    print("去除收尾特殊字符", strip_string)
    if strip_string.count("-") > 0:
        count_string = strip_string.replace("-", ",")
        print("替换-的结果:", count_string)
        sentence_list = count_string.split(",")
        print("有这些短句:", sentence_list)
        no_symbol_string = strip_string.replace(",", "")
        every_words = ",".join(no_symbol_string)
        print("有这些字:", every_words)
        print("有这些字:", every_words.split(","))