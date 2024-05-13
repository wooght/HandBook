# -- coding: utf-8 -
"""
@project    :HandBook
@file       :main.py
@Author     :wooght
@Date       :2024/5/11 19:26
@Content    :
"""

from hello import say

print('调用celery')
result = say.delay(1, 2)
print('任务ID{}'.format(result.id))
# result.forget()
print(result)