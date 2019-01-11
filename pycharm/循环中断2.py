#  循环中断之 continue

#   continue: 中断一次循环，但没有跳出循环语句块，下次循环正常运行
# 清洗数据
while True:
    s = input('随便输入：')

    if len(s)<3:
        print('太短了，请输入三个以上字符的内容。')
        continue

    print('你输入的内容是：{},长度是{}'.format(s,len(s)))
# 需求；: 软件需要有退出功能。循环中达到我们想要的条件时退出。节省计算机资源。
#   循环的中断

# bregk;退出循环，跳出循环语句块
# len(对象）:返回对象的长度

# while True:
#     s = input('随便输入')
#
#     if s == 'quit':  #达到这个条件时中断循环
#         break
#
#     print('长度是{}',format(len(s)))
# print('完')