import matplotlib as mpl
import matplotlib.pyplot as plt     #matplotlib.pyplot 绘图主键
import seaborn as sns
import numpy as np
import pandas as pd

import time

mpl.rcParams['font.sans-serif'] = ['SimHei']    #指定默认字体 解决中文问题

sns.set(style="ticks")
exercise = sns.load_dataset("http://api.money.126.net/data/feed/0601398")
# g = sns.factorplot(x="time", y="pulse", hue="kind",
#                     data=exercise, kind="violin")
print(exercise)
plt.show()
