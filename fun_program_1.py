#变量可以指向函数
f = abs
f(-10)

#函数名其实就是指向函数的变量
#一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
def add(x, y, f):
    return f(x) + f(y)

x = -5
y = 6
f = abs
print(add(-5, 6, abs))


#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return x*x

r = map(f,[1,2,3,4,5,6,7,8,9])
list(r)
# [1, 4, 9, 16, 25, 36, 49, 64, 81]


#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
#效果如下：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import redece
def fn(x,y):
    return x*10+y

reduce(fn,[1,3,5,7,9])

#把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
   name=name[0].upper()+name[1:].lower()
   return name
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


#接受一个list并利用reduce()求积
from functools import reduce
def prod(L):
    def quadrature(x, y):
        return x*y
    return reduce(quadrature, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


#编写一个str2float函数，把字符串转换成浮点数
from functools import reduce
def str2float(s):
    def g(s):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
    def h(x,y):
        return 10*x + y
    def a(x,y):
        return x/10 + y
    L = s.split('.')
    q = list(map(g,L[0]))
    u = list(map(g,L[1]))
    b = u[::-1]
    return reduce(h,q) + reduce(a,b)/10

print (str2float('123.4565778'))