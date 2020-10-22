"""
@author:li kunlun
@time:2020-10-17
@description: 绘制等高图
"""
import matplotlib.pyplot as plt
import numpy as np

# 创建x y（-10,10）之间有100个等差点
x = np.linspace(-10, 10, 100)
print("x", x)
y = np.linspace(-10, 10, 100)
print("y", y)

# 计算x y相交的点 X Y
X, Y = np.meshgrid(x, y)
# 计算Z
Z = np.sqrt(X ** 2 + Y ** 2)
print(type(Z))
print("Z", Z)
# 绘制等高线图，Z表示网格数据对应网格的高度值
# contour() 是绘制轮廓线，contourf()会填充轮廓
# plt.contour(X, Y, Z)
plt.contourf(X, Y, Z)
plt.show()
