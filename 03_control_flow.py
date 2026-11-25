# -*- coding: utf-8 -*-
# ====================================================
# 3. 流程控制和迭代器
# 来源：https://learnxinyminutes.com/zh-cn/python/
# 说明：文件读写演示改用临时目录，运行结束后自动清理，
#       不会在你项目里留下 myfile.txt 之类的文件。
# ====================================================

import json
import os
import shutil
import tempfile

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
x = 0
while x < 4:
    print(x)
    x += 1  # x = x + 1 的简写


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

# 演示文件操作：使用临时目录
workdir = tempfile.mkdtemp(prefix="python_basics_")
print("本次演示使用的临时目录:", workdir)

# 先准备一个 myfile.txt，供 with 语句读取
myfile_txt = os.path.join(workdir, "myfile.txt")
with open(myfile_txt, "w", encoding="utf-8") as f:
    f.write("第一行\n第二行\n")

# 你可以使用 with 语句来代替 try/finally 对操作进行结束的操作
with open(myfile_txt, encoding="utf-8") as f:
    for line in f:
        print(line, end="")

# 写入文件
contents = {"aa": 12, "bb": 21}
myfile1 = os.path.join(workdir, "myfile1.txt")
with open(myfile1, "w+", encoding="utf-8") as file:
    file.write(str(contents))        # 写入字符串到文件

myfile2 = os.path.join(workdir, "myfile2.txt")
with open(myfile2, "w+", encoding="utf-8") as file:
    file.write(json.dumps(contents))  # 写入对象到文件

# 从文件读取字符串
with open(myfile1, "r+", encoding="utf-8") as file:
    contents = file.read()
print(contents)
# print: {"aa": 12, "bb": 21}

# 从文件读取 json 对象
with open(myfile2, "r+", encoding="utf-8") as file:
    contents = json.load(file)
print(contents)
# print: {"aa": 12, "bb": 21}

# Windows 环境调用 open() 读取文件的默认编码为 ANSI，如果需要读取 utf-8 编码的文件，
# 需要指定 encoding 参数:
# open("myfile3.txt", "r+", encoding="utf-8")

# 清理本次演示生成的临时文件
shutil.rmtree(workdir)
print("已清理临时目录")


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
