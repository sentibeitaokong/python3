# 导入整个模块
import fibo
print(fibo.fib(1000))
# 导入模块的名称
print(fibo.__name__)

# 将来自某个模块的名称直接导入到导入方模块的命名空间
from fibo import fib, fib2
print(fib(500))

# 导入模块内定义的所有名称
from fibo import *
print(fib(500))

# 自定义导入模块名称
from fibo import fib as fibonacci
print(fibonacci(500))

# 包是通过使用“带点号模块名”来构造 Python 模块命名空间的一种方式

"""
sound/                          最高层级的包
      __init__.py               初始化 sound 包  需要有 __init__.py 文件才能让 Python 将包含该文件的目录当作包来处理
      formats/                  用于文件格式转换的子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  用于音效的子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  用于过滤器的子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...
"""

# 从包中导入单个模块
# import sound.effects.echo

# 加载子模块 sound.effects.echo
# from sound.effects import echo

# Import 语句的另一种变体是直接导入所需的函数或变量
# from sound.effects.echo import echofilter

# from sound.effects import * 提供包的显式索引可以控制导入包的模块名列表
# 包的 __init__.py 代码定义了列表 __all__，运行 from package import * 时，它就是被导入的模块名列表。
# __all__ = ["echo", "surround", "reverse"]   __init__.py

"""
__all__ = [
    "echo",      # 指向 'echo.py' 文件
    "surround",  # 指向 'surround.py' 文件
    "reverse",   # !!! 现在指向 'reverse' 函数 !!!
]

def reverse(msg: str):  # <-- 此名称将覆盖 'reverse.py' 子模块
    return msg[::-1]    #     针对 'from sound.effects import *' 的情况
"""

# 相对导入
"""
from . import echo
from .. import formats
from ..filters import equalizer
"""