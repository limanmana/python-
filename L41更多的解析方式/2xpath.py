# xpath

# 先转文档树在解析  需要lxml包

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <title>lxml中xpath的用法</title>
</head>
<body>
    <ul>
        <li><a href="https://www.baidu.com" class="first_a">百度一下</a></li>
        <li><a href="https://mail.qq.com" id="second_a">QQ邮箱</a></li>
        <li><a href="https://www.taobao.com">淘宝网</a></li>
        <li>
            <a href="https://pypi.python.org" class="first_a">Python官网</a>
            <a href="https://pypi.python.org" class="second_a">Python</a>
        </li>
    </ul>
    <p class="one">first_p_tag</p>
    <p id="second">second_p_tag</p>
    <div class="one">
        first_div_tag
        <p class="first second third">11111111</p>
        <a href="#">22222222</a>
    </div>
</body>
</html>
"""

from lxml import etree


# etree对象 字符串互转

# 把html字符串etree对象
html = etree.HTML(html)
print(html)

#/表示从文档顶层开始匹配 /bady/ul/l1
#//表示匹配标签，目标标签前可能有多级父节点

# 搜索a标签
# etree.xpath(xpath表达式) 查找所有符合，返回列表，每一项是元素对象
print(html.xpath('//a'))  #[<Element a at 0x214ab7b05c8>]

# 提取标签属性值
# xpath表达式  //查找标签/@属性名
print(html.xpath('//a/@href'))

# 获取标签内容
# //查找标签/text()

print(html.xpath('//a/text()'))
for i in html.xpath('//a/text()'):
    print(i)

# 查找时根据属性限制标签
# 标签[@属性名=属性值]
print(html.xpath('//ul/li/a[@id="second_a"]/text()'))

# 包含条件
# conntains(@class,"class值")  适合没有id、name属性但有class属性的情况
print(html.xpath('//div[@class="one"]/p[contains(@class,"first")]/text()')[0])


# //查询下一级节点，省略中间的层级
print(html.xpath('//ul//a[@class="first_a"]'))