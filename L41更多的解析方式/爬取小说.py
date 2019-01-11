import urllib.request
from fake_useragent import UserAgent
import re
from lxml import etree
from bs4 import BeautifulSoup



for i in range(0,1):
    # url = 'https://qxs.la/180323/'+str(i)
    url = 'https://www.kanunu8.com/book2/10913/192787.html'
    print(url)
    ua = UserAgent()
    headers = {'User-Agent': ua.random}
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    html_content = resp.read().decode('gbk')
    html = etree.HTML(html_content)
    print(html.xpath('//br/text()'))
    # n2 = re.compile(r'<br />　　(.*?)<!--over-->', re.S)
    # results_1 = re.findall(n2, html_content)
    # print(results_1)

