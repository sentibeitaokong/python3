# -*- coding: utf-8 -*-
# ====================================================
# 7. 高级用法
# 来源：https://learnxinyminutes.com/zh-cn/python/
# ====================================================

# 用生成器(generators)方便地写惰性运算
def double_numbers(iterable):
    for i in iterable:
        yield i + i

# 生成器只有在需要时才计算下一个值。它们每一次循环只生成一个值，而不是把所有的
# 值全部算好。
#
# range 的返回值也是一个生成器，不然一个 1 到 900000000 的列表会花很多时间和内存。
#
# 如果你想用一个 Python 的关键字当作变量名，可以加一个下划线来区分。
range_ = range(1, 900000000)
# 当找到一个 >=30 的结果就会停
# 这意味着 `double_numbers` 不会生成大于 30 的数。
for i in double_numbers(range_):
    print(i)
    if i >= 30:
        break
# 你也可以把一个生成器推导直接转换为列表
values = (-x for x in [1, 2, 3, 4, 5])
gen_to_list = list(values)
print(gen_to_list)  # => [-1, -2, -3, -4, -5]


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
