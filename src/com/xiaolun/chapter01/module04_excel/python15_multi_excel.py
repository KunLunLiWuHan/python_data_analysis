"""
@author:li kunlun
@time:2020-10-22
@description:多表联合
"""
import pandas as pd

students = pd.read_excel('D:/Student_score.xlsx', sheet_name='Students', index_col='ID')
scores = pd.read_excel('D:/Student_score.xlsx', sheet_name='Scores', index_col='ID')
# 将右表Scores以左表的Students的ID为基准进行连接。Scores中没有的数据补零后显示。
table = students.join(scores, how='left').fillna(0)
# 将Score中的数据变成整数
table.Score = table.Score.astype(int)
print(table)
