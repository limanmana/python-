#  （爬虫 diango之前讲）
# 需求 给你一个网站一个页面的源代码，要求吧网址都选出来，返回列表
# 正则： re regex ，专业做字符串查找筛选。比‘’.find() 强大的多。有自己专用语法。优点：功能强大；缺点：学习门槛高。
# regex 三方包，功能比内置的re包强大
# 前缀，rew原始字符串，运行中不需要处理转义字符  print(r'nihao \n adc')

import re

# 简单 但功能有限不方便
html = r'<html><body></body></html>'
start_index = html.find('<h1>')
end_index = html.find('</h1>')
print(html[start_index:end_index+1])


# 1> 匹配固定字符串1次
key = r'javadfghjkl'
pattern1 = re.compile(r'java')
matcher1 = re.search(pattern1, key)
print(matcher1)
print(matcher1[0])

# re.compile(正则规则)  返回包含规则的匹配器对象
# re.search(匹配器对象，待查找字符串)

# 2> 任意字符串   .匹配任意字符  +修饰前面的匹配规则重复一次或多次    .+匹配一个或多个任意字符
key2 = r'<h1>dawda</h1>'
pattern2 = re.compile(r'<h1>.+</h1>')
matcher2 = re.search(pattern2, key2)
print(matcher2[0])



# 3>  匹配 点 加号 。 转义\     .匹配任意字符， +前面的字符一次或多次。
key3 = r'adadwawdakksaka,  kasll@qq.com welrrf.'
p3 = re.compile(r'.+@qq\.com')    # 判断用户输入是否是qq邮箱。   .+ 不太准确
m3 = re.search(p3, key3)
print(m3[0])


# 4> * 前面的字符出现0次或多次
key4 = r'https://www.baidu.com  http://www.douban.com'
p4 = re.compile(r'http*://')
m4 = re.search(p4,key4)
matcher4 = p4.findall(key4)
print(matcher4)

# 匹配器。findall(带匹配字符串)  返回列表

# 5> []匹配一个字符， 中括号里任意一个字符符合就算匹配到
key5 = r'seseSeSSEessesesSEESESEsesa'             # sql大小写不敏感
p5 = r'[se][SE][Se][sE][Ee]'
pattern1 = re.compile(p5)
print(pattern1.findall(key5))

# 6> 排除
key6 = r'mat cat phat pat'
p6 = re.compile(r'[^c]')
print("大",p6.findall(key6))


# 7> 如果符合条件默认匹配尽可能多的字符。 贪婪匹配
key7 = r'dadawadwa@163.com.cn'  # 需求 截取出dadawadwa@163.
p7 = re.compile(r'.+@.+\.')
print(p7.findall(key7))


# 8>  惰性匹配   +? 符合任意多字符的情况下 字符最少的
p8 = re.compile(r'.+@.+?')
print(p8.findall(key7))

# 9> 固定次数的
key9 = r'saas and  and asssassasa'
p9 = re.compile(r'sa{1,2}s')    # 表示a出现1到两次的
print(p9.findall(key9))


# 10>匹配换行后的内容  re.S
key10 = r"""helloworld
aadddklllhello
dwadad
world
aaa
"""
p10 = re.compile(r'hello.*?world',re.S)
print(p10.findall(key10))



# 11> 分组  （）
keyll = r"""hello小明worldqaa"""
pll = re.compile(r'hello(.*?)world(.*?)')
print(pll.findall(keyll))


