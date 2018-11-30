class S():
    def __init__(self, z, c, v, b, n):
        self.z = z
        self.c = c
        self.v = v
        self.b = b
        self.n = n
    def n1(self):
        print('姓名：{}   国家：{} 人种：{} 身高cm：{} 体重kg：{}'.format(self.z, self.c, self.v, self.b, self.n))
    def n2(self):
        print('姓名：{} 国家: {} 人种：{} 身高cm：{} 体重kg：{}'.format(self.z, self.c, self.v, self.b, self.n))
    def n3(self):
        print('姓名：{}   国家：{} 人种：{} 身高cm：{} 体重kg：{}'.format(self.z, self.c, self.v, self.b, self.n))

b1 = S('鲁迅', '中国', '黄种人', 170, 60)
b2 = S('特朗普', '美国', '白种人', 150, 20)
b3 = S('棒子', '韩国', '黑种人', 140, 50)


b1.n1()
b2.n2()
b3.n3()





