# 学生管理系统-函数封装版
# 使重复代码简化，易于维护
def n1():
    print('编号', '\t', '姓名')
    print('-----------------')
    for i in range(0, len(x)):
        print(i + 1, '\t''\t', x[i])
def n2():
    e = input('请输入要添加的姓名:')
    x.append(e)
    print('保存成功')
def n3():
    r = int(input('请输入要修改学生的编号:'))
    t = input('请输入修改后的姓名:')
    x[r - 1] = t
    print('修改完成')
def n4():
    y = int(input('请输入要删除学生的编号:'))
    x.pop(y - 1)
    print('删除成功')

x = ['小王','小李','小红']
def main():   # 主函数，程序入口
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
            print('系统已退出')
            break
main()





