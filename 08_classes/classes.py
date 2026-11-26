# 作用域和命名空间示例
# nonlocal：指向外层函数变量 global：指向模块级（全局）变量
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam) # After local assignment: test spam
    do_nonlocal()
    print("After nonlocal assignment:", spam) # After nonlocal assignment: nonlocal spam
    do_global()
    print("After global assignment:", spam) # After global assignment: nonlocal spam

scope_test()
print("In global scope:", spam) # In global scope: global spam

# 类
# 当一个类定义了 __init__() 方法时，类的实例化会自动为新创建的类实例唤起 __init__()。
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    def f(self):
        print('hello world')

x = Complex(3.0, -4.5)
print(x.r, x.i)  # 3.0 -4.5

# 实例对象
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)   # 16
del x.counter

#  方法对象
xf = x.f
print(xf())  # hello world

# 类和实例变量
class Dog:

    kind = 'canine'         # 类变量被所有实例所共享

    def __init__(self, name):
        self.name = name    # 实例变量为每个实例所独有

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)               # 'canine'  被所有的 Dog 实例所共享
print(e.kind)               # 'canine'  被所有的 Dog 实例所共享
print(d.name)               # 'Fido
print(e.name)               # 'Buddy'

class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []    # 为每个 Dog 实例新建一个空列表

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)       # ['roll over']
print(e.tricks)       # ['play dead']

# 如果同样的属性名称同时出现在实例和类中，则属性查找会优先选择实例:
class Warehouse:
   purpose = 'storage'
   region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)   # storage west
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)   # storage east