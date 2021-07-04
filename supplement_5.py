#迭代器Iterable：可以直接作用于for循环的对象统称为可迭代对象
from collections.abc import Iterable
isinstance([], Iterable) #isinstance()判断一个对象是否是Iterator对象

#可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
from collections.abc import Iterator
isinstance((x for x in range(10)), Iterator)

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
isinstance(iter([]), Iterator) #把list、dict、str等Iterable变成Iterator可以使用iter()函数

#Python的for循环本质上就是通过不断调用next()函数实现的