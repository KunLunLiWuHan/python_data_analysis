"""
@author:li kunlun
@time:2020-10-21
@description:分组柱状图及优化
"""
import pandas as pd
import matplotlib.pyplot as plt

students = pd.read_excel('D:/Students.xlsx')
students.sort_values(by='2017', inplace=True, ascending=False)
print(students)
# 绘制一个分组的的柱图
students.plot.bar('Field', ['2016', '2017'], color=['orange', 'Red'])
plt.title('International Students by Field', fontsize=16)
plt.xlabel('Field', fontweight='bold')
plt.ylabel('Number', fontweight='bold')
plt.tight_layout()
ax = plt.gca()
# ha='right'表示Field中（x轴）的标签按照右顶点进行旋转。默认按照字体的中间进行旋转
ax.set_xticklabels(students['Field'], rotation=40, ha='right')
# 将子图左和底部各留出20%的空余
plt.gcf().subplots_adjust(left=0.2, bottom=0.42)
plt.show()
