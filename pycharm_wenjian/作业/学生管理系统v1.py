# 学生管理系统



x = ['小王','小李','小红']
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
    #第一部分
    if n == 1:
        print('编号', '\t', '姓名')
        print('-----------------')
        for i in range(0, len(x)):
            print(i+1, '\t''\t', x[i])
    # 第二部分
    if n == 2:
        e = input('请输入要添加的姓名:')
        x.append(e)
        print('保存成功')
        # x.append(input('请输入要添加的姓名'))
    # 第三部分
    if n == 3:
        print('编号', '\t', '姓名')
        print('-----------------')
        for i in range(0, len(x)):
            print(i + 1, '\t''\t', x[i])
        r = int(input('请输入要修改学生的编号:'))
        t = input('请输入修改后的姓名:')
        x[r-1] = t
        print('修改完成')
    # 第四部分
    if n == 4:
        print('编号', '\t', '姓名')
        print('-----------------')
        for i in range(0, len(x)):
            print(i + 1, '\t''\t', x[i])
        y = int(input('请输入要删除学生的编号:'))
        x.pop(y-1)
        print('删除成功')
    # 第五部分
    if n == 0:
        print('程序已退出')
        break














