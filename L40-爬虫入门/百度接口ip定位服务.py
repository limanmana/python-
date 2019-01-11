import socket
import urllib.request
import json
import urllib.parse
# 获取本机计算机名称
hostname = socket.gethostname()
# 获取本机ip
ip = socket.gethostbyname(hostname)
print(ip)
pivotal = {'ak':'Gu7UDyhUgr0Ild0iRiLn29sMTVxWURDs'}
b64_args = urllib.parse.urlencode(pivotal)
url = 'http://api.map.baidu.com/location/ip?'+ip+'&'+b64_args
print(url)
resp = urllib.request.urlopen(url)
decode = resp.read().decode()
print(decode)

n1 = json.loads(decode)
print(n1)

site = n1['content']
site_1 = site['address']
print('地址:',site_1)
