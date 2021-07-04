#迭代 for in 循环来遍历list或tuple，甚至其他可迭代对象如dict
from collections import Iterable #判断一个对象是都是可迭代对象

print(isinstance('abc', Iterable))


d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k,v)

#Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']): 
    print(i, value)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


def findMinAndMax(L):
    min = None
    max = None

    print(L)
    print()
    # 拦截空list
    if len(L) == 0:
        return (min, max)
    # 非空操作
    min = max = L[0]
    # print(min, max)
    for i in L:
        if i <= min:
            min = i
        elif i >= max:
            max = i
        # print(min, max)
    return (min, max)
