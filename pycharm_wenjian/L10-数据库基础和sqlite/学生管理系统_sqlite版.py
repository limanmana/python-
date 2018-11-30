# 学生管理系统


import sqlite3
connect = sqlite3.connect("testsqlite.db")
cursor = connect.cursor()

# 添加


def n1():

    input_name = str(input("请输入您的姓名："))
    input_sex = str(input("请输入您的性别："))
    connect.execute("insert into students(name,sex) values(?,?)", (input_name, input_sex))
    print("添加成功")

# 查询


# 返回字典版信息
def dict_factory(cursor, row):
  d = {}
  for idx, col in enumerate(cursor.description):
    d[col[0]] = row[idx]
  return d

connect = sqlite3.connect("testsqlite.db")
connect.row_factory = dict_factory
cursor = connect.cursor()
cursor.execute("select * from students;")

m = cursor.fetchall()
def n2():
    print('行号', '\t', '\t', '姓名', '\t', '性别', '\t', '年龄', '\t', '电话')
    print('----------------------------------------------')
    for i in range(0, len(m)):
        v = m[i]
        v1 = (v['name'])
        v2 = (v['sex'])
        v4 = int(v['age'])
        v5 = (v['phone'])
        print('{}\t\t\t{}\t\t{}\t\t{}\t\t{}'.format(i+1, v1, v2, v4, v5))

# 删除


def n3():

    input_name = str(input('请输入要删除学生姓名：'))
    cursor.execute("delete from students where name="+input_name)
    print('删除成功')

# 修改
 

def n4():

    input_name1 = str(input('请输入要修改学生姓名：'))
    input_name = str(input('请输入要修改后的姓名：'))
    input_sex = str(input('请输入修改后的性别：'))
    cursor.execute("update students set name=?, sex= ? where name="+input_name1, (input_name, input_sex))
    print('修改成功')


def main():
    while True:
        print("""
        欢迎使用学生管理系统
        输入对应编号进行操作:
        1-查询学员
        2-添加学员
        3-修改学员
        4-删除学员
        0-保存并退出'""")
        n = int(input('请输入编号:'))

        if n == 1:
            n2()
        if n == 2:
            n1()
        if n == 3:
            n4()
        if n == 4:
            n3()
        if n == 0:
            connect.commit()
            connect.close()
            print('已退出')
            break


main()






