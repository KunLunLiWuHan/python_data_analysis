"""
@author:li kunlun
@time:2020-10-16
@description: numpy创建Array
"""
import numpy as np

# 创建一个一维Array数组，使用list表的形式，并指令类型
test = np.array([1, 2, 3], dtype=np.int)
# 输出：[1 2 3]
print(test)
# 输出：int32
print(test.dtype)

# 定义一个二维的矩阵
test2 = np.array([[1, 2, 3],
                  [4, 5, 6]])
print(test2)

# 定义一个2*3的零矩阵
# [[0. 0. 0.]
#  [0. 0. 0.]]
test3 = np.zeros((2, 3))
print(test3)

# 定义全1矩阵
# [[1 1 1]
#  [1 1 1]]
test4 = np.ones((2, 3), dtype=np.int16)
print(test4)

# 空矩阵
# [[0. 0. 0.]
#  [0. 0. 0.]]
test5 = np.empty((2, 3))
print(test5)

# 生成一个3*4的矩阵
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
test6 = np.arange(12).reshape((3, 4))
print(test6)

print("--------------矩阵操作-----------------")
n1 = np.mat([1, 2, 3])
print(n1)  # 输出：[[1 2 3]]
print(type(n1))  # <class 'numpy.matrix'>
