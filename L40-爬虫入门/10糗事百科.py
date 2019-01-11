#coding:utf-8
## 糗事百科热点文章爬取

# 分析： 请求 url https://www.qiushibaike.com/hot/page/1/   要抓取div class='article'下内容   urllib或requests
import urllib.request
from fake_useragent import UserAgent
import re
base_url = 'https://www.qiushibaike.com/hot/page/1'
url = 'https://book.douban.com/latest?icn=index-latestbook-all/'
print(url)

ua = UserAgent()
headers={'User-Agent':ua.random}


req = urllib.request.Request(url,headers=headers)
resp = urllib.request.urlopen(req)
html_content = resp.read().decode('utf-8')
print(html_content)

#
# pattern=re.compile(r'<div class="content">\n<span>(.*?)</span>',re.S)
# results = re.findall(pattern,html_content)
# print(results)


pattern_1 = re.compile(r'<li>.*?<div class="detail-frame">.*?<a href=".*?">(.+?)</a>',re.S)


results_1 = re.findall(pattern_1,html_content)
print(results_1)


for row in results_1:
    print(row)