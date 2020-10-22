"""
@author:li kunlun
@time:2020-10-22
@description: 读取csv,txt,tsv文件
"""
import pandas as pd

students1 = pd.read_csv('D:/Students.csv', index_col='ID')
students2 = pd.read_csv('D:/Students.tsv', sep='\t', index_col='ID')
students3 = pd.read_csv('D:/Students.txt', sep='|', index_col='ID')

print(students1)
print(students2)
print(students3)
