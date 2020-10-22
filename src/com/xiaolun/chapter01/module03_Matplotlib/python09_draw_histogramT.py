"""
@author:li kunlun
@time:2020-10-17
@description: 绘制直方图
"""
import matplotlib.pyplot as plt
import numpy as np

# 生成10个标志的正态分布随机数
x = np.random.randn(10)
# plt.hist(x)
# 修改柱的宽度  使用bins
# bins参数指定bin(箱子)的个数,也就是总共有几条条状图，下面有100个bins
plt.hist(x, bins=2)  # (10/2)正态分布中的每个5个柱（数）装在一起
plt.show()

print("-------------------------")
# 使用np.random.normal()指定期望和均值的正太分布
# loc（均值），scale（标准差）， size
x = np.random.normal(0, 0.8, 1000)
y = np.random.normal(-2, 1, 1000)
z = np.random.normal(3, 2, 1000)
# 创建字典类型的数据，并将数据传到直方图plt.hist中
kwargs = dict(bins=100, alpha=0.5)  # alpha是透明度
plt.hist(x, **kwargs)
plt.hist(y, **kwargs)
plt.hist(z, **kwargs)
plt.show()
