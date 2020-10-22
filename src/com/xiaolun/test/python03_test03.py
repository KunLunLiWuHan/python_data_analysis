"""
@author:li kunlun
@time:2020-10-17
@description:
"""
import numpy as np

pointx = np.array([1, 2, 3])
pointy = np.array([4, 5])
mesh = np.meshgrid(pointx, pointy)
print(mesh)
