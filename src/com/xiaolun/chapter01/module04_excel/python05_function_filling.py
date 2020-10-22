"""
@author:li kunlun
@time:2020-10-17
@description: 函数填充，计算列
"""
import pandas as pd

books = pd.read_excel("D:\\Books_price.xlsx", index_col='ID')
# 指定数据范围计算
# for i in range(5, 16):

# for i in books.index:
#     books["Price"].at[i] = books["ListPrice"].at[i] * books["Discount"].at[i]
#
# print(books)

"""
1、使用这种方式将ListPrice列 + 2
2、比较简单，但是难以理解。
"""
# books["ListPrice"] += 2
# print(books)


# 我们也可以使用下面的方式来进行ListPrice + 2
def add_2(x):
    return x + 2


books["ListPrice"] = books["ListPrice"].apply(add_2)
print(books)