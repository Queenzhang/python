#切片 slice
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取前n个元素
print(L[0:3])
print(L[:3])

#取后n个元素
print(L[-2:])



L = list(range(100))
#取前11-20个元素
print(L[10:20])
#取前十个元素，每2个取一个
print(L[:10:2])
#所有数，每5个取一个
print(L[::5])
#复制一个list
print(L[:])

#利用切片操作，实现一个trim()函数，去除字符串首尾的空格，
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[0:-1]
    return s
print(trim(' hello '))