"""
@author:li kunlun
@time:2020-10-17
@description: 绘制散点图
"""
import matplotlib.pyplot as plt
import numpy as np

# 画10种大小， 10种颜色的散点图
np.random.seed(0)  # 执行多次每次获取的随机数都是一样的
x = np.random.rand(10)
print("x", x)
y = np.random.rand(10)
print("y", y)
# 10种的颜色
colors = np.random.rand(10)
# 生成10种大小,*100作用是将点的大小放大放大。其个数和x或者y的个数相同
size = np.random.rand(10) * 100
# colors表示点的颜色, size表示点的大小,alpha表示透明度(用于重叠问题)
plt.scatter(x, y, c=colors, s=size, alpha=0.7)
plt.show()
'''
注意：点的个数和颜色的个数要相同
      点的个数和点大小的个数可以不同，如果点的个数大于大小的个数，则会循环获取大小
'''
