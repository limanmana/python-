import pymongo


# 连接数据库
client = pymongo.MongoClient('127.0.0.1', 27017)
print(client)
# URL连接方式: MongoClient("mongodb://$[username]:$[password]@$[hostlist]/$[database]?authSource=$[authSource]")
# 切换数据库。如果数据库不存在则新建
db = client.test
print(db.name)
# 创建collection集合（相当于mysql中table表）
db.my_collection
print(db.my_collection)
# 插入数据
db.my_collection.insert_one({"x":'小明'})
db.my_collection.insert_one({"x":120})
db.my_collection.insert_one({"x":'老万'})
db.my_collection.insert_one({"x":560})
# 查找一条数据，文档
n1 = db.my_collection.find_one()
print(n1)
# 查找一个集合中的所有数据
n2 = db.my_collection.find()
for item in n2:
    print(item)