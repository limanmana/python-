



def y(n):
    return n * n
print(y(3))


# 关键字 lambda，与上面def定义的函数功能一致。
# lambda后面跟的是返参数 相当于普通写法的形参，冒号后面跟的是返回值，相当于普通写法return后面的表达式。
# 好处 ，可以写成单行，更加简洁，与其他表达式连用。

f = lambda x:x*x  # 没有名字的函数，我想调用它，先把它赋值给一个变量。
print(f(3))

# 场景适合不太复杂的函数和其他表达式连用。


## map(方法，可迭代列表)方法
def y(n):
    return n * n
for i in map(y,[1,2,3]):
    print(i)


#








