import jieba
import jieba.posseg
import jieba.analyse

#cut_all=True 全模式
seg = jieba.cut("我毕业于攀枝花学院计算机系",cut_all=True)
print("FullMode:"+"/".join(seg))

#cut_all=False 精确模式 默认
seg = jieba.cut("我毕业于攀枝花学院计算机系",cut_all=False)
print("FullMode:"+"/".join(seg))

seg = jieba.cut("我毕业于攀枝花学院计算机系")
print("FullMode:"+"/".join(seg))

#cut_for_search 搜索引擎模式
seg = jieba.cut_for_search("我毕业于攀枝花学院计算机系")
print("Search Mode:"+"/".join(seg))

#引入自定义字典
jieba.load_userdict("module/jiaba.txt")

seg_list = jieba.cut("蒲文锋是python爬虫砖家也是云计算方面的专驾。")
print("Origin: " + "/".join(seg_list))

#动态调整词典
jieba.add_word("专驾")
#del_word()删除单词

print("/".join(jieba.cut("如果放到POST中将出错",HMM=False)))

#调节词频 使中，将可以分出来
jieba.suggest_freq(("中","将"),tune=True)     #tune True 分出来,False不单独分出来
print("/".join(jieba.cut("如果放到POST中将出错",HMM=False)))

Original = "/".join(jieba.cut("遂宁市涪江大桥参加了沱江大桥的通车仪式。", HMM = False))
print("Original: " + Original)

#调节频率 freq 频率高低
jieba.add_word("江大桥", freq = 20000, tag = None)
Original = "-".join(jieba.cut("遂宁市涪江大桥参加了沱江大桥的通车仪式。"))
print("Original:"+Original)

jieba.add_word("江大桥", freq = 1, tag = None)
Original = "-".join(jieba.cut("遂宁市涪江大桥参加了沱江大桥的通车仪式。"))
print("Original:"+Original)


print(jieba.lcut("360借壳上市"))    #lcut 直接返回list格式
print(jieba.cut("360借壳上市"))     #cut得到cut对象,但可以for in 出来
jiebacut = jieba.cut("360借壳上市")
for i in jiebacut:
    print(i)

#词性 posseg.cut切去并获取词性
str = jieba.posseg.cut("我爱北京天安门,我也爱成都天府广场,我在否定南方")
for w in str:
    print("%s %s"%(w.word,w.flag))


# a:        形容词
# b:        区别词
# c:        连词
# d:        副词
# e:        叹词
# g:        语素字
# h:        前接成分
# i:        习用语
# j:        简称
# k:        后接成分
# m:        数词
# n:        普通名词
# nd:        方位名词
# nh:        人名
# nt:        机构名
# nl:        处所名词
# ns:        地名
# nt:        时间词
# nz:        其他专名
# o:        拟声词
# p:        介词
# q:        量词
# r:        代词
# u:        助词
# v:        动词
# wp:        标点符号
# ws:        字符串
# x:        非语素字


#textrank 提取关键词 并返回权重
# jieba.analyse.set_idf_path('module/jiaba.txt')  关键词语料库  格式: 单词 权重  如:航城科技  13.1112121

print('关键词提取,返回权重:')
s = "航城科技与昨日在纳斯达克上市,上市首日大涨11.4%,对于为什么会大涨,航城科技给出回答表示美国民众看好中国互联网市场前景.航城科技未来是否会继续大涨,经济学家普遍持否定态度."
cutstr = jieba.lcut(s,cut_all=False)
print(cutstr)

tags = jieba.analyse.extract_tags(s, topK = 15, withWeight = False)
print(tags)

#计算关键词词频
def str_freq(str):
    word_freq = {}
    for word in tags:
        word_freq[word]=0
        for w in cutstr:
            if(word==w):
                word_freq[word]+=1
    #sorted排序用法
    return sorted(word_freq.items(),key=lambda d:d[1],reverse=True)      #reverse True降序, False默认升序 ,key 指对元素的某一部分进行排序

word_freq = str_freq(tags)
for i,n in word_freq:
    print(i+'-','\t\t',n)

#返回关键词和其权重
for x, w in jieba.analyse.extract_tags(s, topK = 15, withWeight = True,allowPOS=('nt','v','n','a')):
    print("%s %s" % (x, w))
#topK  返回几个TF/IDF权重最大的关键词
#withWeight 是否一并返回权重值
# allowPOS 返回的词性


#Tokenize 返回词语出现的起止位置 只接受Unicode编码
#默认模式
result = jieba.tokenize(u"永和服装饰品有限公司")
for tk in result:
    print("%s \t start at: %d \t end at: %d" %(tk[0], tk[1], tk[2]))
#搜索模式
jieba.suggest_freq(("有限","公司"),tune=True)
str = u"永和服装饰品有限公司饰品"
result = jieba.tokenize(str, mode = "search")
zb = {}
for tk in result:
    zb[tk[0]]=[tk[1],tk[2]]
    print("%s \t start at: %d \t end at: %d" % (tk[0], tk[1], tk[2]))
print(zb)

#在原字符串中高亮显示指定词语
def gaoliang(zb,str):
    return str[0:zb[0]]+'['+str[zb[0]:zb[1]]+']'+str[zb[1]:]
print(gaoliang(zb['有限'],str))
