"""
@author:li kunlun
@time:2020-10-22
@description:条件格式
"""
import pandas as pd

# == == == == == ==将不及格的数据标红== == == == == ==
def low_score_red(s):
    color = 'red' if s < 60 else 'green'
    return f'color:{color}'


students = pd.read_excel('D:/Students.xlsx')
# apply 用在dataframe上，用于对row或者column进行计算；
# applymap 用于dataframe上，是元素级别的操作
students.style.applymap(low_score_red, subset=['Test_1', 'Test_2', 'Test_3'])

# == == == == == ==找出一列中的最大值 == == == == == ==

import pandas as pd


def highest_score_green2(col):
    return ['background-color:lime' if v == col.max() else 'background-color:red' for v in col]


students = pd.read_excel('D:/Students.xlsx')
students.style.apply(highest_score_green2, subset=['Test_1', 'Test_2', 'Test_3'])

# == == == == =颜色深浅= == == == == == == ==

import pandas as pd
import seaborn as sns

color_map = sns.light_palette('green', as_cmap=True)

students = pd.read_excel('D:/Students.xlsx')
students.style.background_gradient(cmap=color_map, subset=['Test_1', 'Test_2', 'Test_3'])

# == == == == ==数据条 == == == == == == ==

import pandas as pd

students = pd.read_excel('D:/Students.xlsx')
students.style.bar(color='orange', subset=['Test_1', 'Test_2', 'Test_3'])
