"""
@author:li kunlun
@time:2020-10-16
@description: numpy的拷贝操作
"""
import numpy as np

t1 = np.arange(4)
t2 = t1  # 浅拷贝，t1改变会影响t2
t1[0] = 10
# [10  1  2  3]
print(t2)
t3 = t1.copy()  # 深拷贝
t1[1] = 20
# [10  1  2  3]
print(t3)
