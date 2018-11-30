# open() 更多模式

"""
open()第二个参数mode模式：
'r',read 读取信息
'w',write 写信息
'rb', read byte 读取字节信息
'wb',write byte 写字节信息



"""
with open('8-write.txt', 'w', encoding='utf-8') as f:
    f.write('你好\n')
    f.write('RNG')

with open('8-write.txt', 'w', encoding='utf-8') as f:
    f.write('第二次写入信息')


"""
w 写模式 ，每一次打开文件写信息，会将之前的信息覆盖掉。所以用'a'追加到末尾
"""
with open('8-write.txt', 'a', encoding='utf-8') as f:
    f.write('\n追加信息到末尾')
    f.write('\nRNG')


