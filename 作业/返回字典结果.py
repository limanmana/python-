
import sqlite3
#
# def dict_factory(cursor, row):
#     d = {}
#     for idx, col in enumerate(cursor.description):
#         d[col[0]] = row[idx]
#     return d
#
# con = sqlite3.connect("testsqlite.db")
# con.row_factory = dict_factory
# cur = con.cursor()
# cur.execute("select 1 as a")
# n1 = cur.fetchone()["a"]
# print(n1)

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

con = sqlite3.connect(":memory:") #打开在内存里的数据库
con.row_factory = dict_factory
cur = con.cursor()
cur.execute("select 1 as a")
print(cur.fetchone())