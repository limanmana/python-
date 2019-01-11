# # (了解）类的补充内容
#
#
# # @property装饰器，语法糖
# # 1 dir() directory文件目录，列出一个类中的所有方法。
# class A(object):
#     def __init__(self, name):
#         self.name = name
#     def tun(self):
#         print('你好')
#     def __str__(self):
#         return''
# print(dir(A))
#
#
# # 双下划线开头的名字函数都有特殊用途。
# # __class__ 类自己 __ doc__  文档  __repr__
#
#
# # 2 slot
# # 由于python是动态语言，类在运行的时候可能会被攻击添加新的属性存放恶意信息，导致安全问题。 __slots__ = (属性1，属性2)确定了类中有哪些属性，配置中未列出的，在程序运行时，往类中添加属性，如果新添加的属性不在 slots 定义当中，就会报错。从而确保属性不能随意被修改，确保安全。
# class A(object):
#     __slots__ = ('name')  # 表示不可修改 修改程序会报错
#     def __init__(self, name):
#         self.name = name
#
# name1 = A(50)
# name1.name = 90
# name1.name2 = 'eval("python xx.py")' # 恶意添加的属性
# print(name1.name)
#
# # 3 多重继承
# # 一个子类具备多个父类的特征
class Animal(object):
    print('上午好')
    def __init__(self, name):
        self.name = name



class Catoon(object):
    print('下午好')
class Hellokitty(Animal, Catoon):   # 有几个父类，逗号分隔
    pass
print(Animal('小王'))


# 面试题：什么是单例模式？
# 扩展：(软件设计模式）https://www.cnblogs.com/microsoft-zyl/p/6279176.html
# 扩展：（软件设计模式）http://www.runoob.com/design-pattern/design-pattern-intro.html
