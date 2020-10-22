"""
@author:li kunlun
@time:2020-10-22
@description:创建透视表
"""
import pandas as pd
import numpy as np
from datetime import date

orders = pd.read_excel('D:/Orders.xlsx', dtype={'Date': date})
orders['Year'] = pd.DatetimeIndex(orders.Date).year
pt = orders.pivot_table(index='Category', columns='Year', values='Total', aggfunc=np.sum)
print(pt)
