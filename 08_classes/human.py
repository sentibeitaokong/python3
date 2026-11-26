# -*- coding: utf-8 -*-
# ====================================================
# 教程第 6 节：Human 类
# 教程在 6.1 节建议“把这个类放在独立的文件中，比如说 human.py”，
# 因此 08_classes.py 和 inheritance.py 都会导入本模块。
# ====================================================


class Human:

    # 一个类的字段。 这个字段共享给这个类的所有实例。
    species = "H. sapiens"

    # 构造方法，当实例被初始化时被调用。注意名字前后的双下划线，这是表明这个属性
    # 或方法对 Python 有特殊意义，但是允许用户自行定义。
    # 方法(可能是对象或者属性) 类似: __init__, __str__, __repr__ etc
    # 都是特殊的方法
    # 你自己取名时不应该用这种格式
    def __init__(self, name):
        # 将参数赋值给实例的 name 字段
        self.name = name

        # 初始化属性
        self._age = 0

    # 实例方法，第一个参数总是 self，也就是这个实例对象
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    # 另一个实例方法
    def sing(self):
        return 'yo... yo... microphone check... one two... one two...'

    # 类方法，被所有此类的实例共用。
    # 第一个参数是这个类对象。
    @classmethod
    def get_species(cls):
        return cls.species

    # 静态方法。调用时没有实例或类的绑定。
    @staticmethod
    def grunt():
        return "*grunt*"

    # property 有点类似 getter
    # 它把方法 age() 转换为同名并且只读的属性
    # 通常情况下，可以不需要编写复杂的 getter 和 setter。
    @property
    def age(self):
        return self._age

    # 允许属性被修改
    @age.setter
    def age(self, age):
        self._age = age

    # 允许属性被删除
    @age.deleter
    def age(self):
        del self._age


if __name__ == '__main__':
    # 直接运行本文件时的简单演示
    h = Human("Demo")
    h.say("Hello")
    print(h.get_species())
    print(Human.grunt())
