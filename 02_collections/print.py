# print 是内置的打印函数
print("I'm Python. Nice to meet you!")

# print() 函数会略去标示用的引号，并打印经过转义的特殊字符，产生更为易读的输出:
s = 'First line.\nSecond line.'  # \n 表示换行符
s  # 不用 print()，特殊字符将包括在字符串中 'First line.\nSecond line.'
print(s)  # 用 print()，特殊字符会被转写，因此 \n 将产生一个新行
'''
    First line.
    Second line.
'''

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