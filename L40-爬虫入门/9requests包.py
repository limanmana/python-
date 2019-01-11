# requests包
# urllib偏底层  参数编码，修改useragent或使用proxy时需要几行代码来进行构造


import requests


# GET请求 无参数
# response = requests.get('http://www.baidu.com')
# print(response.status_code)
# print(response.content)   # content 二进制原始参数
# print(response.text)  # 解码后的字符串


# 有参数
resp = requests.get('http://www.baidu.com', params={'kw':'游戏'})
print(resp.text)
print(resp.url)



# 添加自定义请求头信息headers
headers = {
    'User_Agent':''    # 上节课随机useragent的值填过来
}
requests.get('http://www.baidu.com',headers=headers)

# post
parmas = {'username':'张三','address':'郑州'}
requests.post('https://www.baidu.com',parmas=parmas)

# 代理
proxies = {
    'http':'http://{}:{}'.format('185.132.133.107','8571')

}

requests.get('www.baidu.com', headers=headers, proxies=proxies)


