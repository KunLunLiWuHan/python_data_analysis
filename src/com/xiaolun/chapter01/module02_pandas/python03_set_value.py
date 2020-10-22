"""
@author:li kunlun
@time:2020-10-20
@description: 设置值
"""
import pandas as pd
import numpy as np

dates = pd.date_range("20130101", periods=3)
df = pd.DataFrame(np.arange(12).reshape(3, 4), index=dates, columns=['A', 'B', 'C', 'D'])

# 对坐标（2，2）的数据进行赋值
# df.iloc[2, 2] = 1111  # 推荐使用这一个
# df.loc['20130101', 'B'] = 2222

# 将A列中大于0对应这一行的数据置为0
# df[df.A > 0] = 0

# 将A列中大于0的数据赋值为0
# df.A[df.A > 0] = 0

# 添加E列，并赋值为NaN
df["E"] = np.nan
# 添加F列，
df["F"] = pd.Series([1, 2, 3], index=pd.date_range("20130101", periods=3))
print(df)
