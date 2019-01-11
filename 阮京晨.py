#
# 1.
# def n1(z, x):
#     return z*x
# z = n1(3,3)
# print(z)
#
#
# 2.
# 圆面积
# def n1(z):
#     return 3.14*z*z
# x = n1(3)
# print(x)
#
# # 体积
# def n1(z):
#     return z**3
# x = n1(4)
# print(x)
#
# # 半径
# def n1(z):
#     return (4/3)*3.14*(z**3)
# x = n1(6)
# print(x)
#
# # 3.
# def n(p):
#     if p < 60:
#         print('F')
#     if 60 <= p < 69:
#         print('D')
#     if 70 < p < 79:
#         print('C')
#     if 80 < p < 89:
#         print('B')
#     if 90 < p < 100:
#         print('A')
# n(78)
#
# # 4.
# n = int(input('请输入年份'))
# n1 = (n % 4)
# if n1 == 0:
#     print('闰年')
# else:
#     print('不是闰年')
#
# #
# # 5.
# #第一种解法
# # n = 0
# # for i in range(1, 50):
# #     n = n+i
# #     print(n)
#
# # 第二种解法
# def f(n):
#     if n == 1:
#         return 1
#     return f(n-1)+n
# print(f(49))
#
# # 6.
#
#
# # 7.
list1 = [1, 2, 3, 2, 1, 4, 5]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)

# 8.
# list1 = [2, -1, 5, 0, 99, -1]
# for i in list1:
#     print(i)
# 9.
# class Phone():
#     def __init__(self, n1, n2, n3):
#         self.n1 = n1
#         self.n2 = n2
#         self.n3 = n3
# n = Phone('brand', 'price', 'stock')
# 10.
# y = [{'z': '001', 'x': 'vivoX9', 'c': 2798}, {'z': '002', 'x': 'mate20', 'c': 400}, {'z': '003', 'x': 'iphone', 'c': 8000}]
#
#
# def n1():
#     print('序号', '\t\t\t', '编号', '\t', '手机品牌', '\t', '手机价格')
#     print('-------------------------------')
#     for i in range(0, len(y)):
#         w = y[i]
#         v1 = w['z']
#         v2 = w['x']
#         v3 = w['c']
#         print(i + 1, '\t\t\t', v1, '\t', v2, '\t', v3)
#
#
# def n2():
#     x1 = input('请输入要添加的编号：')
#     x2 = input('请手机品牌：')
#     x3 = int(input('请输入手机价格：'))
#     x = {'z': x1, 'x': x2, 'c': x3}
#     y.append(x)
#     print('添加成功')
#
#
# def n3():
#     z1 = int(input('请输入要修改的序号：'))
#     z2 = input('请输入修改后的编号:')
#     z3 = input('请输入修改后手机品牌：')
#     z4 = int(input('请输入修改后的价格：'))
#     y[z1 - 1]['z'] = z2
#     y[z1 - 1]['x'] = z3
#     y[z1 - 1]['c'] = z4
#     print('修改成功')
#
# def main():
#     while True:
#         print('请输入要操作的编号：\n'
#               '1.查看所有手机品牌 \n'
#               '2.添加新产品 \n'
#               '3.修改原有产品信息 \n'
#               '4.退出程序 \n')
#         n = int(input('请输入序号：'))
#         if n == 1:
#             n1()
#         if n == 2:
#             n2()
#         if n == 3:
#             n3()
#         if n == 4:
#             break
# main()

















