# -*- coding: utf-8 -*-
# ====================================================
# 6. 类
# 来源：https://learnxinyminutes.com/zh-cn/python/
# 说明：Human 类的完整定义（含注释）在 human.py 中，
#       本文件导入它并演示类的实例化、类方法、静态方法和 property。
# ====================================================

import os
import sys

# 让本文件无论从哪里运行，都能找到同目录下的 human.py
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from human import Human

# 当 Python 解释器在读取源文件的时候，就会执行文件中所有的代码
# 对 __name__ 的检查可以保证这块代码只会在这个模块是主程序的情况下被运行（而不是在引用时运行）
if __name__ == '__main__':
    i = Human(name="Ian")
    i.say("hi")                     # "Ian: hi"
    j = Human("Joel")
    j.say("hello")                  # "Joel: hello"
    # i 和 j 都是 Human 实例化后的对象，换一句话说，它们都是 Human 实例

    # 运行类方法 (classmethod)
    i.say(i.get_species())          # "Ian: H. sapiens"
    # 修改共享的类属性
    Human.species = "H. neanderthalensis"
    i.say(i.get_species())          # => "Ian: H. neanderthalensis"
    j.say(j.get_species())          # => "Joel: H. neanderthalensis"

    # 运行静态方法 (staticmethod)
    print(Human.grunt())            # => "*grunt*"

    # 实例上也可以执行静态方法
    print(i.grunt())                # => "*grunt*"

    # 更新实例的属性
    i.age = 42
    # 访问实例的属性
    i.say(i.age)                    # => "Ian: 42"
    j.say(j.age)                    # => "Joel: 0"
    # 删除实例的属性
    del i.age
    # i.age                         # => 这会抛出一个错误: AttributeError
