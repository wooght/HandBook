# -- coding: utf-8 -
"""
@project    :HandBook
@file       :linear_re.py
@Author     :wooght
@Date       :2024/4/12 20:06
@Content    :原生实现一元线性回归
"""
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

"""
    y = mx + c
    m = (∑(x-x平)(y-y平))/(∑(x-x平)**2)
    c = ∑(Y平-m*X平)
"""

raw_data = pd.DataFrame({
    'smoke': np.linspace(5000, 7000, 20).astype(int),
    'turnover': np.linspace(12000,15000, 20). astype(int)
})
raw_data['smoke'] = raw_data['smoke'].apply(lambda x:x+np.random.uniform(-100,100))
raw_data['turnover'] = raw_data['turnover'].apply(lambda x:x+np.random.uniform(-300,900))
print(raw_data)
fig, ax = plt.subplots()
ax.scatter(x=raw_data['smoke'], y=raw_data['turnover'])

raw_data['smoke_ad'] = raw_data['smoke'].apply(lambda x:x-raw_data['smoke'].mean())
raw_data['turnover_ad'] = raw_data['turnover'].apply(lambda x:x-raw_data['turnover'].mean())
fenzi = (raw_data['smoke_ad'] * raw_data['turnover_ad']).sum()
fenmu = (raw_data['smoke_ad']**2).sum()
m = fenzi/fenmu
c = raw_data['turnover'].mean() - m * raw_data['smoke'].mean()
demo_smoke = np.linspace(4000,7000, 20).astype(int)
demo_data = pd.DataFrame({
    'smoke': demo_smoke,
    'turnover': (demo_smoke * m + c)
})
print(demo_data)
ax.plot(demo_data['smoke'], demo_data['turnover'])
ax.set_title('线性回归')
plt.show()