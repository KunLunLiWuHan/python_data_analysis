"""
@author:li kunlun
@time:2020-10-21
@description:叠加柱状图
"""
import pandas as pd
import matplotlib.pyplot as plt

users = pd.read_excel('D:/Users.xlsx')
# 为Users表设置一个属性，用来降序排列
users['Total'] = users['Oct'] + users['Nov'] + users['Dec']
users.sort_values(by='Total', inplace=True, ascending=False)
print(users)

#  正常方向上（垂直方向上）。stacked=True 用来叠加数据
# users.plot.bar(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True)
# 水平方向上图形显示
users.plot.barh(x='Name', y=['Oct', 'Nov', 'Dec'], stacked=True)
plt.tight_layout()
plt.show()
