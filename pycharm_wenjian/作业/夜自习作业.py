# 练习题 学生成绩
p = input('请输入分数:')
p = float(p)
if p<0 or p>=100:
    print('用户输入不合法')
if p < 60:
    print('不及格')
else :
    print('及格')
    if 60 <= p < 70:
        print('D')
    elif 70 <= p <80:
        print('C')
    elif 80 <= p <90:
        print('B')
    elif 90 <= p <=100:
        print('A')



































