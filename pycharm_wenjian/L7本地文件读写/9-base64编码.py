# base64编码
"""
 引题：读写图片、视频的时候读的是二进制。
 计算机之间交流一般用通用格式信息，比如'hello world'。比较老式的服务器由于硬件和软件的限制，只支持ascii编码，不支持特殊符号，直接传输字节信息可能会出错。


 图片（jpg） > 二进制（base64编码 > 处理后的字符串

 处理后字符串适合在网络中传播

 base64编码：一种简单的加密方法。主要作用是轻度加密和兼容老服务器。会把原信息转换成由大小写字母和常见字符组成的新字符串。

 场景：
 1.网址。网址含有中文，比如http://www.baidu.com/ ,网址复制粘贴出来后形如https://1owo.com/flask/%E6%A1%8/，这就是经过base64转码后的结果，服务器识别网址时就不会出错了。

# 2.传图片。不传字节而传通用的字符串。
# 3.简单加密。比如论坛上自曝微信号的时候发出来是经过base64编码后的内容。

"""
import base64
content = base64.b64encode('密码123345'.encode())   # 先通过base64编码
print(content)
y = base64.b64decode(content)                       # 在通过base64解码成字节
print(y)
print(y.decode())                                   # base64解码得到的字节通过utf-8解码成原始信息

# # encode 编码 （encoding = '编码类型'）
# # decode 解码 （encoding = '解码类型'）
# n = '世界'.encode(encoding='utf-8')
# print(n)
# #
# n3 =b'\xe4\xb8\x96\xe7\x95\x8c'.decode(encoding='utf-8')
# print(n3)
# import base64
# with open('im.jpg', 'rb') as f:
#     content_bytes = f.read()
#     content_b64 = base64.b64encode(content_bytes)
#     print(content_b64)