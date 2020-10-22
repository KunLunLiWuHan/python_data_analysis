"""
@author:li kunlun
@time:2020-10-16
@description:测试
"""
import pandas as pd
import numpy as np

# [3 3 3 3]
print(np.array([3] * 4))
# 输出
# 0    1
# 1    1
# 2    1
# 3    1
print(pd.Series(1, index=list(range(4))))
