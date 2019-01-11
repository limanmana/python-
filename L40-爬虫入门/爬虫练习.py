import urllib.request
from fake_useragent import UserAgent
import re




for i in range(0,15):
    url = 'http://www.jjxsw.com/read/11/30365/'+str(i)+'.html'
    print(url)
    ua = UserAgent()
    headers={'User-Agent':ua.random}
    req = urllib.request.Request(url,headers=headers)
    resp = urllib.request.urlopen(req)
    html_content = resp.read().decode('utf-8')
    print(html_content)
    n2 = re.compile(r'<div id="view_content_txt">.*?<p>(.*?)</p><p></p>', re.S)
    results_1 = re.findall(n2, html_content)
    print(results_1)
    for y in results_1:
        print(y)
        file = open('爬虫内容存储.md', 'a', encoding='utf-8')
        file.write(str(y))





