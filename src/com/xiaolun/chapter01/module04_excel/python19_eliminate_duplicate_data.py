"""
@author:li kunlun
@time:2020-10-22
@description:消除重复数据
"""
import pandas as pd

students = pd.read_excel('D:/Students_Duplicates.xlsx')
# keep='first'（last）保持前面的数据
students.drop_duplicates(subset='Name', inplace=True, keep='first')
# subset:限定函数作用范围
# dupe = students.duplicated(subset='Name')
# 表示将dataFrame中的数据扫描一遍，看看那些行是重复的。重复为True。
# dupe = dupe[dupe == True]  # dupe = dupe[dupe]
# 将重复数据的索引打印出来
# print(students.iloc[dupe.index])
print(students)
