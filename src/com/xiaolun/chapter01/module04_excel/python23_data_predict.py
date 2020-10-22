"""
@author:li kunlun
@time:2020-10-22
@description:线性回归，数据预测
"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

sales = pd.read_excel('D:/Sales.xlsx', dtype={'Month': str, 'Revenue': float})

# 使用内置函数
slope, intercept, r_value, p_value, std_err = linregress(sales.index, sales.Revenue)
exp = sales.index * slope + intercept

plt.scatter(sales.index, sales.Revenue)
plt.plot(sales.index, exp, color='red')
plt.xticks(sales.index, sales.Month, rotation=90)
plt.show()
