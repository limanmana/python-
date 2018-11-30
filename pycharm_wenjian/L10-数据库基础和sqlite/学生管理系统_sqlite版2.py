import sqlite3
def y():
    connect = sqlite3.connect("testsqlite.db")
    cursor = connect.cursor()
    cursor.execute("""
        create table students1
        (
            id    INTEGER
        primary key
        autoincrement,
        name  text not null,
        sex   text not null,
        age   integer default 18,
        phone text    default 1234457888
        );""")


if __name__ == '__main__':
    # y
    pass


