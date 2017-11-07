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
jieba.suggest_freq(("中","将"),tune=True)
print("/".join(jieba.cut("如果放到POST中将出错",HMM=False)))

Original = "/".join(jieba.cut("遂宁市涪江大桥参加了沱江大桥的通车仪式。", HMM = False))
print("Original: " + Original)

#调节词频 freq 频率高低
jieba.add_word("江大桥", freq = 20000, tag = None)
Original = "-".join(jieba.cut("遂宁市涪江大桥参加了沱江大桥的通车仪式。"))
print("Original:"+Original)

jieba.add_word("江大桥", freq = 1, tag = None)
Original = "-".join(jieba.cut("遂宁市涪江大桥参加了沱江大桥的通车仪式。"))
print("Original:"+Original)

#词性
str = jieba.posseg.cut("我爱北京天安门")
for w in str:
    print("%s %s"%(w.word,w.flag))

#textrank 提取关键词 并返回出现频率
#jieba.analyse.set_idf_path('module/jiaba.txt')
s = "此外，公司拟对全资子公司吉林欧亚置业有限公司增资4.3亿元，增资后，吉林欧亚置业注册资本由7000万元增加到5亿元。吉林欧亚置业主要经营范围为房地产开发及百货零售等业务。目前在建吉林欧亚城市商业综合体项目。2013年，实现营业收入0万元，实现净利润-139.13万元。"
for x, w in jieba.analyse.textrank(s, topK = 10, withWeight = True):
    print("%s %s" % (x, w))
#topK  返回几个TF/IDF权重最大的关键词
#withWeight 是否一并返回权重值


#Tokenize 返回词语出现的起止位置 只接受Unicode编码
jieba.suggest_freq(("有限","公司"),tune=True)
#默认模式
result = jieba.tokenize(u"永和服装饰品有限公司")
for tk in result:
    print("%s \t start at: %d \t end at: %d" %(tk[0], tk[1], tk[2]))
#搜索模式
result = jieba.tokenize(u"永和服装饰品有限公司", mode = "search")
for tk in result:
    print("%s \t start at: %d \t end at: %d" % (tk[0], tk[1], tk[2]))
