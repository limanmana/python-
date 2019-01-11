# 数据库图形管理工具
"""
 常用数据库图形管理工具
 1.navicat系列 navicat for sqlite
 优点navicatForMysql用户多 表多的时候界面方便，缺点是付费，体验一般
 2.datagrip ,jetbrains出品，优点一软件连接过个客户端；操作习惯跟pycharm类似，缺点用户少；驱动不好下。

datageip操作方法：
1.pycharm左下角调出工具栏，打开pycharm右侧Database工具。
2.点加号-DataSource数据源-sqlite。
3.弹出对话框选择 drivers-sqilte(Xerial)w
4.点击download sqlite-jdbc[latest]
5.网速不好的话 下载sqlite-jdbc-3.20.1.jar。对话框+号-cutom jars 从本地安装
6.驱动安装成功后点击applyd
7.File路径点击...图标，选择要连接的.db文件。
8.点test connection，seccessful为成功
9.点击ok退出，看到连接的数据库实例下有表。

"""
"""
（了解）
JDBC：java操作数据库的驱动包。因为pycharm、datagrip是用java开发的。

database工具使用：
展开目录，找到 表。
schemas 模型，理解为大的仓库，默认有一个仓库main，main仓库下是我们建的表。
sqlite_masters是数据库系统内置表，不用关注它，不能删除。
不用关注collations文件夹。
双击表查看表数据。
图形化界面 加减号增加修改数据，注意修改完需要submit提交。
点击console图标，打开sql命令行工具，可以在里面写sql语句，点击execute按钮执行，得到结果集。
选中库，右键new-table，可视化界面创建表。
"""