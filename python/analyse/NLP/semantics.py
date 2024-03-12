# -*- coding: utf-8 -*-
#
# 语义分析 wooght
# by wooght
# 2017-11
#
import marshal
import os
from math import log, exp

from frequency import freq
from participle import pp

data_path = os.path.dirname(__file__)+"/corpus/"

import sys,io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

class seman(object):
    def __init__(self):
        self.words = {}
        self.ask = {}
        self.total = 0
        self.pass_words = {'x','m','url','eng','nts'}

    #加载序列化数据
    def load(self,path):
        f = open(path,'rb')
        arr = marshal.load(f)
        for i in arr:
            self.ask[i] = freq()
            self.ask[i].__dict__ = arr[i]
            self.total+=arr[i]['total']
        f.close()

    #加载语料库
    def load_corpus(self,pospath,negpath):
        map_list = [('pos',pospath),('neg',negpath)]
        for map in map_list:
            lines = []
            f = open(map[1],'r',encoding='utf-8')
            for l in f.readlines():
                lines.append(l.strip())
            f.close()
            self.pp_rate(map[0],lines)

    #简单分词
    def pp(self,str):
        pp_words = pp.flag_cut(str)
        words = []
        for word in pp_words:
            if(word.flag not in self.pass_words):
                words.append(word.word)
        return words

    #分词,计词频
    def pp_rate(self,map,lines):
        totle = 0
        dicts = {}
        for line in lines:
            words = pp.flag_cut(line)
            for word in words:
                if(word.flag not in self.pass_words):
                    if(word.word not in dicts):
                        dicts[word.word]=1
                    else:
                        dicts[word.word]+=1
                    totle+=1
        dicts['total'] = totle
        self.words[map] = dicts

    #序列化数据
    def save(self,path):
        f = open(path,'wb')
        marshal.dump(self.words,f)
        f.close()

    #贝叶斯概率
    def bayes(self, askwords):
        log_num = {}
        for i in self.ask:
            log_num[i] = log(self.ask[i].total) - log(self.total)               #组单词总量的对数差 <0
            for word in askwords:
                log_num[i] += log(self.ask[i].freq(word)[0])                    #所在组的频率对数 <<0
        ret, prob = '', 0
        for k in self.ask:
            exp_num = 0
            try:
                for otherk in self.ask:
                    exp_num += exp(log_num[otherk]-log_num[k])                  #exp_num = 1+对数差的幂 注意这里减数和被减数
                exp_num = 1/exp_num
            except OverflowError:
                exp_num = 0
            if exp_num > prob:
                ret, prob = k, exp_num                                          #返回概率大的概率和标识
        return (ret, prob)

    #态度分析
    def attitude(self,str):
        words = self.pp(str)
        print(words)
        ret,prob = self.bayes(words)
        if(ret=='neg'):
            return 1-prob
        return prob


seman = seman()
seman.load(data_path+"semantics.wooght")

# if(__name__=='__main__'):
#     import sys,io
#     sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
#     seman.load_corpus(data_path+"positive.txt",data_path+"negative.txt")
#     seman.save(data_path+"semantics.wooght")

print(seman.attitude('乐视影业背后星光熠熠的大咖们可能无法在乐视网完成套现，乐视影业股权可能会被万达 或者光线 甚至阿里收购'))
