# -*- coding: utf-8 -*-
# ====================================================
# 教程第 6.2 节：多重继承
# Bat 是第二个父类，也提供 say 方法（会被 07 文件用于演示 MRO）。
# ====================================================


# 定义另一个类
class Bat:

    species = 'Baty'

    def __init__(self, can_fly=True):
        self.fly = can_fly

    # 这个类同样有 say 的方法
    def say(self, msg):
        msg = '... ... ...'
        return msg

    # 新增一个独有的方法
    def sonar(self):
        return '))) ... ((('


if __name__ == '__main__':
    b = Bat()
    print(b.say('hello'))
    print(b.fly)
