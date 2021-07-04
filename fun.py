def add_end(L=None): #默认参数必须指向不变对象！
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end())


#可变参数,接收的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum

print(calc())


#关键字参数,接收的是一个dict
def person(name, age, **kw):
    print ('name:',name, 'age',age,'other',kw)

extra = {'city':'Beijing','job':'Engineer'}
person('Michael',30, **extra)
#  **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。


#汉诺塔
#从左到右有A、B、C三根柱子，其中A柱子上面有从小叠到大的n个圆盘，现要求将A柱子上的圆盘移到C柱子上去，期间只有一个原则：一次只能移到一个盘子且大盘子不能在小盘子上面，求移动的步骤和移动的次数
#实现这个算法可以简单分为三个步骤：
#（1）     把n-1个盘子由A 移到 B；
#（2）     把第n个盘子由 A移到 C；
#（3）     把n-1个盘子由B 移到 C；
def hanoi(n,a,b,c):
    if n==1:
        print(a,'-->',c)
    else:
        hanoi(n-1,a,c,b)
        print(a,'-->',c)
        hanoi(n-1,b,a,c)
hanoi(3, 'A', 'B', 'C')