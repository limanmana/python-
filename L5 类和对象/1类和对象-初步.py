


# # 1.函数封装
# n = {'q':'小明','w':70}
# t = {'q':'夏红','w':80}
#
# def y(stu):
#     print('学生:{}''\t''成绩:{}'.format(stu['q'],stu['w']))
# y(n)
# y(t)


# 2.(常用)面向对象
class Student():
    def __init__(self, z, c):
        self.z = z
        self.c = c

    def score(self):
        print('{}的性别是：{}'.format(self.z, self.c))

    def sex(self):
        print('{}的性别是：{}'.format(self.z, self.c))
# 实例化
n1 = Student('小青', '女')
n2 = Student('小王', '男')

# 调用对象方法
n1.score()
n2.sex()

""""
# 语法：类关键字 class 类名
# 驼峰命名
# 封装：高级   
# __init__:双下划线开头的方法为内置或特殊用途方法。
# self：
"""""













