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