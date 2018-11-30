# 异常介绍
"""异常(Exception)：代码写错了，解释器无法运行。主要包括书写语法上的错误
  从轻到重：拼写检查inspertion < 普通information < 警告warning < 运行时错误runtime Erroe < 异常Exception < 严重的错误Erroe 崩溃
"""

"""
错误跟踪栈 Traceback: 错误栈展示出错信息：哪一个文件、第几行、在哪个模块下、出错的代码。根据函数的嵌套和调用执行程序，按从早到晚排序。最好是出错类型和描述。

如何排错： 看看错误栈的前面的信息，知道从哪个代码开始出错；看看后面的信息，知道哪一句代码出错了；看看最后一句错误类型和描述。

"""
# 遇到过的错误
"""
1.变量未声明就调用 print(a)   NameError: name 'a' is not defined

2.语法错误。少些冒号等。 SyntaxError: invalid syntax
3.缩进错误。  IndentationError: expected an indented block
4.索引错误。[1,2,3][4]  IndexError: list index out of range
5.类型错误。调用函数时参数的类型或个数不匹配。
6.值错误
7.零除错误。 1/0   ZeroDivisionError: division by zero
8.递归错误。




"""
print(1/0)

