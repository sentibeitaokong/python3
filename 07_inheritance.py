# -*- coding: utf-8 -*-
# ====================================================
# 6.1 类的继承 / 6.2 多重继承
# 来源：https://learnxinyminutes.com/zh-cn/python/
# 说明：父类 Human 在 human.py，Superhero 在 superhero.py，Bat 在 bat.py，
#       本文件演示多重继承 Batman。
# ====================================================

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from human import Human
from superhero import Superhero
from bat import Bat


# 定义 Batman 作为子类，来同时继承 Superhero 和 Bat
class Batman(Superhero, Bat):

    def __init__(self, *args, **kwargs):
        # 通常要继承属性，你必须调用 super:
        # super(Batman, self).__init__(*args, **kwargs)
        # 然而在这里我们处理的是多重继承，而 super() 只会返回 MRO 列表的下一个基础类。
        # 因此，我们需要显式调用初始类的 __init__
        # *args 和 **kwargs 传递参数时更加清晰整洁，而对于父类而言像是 “剥了一层洋葱”
        Superhero.__init__(self, 'anonymous', movie=True,
                           superpowers=['Wealthy'], *args, **kwargs)
        Bat.__init__(self, *args, can_fly=False, **kwargs)
        # 重写了 name 字段
        self.name = 'Sad Affleck'

    def sing(self):
        return 'nan nan nan nan nan batman!'


if __name__ == '__main__':
    sup = Batman()

    # 获取方法解析顺序 MRO，MRO 被用于 getattr() 和 super()
    # 这个字段是动态的，并且可以被修改
    print(Batman.__mro__)       # => (<class '__main__.Batman'>,
                                # => <class 'superhero.Superhero'>,
                                # => <class 'human.Human'>,
                                # => <class 'bat.Bat'>, <class 'object'>)

    # 调用父类的方法并且使用子类的属性
    print(sup.get_species())    # => Superhuman

    # 调用被重写的类
    print(sup.sing())           # => nan nan nan nan nan batman!

    # 调用 Human 上的方法，(之所以是 Human 而不是 Bat)，是因为继承顺序起了作用
    sup.say('I agree')          # => Sad Affleck: I agree

    # 调用仅存在于第二个继承的父类的方法
    print(sup.sonar())          # => ))) ... (((

    # 继承类的属性
    sup.age = 100
    print(sup.age)              # => 100

    # 从第二个类上继承字段，并且其默认值被重写
    print('Can I fly? ' + str(sup.fly))  # => Can I fly? False
