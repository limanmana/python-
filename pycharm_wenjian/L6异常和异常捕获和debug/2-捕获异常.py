# 捕获异常
# 场景：一个大型项目，业务逻辑复杂。当出现异常错误时，并不需要程序终止，希望程序的主体功能运行，收集分析错误信息。

# 捕获异常
# 示例1
def foo():
    try:
        print(1/1) # 异常
    except ZeroDivisionError:   # 异常代码
        print('不能除以0')   # 出现异常的提示
    finally:
        print('我最后执行')
    print('world')

def boo():
    print('hello')
    try:
        foo()
    except ZeroDivisionError:
        print('foo异常')

boo()
"""
(重点）捕获异常：try     except   finally
场景： 捕获数据库操作代码。

try  括住可能发生问题的语句。偷懒方法try括住程序最外层，但这样捕获后不好定位出错地方。

except 后面跟异常的类名，如果捕获到这种异常，那么就会执行语句块，执行发生异常的后的一些处理  比如提示用户信息、记录日志、业务逻辑。

finally 不管程序是否正常运行，或是出现某种异常被捕获，再或是出行异常没有被捕获，最终都会执行finally语句块的内容。

捕获异常应当适度使用，使用过度代码会比较乱，不用的话可能导致程序崩溃带来损失。
"""
# 示例2

f = open('demo.txt')
try:
    content = f.read()
    print(content)                # rty块里面的变量变成局部变量，注意外部不要引用内部局部变量
except FileNotFoundError:
    print('文件未找到，请检查文件名')
except UnicodeDecodeError:
    print('unicode解码错误')
except Exception as e:  # e = FileNotFoundError()
    print(e)
finally:
    f.close()


"""
rty块里面的变量变成局部变量，注意外部不要引用内部局部变量

如果try块中的代码可能报多种异常，那么多写几个并列的except语块。

不知道错误类的类名；可能会出现代码中定义错误之外的未知新错误。使用所有错误类的父类Exception类来捕获。

finally场景：打开文件资源，不管有没有出错，最终应该保证关闭文件。

as: 把...作为...

"""