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
# 格式说明符是可选的，写在表达式后面，可以更好地控制格式化值的方式。
import math
print(f'The value of pi is approximately {math.pi:.3f}.') # The value of pi is approximately 3.142.
# 在 ':' 后传递整数，为该字段设置最小字符宽度，常用于列对齐：
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
"""
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
"""
# 还有一些修饰符可以在格式化前转换值。 '!a' 应用 ascii() ，'!s' 应用 str()，'!r' 应用 repr():
animals = 'eels'
print(f'My hovercraft is full of {animals}.') # My hovercraft is full of eels.
print(f'My hovercraft is full of {animals!r}.') # My hovercraft is full of 'eels'.
# = 说明符可被用于将一个表达式扩展为表达式文本、等号再加表达式求值结果的形式。
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}') # Debugging bugs='roaches' count=13 area='living room'

# 用 .format 来格式化字符串
print("{} can be {}".format("strings", "interpolated"))
# 可以重复参数以节省时间，按位置访问参数:
print("{0} be nimble, {0} be quick, {0} jump over the {1}".format("Jack", "candle stick"))
# => "Jack be nimble, Jack be quick, Jack jump over the candle stick"
# 按名称访问参数:
print("{name} wants to eat {food}".format(name="Bob", food="lasagna"))
# => "Bob wants to eat lasagna"

# 如果不想分拆较长的格式字符串，最好按名称引用变量进行格式化，不要按位置, 访问参数的项。
# {0[Jack]:d} => 取table第0个参数为Jack的值并且以十进制展示 => table['Jack']
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; '
      'Dcab: {0[Dcab]:d}'.format(table))   # Jack: 4098; Sjoerd: 4127; Dcab: 8637678

# 这也可以通过将 table 字典作为采用 ** 标记的关键字参数传入来实现。
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table)) # Jack: 4098; Sjoerd: 4127; Dcab: 8637678

#对齐文本以及指定宽度:
print('{:<30}'.format('left aligned')) # 左对齐 'left aligned                  '
print('{:>30}'.format('right aligned')) # 右对齐 '                 right aligned'
print('{:^30}'.format('centered'))    # 居中 '           centered           '
print('{:*^30}'.format('centered'))  # 居中填充* '***********centered***********'

# 替代 %+f, %-f 和 % f 以及指定正负号:
print('{:+f}; {:+f}'.format(3.14, -3.14))  # 总是显示 => '+3.140000; -3.140000'
print('{: f}; {: f}'.format(3.14, -3.14))  # 对正数显示一个空格 => ' 3.140000; -3.140000'
print('{:-f}; {:-f}'.format(3.14, -3.14))  # 只显示负号 -- 等同于 '{:f}; {:f}' => '3.140000; -3.140000'

# 替代 %x 和 %o 以及转换基于不同进位制的值:
# 格式也支持二进制数
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))  # => int: 42;  hex: 2a;  oct: 52;  bin: 101010
# with 0x, 0o, or 0b as prefix:
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))  # => int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010

# 使用逗号或下划线作为数字组分隔符:
# ',' 对于整数表示类型 'd' 和 'n' 以外的浮点数表示类型，每 3 个数位插入一个逗号。对于其他表示类型，此选项不受支持。
# '_' 对于整数表示类型 'd' 和 'n' 以外的浮点数表示类型，每 3 个数位插入一个下划线。
# 对于整数表示类型 'b', 'o', 'x' 和 'X'，则每 4 个数位插入一个下划线。对于其他表示类型，此选项不受支持
print('{:,}'.format(1234567890))  # => 1,234,567,890
print('{:_}'.format(1234567890))  # => 1_234_567_890
print('{:_b}'.format(1234567890))  # => 100_1001_1001_0110_0000_0010_1101_0010
print('{:_x}'.format(1234567890))  # => 4996_02d2
print('{:_}'.format(123456789.123456789))  # => 123_456_789.12345679
# print('{:.,}'.format(123456789.123456789))  # 报错: ValueError: Format specifier missing precision
# print('{:,._}'.format(123456789.123456789))  # 报错: ValueError: Format specifier missing precision
# Split the line into chunks, which are concatenated automatically by Python

# 表示为百分数:
points = 19
total = 22
print('Correct answers: {:.2%}'.format(points/total))  # => Correct answers: 86.36%

# 使用特定类型的专属格式化:
import datetime as dt
d = dt.datetime(2010, 7, 4, 12, 15, 58)
print('{:%Y-%m-%d %H:%M:%S}'.format(d))  # => 2010-07-04 12:15:58


# 几行代码将产生一组整齐的数据列，包含给定的整数及其平方与立方: Nd => N为宽度，d为十进制数字
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
"""
1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
"""
# 手动格式化字符串  str.rjust():左侧填充空格。 str.ljust()：右侧填充空格 str.center()：中间填充空格
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 请注意上一行中 'end' 的使用
    print(repr(x*x*x).rjust(4))
"""
 1   1    1
 2   4    8
 3   9   27
 4  16   64
 5  25  125
 6  36  216
 7  49  343
 8  64  512
 9  81  729
10 100 1000
"""

# str.zfill()：在数字字符串左边填充零，且能识别正负号
print('12'.zfill(5)) # '00012'
print('-3.14'.zfill(7)) # '-003.14'
print('3.14159265359'.zfill(5)) # '3.14159265359'

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