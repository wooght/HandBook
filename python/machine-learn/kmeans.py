# -*- coding: utf-8 -*-
#
# @method   : scikit-learn 之 KMeans (K均值聚类)
# @Time     : 2018/3/29
# @Author   : wooght
# @File     : kmeans.py

import numpy as np
from sklearn.cluster import KMeans

data = np.random.rand(100, 3)  # 生成一个随机数据，样本大小为100, 特征数为3
print(data)

# 聚类基本应用
# 构造一个聚类数为3的聚类器, 及需要分成3个类
estimator = KMeans(n_clusters=3)  # 构造聚类器
estimator.fit(data)  # 聚类 训练得到模型
label_pred = estimator.labels_  # 获取聚类标签
centroids = estimator.cluster_centers_  # 获取聚类中心
inertia = estimator.inertia_  # 获取聚类准则的总和
print(label_pred, centroids)
print(inertia)
print('新样本属于:', estimator.predict([[0.8, 0.8, 0.8]]))  # 对新进样本进行归类
print(estimator.fit_predict(data))  # 训练并直接输出结果

import jieba
from sklearn.feature_extraction.text import TfidfVectorizer


def jieba_tokenize(text):
    print(jieba.lcut(text))
    return jieba.lcut(text)


tfidf_vectorizer = TfidfVectorizer(tokenizer=jieba_tokenize, lowercase=False)
'''
tokenizer: 指定分词函数
lowercase: 在分词之前将所有的文本转换成小写，因为涉及到中文文本处理，
所以最好是False
'''
text_list = ["今天的天气真好", "小明上了清华大学", "我今天拿到了Google的Offer", "清华大学在自然语言处理方面真厉害", "今天晚上回家很晚"]
# 需要进行聚类的文本集
tfidf_matrix = tfidf_vectorizer.fit_transform(text_list)
print(tfidf_matrix)

km_cluster = KMeans(n_clusters=3, max_iter=3, n_init=1, init='k-means++', n_jobs=1)
'''
n_clusters: 指定K的值
max_iter: 对于单次初始值计算的最大迭代次数
n_init: 重新选择初始值的次数
init: 制定初始值选择的算法
n_jobs: 进程个数，为-1的时候是指默认跑满CPU
注意，这个对于单个初始值的计算始终只会使用单进程计算，
并行计算只是针对与不同初始值的计算。比如n_init=10，n_jobs=40, 
服务器上面有20个CPU可以开40个进程，最终只会开10个进程
'''
# 返回各自文本的所被分配到的类索引
result = km_cluster.fit_predict(tfidf_matrix)
print("聚类标签:", result)

words_model = km_cluster.fit(tfidf_matrix)
test_matrix = tfidf_vectorizer.fit_transform(['明天下午/解放路佛恩惊世毒妃建瓯市如我减肥放假了的时间反垄断法二季度晶方科技晚上回家吗'])
print(words_model.labels_.tolist())  # 分类标签变list
print(words_model.predict(test_matrix))  # 对新进样本进行归类

from sklearn.externals import joblib
joblib.dump(km_cluster, './data/test_km.pkl')  # 存储模型  joblib.load() 加载模型