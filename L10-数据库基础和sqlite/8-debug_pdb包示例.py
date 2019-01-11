# pdb包示例
import pdb    # python debug包
#
# def test(arg):
#     pdb.set_trace()    # 设置跟踪
#     for i in range(arg):
#         print(i)
#     return arg


# pdb.run("test(3)")


"""
断点：debug运行某一句代码是暂时停住。一句一句向下执行太慢，只需要在可能出现问题的代码前设置断点。

1. 运行程序
2. (pdb)模式下 输入 “c”回车，程序会执行到第一个断电处。信息提示，运行到第几行，在哪个函数哪个文件下。
3. (pdb) 输入 s 回车，向下执行一句代码
4. 输入 a 回车， 查看相关变量的值。


"""
"""
为了使debug方便，pycharm提供了图形化的工具。
1.编辑器左侧行号区域，单击设置断点


"""
def test2(arg):
    for i in range(arg):
        print(i)
    return arg
test2(10)


