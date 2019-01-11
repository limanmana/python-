# urllib包 ，专门处理http请求的内置包
# from urllib.request import urlopen
import urllib.request

response = urllib.request.urlopen('http://www.baidu.com')
print(response)
#
print(response.code)
html_content = response.read()    # socketIO bufferReader 模式rb，从响应体中读网页信息二进制数据出来。
print(html_content)           # 字节类型的网页信息
print(html_content.decode(encoding='utf-8'))  # 字节解码成字符串