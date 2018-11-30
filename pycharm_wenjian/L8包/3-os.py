# os
# os包：IOS macOS , operate 操作系统。 主要负责新建文件、改文件名、路径、操作电脑系统相关的功能。是一个内置包。os包实质调用的是windows上的编程接口
# import os
# from os import path, open
# from os import *

# 1>os.path.exists 判断是否存在文件
# print(os.path.exists('1-包引用.py'))  # True
# print(os.path.exists('text.txt'))   # False

# 2>重命名
# os.rename('aaa.txt', 'bbb.txt')

# 3> 删除文件
# os.remove('aaa.txt')

# 4>创建文件夹 make directory
# os.mkdir('aaa')

# 5>列出当前文件夹下的文件
# print(os.listdir())

# 6>切换当前文件夹 change
# os.chdir()

# 7> 获取当前py所在的文件路径
# print(os.getcwd())

# 7> 获取当前文件所在文件夹。与os.getcwd()不一样的地方，getcwd会受os.chdir()。os.path.dirname只返回当前文件的所在目录，路径分隔用的正斜杠。__file__表示文件名，自身。
# print(os.path.dirname(__file__))
# 相对路径和绝对路径(针对资源管理器路径)
# 绝对路径：从盘符根目录到每一层文件精确到文件
# 相对路径：.当前目录  ..表示父目录
# 相对3os.py而言，./1包引用.py
# 相对路径优点是比较短，整个文件夹路径变化时里面的文件路径不用修改。缺点是容易写错、没有绝对路径准确。

# 8> （常用）拼接路径,获取脚本的绝对路径
# print(os.path.join(os.getcwd(), '3-os.py'))
#
# # 9> 返回绝对路径
# print(os.path.abspath('./1包引用.py'))
# os.path.abspath(os.path.join(os.getcwd(), '3-os.py'))
#
# # 10> 判断是否路径
# print(os.path.isdir('aaa'))
from L7本地文件读写.n1 import *


