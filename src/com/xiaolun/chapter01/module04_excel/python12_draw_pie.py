"""
@author:li kunlun
@time:2020-10-21
@description:绘制饼状图
"""
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('D:/Students.xlsx', index_col='From')
print(students)

# counterclock（逆时针）=False
#  startangle=-270表示从-270为起始点
students['2017'].plot.pie(fontsize=6, counterclock=False)
plt.title('Source of International Students', fontsize=16, fontweight='bold')
plt.ylabel('2017', fontsize=12, fontweight='bold')
plt.show()
