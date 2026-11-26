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

# 要标示引号本身，我们需要对它进行“转义”，即在前面加一个 \。或者，我们也可以使用不同类型的引号:
print('doesn\'t')  # 使用 \' 来转义单引号...
print("doesn't")  # ...或者改用双引号
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')

# 如果不希望前置 \ 的字符转义成特殊字符，可以使用 原始字符串，在引号前添加 r 即可：
print('C:\this\name')  # 这里 \t 表示制表符，\n 表示换行符
print(r'C:\this\name')  # 请注意引号前的 r