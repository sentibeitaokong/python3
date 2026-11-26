# 类的继承
# 指定父类作为类初始化的参数
class Human:

    # 一个类的字段。 这个字段共享给这个类的所有实例。
    species = "H. sapiens"

    # 构造方法，当实例被初始化时被调用。注意名字前后的双下划线，这是表明这个属性
    # 或方法对 Python 有特殊意义，但是允许用户自行定义。
    # 方法(可能是对象或者属性) 类似: __init__, __str__,__repr__ etc
    # 都是特殊的方法
    # 你自己取名时不应该用这种格式
    def __init__(self, name):
        # 将参数赋值给实例的 name 字段
        self.name = name

        # 初始化属性
        self._age = 0

    # 实例方法，第一个参数总是self，也就是这个实例对象
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

# 当 Python 解释器在读取源文件的时候，就会执行文件中所有的代码
# 对 __name__ 的检查可以保证这块代码只会在这个模块是主程序的情况下被运行（而不是在引用时运行）
if __name__ == '__main__':
    #
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

class Superhero(Human):
    # 如果子类需要继承所有父类的定义，并且不需要做任何的修改，
    # 你可以直接使用 "pass" 关键字（并且不需要其他任何语句）
    # 但是在这个例子中会被注释掉，以用来生成不一样的子类。
    # pass

    # 子类可以重写父类定义的字段
    species = 'Superhuman'

    # 子类会自动的继承父类的构造函数包括它的参数，但同时，子类也可以新增额外的参数或者定义，
    # 甚至去覆盖父类的方法比如说构造函数。
    # 这个构造函数从父类 "Human" 上继承了 "name" 参数，同时又新增了 "superpower" 和
    # "movie" 参数:
    def __init__(self, name, movie=False,
                 superpowers=["super strength", "bulletproofing"]):
        # 新增额外类的参数
        self.fictional = True
        self.movie = movie
        # 注意可变的默认值，因为默认值是共享的
        self.superpowers = superpowers

        # "super" 函数让你可以访问父类中被子类重写的方法
        # 在这个例子中，被重写的是 __init__ 方法
        # 这个语句是用来运行父类的构造函数:
        super().__init__(name)

    # 重写父类中的 sing 方法
    def sing(self):
        return 'Dun, dun, DUN!'

    # 新增一个额外的方法
    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {pow}!".format(pow=power))


if __name__ == '__main__':
    sup = Superhero(name="Tick")

    # 检查实例类型
    if isinstance(sup, Human):
        print('I am human')
    if type(sup) is Superhero:
        print('I am a superhero')

    # 获取方法解析顺序 MRO，MRO 被用于 getattr() 和 super()
    # 这个字段是动态的，并且可以被修改
    print(Superhero.__mro__)  # => (<class '__main__.Superhero'>,
    # => <class 'human.Human'>, <class 'object'>)

    # 调用父类的方法并且使用子类的属性
    print(sup.get_species())  # => Superhuman

    # 调用被重写的方法
    print(sup.sing())  # => Dun, dun, DUN!

    # 调用 Human 的方法
    sup.say('Spoon')  # => Tick: Spoon

    # 调用 Superhero 独有的方法
    sup.boast()  # => I wield the power of super strength!
    # => I wield the power of bulletproofing!

    # 继承类的字段
    sup.age = 31
    print(sup.age)  # => 31

    # Superhero 独有的字段
    print('Am I Oscar eligible? ' + str(sup.movie))

# 多重继承
from bat import Bat

# 定义 Batman 作为子类，来同时继承 SuperHero 和 Bat
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
    print('Can I fly? ' + str(sup.fly)) # => Can I fly? False

# 私有变量
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # 原始 update() 方法的私有副本

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # 为 update() 提供了新的签名
        # 但不会破坏 __init__()
        for item in zip(keys, values):
            self.items_list.append(item)