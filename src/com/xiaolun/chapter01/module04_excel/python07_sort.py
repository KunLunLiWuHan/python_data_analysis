"""
@author:li kunlun
@time:2020-10-20
@description:排序，多重排序
"""
import pandas as pd

products = pd.read_excel('D:/List.xlsx', index_col='ID')
# Worthy进行升序排列，Price进行降序排列
products.sort_values(by=['Worthy', 'Price'], ascending=[True, False], inplace=True)
print(products)
