import urllib.request
from fake_useragent import UserAgent
import re
from lxml import etree
from bs4 import BeautifulSoup
# base_url = 'https://www.qiushibaike.com/hot/page/1'
# url = 'http://example.python-scraping.com/places/default/index/0'
# print(url)

# ua = UserAgent()
# headers={'User-Agent':ua.random}
#
#
# req = urllib.request.Request(url,headers=headers)
# resp = urllib.request.urlopen(req)
# html_content = resp.read().decode('utf-8')
# print(html_content)


# bs = BeautifulSoup(html_content,'lxml')
# # print(bs)
# print(bs.label.string)
# html = etree.fromstring(html_content)
# print(html)
# print(html_content.xpath('//a'))
# pattern_1 = re.compile(r'<label class=".*?">(.*?)</label>',re.S)
# n1 = re.findall(pattern_1,html_content)
# print(n1)
# # pattern_2 = re.compile(r'<td class="w2p_fw"><img src="(.*)">(.*?)</td>',re.S)
# # print(re.findall(pattern_2,html_content))
#
#
# for i in n1:
#     print(i)
for i in range(0,5):
    url = 'http://example.python-scraping.com/places/default/index/'+str(i)
    print(url)
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    html_content = resp.read().decode('utf-8')
    html = etree.HTML(html_content)
    for i in html.xpath('//a/text()'):
        print(i)
