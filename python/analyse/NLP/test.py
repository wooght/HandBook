# -*- coding: utf-8 -*-
#
# 基于jieba 的npl应用
# by wooght 2017-11
#

import jieba
import jieba.posseg
import jieba.analyse
import sys,io,re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
jieba.load_userdict("F:\homestead\handbook\python/analyse/NLP/corpus/dict.txt")

s = "航城科技于昨日在纳斯达克上市,上市首日大涨【11.4%】,对于为什么会大涨,我要了，https://www.baidu.com航城科技给出回答表示美国民众看好中国互联网市场前景.航城科技未来是否会继续大涨,经济学家普遍持否定态度."
cutstr = jieba.posseg.lcut(s)
for w in cutstr:
    print(w.word,w.flag)

for x in jieba.analyse.extract_tags(s,withFlag=True,withWeight=True,allowPOS=('n','nts','v','r','p','nz','ad')):
    print(x)
