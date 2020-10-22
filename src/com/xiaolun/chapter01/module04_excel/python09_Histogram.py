"""
@author:li kunlun
@time:2020-10-21
@description:绘制柱状图
"""
import pandas as pd
import matplotlib.pyplot as plt

student = pd.read_excel("D:/Students.xlsx")
student.sort_values(by='Number', inplace=True, ascending=False)
# 使用pandas来画图（该库只能做一些中规中矩的图）
# student.plot.bar(x="Field", y="Number", color="orange", title="International Student by Filed")
plt.bar(student.Field, student.Number, color="orange")
# 对横坐标数据旋转90度
plt.xticks(student.Field, rotation='90')
# 调整图参数，使之填充整个图像区域（紧凑型布局）
plt.tight_layout()
plt.show()
