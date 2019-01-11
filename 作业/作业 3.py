
# n = ['小明','小王','小李','小丽','小米']
# w = ['小米','小娃']
#
# def f(n):
#     if len(n) <5:
#         return None
#     else:
#         return n[:2]
# print(f(n=w))


n = ['小周','小吴','小妮','小李','小阿呆']
w = []
def f(n):
    for i in range(0,len(n)):
        if i % 2 ==1:
            print(n[i])
            w.append(n[i])
    return w
print(f(n))









