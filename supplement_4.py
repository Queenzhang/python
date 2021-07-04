#生成器generator：一边循环一边计算的机制,保存的是算法,不必创建完整的list，从而节省大量的空间
g = (x * x for x in range(10))
g  #<generator object <genexpr> at 0x1022ef630>

#next()函数获得generator的下一个返回值
#计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误
next(g) 

#for循环迭代，不需要关心StopIteration
for n in g:
    print(n)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        #t = (b, a + b) # t是一个tuple
        #a = t[0]
        #b = t[1]
        a, b = b, a + b  
        n = n + 1
    return 'done'

fib(6)

def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fib2(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


#杨辉三角
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
def triangles():
    L = [1]
    while True:
        yield L
        L = [L[i] + L[i + 1 ] for i in range(len(L) - 1 ) ]
        L.insert(0, 1)          #list开头添加 1
        L.append(1) 

n = 0
results = []
for t in triangles():
    results.append(t)
    n = n + 1
    if n == 10:
        break

for t in results:
    print(t)

if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')