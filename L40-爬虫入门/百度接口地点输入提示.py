import urllib.request
import json
import urllib.parse

city = str(input('请输入城市:'))
key = str(input('请输入关键字:'))
pivotal = {'query':key, 'region':city, 'output':'json','ak':'Gu7UDyhUgr0Ild0iRiLn29sMTVxWURDs'}
b64_args = urllib.parse.urlencode(pivotal)
url = 'http://api.map.baidu.com/place/v2/suggestion?'+b64_args
print(url)

resp = urllib.request.urlopen(url)
decode = resp.read().decode()
print(decode)

#json转对象
n1 = json.loads(decode)
print(n1)
for i in n1['result']:
    print(i['name'], i['city'],i['district'])