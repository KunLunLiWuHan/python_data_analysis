"""
@author:li kunlun
@time:2020-10-16
@description: numpy的索引
"""
import numpy as np

t1 = np.arange(3, 12)
# [3 4 5 6 7 8 9]
print(t1)
# 输出：5
print(t1[2])

t2 = np.arange(3, 12).reshape((3, 3))
print("t2 type ", type(t2))  # <class 'numpy.ndarray'>
print(t2)
# 输出第3行：[ 9 10 11]
print(t2[2])
# 索引第2行第2列，下面输出等价
print(t2[1][1])
print(t2[1, 1])

# 输出第2行的所有元素：[6 7 8]
print(t2[1, :])

# 变成一行，输出：[ 3  4  5  6  7  8  9 10 11]
print(t2.flatten())
