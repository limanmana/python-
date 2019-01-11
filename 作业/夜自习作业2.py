# 出租车计费
k = input('请输入里程')
k = int(k)
pay = 0
if 0<=k <=2:
    pay=8
elif 2<k<=12:
    pay=8+10*1.2
elif 12<k:
    pay=8+10*1.2+(k-12)*1.5
print('pay')
