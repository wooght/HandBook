# -*- coding: utf-8 -*-
#
# @method   : python 原生编写决策树分类
# @Time     : 2018/4/3
# @Author   : wooght
# @File     : pwf_decisiontree.py
# 涉及词条:feature[ˈfitʃɚ] 特征
# decision [dɪˈsɪʒən] 决策
from math import log

# 数据集结构
#                     是否能飞
#                 -----------------
#             不能                  能
#              |                    |
#              b                  是否有翅膀
#                         -----------------
#                         没有              有
#                         b                a

dataSet = {
    'data': [
        [1, 1, 'a'],
        [1, 1, 'a'],
        [1, 0, 'b'],
        [0, 1, 'b'],
        [0, 1, 'b']
    ],
    'features':[
        '是否能飞', '是否有脊椎翅膀'
    ]
}
sampleData = dataSet['data']


# 计算香农熵
# H(B)= -（p(c1)*log (pc1) + p(c2) * log (pc2) +　．．．　+p(cn) *log p(cn))  log底数为2
def shares_shang(shares_data, keys):
    toutle_num = len(shares_data)  # 总行数,总条数
    class_count = {}  # 类别容器
    for item in shares_data:
        if item[keys] not in class_count.keys():
            class_count[item[keys]] = 0  # 添加新类别
        class_count[item[keys]] += 1  # 类别数量加一

    h = 0
    for p in class_count.items():
        prob = p[1] / toutle_num  # 求某类的概率 某类数/总数
        h -= prob * log(prob, 2)  # 概率*概率的对数 然后求和  得到香农熵
    return h


# 筛选指定特征下指定值的数据集
def splitData(dataSet, key, value):
    result = []
    for data in dataSet:
        if data[key] == value:
            beforedata = data[:key]
            beforedata.extend(data[key+1:]) # 以上两步去掉了指定特征
            result.append(beforedata)
    return result


# 选择最佳特征 信息增益最大者
# 信息增益公式
# IG(T) = H(B) - H(B|T)
# H(B|T) = A(t)H(B|t)+A(t`)H(B|t`)  t`是t成立
def bestFeature(dataSet):
    feature_len = len(dataSet[0]) - 1  # 只取前面特征列
    min_shang = 0
    bestfeature = 0
    for i in range(feature_len):
        features = [arr[i] for arr in dataSet]  # 所有特征值
        feature = set(features)  # 不重复的特征值
        shares = 0.0
        for f in feature:
            featdict = splitData(dataSet, i, f)
            share = shares_shang(featdict, -1)  # 计算数据集对应类别信息的信息熵
            shares += len(featdict)/len(dataSet[i]) * share  # 整个特征列对应的信息熵
        if min_shang == 0:
            min_shang = shares
        if shares < min_shang:
            bestfeature = i  # 选择信息熵最小的特征 (由于H(B)相同,这里直接选择H(B|T)最小者)

    return bestfeature


# 同一列占比最高值
def mostCount(dataSet):
    classcount = {}
    for i in dataSet:
        if i not in classcount.keys():
            classcount[i] = 0
        classcount[i] += 1
    sortclasscount = sorted(classcount.items(), key=lambda d:d[0], reverse=True)  # 倒叙排列
    return sortclasscount[0][0]


# 创建决策树(ID3算法)
# ID3算法
#                            选择特征(信息增益最大者)
#                               |
#                           划分数据集
#                               |
#                         是否满足终止条件  否--- 继续选择特征
#                              | 是
#                             结束
def createTree(dataSet):
    classlist = [arr[-1] for arr in dataSet]  # 获取数据集所有类别
    if classlist.count(classlist[0]) == len(classlist):  # 如果只有唯一一类,直接返回结果
        return classlist[0]
    if len(dataSet[0]) == 1:  # 对比完所有特征,结果还不只一类时,直接返回类占比最高的类
        return mostCount(classlist)
    # 选择香农熵最低的特征
    besti = bestFeature(dataSet)  # 选择最佳特征
    feature = [arr[besti] for arr in dataSet] # 最佳特征所有值
    feature = set(feature)  # 不重复值
    Tree = {}  # 多层字典 树原型
    # 构建树支 树{'特征列':分支{'特征值':分支...}}
    for feat in feature:
        if besti not in Tree.keys():
            Tree[besti] = {}  # 树分支原型
        Tree[besti][feat] = createTree(splitData(dataSet, besti, feat))  # 递归构建分支
    return Tree


# 根据决策树分类
def classify(tree, testdata):
    besti = list(tree.keys())[0]  # 获取最佳特征列
    treedict = tree[besti]  # 最佳特阵列分支
    for i in treedict.keys():  # 遍历分支特征值
        if testdata[besti] == i:  # 对比特征值,如果吻合,就进入分支继续比较
            if type(treedict[i]).__name__ == 'dict':  # 如果分支继续有分支,递归判断
                testdata.pop(besti)  # 删除已经比对的特征,里层的分支没有外面已经比对的特征
                return classify(treedict[i], testdata)
            else:  # 如果分支是纯净叶片,直接返回叶片结果
                return treedict[i]


if __name__ == '__main__':
    # 流程:
    # 获取最佳特征(特征分类->分类信息增益->求香农熵)
    # 获取不重复特征,循环遍历特征
    # 递归建立特征分支
    # 递归/分支终止条件:只有一类直接返回类/无特征返回概率大的类->树构建完毕
    # 遍历树最佳特征对应分支的特征值
    # 递归判断分支是否结束,分支__name__是否是__dict
    # 返回分类结果
    tree = createTree(sampleData)
    print(tree)
    result = classify(tree, [1, 0])
    print(result)