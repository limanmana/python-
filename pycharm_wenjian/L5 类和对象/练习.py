

#
#
# class S():
#     name = []
#
#     def __init__(self,n):
#         self.n = n
#         S.name.append(self.n)
#         print('{}已制造'.format(n))
#     def n3(self):
#         print('我是机器人：{}'.format(self.name))
#
#
#     @classmethod
#     def n1(cls):
#         print('机器总制造数:{}'.format(len(cls.name)))
#
#
#
#
#
#
#
# n = S('智子')
# n.n1()
# s = S('智子2')
# n.n1()
# n.n3()


class S():
    n = 0

    def __init__(self,name):
        self.name = name
        S.n +=1

    def n2(self):

        print('大家好我是机器人：{}'.format(self.name))

    @classmethod
    def n3(cls):
        print('机器总数：' ,cls.n)


name = S('智子')
name1 = S('智子2')
name.n2()
name.n3()
name.n4()








