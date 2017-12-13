# -*- coding: utf-8 -*-
#
# 分词,jieba
# by wooght
# 2017-11
#
import os,re
import jieba
import jieba.posseg
import jieba.analyse

data_path = os.path.dirname(__file__)+"/corpus/"
jieba.load_userdict(data_path+"dict.txt")
stop_path = data_path+'stopwords.txt'
jieba.analyse.set_stop_words(stop_path)

# import sys,io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

class pp(object):
    def __init__(self):
        self.seg = jieba.posseg
        self.stop_words = []
    def load(self,fname):
        f = open(fname,'r',encoding='utf-8')
        words = f.readlines()
        for l in words:
            self.stop_words.append(l.strip())
        f.close()
    def cut_ju(self,str):
        ju_re = re.compile('[。？?]')
        ju = ju_re.split(body_str)
        return ju
    def lcut(self,str):
        cutstr = jieba.lcut(str)
        words = []
        for word in cutstr:
            if(word not in self.stop_words):
                words.append(word)
        return words
    def flag_cut(self,str):
        cutstr = self.seg.lcut(str)
        words = []
        for word in cutstr:
            if(word.word not in self.stop_words and word.flag!='x'):
                words.append(word)
        return words
    def tags(self,str,allpos=('n','nt','nts','ntp','v','a','i','d','y','r','p','nz','ad')):
        return jieba.analyse.extract_tags(str,withWeight=True,withFlag=True,allowPOS=allpos)

pp = pp()
pp.load(stop_path)      #加载停用词

# s = "航城科技于昨日在纳斯达克上市,我问不会吧,上市首日大涨【11.4%】,对于为什么会大涨，https://www.baidu.com航城科技给出回答表示美国民众看好中国互联网市场前景.航城科技未来是否会继续大涨,经济学家普遍持否定态度."
# word = pp.lcut(s)
# print(word)
