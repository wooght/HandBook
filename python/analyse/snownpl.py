#encoding utf-8
#
# 词义分析,情感分析
# by wooght 2017-11
# 扩展包 SnowNLP
#
from snownlp import SnowNLP

import sys,io
from snownlp import sentiment
from snownlp import seg
sentiment_path = 'D:\Python34\Lib\site-packages\snownlp\sentiment'
seg_path = 'D:\Python34\Lib\site-packages\snownlp/seg'
#sentiment.train(sentiment_path+'/neg.txt', sentiment_path+'\pos.txt')
# seg.train(seg_path+'/data.txt')
# seg.save(seg_path+'/seg.marshal')
# 保存训练好的文本库
#sentiment.save(sentiment_path+'\sentiment.marshal')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

text = '保险行业也不错哦，现在发展势头比较好'
s = SnowNLP(text)
print(s.words)
print(list(s.tags))
print(s.sentiments)         #情感打分 满分1分
