import urllib.request
from fake_useragent import UserAgent
import re
import requests
from lxml import etree
# url = 'https://news.163.com/'
# print(url)
#
#
# ua = UserAgent()
# headers = {'User-Agent': ua.random}
# req = urllib.request.Request(url, headers=headers)
# resp = urllib.request.urlopen(req)
# html_content = resp.read().decode('utf-8')
# html = etree.HTML(html_content)
# print(html)

for i in range(0,1):
    url = 'https://news.163.com/'
    print(url)
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    html_content = resp.read().decode('gbk')
    html = etree.HTML(html_content)
    # print(html.xpath('//div/h2/a[@href="https://news.163.com/18/1224/08/E3PEUSER000189FH.html"]/text()'))
    # print(html.xpath('//div[@class="mod_top_news2" and @id="js_top_news"]/h2/a/text()'))
    # print(html.xpath('//div[@class="mod_top_news2" and @id="js_top_news"]/ul[@class="top_news_ul"]/li/a/text()'))
    # pattern_1 = re.compile(r'<li><a .*?=".*?">(.*?)</a>', re.S)
    #
    # results_1 = re.findall(pattern_1, html_content)
    # print(results_1)
    # for i in html_content.xpath('//h2/text()'):
    #     print(i)
url = 'https://news.163.com'
resp = requests.get(url)
if resp.status_code !=200:
    raise Exception('请求失败')
html_content = resp.text


n1 = '//div[@class="mod_top_news2" and @id="js_top_news"]/h2/a/text()'
n2 = '//div[@class="mod_top_ne ws2" and @id="js_top_news"]/ul[@class="top_news_ul"]/li/a/text()'

tree = etree.HTML(html_content)
new1 = tree.xpath(n1)
new2 = tree.xpath(n2)
for i in new1:
    print(i)
for i in new2:
    print(i)