# -*- coding: utf-8 -*-
# ====================================================
# 5. 模块
# 来源：https://learnxinyminutes.com/zh-cn/python/
# ====================================================

# 导入模块
import math
print(math.sqrt(16))  # => 4.0

# 你可以导入模块中具体的函数
from math import ceil, floor
print(ceil(3.7))   # => 4
print(floor(3.7))  # => 3

# 你可以导入模块中的所有的函数
# 警告: 此操作不推荐
from math import *
print(sqrt(25))    # => 5.0

# 你可以对模块名进行简化
import math as m
print(math.sqrt(16) == m.sqrt(16))  # => True

# Python 模块实质上是 Python 文件
# 你可以自己编写自己的模块，然后导入
# 模块的名称和文件名相同

# 你可以用 "dir()" 查看模块中定义的函数和字段
import math
print(dir(math))

# 当你的脚本文件所在的文件夹也包含了一个名为 math.py 的 Python 文件
# 这个 math.py 文件会被代替引入，而不是引入 Python 內建模块中的 math
# 出现这个情况的原因是本地文件夹的引入优先级要比 Python 內建库引入优先级要高
