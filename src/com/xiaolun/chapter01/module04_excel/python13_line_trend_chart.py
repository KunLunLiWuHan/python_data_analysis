"""
@author:li kunlun
@time:2020-10-22
@description:折线趋势图
"""
import pandas as pd
import matplotlib.pyplot as plt

weeks = pd.read_excel('D:/Orders.xlsx', index_col='Week')

weeks.plot(y=['Accessories', 'Bikes', 'Clothing', 'Components'])
# weeks.plot.area(y=['Accessories', 'Bikes', 'Clothing', 'Components'])
plt.title('Sales Trends', fontsize=16, fontweight='bold')
plt.xticks(weeks.index, fontsize=8)
plt.show()
