"""
@author:li kunlun
@time:2020-10-16
@description: pandas中选择数据
"""
import pandas as pd
import numpy as np

dates = pd.date_range("20201016", periods=3)
df = pd.DataFrame(np.arange(12).reshape(3, 4), index=dates, columns=['a', 'b', 'c','d'])
# 输出
#             a  b   c   d
# 2020-10-16  0  1   2   3
# 2020-10-17  4  5   6   7
# 2020-10-18  8  9  10  11
print(df)
# 选取第一行的数据
print(df[0:1])