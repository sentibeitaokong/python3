# -*- coding: utf-8 -*-
# ====================================================
# 7. 高级用法
# 来源：https://learnxinyminutes.com/zh-cn/python/
# ====================================================

# 迭代器
s = 'abc'
it = iter(s)
print(it)         # 返回一个定义了 __next__() 方法的迭代器对象
print(next(it))   # a
print(next(it))   # b
print(next(it))   # c
# print(next(it))

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
"""

# 自定义类添加迭代器
class Reverse:
    """对一个序列执行反向循环的迭代器。"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)
"""
m
a
p
s
"""

# 用生成器(generators)方便地写惰性运算
def double_numbers(iterable):
    for i in iterable:
        yield i + i

# 生成器只有在需要时才计算下一个值。它们每一次循环只生成一个值，而不是把所有的值全部算好。
# range 的返回值也是一个生成器，不然一个 1 到 900000000 的列表会花很多时间和内存。
# 如果你想用一个 Python 的关键字当作变量名，可以加一个下划线来区分。
range_ = range(1, 900000000)
# 当找到一个 >=30 的结果就会停
# 这意味着 `double_numbers` 不会生成大于 30 的数。
for i in double_numbers(range_):
    print(i)
    if i >= 30:
        break

#生成器表达式
# 你也可以把一个生成器推导直接转换为列表
values = (-x for x in [1, 2, 3, 4, 5])
gen_to_list = list(values)
print(gen_to_list)  # => [-1, -2, -3, -4, -5]

print(i*i for i in range(10))                 # 平方和 285
xvec = [10, 20, 30]
yvec = [7, 5, 3]
print(sum(x*y for x,y in zip(xvec, yvec)))         # 点积 260
data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1))) # ['f', 'l', 'o', 'g']

# 装饰器(decorators)
# 这个例子中，beg 装饰 say
# beg 会先调用 say。如果返回的 say_please 为真，beg 会改变返回的字符串。
from functools import wraps


def beg(target_function):
    @wraps(target_function)
    def wrapper(*args, **kwargs):
        msg, say_please = target_function(*args, **kwargs)
        if say_please:
            return "{} {}".format(msg, "Please! I am poor :(")
        return msg

    return wrapper


@beg
def say(say_please=False):
    msg = "Can you buy me a beer?"
    return msg, say_please


print(say())                # Can you buy me a beer?
print(say(say_please=True))  # Can you buy me a beer? Please! I am poor :(
