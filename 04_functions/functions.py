# -*- coding: utf-8 -*-
# ====================================================
# 4. 函数
# 来源：https://learnxinyminutes.com/zh-cn/python/
# 说明：所有表达式的返回值都用 print() 展示。
# ====================================================
def fibonacci(n):
    result=[]
    a,b=0,1
    if n==0:
        return 0
    while n>0:
        result.append(a)
        a,b=b,a+b
        n=n-1
    print(result)
fibonacci(3)

# 用 def 定义新函数
def add(x, y):
    print("x is {} and y is {}".format(x, y))
    return x + y    # 用 return 语句返回

# 调用函数
print(add(5, 6))  # => 打印 "x is 5 and y is 6" 并且返回 11

# 也可以用关键字参数来调用函数 默认值参数
print(add(y=6, x=5))  # 关键字参数可以用任何顺序

# 重要警告： 默认值只计算一次。默认值为列表、字典或类实例等可变对象时，会产生与该规则不同的结果。例如，下面的函数会累积后续调用时传递的参数：
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
'''
[1]
[1, 2]
[1, 2, 3]
'''
# 不想在后续调用之间共享默认值时，应以如下方式编写函数：
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

# 我们可以定义一个可变参数函数
def varargs(*args):
    return args

print(varargs(1, 2, 3))  # => (1, 2, 3)


# 我们也可以定义一个关键字可变参数函数
def keyword_args(**kwargs):
    return kwargs

# 我们来看看结果是什么：
print(keyword_args(big="foot", loch="ness"))  # => {"big": "foot", "loch": "ness"}


# 这两种可变参数可以混着用
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)

"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""
all_the_args(1, 2, a=3, b=4)

# 调用可变参数函数时可以做跟上面相反的，用 * 展开元组，用 ** 展开字典。
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)             # 相当于 all_the_args(1, 2, 3, 4)
all_the_args(**kwargs)          # 相当于 all_the_args(a=3, b=4)
all_the_args(*args, **kwargs)   # 相当于 all_the_args(1, 2, 3, 4, a=3, b=4)

# 使用返回多个数值（返回值为元组类型）
def swap(x, y):
    return y, x  # 用不带括号的元组的格式来返回多个数值
                 # (注意: 括号不需要加，但是也可以加)

x = 1
y = 2
x, y = swap(x, y)     # => x = 2, y = 1
print(x, y)
# (x, y) = swap(x, y)  # 同上，括号不需要加，但是也可以加


# 函数作用域
x = 5

def setX(num):
    # 局部作用域的 x 和全局域的 x 是不同的
    x = num       # => 43
    print(x)      # => 43

def setGlobalX(num):
    global x
    print(x)      # => 5
    x = num       # 现在全局域的 x 被赋值
    print(x)      # => 6

setX(43)
setGlobalX(6)
print(x)  # => 6


# 函数在 Python 是一等公民
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
print(add_10(3))  # => 13

# 也有匿名函数
print((lambda x: x > 2)(3))                  # => True
print((lambda x, y: x ** 2 + y ** 2)(2, 1))  # => 5

# 内置的高阶函数
print(list(map(add_10, [1, 2, 3])))          # => [11, 12, 13]
print(list(map(max, [1, 2, 3], [4, 2, 1])))  # => [4, 2, 3]

print(list(filter(lambda x: x > 5, [3, 4, 5, 6, 7])))  # => [6, 7]

# 用列表推导式可以简化映射和过滤。列表推导式的返回值是另一个列表。
print([add_10(i) for i in [1, 2, 3]])  # => [11, 12, 13]
print([x for x in [3, 4, 5, 6, 7] if x > 5])  # => [6, 7]

# 你也可以用这种方式实现对集合和字典的构建
print({x for x in 'abcddeef' if x not in 'abc'})  # => {'d', 'e', 'f'}
print({x: x**2 for x in range(5)})  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

