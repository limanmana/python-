# def foo():
#     # 假设代表一些业务逻辑处理
#     print('foo')
#
#
# def boo():
#     print('boo')

# 单脚本的时候，调用方法
# foo()
# boo()
# print(__name__)

# if __name__ == '__main__':
#     foo()
#     boo()
#     print(__name__)

with open('D:/pycharm 文件/L7本地文件读写/write.txt', 'r', encoding='utf-8') as f:
    print(f.read())


