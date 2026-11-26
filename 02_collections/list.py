# 列表
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

# 内置函数 len() 也支持列表：
letters = ['a', 'b', 'c', 'd']
print(len(letters)) # 4

# 嵌套列表（创建包含其他列表的列表）
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)  # [['a', 'b', 'c'], [1, 2, 3]]

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

# 列表推导式
squares = list(map(lambda x: x**2, range(10)))
print(squares)
print([(x, y) for x in [1,2,3] for y in [3,1,4] if x != y])
print([(x, x**2) for x in range(6)])

# 嵌套列表推导式
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[row[i] for row in matrix] for i in range(4)])

# 列表和列表推导式中的解包
x = [1, 2, 3]
print([0, *x, 4, 5, 6])
y = [[1, 2, 3], [4, 5, 6], [], [7], [8, 9]]

# del语句
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)           # [1, 66.25, 333, 333, 1234.5]
del a[:]
print(a)           # []
