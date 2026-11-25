# -*- coding: utf-8 -*-
# ====================================================
# 1. 原始数据类型和运算符
# 来源：https://learnxinyminutes.com/zh-cn/python/
# 说明：为了演示，表达式结果统一用 print() 输出。
# ====================================================

# 用井字符开头的是单行注释

""" 多行字符串用三个引号
    包裹，也常被用来做多
    行注释
"""

# 整数
print(3)  # => 3

# 算术没有什么出乎意料的
print(1 + 1)   # => 2
print(8 - 1)   # => 7
print(10 * 2)  # => 20

# 但是除法例外，会自动转换成浮点数
print(35 / 5)    # => 7.0
print(10.0 / 3)  # => 3.3333333333333335

# 整数除法的结果都是向下取整
print(5 // 3)       # => 1
print(5.0 // 3.0)   # => 1.0  # 浮点数也可以
print(-5 // 3)      # => -2
print(-5.0 // 3.0)  # => -2.0

# 浮点数的运算结果也是浮点数
print(3 * 2.0)  # => 6.0

# 模除
print(7 % 3)  # => 1
# i % j 结果的正负符号会和 j 相同，而不是和 i 相同
print(-7 % 3)  # => 2

# x 的 y 次方
print(2 ** 4)  # => 16

# 用括号决定优先级
print(1 + 3 * 2)    # => 7
print((1 + 3) * 2)  # => 8

# 布尔值 (注意: 首字母大写)
print(True)   # => True
print(False)  # => False

# 用 not 取非
print(not True)   # => False
print(not False)  # => True

# 逻辑运算符，注意 and 和 or 都是小写
print(True and False)  # => False
print(False or True)   # => True

# True 和 False 实质上就是数字 1 和 0
print(True + True)  # => 2
print(True * 8)     # => 8
print(False - 5)    # => -5

# 数值与 True 和 False 之间的比较运算
print(0 == False)   # => True
print(2 == True)    # => False
print(1 == True)    # => True
print(-5 != False)  # => True

# 使用布尔逻辑运算符对数字类型的值进行运算时，会把数值强制转换为布尔值进行运算
# 但计算结果会返回它们的强制转换前的值
# 注意不要把 bool(ints) 与位运算的 "按位与"、"按位或" (&, |) 混淆
print(bool(0))    # => False
print(bool(4))    # => True
print(bool(-6))   # => True
print(0 and 2)    # => 0
print(-5 or 0)    # => -5

# 用 == 判断相等
print(1 == 1)  # => True
print(2 == 1)  # => False

# 用 != 判断不等
print(1 != 1)  # => False
print(2 != 1)  # => True

# 比较大小
print(1 < 10)  # => True
print(1 > 10)  # => False
print(2 <= 2)  # => True
print(2 >= 2)  # => True

# 判断一个值是否在范围里
print(1 < 2 and 2 < 3)  # => True
print(2 < 3 and 3 < 2)  # => False
# 大小比较可以连起来！
print(1 < 2 < 3)  # => True
print(2 < 3 < 2)  # => False

# (is 对比 ==) is 判断两个变量是否引用同一个对象,
# 而 == 判断两个对象是否含有相同的值
a = [1, 2, 3, 4]  # 变量 a 是一个新的列表, [1, 2, 3, 4]
b = a             # 变量 b 赋值了变量 a 的值
print(b is a)     # => True, a 和 b 引用的是同一个对象
print(b == a)     # => True, a 和 b 的对象的值相同
b = [1, 2, 3, 4]  # 变量 b 赋值了一个新的列表, [1, 2, 3, 4]
print(b is a)     # => False, a 和 b 引用的不是同一个对象
print(b == a)     # => True, a 和 b 的对象的值相同


# 创建字符串可以使用单引号（'）或者双引号（"）
print("这是个字符串")
print('这也是个字符串')

# 字符串可以使用加号连接成新的字符串
print("Hello " + "world!")  # => "Hello world!"
# 非变量形式的字符串甚至可以在没有加号的情况下连接
print("Hello " "world!")  # => "Hello world!"

# 字符串可以被当作字符列表
print("Hello world!"[0])  # => 'H'

# 你可以获得字符串的长度
print(len("This is a string"))  # => 16

# 你可以使用 f-strings 格式化字符串（python3.6+）
name = "Reiko"
print(f"She said her name is {name}.")  # => "She said her name is Reiko"
# 你可以在大括号内几乎加入任何 python 表达式，表达式的结果会以字符串的形式返回
print(f"{name} is {len(name)} characters long.")  # => "Reiko is 5 characters long."

# 用 .format 来格式化字符串
print("{} can be {}".format("strings", "interpolated"))
# 可以重复参数以节省时间
print("{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick"))
# => "Jack be nimble, Jack be quick, Jack jump over the candle stick"
# 如果不想数参数，可以用关键字
print("{name} wants to eat {food}".format(name="Bob", food="lasagna"))
# => "Bob wants to eat lasagna"

# 如果你的 Python3 程序也要在 Python2.5 以下环境运行，也可以用老式的格式化语法
print("%s can be %s the %s way" % ("strings", "interpolated", "old"))

# None 是一个对象
print(None)  # => None

# 当与 None 进行比较时不要用 ==，要用 is。is 是用来比较两个变量是否指向同一个对象。
etc = "etc"
print(etc is None)    # => False
print(None is None)   # => True

# None，0，空字符串，空列表，空字典，空元组都算是 False
# 所有其他值都是 True
print(bool(0))    # => False
print(bool(""))   # => False
print(bool([]))   # => False
print(bool({}))   # => False
print(bool(()))   # => False
