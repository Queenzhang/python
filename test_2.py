# -*- coding: utf-8 -*-
# 判断一个对象是够可迭代
from collections import Iterable
isinstance('abc', Iterable)
isinstance([1,2,3], Iterable)
isinstance(123, Iterable)


#enumerate把list变成 索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]: 
    print(x, y)


def findMinAndMax(L):
    if len(L)==0:
        return(None,None)
    else:
        (min,max)=(L[0],L[0])
        for x in L:
            if max<x:
                max=x
            if min>x:
                min=x
        return(min,max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')