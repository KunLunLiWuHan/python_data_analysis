"""
@author:li kunlun
@time:2020-10-17
@description: 文件的创建
"""
import pandas as pd

# 创建一个两列的数据框，
df = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Tom', 'Jack', 'Nick']})
# 为excel表格添加上指定索引,如果不设置，索引默认为1，2，3
df = df.set_index('ID')
df.to_excel('D:/output.xlsx')
print("Done!")
