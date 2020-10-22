"""
@author:li kunlun
@time:2020-10-16
@description: numpy中array的分割
"""
import numpy as np

t1 = np.arange(12).reshape((3, 4))
# 对于列对等分割(分成2块).输出
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]),
# array([[ 2,  3],
#        [ 6,  7],
#        [10, 11]])]
print(np.split(t1, 2, axis=1))
# 不等分割，输出
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2],
#        [ 6],
#        [10]]), array([[ 3],
#        [ 7],
#        [11]])]
print(np.array_split(t1, 3, axis=1))

print("-----------简化的分割函数-----------")
m1 = np.vsplit(t1, 3)  # row方向
# [array([[0, 1, 2, 3]]), array([[4, 5, 6, 7]]), array([[ 8,  9, 10, 11]])]
print(m1)
print(type(m1))  # 输出：<class 'list'>
m2 = np.hsplit(t1, 2)  # col方向
print(m2)
# [array([[0, 1],
#        [4, 5],
#        [8, 9]]), array([[ 2,  3],
#        [ 6,  7],
#        [10, 11]])]
print(type(m2))  # 输出：<class 'list'>
