# 参数的几种类型


# 位置参数。 一个标识符做形参。位置参数普通和常用。
# def get_max(q,w,e):  #这是形参
#     max_num = q
#     if w > max_num:
#         max_num = w
#     if e > max_num:
#         max_num = e
#
#     return  max_num


# get_max(3, 8, 7)  #这是实参
# # 默认参数。带默认值的参数。step=1
# for i in range(1,10):
#     print(i)
# def n(e,w,step=1):
#     i = e
#     while i<w:
#
#         print(i)
#         i+=step
#
# n(1,10,k)
# 上例中的step=1 就是一个默认参数。函数调用时是默认值。如果实参传值的话，传的值可以默认参数，那么这个参数的值就会覆盖参数默认值。
# 参数的顺序：默认参数必须要在位置参数之后。
# 默认值一般定义为你想要的默认信息，数字类型参数默认可以定为0，字符串参数默认值''，布尔默认值一般False。

# 键值对参数(函数调用传实参时)
def print_stu_info(name,sex,score):
    print('姓名{},性别{},分数{}'.format(name, sex, score))

print_stu_info('小明','male',90) #位置参数
# #键值对参数 (namae='小明'，sex=90)
# 当参数比较多，超过五个十个的时候，用位置参数容易混淆出错。
# 实参 键=值，这样就能准确给形参赋值
