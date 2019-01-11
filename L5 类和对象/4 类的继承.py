# 类的继承



class S():
    def __init__(self,name,age,sex,hobby):
        self.name=name
        self.age=age
        self.sex=sex
        self.hobby=hobby
    def tea(self):
        print('hello')
class A():
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def stu(self):
        print('hello')

# 继承：未使用继承前，代码如上，类与相似的类有重复的属性、方法，书写麻烦。所以Python引入了类继承机制。继承是类的三大特性之一。

class Animal(object):
    def __init__(self, name):
        self.name = name
    def run(self):
        print('动物在跑')
class Dog(Animal):
    pass
class Cat(Animal):
    pass


n1 = Dog('来福')
n1.run()
n2 = Cat('长威')
n2.run()

# Animal是‘父类’‘超类’‘基类’；Dog、Cat类就叫做‘子类’、‘衍生类’
# 继承：语法 类定义时，类名后面的小括号里填写父类名。。注意跟类实例化时、函数后面的小括号里的内容不一样。

# object: Python中变量、方法万物皆对象，现实生活中也是万物皆对象。为了面向对象体系，定义了一个默认的、抽象的顶级对象object。object是所有类的父类。每一个类都默认继承object类，具备一些关于类的基础方法.

# 子类继承父类所有的属性、方法

# 继承好处：类与类之间的关系更加清晰；代码量少；公共部分抽象出来，扩展更方便。


