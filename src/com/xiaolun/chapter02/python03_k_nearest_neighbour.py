"""
@author:li kunlun
@time:2020-10-16
@description:  k近邻算法
"""
import numpy as np
import pandas as pd

# 这里直接引入sklearn里的数据集，iris鸢尾花
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split  # 切分数据集为训练集和测试集
from sklearn.metrics import accuracy_score  # 评估过方法：计算分类预测的准确率

# 1. 数据加载和预处理
iris = load_iris()

df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['class'] = iris.target  # 添加新的一类
# 将class类的数据进行预处理
df['class'] = df['class'].map({0: iris.target_names[0], 1: iris.target_names[1], 2: iris.target_names[2]})

# 展示不同列的一些属性
print("df.describe()----", df.describe())

x = iris.data
y = iris.target.reshape(-1, 1)
# (150, 4) (150, 1)
print(x.shape, y.shape)

# 调库，划分训练集和测试集，test_size 测试集占的比例；random_state 随机生成数的种子；stratify按照y等比例分割
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=35, stratify=y)

# 输出：(105, 4) (105, 1)
print(x_train.shape, y_train.shape)
# 输出：(45, 4) (45, 1)
print(x_test.shape, y_test.shape)

a = np.array([[3, 2, 4, 2],
              [2, 1, 4, 23],
              [12, 3, 2, 3],
              [2, 3, 15, 23],
              [1, 3, 2, 3],
              [13, 3, 2, 2],
              [213, 16, 3, 63],
              [23, 62, 23, 23],
              [23, 16, 23, 43]])
b = np.array([[1, 1, 1, 1]])
print(a - b)
np.sum(np.abs(a - b), axis=1)
dist = np.sqrt(np.sum((a - b) ** 2, axis=1))
print(dist)


# 2. 核心算法实现
# 距离函数定义
# 曼哈顿距离。axis=1 表示求和按照行相加，保存成对应的列
# a是一个矩阵，b是一个向量
def l1_distance(a, b):
    return np.sum(np.abs(a - b), axis=1)


def l2_distance(a, b):  # 欧式距离
    return np.sqrt(np.sum((a - b) ** 2, axis=1))


# 分类器实现
class kNN(object):
    # 定义一个初始化方法，__init__ 是类的构造方法
    def __init__(self, n_neighbors=1, dist_func=l1_distance):
        self.n_neighbors = n_neighbors
        self.dist_func = dist_func

    # 训练模型方法，将x,y数据传进来
    def fit(self, x, y):
        self.x_train = x
        self.y_train = y

    # 模型预测方法，只需要传入x,不需要传入y
    def predict(self, x):
        # 初始化预测分类数组
        y_pred = np.zeros((x.shape[0], 1), dtype=self.y_train.dtype)  # 指定数据类型

        # 遍历输入的x数据点，取出每一个数据点的序号i和数据x_test
        # enumerate取出的是一个元组
        for i, x_test in enumerate(x):
            # x_test跟所有训练数据计算距离
            distances = self.dist_func(self.x_train, x_test)

            # 得到的距离按照由近到远排序，取出索引值
            nn_index = np.argsort(distances)

            # 选取最近的k个点（取出来，切片），需要先保存它们对应的分类类别
            nn_y = self.y_train[nn_index[:self.n_neighbors]].ravel()

            # 统计类别中出现频率最高的那个，赋给y_pred[i]
            y_pred[i] = np.argmax(np.bincount(nn_y))

        return y_pred


nn_index = np.argsort(dist)
print("dist: ", dist)
print("nn_index: ", nn_index)
nn_y = y_train[nn_index[:9]].ravel()
print("nn_y: ", nn_y)
print(np.bincount(nn_y))
print(np.argmax(np.bincount(nn_y)))

# 3. 测试
# 定义一个knn实例
knn = kNN(n_neighbors=3)
# 训练模型
knn.fit(x_train, y_train)
# 传入测试数据，做预测
y_pred = knn.predict(x_test)

print(y_test.ravel())
print(y_pred.ravel())

# 求出预测准确率 y_test：真实值；y_pred：测试值
accuracy = accuracy_score(y_test, y_pred)
print("预测准确率: ", accuracy)

# 定义一个knn实例
knn = kNN()
# 训练模型
knn.fit(x_train, y_train)

# 保存结果list
result_list = []

# 针对不同的参数选取，做预测
for p in [1, 2]:
    knn.dist_func = l1_distance if p == 1 else l2_distance

    # 考虑不同的k取值，步长为2
    for k in range(1, 10, 2):
        knn.n_neighbors = k
        # 传入测试数据，做预测
        y_pred = knn.predict(x_test)
        # 求出预测准确率
        accuracy = accuracy_score(y_test, y_pred)
        result_list.append([k, 'l1_distance' if p == 1 else 'l2_distance', accuracy])
df = pd.DataFrame(result_list, columns=['k', '距离函数', '预测准确率'])
print(df)