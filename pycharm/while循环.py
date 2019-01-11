# while 循环
# while True:
 #   print('你好')

# while<条件>:
#    如果条件为True,那么重复运行while语句块中的内容
# 如果while循环的条件一直未True，死循环
# while True:
#     cai = 20
#     caia = int(input('请猜一个数字:'))
#     if caia<cai:
#         print('猜小了')
#     elif caia>cai:
#         print('猜大了')
#     else:
#         print('猜对了')

s=0
while s <= 10:
    print(s)
    s = s+1
#     s+=1  #简写语法