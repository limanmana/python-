# 学生管理系统-练习
y = [{'z': '小明', 'x': 10, 'c': '男'}, {'z': '小王', 'x': 12, 'c': '女'}, {'z': '狗蛋', 'x': 18, 'c': '男'}]

def v1():
    print('序号', '\t\t', '姓名', '\t', '年龄', '\t', '性别')
    print('—————————————————')
    for i in range(0, len(y)):
        w = y[i]
        q1 = w['z']
        q2 = w['x']
        q3 = w['c']
        print(i + 1, '\t\t\t', q1, '\t', q2, '\t', q3)
def v2():
    z1 = int(input('请输入要修改的序号：'))
    z3 = int(input('年龄'))
    z2 = input('请输入修改后的姓名：')
    z4 = input('性别')
    y[z1 - 1]['z'] = z2
    y[z1 - 1]['x'] = z3
    y[z1 - 1]['c'] = z4
    print('修改成功')


def v3():
    x1 = input('请输入要添加姓名：')
    x2 = int(input('请输入年龄：'))
    x3 = input('请输入性别：')
    x = {'z': x1, 'x': x2, 'c': x3}
    y.append(x)
    print('添加成功')


def v4():
    c1 = int(input('请输入要删除的序号：'))
    y.pop(c1 - 1)
    print('删除成功')


def main():
    while True:
        print('欢迎使用学生管理系统')
        print('输入一下序号操作')
        print('1-查询\n'
              '2-修改\n'
              '3-添加\n'
              '4-删除\n'
              '0-退出')
        n = int(input('请输入序号：'))
        if n == 1:
            v1()
        if n == 2:
            v1()
            v2()
        if n == 3:
            v1()
            v3()
        if n == 4:
            v1()
            v4()
        if n == 0:
            break
main()

# n = input('s')
# y1 = ['name']
# if n == 2:
#     z1 = int(input('编号'))
#     z2 = input('姓名')
#     z3 = [z2]
#     y1.append(z3)


