"""
@author:li kunlun
@time:2020-10-16
@description: numpy的属性
"""
import numpy as np

# 一维矩阵 2 * 3
matrix_test = [[1, 2, 3],
               [4, 5, 6]]
# 将矩阵转化为数组
array = np.array(matrix_test)
# 二维数组
# [[1 2 3]
#  [4 5 6]]
print(array)
# 数组的长度：输出 2
print(len(array))
# 数组的维度：2
print("number of dim:", array.ndim)
# 数组的形状,输出：shape: (2, 3)
print("shape:", array.shape)
# 输出：size: 6
print("size:", array.size)
