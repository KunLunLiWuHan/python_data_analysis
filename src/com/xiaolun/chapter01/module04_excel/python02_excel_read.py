"""
@author:li kunlun
@time:2020-10-17
@description: 文件的读取
"""
import pandas as pd

"""
1、当表格不含表头时，使用header=None不显示头信息
2、可以使用下面的语句为表格添加头信息
"""
# people = pd.read_excel("D:\\People.xlsx", header=None)
# people.columns = ('ID', 'Type', 'Title', 'FirstName', 'MiddleName', 'LastName')

people = pd.read_excel("D:\\People.xlsx")
# 列表的（行，列）的尺寸，输出：(19972, 6)
print(people.shape)
# 列表的列信息，输出
# Index(['ID', 'Type', 'Title', 'FirstName', 'MiddleName', 'LastName'], dtype='object')
print(people.columns)
"""
由于excel表格太长，我们展示只显示头信息（默认只看前5行）：
   ID      Type Title FirstName MiddleName    LastName
0   1  Employee   NaN       Ken          J     Sánchez
1   2  Employee   NaN     Terri        Lee       Duffy
2   3  Employee   NaN   Roberto        NaN  Tamburello
3   4  Employee   NaN       Rob        NaN     Walters
4   5  Employee   Ms.      Gail          A    Erickson
"""
# print(people.head())
# 查看前3行
print(people.head(3))
# 查看后3行
# print(people.tail(3))
