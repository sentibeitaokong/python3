# -*- coding: utf-8 -*-
# ====================================================
# 3. 流程控制和迭代器
# 来源：https://learnxinyminutes.com/zh-cn/python/
# 说明：文件读写演示改用临时目录，运行结束后自动清理，
#       不会在你项目里留下 myfile.txt 之类的文件。
# ====================================================

# 先随便定义一个变量
some_var = 5

# 这是个 if 语句。注意缩进在 Python 里是有意义的！
# 缩进要使用 4 个空格而不是 tabs。
# 这段代码会打印 "some_var is smaller than 10"
if some_var > 10:
    print("some_var is totally bigger than 10.")
elif some_var < 10:    # elif 语句是可选的
    print("some_var is smaller than 10.")
else:                  # else 也是可选的
    print("some_var is indeed 10.")

"""
用 for 循环语句遍历列表
打印:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # 你可以使用 format() 格式化字符串并插入值
    print("{} is a mammal".format(animal))

"""
"range(number)" 返回数字列表从 0 到 number 的数字
打印:
    0
    1
    2
    3
"""
for i in range(4):
    print(i)

"""
"range(lower, upper)" 会返回一个包含从 lower 到 upper 的数字迭代器
打印:
    4
    5
    6
    7
"""
for i in range(4, 8):
    print(i)

"""
"range(lower, upper, step)" 会返回一个，从 lower 到 upper、并且间隔值为 step 的迭代器。
如果 step 未传入则会使用默认值 1
打印:
    4
    6
"""
for i in range(4, 8, 2):
    print(i)

# 当对字典执行循环时，可以使用 items() 方法同时提取键及其对应的值。
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

"""
gallahad the pure
robin the brave
"""

# 同时循环两个或多个序列时，用 zip() 函数可以将其内的元素一一匹配：
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))

"""
What is your name?  It is lancelot.
What is your quest?  It is the holy grail.
What is your favorite color?  It is blue.
"""

"""
遍历列表，并且同时返回列表里的每一个元素的索引和数值。
打印:
    0 dog
    1 cat
    2 mouse
"""
animals = ["dog", "cat", "mouse"]
for i, value in enumerate(animals):
    print(i, value)

"""
while 循环直到条件不满足
打印:
    0
    1
    2
    3
"""

# 枚举
from enum import Enum
class Color(Enum):
    RED='red'
    BLUE='blue'
    GREEN='green'

# color=Color(input("Enter your choice of 'red', 'blue' or 'green': "))
# match color:
#     case Color.RED:
#         print('i see red')
#     case Color.BLUE:
#         print('i see blue')
#     case Color.GREEN:
#         print('i see green')
#     case _:
#         print('i see nothing')

singleton = 'hello'
print(len(singleton))

x = 0
while x < 4:
    print(x)
    x += 1  # x = x + 1 的简写

# break
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break

'''
4 equals 2 * 2
6 equals 2 * 3
8 equals 2 * 4
9 equals 3 * 3
'''

# continue
for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue
    print(f"Found an odd number {num}")

'''
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
'''

# pass语句不执行任何动作。语法上需要一个语句，但程序毋需执行任何动作时，可以使用该语句
# while True:
#     pass  # 无限等待键盘中断 (Ctrl+C)
#
# # 创建一个最小的类：
# class MyEmptyClass:
#     pass
#
# # pass 还可用作函数或条件语句体的占位符，让你保持在更抽象的层次进行思考
# def initlog(*args):
#     pass   # 记得实现这个！

# match 语句
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

print(http_error(400))


# 用 try/except 块处理异常状况
try:
    # 用 raise 抛出异常
    raise IndexError("This is an index error")
except IndexError as e:
    print("捕获到 IndexError:", e)
except (TypeError, NameError):
    pass    # 可以同时处理不同类的错误
else:       # else 语句是可选的，必须在所有的 except 之后
    print("All good!")   # 只有当 try 运行完没有错误的时候这句才会运行
finally:    # 在任何情况下都会执行
    print("We can clean up resources here")

# 补充：没有异常时，else 分支会执行
try:
    demo_value = 1 + 1
except Exception:
    pass
else:
    print("All good!")
finally:
    print("We can clean up resources here")

# Python 提供一个叫做可迭代 (iterable) 的基本抽象。一个可迭代对象是可以被当作序列
# 的对象。比如说上面 range 返回的对象就是可迭代的。

filled_dict = {"one": 1, "two": 2, "three": 3}
our_iterable = filled_dict.keys()
print(our_iterable)  # => dict_keys(['one', 'two', 'three'])，是一个实现可迭代接口的对象

# 可迭代对象可以遍历
for i in our_iterable:
    print(i)    # 打印 one, two, three

# 但是不可以随机访问
try:
    our_iterable[1]  # 抛出 TypeError
except TypeError as e:
    print("TypeError:", e)

# 可迭代对象知道怎么生成迭代器
our_iterator = iter(our_iterable)

# 迭代器是一个可以记住遍历的位置的对象
# 用 "next()" 获得下一个对象
print(next(our_iterator))  # => "one"

# 再一次调取 "next()" 时会记得位置
print(next(our_iterator))  # => "two"
print(next(our_iterator))  # => "three"

# 当迭代器所有元素都取出后，会抛出 StopIteration
try:
    next(our_iterator)  # 抛出 StopIteration
except StopIteration:
    print("StopIteration: 迭代器中的元素已经全部取出")

# 我们还可以通过遍历访问所有的值，实际上，for 内部实现了迭代
our_iterator = iter(our_iterable)
for i in our_iterator:
    print(i)  # 依次打印 one, two, three

# 可以用 list 一次取出迭代器或者可迭代对象所有的元素
print(list(filled_dict.keys()))  # => 返回 ["one", "two", "three"]
print(list(our_iterator))        # => 返回 [] 因为迭代的位置被保存了




