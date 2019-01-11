# 多态
# 多态是类的三大特性之一


class A(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print('常威在打来福')

class T(A):
    def run(self):
        print('没有打')

class Y(A):
    def run(self):
        print('打了')

def b(b1):
    b1.run()

n1 = T()
n2 = Y()
b(n1)
b(n2)



