"""
@author:li kunlun
@time:2020-10-17
@description: zip()是Python的一个内建函数，它接受一系列可迭代的对象作为参数，
将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）
"""
seq = ['one', 'two', 'three']
seq1 = [1, 2, 3]

# [('one', 1), ('two', 2), ('three', 3)]
print(list(zip(seq, seq1)))
print(type(zip(seq, seq1)))
for m1, n1 in zip(seq, seq1):
    print("m1:{0},n1:{1}".format(m1, n1))
