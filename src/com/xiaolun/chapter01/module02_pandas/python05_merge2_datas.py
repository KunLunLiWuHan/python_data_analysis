"""
@author:li kunlun
@time:2020-10-20
@description:合并数据merge
"""
import pandas as pd
import numpy as np

left = pd.DataFrame({'key': ['k0', 'k1'], 'A': ['A0', 'A1']})
right = pd.DataFrame({'key': ['k0', 'k1'], 'B': ['B0', 'B1']})
# 按照key进行合并
# how=['left','right','outer','inner']
# indicator提示merge以怎么样的形式进行合并
res = pd.merge(left, right, on='key', how='right', indicator=True)
print(res)

