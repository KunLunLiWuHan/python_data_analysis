"""
@author:li kunlun
@time:2020-10-20
@description:合并数据concat
"""
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns=['a', 'b', 'c', 'd'])

# 对行进行合并，忽略索引。
# 默认join="inner"(outer表示外连接，将不相同的进行补全)
# res = pd.concat([df1, df2], axis=0, join="inner",ignore_index=True)

print("-----------------追加数据----------------")
s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
res2 = df1.append(s1, ignore_index=True)
print(res2)

