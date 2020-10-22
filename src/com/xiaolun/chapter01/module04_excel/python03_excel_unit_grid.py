"""
@author:li kunlun
@time:2020-10-17
@description: 单元格
"""
import pandas as pd

l1 = [100, 200, 300]
l2 = ['x', 'y', 'z']

s1 = pd.Series(l1, index=l2)
# 输出：Index(['x', 'y', 'z'], dtype='object')
print(s1.index)
# 输出：[100 200 300]
print(s1.values)

print("---------------------------------------")

s1 = pd.Series((1, 2, 3), index=(1, 2, 3), name='A')
s2 = pd.Series((10, 20, 30), index=(1, 2, 3), name='B')
s3 = pd.Series((100, 200, 300), index=(1, 2, 3), name='c')
df = pd.DataFrame({s1.name: s1, s2.name: s2, s3.name: s3})

"""
1、index索引是为了对齐,
如果定义的index在原字典中已经存在，那么该索引会一直对应
原字典的值，如果index对应不到原字典的值，则会返回NaN。
2、name是表头
输出：
   A   B    c
1  1  10  100
2  2  20  200
3  3  30  300
"""
print(df)
