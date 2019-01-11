# mysql 驱动
# 引题：已经学习了sql语法，sqlite驱动操作sqlite数据库，我们要找python操作mysql驱动

"""
驱动选择：
1.MYSQLDB。已经有C驱动musql的成熟包，mysqldb包python对这个c驱动包封装。优点是效率高，py2环境和众多项目中使用，缺点windows下安装报错。解决方案是去mysql官网下载对应平台的connector.msi安装。
pip install mysql-python
2.（推荐）pymysql。纯python写的。缺点效率稍低。优点安装方便，完全兼容，mysqldb的语法。市场占有率越来越高
3. mysql-connector。python书写。类似mysqldb但不依赖c语言驱动

"""
import pymysql.cursors
import pymysql

connection = pymysql.connect(port=3306,host='127.0.0.1',
                             user='root',
                             password='root',   # 安全风险，未来会从环境变量读取
                             db='test',
                             charset='utf8mb4',  #可以省略，8.0客户端默认utf-8
                             cursorclass=pymysql.cursors.DictCursor)  # 返回字典结果集，不写默认返回元组格式

try:
    with connection.cursor() as cursor:
        sql = """select * from shirt;"""
        cursor.execute(sql)
        result = cursor.fetchall()
        # print(result)
        for row in result:
            print('小红有{}色的{}'.format(row[2], row[1]))

    with connection.cursor() as cursor:
        sql = """insert into shirt value (%s,%s,%s,%s)"""
        cursor.execute(sql,(None,'裤子','蓝', 3))

        # sql_insert = """insert into user(id,style,color) values(None,'蓝','帽子')"""
        # cursor.execute(sql_insert)

    connection.commit()


except Exception as e:
    connection.rollback()
    print(e)
finally:
    connection.close()





"""
(了解)sql注入攻击



"""

