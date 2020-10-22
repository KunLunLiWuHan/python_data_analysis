"""
@author:li kunlun
@time:2020-10-17
@description: 数据区域自动填充
"""
import datetime
import pandas as pd

"""
1、月份自动填充
    d：传进来的其实时间
    md：增加的步长
"""


def add_month(d, md):
    yd = md // 12  # 传进来的月份包含多少年
    m = d.month + md % 12  # 剩余下的月份=当前月份 + 取余月份
    """
    如果传进来的月份是11月，增减月份为3，那么上式m=14，我们还需要对其进一步处理。
    """
    if m != 12:
        yd += m // 12
        m = m % 12
    return datetime.date(d.year + yd, m, d.day)


"""
1、dtype={'ID': str}：将ID这一行的数据变成str类型的
"""
books = pd.read_excel("D:\\Books.xlsx", skiprows=3, usecols="C:F", index_col=None,
                      dtype={'ID': str, 'InStore': "str", 'Date': "str"})
# print(books.head())
# 输出：RangeIndex(start=0, stop=20, step=1)
print(books.index)
start = datetime.date(2018, 1, 1)
# 填充ID,InStore列
for i in books.index:
    books['ID'].at[i] = i + 1
    books['InStore'].at[i] = 'YES' if i % 2 == 0 else 'NO'
    # 天，月，年增加
    books['Date'].at[i] = start + datetime.timedelta(days=i)
    # books['Date'].at[i] = add_month(start, i)
    # books['Date'].at[i] = datetime.date(start.year + i, start.month, start.day)

print(books)
