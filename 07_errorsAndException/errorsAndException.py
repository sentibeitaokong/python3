# 异常处理
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

# except 子句 可能会在异常名称后面指定一个变量。这个变量将被绑定到异常实例，该实例通常会有一个存储参数的 args 属性。
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # 异常的类型
    print(inst.args)     # 参数保存在 .args 中
    print(inst)          # __str__ 允许 args 被直接打印，
                         # 但可能在异常子类中被覆盖
    x, y = inst.args     # 解包 args
    print('x =', x)
    print('y =', y)
"""
<class 'Exception'>
('spam', 'eggs')
('spam', 'eggs')
x = spam
y = eggs
"""

# BaseException 是所有异常的共同基类。它的一个子类，Exception，是所有非致命异常的基类。
try:
    f = open('workfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

# 异常处理程序不仅会处理在 try 子句 中立刻发生的异常，还会处理在 try 子句 中调用（包括间接调用）的函数。例如:
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error:', err)

# 触发异常 raise 语句支持强制触发指定的异常。
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')

# 异常链
# def func():
#     raise ConnectionError
#
# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc

# 定义清理操作
# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)
"""
result is 2.0
executing finally clause
"""
divide(2, 0)
"""
division by zero!
executing finally clause
"""
# divide("2", "1")
"""
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    divide("2", "1")
    ~~~~~~^^^^^^^^^^
  File "<stdin>", line 3, in divide
    result = x / y
             ~~^~~
TypeError: unsupported operand type(s) for /: 'str' and 'str'
"""

# 预定义的清理操作
with open("workfile.txt") as f:
    for line in f:
        print(line, end="")
    f.close()

# 引发和处理多个不相关的异常
# def f():
#     raise ExceptionGroup(
#         "group1",
#         [
#             OSError(1),
#             SystemError(2),
#             ExceptionGroup(
#                 "group2",
#                 [
#                     OSError(3),
#                     RecursionError(4)
#                 ]
#             )
#         ]
#     )
#
# try:
#     f()
# except* OSError as e:
#     print("There were OSErrors")
# except* SystemError as e:
#     print("There were SystemErrors")

"""
There were OSErrors
There were SystemErrors
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 2, in <module>
  |     f()
  |     ~^^
  |   File "<stdin>", line 2, in f
  |     raise ExceptionGroup(
  |     ...<12 lines>...
  |     )
  | ExceptionGroup: group1 (1 sub-exception)
  +-+---------------- 1 ----------------
    | ExceptionGroup: group2 (1 sub-exception)
    +-+---------------- 1 ----------------
      | RecursionError: 4
      +------------------------------------
"""

# 用注释细化异常情况
try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    e.add_note('Add some more information')
