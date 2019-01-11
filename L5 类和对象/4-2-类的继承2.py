# 类的继承和重写


class Animal(object):
    def __init__(self, name):
        self.name = name
    def run(self):
        print('动物在跑')


class Dog(Animal):
    def n1(self):
        print('狗会爬树')


class Cat(Animal):
    def n2(self):
        print('猫会游泳')
    def run(self):
        print('猫会灵活的跑')  # 重写，不用父类的属性



b1 = Dog('长威')
b1.run()
b1.n1()
b2 = Cat('来福')
b2.run()
b2.n2()

"""
子类个性化：只要在子类当中书写个性化属性和方法

重写：多个子类共用一个run方法，但有些子类需要个性化的run方法，就直接在子类下面重写run方法，直接覆盖父类run方法


"""

