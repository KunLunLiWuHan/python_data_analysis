"""
@author:li kunlun
@time:2020-10-16
@description: pandas介绍
"""
import pandas as pd
import numpy as np

s1 = pd.Series([2, 4, 6])
# 输出：左边有序号，右边是数据
# 0    2
# 1    4
# 2    6
print("s1", s1)

dates = pd.date_range("20201016", periods=2)
# DatetimeIndex(['2020-10-16', '2020-10-17'], dtype='datetime64[ns]', freq='D')
print(dates)

# DataFrame相当于一个二维矩阵
df = pd.DataFrame(np.random.randn(2, 2), index=dates, columns=['a', 'b'])
# 输出：以dates作为左侧行的索引，以字母a,b作为列的索引
#                    a        b
# 2020-10-16  0.442655 -0.22998
# 2020-10-17 -1.157189 -0.27214
print(df)

df2 = pd.DataFrame(
    {"A": 1, "B": pd.Timestamp("20201016"), "c": "foo", "d": pd.Series([3] * 4, index=list(range(4, 8)))})
# 1、字典中d的index指定索引值，不然会报错
# 2、c中的foo和B自动填充
#    A          B    c  d
# 4  1 2020-10-16  foo  3
# 5  1 2020-10-16  foo  3
# 6  1 2020-10-16  foo  3
# 7  1 2020-10-16  foo  3
print(df2)
# Int64Index([4, 5, 6, 7], dtype='int64')
print(df2.index)
# Index(['A', 'B', 'c', 'd'], dtype='object'
print(df2.columns)
# 将矩阵中的值打印出来
print(df2.values)

# 对df2的描述，方差，平均值什么的。
#        A    d
# count  4.0  4.0
# mean   1.0  3.0
# std    0.0  0.0
# min    1.0  3.0
# 25%    1.0  3.0
# 50%    1.0  3.0
# 75%    1.0  3.0
# max    1.0  3.0
print(df2.describe())

print("--------------排序后输出-----------------")
sort1 = df2.sort_index(axis=0, ascending=False)
# 根据索引值对行进行降序输出
#    A          B    c  d
# 7  1 2020-10-16  foo  3
# 6  1 2020-10-16  foo  3
# 5  1 2020-10-16  foo  3
# 4  1 2020-10-16  foo  3

# 指定对A列中的数据进行排序
# sort1 = df2.sort_values(by="A", ascending=False)
print(sort1)
