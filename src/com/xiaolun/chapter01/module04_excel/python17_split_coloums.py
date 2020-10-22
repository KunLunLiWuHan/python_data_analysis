"""
@author:li kunlun
@time:2020-10-22
@description:将一列数据划分为两列
"""
import pandas as pd

employees = pd.read_excel('D:/Employees.xlsx', index_col='ID')
df = employees['Full Name'].str.split(expand=True)
employees['First Name'] = df[0]
employees['Last Name'] = df[1]
print(employees)
