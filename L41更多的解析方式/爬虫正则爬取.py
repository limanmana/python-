import urllib.request
from fake_useragent import UserAgent
import re
from lxml import etree
for i in range(0,5):
    url = 'http://example.python-scraping.com/places/default/index/'+str(i)
    print(url)
    ua = UserAgent()
    headers={'User-Agent':ua.random}
    req = urllib.request.Request(url,headers=headers)
    resp = urllib.request.urlopen(req)
    html_content = resp.read().decode('utf-8')
    print(html_content)
    n2 = re.compile(r'<img src=".*?" />(.*?)</a>', re.S)
    results_1 = re.findall(n2, html_content)
    print(results_1)
    for i in results_1:
        print(i)
        file = open('爬虫内容存储.md', 'a', encoding='utf-8')
        file.write(str(i))