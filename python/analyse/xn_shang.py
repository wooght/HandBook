# -*- coding: UTF-8 -*-
#
# 香农熵(消息熵)算法
# by wooght 2017-11
# 依赖: log 对数
# 表示随机变量不确定性，即混乱程度的量化指标 熵越大，不确定性越大
# = -（p1*log p1 + p2 * log p2 +　．．．　+pn *log pn)  log底数为2
from math import log


#测试数据
# 政策,正面,负面,前期涨跌
shares_data = [
                {'zc':1,'zm':1,'fm':2,'zd':0},
                {'zc':1,'zm':1,'fm':2,'zd':2},
                {'zc':1,'zm':1,'fm':0,'zd':0},
                {'zc':1,'zm':0,'fm':2,'zd':2},
                {'zc':1,'zm':1,'fm':0,'zd':0},
                {'zc':1,'zm':0,'fm':2,'zd':1},
                {'zc':2,'zm':3,'fm':0,'zd':1},
                {'zc':1,'zm':1,'fm':2,'zd':2},
                {'zc':1,'zm':4,'fm':1,'zd':0},
                {'zc':1,'zm':1,'fm':1,'zd':2},
                {'zc':1,'zm':0,'fm':1,'zd':0},
                ]

#计算香农熵
def shares_shang(shares_data,keys):
    toutle_num = len(shares_data)                   #总行数,总条数
    class_count = {}                                #类别容器
    for item in shares_data:
        if(item[keys] not in class_count.keys()):
            class_count[item[keys]] = 0             #添加新类别
        class_count[item[keys]]+=1                  #类别数量加一

    h = 0
    print(class_count)
    for p in class_count.items():
        prob = p[1]/toutle_num                      #求某类的概率 某类数/总数
        h -= prob * log(prob,2)                     #概率*概率的对数 然后求和  得到香农熵
    return h
print('负面的香农熵:',shares_shang(shares_data,'fm'))
print('政策的香农熵:',shares_shang(shares_data,'zc'))
print('涨跌的香农熵:',shares_shang(shares_data,'zd'))
print('正面的香农熵:',shares_shang(shares_data,'zm'))
