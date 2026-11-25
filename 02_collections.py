# -*- coding: utf-8 -*-
# ====================================================
# 2. 变量和集合
# 来源：https://learnxinyminutes.com/zh-cn/python/
# 说明：
#   - 表达式结果用 print() 输出；
#   - 原教程中会抛异常的语句用 try/except 包住，避免演示中断；
#   - input() 演示改为固定值，避免运行到一半等待键盘输入。
# ====================================================

# print 是内置的打印函数
print("I'm Python. Nice to meet you!")

# 默认情况下，print 函数会在输出结果后加入一个空行作为结尾
# 可以使用附加参数改变输出结尾
print("Hello, World", end="!")  # => Hello, World!
print()  # 补一个换行，方便阅读

# 可以很简单的从终端获得输入数据
# input_string_var = input("Enter some data: ")  # 返回字符串数值
# 为了演示不阻塞，这里直接给一个固定值：
input_string_var = "some data"
print(input_string_var)

# 在给变量赋值前不用提前声明
# 习惯上变量命名是小写，用下划线分隔单词
some_var = 5
print(some_var)  # => 5

# 访问未赋值的变量会抛出异常
# 参考流程控制一段来学习异常处理
try:
    some_unknown_var  # 抛出 NameError
except NameError as e:
    print("NameError:", e)

# "if" 可以用作表达式，它的作用等同于 C 语言的三元运算符 "?:"
print("yay!" if 0 > 1 else "nay!")  # => "nay!"

# 用列表 (list) 储存序列
li = []
# 创建列表时也可以同时赋给元素
other_li = [4, 5, 6]

# 用 append 在列表最后追加元素
li.append(1)    # li 现在是 [1]
li.append(2)    # li 现在是 [1, 2]
li.append(4)    # li 现在是 [1, 2, 4]
li.append(3)    # li 现在是 [1, 2, 4, 3]
print(li)
# 用 pop 从列表尾部删除
print(li.pop())  # => 3 且 li 现在是 [1, 2, 4]
print(li)
# 把 3 再放回去
li.append(3)     # li 变回 [1, 2, 4, 3]
print(li)

# 列表存取跟数组一样
print(li[0])   # => 1
# 取出最后一个元素
print(li[-1])  # => 3

# 越界存取会造成 IndexError
try:
    li[4]  # 抛出 IndexError
except IndexError as e:
    print("IndexError:", e)

# 列表有切割语法
print(li[1:3])    # => [2, 4]
# 取尾
print(li[2:])     # => [4, 3]
# 取头
print(li[:3])     # => [1, 2, 4]
# 隔一个取一个
print(li[::2])    # => [1, 4]
# 倒排列表
print(li[::-1])   # => [3, 4, 2, 1]
# 可以用三个参数的任何组合来构建切割
# li[始:终:步伐]

# 简单的实现了单层数组的深度复制
li2 = li[:]  # => li2 = [1, 2, 4, 3] ，但 (li2 is li) 会返回 False
print(li2)
print(li2 is li)  # => False

# 用 del 删除任何一个元素
del li[2]     # li 现在为 [1, 2, 3]
print(li)

# 删除第一个匹配的元素
li.remove(2)  # li 现在为 [1, 3]
print(li)
try:
    li.remove(2)  # 抛出错误 ValueError: 2 is not in the list
except ValueError as e:
    print("ValueError:", e)

# 在指定索引处插入一个新的元素
li.insert(1, 2)  # li 现在是 [1, 2, 3]
print(li)

# 获得列表第一个匹配的值的索引
print(li.index(2))  # => 1
try:
    print(li.index(4))  # 抛出一个 ValueError: 4 is not in the list
except ValueError as e:
    print("ValueError:", e)

# 列表可以相加
# 注意：li 和 other_li 的值都不变
print(li + other_li)  # => [1, 2, 3, 4, 5, 6]

# 用 "extend()" 拼接列表
li.extend(other_li)   # li 现在是 [1, 2, 3, 4, 5, 6]
print(li)

# 用 "in" 测试列表是否包含值
print(1 in li)  # => True

# 用 "len()" 取列表长度
print(len(li))  # => 6


# 元组类似列表，但是不允许修改
tup = (1, 2, 3)
print(tup[0])  # => 1
try:
    tup[0] = 3  # 抛出 TypeError
except TypeError as e:
    print("TypeError:", e)

# 如果元素数量为 1 的元组必须在元素之后加一个逗号
# 其他元素数量的元组，包括空元组，都不需要
print(type((1)))    # => <class 'int'>
print(type((1,)))   # => <class 'tuple'>
print(type(()))     # => <class 'tuple'>

# 列表允许的操作元组大多都可以
print(len(tup))         # => 3
print(tup + (4, 5, 6))  # => (1, 2, 3, 4, 5, 6)
print(tup[:2])          # => (1, 2)
print(2 in tup)         # => True

# 可以把元组合列表解包，赋值给变量
a, b, c = (1, 2, 3)     # 现在 a 是 1，b 是 2，c 是 3
print(a, b, c)
# 也可以做扩展解包
a, *b, c = (1, 2, 3, 4)  # 现在 a 是 1, b 是 [2, 3]， c 是 4
print(a, b, c)
# 元组周围的括号是可以省略的
d, e, f = 4, 5, 6  # 元组 4, 5, 6 通过解包被赋值给变量 d, e, f
print(d, e, f)
# 交换两个变量的值就这么简单
e, d = d, e     # 现在 d 是 5，e 是 4
print(d, e)


# 字典用来存储 key 到 value 的映射关系
empty_dict = {}
# 初始化的字典
filled_dict = {"one": 1, "two": 2, "three": 3}
print(empty_dict)
print(filled_dict)

# 字典的 key 必须为不可变类型。 这是为了确保 key 被转换为唯一的哈希值以用于快速查询
# 不可变类型包括整数、浮点、字符串、元组
try:
    invalid_dict = {[1, 2, 3]: "123"}  # => 抛出 TypeError: unhashable type: 'list'
except TypeError as e:
    print("TypeError:", e)
valid_dict = {(1, 2, 3): [1, 2, 3]}   # 然而 value 可以是任何类型
print(valid_dict)

# 用 [] 取值
print(filled_dict["one"])  # => 1

# 用 keys 获得所有的键。
# 因为 keys 返回一个可迭代对象，所以我们需要把它包在 "list()" 里才能转换为列表。
# 我们下面会详细介绍可迭代。
# 注意: 对于版本 < 3.7 的 python, 字典的 key 的排序是无序的。你的运行结果
# 可能与下面的例子不符，但是在 3.7 版本，字典中的项会按照他们被插入到字典的顺序进行排序
print(list(filled_dict.keys()))  # => ["one", "two", "three"]（Python 3.7+）

# 用 "values()" 获得所有的值。跟 keys 一样也是可迭代对象，要使用 "list()" 才能转换为列表。
print(list(filled_dict.values()))  # => [1, 2, 3]（Python 3.7+）

# 用 in 测试一个字典是否包含一个键
print("one" in filled_dict)  # => True
print(1 in filled_dict)      # => False

# 访问不存在的键会导致 KeyError
try:
    filled_dict["four"]  # KeyError
except KeyError as e:
    print("KeyError:", e)

# 用 "get()" 来避免 KeyError
print(filled_dict.get("one"))      # => 1
print(filled_dict.get("four"))     # => None
# 当键不存在的时候 "get()" 方法可以返回默认值
print(filled_dict.get("one", 4))   # => 1
print(filled_dict.get("four", 4))  # => 4

# "setdefault()" 方法只有当键不存在的时候插入新值
print(filled_dict.setdefault("five", 5))  # filled_dict["five"] 设为 5，返回 5
print(filled_dict.setdefault("five", 6))  # filled_dict["five"] 还是 5
print(filled_dict)

# 字典赋值
filled_dict.update({"four": 4})   # => {"one": 1, "two": 2, "three": 3, "five": 5, "four": 4}
print(filled_dict)
filled_dict["four"] = 4           # 另一种赋值方法
print(filled_dict)

# 用 del 删除项
del filled_dict["one"]  # 从 filled_dict 中把 one 删除
print(filled_dict)


# 用 set 表达集合
empty_set = set()
# 初始化一个集合，语法跟字典相似。
some_set = {1, 1, 2, 2, 3, 4}   # some_set 现在是 {1, 2, 3, 4}
print(empty_set)
print(some_set)

# 类似字典的 keys，set 的元素也必须是不可变类型
try:
    invalid_set = {[1], 1}  # => Raises a TypeError: unhashable type: 'list'
except TypeError as e:
    print("TypeError:", e)
valid_set = {(1,), 1}
print(valid_set)

# 可以把集合赋值于变量
filled_set = some_set
print(filled_set)

# 为集合添加元素
filled_set.add(5)   # filled_set 现在是 {1, 2, 3, 4, 5}
print(filled_set)
# set 没有重复的元素
filled_set.add(5)   # filled_set 依然是 {1, 2, 3, 4, 5}
print(filled_set)

# "&" 取交集
other_set = {3, 4, 5, 6}
print(filled_set & other_set)   # => {3, 4, 5}

# "|" 取并集
print(filled_set | other_set)   # => {1, 2, 3, 4, 5, 6}

# "-" 取补集
print({1, 2, 3, 4} - {2, 3, 5})   # => {1, 4}

# "^" 取异或集（对称差）
print({1, 2, 3, 4} ^ {2, 3, 5})  # => {1, 4, 5}

# 判断左边的集合是否是右边集合的超集
print({1, 2} >= {1, 2, 3})  # => False

# 判断左边的集合是否是右边集合的子集
print({1, 2} <= {1, 2, 3})  # => True

# in 测试集合是否包含元素
print(2 in filled_set)   # => True
print(10 in filled_set)  # => False

# 单层集合的深度复制
filled_set = some_set.copy()  # filled_set 是 {1, 2, 3, 4, 5}
print(filled_set)
print(filled_set is some_set)  # => False
