# 情况2:纯静态网页获取图片
# 解决方案： requests包会接收响应的二进制的数据，取出后写入本地。
# 分析网页，比静态纯文本麻烦一点，图片往往通过src标签或a标签引入到网页，第一步先分析获取图片在网页上的url资源地址，第二步请求静态资源地址获取图片二进制信息。

import requests
from lxml import etree
import os
import time
url = 'http://www.ivsky.com/tupian/yueliang_v49822/'
# url = 'http://www.ivsky.com/tupian/'
resp = requests.get(url)

html_content = resp.text
html_dom = etree.HTML(html_content)
# print(html_content)
pattern_img_src = '//ul[@class="pli"]/li/div/a/img/@src'
img_src_list = html_dom.xpath(pattern_img_src)
# y1 = '//ul[@class="ali"]/li/div/a/@title'
# y2 = html_dom.xpath(y1)
# print(y2)

for index,img_src_url in enumerate(img_src_list):
    resp = requests.get(img_src_url, timeout=10)
    if resp.status_code !=200:
        raise Exception("图片请求失败")
    n3 = resp.content
    # print(n3)
    y1 = str(index)
    n4 =   y1 + '.jpg'
    with open('D:\\testimg\\夜空的月亮\\'+n4, 'wb') as file:
        file.write(n3)

n1 = os.path.exists('D:\\testimg\\夜空的月亮')

if n1 == False:
    os.mkdir('D:\\testimg')
    os.mkdir('D:\\testimg\\夜空的月亮')