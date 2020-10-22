"""
@author:li kunlun
@time:2020-10-17
@description: 绘制直线和折线
"""
import matplotlib.pyplot as plt

# 准备绘制的两个点(1,2) (4,8)
# 调用绘制plot方法
plt.plot([1, 4], [4, 8])
# 显示绘制的图
plt.show()

print("------------绘制y=x^2的线段----------------")
# 准备绘制的点
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]
# 调用绘制方法
plt.plot(x, y)
# 显示图
plt.show()
