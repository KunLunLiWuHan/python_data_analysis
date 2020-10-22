"""
@author:li kunlun
@time:2020-10-22
@description:散点图，直方图
"""
import pandas as pd
import matplotlib.pyplot as plt

# 用于在控制台打印数据（将Excel的信息都显示出来）
pd.options.display.max_columns = 999
homes = pd.read_excel('D:/home_data.xlsx')
print(homes.head())
# 两列之间数据的相关性
print(homes.corr())
# 散点图
# homes.plot.scatter(x='sqft_living', y='price')
# 密度图（kernel density）
homes.sqft_living.plot.kde()
# 直方图
# homes.sqft_living.plot.hist(bins=100)
# # 500表示x轴的步长
# plt.xticks(range(0, max(homes.sqft_living), 500), fontsize=8, rotation=90)
plt.show()
