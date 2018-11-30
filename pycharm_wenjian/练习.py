shenggao = input('请输入身高:')
tizhong = input('请输入体重:')
shenggao = float(shenggao)
tizhong = float(tizhong)
bmi = tizhong / (shenggao/100 * shenggao/100)
print(bmi)
if bmi < 18.5:
    print('小伙子你得吃点肉啊')
elif 18.5 <= bmi <23.9:
    print('你的体重让人羡慕')
elif 23.9 <= bmi <32:
    print('姑娘你该减肥了')
elif bmi >= 32:
    print('坐着等死吧')


