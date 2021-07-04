#列表生成式 List Comprehensions 是Python内置的非常简单却强大的可以用来创建list的生成式。

print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])  #if在for循环里不能加else
print([x if x % 2 == 0 else -x for x in range(1, 11)]) #if在前需要加else
print([m + n for m in 'ABC' for n in 'XYZ'])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + v for k, v in d.items()])