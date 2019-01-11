import sqlite3

connect = sqlite3.connect("testsqlite.db")
cursor = connect.cursor()
cursor.execute("""
    SELECT * from employsee;

""")
n1 = cursor.fetchall()
print(n1)
cursor.execute("""
    SELECT * from employsee where sex="男";
""")
n2 = cursor.fetchall()
print(n2)   # 查询

# cursor.execute("""insert into employsee (name,sex,phone) values ("智游", "男", "123413");
# """)   # 添加

# cursor.execute("""
#     ALTER TABLE employsee ADD "智游" text null ;
# """) # 添加字段



# 假性删除，为了防止数据误删和方便找回。专门新建一个标识字段表示用户状态（正常，注销）
cursor.execute("""
    update employsee set 智游="314";
""")  # 修改

# cursor.execute("""
#     delete from employsee where name="小明";
# """) # 删除

cursor.execute("""
    select * from employsee where del_flag=0; 
""")  #假性删除

connect.commit()
connect.close()