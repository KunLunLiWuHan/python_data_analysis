"""
@author:li kunlun
@time:2020-10-22
@description:旋转表格
"""
import pandas as pd

pd.options.display.max_columns = 999
# 需要添加上index_col='Month'，不然旋转后在原来的数据表上会多出一行
videos = pd.read_excel('D:/Videos.xlsx', index_col='Month')
# 下面两行代码等价
table = videos.transpose()
# table = videos.T
print(table)
