# 枚举
# 一个一个列出来
# 场景：循环列表，既想获得索引，又想获得元素内容


#  1.普通写法

n = ['小明', '小红', '老王']
for i in range(0,len(n)):
    print(i,n[i])


# 2.枚举 enumerate
for i,y in enumerate(n):
    print(i,y)


for i, y in enumerate({'ma':'小明','wa':'带娃', 'wa ':'为'}):
    print(i,y)







