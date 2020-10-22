"""
@author:li kunlun
@time:2020-10-16
@description: numpy的基础运算
"""
import numpy as np

test1 = np.array([2, 3, 4])
test2 = np.arange(3)
# 输出：[0 1 2]
print(test2)
sub = test1 - test2
# 输出：[2 2 2]
print(sub)

test3 = np.sin(test1)
print(test3)

test4 = np.array([[1, 1],
                  [0, 1]])
test5 = np.array([[0, 1],
                  [2, 3]])

# 对应项相乘
# [[0 1]
#  [0 3]]
test6 = test4 * test5

# 举证真正的乘法
# [[2 4]
#  [2 3]]
test_doc = np.dot(test4, test5)
print(test6)
print(test_doc)

# 创建一个2*3矩阵的随机数
# [[0.40444673 0.60621217 0.7454439 ]
#  [0.06838504 0.19788044 0.97726666]]
t1 = np.random.random((2, 3))
print(t1)

# 在每一列中求最大值
print("----------------")
print(np.max(t1, axis=0))
# 在每一行中求最大值
print("----------------")
print(np.max(t1, axis=1))

print("-------------------第二阶段-------------------")
m1 = np.arange(1, 5).reshape((2, 2))
# 返回当前矩阵最大值的索引
print(np.argmax(m1))

# 输出：
# [[1 2]
#  [2 2]]
# 切割，[1，2]之间的数为原始值，大于2的数为2，小于1的值为1
print(np.clip(m1, 1, 2))
