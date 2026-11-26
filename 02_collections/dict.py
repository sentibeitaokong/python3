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

# 列表推导式

# dict() 构造函数可以直接用键值对序列创建字典：
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])) # {'sape': 4139, 'guido': 4127, 'jack': 4098}

# 字典推导式可以用任意键值表达式创建字典：
print({x: x**2 for x in (2, 4, 6)}) # {2: 4, 4: 16, 6: 36}

# 而字典解包 (通过 **) 则可被用来合并多个字典
odds = {i: i**2 for i in (1, 3, 5)}
evens = {i: i**2 for i in (2, 4, 6)}
print({**odds, **evens})  # {1: 1, 3: 9, 5: 25, 2: 4, 4: 16, 6: 36}

# 关键字是比较简单的字符串时，直接用关键字参数指定键值对更便捷
print(dict(sape=4139, guido=4127, jack=4098))  # {'sape': 4139, 'guido': 4127, 'jack': 4098}
