# os模块提供了许多与操作系统交互的函数:
import os
# 返回当前工作目录
print(os.getcwd())
# os.chdir('/server/accesslogs')   # 改变当前工作目录
# os.system('mkdir today')   # 在系统 shell 中运行 mkdir 命令
print(dir(os))   # <返回由模块的所有函数组成的列表>
# print(help(os))  # <返回根据模块文档字符串创建的详细说明页面>

# glob模块提供了一个在目录中使用通配符搜索创建文件列表的函数:
import glob
print(glob.glob('*.py'))   # 当前目录下的以py结尾的文件名称

# 命令行参数 sys 模块
import sys
print(sys.argv)
# sys 模块还具有 stdin ， stdout 和 stderr 的属性。后者对于发出警告和错误消息非常有用
sys.stderr.write('Warning, log file not found starting a new one\n')

# 字符串模式匹配  re 模块为高级字符串处理提供正则表达式工具。
import re
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))  # ['foot', 'fell', 'fastest']
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))   # 'cat in the hat'
print('tea for too'.replace('too', 'two')) # 'tea for two'

# 数学  math 模块提供对用于浮点数学运算的下层 C 库函数的访问:
import math
print(math.cos(math.pi / 4)) # 0.70710678118654757
print(math.log(1024, 2)) # 10.0

# random 模块提供了进行随机选择的工具:
import random
print(random.choice(['apple', 'pear', 'banana'])) # 随机选一个
print(random.sample(range(100), 10))   # 无放回抽样
print(random.random())   # [0.0, 1.0) 区间的随机浮点数
print(random.randrange(6))    # 从 range(6) 中随机选取的整数

# statistics 模块计算数值数据的基本统计属性（均值，中位数，方差等）:
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))   #均值 1.6071428571428572
print(statistics.median(data)) #中位数 1.25
print(statistics.variance(data)) #方差 1.3720238095238095

# 互联网访问  urllib.request 用于从URL检索数据，以及 smtplib 用于发送邮件:
# from urllib.request import urlopen
# with urlopen('https://docs.python.org/3/') as response:
#     for line in response:
#         line = line.decode()
#         if 'updated' in line:
#             print(line.rstrip())         # Last updated on Nov 26, 2026 (12:22 UTC).

# import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
# """To: jcaesar@example.org
# From: soothsayer@example.org
#
# Beware the Ides of March.
# """)
# server.quit()

# 日期和时间 datetime 模块提供了以简单和复杂的方式操作日期和时间的类。
# 方便地构造和格式化日期
import datetime as dt
now = dt.date.today()
print(now)   # 今天的日期
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")) #今天格式化后的日期

# 日期支持历法运算
birthday = dt.date(1964, 7, 31)
age = now - birthday
print(age.days) #1964年7月31日距离今天的天数

# 输出的格式化 reprlib 模块提供了一个定制化版本的 repr() 函数，用于缩略显示大型或深层嵌套的容器对象:
import reprlib
print(reprlib.repr(set('supercalifragilisticexpialidocious'))) # "{'a', 'c', 'd', 'e', 'f', 'g', ...}"

# pprint 模块提供了更加复杂的打印控制，其输出的内置对象和用户自定义对象能够被解释器直接读取。
import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
    'yellow'], 'blue']]]
print(pprint.pprint(t, width=30))
"""
[[[['black', 'cyan'],
   'white',
   ['green', 'red']],
  [['magenta', 'yellow'],
   'blue']]]
"""

# textwrap 模块能够格式化文本段落，以适应给定的屏幕宽度:
import textwrap
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))
"""
The wrap() method is just like fill()
except that it returns a list of strings
instead of one big string with newlines
to separate the wrapped lines.
"""

# locale 模块处理与特定地域文化相关的数据格式。
import locale
# print(locale.setlocale(locale.LC_ALL, 'English_United States.1252'))  # 'English_United States.1252'

# 多线程 threading：Python 标准库的多线程模块, 处zipfile：处理 ZIP 压缩文件的标准库。
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infile, outfile):
        super().__init__()
        self.infile = infile
        self.outfile = outfile

    def run(self):
        # 创建 ZIP 文件，'w' 表示写入模式，ZIP_DEFLATED 表示用 zlib 压缩
        with zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED) as f:
            f.write(self.infile)
        print('Finished background zip of:', self.infile)

background = AsyncZip('mydata.txt', 'myarchive.zip')
background.start()
print('The main program continues to run in foreground.')
background.join()    # 等待后台任务结束
print('Main program waited until background was done.')

# 日志记录:logging 模块提供功能齐全且灵活的日志记录系统。
import logging
print(logging.debug('Debugging information'))
print(logging.info('Informational message'))
print(logging.warning('Warning:config file %s not found', 'server.conf'))
print(logging.error('Error occurred'))
print(logging.critical('Critical error -- shutting down'))

# 弱引用  weakref 模块提供的工具可以不必创建引用就能跟踪对象
import weakref, gc
class A:
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return str(self.value)

a = A(10)                   # 创建引用
d = weakref.WeakValueDictionary()
d['primary'] = a            # 不创建引用
d['primary']                # 如果对象仍存在则提取它 10
del a                       # 移除一个引用
gc.collect()                # 立即运行垃圾收集
# print(d['primary'])        # 条目已被自动移除
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    d['primary']                # 条目已被自动移除
  File "C:/python315/lib/weakref.py", line 46, in __getitem__
    o = self.data[key]()
KeyError: 'primary'
"""

# collections 模块提供了一种 deque 对象，它类似于列表，但从左端添加和弹出的速度较快而在中间查找的速度较慢。
from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())  # Handling task1

# 用于操作列表的工具 array 模块提供了一种 array 对象，它类似于列表，但只能存储类型一致的数据且存储密度更高。
from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))  # 26932
print(a[1:3])  # array('H', [10, 700])

# 十进制浮点算术
from decimal import *
print(round(Decimal('0.70') * Decimal('1.05'), 2))  # 0.74
print(round(.70 * 1.05, 2))   # 0.73

