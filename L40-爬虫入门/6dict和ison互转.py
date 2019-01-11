# python字典和通用结构json互转

import json

student_List = [
    {'no':1, 'name':'小王', 'age':13},
    {'no':2, 'name':'小明', 'age':24},
    {'no':3, 'name':'下咯', 'age':63},
]

student_json = """
{
    "student_list":[
    {"no": 1, "name": "小明", "age": 13},
    {"no": 2, "name": "小红", "age": 13},
    {"no": 3, "name": "小李", "age": 13}    
    ],
    "school_name":"智游",
    "address":"经开十六大街"
}
"""

# 对象转json

stu_json = json.dumps(student_List, indent=4)
print(stu_json)

"""
json.dumps(数据对象) 返回json格式字符串。

"""



# json转对象


stu_obj = json.loads(student_json)
# print(stu_obj)
for stu in stu_obj['student_list']:
    print(f'学生姓名{stu["name"]}')

# json.dump() json.;oad() 这两个方法的参数是文件
# dumps（） loads（） 参数是变量
with open("7天气接口访问数据.json", encoding="utf-8")as file:
    weather_obj = json.load(file)
    print(weather_obj)