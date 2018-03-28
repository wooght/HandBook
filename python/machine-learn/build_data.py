# -*- coding: utf-8 -*-
#
# @method   : 构造数据
# @Time     : 2018/3/27
# @Author   : wooght
# @File     : build_data.py

import sys

sys.path.append('/home/vagrant/www/scripy_wooght/caijing_scrapy')

from factory.data_analyse import *
import pandas as pd

ddpct = dd_pct()
ddpct.select_companyies()
ddmath = dd_math()
zhmath = zuhe_math()
zh_focus = zhmath.group_mean()
alldd = ddmath.select_alldd()
ddpct.dd_repository = alldd
codeids = ddpct.have_dd(days=100, nums=20)
dd_df_dict = {}
for id in codeids:
    if id not in zh_focus:
        continue
    dd_df_dict[id] = alldd[alldd.code_id == id].copy()

last_df = ddmath.quotes_install(dd_df_dict)
default_df = last_df[601318].pd
default_df['codeid'] = 601318
for i in last_df:
    print(last_df[i].pd)
    if i != 601318:
        last_df[i].pd['codeid'] = i
        default_df = pd.concat([default_df, last_df[i].pd], axis=0)  # axis 横向拼接
default_df.to_csv('data.csv')