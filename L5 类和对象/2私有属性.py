# 私有属性

# 1.引题
# class Student():
#     def __init__(self, z, c):
#         self.z = z
#         self.c = c
#
#     def score(self):
#         print('{}的性别是：{}'.format(self.z, self.c))
#
#     def sex(self):
#         print('{}的性别是：{}'.format(self.z, self.c))
# # 实例化
# n1 = Student('小青', '女')
# n2 = Student('小王', '男')
#
# # 调用对象的属性
# print(n1.z)
# print(n2.c)
#
# # 写属性(修改属性）
# n1.z = 100
# print(n1.z)

# 上面的例子说明类的属性可以被修改。但是这样会导致安全问题，比如可以修改成绩。类内部保密只需要暴露外部接口。外部不应该直接修改类的属性

# 2.私有变量
# class Student2():
#     def __init__(self, z, c):
#         self.__z = z
#         self.__c = c
#
# n1 = Student2('小青', '女')09-
#
# print(n1.z)

# 双下划线开头的属性不能直接访问，这样确保以一定的安全性。
# 但是有的时候我们又想获取对象的信息。
# 3.getter函数
class Student2():
    def __init__(self, z, c):
        self.__z = z
        self.__c = c
    def get_z(self):
        return self.__z

n1 = Student2('小青', '女')

print(n1.get_z())