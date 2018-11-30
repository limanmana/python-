# 继承 > 重写



class S(object):
    def __init__(self, name, age, sex, s):
        self.name = name
        self.age = age
        self.sex = sex
        self.s = s
    def r(self):
        print('你好')


# 关键词 super().
class T(S):
    def __init__(self, name, age, sex, s):
        super().__init__(name, age, sex)  # 继承父类属性
        self.s = s

    def u(self):
        print('{}, {} ,{} ,{}'.format(self.name, self.age, self.sex, self.s))

n1 = S('小明', 10, '男', '工人')
print(n1.name, n1.age, n1.sex)
n1.r()

