# beautifulsoup
# bs包包html按照节点的层级关系转换为树形文档，然后解析，简单易用
# 安装 pip install beautifulsoup4
# lxml是安全解析html标签到文档树，支持bs4和xpath
# 安装pip install lxml


from bs4 import BeautifulSoup


html = """
<html>
    <body>
        <a id="aaa" href='http://www.baidu.com' name='aaa' class="aaa">百度一下</a>
        <a href='http://www.baidu.com'>百度一下2</a>
        <h1>大家好<h1>
    </body>
</html>
"""
# 实例化bs ，传入参数待解析html内容和解析器
# html.parser python内置，方便兼容性好；lxml基于c，效率较高，需要额外安装包
bs = BeautifulSoup(html,'lxml')
# bs = BeautifulSoup(html,'html.parser')
# 格式化输出
# print(bs.prettify())

# 查找标签
# print(bs.head)   # 标签不存在返回None
# print(bs.a)    # 返回一个a标签
# print(bs.find_all('a'))  # 返回所有a标签

# (了解)标签名称
# print(bs.name)
# print(bs.a.name)


# 获取标签属性值

# print(bs.a['href'])

# (了解) 删除标签属性
# print(bs.a)
# del bs.a['id']
# print(bs.a.attrs)

# 标签内容

print(bs.a.string)
# # 子节点和父节点
print(bs.body.contents)   #返回列表标签下所有字标签
print(bs.body.children)   # 返回迭代器 子节点
for i in bs.body.children:
    print(i)

# 搜索
# print(bs.find_all('a'))
# print(bs.find_all(['a','h1']))

# 搜索 根据属性搜索
# print(bs.find(id='aaa'))

# (了解)根据class
# print(bs.find_all(class_='aaa'))
# (了解)根据css选择器语法
# print(bs.select('a'))
# print(bs.select('.aaa'))
# print(bs.select('#aaa'))
# print(bs.select('body .aaa'))