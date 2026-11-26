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

# 构造 0 个或 1 个元素的元组比较特殊：为了适应这种情况，对句法有一些额外的改变。用一对空圆括号就可以创建空元组；
# 只有一个元素的元组可以通过在这个元素后添加逗号来构建（圆括号里只有一个值的话不够明确）。丑陋，但是有效。
empty = ()
singleton = 'hello',    # <-- 注意末尾的逗号
print(len(empty))       # 0
print(len(singleton))   # 1
print(singleton)        # ('hello',)