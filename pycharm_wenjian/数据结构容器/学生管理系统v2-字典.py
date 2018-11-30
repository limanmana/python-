# 左侧的structure可以看脚本结构,声明的变量
m = [{'id': '小明', 'x': 12, 'c': '男'}, {'z': '小红', 'x': 11, 'c': '女'}, {'z': '老王', 'x': 45, 'c': '男'}]


def n1():
    print('行号', '\t', '\t', '姓名', '\t', '年龄', '\t', '性别')
    print('----------------------------------------------------')
    for i in range(0,len(m)):
        v = m[i]
        v1 = (v['z'])
        v2 = (v['x'])
        v3 = (v['c'])
        print('{}\t\t\t{}\t\t{}\t\t{}'.format(i+1, v1, v2, v3))

def n2():
        z1 = input('请输入要添加的学生姓名:')
        z2 = input('请输入年龄:')
        z3 = input('请输入性别:')
        m1 = {'z': z1, 'x': z2, 'c': z3}
        m.append(m1)
        print('添加成功')


def n3():
    x1 = int(input('请输入要修改的学生编号:'))
    x2 = input('请输入修改后的姓名:')
    x3 = int(input('修改后的年龄是:'))
    m[x1-1]['z'] = x2
    m[x1-1]['x'] = x3
    print('修改成功')


def n4():
    print("""请输入操作子编号：
           1）按照编号删除
           2）全部删除(谨慎操作)    
    """)
    n = int(input('请操作'))
    if n == 1:
     t1 = int(input('要删除的学生编号:'))
     m.pop(t1-1)
    elif n == 2:
        n2 = input('确认全部删除！！！(y\n):')
        if n2 == 'y':
            m.clear()
            print('已全部删除')


def main():
    while True:
        print("""
        欢迎使用学生管理系统
        输入对应编号进行操作:
        1-查询学员姓名
        2-添加学员姓名
        3-修改学员姓名
        4-删除学员姓名
        0-退出程序'""")
        n = int(input('请输入编号:'))
        if n == 1:
            n1()
        if n == 2:
            n2()
        if n == 3:
            n1()
            n3()
        if n == 4:
            n1()
            n4()
        if n == 0:
            print('程序已退出')
            break


main()
















