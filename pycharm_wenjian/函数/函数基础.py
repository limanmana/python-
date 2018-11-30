## 需求，已知圆的半径为2cm，算这个圆的面积

# r = 2
# print(3.14 * r * r)

# ## 需求2 已知三个圆的半径分别为 1cm 3.5cm 10cm，求这个三个圆的面积。
# r1 = 1
# r2 = 3.5
# r3 = 10
# print('第一个圆面积',3.14*r1*r1)
# print('第二个圆面积',3.14*r2*r2)
# print('第三个圆面积',3,14*r3*r3)

## 上面的代码重复，工作越来越多。将重复的代码抽象出来，供多次调用，这就是函数。

# 函数 function（def)；将重复公共的代码抽象出来，多次调用。
# 封装代码,函数把业务逻辑打包起来，我们使用时直接调用，不必关心内部是如何实现的，降低项目难度。实现某一种功能。好处：减少重复代码节省代码量。模块逻辑清晰

## 语法
# 函数定义：关键字def(define) 函数名（参数）:   语句块
# 参数：输入一些运行时的信息、数值，函数根据传入的参数，参与内部的逻辑运算。
### 函数调用:函数名(参数)。


# def calculate_area(r):
#     print('圆面积',3.14*r*r)
#
# calculate_area(3)
# calculate_area(6)
# calculate_area(12)


# 函数的返回值(return)

# def get_max(q,w,e):
#     max_num = q
#     if w > max_num:
#         max_num = w
#     if e > max_num:
#         max_num = e
#
#     return max_num
#
# max_number = get_max(3, 8, 7)
# print('最大值', max_number)


# 函数返回值：参数进入函数，经过业务逻辑处理，返回处理后的结果。
# 返回值以关键字return开头，可以返回数字、字符串、布尔。
# 函数一般明确返回值。
# 函数一般明确返回值，设计上应该计算逻辑和业务逻辑分离开。建议明确返回的值。没有返回值的函数默认返回None。

# 2. 不需要返回值的函数，只是一些功能的封装
# def myday():
#     print('起床')
#     print('吃早餐')
#     print('上班')
#     print('下班')
#     print('睡觉')

# 3. 返回多个值的函数
# def get_max_min(q,w,e):
#     max_num = q
#     max_min = q
#     if w > max_num:
#         max_num = w
#     if e > max_num:
#         max_num = e
#
#     if w<max_min:
#         max_min=w
#     if e<max_min:
#         max_min=e
#
#
#     return max_num,max_min
#
# num1,num2 = get_max_min(3, 0, 9)
# print('最大值{}''最小值{}'.format(num1,num2))
# 函数可以有多个返回值，return的时候逗号隔开
# 析构赋值、解包赋值：函数返回多个值，就用多少个变量去接收，顺序一致。



### 参数

# 不需要参数的函数
def myday():
    print('起床')
    print('吃早餐')
    print('上班')
    print('下班')
    print('睡觉')


# 一个参数的函数

def calculate_area(r):
    print('圆面积',3.14*r*r)

calculate_area(3)


#  多个参数的函数

# def get_max(q,w,e):  #这是形参
#     max_num = q
#     if w > max_num:
#         max_num = w
#     if e > max_num:
#         max_num = e
#
#     return  max_num
#
#
# get_max(3, 8, 7)  #这是实参


# 参数argument:函数运行前需要告诉函数一些运行时需要的信息原料、数值，函数根据传入的参数，参与内部的逻辑运算。
# 形参： 函数定义的时候。占位、将要传进数值的“形式上的代表”。形参名可变，只需要关注形参的类型
# 实参： 函数调用的时候。传入函数的“实际具体数值”。注意实参的值要与形参的个数、类型保持一致。
# 可能出现的错误：实参和形参个数或类型不一致报错。
# (了解) 常用的内置之一。注意变量命名不要用内置关键字或函数。












