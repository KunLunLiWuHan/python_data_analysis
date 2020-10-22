"""
@author:li kunlun
@time:2020-10-20
@description:处理丢失数据
"""
import pandas as pd
import numpy as np

dates = pd.date_range("20130101", periods=3)
df = pd.DataFrame(np.arange(12).reshape(3, 4), index=dates, columns=['A', 'B', 'C', 'D'])
df.iloc[0, 0] = np.nan
df.iloc[0, 1] = np.nan
# print(df)
# 过滤数据中的缺失数据。
# how='any'表示如果在一行中有Nan的数据，就把这一行丢掉
# how='all'表示这一行全部等于Nan才会被过滤。
# print(df.dropna(axis=0, how='all'))
# 将nan数据替换为0
print(df.fillna(value=0))
