import urllib.request
import json
import urllib.parse
# http://api.map.baidu.com/place/v2/search?query=ATM机&tag=银行&region=北京&output=json&ak=您的ak //GET请求
origin_args={'query':'ATM机', 'region':'新县', 'output':'json', 'ak':'Gu7UDyhUgr0Ild0iRiLn29sMTVxWURDs'}
b64_args = urllib.parse.urlencode(origin_args)
base_url = 'http://api.map.baidu.com/place/v2/search'
url = base_url+'?'+b64_args
print(url)
resp = urllib.request.urlopen(url)
content_json = resp.read().decode()
print(resp)
print(content_json)
# json转对象
content_obj = json.loads(content_json)
print(content_obj)
results = content_obj['results']
for row in results:
    print(row['name'],row['address'])



