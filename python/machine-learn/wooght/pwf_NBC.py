# -*- coding: utf-8 -*-
#
# @method   : 原生实现朴素贝叶斯
# @Time     : 2018/4/11
# @Author   : wooght
# @File     : pwf_NBC.py

import numpy as np

# 朴素贝叶斯公式:
# A(A|B) = PA*A(B|A)/PB
# B有N个特征
# A(B|A)PA = A(b1,b2,...bn|A)PA
# 假设N个特征相互独立,互不影响
# 则有: A(b1,b2,...bn|A) = A(b1|A) * A(b2|A)...A(bn|A)
# 由于在实际中通常不需要准确的概率(特征多的情况下,条件概率很低),而只需要概率最大者,故只求分子,不求分母
# 及朴素贝叶斯公式: max(A(类别A|特征),A(类别B|特征),... A(类别N|特征))
# A(类别A|特征集) = {A(b1|A) * A(b2|A)...A(bn|A)} * PA
# 词汇: vector [ˈvɛktɚ] 向量
# vocab ['voʊkæb] 词汇


class ClassifyNB:
    # 流程
    # 创建词汇表
    # 创建各类别向量,默认为1
    # 依次提取样本,获取样本向量,并入对应类别向量
    # 类别向量/类别词汇总数得到概率,再求对数-->得到分类器
    # 预测样本转换为向量,分别和各类别求对数和-->找最大者-->输出预测类别

    # 训练入口
    def fit(self, X, y):
        self.vocabList = self.createVocabList(X)  # 训练所需词汇表
        self.classVec = y  # 分类标签
        self.createNbclassifier(X)  # 创建分类器


    # 创建词汇表
    # 根据训练样本,提取不重复词汇
    def createVocabList(self, dataSet):
        vocabSet = set([])
        for document in dataSet:
            vocabSet = vocabSet | set(document)  # 合并,取不重复词

        return list(vocabSet)


    # 创建文档词向量
    # 和词汇表长度一一对应,出现此则为1 ,未出现则为0
    def createDocumentVector(self, inputSet):
        docVec = [0] * len(self.vocabList)
        for words in inputSet:
            if words in self.vocabList:
                docVec[self.vocabList.index(words)] = 1  # 位置一一对应

        return docVec

    # 创建分类器
    # 获取训练样本词向量
    # 创建各类概率对数向量
    def createNbclassifier(self, dataSet):
        docNums = len(self.classVec)  # 总样本数
        vocabNums = len(self.vocabList)  # 词汇总数
        pPosArr = np.ones(vocabNums)  # 积极面训练向量 默认为1而不是0(平滑处理,防止出现0则全盘为0)
        pNegArr = np.ones(vocabNums)  # 消极面训练向量
        posWords = 2.0  # pos词总数, 单个词/词总数=词概率及条件概率之一P(词|类)
        negWords = 2.0  # 将所有词的初始出现次数设为1,分母默认2  拉普拉斯平滑
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
    # 求各类概率对数  返回最大者
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


if __name__ == '__main__':
    clf = ClassifyNB()
    clf.fit(sampleList, classVec)
    print(clf.predict(['侮辱', '上涨', '单调']))