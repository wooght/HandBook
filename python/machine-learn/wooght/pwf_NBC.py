# -*- coding: utf-8 -*-
#
# @method   : 原生实现朴素贝叶斯
# @Time     : 2018/4/11
# @Author   : wooght
# @File     : pwf_NBC.py

import numpy as np

# 朴素贝叶斯公式:
# P(A|B) = PA*P(B|A)/PB
# B有N个特征
# P(B|A)PA = P(b1,b2,...bn|A)PA
# 假设N个特征相互独立,互不影响
# 则有: P(b1,b2,...bn|A) = P(b1|A) * P(b2|A)...P(bn|A)
# 由于在实际中通常不需要准确的概率(特征多的情况下,条件概率很低),而只需要概率最大者,故只求分子,不求分母
# 及朴素贝叶斯公式: max(P(类别A|特征),P(类别B|特征),... P(类别N|特征))
# P(类别A|特征集) = {P(b1|A) * P(b2|A)...P(bn|A)} * PA
# 词汇: vector [ˈvɛktɚ] 向量
# vocab ['voʊkæb] 词汇


class ClassifyNB:
    # 训练入口
    def fit(self, X, y):
        self.vocabList = self.createVocabList(X)  # 训练所需词汇表
        self.classVec = y  # 分类标签
        self.createNbclassifier(X)  # 创建分类器


    # 创建词汇表
    def createVocabList(self, dataSet):
        vocabSet = set([])
        for document in dataSet:
            vocabSet = vocabSet | set(document)  # 合并,取不重复词

        return list(vocabSet)


    # 创建文档词向量,和词汇表长度一一对应,出现此则为1 ,未出现则为0
    def createDocumentVector(self, inputSet):
        docVec = [0] * len(self.vocabList)
        for words in inputSet:
            if words in self.vocabList:
                docVec[self.vocabList.index(words)] = 1  # 位置一一对应

        return docVec

    # 创建分类器
    def createNbclassifier(self, dataSet):
        docNums = len(self.classVec)  # 总样本数
        vocabNums = len(self.vocabList)  # 词汇总数
        pPosArr = np.ones(vocabNums)  # 积极面训练向量 默认为1而不是0(平滑处理,防止出现0则全盘为0)
        pNegArr = np.ones(vocabNums)  # 消极面训练向量
        posWords = 0.0  # pos词总数, 单个词/词总数=词概率及条件概率之一P(词|类)
        negWords = 0.0
        negClassNums = 0  # neg样本数
        for i in range(docNums):
            tmpVec = self.createDocumentVector(dataSet[i])  # 词向量
            if classVec[i] == 'pos':
                pPosArr += tmpVec
                posWords += sum(tmpVec)  # 出现单词个数
            else:
                pNegArr += tmpVec
                negWords += sum(tmpVec)
                negClassNums += 1

        self.pPosVec = np.log(pPosArr / posWords)  # 求对数,防止下溢出(如0.001*0.003*0.0009...越乘越小)
        self.pNegVec = np.log(pNegArr / negWords)
        self.pNeg = negClassNums / docNums


    # 分类预测
    def predict(self, X):
        documentVec = self.createDocumentVector(X)
        pdPos = sum(documentVec * self.pPosVec) + np.log(1-self.pNeg)  # log(AB) = logA + logB
        pdNeg = sum(documentVec * self.pNegVec) + np.log(self.pNeg)
        if pdPos > pdNeg:
            return ('pos', pdPos)
        else:
            return ('neg', pdNeg)



sampleList = [['给力', '好样的', '上涨', '恭喜', '旺旺', '赚翻天'],
              ['不行', '弱势', '下滑', '压力', '衰', '亏本'],
              ['榜样', '支持', '大卖', '天天向上', '正能量'],
              ['甩卖', '损坏', '质量差', '侮辱', '单调', '没什么']]
classVec = ['pos', 'neg', 'pos', 'neg']


clf = ClassifyNB()
clf.fit(sampleList, classVec)
print(clf.predict(['侮辱', '上涨', '单调']))