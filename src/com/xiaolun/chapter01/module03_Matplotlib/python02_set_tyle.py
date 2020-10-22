"""
@author:li kunlun
@time:2020-10-17
@description: 设置样式，绘制一元二次曲线，正弦曲线
"""
import matplotlib.pyplot as plt
import numpy as np

# 解决图像中负号不显示的问题
plt.rcParams['axes.unicode_minus'] = False

# 准备x y
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# 绘制折线
# linewidth属性设置线条的宽度
plt.plot(x, y, linewidth=5)
# 添加x y轴名称
plt.xlabel('x')
plt.ylabel('y=x^2')
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# 给图标添加标题
plt.title('多个点绘制折线图')
plt.show()

print("----------------绘制一元二次方程曲线-----------------")
# 准备x  y
x = range(-100, 100)  # 200个点
y = [i ** 2 for i in x]
# 绘制一元二次方程曲线
plt.plot(x, y)
# 保存图片
plt.savefig('result')  # 默认的格式png
# plt.savefig('result.jpg')
plt.show()

print("----------------绘制正弦曲线-----------------")
# 生成0-10之间 100个等差数
x = np.linspace(0, 10, 100)
sin_y = np.sin(x)
# 进行绘制正弦曲线
plt.plot(x, sin_y)

cos_y = np.cos(x)
# 绘制余弦曲线
plt.plot(x, cos_y)
# 保存成图片，图片中蓝色为第一个曲线，黄色为第二个
plt.savefig('sin_cos.jpg')
plt.show()
