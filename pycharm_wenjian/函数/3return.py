# 函数的返回值

def get_max(q,w,e):
    r = q
    if w > r:
        r = w
    if e > r:
        r = e
    return r
max_number=get_max(1,5,6)
print('最大值',max_number)

# 函数返回值：参数进入函数，经过业务逻辑处理，返回处理后的结果。
# 返回值以关键字return开头，可以返回数字、字符串、布尔。
