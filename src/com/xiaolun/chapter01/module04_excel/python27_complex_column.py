"""
@author:li kunlun
@time:2020-10-22
@description:复杂计算列-计算公式比较复杂
"""
import pandas as pd
import numpy as np


# 结构化的方式来计算
def get_circumcircle_area(l, h):
    r = np.sqrt(l ** 2 + h ** 2) / 2
    return r ** 2 * np.pi


def wrapper(row):
    return get_circumcircle_area(row['Length'], row['Height'])


rects = pd.read_excel('D:/Rectangles.xlsx', index_col='ID')
rects['Circumcircle Area'] = rects.apply(wrapper, axis=1)
print(rects)
