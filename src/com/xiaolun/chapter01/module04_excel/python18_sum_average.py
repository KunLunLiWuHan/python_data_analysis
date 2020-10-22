"""
@author:li kunlun
@time:2020-10-22
@description:求数据的和和平均数
"""
import pandas as pd

students = pd.read_excel('D:/Students.xlsx', index_col='ID')

# 跨行操作，进行一行的的求和和统计平均操作
row_sum = students[['Test_1', 'Test_2', 'Test_3']].sum(axis=1)
row_mean = students[['Test_1', 'Test_2', 'Test_3']].mean(axis=1)

students['Total'] = row_sum
students['Average'] = row_mean

col_mean = students[['Test_1', 'Test_2', 'Test_3', 'Total', 'Average']].mean()
# 在Name中追加一列Summary
col_mean['Name'] = 'Summary'
students = students.append(col_mean, ignore_index=True)
print(students)
