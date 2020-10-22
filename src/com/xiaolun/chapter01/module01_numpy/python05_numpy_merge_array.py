"""
@author:li kunlun
@time:2020-10-16
@description: numpy合并array
"""
import numpy as np

t1 = np.array([1, 1, 1])
print(type(t1))  # <class 'numpy.ndarray'>
print(t1.shape)  # 输出：(3,)!!!!!!!。说明t1是一个序列，不是矩阵

# 方法1：转换成矩阵操作
t1_2_mat = np.mat(t1)
print(type(t1_2_mat))  # <class 'numpy.matrix'>
print("t1_2_mat.shape:", t1_2_mat.shape)  # (1, 3)

# 方法2：再添加一个[],变换一个格式
m1 = np.array([[1, 2, 3]])
print(m1)
print(m1.shape)  # (1, 3)

t2 = np.array([2, 2, 2])
t3 = np.vstack((t1, t2))  # 上下合并
t4 = np.hstack((t1, t2))  # 左右合并
# 输出：
# [[1 1 1]
#  [2 2 2]]
print("t3：", t3)

print("--------------------------------")
n1 = t1[:, np.newaxis]  # 插入新维度,将一维的数据转变成一个矩阵
# 输出：
# [[1]
#  [1]
#  [1]]
print(n1)
print(n1.shape)  # (3, 1)
print(type(n1))  # <class 'numpy.ndarray'>

n2 = t1[np.newaxis, :]  # 插入新维度
print(n2)  # [[1 1 1]]
print(n2.shape)  # (1, 3)
