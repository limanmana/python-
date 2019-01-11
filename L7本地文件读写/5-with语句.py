# with
# 传统写法
# file = open('english_ascii.txt', 'r')
# content = file.readlines()
# print(content)
# file.close()
# 传统写法缺点 每一次都要记得打开关闭文件，跟try except连用时结构不太清晰。

# with
# with open('write.txt', 'r', encoding='utf-8') as f:
#     # f._enter_()  文件打开的预处理
#     content = f.read()
#     print(content)
    # f._exit_() # 对象结束后的操作，例如 f.close()

"""
with: with语句要求后面的对象实现  进入方法_enter_() 退出方法_exit_()
as: 把... 当做...  跟等号相似。
场景：一项任务有固定的预处理和退出处理，把这些任务的实现代码封装到__enter__()__exit__()中， 这样在with语句块中只用写主要的业务逻辑，代码更加清晰。

"""

with open('write.txt', 'w', encoding='utf-8') as f:
    f.write('你好')
    f.write('\n')
    f.write('RNG')
    n = f.read()



