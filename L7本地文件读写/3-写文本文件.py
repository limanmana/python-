
# 写文本文件


# 回忆读取文本文件示例

file = open(file='chinese_bgk.txt', mode='r', encoding='utf-8')
content = file.read()
print(content)
file.close


# 写文件
file = open('write.txt', 'w', encoding='utf-8')
file.write('你好')
file.write('\n')
file.write('RNG')



""" bXZCV
写入文件 open函数先打开一个空文本文件。如果文件不存在，会自动新建一个文件
模式为’w‘,意为write 写。
utf-8 UTF-8 utf8 utf_8 这些写法都行。同理ascii ASCII gbk GBK都可以。



"""




