"""
@author:li kunlun
@time:2020-10-16
@description:线性回归调用sklearn库代码实现
"""
import numpy as np
import matplotlib.pyplot as plt

points = np.genfromtxt('data.csv', delimiter=',')

points[0, 0]

# 提取points中的两列数据，分别作为x，y
x = points[:, 0]
y = points[:, 1]

# 用plt画出散点图
plt.scatter(x, y)
plt.show()


# 损失函数是系数的函数，另外还要传入数据的x，y
def compute_cost(w, b, points):
    total_cost = 0
    M = len(points)

    # 逐点计算平方损失误差，然后求平均数
    for i in range(M):
        x = points[i, 0]
        y = points[i, 1]
        total_cost += (y - w * x - b) ** 2

    return total_cost / M


# 引入第三方的库，调用已经训练好的模型库
from sklearn.linear_model import LinearRegression

lr = LinearRegression()

"""
1、x.reshape(-1, 1)变成n行1列的矩阵
 -1表示
"""
x_new = x.reshape(-1, 1)
# 存放的是 [[32.50234527],[53.42680403]]
print("x_new-----", x_new)
y_new = y.reshape(-1, 1)
lr.fit(x_new, y_new)

# 从训练好的模型中提取系数和截距
w = lr.coef_[0][0]  # 存储线性模型的系数 w存储
b = lr.intercept_[0]  # intercept:截距

print("w is: ", w)
print("b is: ", b)

cost = compute_cost(w, b, points)
print("cost is: ", cost)

plt.scatter(x, y)
# 针对每一个x，计算出预测的y值
pred_y = w * x + b

plt.plot(x, pred_y, c='r')
plt.show()
