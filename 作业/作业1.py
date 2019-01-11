# 第一题
# for n in [1,2,3,4]:
#     print('****')


# 第4题
# e = 0
# for n in range(10,21):
#     e = e + n
#     print(e)


# 第五题
# e = 1
# for n in range(1,11):
#     e = e*n
#     print(e)


# 第二题
# for n in range(1,11):
#     for y in range(1,n+1):
#         print('*',end='')
#     print()


# 第三题
# for n in range(1,10):
#     for b in range(1,n+1):
#         print(b, end='')
#     print()
#

# 第八题 回文数
# total=0
# for n in range(10000,99999+1):
#     b5 = n // 10000
#     b4 = (n - b5*10000)//1000
#     b3 = (n - b5*10000 - b4*1000)//100
#     b2 = (n - b5*10000 - b4*1000 - b3*100)//10
#     b1 = (n - b5*10000 - b4*1000 - b3*100 - b2*10)
#     if b5 ==b1 and b2 ==b4:
#         total += 1
#         print(n)
# print(total)


# # 第九题 水仙数
# for n in range(100,999+1):
#     b3 = n//100
#     b2 = (n - b3*100)//10
#     b1 = (n - b3*100 - b2*10)
#     if b3**3+b2**3+b1**3 == n:
#         print(n)

# 第六题
# b=0
# for n in range(1,1000,2):
#     b = b+n
#     print(b)

# # 第七题
# e = 0
# n = 11
# for b in range(1,n+1):
#     if n % b == 0:
#         e = e+1
# if e == 2:
#     print('质数{}'.format(n))
# elif e > 2:
#     print(n,'合数')


# 判断用户输入的字母，数字，空格，其他，各有多少个
# zimu = 0
# shuzi = 0
# kongge = 0
# qita = 0
# n = input('请随意输入')
#
# for i in n:
#     if i.isalpha():
#         zimu+=1
#     elif i.isdigit():
#         shuzi+=1
#     elif i.isspace():
#         kongge+=1
#     else:
#         qita+=1
# print('字母{}，数字{}，空格{}，其他{}'.format(zimu,shuzi,kongge,qita))



# 已知三个数比大小
# q = int(input('请输入第一个数'))
# w = int(input('请输入第二个数'))
# e = int(input('请输入 第三个数'))
#
# r = q
# if w>r:
#     r=w
# if e>r:
#     r=e
# print('最大值', r)







    # print(n)

# if w < q > e:
#     print('第一最大')
# elif q < w > e:
#     print('第二最大')
# elif w < e > q:
#     print('第三最大')


# 输出一定长度的斐波那些数列（1、1、2、3、5、8...）,第一和第二个数字是(1,1)后面的每个数字都是前面两个数字之和。
print('1、','1、',end='')
a = 1
b = 1
for i in range(3,10):
    c = a + b
    a = b
    b = c
    print(c, '、', end='')



















































